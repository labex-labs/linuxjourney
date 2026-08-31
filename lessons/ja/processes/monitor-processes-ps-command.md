---
lesson_id: "monitor-processes-ps-command"
course_id: "processes"
lang: "ja"
order_index: 1
title: "ps (プロセス)"
description: "`ps` でプロセスのスナップショットを取得し、`top` で変化する活動を監視する方法を学びます。"
meta_title: "ps (プロセス) - プロセス一覧"
meta_description: "Linux の ps コマンドを包括的なガイドで探求しましょう。Linux での ps -ef コマンドやその他のオプションを使用して、実行中のプロセスを表示し、PID を理解し、システムタスクを管理する方法を学びます。Linux の旅の完璧なスタートです。"
meta_keywords: "ps コマンド，ps -ef linux, ps -ef コマンド，linux ps -ef, ps -e linux, Linux プロセス，プロセス ID, PID, top コマンド，Linux の旅"
---

プロセスは、プログラムの実行中のインスタンスと、そのメモリ、認証情報、開いているリソース、実行状態を合わせたものです。Linux は各プロセスを数値のプロセス ID（PID）で識別します。同時に存在する間は一意ですが、終了後にカーネルが再利用できます。

## 基本的なスナップショット

オプションなしの `ps` は実装の既定条件で選んだスナップショットを表示し、通常は現在の端末とユーザーに関連するプロセスを示します。

```text
$ ps
    PID TTY          TIME CMD
  41230 pts/4    00:00:00 bash
  51224 pts/4    00:00:00 ps
```

一般的なフィールドは次のとおりです。

- `PID`：プロセス ID
- `TTY`：制御端末。関連付けがなければ `?`
- `TIME`：経過時間ではなく、累積 CPU 時間
- `CMD`：選択形式に応じたコマンド名またはコマンドライン

正確な列と既定の選択条件は `ps` の実装や環境で異なります。

:::single-choice{#ps-command-pid-meaning}
`PID` 列は何を識別しますか？

::option[プロセスの現在のディレクトリ番号。]{#ps-command-pid-directory explanation="現在のディレクトリはファイルシステム参照で、PID では表しません。"}
::option[秒単位の累積 CPU 時間。]{#ps-command-pid-cpu explanation="CPU 使用時間は TIME など別のフィールドに表示します。"}
::option[カーネルが割り当てたプロセス ID。]{#ps-command-pid-kernel .correct explanation="PID は実行中のプロセスを参照する数値識別子です。"}
:::

## BSD 形式のオプションで一覧表示する

Linux の `ps` は複数のオプション形式を受け付けます。BSD 形式は先頭のダッシュなしで書くのが一般的です。

```bash
$ ps aux
```

この組み合わせでは次の意味があります。

- `a`：端末を持つほかのユーザーのプロセスまで選択を広げる。
- `x`：制御端末のないプロセスも含め、`a` とともに選択を広げる。
- `u`：`USER`、`%CPU`、`%MEM`、`VSZ`、`RSS` などを持つユーザー指向形式を選ぶ。

オプションの意味は相互作用するため、各文字を独立したコマンドと考えず、組み合わせ全体を解釈してください。

:::single-choice{#ps-command-aux-user-format}
`ps aux` でユーザー指向の出力形式を要求するオプションはどれですか？

::option[`u`]{#ps-command-aux-u .correct explanation="BSD 形式の u はユーザー指向の出力列を選びます。"}
::option[`x`]{#ps-command-aux-x explanation="x は特に制御端末のないプロセスなど、選択対象へ影響します。"}
::option[`a`]{#ps-command-aux-a explanation="a は現在のユーザーの端末プロセスだけでなく、選択範囲を広げます。"}
:::

## 標準形式のオプションを使う

広く使われる `ps -ef` は先頭にダッシュを付けます。

```bash
$ ps -ef
```

- `-e`：呼び出し元から見えるすべてのプロセスを選ぶ。
- `-f`：完全形式の一覧を要求する。

通常は `UID`、`PID`、`PPID`、開始時刻、コマンド情報を含みます。`PPID` は親プロセス ID です。この一覧は本質的に階層表示ではありません。親子関係が重要なら、対応環境で `--forest`、または `pstree` を使います。

:::single-choice{#ps-command-ef-selection}
`ps -ef` の `-e` は何を要求しますか？

::option[中断するまで毎秒更新すること。]{#ps-command-e-refresh explanation="ps はスナップショットを生成し、継続更新は top などの機能です。"}
::option[呼び出し元から見えるすべてのプロセスを含む選択。]{#ps-command-e-every .correct explanation="標準形式の -e は、選択可能な全プロセスへスナップショットを広げます。"}
::option[コマンドがエラーで終了したプロセスだけ。]{#ps-command-e-errors explanation="選択はコマンドの将来の終了状態に基づきません。"}
:::

## 時間とともに活動を監視する

`ps` は1回のスナップショットを出力して終了します。定期的に更新する対話型ビューには `top` を使います。

```bash
$ top
```

CPU とメモリの消費が変化するプロセスを見つけられますが、値は変動するサンプルです。複数回観測し、割合を CPU 数、メモリ計算、ワークロードと関連付けて疑わしい問題を確認してください。

:::single-choice{#ps-command-snapshot-versus-top}
ここで紹介したうち、既定でプロセス表示を定期更新するツールはどれですか？

::option[`top`]{#ps-command-top-refresh .correct explanation="top は一定間隔で表示を更新する対話型モニターです。"}
::option[`ps -ef`]{#ps-command-ps-ef-snapshot explanation="完全形式のプロセススナップショットを出力して終了します。"}
::option[`ls -l`]{#ps-command-ls-files explanation="ファイルシステムの項目を表示し、ライブプロセスモニターではありません。"}
:::

実践には [Linux プロセスの管理と監視](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) でスナップショットと対話型モニターを比較するか、[Linux `top` コマンド](https://labex.io/labs/linux-linux-top-command-real-time-system-monitoring-388500) で並べ替えと絞り込みを試してください。

## まとめ

プロセスビューを選び、基本的な識別子を解釈できるようになりました。

1. PID を現在実行中のプロセスに対する再利用可能な識別子として扱う。
2. 小さな既定スナップショットにはオプションなしの `ps` を使う。
3. 広い選択と豊富な列には `ps aux` または `ps -ef` を使う。
4. 時間変化が重要なら `top` を使う。
