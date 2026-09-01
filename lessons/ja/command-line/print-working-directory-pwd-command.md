---
lesson_id: "print-working-directory-pwd-command"
course_id: "command-line"
lang: "ja"
order_index: 2
title: "pwd（作業ディレクトリの表示）"
description: "`pwd` を使って Linux ファイルシステム内の現在位置を確認する方法を学びます。"
meta_title: "pwd（作業ディレクトリの表示） - コマンドライン"
meta_description: "Linuxのpwdコマンドについて学び、作業ディレクトリの意味や絶対パスがファイルシステム内の現在位置を示す方法を理解しましょう。"
meta_keywords: "pwdコマンド, linux pwd, 作業ディレクトリの表示, 現在のディレクトリ linux, 絶対パス, linux ファイルシステム, ディレクトリツリー"
---

Linux では、ファイルとディレクトリはファイルシステムと呼ばれる階層に整理されています。迷わず移動するには、まず自分がどこにいるかを知る必要があります。`pwd` コマンドは、現在の作業ディレクトリを表示して、その問いに答えます。

## Linux のディレクトリツリー

ファイルシステム全体は、ルートディレクトリと呼ばれる 1 つの最上位ディレクトリから始まります。ルートはスラッシュ（`/`）で表します。ルートからディレクトリツリーがサブディレクトリへ枝分かれし、その中にファイルやさらに別のサブディレクトリを置けます。

簡略化した構造は次のようになります。

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

:::single-choice{#identify-root-subdirectories} 上のディレクトリツリーで、`home` と `etc` は `/` とどのような関係にありますか？

::option[`/` から枝分かれするサブディレクトリです。]{#root-subdirectories .correct explanation="どちらもツリー内で `/` の直下にあります。ファイルシステムはルートからサブディレクトリへ枝分かれします。"}
::option[`bin` ディレクトリ内に保存されたファイルです。]{#files-inside-bin explanation="ツリーでは `home` と `etc` は `bin` の中ではなく、同じ階層にあります。この例ではファイルではなくディレクトリです。"}
::option[ルートディレクトリの別名です。]{#alternate-root-names explanation="Linux のファイルシステムルートは `/` で表す 1 つだけです。`home` と `etc` はその下にあるディレクトリです。"}
:::

## ファイルパスを理解する

ファイルやディレクトリの場所はパスで表します。パスは、ある出発点から特定の目的地までをたどるディレクトリの並びです。

たとえば、`/home` の中に `pete` フォルダーがあり、さらにその中に `Movies` フォルダーがある場合、完全なパスは次のとおりです。

```plaintext
/home/pete/Movies
```

`/` で始まるパスは、ルートディレクトリから始まるため絶対パスです。`Movies` のようなパスは現在位置によって意味が変わるため、相対パスです。

:::single-choice{#recognize-absolute-path} `/home/pete/Movies` が絶対パスである理由は何ですか？

::option[`/` で区切られた複数のディレクトリ名を含むから。]{#contains-directories explanation="絶対パスと相対パスのどちらも複数のディレクトリ名を含められます。種類を決めるのは名前の数ではなく出発点です。"}
::option[`Movies` という名前のディレクトリで終わるから。]{#ends-with-movies explanation="目的地の名前によって絶対パスかどうかは決まりません。絶対パスはルートから始まることで識別します。"}
::option[先頭の `/` でルートから始まるから。]{#starts-at-root .correct explanation="絶対パスはルートディレクトリから始まります。先頭の `/` がその出発点を示します。"}
:::

## Linux の PWD は何の略か

`pwd` は「print working directory」の略です。作業ディレクトリとは、現在シェルがいるディレクトリです。相対パスを使うコマンドは、この場所を出発点にします。

:::single-choice{#expand-pwd-name} `pwd` は何の略ですか？

::option[Print working directory]{#print-working-directory .correct explanation="名前が表すとおり、シェルの現在の作業ディレクトリを表示するコマンドです。"}
::option[Present working directory]{#present-working-directory explanation="日常会話では現在位置を present directory と呼べますが、`pwd` の展開ではありません。"}
::option[Print whole directory]{#print-whole-directory explanation="`pwd` は現在のディレクトリのパスを報告し、ディレクトリ内容全体は表示しません。"}
:::

## `pwd` コマンドを使う

現在のディレクトリを確認するには、`pwd` と入力して Enter を押します。

```bash
$ pwd
/home/pete
```

出力は絶対パスです。この例では、シェルは現在 `pete` ユーザーのホームディレクトリにいます。

ユーザー名、ホームディレクトリ、現在位置は異なる場合があるため、実際の出力もシステムによって変わります。`pwd` は情報を表示するだけで、作業ディレクトリは変更しません。一方、`cd` はシェルの作業ディレクトリを変更します。

:::single-choice{#check-location-without-changing-it} 現在のディレクトリを変更せずに確認する操作はどれですか？

::option[`cd` を実行し、移動先のディレクトリを読む。]{#run-cd explanation="`cd` は作業ディレクトリを変更するため、場所を変えずに確認するという要件を満たしません。"}
::option[`/home/pete` と入力し、そのパスをコマンドとして使う。]{#run-path explanation="絶対パスは場所を識別しますが、パス自体は現在のディレクトリを報告するコマンドではありません。"}
::option[`pwd` を実行し、表示される絶対パスを読む。]{#run-pwd .correct explanation="`pwd` はシェルを移動せず現在位置を報告するため、どこにいるか確認したいとき安全に使えます。"}
:::

## `pwd` が役立つ場面

次のような場合に `pwd` を使います。

- 手順に従っていて、現在位置を確認する必要がある
- ファイルパスが誤っていてコマンドが失敗した
- 複数のディレクトリを移動し、自分の場所が分からなくなった
- 現在のディレクトリパスを別のコマンドへコピーしたい

たとえば、次のようにします。

```bash
$ pwd
/home/pete/projects
$ ls
app.py  README.md
```

これにより、`app.py` と `README.md` が `/home/pete/projects` にあると分かります。

Linux ファイルシステムの移動と現在位置の確認を身に付けるには、次のハンズオンラボを利用してください。

1. **[Linux pwd コマンド：ディレクトリの表示](https://labex.io/ja/labs/linux-linux-pwd-command-directory-displaying-209734)**：`pwd` コマンドの概要と実践的な使い方を学びます。
2. **[Linux のディレクトリ移動](https://labex.io/ja/labs/linux-directory-navigation-387844)**：さまざまなディレクトリを移動し、パスとファイルシステム構造の理解を深めます。
3. **[Linux cd コマンド：ディレクトリの変更](https://labex.io/ja/labs/linux-linux-cd-command-directory-changing-209733)**：`cd` で効率よくファイルシステムを移動する方法を学びます。

## まとめ

これで `pwd` を使い、Linux ファイルシステム内の現在位置を確認できるようになりました。

1. ディレクトリツリーのルートを識別する。
2. 絶対パスと相対パスを区別する。
3. `pwd` の意味と報告内容を説明する。
4. 作業ディレクトリを変更せず確認する。
