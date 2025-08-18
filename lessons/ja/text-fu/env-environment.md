---
lang: "ja"
title: "env (環境)"
meta_title: "env (環境) - テキスト操作"
meta_description: "「env」コマンドを使用して Linux 環境変数について学びます。PATH、HOME、USER 変数について理解します。Linux 環境を管理するための初心者向けガイドを入手してください。"
meta_keywords: "env command, Linux environment variables, PATH variable, Linux tutorial, beginner Linux, shell variables, Linux guide"
---

## Lesson Content

次のコマンドを実行してください。

```bash
echo $HOME
```

ホームディレクトリへのパスが表示されるはずです。私の場合、/home/pete のようになります。

では、このコマンドはどうでしょうか？

```bash
echo $USER
```

あなたのユーザー名が表示されるはずです！

この情報はどこから来ているのでしょうか？それは環境変数から来ています。これらを表示するには、次のように入力します。

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

特に重要な変数の 1 つは PATH 変数です。これらの変数には、次のように変数の前に `$` を付けることでアクセスできます。

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
```

これは、コマンドを実行するときにシステムが検索する、コロンで区切られたパスのリストを返します。インターネットからパッケージを手動でダウンロードしてインストールし、標準以外のディレクトリに配置して、そのコマンドを実行したいとします。`$ coolcommand` と入力すると、プロンプトに「command not found」と表示されます。それはおかしいですね。あなたはフォルダ内のバイナリを見ていて、それが存在することを知っています。何が起こっているかというと、`$PATH` 変数がこのバイナリのそのディレクトリをチェックしないため、エラーをスローしているのです。

そのディレクトリから実行したいバイナリが大量にあるとします。PATH 環境変数にそのディレクトリを含めるように PATH 変数を変更するだけで済みます。

## Exercise

次の出力は何ですか？なぜですか？

```bash
echo $HOME
```

## Quiz Question

環境変数を表示するにはどうすればよいですか？

## Quiz Answer

env
