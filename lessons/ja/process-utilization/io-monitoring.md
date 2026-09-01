---
lesson_id: "io-monitoring"
course_id: "process-utilization"
lang: "ja"
order_index: 5
title: "I/O 監視"
description: "iostat のサンプルを使って CPU とブロックデバイスの活動を調査する方法を学びます。"
meta_title: "I/O 監視 - プロセス利用率"
meta_description: "iostat コマンドで Linux の I/O 監視を習得。CPU とディスク使用率のメトリクスを分析し、システムパフォーマンスを最適化する方法を解説します。"
meta_keywords: "i/o 監視，iostat, linux i/o 監視，cpu 使用率，ディスク使用率，システムパフォーマンス，iowait, linux コマンド"
---

一般に `sysstat` パッケージが提供する `iostat` は、CPU とブロックデバイスの活動を報告します。スループットや使用率だけでは、ストレージがユーザーから見える問題を引き起こしていると断定できません。繰り返しサンプルとアプリケーション遅延を合わせて確認してください。

## 有用なサンプルを収集する

1秒間隔で拡張デバイス統計を実行します。

```bash
$ iostat -xz 1
```

一般的な実装では、最初のレポートが起動後の平均を含み、それ以降が各区間を表します。`-x` は拡張フィールドを追加し、`-z` は非活動デバイスを省略します。正常な時間帯と問題のある時間帯を捉えるため、複数の区間を観測してください。

:::single-choice{#iostat-first-report} `iostat` の最初のレポートは一般に何を表しますか？

::option[コマンドの最後の1秒だけに発生した操作。]{#iostat-final-second explanation="これは最初の累積レポートを表す説明ではありません。"}
::option[システム起動後の活動平均。]{#iostat-since-boot .correct explanation="後続レポートは通常区間ごとなので、最初のレポートは別に解釈する必要があります。"}
::option[翌日のデバイス使用率予測。]{#iostat-forecast explanation="このツールは将来の需要ではなく、観測済み統計を報告します。"}
:::

## CPU フィールドを読む

CPU セクションには通常、ユーザー（`%user`）、システム（`%system`）、アイドル（`%idle`）、I/O 待ち（`%iowait`）、仮想マシンの steal（`%steal`）時間があります。I/O 待ちは、未完了の I/O 要求が存在する間の CPU アイドル時間であり、ディスクがビジーである割合ではありません。

:::single-choice{#iostat-iowait-meaning} `%iowait` は何を表しますか？

::option[すでに使用されているディスク容量の割合。]{#iostat-capacity explanation="ファイルシステム容量と CPU 時間は別の測定値です。"}
::option[I/O 要求が未完了である間の CPU アイドル時間。]{#iostat-iowait-cpu .correct explanation="これは CPU 時間の分類であり、それだけでデバイスを特定できません。"}
::option[削除待ちのファイル数。]{#iostat-delete-queue explanation="このフィールドはファイル削除数を表しません。"}
:::

## デバイスフィールドを読む

フィールド名は sysstat のバージョンによって異なりますが、重要な概念には次があります。

- 1秒あたりの読み書き操作数またはデータ量は、ワークロードの速度を示します。
- `await` は、キュー待ちとサービス時間を含む平均要求遅延を示します。
- 平均キューサイズのフィールドは、待機中または処理中の要求を示します。
- `%util` は、経過時間のうちデバイスで I/O が進行していた割合を示します。

高い `%util` は単純な直列デバイスの飽和を示す場合がありますが、並列ストレージ、アレイ、仮想デバイスの性能容量へそのまま換算できません。遅延をデバイス設計、ワークロードパターン、サービス目標と比較してください。

:::single-choice{#iostat-await-purpose} 平均 I/O 要求遅延と最も直接関連するフィールドはどれですか？

::option[デバイス名。]{#iostat-device-name explanation="名前はデバイスを識別しますが、要求時間は測定しません。"}
::option[`await`]{#iostat-await .correct explanation="Await はキュー待ちとサービス時間を含む要求の平均時間を反映します。"}
::option[`%idle`]{#iostat-idle explanation="これはデバイス要求遅延ではなく CPU フィールドです。"}
:::

## 証拠を相関させる

結論を出す前に、デバイス名をマウントと下位デバイスへ対応付けます。

```bash
$ lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
$ findmnt
```

次に `iostat` の区間を、アプリケーション応答時間、データベースまたはファイルシステム指標、プロセス単位の I/O と照合します。Device mapper、RAID、コンテナ、ネットワーク接続ストレージは層を追加し、それぞれ固有のツールが必要になる場合があります。

:::single-choice{#iostat-high-util-conclusion} デバイスで高い `%util` を確認した後はどうすべきですか？

::option[すべてのファイルシステムで空き容量がないと仮定する。]{#iostat-assume-full explanation="ビジー時間はファイルシステム容量を報告しません。"}
::option[マウントされたワークロードを特定する前にファイルを削除する。]{#iostat-delete-first explanation="削除は状態変更を伴う操作であり、I/O ボトルネックの証明とは無関係です。"}
::option[遅延とワークロードの動作をストレージ設計と照合する。]{#iostat-correlate .correct explanation="デバイスの並列性とワークロード目標によって、その観測が有害かどうかが決まります。"}
:::

## まとめ

`iostat` を I/O 調査の証拠として使えるようになりました。

1. 拡張統計を複数の区間で収集する。
2. CPU の I/O 待ちとデバイスのビジー時間を区別する。
3. 遅延、キュー、スループット、使用率を合わせて解釈する。
4. デバイスをワークロードへ対応付け、アプリケーションへの影響を検証する。
