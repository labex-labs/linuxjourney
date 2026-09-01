---
lesson_id: "process-creation"
course_id: "processes"
lang: "ja"
order_index: 4
title: "プロセス生成"
description: "fork、exec、PID、親子関係が Linux のプロセス生成にどう関わるか学びます。"
meta_title: "プロセス生成 - プロセス"
meta_description: "Linux におけるプロセス生成の基本を探ります。このガイドでは、fork と execve システムコール、親/子関係（PID と PPID）、init プロセスの役割について解説します。Linux でプロセスを作成する方法を学び、オペレーティングシステムにおけるプロセス生成の核となる概念を理解しましょう。"
meta_keywords: "linux プロセス生成，linux プロセス作成，linux プロセス作成方法，オペレーティングシステム プロセス生成，プロセス生成，fork, execve, PID, PPID, init プロセス，Linux プロセス"
---

Linux のプロセスは親子関係を形成します。シェルは通常、子プロセスを作り、その子が要求されたプログラムを実行するよう整えて外部コマンドを開始します。古典的な説明では、この処理を `fork` と `exec` に分けます。

## `fork` で子を作る

`fork()` システムコールは呼び出し元を基に子プロセスを作ります。親と子は `fork` の戻り位置から処理を続けますが、異なる戻り値と PID を持ちます。

子は論理的に独立したプロセス状態を得ます。Linux は最初、copy-on-write で物理メモリページを共有し、一方が変更したときだけコピーできます。開いたファイル記述子は継承され、同じ基盤の open file description を参照するため、ファイルオフセットなどが共有されたままの場合があります。

:::single-choice{#process-creation-fork-result} 成功した `fork()` は何を作りますか？

::option[同じプロセス内の置き換え用プログラムだけ。]{#process-creation-fork-replacement explanation="現在のプログラムイメージを置き換えるのは exec 操作です。"}
::option[新しい PID を持つ子プロセス。]{#process-creation-fork-child .correct explanation="fork() は別の子プロセスと親子関係を作ります。"}
::option[全物理メモリページの永久的なコピーを即座に作る。]{#process-creation-fork-full-copy explanation="Linux は通常、全ページをすぐ複製せず copy-on-write を使います。"}
:::

## `execve` でプログラムを置き換える

`execve()` は新しいプログラムを呼び出し元プロセスへ読み込みます。成功するとプロセスイメージを置き換え、古いプログラムへ戻りません。新しいプロセスを作らないため PID は同じです。

多くのシェルコマンドは fork-exec パターンに従います。

1. シェルが子を作る。
2. 子がリダイレクトなどの実行状態を準備する。
3. 子が要求されたプログラムを実行する。
4. フォアグラウンドかバックグラウンドかに応じ、シェルが待つか続行する。

ライブラリやアプリケーションは `posix_spawn()` などの上位インターフェースを公開でき、Linux には `clone()` など追加の仕組みもあります。fork-exec は唯一の方法ではありませんが、理解に有用なモデルです。

:::single-choice{#process-creation-exec-pid} `execve()` が成功した後、プロセスの PID はどうなりますか？

::option[親の PID と同じになる。]{#process-creation-exec-parent-pid explanation="親と子は別々のプロセス ID を保ちます。"}
::option[プログラムイメージが置き換わっても PID は同じまま。]{#process-creation-exec-same-pid .correct explanation="execve() は別プロセスを作らず、呼び出し元を変換します。"}
::option[新しいプログラムの開始前に削除される。]{#process-creation-exec-pid-removed explanation="既存プロセスが同じ PID で、新しいコード、データ、スタックなどを持って続きます。"}
:::

## 親と子の ID を調べる

`PID` はプロセス、`PPID` は親を識別します。

```bash
$ ps -o pid,ppid,stat,cmd
```

シェルが `ps` を開始すると、通常そのシェルの PID が `ps` の `PPID` に現れます。短命なプロセスは別の観測までに終了する場合があるため、タイミングが重要です。

:::single-choice{#process-creation-ppid} プロセス一覧の `PPID` は何を表しますか？

::option[以前そのプロセスへ割り当てられていた PID。]{#process-creation-previous-pid explanation="PID は再利用されますが、PPID は識別子の履歴ではありません。"}
::option[プロセスのスケジューリング優先度 ID。]{#process-creation-priority-id explanation="優先度は priority や nice 値など別のフィールドで表します。"}
::option[親プロセスのプロセス ID。]{#process-creation-parent-pid .correct explanation="PPID は現在の親プロセス関係を記録します。"}
:::

## PID 1 と親の付け替え

カーネルは最初のユーザー空間プロセスを PID 1 で開始します。システムによって `systemd`、別の init、コンテナや PID 名前空間内の小さな init などです。PID 1 はユーザー空間の一部を開始・監督し、シグナルと孤児回収について特別な責任を持ちます。

親が子より先に終了すると、子は PID 名前空間内の適切な subreaper または init プロセスへ付け替えられます。元の親が終わっても、子が終了する必要はありません。

:::single-choice{#process-creation-pid-one} PID 1 について正しい説明はどれですか？

::option[実行ファイル名が必ず正確に `init` である。]{#process-creation-pid-one-name explanation="systemd、別の init、コンテナ固有のプログラムなどを使えます。"}
::option[現在実行中の全プロセスを直接作った親である。]{#process-creation-pid-one-direct explanation="大半のプロセスは何世代もの中間の親を通じて作られます。"}
::option[その PID 名前空間の最初のプロセスで、init のような責任を持つ。]{#process-creation-pid-one-init .correct explanation="PID 名前空間内でユーザー空間の監督と回収の基点になります。"}
:::

[Linux プロセスの管理と監視](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) では、フォアグラウンド・バックグラウンドコマンドを動かしながら親子 ID を観測できます。

## まとめ

古典的な Linux プロセス生成手順を追跡できるようになりました。

1. `fork()` で別の PID を持つ子を作る。
2. `execve()` で PID を変えずプロセスイメージを置き換える。
3. PID と PPID から親子関係を識別する。
4. PID 1 と subreaper を、親が付け替えられた子の受け入れ先として理解する。
