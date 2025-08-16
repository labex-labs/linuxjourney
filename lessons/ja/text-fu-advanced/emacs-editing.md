---
title: "Emacs編集"
description: "Emacsの編集の基本：テキストのナビゲート、カット、効率的なペーストを学びます。この初心者向けのガイドは、LinuxでEmacsの必須コマンドを習得するのに役立ちます。"
keywords: "Emacs, Emacsチュートリアル, Emacsコマンド, テキストエディタ, Linuxエディタ, Emacsナビゲーション, 初心者Emacs, Emacsガイド"
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

Emacsでカット（kill）またはペースト（yank）するには、まずテキストを選択できる必要があります。テキストを選択するには、カットまたはペーストしたい場所にカーソルを移動し、`C-space key`を押します。その後、ナビゲーションキーを使用して、目的のテキストを選択できます。これで、次のようにカットアンドペーストできます。

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
