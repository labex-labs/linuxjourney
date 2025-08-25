---
index: 8
lang: "ja"
title: "head"
meta_title: "head - テキスト操作"
meta_description: "Linux の 'head' コマンドを使ってファイルの先頭を表示する方法を学びましょう。行数を指定する -n オプションなどを理解します。Linux コマンドの必須チュートリアルです。"
meta_keywords: "head コマンド，Linux head, ファイルの先頭を表示，Linux チュートリアル，Linux コマンド，初心者向け Linux, head -n, Linux ガイド"
---

## Lesson Content

非常に長いファイルがあるとしましょう。実際、選択肢はたくさんあります。`cat /var/log/syslog` を実行してみてください。何ページにもわたるテキストが表示されるはずです。このテキストファイルの最初の数行だけを見たい場合はどうすればよいでしょうか？それは `head` コマンドで可能です。デフォルトでは、`head` コマンドはファイルの最初の 10 行を表示します。

```bash
head /var/log/syslog
```

行数を任意に変更することもできます。代わりに最初の 15 行を見たいとしましょう。

```bash
head -n 15 /var/log/syslog
```

`-n` フラグは「行数 (number of lines)」を意味します。

## Exercise

練習は完璧をもたらします！ファイルの先頭を表示することと一般的なテキストファイル操作の理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux head コマンド：ファイルの先頭表示](https://labex.io/ja/labs/linux-linux-head-command-file-beginning-display-214302)** - この演習では、`head` コマンドを使用してテキストファイルの最初の行を表示する方法を学びます。行数の変更も含まれます。
2. **[Linux でのログファイルと設定ファイルの表示](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - システムログや設定ファイルなど、`head` のようなコマンドを必要とすることが多いテキストファイルを効率的に表示およびナビゲートするための、Linux の基本的なコマンドラインスキルを練習します。
3. **[迅速な脅威検出](https://labex.io/ja/labs/linux-rapid-threat-detection-387930)** - `head` (および `tail`) の知識を応用して、最近のログエントリを迅速に抽出し分析し、実際のサイバーセキュリティ分析をシミュレートします。

これらの演習は、実際のシナリオで概念を適用し、Linux でのテキストファイルの表示と分析に自信をつけるのに役立ちます。

## Quiz Question

`head` コマンドで表示したい行数を変更するには、どのフラグを使用しますか？

## Quiz Answer

-n
