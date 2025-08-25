---
index: 4
lang: "ja"
title: "Vim 検索パターン"
meta_title: "Vim 検索パターン - 高度なテキスト操作"
meta_description: "Vim の検索パターンを学びましょう：順方向 (/) と逆方向 (?) 検索。'n' と 'N' で結果をナビゲートします。Vim スキルを今日から向上させましょう！"
meta_keywords: "Vim 検索，Vim コマンド，Linux テキストエディタ，Vim チュートリアル，Vim ガイド，初心者 Vim"
---

## Lesson Content

Vim セッション中に式を検索するには、`/`キーを押してから検索語を入力します。Enter キーを押すと、`n`を押して検索結果を順方向に進むか、`N`を押して逆方向に進むことができます。

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

`?`検索コマンドは、テキストファイルを逆方向に検索します。したがって、前の例では、最後の「pretty」が最初に出てきます。

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

練習は完璧をもたらします！Linux でのテキスト編集と検索の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Vim と Nano で Linux のテキストファイルを編集する](https://labex.io/ja/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Vim と Nano を使用してテキストファイルの作成、編集、保存、ナビゲートを練習します。このラボは、検索機能を含む必須のテキスト編集ツールに習熟するのに役立ちます。

このラボは、実際のシナリオで概念を適用し、Linux でのテキストファイル操作に自信をつけるのに役立ちます。

## Quiz Question

Vim で検索に使用するキーは何ですか？

## Quiz Answer

/
