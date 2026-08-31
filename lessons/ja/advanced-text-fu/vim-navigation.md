---
lesson_id: "vim-navigation"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 5
title: "Vim ナビゲーション"
description: "Vim のノーマルモードで、文字、単語、行、ファイル内の位置を単位に移動する方法を学びます。"
meta_title: "Vim ナビゲーション - 高度なテキスト操作術"
meta_description: "h、j、k、l キーを使用して Vim ナビゲーションの基本を学びます。初心者向けの必須の Vim 移動を理解し、Linux コマンドラインスキルを向上させましょう。"
meta_keywords: "Vim ナビゲーション，Vim チュートリアル，Linux Vim, Vim 移動，Vim の基本，初心者 Vim, Linux テキストエディタ，Vim ガイド"
---

Vim には、マウスがなくても端末で使えるキーボードの移動コマンドがあります。一部の Vim 設定はマウス入力にも対応しますが、移動コマンドを覚えると編集コマンドと組み合わせられます。

練習前に `Esc` を押してノーマルモードへ戻ってください。

## 文字と画面上の行を単位に移動する

ノーマルモードの基本的な移動キーは次のとおりです。

- `h`：左へ 1 文字移動する
- `j`：画面上で下へ 1 行移動する
- `k`：画面上で上へ 1 行移動する
- `l`：右へ 1 文字移動する

一般に矢印キーでも同様に移動できますが、`h`、`j`、`k`、`l` なら、ほかのコマンドの近くに手を置いたまま操作できます。表示上で折り返された行では、通常 `j` と `k` はファイルの行を単位に移動し、`gj` と `gk` は画面に表示された行を単位に移動します。

:::single-choice{#vim-navigation-down}
ノーマルモードでカーソルを下へ 1 行移動するキーはどれですか？

::option[`k`]{#vim-nav-k-up explanation="`k` は上へ 1 行移動します。"}
::option[`l`]{#vim-nav-l-right explanation="`l` は右へ 1 文字移動します。"}
::option[`j`]{#vim-nav-j-down .correct explanation="ノーマルモードでは、`j` で下へ 1 行移動します。"}
:::

## 移動コマンドの前に回数を付ける

多くの移動コマンドの前に正の数を入力すると、その回数だけ繰り返せます。たとえば次のようにします。

```text
5j
3l
```

`5j` は下へ 5 行移動し、`3l` は可能な範囲で右へ 3 文字分移動します。回数は単語移動や編集コマンドとも組み合わせられます。

:::single-choice{#vim-navigation-count}
ノーマルモードで `4k` は何をしますか？

::option[可能な範囲で下へ 4 行移動します。]{#vim-nav-four-down explanation="下への移動には `j` を使い、`k` は反対方向へ移動します。"}
::option[可能な範囲で上へ 4 行移動します。]{#vim-nav-four-up .correct explanation="回数の `4` により、上へ移動する `k` を 4 回繰り返します。"}
::option[カーソルより上の 4 行を削除します。]{#vim-nav-delete-four explanation="移動コマンドだけならカーソル位置が変わります。削除には `d` などの演算子が必要です。"}
:::

## 単語を単位に移動する

便利な単語移動には次のものがあります。

- `w`：次の単語の先頭へ移動する
- `b`：現在または前の単語の先頭へ移動する
- `e`：現在または次の単語の末尾へ移動する

大文字の `W`、`B`、`E` は、句読記号を異なる形で扱い、空白で区切られた WORD を単位にします。`3w` のように回数を前に付けると、複数の単語を移動できます。

:::single-choice{#vim-navigation-next-words}
前方にある 3 番目の単語先頭位置へ移動するノーマルモードのコマンドはどれですか？

::option[`3w`]{#vim-nav-three-words .correct explanation="回数によって、次の単語へ移動するコマンドを 3 回適用します。"}
::option[`w3`]{#vim-nav-word-three explanation="このコマンド形式では、回数は移動コマンドの前に置きます。後ろの `3` では目的の移動を表せません。"}
::option[`3b`]{#vim-nav-three-back explanation="`b` は前方ではなく、前にある単語の先頭へ向かいます。"}
:::

## 行内を移動する

次の移動コマンドは、現在の行にある位置を対象にします。

- `0`：列 0 へ移動する
- `^`：最初の空白以外の文字へ移動する
- `$`：行末へ移動する

インデントされた行では、`0` と `^` の違いが重要です。

:::single-choice{#vim-navigation-first-nonblank}
インデントされた行の最初の空白以外の文字へ移動するコマンドはどれですか？

::option[`0`]{#vim-nav-column-zero explanation="0 は最初の列へ移動しますが、そこにはインデント用の空白がある場合があります。"}
::option[`$`]{#vim-nav-line-end explanation="ドル記号は行末を対象にします。"}
::option[`^`]{#vim-nav-first-nonblank .correct explanation="キャレットは先頭の空白を飛ばし、最初の空白以外の文字へ移動します。"}
:::

## ファイル内を移動する

大きく移動するには、ノーマルモードで次のコマンドを使います。

- `gg`：最初の行へ移動する
- `G`：最後の行へ移動する
- `42G`：42 行目へ移動する
- `Ctrl+F`：約 1 画面分前方へ移動する
- `Ctrl+B`：約 1 画面分後方へ移動する

`:42` と入力して Enter を押す方法でも、42 行目へ移動できます。

:::single-choice{#vim-navigation-file-end}
バッファーの最後の行へ移動するノーマルモードのコマンドはどれですか？

::option[`gg`]{#vim-nav-first-line explanation="小文字の `gg` は最後ではなく最初の行へ移動します。"}
::option[`$`]{#vim-nav-current-line-end explanation="ドル記号はファイル末尾ではなく、現在の行末へ移動します。"}
::option[`G`]{#vim-nav-last-line .correct explanation="回数を付けない大文字の `G` は最後の行へ移動します。"}
:::

使い捨てのファイルを編集しながらキーボード移動を練習するには、次のハンズオンラボを利用してください。

1. **[Vim と Nano で Linux のテキストファイルを編集する](https://labex.io/ja/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)**：実際の Linux 環境で、Vim と Nano の両方を使ってファイルの作成、テキスト編集、保存、移動を練習します。

## まとめ

これで、Vim のバッファー内を複数の便利な単位で移動できるようになりました。

1. `h`、`j`、`k`、`l` で文字または行を単位に移動する。
2. 数字を前に付けて移動を繰り返す。
3. `w`、`b`、`e` で単語の境界間を移動する。
4. 行頭、最初の文字、行末を選んで移動する。
5. `gg`、`G`、行番号でファイル内の位置へ移動する。
