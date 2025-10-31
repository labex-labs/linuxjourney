---
index: 17
lang: "ja"
title: "whatis とは"
meta_title: "whatis - コマンドライン"
meta_description: "Linux の whatis コマンドを発見しましょう。linux whatis コマンドが他のコマンドの 1 行説明を提供する方法を学び、コマンドラインを操作するための重要なツールであることを理解します。"
meta_keywords: "whatis コマンド linux, whatis linux, linux whatis コマンド，whatis コマンド linux, linux whatis, コマンドライン，linux コマンド"
---

## Lesson Content

Linux コマンドラインを探索するにつれて、膨大な数のコマンドに出会うことになります。特定のコマンドが何をするのか忘れてしまうのは自然なことです。幸いなことに、それを助けるための簡単なユーティリティがあります。

### Linux における whatis コマンドとは

Linux の`whatis`コマンドは、コマンドのマニュアル（man）ページから、そのコマンドの簡潔な 1 行の説明を表示します。これは、man ページ全体を読まずにコマンドの主な機能を素早く思い出すための方法です。**linux whatis**コマンドをターミナルのクイック辞書と考えてください。

### whatis コマンドの使い方

**whatis command linux**の使用は簡単です。`whatis`の後に、知りたいコマンド名を入力するだけです。例えば、`cat`コマンドについて不確かであれば、以下を実行できます。

```bash
whatis cat
```

これにより、「cat - ファイルを連結して標準出力に出力する」のような短い説明が返されます。

### 出力の理解

**linux whatis command**によって提供される説明は、コマンドのマニュアルページの NAME セクションから直接取得されます。これにより、情報が正確であり、システムのドキュメントと一貫していることが保証されます。コマンドが異なるセクションに複数のマニュアルページを持っている場合、`whatis`はそれぞれの行を表示することがあり、そのさまざまなコンテキストを理解するのに役立ちます。

## Exercise

練習あるのみです！`whatis`コマンドに特化したラボはありませんが、コマンドやファイルに関する情報を見つける方法を理解することは非常に重要です。Linux でコマンドやファイルを見つける理解を深めるための実践的なラボを次に示します。

1. **[Linux which コマンド：コマンドの場所特定](https://labex.io/ja/labs/linux-linux-which-command-command-locating-215210)** - `which`コマンドを使用して実行可能ファイルを見つけ、システムの PATH におけるコマンドの優先順位を理解する練習をします。
2. **[Linux whereis コマンド：ファイルとコマンドの検索](https://labex.io/ja/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - `whereis`を使用してコマンドのバイナリ、ソース、マニュアルページを見つけ、コマンドがどのように構成されているかの理解を深めます。
3. **[重要なシステムリソースの発見](https://labex.io/ja/labs/linux-discover-critical-system-resources-388032)** - このチャレンジでは、`which`、`whereis`、`find`を組み合わせて、ファイルシステムを効率的に移動し、重要なシステムリソースを発見するのに役立ちます。

これらのラボは、コマンドとファイル発見の概念を実際のシナリオに応用し、不可欠な Linux ユーティリティに対する自信を築くのに役立ちます。

## Quiz Question

コマンドの簡単な説明を見るには、どのコマンドを使用できますか？小文字に注意して、英語で回答してください。

## Quiz Answer

whatis
