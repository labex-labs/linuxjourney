---
lesson_id: "kernel-logging"
course_id: "logging"
lang: "ja"
order_index: 4
title: "カーネルロギング"
description: "dmesg と journalctl を使い、現在および保存済みの Linux カーネルメッセージを問い合わせる方法を学びます。"
meta_title: "カーネルロギング - ロギング"
meta_description: "Linux カーネルログ（/var/log/kern.log や dmesg を含む）を探索します。起動メッセージ、ハードウェアドライバ情報、システム問題のトラブルシューティングのために kern ログを確認する方法を学びます。カーネルログ Linux ファイルに関するガイド。"
meta_keywords: "カーネルログ，kern.log, /var/log/kern.log, カーネルログ linux, kern ログ，dmesg, linux ロギング，起動メッセージ，カーネルイベント"
---

カーネルは boot、driver、device、filesystem、networking、memory、failure に関するメッセージを発します。これらのレコードは低レベルの症状を説明できますが、一つの warning 文字列だけでハードウェア故障を証明することはできません。

## カーネル Ring Buffer を読む

`dmesg` はカーネル ring buffer のメッセージを読みます。

```bash
$ dmesg --human
```

buffer の容量は有限なので、新しいメッセージが古いものを上書きする場合があります。アクセスが特権ユーザーに制限されることもあります。対応実装では `dmesg --follow` で新しいカーネルメッセージを追跡できます。範囲を限定した再現後に停止してください。

:::single-choice{#kernel-log-ring-buffer-limit}
古いカーネルイベントが現在の `dmesg` 出力にない場合があるのはなぜですか？

::option[カーネルイベントには一文字しか含められないから。]{#kernel-log-one-character explanation="カーネルメッセージには通常の診断テキストと metadata を含められます。"}
::option[`dmesg` が表示後に全行を恒久的に削除するから。]{#kernel-log-display-deletes explanation="通常の読み取りでは、表示した全カーネルメッセージを消費しません。"}
::option[有限の ring buffer が上書きした可能性があるから。]{#kernel-log-overwritten .correct explanation="メモリ内 buffer が保持できるカーネルメッセージデータの量には上限があります。"}
:::

## 読みやすい Timestamp を使う

生のカーネル timestamp は通常 boot からの相対時間です。`dmesg --ctime` または `--human` は wall-clock time へ変換できますが、変換値は時計の履歴に依存し、boot 後に時計が変わると不正確になる場合があります。正確な順序が重要なら boot-relative timing を保持してください。

:::single-choice{#kernel-log-timestamp-caution}
変換済み `dmesg` の wall-clock timestamp を慎重に扱うべきなのはなぜですか？

::option[常に別のマシンを参照するから。]{#kernel-log-other-machine explanation="ローカルで導かれる値ですが、時計変更が変換へ影響します。"}
::option[変化し得る時計へ boot-relative time を対応付けているから。]{#kernel-log-clock-change .correct explanation="時刻同期や手動変更により、表示された wall time が誤解を招く場合があります。"}
::option[時刻ではなくファイルシステムの空き容量を示すから。]{#kernel-log-free-space explanation="timestamp option が表示するのは時刻であり、storage capacity ではありません。"}
:::

## 永続的なカーネルレコードを問い合わせる

systemd ホストでは、現在の boot のカーネルレコードを問い合わせます。

```bash
$ journalctl -k -b
```

persistent journal storage が以前の boot を保持している場合、boot list を調べて一つ選びます。

```bash
$ journalctl --list-boots
$ journalctl -k -b -1
```

従来の syslog routing が `/var/log/kern.log` などを作る場合がありますが、設定によって異なります。保存済み `/var/log/dmesg` も普遍的ではなく、boot 時の snapshot にすぎない場合があります。

:::single-choice{#kernel-log-previous-boot}
保存されている一つ前の boot のカーネルメッセージを要求するコマンドはどれですか？

::option[`journalctl -u kernel -f`]{#kernel-log-unit-follow explanation="カーネルメッセージは `-k` で選び、follow は以前の boot を選択しません。"}
::option[`dmesg --clear`]{#kernel-log-clear explanation="clear は buffer 状態を変更し、以前の boot を取得しません。"}
::option[`journalctl -k -b -1`]{#kernel-log-previous .correct explanation="kernel filter と boot offset のマイナス 1 により、一つ前の保存済み boot を選びます。"}
:::

## カーネルイベントを調査する

boot、timestamp、device、subsystem、その時点の操作を特定します。周辺の kernel record と service record を問い合わせ、hardware inventory と現在状態を比較します。

```bash
$ journalctl -k -b --since '10 minutes ago'
$ lspci -k
$ lsblk
```

subsystem に関係するツールだけを使ってください。driver の reload、device の unbind、reboot の前に、storage、network、console、service への影響を評価し、復旧アクセスを確保します。

:::single-choice{#kernel-log-warning-response}
一つのカーネル warning 行に対する最善の対応はどれですか？

::option[読み込まれている全 driver を直ちに unload する。]{#kernel-log-unload-all explanation="重要な device を中断する可能性があり、warning の原因も切り分けられません。"}
::option[マシン全体を交換する必要があると判断する。]{#kernel-log-replace-machine explanation="一つのレコードだけでは、その結論を支える証拠が足りません。"}
::option[周辺イベントおよび現在の subsystem 状態と相関させる。]{#kernel-log-correlate .correct explanation="修正操作を選ぶ前に、文脈と再現可能な影響が必要です。"}
:::

## まとめ

これで、live kernel buffer のメッセージと保存済み kernel log を区別できます。

1. `dmesg` で有限の ring buffer を読む。
2. boot-relative timestamp と変換済み timestamp を慎重に解釈する。
3. `journalctl -k` で現在または以前の boot を問い合わせる。
4. 中断を伴う変更前にカーネルメッセージを相関させる。
