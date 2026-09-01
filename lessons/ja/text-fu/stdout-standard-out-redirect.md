---
lesson_id: "stdout-standard-out-redirect"
course_id: "text-fu"
lang: "ja"
order_index: 1
title: "標準出力 (stdout)"
description: "標準出力が端末へ流れる仕組みと、Bash でファイルへリダイレクトする方法を学びます。"
meta_title: "標準出力 (stdout) - Text-Fu"
meta_description: "標準出力 (stdout) と I/O リダイレクトを習得して Linux 学習を始めましょう。このレッスンでは、> および >> 演算子を使用してコマンド出力をファイルにリダイレクトする方法を解説します。これはすべての Linux ユーザーにとって不可欠なスキルです。"
meta_keywords: "Linux, Linux 学習，stdout, 標準出力，I/O リダイレクト，出力リダイレクト，bash, シェルスクリプト，Linux コマンド，Linux チュートリアル"
---

プログラムは入出力ストリームを通じて情報をやり取りします。**stdout** と略される標準出力は、通常の結果を出すためにプログラムが使うストリームです。端末では、シェルが初めにこのストリームを端末表示へ接続します。

## 標準出力へ書き込む

`echo` コマンドは引数を stdout へ書き込みます。

```bash
$ echo Hello World
Hello World
```

stdout はファイル記述子 `1` で、複数のストリームをリダイレクトするときに役立つ番号です。プログラムには標準入力の stdin と標準エラーの stderr もあります。次のレッスンで扱います。

:::single-choice{#stdout-default-destination} リダイレクトなしの場合、対話型端末で `echo Hello World` は通常の出力をどこへ送りますか？

::option[現在のディレクトリにある `stdout` というファイル。]{#stdout-file explanation="標準出力はストリームであり、`stdout` というファイルが自動作成されるわけではありません。ファイルは明示的にリダイレクトした場合だけ使われます。"}
::option[標準出力を通じて端末へ送ります。]{#stdout-terminal .correct explanation="通常、シェルはコマンドの stdout を端末へ接続するため、`echo` の結果がそこへ表示されます。"}
::option[コマンドの標準入力ストリームへ送ります。]{#stdout-to-stdin explanation="標準入力はプログラムへ入るデータを運びます。`echo` は通常の結果を stdout から外へ送ります。"}
:::

## `>` でファイルを置き換える

Bash は `>` を出力リダイレクト演算子として解釈します。コピー先ファイルを開き、コマンドの stdout を接続します。

```bash
$ echo Hello World > peanuts.txt
```

stdout は `peanuts.txt` へ向かうため、テキストは端末に現れません。ファイルがなければシェルが作成し、存在すればコマンドの書き込み前に切り詰めるため、以前の内容は失われます。

`cat` で結果を確認します。

```bash
$ cat peanuts.txt
Hello World
```

:::single-choice{#stdout-replace-file} `notes.txt` にすでにテキストがあります。`echo new > notes.txt` は何をしますか？

::option[ファイル内容を `new` へ置き換えます。]{#stdout-replace-existing .correct explanation="シェルが `>` の既存コピー先を切り詰め、空になったファイルへ `echo` の出力を送ります。"}
::option[既存テキストの後に `new` を追加します。]{#stdout-add-existing explanation="追加には `>>` が必要で、1 つの `>` はコピー先の以前の内容を維持しません。"}
::option[ファイルを変更せず `new` を表示します。]{#stdout-display-only explanation="リダイレクトが stdout を `notes.txt` へ送るため、通常の出力は端末に残りません。"}
:::

シェルはコマンドの実行前にコピー先を開くため、Enter を押す前にパス名を確認してください。綴りを誤ったり、意図しない既存ファイルを指定したりすると、コマンド自体が後で失敗しても切り詰められます。

## `>>` でファイルへ追記する

既存内容の後へ新しい stdout を追加する場合は `>>` を使います。

```bash
$ echo Another line >> peanuts.txt
$ cat peanuts.txt
Hello World
Another line
```

`>` と同じく、`>>` も存在しないコピー先を作成します。既存ファイルの開き方が異なり、`>>` は切り詰めず追記します。

:::single-choice{#stdout-append-file} `status.log` の既存内容を消さず、末尾へ `Finished` を追加するコマンドはどれですか？

::option[`echo Finished > status.log`]{#stdout-truncate-status explanation="1 つの `>` は書き込み前に既存コピー先を切り詰め、以前のログ内容を消します。"}
::option[`echo Finished >> status.log`]{#stdout-append-status .correct explanation="`echo` がテキストを生成し、`>>` がその stdout をコピー先ファイルへ追記します。"}
::option[`cat Finished >> status.log`]{#stdout-cat-filename explanation="これは `cat` に `Finished` というファイルを読ませるもので、要求されたテキストを stdout として生成しません。"}
:::

## リダイレクトを解釈するのはシェル

シェルが `>` と `>>` を認識し、プログラムへ渡す引数から取り除き、ファイルを開いてストリームの接続を準備します。コマンド自体は通常どおり stdout へ書き込むだけです。

したがって、同じリダイレクト構文を多数のコマンドで使えます。

```bash
$ pwd > current-directory.txt
$ ls -la >> directory-list.txt
```

:::single-choice{#stdout-shell-role} `pwd > current-directory.txt` の `>` を通常解釈するのは誰ですか？

::option[`>` を引数として受け取った後の `pwd` コマンド。]{#stdout-pwd-redirection explanation="シェルがリダイレクト構文を消費するため、通常 `pwd` は `>` やコピー先を通常の引数として受け取りません。"}
::option[`pwd` を起動する前の Bash シェル。]{#stdout-bash-redirection .correct explanation="Bash がコマンドの実行前にコピー先を開き、ファイル記述子 1 を接続します。"}
::option[`pwd` が画面へパスを表示した後の端末。]{#stdout-terminal-redirection explanation="出力を書き込む前にストリームがリダイレクトされるため、端末はその stdout を最初から受け取りません。"}
:::

標準ストリームのリダイレクトを練習するには、次のハンズオンラボを利用してください。

1. **[Linux で入出力をリダイレクトする](https://labex.io/ja/labs/comptia-redirecting-input-and-output-in-linux-590840)**：`>`、`>>`、`2>`、`tee` などで stdout、stderr、stdin を操作し、コマンドのデータフローを制御します。

## まとめ

これで置換と追記を混同せず、コマンドの標準出力をリダイレクトできるようになりました。

1. stdout を通常のコマンド結果用ストリームとして認識する。
2. `>` でファイル内容を置き換える。
3. `>>` で既存内容を保持して追記する。
4. シェルがコピー先を開く前に、そのパスを確認する。
