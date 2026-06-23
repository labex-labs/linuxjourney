---
index: 12
lang: "ja"
title: "mkdir（ディレクトリ作成）"
meta_title: "mkdir（ディレクトリ作成） - コマンドライン"
meta_description: "Linuxのmkdirコマンドを学び、単一ディレクトリの作成、複数ディレクトリの作成、親ディレクトリのネスト作成、権限設定の例を紹介します。"
meta_keywords: "mkdirコマンド, linux mkdir, ディレクトリ作成 linux, ディレクトリ作成コマンド, mkdir -p, mkdir -m, フォルダ作成 linux"
---

## Lesson Content

ファイルを扱う際には、それらをディレクトリに整理する必要があります。この作業の基本的なツールが `mkdir` コマンドで、これは「make directory（ディレクトリを作る）」の略です。

基本的な構文は次の通りです。

```bash
mkdir [OPTIONS] DIRECTORY...
```

### 単一ディレクトリの作成

`mkdir` の最も基本的な使い方は、単一の新しいディレクトリを作成することです。ディレクトリがまだ存在しなければ、このコマンドで現在の場所に作成されます。

```bash
$ mkdir documents
```

### 複数ディレクトリの作成

複数のディレクトリを一度に作成することもできます。名前をスペースで区切って並べるだけです。複数のフォルダを素早く準備する効率的な方法です。

```bash
$ mkdir books paintings
```

### ネストされたディレクトリの作成

時には、ディレクトリとその親ディレクトリを同時に作成したい場合があります。`-p` オプションがこれに最適で、親ディレクトリが存在しなくてもエラーになりません。

```bash
$ mkdir -p books/hemingway/favorites
```

この1つのコマンドで、`books`、`hemingway`、`favorites` がまだ存在しなければ作成されます。

### ディレクトリの権限設定

ディレクトリを作成するときに権限を設定するには `-m` を使います。

```bash
$ mkdir -m 755 public
```

権限については後で詳しく学びますが、この例では所有者が書き込み可能で、他のユーザーは読み取りとディレクトリへの移動ができるディレクトリを作成しています。

### よく使う mkdir オプション

- `-p`：必要に応じて親ディレクトリも作成する。
- `-m MODE`：新しいディレクトリの権限を設定する。
- `-v`：作成したディレクトリごとにメッセージを表示する。

例：

```bash
$ mkdir -pv projects/app/src
mkdir: created directory 'projects'
mkdir: created directory 'projects/app'
mkdir: created directory 'projects/app/src'
```

### よくある質問

**mkdir が「File exists」と言うのはなぜ？** その名前のファイルまたはディレクトリが既に存在しているためです。`ls` コマンドで確認しましょう。

**ネストされたディレクトリはどうやって作るの？** `mkdir -p parent/child/grandchild` を使います。

**mkdir でファイルは作れますか？** いいえ。空のファイルを作るには `touch` を使います。

## Exercise

練習が上達の鍵です！ディレクトリ作成と管理の理解を深めるための実践的なラボを紹介します：

1. **[Linux mkdir コマンド：ディレクトリ作成](https://labex.io/ja/labs/linux-linux-mkdir-command-directory-creating-209739)** - Linuxでの `mkdir` コマンドの使い方を学び、ディレクトリの作成、権限設定、ファイルシステムの整理方法を習得します。基本から応用まで、ネストされたディレクトリの作成もカバーしています。
2. **[新しいプロジェクト構造の設定](https://labex.io/ja/labs/linux-setting-up-a-new-project-structure-387859)** - 特定のプロジェクト構造を作成し、`mkdir` や `cd` などの基本コマンドを使って操作することで、Linuxのディレクトリ管理スキルを実践的に磨きます。

これらのラボで実際のシナリオに概念を適用し、Linuxでのディレクトリ作成と整理に自信をつけましょう。

## Quiz Question

ディレクトリを作成するコマンドは何ですか？小文字の英語コマンドだけで答えてください。

## Quiz Answer

mkdir
