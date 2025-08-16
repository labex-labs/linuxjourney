---
lang: "ja"
title: "Emacs 編集"
description: "Emacs の編集の基本：テキストのナビゲート、カット、効率的なペーストを学びます。この初心者向けのガイドは、Linux で Emacs の必須コマンドを習得するのに役立ちます。"
keywords: "Emacs, Emacs チュートリアル，Emacs コマンド，テキストエディタ，Linux エディタ，Emacs ナビゲーション，初心者 Emacs, Emacs ガイド"
---

## Lesson Content

### Text Navigation

```
C-up arrow: move up one paragraph
C-down arrow: move down one paragraph
C-left arrow: move one word left
C-right arrow: move one word right
M->: move to the end of the buffer
```

テキストナビゲーションでは、通常のテキストボタン（Home、End、Page Up、Page Down、矢印キーなど）は期待通りに機能します。

### Cutting and Pasting

Emacs でカット（kill）またはペースト（yank）するには、まずテキストを選択できる必要があります。テキストを選択するには、カットまたはペーストしたい場所にカーソルを移動し、`C-space key`を押します。その後、ナビゲーションキーを使用して、目的のテキストを選択できます。これで、次のようにカットアンドペーストできます。

```
C-w: cut
C-y: yank
```

## Exercise

テキストナビゲーションを試してみてください。

## Quiz Question

バッファの末尾に移動するにはどうすればよいですか？

## Quiz Answer

M->
