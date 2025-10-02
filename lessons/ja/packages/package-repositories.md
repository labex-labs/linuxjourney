---
index: 2
lang: "ja"
title: "パッケージリポジトリ"
meta_title: "パッケージリポジトリ - パッケージ"
meta_description: "Linux のパッケージリポジトリと、それらがソフトウェアをどのように管理するかを学びます。簡単なインストールのために、/etc/apt/sources.list のようなパッケージソースを見つけて追加する方法を発見してください。"
meta_keywords: "Linux パッケージリポジトリ，apt sources list, /etc/apt/sources.list, Linux パッケージ，初心者 Linux, Linux チュートリアル，パッケージ管理"
---

## Lesson Content

インターネットにアップロードされたパッケージは、どのようにして私たちのコンピューターに届くのでしょうか？必要なパッケージごとにダウンロードページにアクセスし、ダウンロードとインストールをクリックしますか？そうすることもできますが、より良い解決策があります。それがパッケージリポジトリです。リポジトリは、パッケージのための中央ストレージの場所です。多くのパッケージを保持する多数のリポジトリがあり、そして何よりも、それらはすべてインターネット上で見つけることができます。面倒なインストールディスクは必要ありません。どこを探すべきかを明示的に指示しない限り、あなたのマシンはこれらのリポジトリがどこにあるかを知りません。

たとえば、自分のマシンに Docker ソフトウェアが欲しいとしましょう。Docker は、コンテナパッケージのために独自のリポジトリを管理しています。このリポジトリ内には、`docker-ce`パッケージ、`docker-ce-cli`パッケージ、`containerd.io`パッケージなど、複数のパッケージがあります。Docker は、このリポジトリを次のソースリンクでホストしています。
`https://download.docker.com/linux/ubuntu`

これで、パッケージを直接ダウンロードするために彼らのウェブサイトに行く代わりに、ソースリンクから Docker ソフトウェアを見つけるようにマシンに指示することができます。

あなたのディストリビューションには、パッケージを取得するための事前に承認されたソースがすでに付属しており、これがシステム上に見られるすべてのベースパッケージをインストールする方法です。Debian システムでは、このソースファイルは`/etc/apt/sources.list`ファイルです。あなたのマシンは、そこを見て、追加したソースリポジトリをチェックすることを知っています。

> **注：** 古い Debian/Ubuntu システムでは、リポジトリは`/etc/apt/sources.list`で構成されますが、新しい Ubuntu バージョン (22.04 以降) では、`ubuntu.sources`のような`/etc/apt/sources.list.d/`内の構造化されたファイルを使用します。どちらの形式も apt によってサポートされています。

## Exercise

練習は完璧をもたらします！ここでは、Linux のパッケージ管理とリポジトリの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Software Installation on Linux](https://labex.io/ja/labs/linux-software-installation-on-linux-18005)** - `sources.list`の概念に直接関連する、apt の使用や.deb ファイルの処理など、Ubuntu システムでソフトウェアをインストールおよび管理するためのさまざまな方法を練習します。
2. **[Installing and Removing Packages](https://labex.io/ja/labs/linux-installing-and-removing-packages-385380)** - Debian ベースのシステムでシステムを更新し、パッケージをインストールおよび削除する方法を学び、パッケージマネージャーがリポジトリとどのように相互作用するかについての理解を固めます。
3. **[Query and Update Packages with YUM in Linux](https://labex.io/ja/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - YUM を使用して RHEL ベースの Linux システムでソフトウェアパッケージを管理する方法を探り、異なるディストリビューション間でのパッケージ管理のより広い視点を提供します。

これらのラボは、パッケージリポジトリとソフトウェア管理の概念を実際のシナリオに適用し、システム管理タスクへの自信を築くのに役立ちます。

## Quiz Question

Debian システムでソースファイルはどこにありますか？

## Quiz Answer

/etc/apt/sources.list
