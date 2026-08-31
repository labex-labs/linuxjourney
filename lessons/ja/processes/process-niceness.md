---
lesson_id: "process-niceness"
course_id: "processes"
lang: "ja"
order_index: 8
title: "ニース値"
description: "nice 値が通常の Linux プロセスの CPU スケジューリング重みに影響する仕組みを学びます。"
meta_title: "ニース値 - プロセス"
meta_description: "Linux におけるニース値とは何か、それがプロセス優先度にどのように影響するかを発見してください。このレッスンでは、nice コマンドと renice コマンドを使用して CPU スケジューリングを管理し、システムパフォーマンスを向上させる方法を解説します。"
meta_keywords: "ニース値 linux, linux ニース値，linux ニース値とは，linux プロセス ニース値，プロセス ニース値，プロセス優先度，nice コマンド，renice コマンド，CPU スケジューリング"
---

Linux は異なる CPU コアで複数スレッドを同時実行し、1つのコアでは同時に動かせる数を超える実行可能スレッドへ時間を分配できます。スケジューラーは方針、優先度、affinity、ワークロードに従って選び、nice 値は通常の時分割方針における1つの入力です。

## Nice 値を解釈する

一般的な範囲は `-20` から `19` です。

- 低い値は、比較可能なタスクに対して相対的に大きなスケジューリング重みを与える。
- 高い値はより「nice」で、相対的な重みが小さい。
- 既定値は一般に `0`。

CPU の割合を予約したり、即時実行を保証したりはしません。効果は比較可能な実行可能タスクが CPU 時間を競うときに最も見えます。リアルタイム方針、cgroup、CPU affinity、I/O 待ちなどが観測結果を左右する場合があります。

:::single-choice{#process-niceness-lower-value}
同じ通常スケジューリング方針で、相対的な CPU 重みが最も大きい nice 値はどれですか？

::option[`10`]{#process-niceness-value-ten explanation="正の値はより nice で、通常0や負の値より重みが小さくなります。"}
::option[`19`]{#process-niceness-value-nineteen explanation="一般的な範囲で最も nice な端にあり、相対的な重みが小さい値です。"}
::option[`-5`]{#process-niceness-value-minus-five .correct explanation="低い nice 値ほど、比較可能な通常タスク間で相対的な重みが大きくなります。"}
:::

## Niceness を表示する

`top` の `NI` 列で確認できます。`ps` でも明示できます。

```bash
$ ps -o pid,ni,pri,stat,cmd -p 3245
```

`NI` はユーザーから見える nice 値です。`PRI` などは導出されたスケジューラー優先度の場合があり、尺度はツールやクラスで異なるため、交換可能だと思わないでください。

:::single-choice{#process-niceness-top-column}
`top` で nice 値を通常表示する列はどれですか？

::option[`PID`]{#process-niceness-column-pid explanation="プロセスを識別し、スケジューリング調整は示しません。"}
::option[`TTY`]{#process-niceness-column-tty explanation="制御端末の関連付けを識別します。"}
::option[`NI`]{#process-niceness-column-ni .correct explanation="プロセスまたはスレッドの nice 値を表す一般的な略称です。"}
:::

## `nice` でコマンドを開始する

```bash
$ nice -n 5 long-computation
```

要求する調整と対応構文はローカルのマニュアルで確認できます。非特権ユーザーは通常、値を増やしてコマンドをより nice にできます。値を下げ、有利な重みを与えるには適切な権限またはリソース制限設定が必要です。

:::single-choice{#process-niceness-nice-command}
`nice -n 5 long-computation` は何をしますか？

::option[許可されれば nice 値5でコマンドを開始する。]{#process-niceness-start-five .correct explanation="nice は要求したスケジューリング調整を使って新しいコマンドを起動します。"}
::option[PID 5 を最小の nice 値へ変更する。]{#process-niceness-pid-five explanation="-n の後は対象 PID ではなく nice 値です。"}
::option[コマンドへ1 CPU の正確に5%を保証する。]{#process-niceness-five-percent explanation="nice 値は相対的な重みで、固定割合を予約しません。"}
:::

## `renice` で既存プロセスを変更する

```bash
$ renice -n 10 -p 3245
```

PID `3245` へ nice 値 `10` を要求します。PID は再利用されるため対象を先に確認し、結果も検証します。権限は所有者、特権、リソース制限、システム方針次第です。自分のプロセスの値を増やすことは通常可能ですが、特権なしでは元へ戻せない場合があります。

:::single-choice{#process-niceness-renice-purpose}
既存プロセスの nice 値を変更するツールはどれですか？

::option[`nice`]{#process-niceness-tool-nice explanation="主に調整値を付けて新しいコマンドを開始します。"}
::option[`kill`]{#process-niceness-tool-kill explanation="シグナルを送り、通常の niceness 編集ツールではありません。"}
::option[`renice`]{#process-niceness-tool-renice .correct explanation="オプションに従い、既存の PID、プロセスグループ、ユーザーを対象にします。"}
:::

[Linux プロセスの管理と監視](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) では nice 値の表示と変更を練習できます。アイドルなシステムで差を期待せず、競合する CPU バウンドタスクを比較してください。

## まとめ

niceness を CPU 保証と誤解せず、解釈・調整できるようになりました。

1. 低い nice 値をより大きな相対スケジューリング重みとして読む。
2. `NI` を導出された優先度フィールドと分けて調べる。
3. コマンド起動時は `nice` を使う。
4. 確認済みの既存プロセスには `renice` を使う。
