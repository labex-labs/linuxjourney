---
index: 5
lang: "ja"
title: "env (環境)"
meta_title: "env (環境) - Text-Fu"
meta_description: "「env」コマンドで Linux 環境変数について学びましょう。PATH、HOME、USER 変数を理解し、Linux 環境を管理するための初心者向けガイドを入手してください。"
meta_keywords: "env コマンド，Linux 環境変数，PATH 変数，Linux チュートリアル，初心者向け Linux, シェル変数，Linux ガイド"
---

## Lesson Content

次のコマンドを実行します。

```bash
echo $HOME
```

ホームディレクトリへのパスが表示されるはずです。私の場合、/home/pete のようになります。

このコマンドはどうでしょうか？

```bash
echo $USER
```

ユーザー名が表示されるはずです！

この情報はどこから来ているのでしょうか？これは環境変数から来ています。これらは次のように入力して表示できます。

```bash
env
```

これにより、現在設定されている環境変数に関する多くの情報が出力されます。これらの変数には、シェルや他のプロセスが使用できる有用な情報が含まれています。

簡単な例を次に示します。

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

特に重要な変数の 1 つは PATH 変数です。これらの変数には、次のように変数名の前に `$` を付けることでアクセスできます。

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
```

これは、コマンドを実行するときにシステムが検索する、コロンで区切られたパスのリストを返します。インターネットからパッケージを手動でダウンロードしてインストールし、非標準のディレクトリに配置して、そのコマンドを実行したいとします。`$ coolcommand` と入力すると、プロンプトに「command not found」と表示されます。それはおかしいです。フォルダー内のバイナリを見て、それが存在することを知っています。何が起こっているかというと、`$PATH` 変数がこのバイナリのそのディレクトリをチェックしないため、エラーが発生しているのです。

そのディレクトリから実行したいバイナリがたくさんあるとします。PATH 環境変数にそのディレクトリを含めるように PATH 変数を変更するだけで済みます。

## Exercise

練習は完璧をもたらします！Linux 環境変数の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux でシェル環境と設定を管理する](https://labex.io/ja/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - ローカル変数と環境変数の作成と管理、継承の理解、`.bashrc` ファイルの変更による設定の永続化を練習します。
2. **[Linux の環境変数](https://labex.io/ja/labs/linux-environment-variables-in-linux-385274)** - 環境変数の概念と使用法、それらの作成、変更、管理方法、およびシステム構成における役割を学びます。
3. **[Linux 環境変数を設定する](https://labex.io/ja/labs/linux-configure-linux-environment-variables-437861)** - Linux システムで環境変数を作成、設定、管理する実践的な経験を積みます。

これらのラボは、実際のシナリオで概念を適用し、Linux シェル環境の管理に自信を築くのに役立ちます。

## Quiz Question

環境変数を表示するにはどうすればよいですか？

## Quiz Answer

env
