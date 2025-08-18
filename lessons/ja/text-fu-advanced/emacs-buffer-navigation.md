---
lang: "ja"
title: "Emacs のバッファナビゲーション"
meta_title: "Emacs のバッファナビゲーション - 高度なテキスト操作"
meta_description: "Emacs のバッファナビゲーションコマンドを学びましょう。この初心者向けの Emacs チュートリアルで、バッファの切り替え、閉じ方、分割を効率的に行い、ワークフローを改善しましょう！"
meta_keywords: "Emacs バッファナビゲーション，Emacs コマンド，C-x b, C-x k, Linux チュートリアル，Emacs ガイド，初心者 Emacs"
---

## Lesson Content

バッファ（または開いているファイル）間を移動するには、以下のコマンドを使用します。

### Switch buffers

```
C-x b - switch buffer
C-x right arrow - right-cycle through buffer
C-x left arrow - left-cycle through buffer
```

### Close the buffer

```
C-x k
```

### Split the current buffer

```
C-x 2
```

これにより、1 つの画面で複数のバッファを表示できます。これらのバッファ間を移動するには、C-x o を使用します。

### Set a single buffer as the current screen

```
C-x 1
```

`screen` や `tmux` のようなターミナルマルチプレクサを使用したことがあるなら、バッファコマンドは非常に馴染み深く感じるでしょう。

## Exercise

バッファを操作してみましょう。

## Quiz Question

バッファを終了するにはどうしますか？

## Quiz Answer

C-x k
