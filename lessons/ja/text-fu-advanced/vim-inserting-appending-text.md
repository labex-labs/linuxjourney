---
title: "Vim でのテキスト挿入と追記"
description: "Vim の挿入モードと追記モードを学びます。効率的なテキスト編集のための 'i'、'a'、'I'、'A'、'o'、'O' コマンドを理解しましょう。今すぐ Vim スキルを向上させましょう！"
keywords: "Vim insert mode, Vim append, Vim commands, Vim tutorial, Linux text editor, beginner Vim, Vim guide, Vim 'i' 'a"
---

## Lesson Content

Vim には、頻繁に使用する 2 つの主要なモードがあります。Normal モード（コマンド用）と Insert モード（テキスト入力用）です。

- いつでも `Esc` を押すと Normal モードに戻ります。

テキストを入力したい場所に応じて、さまざまな方法で Insert モードに入ります。

- `i` – カーソルの前に挿入
- `a` – カーソルの後に追記
- `I` – 現在の行の先頭に挿入
- `A` – 現在の行の末尾に追記
- `o` – 現在の行の下に新しい行を開いて挿入を開始
- `O` – 現在の行の上に新しい行を開いて挿入を開始

ヒント：これらのコマンドの前に数値を付けることができます。例えば、`3o` は下に 3 つの新しい行を開きます。

テキストの挿入が完了したら、`Esc` を押して Normal モードに戻ります。

## Exercise

`vim [file]` で任意のテキストファイルを開き、`i`、`a`、`I`、`A`、`o`、`O` を試した後、それぞれ `Esc` を押して Normal モードに戻ってください。

## Quiz Question

カーソルの前に Insert モードに入るキーはどれですか？

## Quiz Answer

i
