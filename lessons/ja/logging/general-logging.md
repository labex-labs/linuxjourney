---
index: 3
lang: "ja"
title: "一般的なログ"
meta_title: "一般的なログ - ログ"
meta_description: "Linux のログファイル（/var/log/messages や syslog など）について学びましょう。効果的なシステムトラブルシューティングのために、それらの違いを理解してください。Linux の旅を始めましょう！"
meta_keywords: "Linux ログ，syslog, var/log/messages, Linux トラブルシューティング，Linux 初心者，Linux ガイド，システムログ"
---

## Lesson Content

システム上で表示できるログファイルは多数あり、その多くは`/var/log`の下にあります。すべてを網羅するわけではありませんが、主要なものをいくつか説明します。

システムが何をしているかを把握するために表示できる一般的なログファイルが 2 つあります。

### `/var/log/messages`

このログには、起動時（dmesg）、認証、cron、デーモンなど、非クリティカルおよび非デバッグのすべてのメッセージが含まれます。マシンの動作状況を把握するのに非常に役立ちます。

### `/var/log/syslog`

これは認証メッセージを除くすべてをログに記録します。マシンのエラーをデバッグするのに非常に役立ちます。

これらの 2 つのログは、システムの問題をトラブルシューティングする際に十分すぎるほど役立つはずです。ただし、特定のログコンポーネントだけを表示したい場合は、それらにも個別のログがあります。

## Exercise

練習は完璧をもたらします！ログファイルの表示と分析の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux tail コマンド：ファイルの末尾表示](https://labex.io/ja/labs/linux-linux-tail-command-file-end-display-214303)** - ログ分析に不可欠な、テキストファイルの末尾を表示および監視するための Linux `tail`コマンドを学びます。
2. **[Linux head コマンド：ファイルの先頭表示](https://labex.io/ja/labs/linux-linux-head-command-file-beginning-display-214302)** - テキストファイルの最初の行を表示する`head`コマンドを探索し、ログヘッダーを素早く確認するのに役立ちます。
3. **[迅速な脅威検出](https://labex.io/ja/labs/linux-rapid-threat-detection-387930)** - `tail`と`head`を使用して最近のログエントリを迅速に抽出し分析することで、サイバーセキュリティ分析のための必須の Linux コマンドラインスキルを練習します。

これらのラボは、ログファイル表示の概念を実際のシナリオに適用し、システム監視に自信をつけるのに役立ちます。

## Quiz Question

認証メッセージを除くすべてをログに記録するログファイルは何ですか？

## Quiz Answer

syslog
