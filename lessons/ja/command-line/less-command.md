---
index: 8
lang: "ja"
title: "less"
meta_title: "less - コマンドライン"
meta_description: "効率的なテキストファイル表示のために Linux の less コマンドを習得しましょう。このガイドでは、less コマンドの使い方、ナビゲーション、unix less 検索の実行方法、および less を終了する方法を解説します。"
meta_keywords: "less コマンド，コマンド less, less 終了，unix less 検索，linux less, テキストファイル表示，ファイルナビゲーション，linux コマンドライン"
---

## Lesson Content

画面全体に収まらないほど大きなテキストファイルを表示する場合、`less command`は非常に貴重なツールです。古い Unix の格言にあるように、「less is more」（少ないことはより豊かである）です。（これは、同様の機能を持つ`more`コマンドも存在するという事実にかけたものです）。`less`ユーティリティはテキストをページ形式で表示し、ファイル全体をメモリにロードすることなく、ページごとにファイルを移動できるようにします。

### less コマンドの開始方法

ファイル表示を開始するには、単に`command less`の後にファイル名を指定します。これにより、ファイルが`less`インターフェースで開かれます。

```bash
less /home/pete/Documents/text1
```

`less`ビューア内に入ると、標準のシェルコマンドは機能しません。代わりに、テキストを移動および操作するために特定のキーセットを使用します。

### ナビゲーションとコントロール

ドキュメント内を移動するために、いくつかのキーを使用できます。

- **矢印キーとページキー**: `Page Up`、`Page Down`、`Up`、`Down`を使用して、1 行ごと、または 1 ページごとに移動します。
- **先頭へ移動**: `g`を押すと、テキストファイルの先頭に直接移動します。
- **末尾へ移動**: `G`（Shift + g）を押すと、テキストファイルの末尾にジャンプします。
- **ヘルプメニュー**: `less`内でコマンドを忘れた場合は、`h`を押すだけで役立つ概要が表示されます。

### Unix less 検索

`less`の強力な機能の 1 つは、テキストを検索する機能です。`unix less search`を実行するには、`/`の後に検索したいテキストを入力し、Enter キーを押します。これにより、検索語句のすべての出現箇所がハイライトされます。

- `/search_term`: "search_term"を前方検索します。
- `?search_term`: "search_term"を後方検索します。
- `n`: 検索語句の次の出現箇所にジャンプします。
- `N`: 前の出現箇所にジャンプします。

### less を終了する方法

ファイル表示を終えたら、`exit less`してコマンドプロンプトに戻る方法を知る必要があります。

- **終了**: 単に`q`を押すと、`less`ビューアが終了し、シェルに戻ります。

`less command`を習得することは、Linux コマンドラインで作業する人にとって基本的なスキルであり、ファイル検査をはるかに効率的にします。

## Exercise

練習あるのみです！Linux でのテキストファイルの表示とナビゲーションに関する理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux less Command: File Paging](https://labex.io/ja/labs/linux-linux-less-command-file-paging-214301)** - Linux の'less'コマンドを使用して、検索、行番号、パターンマッチングを含むテキストファイルの効率的な表示とナビゲーションを学習します。
2. **[Linux more Command: File Scrolling](https://labex.io/ja/labs/linux-linux-more-command-file-scrolling-214299)** - Linux の'more'コマンドを使用して、基本的な使用法、特定の行からの開始、表示のカスタマイズを含むテキストファイルの効率的な表示を学習します。
3. **[Viewing Log and Configuration Files in Linux](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `cat`、`more`、`less`などのコマンドを使用して、システムログや設定ファイルを含むテキストファイルの効率的な表示とナビゲーションのための必須の Linux コマンドラインスキルを学習します。

これらのラボは、概念を実際のシナリオに適用し、テキストファイルの操作とナビゲーションに対する自信を構築するのに役立ちます。

## Quiz Question

`less`コマンドから終了するにはどうすればよいですか？回答として単一の文字キーを提供してください。注：回答は大文字と小文字が区別される英字です。

## Quiz Answer

q
