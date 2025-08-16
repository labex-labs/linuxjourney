---
lang: "ja"
title: "Vim の検索パターン"
description: "Vim の検索パターンを学びましょう：順方向 (/) と逆方向 (?) 検索。'n' と 'N' で結果をナビゲートします。今日から Vim スキルを向上させましょう！"
keywords: "Vim 検索，Vim コマンド，Linux テキストエディタ，Vim チュートリアル，Vim ガイド，初心者 Vim"
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

検索キーを試してみてください。`vim [textfile]`で Vim でテキストファイルを開き、検索を開始してください！

## Quiz Question

Vim で検索するために使用されるキーは何ですか？

## Quiz Answer

/
