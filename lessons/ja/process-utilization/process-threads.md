---
lesson_id: "process-threads"
course_id: "process-utilization"
lang: "ja"
order_index: 3
title: "プロセススレッド"
description: "Linux のスレッドがプロセス資源を共有する仕組みと、ps で調べる方法を学びます。"
meta_title: "プロセススレッド - プロセス利用率"
meta_description: "Linux プロセススレッドのガイド。シングルスレッドプロセスとマルチスレッドプロセスの違い、および ps コマンドを使用してスレッドを表示する方法を学びます。"
meta_keywords: "Linux スレッド，プロセススレッド，ps スレッド表示，ps m, マルチスレッド，シングルスレッド，軽量プロセス，Linux プロセス管理"
---

スレッドは、プロセス内でスケジュールされる実行の流れです。実行中の各プロセスには少なくとも一つのスレッドがあり、マルチスレッドプロセスには並行して進行できる複数の流れがあります。

## プロセスとスレッド

一つのプロセス内のスレッドは、仮想アドレス空間や開いているファイル記述子などの資源を共有します。各スレッドは、それでもレジスターやスタックを含む固有の実行状態を持ちます。共有により効率的に通信できますが、同期されていない一つのスレッドの変更がほかへ影響することも意味します。

別々のプロセスは通常、異なるアドレス空間を持ち、明示的なプロセス間通信機構を通じて通信します。どちらの設計が自動的に高速または安全ということはなく、ワークロードと実装によってトレードオフが決まります。

:::single-choice{#threads-shared-resource}
同じプロセス内のスレッドが通常共有する資源はどれですか？

::option[プロセスの仮想アドレス空間。]{#threads-shared-address-space .correct explanation="プログラムの同期に従い、スレッドは同じプロセスメモリへアクセスできます。"}
::option[スレッドごとに独立したカーネルのインストール。]{#threads-separate-kernel explanation="すべてのスレッドは実行中のシステムカーネルを使います。"}
::option[スレッドごとに異なるファイルシステムルート。]{#threads-different-root explanation="通常、スレッドは別々のルートを与えられず、プロセスのファイルシステムコンテキストを共有します。"}
:::

## スレッド識別子

Linux は各スレッドを、固有のスレッド ID を持つスケジュール可能なタスクとして表します。スレッドグループリーダーの ID は一般にプロセス ID として表示され、全メンバーが一つのスレッドグループ ID を共有します。ツールは `PID`、`TID`、`LWP`、`SPID` などのラベルを使うため、すべて同じ意味だと考えず、各ツールのフィールド定義を確認してください。

:::single-choice{#threads-own-scheduling-state}
各スレッドが独立して維持するものは何ですか？

::option[プロセスの完全なオープンファイルテーブル。]{#threads-open-files-shared explanation="一つのプロセス内のスレッドは通常、開いているファイル記述子を共有します。"}
::option[マシン全体のユーザーデータベース。]{#threads-user-database explanation="アカウントデータベースはスレッド固有の状態ではありません。"}
::option[自身の実行状態とスタック。]{#threads-stack-state .correct explanation="プロセス資源を共有していても、スレッドには固有の実行コンテキストが必要です。"}
:::

## ps でスレッドを一覧表示する

曖昧な既定レイアウトを避けるため、出力フィールドを明示します。

```bash
$ ps -eLo pid,tid,psr,stat,comm
```

procps の `ps` では、`-L` がスレッドを表示し、`-e` が全プロセスを選択します。`pid` はスレッドグループ、`tid` は個々のスレッド、`psr` は最後に実行された CPU、`stat` は状態を示します。一つのプロセスを調べるには次を使います。

```bash
$ ps -L -p 1234 -o pid,tid,stat,pcpu,comm
```

スレッド一覧はスナップショットです。直後にスレッドが終了したり状態を変えたりする場合があります。

:::single-choice{#threads-ps-one-process}
PID 1234 に属するスレッドを明示的なフィールドで一覧表示するコマンドはどれですか？

::option[`ps -p 1234 -o pid,ppid,stat,pcpu,comm`]{#threads-process-only explanation="この出力ではスレッドごとの行を要求していません。"}
::option[`ps -L -p 1234 -o pid,tid,stat,pcpu,comm`]{#threads-ps-l .correct explanation="`-L` オプションは、選択したプロセスのスレッド行を要求します。"}
::option[`ps -e -o pid,user,stat,pcpu,comm`]{#threads-all-processes explanation="これはシステム全体のプロセスを選びますが、スレッド ID は表示しません。"}
:::

## スレッドの活動を解釈する

一つのスレッドの高い CPU 使用率が、プロセス全体の平均に隠れる場合があります。スレッド単位の CPU サンプルを、アプリケーションログ、スタックトレース、プロファイリングツールと組み合わせてください。停止、権限、サービスへの影響を理解せず、本番タスクへデバッガーを接続したりシグナルを送ったりしてはいけません。

:::single-choice{#threads-snapshot-limit}
`ps` のスレッド一覧を永続的な状態として扱うべきでないのはなぜですか？

::option[`ps` が各行について代替スレッドを作成するから。]{#threads-ps-creates explanation="このコマンドはタスクを観察し、一覧にした各タスクを複製しません。"}
::option[スレッド ID がすべての Linux ホストで同一だから。]{#threads-identical-ids explanation="識別子は稼働中システム内で割り当てられ、普遍的ではありません。"}
::option[スナップショット後にスレッドが状態を変えたり終了したりするから。]{#threads-change-after-snapshot .correct explanation="プロセス調査は、絶えず変化するシステムの一瞬を観察します。"}
:::

## まとめ

プロセス資源とスレッド固有の実行状態を区別できるようになりました。

1. すべてのプロセスに少なくとも一つのスレッドがあると理解する。
2. 一つのプロセス内でスレッドが共有する資源を識別する。
3. `ps -L` でプロセス ID とスレッド ID を明示して一覧表示する。
4. スレッド出力をスナップショットとして扱い、ほかの証拠と照合する。
