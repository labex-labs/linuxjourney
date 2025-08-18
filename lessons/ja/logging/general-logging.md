---
index: 3
lang: "ja"
title: "一般的なロギング"
meta_title: "一般的なロギング - ロギング"
meta_description: "Linux のログファイル（/var/log/messages や syslog など）について学びます。効果的なシステムトラブルシューティングのために、それらの違いを理解しましょう。Linux の学習を始めましょう！"
meta_keywords: "Linux ログ，syslog, var/log/messages, Linux トラブルシューティング，Linux 初心者，Linux ガイド，システムログ"
---

## Lesson Content

システム上で確認できるログファイルは多数あり、その多くは `/var/log` 以下にあります。すべてを網羅するわけではありませんが、主要なものをいくつか説明します。

システムが何をしているかを把握するために確認できる一般的なログファイルは 2 つあります。

### `/var/log/messages`

このログには、起動時 (dmesg)、auth、cron、daemon などで記録されたメッセージを含む、重要ではないメッセージやデバッグ以外のすべてのメッセージが含まれます。マシンの動作状況を把握するのに非常に役立ちます。

### `/var/log/syslog`

これは auth メッセージを除くすべてをログに記録します。マシンのエラーをデバッグするのに非常に役立ちます。

これらの 2 つのログは、システムの問題をトラブルシューティングする際に十分役立つはずです。ただし、特定のログコンポーネントだけを表示したい場合は、それらにも個別のログがあります。

## Exercise

`/var/log/messages` と `/var/log/syslog` ファイルを見て、違いを確認してください。

## Quiz Question

auth メッセージを除くすべてをログに記録するログファイルは何ですか？

## Quiz Answer

syslog
