---
lesson_id: "tracking-processes-top"
course_id: "process-utilization"
lang: "ja"
order_index: 1
title: "プロセスの追跡：top"
description: "top を使ってシステム負荷、CPU、メモリ、プロセスごとの活動を解釈する方法を学びます。"
meta_title: "プロセスの追跡：top - プロセス利用率"
meta_description: "`top`コマンドを習得して Linux を学ぶ最良の方法を見つけましょう。このガイドでは、システムリソースの監視、プロセスの追跡、VIRT や RES などのメトリクスの理解方法を解説します。Linux の仕組みを理解するための重要な要素です。"
meta_keywords: "Linux top コマンド，プロセス監視，システム利用率，Linux の仕組み，linux top virt res, Linux 学習法，Linux パフォーマンス，プロセス管理，証明書付き無料オンライン Linux トレーニング"
---

`top` はシステム活動と実行中プロセスを繰り返し更新して表示します。パフォーマンスに関する仮説を立てるのに役立ちますが、一度の高負荷サンプルだけでは問題の原因を証明できません。複数回の更新を比較し、ログやワークロード固有の指標と照合してください。

## システム概要を読む

一般的な表示では、概要行の後にプロセステーブルが続きます。

```text
top - 18:06:26 up 6 days, 4:07, 2 users, load average: 0.92, 0.62, 0.59
Tasks: 389 total, 1 running, 387 sleeping, 0 stopped, 1 zombie
%Cpu(s): 1.8 us, 0.4 sy, 0.0 ni, 97.6 id, 0.1 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 32099.0 total, 5276.3 free, 7031.2 used, 19791.5 buff/cache
MiB Swap: 32700.0 total, 32661.0 free, 39.0 used
```

最初の行には現在時刻、稼働時間、ログイン中ユーザー数、1分、5分、15分の負荷平均があります。タスク行はプロセス状態を数えます。負荷平均は CPU 使用率そのものではありません。Linux では実行可能なタスクと割り込み不能スリープ中のタスクを反映するため、CPU 数、I/O 活動、遅延と合わせて解釈します。

:::single-choice{#top-load-average-periods}
`top` の三つの負荷平均値は何を表しますか？

::option[1分、5分、15分間の平均負荷。]{#top-one-five-fifteen .correct explanation="これらの値は、徐々に長くなる直近の時間窓を要約します。"}
::option[最も忙しい三つのプロセスによる CPU 使用率。]{#top-three-processes explanation="プロセスごとの CPU は、この三つの概要値ではなくプロセステーブルに表示されます。"}
::option[メガバイト単位の空きメモリ、キャッシュ、swap。]{#top-three-memory-values explanation="メモリと swap には別の概要行があります。"}
:::

## CPU 時間を解釈する

一般的な CPU フィールドには次のものがあります。

- `us`: ユーザー空間での実行時間。
- `sy`: カーネルでの実行時間。
- `ni`: nice 値が設定されたタスクのユーザー空間時間。
- `id`: アイドル時間。
- `wa`: 未完了の I/O 要求がある間のアイドル時間。
- `hi` と `si`: ハードウェア割り込みとソフトウェア割り込みの処理。
- `st`: ハイパーバイザーがほかのゲストに使った仮想 CPU 時間。

高い `wa` 値は I/O 待ちという仮説を支持しますが、デバイスの特定や、ストレージが唯一のボトルネックであることまでは証明しません。結論を出す前にデバイス遅延とアプリケーションの動作を調べます。

:::single-choice{#top-cpu-wa-meaning}
CPU フィールド `wa` は何を報告しますか？

::option[通常のユーザーコードを実行した時間。]{#top-wa-user explanation="ユーザー空間での実行は `us` に報告されます。"}
::option[起動後に swap へ書き込まれたメモリページ数。]{#top-wa-swap explanation="Swap 活動は CPU 時間の分類ではありません。"}
::option[I/O 要求が未完了である間の CPU アイドル時間。]{#top-wa-io .correct explanation="このフィールドは I/O 待ち時間であり、診断にはデバイス側の補強証拠が必要です。"}
:::

## プロセステーブルを読む

重要な列には一般に次のものがあります。

- `PID`、`USER`、`COMMAND`: 識別情報と所有者。
- `S`: 実行中（`R`）、スリープ（`S`）、割り込み不能スリープ（`D`）、停止（`T`）、ゾンビ（`Z`）などの状態。
- `%CPU` と `%MEM`: サンプリングされた CPU 活動と物理メモリの割合。
- `TIME+`: 累積 CPU 時間。
- `VIRT`: タスクに関連する仮想アドレス空間の合計。
- `RES`: 現在そのタスクに割り当てられ、swap されていない常駐物理メモリ。
- `SHR`: ほかのプロセスと共有される可能性がある常駐メモリ。

`VIRT` は消費している物理 RAM 量ではありません。マッピング済みファイル、共有ライブラリ、予約済みアドレス空間、swap されたページを含む場合があります。共有ページは割り当てを複雑にするため、`RES` も慎重に解釈する必要があります。

:::single-choice{#top-res-versus-virt}
プロセスの現在の常駐物理メモリにより近いフィールドはどれですか？

::option[`TIME+`]{#top-time-field explanation="これはメモリではなく CPU 時間を累積します。"}
::option[`VIRT`]{#top-virt-field explanation="仮想サイズには RAM に常駐する必要のないアドレス空間も含まれます。"}
::option[`RES`]{#top-res-field .correct explanation="常駐サイズは、共有に関する注意はあるものの、現在プロセスのために常駐する物理ページを反映します。"}
:::

## 対象を絞って並べ替える

既知の PID を直接監視します。

```bash
$ top -p 1234,5678
```

一般的な procps-ng 実装では、`top` 内で `P` を押すと CPU 順、`M` でメモリ順、`1` で CPU ごとの行を切り替え、`q` で終了します。キーとフィールドは実装によって異なるため、`h` でローカルの対話ヘルプを表示してください。

操作する前に PID、コマンド、タイムスタンプ、複数のサンプルを記録します。プロセスが一時的に最上位へ来るのは正常な場合があり、終了させるとデータ損失や障害を引き起こす可能性があります。

:::single-choice{#top-monitor-known-pid}
表示を PID 1234 に限定する呼び出しはどれですか？

::option[`top -u 1234`]{#top-user-filter explanation="`-u` 形式は値を PID とせず、ユーザーで絞り込みます。"}
::option[`top -d 1234`]{#top-delay-filter explanation="一般的な実装の `-d` は更新間隔を制御します。"}
::option[`top -p 1234`]{#top-pid-filter .correct explanation="`-p` オプションは監視する一つ以上のプロセス ID を選択します。"}
:::

## まとめ

`top` を使ってシステムパフォーマンスの仮説を立て、検証できるようになりました。

1. 負荷平均を CPU 使用率ではなく、時間窓ごとの負荷として読む。
2. 複数のサンプルで CPU の各分類を比較する。
3. 仮想アドレス空間と常駐メモリを区別する。
4. 既知の PID に絞り、操作前に証拠を検証する。
