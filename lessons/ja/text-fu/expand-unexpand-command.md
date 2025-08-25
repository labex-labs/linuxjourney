---
index: 10
lang: "ja"
title: "expand と unexpand"
meta_title: "expand と unexpand - Text-Fu"
meta_description: "`expand`コマンドでタブをスペースに、`unexpand`コマンドでスペースをタブに変換する方法を学びます。この Linux チュートリアルでテキストファイルの書式設定を改善しましょう。"
meta_keywords: "expand command, unexpand command, Linux tabs, Linux spaces, text formatting, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

`cut`コマンドに関するレッスンでは、タブを含む`sample.txt`ファイルがありました。通常、タブは目に見える違いを示すものですが、一部のテキストファイルではそれが十分に表示されません。テキストファイルにタブがあると、望ましい間隔が得られない場合があります。タブをスペースに変換するには、`expand`コマンドを使用します。

```bash
expand sample.txt
```

上記のコマンドは、各タブがスペースのグループに変換された出力を表示します。この出力をファイルに保存するには、以下に示すように出力リダイレクトを使用します。

```bash
expand sample.txt > result.txt
```

`expand`とは反対に、`unexpand`コマンドを使用して、各スペースのグループをタブに変換し直すことができます。

```bash
unexpand -a result.txt
```

## Exercise

練習は完璧をもたらします！ここでは、Linux でのテキスト操作とリダイレクトの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux での入出力のリダイレクト](https://labex.io/ja/labs/comptia-redirecting-input-and-output-in-linux-590840)** - `>`や`>>`などの演算子を使用して、標準出力 (stdout)、標準エラー (stderr)、および標準入力 (stdin) を操作することにより、コマンドからのデータフローを制御する練習をします。
2. **[シンプルなテキスト処理](https://labex.io/ja/labs/linux-simple-text-processing-18004)** - `tr`、`col`、`join`、`paste`などの強力なコマンドを使用して、テキストデータを効率的に操作および分析する方法を学び、データ処理のためのコマンドラインスキルを向上させます。
3. **[テキスト処理と正規表現](https://labex.io/ja/labs/linux-text-processing-and-regular-expressions-18003)** - 強力なテキスト処理ツールである`grep`、`sed`、`awk`を学び、正規表現を使用して Linux で効率的なテキスト操作とパターンマッチングを行います。

これらのラボは、実際のシナリオでテキスト変換とファイル操作の概念を適用し、Linux コマンドラインツールに自信を持つのに役立ちます。

## Quiz Question

タブをスペースに変換するために使用されるコマンドは何ですか？

## Quiz Answer

expand
