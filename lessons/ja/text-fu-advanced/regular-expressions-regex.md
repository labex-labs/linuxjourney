---
index: 1
lang: "ja"
title: "regex（正規表現）"
meta_title: "regex（正規表現） - 高度なテキスト操作"
meta_description: "Linux のパターンマッチングのための正規表現（regex）を学びます。テキスト操作のための^、$、.、[]などの regex 構文を理解します。grep スキルを向上させましょう！"
meta_keywords: "正規表現，regex, Linux regex, grep regex, パターンマッチング，regex チュートリアル，Linux コマンド，初心者"
---

## Lesson Content

正規表現は、パターンベースの選択のための強力なツールです。これらは、すでに遭遇した `*` ワイルドカードのような特殊な表記法を使用します。

最も一般的な正規表現をいくつか見ていきます。これらは、ほとんどすべてのプログラミング言語で普遍的に使用されています。

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

### 3. 任意の 1 文字にマッチする `.`

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

ブラケット内で使用される以前のアンカータグ `^` は、ブラケット内の文字を除くすべてを意味します。

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

これらが基本的な正規表現です。

## Exercise

`grep` と正規表現を組み合わせて、いくつかのファイルを検索してみてください。

```bash
grep [regular expression here] [file]
```

## Quiz Question

1 文字にマッチさせるには、どのような正規表現を使用しますか？

## Quiz Answer

.
