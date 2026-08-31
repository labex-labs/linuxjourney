---
lesson_id: "cat-command"
course_id: "command-line"
lang: "ja"
order_index: 7
title: "cat"
description: "`cat` コマンドでファイル内容を安全に表示、連結、リダイレクトする方法を学びます。"
meta_title: "cat - コマンドライン"
meta_description: "Linuxのcatコマンドを学び、ファイルの表示、ファイルの連結、行番号付け、ファイル作成、安全なリダイレクションの使い方を例とともに解説します。"
meta_keywords: "linux cat コマンド, cat コマンド, linux ファイル表示, ファイル連結, cat -n, cat -b, cat リダイレクション, linux cat"
---

ファイルを識別する方法を学んだら、次はその内容を読みましょう。`cat` コマンドはファイルを表示し、その内容を結合します。名前は「concatenate」の略です。

## ファイル内容を表示する

`cat` の最も簡単な使い方は、ファイルを端末へ直接表示することです。

```bash
$ cat myfile.txt
```

コマンドはファイル全体を標準出力へ書き込みます。短いテキストには適していますが、長いファイルは速すぎて画面から流れ去ることがあります。

:::single-choice{#display-short-file}
`myfile.txt` の全内容を端末へ表示するコマンドはどれですか？

::option[`file myfile.txt`]{#classify-myfile explanation="`file` はファイルの種類を推定して報告し、保存されたテキスト全体は表示しません。"}
::option[`touch myfile.txt`]{#update-myfile explanation="`touch` はタイムスタンプを更新するか、存在しないファイルを作り、内容は表示しません。"}
::option[`cat myfile.txt`]{#display-myfile .correct explanation="`cat` は `myfile.txt` を読み、その内容を標準出力へ書き込みます。ここでは標準出力が端末です。"}
:::

## ファイルを連結する

`cat` に複数のファイルを渡すと、オペランドの順に読み、その内容を続けて書き込みます。

```bash
$ cat dogfile birdfile
```

`dogfile` が先、`birdfile` が後に表示されます。結合した出力を新しいファイルへ保存するには、`>` で標準出力をリダイレクトします。

```bash
$ cat dogfile birdfile > animals
```

シェルは `cat` を実行する前に `animals` を作成または切り詰め、そこへ結合した出力を送ります。入力ファイルの 1 つを出力先にすると、`cat` が読む前に空になる可能性があるため、使用しないでください。

:::single-choice{#combine-files-in-order}
`part1` に続けて `part2` を、新規または置換される `whole` ファイルへ書き込むコマンドはどれですか？

::option[`cat whole > part1 part2`]{#reverse-redirection explanation="リダイレクト先は 1 つで、そのほかの単語は `cat` のオペランドになります。要求された入出力順を表しません。"}
::option[`cat part1 part2 > whole`]{#ordered-inputs .correct explanation="`cat` は一覧の順に 2 ファイルを出力し、`>` が結合出力を `whole` へリダイレクトします。"}
::option[`cat part2 part1 > whole`]{#reverse-inputs explanation="同じ 2 入力を `whole` へ書きますが、`part1` より先に `part2` を読みます。オペランドの順序が出力順を制御します。"}
:::

## 端末入力をファイルへ書き込む

入力ファイルを指定しない場合、`cat` は標準入力を読みます。この動作を `>` と組み合わせ、端末から入力したテキストをファイルへ書き込めます。

```bash
$ cat > newfile.txt
```

コマンドの後で目的のテキストを入力します。`Ctrl+D` でファイル終端信号を送り、シェルへ戻ります。`newfile.txt` がすでに存在すると、`>` が以前の内容を切り詰めるため注意してください。

既存内容を置き換えず、新しい入力を追加するには `>>` を使います。

```bash
$ cat >> notes.txt
```

:::single-choice{#append-terminal-input}
既存の `notes.txt` の末尾へ追加するテキストを入力したい場合、ファイルを切り詰めずに操作を始めるコマンドはどれですか？

::option[`cat > notes.txt`]{#overwrite-notes explanation="1 つの `>` は出力先を切り詰めてから入力をリダイレクトするため、`notes.txt` の既存テキストを失います。"}
::option[`cat >> notes.txt`]{#append-notes .correct explanation="`>>` 演算子は出力先を追記用に開き、`cat` が読むテキストを既存内容の後へ追加します。"}
::option[`cat notes.txt > notes.txt`]{#same-input-output explanation="同じファイルを入力と `>` の出力先にすると、`cat` が読む前に切り詰められる可能性があります。安全な追記ではありません。"}
:::

## 出力を整形する

いくつかのオプションで出力を確認しやすくできます。

- `-n`：1 から始め、すべての出力行に番号を付ける
- `-b`：空でない出力行だけに番号を付ける
- `-s`：複数の空行を 1 つの空行へまとめる
- `-A`：非表示文字、タブ、行末を表示する

例を示します。

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

:::single-choice{#number-nonempty-lines}
`notes.txt` の空でない出力行だけに番号を付けるコマンドはどれですか？

::option[`cat -b notes.txt`]{#number-nonblank .correct explanation="`-b` は空でない出力行に番号を付け、空行には番号を付けません。"}
::option[`cat -n notes.txt`]{#number-all-lines explanation="`-n` は空行を含むすべての出力行に番号を付け、空でない行だけという条件を満たしません。"}
::option[`cat -s notes.txt`]{#squeeze-blank-lines explanation="`-s` は連続する空行を 1 つに減らしますが、行番号は追加しません。"}
:::

## 長いファイル用のビューアーを選ぶ

出力全体を一度に必要とする場合は `cat` を使います。長いファイルは、端末へ大量に流さずスクロール、検索、終了できる `less` の方が便利です。

```bash
$ less /var/log/syslog
```

:::single-choice{#choose-viewer-for-long-file}
長いログファイルを対話的に読むのに適したコマンドはどれですか？

::option[`less /var/log/syslog`]{#page-through-log .correct explanation="`less` はスクロール、検索、制御された終了を提供し、長いファイルを対話的に読むのに適しています。"}
::option[`cat /var/log/syslog`]{#print-entire-log explanation="`cat` はログ全体を一度に端末へ書き込み、確認前に画面から流れ去ることがあります。"}
::option[`touch /var/log/syslog`]{#update-log-time explanation="`touch` はタイムスタンプを変え、権限が必要なことがあります。ログを読むコマンドではありません。"}
:::

ファイル内容の表示と結合を練習するには、次のハンズオンラボを利用してください。

1. **[Linux cat コマンド：ファイルの連結](https://labex.io/ja/labs/linux-linux-cat-command-file-concatenating-210986)**：`cat` でテキストファイルを表示、連結、操作する方法を学びます。
2. **[Linux でログと設定ファイルを表示する](https://labex.io/ja/labs/linux-viewing-log-and-configuration-files-in-linux-387914)**：`cat` などでシステムログや設定ファイルを効率よく表示し、必要な情報を取り出します。

## まとめ

これで安全なリダイレクトを選びながら、`cat` でファイル内容を表示、結合できるようになりました。

1. 短いファイルの全内容を表示する。
2. 選んだ順序でファイルを連結する。
3. 出力先の置換または追記を意図的に選ぶ。
4. 行に番号を付けるか、出力を簡略化する。
5. 対話的な読み取りに適する場合は `less` を選ぶ。
