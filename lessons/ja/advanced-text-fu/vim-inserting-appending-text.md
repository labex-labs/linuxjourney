---
lesson_id: "vim-inserting-appending-text"
course_id: "advanced-text-fu"
lang: "ja"
order_index: 6
title: "Vim でのテキストの挿入と追記"
description: "Vim で現在のカーソル位置の前後や、現在行の上下から挿入モードへ入る方法を学びます。"
meta_title: "Vim でのテキスト挿入と追記 - 高度なテキスト操作術"
meta_description: "Vim の挿入モードと追記モードの違いを学びます。「i」、「a」、「o」などのコマンドを習得し、効率的にテキストを編集し、Vim で内容を追記したり、行を追加したりする方法をマスターしましょう。"
meta_keywords: "vim 追記，挿入と追記の違い vim, vim 挿入と追記，vim 行追加，vim テキスト編集，vim コマンド，vim チュートリアル，挿入モード，追記モード"
---

ノーマルモードでは、Vim はキーをコマンドとして解釈します。挿入モードでは、入力したテキストをバッファーへ挿入します。複数のノーマルモードコマンドを使い分けると、別途移動せず、異なる位置から挿入モードへ入ってすぐに入力を始められます。

`Esc` を押すと挿入モードを終了し、ノーマルモードへ戻ります。現在のモードが分からない場合、`Esc` を押せばノーマルモードを確立できます。ただし、処理中の操作が取り消されることはあります。

:::single-choice{#vim-insert-return-normal}
通常、挿入モードからノーマルモードへ戻るキーはどれですか？

::option[`Esc`]{#vim-insert-escape .correct explanation="Escape は現在の挿入を終え、Vim をノーマルモードへ戻します。"}
::option[`Enter`]{#vim-insert-enter explanation="Enter は挿入モードのまま改行を挿入します。"}
::option[`Tab`]{#vim-insert-tab explanation="Tab はインデントを挿入するか、設定済みの補完動作を始めます。通常は挿入モードを終了しません。"}
:::

## カーソルの前または後に挿入する

ノーマルモードでは次を使います。

- `i`：カーソルの前で挿入モードへ入る
- `a`：カーソルの後で挿入モードへ入る

たとえば `abc` の `b` にカーソルがある場合、`i` は `b` の前から、`a` は `b` の後から入力を始めます。どちらのコマンドもモードを変更し、その後に入力するテキストが挿入されます。

:::single-choice{#vim-insert-before-cursor}
カーソルのすぐ前で挿入モードへ入るノーマルモードのキーはどれですか？

::option[`a`]{#vim-insert-a-after explanation="小文字の `a` はカーソルの前ではなく、後から追記します。"}
::option[`o`]{#vim-insert-o-below explanation="小文字の `o` は現在行の下に新しい行を開いてから、挿入モードへ入ります。"}
::option[`i`]{#vim-insert-i-before .correct explanation="小文字の `i` は現在のカーソル位置、つまりその文字の前から挿入を始めます。"}
:::

## 行の境界で挿入する

大文字のコマンドは、現在行の意味のある位置を対象にします。

- `I`：最初の空白以外の文字の前で挿入モードへ入る
- `A`：行末で挿入モードへ入る

インデントされた行では、`I` はインデントを飛ばして最初のテキストの前から始めます。列 0 へ挿入する必要がある場合は `0i` を使います。

:::single-choice{#vim-insert-first-nonblank}
現在行の最初の空白以外の文字の前で挿入を始めるノーマルモードのコマンドはどれですか？

::option[`i`]{#vim-insert-lower-i explanation="小文字の `i` は現在のカーソル位置を使い、最初のテキストへは移動しません。"}
::option[`A`]{#vim-insert-capital-a explanation="大文字の `A` は現在行の末尾から挿入を始めます。"}
::option[`I`]{#vim-insert-capital-i .correct explanation="大文字の `I` は最初の空白以外の文字へ移動し、その前で挿入モードへ入ります。"}
:::

:::single-choice{#vim-append-line-end}
現在行の末尾へ移動し、挿入モードへ入るノーマルモードのコマンドはどれですか？

::option[`A`]{#vim-append-capital-a .correct explanation="大文字の `A` は行末への移動と挿入モードへの切り替えを組み合わせます。"}
::option[`$`]{#vim-move-line-end explanation="ドル記号は行末へ移動しますが、ノーマルモードのままです。"}
::option[`a`]{#vim-append-one-position explanation="小文字の `a` は現在のカーソルの後から始め、行末へは移動しません。"}
:::

## 新しい行を開く

ノーマルモードでは次を使います。

- `o`：現在行の下に新しい行を開き、挿入モードへ入る
- `O`：現在行の上に新しい行を開き、挿入モードへ入る

Vim は現在の設定とファイル形式の規則に従ってインデントを適用します。回数を付けて行を開く操作を繰り返すこともできますが、まず 1 行だけの形式を学び、結果のカーソル位置を予測できるようにしてください。

:::single-choice{#vim-open-line-above}
現在行の上に新しい行を開き、挿入モードへ入るノーマルモードのコマンドはどれですか？

::option[`o`]{#vim-open-lower-o explanation="小文字の `o` は現在行の下に開きます。"}
::option[`O`]{#vim-open-upper-o .correct explanation="大文字の `O` は上に新しい行を開き、そこで挿入を始めます。"}
::option[`A`]{#vim-open-upper-a explanation="大文字の `A` は既存行の末尾へ追記し、上に新しい行は開きません。"}
:::

ノーマルモードと挿入モードを切り替える練習には、次のハンズオンラボを利用してください。

1. **[Vim と Nano で Linux のテキストファイルを編集する](https://labex.io/ja/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)**：vi/vim と nano でファイルの作成、テキスト編集、保存、移動を練習し、Vim のノーマルモードと挿入モードの基本を身に付けます。

## まとめ

これで、新しいテキストを入れたい位置から挿入モードへ入れるようになりました。

1. `Esc` でノーマルモードへ戻る。
2. `i` または `a` でカーソルの前または後に挿入する。
3. `I` または `A` で最初のテキストまたは行末に挿入する。
4. `o` で下に行を開く。
5. `O` で上に行を開く。
