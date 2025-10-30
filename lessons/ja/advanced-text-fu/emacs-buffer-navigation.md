---
index: 11
lang: "ja"
title: "Emacs バッファナビゲーション"
meta_title: "Emacs バッファナビゲーション - 高度なテキスト操作"
meta_description: "Emacs のバッファナビゲーションコマンドを学びましょう。この初心者向け Emacs チュートリアルで、バッファの切り替え、閉じ方、分割を効率的に行い、ワークフローを改善しましょう！"
meta_keywords: "Emacs バッファナビゲーション，Emacs コマンド，C-x b, C-x k, Linux チュートリアル，Emacs ガイド，初心者 Emacs"
---

## Lesson Content

バッファ（または現在開いているファイル）間を移動するには、以下のコマンドを使用します。

### バッファの切り替え

```
C-x b - switch buffer
C-x right arrow - right-cycle through buffer
C-x left arrow - left-cycle through buffer
```

### バッファを閉じる

```
C-x k
```

### 現在のバッファを分割する

```
C-x 2
```

これにより、複数のバッファを 1 つの画面で表示できます。これらのバッファ間を移動するには、C-x o を使用します。

### 単一のバッファを現在の画面として設定する

```
C-x 1
```

`screen` や `tmux` のようなターミナルマルチプレクサを使用したことがあるなら、バッファコマンドは非常に馴染み深く感じるでしょう。

## Exercise

練習は完璧をもたらします！テキストファイルとバッファのナビゲーションと操作の理解を深めるための実践的な演習をいくつか紹介します。

1. **[Vim と Nano で Linux のテキストファイルを編集する](https://labex.io/ja/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - バッファを扱う上で不可欠な Vim および Nano エディタ内でのテキストの作成、編集、保存、ナビゲーションを練習します。
2. **[Linux cat コマンド：ファイルの連結](https://labex.io/ja/labs/linux-linux-cat-command-file-concatenating-210986)** - テキストファイルの表示、連結、操作を学び、バッファコンテンツとどのようにやり取りするかを直接応用します。
3. **[Linux でのログファイルと設定ファイルの表示](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `cat`、`more`、`less`などのコマンドを使用してテキストファイルを効率的に表示およびナビゲートする練習をし、バッファのようなコンテンツを調べる実際のシナリオをシミュレートします。

これらの演習は、実際のシナリオで概念を適用し、Linux でのテキストファイルとバッファの操作に自信をつけるのに役立ちます。

## Quiz Question

バッファを終了するにはどうすればよいですか？

## Quiz Answer

C-x k
