---
lesson_id: "process-states"
course_id: "processes"
lang: "ja"
order_index: 9
title: "プロセス状態"
description: "`ps` のスナップショットで、一般的な Linux プロセス状態コードを解釈する方法を学びます。"
meta_title: "プロセス状態 - プロセス管理"
meta_description: "Linux プロセス状態の包括的なガイド。Linux における様々なプロセス状態（R、S、D、Z、T）と、`ps`コマンドを使った解釈方法を学びます。"
meta_keywords: "Linux プロセス状態，Linux プロセス状態，Linux プロセス状態，Linux プロセス状態，Linux プロセス状態 解説，ps コマンド，STAT コード，プロセス管理"
---

Linux のタスクは実行、待機、停止、終了に伴い、状態間を移動します。`ps` の `STAT` は一瞬を捉えるため、診断には1文字だけより繰り返し観測する方が有用です。

```bash
$ ps -o pid,ppid,stat,wchan:24,cmd
```

`STAT` の先頭文字が主状態で、後続文字はセッションリーダーやフォアグラウンドプロセスグループ所属などの性質を表す修飾子です。完全な一覧はローカルの `ps` マニュアルを参照してください。

## 実行中と割り込み可能なスリープ

- `R`：実行中または実行可能。CPU 上で実行中か、実行キューで CPU 時間を待っている。
- `S`：割り込み可能なスリープ。イベントを待ち、適切なシグナルやイベントで起こせる。

スリープは正常です。対話型プログラムやサービスは継続的に CPU を消費せず、入力、タイマー、ネットワーク通信、ロックなどを待つ時間が多くあります。

:::single-choice{#process-states-runnable-code} 主状態 `R` は何を意味しますか？

::option[CPU 上で実行中、または実行準備済み。]{#process-states-r-running .correct explanation="現在実行中と CPU サービスを待つ実行可能なタスクをまとめて表します。"}
::option[親が状態を回収した後のプロセス。]{#process-states-r-reaped explanation="完全に回収されたプロセスは通常のプロセス表エントリーとして現れません。"}
::option[割り込み不可能なスリープで待機中。]{#process-states-r-uninterruptible explanation="割り込み不可能なスリープは D です。"}
:::

:::single-choice{#process-states-interruptible-code} 割り込み可能なスリープを表す主状態はどれですか？

::option[`D`]{#process-states-sleep-d explanation="D は割り込み不可能なスリープです。"}
::option[`Z`]{#process-states-sleep-z explanation="Z は終了したが状態を回収されていない子です。"}
::option[`S`]{#process-states-sleep-s .correct explanation="割り込み可能な待機を示す一般的な ps コードです。"}
:::

## 割り込み不可能なスリープ

`D` は、ストレージやネットワークファイルシステムの I/O など、一部のカーネル操作を待つ割り込み不可能なスリープです。待機を離れるまで通常のシグナルへ反応せず、その間シグナルは保留される場合があります。

短時間なら正常です。長く続く、または多数の `D` は遅い・利用不能・故障した I/O を示す場合がありますが、状態だけでは原因を特定できません。結論前に待機チャネル、カーネルログ、ストレージとネットワークの正常性、関連サブシステムを調べます。

:::single-choice{#process-states-uninterruptible-code} 割り込み不可能なスリープを示す主状態はどれですか？

::option[`T`]{#process-states-d-stopped explanation="T は停止したタスクです。"}
::option[`D`]{#process-states-d-uninterruptible .correct explanation="割り込み不可能なカーネルスリープで待つタスクに使います。"}
::option[`R`]{#process-states-d-runnable explanation="R は実行中または実行可能なタスクです。"}
:::

## 停止とゾンビ状態

- `T`：通常は `SIGTSTP` などのジョブ制御、または `SIGSTOP` で停止。追跡による停止には小文字 `t` を使うツールもある。
- `Z`：実行を終えたが、親が終了記録をまだ回収していないゾンビ。

適切なら `SIGCONT` でジョブ制御による停止を再開します。ゾンビはすでに実行していないため、再開も kill もできず、親または引き取った reaper が回収します。

:::single-choice{#process-states-zombie-code} 主状態 `Z` は何を識別しますか？

::option[終了記録の回収を待つ、終了済みプロセス。]{#process-states-z-zombie .correct explanation="実行終了後も、親から見える最小限の状態を保持しています。"}
::option[端末の一時停止シグナルで停止したプロセス。]{#process-states-z-terminal-stop explanation="ジョブ制御による停止は通常 T です。"}
::option[現在 CPU コア全体を使っているプロセス。]{#process-states-z-cpu explanation="実行中は R で、ゾンビは命令を実行しません。"}
:::

## 文脈の中で状態を読む

状態コードは観測結果で、診断ではありません。経過時間、CPU 使用量、待機チャネル、親関係、ログ、繰り返しサンプルと組み合わせます。カーネルが報告した瞬間から画面を読むまでに状態が変わる場合もあります。

[Linux プロセスの管理と監視](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) では、フォアグラウンド、スリープ中、停止中、終了済みのタスクを安全に観測できます。

## まとめ

最も一般的な主プロセス状態を解釈できるようになりました。

1. `R` を実行中・実行可能、`S` を割り込み可能なスリープとして読む。
2. 長く続く `D` を診断ではなく待機症状として調べる。
3. 停止中の `T` と、終了済み未回収の `Z` を区別する。
4. 繰り返し観測し、周囲の証拠と組み合わせる。
