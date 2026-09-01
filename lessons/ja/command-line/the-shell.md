---
lesson_id: "the-shell"
course_id: "command-line"
lang: "ja"
order_index: 1
title: "シェルとは"
description: "Linux のシェルとは何か、コマンドがどのように実行されるかを学びます。"
meta_title: "シェルとは - コマンドライン"
meta_description: "Linuxシェルとは何か、Bashプロンプトの仕組み、そして初心者向けのコマンド例で最初のコマンドを実行する方法を学びましょう。"
meta_keywords: "linux シェル, bash シェル, コマンドライン, linux ターミナル, シェルプロンプト, echo コマンド, 基本的な linux コマンド"
---

## Linux シェルとは

Linux の学習へようこそ。最初のステップは Linux シェルを理解することです。シェルは、入力したコマンドを受け取り、オペレーティングシステムへ実行を依頼し、その結果を端末へ表示するプログラムです。

グラフィカルユーザーインターフェースを使ったことがあれば、ウィンドウ、メニュー、ボタンをクリックする操作に慣れているでしょう。コマンドラインでは、代わりに正確な指示を入力します。「Terminal」「Console」「Konsole」などのアプリケーションは、通常、シェルセッションを開きます。

端末は入力するためのウィンドウまたはアプリケーションで、シェルはその中で動作するプログラムです。

シェルは高速で、スクリプト化でき、ほぼすべての Linux システムで利用できるため便利です。コマンドを学ぶにつれ、それらを組み合わせてファイルを調べ、ディレクトリを管理し、テキストを検索し、ソフトウェアをインストールし、繰り返し作業を自動化できます。

:::single-choice{#distinguish-shell-and-terminal} 端末とシェルの関係を正しく説明しているものはどれですか？

::option[端末がウィンドウを提供し、その中でシェルが動作します。]{#shell-runs-in-terminal .correct explanation="端末は操作するためのインターフェースで、シェルはその中で動作するコマンド処理プログラムです。"}
::option[端末がコマンドを受け取り、シェルはその出力を表示するだけです。]{#terminal-accepts-commands explanation="役割が逆です。端末がインターフェースを提供し、シェルがコマンドを受け取って実行します。"}
::option[端末とシェルは、同じプログラムを表す 2 つの名前です。]{#terminal-equals-shell explanation="両者は連携しますが、同じプログラムではありません。端末がセッションを開き、その中でシェルが動作します。"}
:::

## Bash シェルと対話する

このコースでは Bourne Again Shell の略である Bash を中心に扱います。Bash は最も一般的な Linux シェルの 1 つで、後で `zsh`、`fish`、そのほかのシェルを使う場合にも良い基礎になります。

端末を開くと、シェルプロンプトが表示されます。外観はさまざまですが、多くの場合はユーザー名、ホスト名、現在のディレクトリを示します。

```plaintext
pete@icebox:/home/pete $
```

`$` 記号は、シェルが通常ユーザーからの入力を待っていることを示します。コマンド入力時にこの記号は入力しません。シェルが表示するものです。`#` が表示されていれば、通常はより強力で危険も大きい root ユーザーとして作業しています。

:::single-choice{#interpret-dollar-prompt} 例のプロンプト末尾にある `$` は何を示しますか？

::option[シェルが root ユーザーの権限で動作しています。]{#root-user-ready explanation="root のプロンプトは通常、`$` ではなく `#` で終わります。root アクセスには追加の権限と危険があります。"}
::option[シェルが通常ユーザーからの入力を待っています。]{#normal-user-ready .correct explanation="`$` は通常ユーザーのプロンプトを表し、シェルがコマンドを受け付ける準備ができていることを示します。"}
::option[次のコマンドはドル記号から始める必要があります。]{#type-dollar-first explanation="`$` はプロンプトの一部です。記号をコピーせず、その後に続くコマンドだけを入力します。"}
:::

コマンドは多くの場合、次の形式を取ります。

```bash
command options arguments
```

たとえば `echo Hello World` では、`echo` がコマンドで、`Hello World` が渡されるテキストです。

:::single-choice{#identify-command-name} `echo Hello World` で、コマンド名はどの部分ですか？

::option[`Hello`]{#hello-command explanation="`Hello` はコマンド名の後にあるため、`echo` へ渡すテキストの一部です。"}
::option[`World`]{#world-command explanation="`World` も `echo` へ渡すテキストで、実行するコマンドの名前ではありません。"}
::option[`echo`]{#echo-command .correct explanation="`echo` は、シェルが実行すべきプログラム名です。その後の単語は引数として渡されます。"}
:::

## 最初の Linux コマンド

初心者向けの最も基本的な Linux コマンドの 1 つ、`echo` から始めましょう。このコマンドは、指定したテキストを端末へ表示します。

```bash
$ echo Hello World
Hello World
```

さらにいくつか試してみます。

```bash
$ echo Linux is fun
Linux is fun
$ echo "Hello from Bash"
Hello from Bash
```

複数の単語を 1 つのテキストとしてシェルに扱わせたいとき、引用符が役立ちます。

:::single-choice{#group-words-with-quotes} `Hello from Bash` を、引用符で囲んだ 1 つのテキストとしてシェルに扱わせるコマンドはどれですか？

::option[`echo "Hello from Bash"`]{#quoted-words .correct explanation="引用符によって 3 つの単語が、`echo` へ渡す 1 つの引数にまとめられます。"}
::option[`echo Hello from Bash`]{#unquoted-words explanation="見える結果は同じですが、引用符がないため、シェルはそれらを別々の引数として扱います。"}
::option[`"echo Hello from Bash"`]{#quoted-command explanation="行全体を引用すると、`echo` とテキストに分けず、その全体を名前とするコマンドを探します。"}
:::

これらのスキルを練習するには、包括的な [シェル学習パス](https://labex.io/ja/learn/shell) を利用してください。

## 初心者向けのヒント

- `Enter` を押してコマンドを実行する
- `上矢印` キーで以前のコマンドを呼び出す
- Linux のコマンドとファイル名では、大文字と小文字が区別される
- 空白には意味がある。`echo hello` と `echohello` は異なる
- コマンドが停止したように見える場合、`Ctrl-C` で取り消せることが多い

## まとめ

これでシェルの役割を説明し、基本的なシェルプロンプトを操作できるようになりました。

1. 端末とシェルを区別する。
2. コマンドプロンプトを識別する。
3. `echo` で簡単なコマンドを実行する。
