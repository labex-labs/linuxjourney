---
lesson_id: "proc-filesystem"
course_id: "processes"
lang: "ja"
order_index: 10
title: "/proc ファイルシステム"
description: "Linux が仮想 `/proc` ファイルシステムを通じ、実行中のプロセスとカーネル情報を公開する仕組みを学びます。"
meta_title: "/proc ファイルシステム - プロセス"
meta_description: "Linux の仮想ディレクトリである/proc ファイルシステムについて解説します。これはカーネルと実行中のプロセスをダッシュボードのように表示します。標準コマンド以上の追加のプロセス詳細情報へのアクセス方法を学びましょう。"
meta_keywords: "/proc ファイルシステム，linux proc, プロセス情報，linux proc 拡張，システムダッシュボード，Linux プロセス，カーネル情報"
---

Linux は通常 `procfs` を `/proc` にマウントします。この仮想ファイルシステムはカーネルが生成したインターフェースをファイルとディレクトリとして示し、内容はディスク上の通常の永続ファイルではありません。プロセス状態と、一部のシステム全体のカーネル情報を公開します。

## プロセスディレクトリを見つける

```bash
$ findmnt /proc
$ ls /proc
```

数値のディレクトリ名は、呼び出し元の PID 名前空間から見えるプロセス ID に対応します。たとえば `/proc/12345` は、存在する瞬間の PID 12345 を表します。`/proc/self` は観測プロセス自身のディレクトリ、`/proc/thread-self` は現在のスレッドへ解決されるシンボリックリンクです。

可視性とアクセスは認証情報、名前空間、セキュリティ方針、`hidepid` などの procfs マウントオプション次第です。ディレクトリ一覧とファイルを開く間にプロセスが終了する場合があり、消失は検査ツールが扱うべき正常な競合です。

:::single-choice{#proc-filesystem-numeric-directory}
数値ディレクトリ `/proc/12345` は通常何を表しますか？

::option[番号12345のディスクブロック。]{#proc-filesystem-disk-block explanation="/proc は仮想カーネルインターフェースで、生のディスクブロック一覧ではありません。"}
::option[現在見えている PID 12345 のプロセス。]{#proc-filesystem-pid-directory .correct explanation="プロセス単位の procfs データは、見える PID 名のディレクトリ下にまとめられます。"}
::option[UID 12345 のユーザーアカウント。]{#proc-filesystem-user-directory explanation="トップレベルの数値プロセスディレクトリは UID ではなく PID に基づきます。"}
:::

## プロセス情報を読む

権限があれば状態ファイルを調べます。

```bash
$ less /proc/12345/status
```

プロセス名、状態、ID、認証情報、メモリカウンター、capability、シグナルマスクなどを含みます。ほかの有用な項目は次のとおりです。

- `/proc/12345/cmdline`：null バイトで区切られたコマンドライン引数
- `/proc/12345/environ`：アクセス制御され、機密情報を含み得る環境変数
- `/proc/12345/fd/`：開いたファイル記述子を表すシンボリックリンク
- `/proc/12345/maps`：現在のメモリマッピング
- `/proc/12345/cwd`：現在の作業ディレクトリへのシンボリックリンク

これらは変化する観測結果です。カーネルバージョンでフィールドが異なり、複数ファイルを読む間に状態が変わり、名前だけでは分からない注意点を持つカウンターもあります。

:::single-choice{#proc-filesystem-status-file}
PID 12345 のフィールド形式の概要を含むパスはどれですか？

::option[`/proc/status/12345`]{#proc-filesystem-status-reversed explanation="プロセス単位ファイルはトップレベルの status 下ではなく、PID 名ディレクトリ内にあります。"}
::option[`/proc/12345/status`]{#proc-filesystem-process-status .correct explanation="識別子、状態、メモリ、シグナル、認証情報のフィールドを示します。"}
::option[`/proc/cpuinfo/12345`]{#proc-filesystem-cpuinfo-pid explanation="/proc/cpuinfo はシステム全体のインターフェースで、PID ごとの状態ディレクトリではありません。"}
:::

## システム全体のインターフェース

すべてがプロセス用ではありません。

- `/proc/cpuinfo`：カーネルが報告する CPU 情報
- `/proc/meminfo`：システムメモリカウンター
- `/proc/mounts`：現在のプロセスから見えるマウント
- `/proc/loadavg`：ロード平均と実行可能タスク情報
- `/proc/sys/`：実行時のカーネルパラメーター

特に `/proc/sys` の一部は書き込み可能な設定インターフェースです。通常ファイルに見えるという理由だけで書き込まず、許可された変更前にパラメーター、範囲、永続化方式、ロールバックを理解してください。

:::single-choice{#proc-filesystem-system-interface}
1プロセスの状態ではなく、システム全体のメモリカウンターを提供する項目はどれですか？

::option[`/proc/self/status`]{#proc-filesystem-self-status explanation="観測プロセス自身の状態へ解決されます。"}
::option[`/proc/meminfo`]{#proc-filesystem-memory-info .correct explanation="カーネルが報告するシステムメモリ統計を含みます。"}
::option[`/proc/1/fd`]{#proc-filesystem-one-fd explanation="アクセス制御の範囲で PID 1 のファイル記述子を表します。"}
:::

## ツールを通じて `/proc` を使う

Linux の `ps`、`top`、`free` などは procfs などのカーネルインターフェースから多くのデータを得て、ラベル付け、計算、整形します。必要なフィールドを提供するなら日常作業ではツールを優先し、特定の詳細やスクリプトで直接読む場合はインターフェース文書を先に確認します。

直接読む処理は、形式を正しく解析し、プロセス消失を許容し、機密出力を保護し、1回の読み取りを原子的なシステムスナップショットと思わない設計が必要です。

:::single-choice{#proc-filesystem-live-data}
2つの検査コマンドの間に `/proc/PID` が消えることがあるのはなぜですか？

::option[全 procfs ファイルが毎秒自動で名前変更されるから。]{#proc-filesystem-renamed explanation="全項目を定期的に名前変更する規則はありません。"}
::option[`status` を読むとプロセスディレクトリが削除されるから。]{#proc-filesystem-read-delete explanation="状態の読み取りは読み取り専用で、プロセスを終了・削除しません。"}
::option[観測中にプロセスが終了できるから。]{#proc-filesystem-process-exit .correct explanation="procfs は実行中の状態を反映し、プロセス消失後にカーネルがディレクトリを取り除きます。"}
:::

## まとめ

procfs を実行中でアクセス制御されたカーネルインターフェースとして使えるようになりました。

1. 数値の `/proc` ディレクトリを見える PID へ対応付ける。
2. 競合と機密性を考慮し、選択したプロセス単位ファイルを読む。
3. プロセスディレクトリとシステム全体のインターフェースを区別する。
4. 信頼できる日常検査には文書化されたツールと形式を優先する。
