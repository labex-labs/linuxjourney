---
index: 17
lang: "ja"
title: "whatis コマンド"
meta_title: "whatis - コマンドライン"
meta_description: "Linuxのwhatisコマンドを学び、manページから一行のコマンド説明を取得し、複数のマニュアルセクションを理解する方法を例とともに解説します。"
meta_keywords: "whatis コマンド, linux whatis, コマンド説明 linux, manページ概要, コマンドラインヘルプ, apropos"
---

## Lesson Content

Linuxのコマンドラインを探索していると、膨大な数のコマンドに出会います。特定のコマンドが何をするのか忘れてしまうのは自然なことです。幸いにも、それを助けてくれるシンプルなユーティリティがあります。

### whatis コマンドとは

`whatis` コマンドは、コマンドのマニュアルページから直接、一行の簡潔な説明を表示します。マニュアル全体を読むことなく、コマンドの主な機能を素早く思い出すための方法です。

### whatis コマンドの使い方

`whatis` の使い方は簡単です。`whatis` に続けて知りたいコマンド名を入力します。

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

### 出力の理解

`whatis` が提供する説明は、コマンドのマニュアルページの `NAME` セクションから取得されます。もし同じ名前のマニュアルページが複数のセクションに存在する場合、`whatis` は複数行表示することがあります。

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

括弧内の数字はマニュアルページのセクション番号です。

### whatis と man と apropos の違い

- `whatis ls`: 正確なコマンド名の一行説明を表示します。
- `man ls`: 完全なマニュアルページを開きます。
- `apropos keyword`: キーワードでマニュアルページの説明を検索します。

例えば：

```bash
$ apropos password
```

コマンド名は覚えているが、何をするか忘れたときに `whatis` を使いましょう。

### よくある質問

**なぜ whatis は「nothing appropriate」と表示するのですか？** コマンドのマニュアルページがインストールされていないか、manデータベースの更新が必要な場合があります。

**whatis はコマンドのオプションを表示しますか？** いいえ。オプションは `man COMMAND` または `COMMAND --help` を使って確認してください。

**whatis は which と同じですか？** いいえ。`whatis` はコマンドの説明を表示し、`which` は実行ファイルのパスを表示します。

## Exercise

練習は上達の鍵です！`whatis` コマンド専用のラボはありませんが、コマンドやファイルの情報を見つける方法を理解することは非常に重要です。Linuxでコマンドやファイルを見つける理解を深めるための実践的なラボをいくつか紹介します：

1. **[Linux which コマンド: コマンドの場所特定](https://labex.io/ja/labs/linux-linux-which-command-command-locating-215210)** - `which` コマンドを使って実行ファイルの場所を特定し、システムのPATHにおけるコマンドの優先順位を理解しましょう。
2. **[Linux whereis コマンド: ファイルとコマンドの検索](https://labex.io/ja/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - `whereis` を使ってコマンドのバイナリ、ソース、マニュアルページを見つけ、コマンドの構造を深く理解しましょう。
3. **[重要なシステムリソースの発見](https://labex.io/ja/labs/linux-discover-critical-system-resources-388032)** - `which`、`whereis`、`find` を組み合わせてファイルシステムを効率的にナビゲートし、重要なシステムリソースを見つけるチャレンジです。

これらのラボは、実際のシナリオでコマンドやファイルの発見の概念を応用し、Linuxの基本的なユーティリティに自信を持つのに役立ちます。

## Quiz Question

コマンドの簡単な説明を表示するために使うコマンドは何ですか？小文字に注意して英語で答えてください。

## Quiz Answer

whatis
