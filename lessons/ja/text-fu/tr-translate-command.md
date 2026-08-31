---
lesson_id: "tr-translate-command"
course_id: "text-fu"
lang: "ja"
order_index: 13
title: "tr (変換)"
description: "標準入力ストリームの文字集合を変換、削除、圧縮する方法を学びます。"
meta_title: "tr (変換) - Text-Fu"
meta_description: "文字の変換、削除、繰り返しの圧縮、文字クラスの使用、テキストのクリーンアップなど、Linuxのtrコマンドを例とともに学びましょう。"
meta_keywords: "linux tr コマンド, tr コマンド, tr -d, tr -s, 文字変換, 文字削除, 文字クラス, テキスト処理 linux"
---

translate の略である `tr` コマンドは、stdin から読んだ文字を変換、削除、圧縮します。通常の入力ファイルオペランドは受け取らないため、パイプまたは入力リダイレクトでデータを渡します。

基本構文は次のとおりです。

```bash
tr [OPTIONS] SET1 [SET2]
```

`tr` が扱うのは文字集合で、単語や一般的な正規表現ではありません。完全な単語、行構造、周囲の文脈に依存する変換には別のツールを使います。

## 文字を変換する

2 つの集合を指定すると、`SET1` の文字を同じ位置にある `SET2` の文字へ対応付けます。

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

```bash
$ echo "2026-06-23" | tr '-' '/'
2026/06/23
```

```bash
$ echo "abc123" | tr 'abc' 'ABC'
ABC123
```

集合式はシェルにそのまま渡るよう引用します。`SET1` に含まれない文字は変更されません。

:::single-choice{#tr-map-characters}
`printf '%s\n' 'abc123' | tr 'abc' 'ABC'` は何を表示しますか？

::option[`ABCABC`]{#tr-uppercase-digits explanation="数字は変換元集合にないため、文字へ置き換えられません。"}
::option[`ABC123`]{#tr-uppercase-abc .correct explanation="`a`、`b`、`c` は `ABC` の同じ位置の文字へ対応し、数字は変わりません。"}
::option[`abc123ABC`]{#tr-append-set explanation="`tr` は一致する入力文字を変換し、変換先集合をストリーム末尾へ追加しません。"}
:::

## 文字を削除する

1 つの集合と `-d` を使うと、一致するすべての文字を削除します。

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

```bash
$ echo "Hello, world!" | tr -d '[:punct:]'
Hello world
```

```bash
$ printf "one\ntwo\nthree\n" | tr -d '\n'
onetwothree
```

数字は完全な数値トークンではなく 1 文字ずつ削除されます。文字クラスは現在のロケールで定義される集合を表します。改行を削除すると代わりの区切りを入れずに行が連結されます。

:::single-choice{#tr-delete-digits}
他の文字を変えず、stdin からすべての数字を削除するコマンドはどれですか？

::option[`tr -d '[:digit:]'`]{#tr-delete-digit-class .correct explanation="`-d` は入力ストリームから数字クラスの全文字を削除します。"}
::option[`tr -s '[:digit:]'`]{#tr-squeeze-digits explanation="`-s` は連続する数字を圧縮しますが、各並びから 1 文字は残します。"}
::option[`tr '[:digit:]'`]{#tr-one-set-no-delete explanation="通常の変換には第 2 集合が必要で、集合だけでは削除を要求しません。"}
:::

## 連続する文字を圧縮する

`-s SET` は、集合内の同じ文字が続く並びを 1 文字へ置き換えます。

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

```bash
$ printf "one\n\n\nTwo\n" | tr -s '\n'
one
Two
```

最初の集合に含まれるのは通常の空白だけなので、タブや改行はそのコマンドでは圧縮されません。

:::single-choice{#tr-squeeze-spaces}
stdin 内の通常の空白の連続をすべて 1 個へ減らすコマンドはどれですか？

::option[`tr -s ' '`]{#tr-squeeze-space .correct explanation="`-s` は指定集合の連続文字を圧縮し、この集合には通常の空白が 1 つ含まれます。"}
::option[`tr -d ' '`]{#tr-delete-space explanation="`-d` は各並びに 1 個残すのではなく、通常の空白をすべて削除します。"}
::option[`tr ' ' ''`]{#tr-empty-destination explanation="空の変換先集合は圧縮を要求する明確で移植性のある方法ではありません。`-s` を使います。"}
:::

## 文字クラスと補集合を使う

一般的な文字クラスには `[:lower:]`、`[:upper:]`、`[:digit:]`、`[:alpha:]`、`[:alnum:]`、`[:space:]`、`[:punct:]` があります。

```bash
$ echo "linux journey" | tr '[:lower:]' '[:upper:]'
LINUX JOURNEY
```

```bash
$ echo "user@example.com!" | tr -cd '[:alnum:]'
userexamplecom
```

`-c` は `SET1` の補集合、つまり集合にないすべての文字を意味します。`-d` と組み合わせれば選択した種類だけを残せます。この例では改行も英数字でないため削除されます。レコード境界が重要なら区切りを意図的に残してください。

:::single-choice{#tr-keep-alphanumeric}
`tr -cd '[:alnum:]'` は stdin に何をしますか？

::option[英数字を削除し、それ以外を残す。]{#tr-delete-alnum explanation="補集合によって `-d` の対象が変わり、英数字集合そのものは残ります。"}
::option[英数字でないすべての文字を削除する。]{#tr-delete-nonalnum .correct explanation="`-c` が英数字集合を反転し、`-d` がその非英数字集合を削除します。"}
::option[すべての文字と数字を大文字へ変換する。]{#tr-uppercase-alnum explanation="変換先集合がないため、大文字小文字の変換は行いません。"}
:::

## ストリーム変換を組み立てる

処理を分けたほうが明確なら複数の `tr` を接続できます。

```bash
$ echo "Hello,,,     world!!!" | tr -d '[:punct:]' | tr -s ' '
Hello world
```

```bash
$ printf "name\tlevel\npete\tbeginner\n" | tr '\t' ','
name,level
pete,beginner
```

```bash
$ tr '[:lower:]' '[:upper:]' < names.txt
```

`tr` は stdin を読むため、ファイルは `<` で渡せます。結果を保存するなら stdout を別ファイルへ送り、読み取り前に入力を切り詰める同じパスへのリダイレクトは避けます。

:::single-choice{#tr-read-file-input}
`tr` に `names.txt` を stdin として読ませ、小文字を大文字へ変換するコマンドはどれですか？

::option[`tr names.txt '[:lower:]' '[:upper:]'`]{#tr-file-operand explanation="`tr` は通常の入力ファイル名をこの形で受け取らず、余分なオペランドで構文が不正になります。"}
::option[`tr -d '[:lower:]' < names.txt`]{#tr-delete-lowercase explanation="ファイルの読み方は正しいですが、小文字を変換せず削除します。"}
::option[`tr '[:lower:]' '[:upper:]' < names.txt`]{#tr-input-redirection .correct explanation="シェルが `names.txt` を stdin で開き、`tr` が小文字クラスを大文字クラスへ対応付けます。"}
:::

文字単位のストリーム変換を練習するには、次のラボを試してください。

1. **[Linux tr コマンド：文字の変換](https://labex.io/ja/labs/linux-linux-tr-command-character-translating-219198)** - 文字の変換、削除、文字クラス、連続文字の圧縮を練習します。

## まとめ

目的を絞った `tr` 操作で文字ストリームを変換できるようになりました。

1. 対応する集合間で文字を変換する。
2. `-d` で選択した文字を削除する。
3. `-s` で連続する文字を圧縮する。
4. ロケール依存のクラスと補集合を意図的に使う。
5. ファイルオペランドではなく stdin から入力を渡す。
