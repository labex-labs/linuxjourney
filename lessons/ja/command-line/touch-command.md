---
index: 5
lang: "ja"
title: "touch"
meta_title: "touch - コマンドライン"
meta_description: "Linuxのtouchコマンドを学び、空ファイルの作成、タイムスタンプの更新、日時設定、参照ファイルの使用、上書き回避の例を紹介します。"
meta_keywords: "linux touch コマンド, touch コマンド, linux ファイル作成, linux タイムスタンプ更新, touch -d, touch -r, touch -c"
---

## Lesson Content

`touch` コマンドはUnix系OSで標準的に使われるユーティリティです。主な目的はファイルのタイムスタンプを変更することですが、新しい空のファイルを作成するためにもよく使われます。

基本的な構文は以下の通りです。

```bash
touch [OPTIONS] FILE...
```

### 新しいファイルの作成

空のファイルを作成する最も簡単な方法は、`touch` の後にファイル名を指定することです。ファイルが存在しない場合、`touch` はそのファイルを作成します。

```bash
$ touch mysuperduperfile
```

このコマンドを実行すると、現在のディレクトリに `mysuperduperfile` という名前の新しい空ファイルが作成されます。複数のファイルを一度に作成するには、ファイル名を並べて指定します。

```bash
$ touch file1.txt file2.txt file3.log
```

これはプロジェクト構造を設定したり、内容を追加する前にプレースホルダファイルを作成したりする際に便利です。

### ファイルのタイムスタンプの更新

`touch` の元々の機能は、ファイルやディレクトリのアクセス時間と修正時間のタイムスタンプを更新することです。既存のファイルに対して `touch` を使うと、そのファイルのタイムスタンプが現在の時刻に更新されます。

`ls -l` でファイルのタイムスタンプを確認し、`touch` を実行してから再度確認するとわかります。

```bash
# Check the original timestamp
$ ls -l mysuperduperfile

# Update the timestamp
$ touch mysuperduperfile

# Check the new timestamp
$ ls -l mysuperduperfile
```

### 高度なタイムスタンプ制御

`touch` コマンドはより正確なタイムスタンプ操作のためのオプションも提供しています。

`-r` オプションを使うと、参照ファイルのタイムスタンプを別のファイルにコピーできます。

```bash
$ touch -r file1.txt file2.txt
```

`-d` オプションで特定の日付と時刻を設定します：

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

`-c` オプションは、ファイルが既に存在する場合のみ更新したいときに使います。`-c` を使うと、存在しないファイルは作成されません。

```bash
$ touch -c existing-file.txt
```

### よく使う touch オプション

- `-a`: アクセス時間のみを変更する。
- `-m`: 修正時間のみを変更する。
- `-c`: ファイルが存在しない場合は作成しない。
- `-d "DATE"`: 特定の日付文字列を使う。
- `-r FILE`: 他のファイルのタイムスタンプを参照する。
- `-t STAMP`: コンパクトな数値形式のタイムスタンプを使う。

例えば、修正時間のみを変更するには次のようにします：

```bash
$ touch -m notes.txt
```

### よくある質問

**touchはファイルにテキストを追加しますか？** いいえ。`touch` は空のファイルを作成するかタイムスタンプを更新するだけです。テキストを追加するにはエディタや `echo`、`cat` を使ってください。

**touchは既存のファイルを上書きしますか？** いいえ。タイムスタンプを更新しますが、ファイルの内容は置き換えません。

**スクリプトでtouchを使う理由は？** ファイルの存在を素早く保証したり、ある処理が特定の時刻に行われたことを示すための手段として便利だからです。

## Exercise

練習が上達の鍵です！ファイルシステムオブジェクトの作成と管理を強化するためのハンズオンラボを紹介します：

1. **[Linux mkdirコマンド：ディレクトリ作成](https://labex.io/ja/labs/linux-linux-mkdir-command-directory-creating-209739)** - Linuxの`mkdir`コマンドを使ってディレクトリを作成し、権限を設定し、ファイルシステムを整理する方法を学びます。ファイルシステム内の新しいアイテム作成の広い概念を理解するのに役立ちます。
2. **[新しいプロジェクト構造の設定](https://labex.io/ja/labs/linux-setting-up-a-new-project-structure-387859)** - `mkdir`や`cd`などの基本コマンドを使い、特定のプロジェクト構造を作成してナビゲートすることで、Linuxのディレクトリ管理スキルを実践的に磨きます。

これらのラボは、ファイルシステムの作成と整理の概念を実際のシナリオで応用し、Linuxコマンドの自信を深めるのに役立ちます。

## Quiz Question

`myfile` という名前のファイルを作成するにはどうしますか？大文字小文字を区別して、英語のコマンドだけで答えてください。

## Quiz Answer

touch myfile
