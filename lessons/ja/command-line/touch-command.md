---
lesson_id: "touch-command"
course_id: "command-line"
lang: "ja"
order_index: 5
title: "touch"
description: "`touch` コマンドで空のファイルを作成し、ファイルのタイムスタンプを管理する方法を学びます。"
meta_title: "touch - コマンドライン"
meta_description: "Linuxのtouchコマンドを学び、空ファイルの作成、タイムスタンプの更新、日時設定、参照ファイルの使用、上書き回避の例を紹介します。"
meta_keywords: "linux touch コマンド, touch コマンド, linux ファイル作成, linux タイムスタンプ更新, touch -d, touch -r, touch -c"
---

`touch` コマンドはファイルのタイムスタンプを変更します。また、1 つ以上の空のファイルを作るためにも広く使われます。

基本構文は次のとおりです。

```bash
touch [OPTIONS] FILE...
```

## 空のファイルを作成する

指定したファイルが存在しなければ、`touch` は空のファイルとして作成します。

```bash
$ touch mysuperduperfile
```

各ファイル名を並べると、1 つのコマンドで複数のファイルを作れます。

```bash
$ touch file1.txt file2.txt file3.log
```

これはプレースホルダーの作成に便利ですが、`touch` はファイルへテキストを追加しません。空でないファイルが必要なら、テキストエディタや内容を書き込むための別のコマンドを使ってください。

:::single-choice{#create-several-empty-files} まだ存在しない場合に、`one`、`two`、`three` という 3 つの空ファイルを作るコマンドはどれですか？

::option[`touch "one two three"`]{#touch-one-spaced explanation="引用符により、空白を含む 1 つのファイル名になります。このコマンドが対象にするのは 3 つではなく 1 ファイルです。"}
::option[`mkdir one two three`]{#mkdir-three explanation="`mkdir` は空の通常ファイルではなくディレクトリを作ります。ここでは `touch` を使います。"}
::option[`touch one two three`]{#touch-three .correct explanation="`touch` は複数のファイルオペランドを受け取り、内容を加えず、存在しない各ファイルを作成します。"}
:::

## ファイルのタイムスタンプを更新する

ファイルはいくつかのタイムスタンプを記録します。既定では、既存ファイルに `touch` を実行すると、アクセス時刻と変更時刻の両方が現在時刻に変わり、ファイル内容は変わりません。

コマンドの前後で、表示される変更時刻を比較できます。

```bash
$ ls -l mysuperduperfile
$ touch mysuperduperfile
$ ls -l mysuperduperfile
```

通常、`ls -l` の出力が表示するのは、アクセス時刻ではなく変更時刻です。

:::single-choice{#touch-existing-file} すでに存在する `report.txt` に `touch report.txt` を実行するとどうなりますか？

::option[内容を置き換えず、タイムスタンプが更新されます。]{#timestamps-only .correct explanation="既定の `touch` は既存ファイルのアクセス時刻と変更時刻を更新し、データを上書きしません。"}
::option[内容が削除され、空のファイルになります。]{#contents-deleted explanation="空ファイルを作るのはファイルが存在しない場合です。既存ファイルでは、タイムスタンプを更新しても内容を維持します。"}
::option[ファイル名がすでに使われているため失敗します。]{#existing-error explanation="`touch` は存在しないファイルだけでなく、既存ファイルも操作するよう設計されています。名前が存在するだけではエラーになりません。"}
:::

## 変更するタイムスタンプを制御する

アクセス時刻だけを変更するには `-a`、変更時刻だけなら `-m` を使います。

```bash
$ touch -a notes.txt
$ touch -m notes.txt
```

:::single-choice{#change-modification-time-only} `notes.txt` の変更時刻だけを更新するコマンドはどれですか？

::option[`touch -a notes.txt`]{#access-only explanation="`-a` はアクセス時刻だけを変更し、ここで求める変更時刻は選びません。"}
::option[`touch -m notes.txt`]{#modification-only .correct explanation="`-m` は変更対象を変更時刻に限定し、アクセス時刻を変えません。"}
::option[`touch -c notes.txt`]{#no-create explanation="`-c` は存在しないファイルを作成するか制御し、更新対象を 1 つのタイムスタンプには限定しません。"}
:::

## 時刻を指定またはコピーする

`-d` オプションは現在時刻の代わりに日時文字列を受け取ります。

```bash
$ touch -d "2026-06-23 12:30:00" mysuperduperfile
```

参照ファイルと同じアクセス時刻と変更時刻を設定するには、`-r` を使います。

```bash
$ touch -r file1.txt file2.txt
```

ここでは `file1.txt` がタイムスタンプを提供し、`file2.txt` が変更されます。`-t` オプションでも、短い数値形式で時刻を指定できます。

:::single-choice{#copy-reference-timestamps} `source.txt` のタイムスタンプを `target.txt` へコピーするコマンドはどれですか？

::option[`touch -r source.txt target.txt`]{#reference-source .correct explanation="`-r` では次のオペランドが参照ファイル、最後のオペランドがタイムスタンプを更新するファイルです。"}
::option[`touch -r target.txt source.txt`]{#reference-target explanation="ファイルの役割が逆です。`target.txt` を参照として、`source.txt` を更新します。"}
::option[`touch -d source.txt target.txt`]{#date-source explanation="`-d` は参照ファイル名ではなく日時文字列を受け取ります。別ファイルのタイムスタンプには `-r` を使います。"}
:::

## ファイルを作成しない

通常、指定したパスが存在しなければ `touch` はファイルを作成します。すでに存在する場合だけ更新するには `-c` を追加します。

```bash
$ touch -c existing-file.txt
```

`existing-file.txt` が存在しなければ、このコマンドは作成しません。新しいファイルを導入せずにタイムスタンプを更新したいスクリプトで役立ちます。

:::single-choice{#update-without-creating} `status.log` が存在すれば更新し、存在しなければ作成しないコマンドはどれですか？

::option[`touch -a status.log`]{#touch-access explanation="`-a` はアクセス時刻を選びますが、ファイルがなければ作成されることがあります。必要な作成抑止は行いません。"}
::option[`touch -m status.log`]{#touch-modification explanation="`-m` は変更時刻を選びますが、存在しないファイルの作成を防ぎません。その条件には `-c` を使います。"}
::option[`touch -c status.log`]{#touch-no-create .correct explanation="`-c` は存在しないファイルの作成を抑止し、既存ファイルならタイムスタンプを更新できます。"}
:::

## まとめ

これで `touch` を使い、空のファイルを作成してファイルのタイムスタンプを制御できるようになりました。

1. 1 つ以上の空ファイルを作成する。
2. ファイル内容を変えずにタイムスタンプを更新する。
3. アクセス時刻または変更時刻を選ぶ。
4. 特定の時刻を設定するか、参照ファイルのタイムスタンプをコピーする。
5. 存在しないファイルの作成を防ぐ。
