---
index: 1
lang: "ja"
title: "正規表現（Regular Expressions）"
meta_title: "正規表現（regex） - 高度なテキスト操作"
meta_description: "Linux のパターンマッチングのための正規表現（regex）を学びます。`^`、`$`、`.`、`[]`などの正規表現の構文を理解してテキスト操作を行います。grep スキルを向上させましょう！"
meta_keywords: "正規表現，regex, Linux regex, grep regex, パターンマッチング，regex チュートリアル，Linux コマンド，初心者"
---

## Lesson Content

正規表現は、パターンベースの選択のための強力なツールです。これらは、`*` ワイルドカードなど、すでに遭遇したことのある特殊な表記法を使用します。

最も一般的な正規表現のいくつかを見ていきます。これらは、ほとんどすべてのプログラミング言語で普遍的に使用できます。

このフレーズをテスト文字列として使用します。

```plaintext
sally sells seashells
by the seashore
```

### 1. 行頭の `^`

```plaintext
^by
would match the line "by the seashore"
```

### 2. 行末の `$`

```plaintext
seashore$
would match the line "by the seashore"
```

### 3. 任意の単一文字に一致する `.`

```plaintext
b.
would match by
```

### 4. ブラケット表記 `[]` と `()`

これは少し複雑かもしれません。ブラケットを使用すると、ブラケット内にある文字を指定できます。

```plaintext
d[iou]g
would match: dig, dog, dug
```

以前のアンカータグ `^` は、ブラケット内で使用されると、ブラケット内の文字以外のすべてを意味します。

```plaintext
d[^i]g
would match: dog and dug but not dig
```

ブラケットは、使用したい文字の量を増やすために範囲を使用することもできます。

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

ただし、ブラケットは大文字と小文字を区別するので注意してください。

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

これらが基本的な正規表現の一部です。

## Exercise

練習は完璧をもたらします！正規表現とパターンマッチングの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux で grep を使ってテキストを検索する](https://labex.io/ja/labs/comptia-search-text-with-grep-in-linux-590841)** - このラボでは、`grep` コマンドを使用して Linux システム上のファイル内のテキストを検索する方法を学びます。基本的な検索を実行し、行番号を表示し、`^` や `$` などのアンカーを使用して行の位置に一致させ、基本的な正規表現と拡張正規表現の両方を活用して複雑なパターンマッチングを行います。
2. **[テキスト処理と正規表現](https://labex.io/ja/labs/linux-text-processing-and-regular-expressions-18003)** - 強力なテキスト処理ツールである grep、sed、awk を学びます。Linux で効率的なテキスト操作とパターンマッチングのために正規表現を使用する方法を学びます。
3. **[メールと数字の抽出](https://labex.io/ja/labs/linux-extracting-mails-and-numbers-17991)** - このチャレンジでは、grep と正規表現を使用してファイルからメールアドレスと数字を抽出する方法を学び、Linux の重要なテキスト処理スキルを実証します。

これらのラボは、実際のシナリオで概念を適用し、正規表現とテキスト処理に自信をつけるのに役立ちます。

## Quiz Question

単一の文字に一致させるには、どのような正規表現を使用しますか？

## Quiz Answer

.
