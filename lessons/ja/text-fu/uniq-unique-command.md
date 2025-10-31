---
index: 14
lang: "ja"
title: "uniq (重複なし)"
meta_title: "uniq (重複なし) - Text-Fu"
meta_description: "Linux の uniq コマンドを使用して、テキストから重複する隣接行をフィルタリングおよび削除する方法を探ります。-c、-u、-d などのオプションを使用して uniq Linux ツールを使用する方法や、sort と組み合わせて強力なテキスト処理を行う方法を学びましょう。"
meta_keywords: "uniq コマンド，Linux uniq, uniq linux, 重複削除，sort uniq, テキスト処理，データクレンジング，Linux チュートリアル"
---

## Lesson Content

Linux の `uniq` (ユニーク) コマンドは、テキスト処理において不可欠なツールです。テキストファイル内の重複行をフィルタリングおよび管理するのに役立ちますが、効果的に使用するにはその動作を理解することが重要です。

### 基本的な重複行の削除

`uniq` コマンドの主な機能は、隣接する重複行を削除することです。以下のような内容の `reading.txt` というファイルがあると想像してください。

```plaintext
book
book
paper
paper
article
article
magazine
```

重複行を削除するには、`uniq` コマンドを実行します。

```bash
$ uniq reading.txt
book
paper
article
magazine
```

ご覧のとおり、`uniq` は隣接する重複行が削除されたバージョンのファイルを出力します。

### 高度なフィルタリングオプション

`uniq` コマンドには、より詳細な分析のためのいくつかのオプションも用意されています。

各行の出現回数をカウントするには、`-c` (count) フラグを使用します。

```bash
$ uniq -c reading.txt
      2 book
      2 paper
      2 article
      1 magazine
```

重複していない行（つまり、一意な行）のみを表示するには、`-u` (unique) フラグを使用します。

```bash
$ uniq -u reading.txt
magazine
```

逆に、重複している行のみを表示するには、`-d` (duplicated) フラグを使用します。

```bash
$ uniq -d reading.txt
book
paper
article
```

### ソートの重要性

**uniq linux** コマンドに関する重要な点は、重複行を検出するのは、それらが互いに隣接している場合に限られるということです。重複がファイル全体に散らばっている場合、`uniq` はそれを識別しません。

重複が隣接していない `reading.txt` のバージョンを考えてみましょう。

```plaintext
book
paper
book
paper
article
magazine
article
```

このファイルに対して `uniq` を実行すると、驚くべき結果が得られます。

```bash
$ uniq reading.txt
book
paper
book
paper
article
magazine
article
```

隣接する同一の行がなかったため、行は削除されませんでした。これを解決するには、まずファイルのコンテンツをソートする必要があります。`sort` の出力を `uniq` にパイプすることで、すべての同一行が隣接することが保証され、`uniq` が正しく機能するようになります。この組み合わせは、シェルスクリプトにおける強力で一般的なパターンです。

```bash
$ sort reading.txt | uniq
article
book
magazine
paper
```

このコマンドは、まず行をアルファベット順にソートし、次に `uniq` が重複をフィルタリングして、クリーンな一意のエントリのリストを提供します。

## Exercise

練習あるのみです！`uniq` と `sort` を使用したテキスト処理の理解を深めるための実践的なラボをいくつかご紹介します。

1. **[Linux uniq コマンド：重複フィルタリング](https://labex.io/ja/labs/linux-linux-uniq-command-duplicate-filtering-219199)** - `sort` コマンドと組み合わせて Linux の `uniq` コマンドを使用して、テキストファイル内の重複行を識別、フィルタリング、分析する方法を学びます。
2. **[Linux sort コマンド：テキストのソート](https://labex.io/ja/labs/linux-linux-sort-command-text-sorting-219196)** - `sort` コマンドを使用してテキストファイルの行を整理する練習をします。これは `uniq` を効果的に使用する前の重要なステップです。
3. **[単語数カウントとソート](https://labex.io/ja/labs/linux-word-count-and-sorting-388125)** - この実践的な課題で、必須の Linux テキスト処理ツールである `wc` (単語数カウント) と `sort` を学びます。行、単語、文字をカウントし、頻繁なパターンを見つけ、さまざまなテキスト分析タスクのためにデータを効率的にソートする方法を学びます。

これらのラボは、実際のシナリオで概念を適用し、Linux でのテキスト処理とデータ操作に対する自信を構築するのに役立ちます。

## Quiz Question

ファイル内の隣接する重複行を削除するには、どのコマンドを使用しますか？コマンド名のみを小文字の英字で回答してください。

## Quiz Answer

uniq
