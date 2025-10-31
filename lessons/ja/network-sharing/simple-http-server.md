---
index: 3
lang: "ja"
title: "シンプルな HTTP サーバー"
meta_title: "シンプルな HTTP サーバー - ネットワーク共有"
meta_description: "Python の http.server モジュールを使用して、Linux でシンプルな HTTP サーバーを素早くセットアップする方法を学びます。このガイドでは、ネットワーク全体で簡単にファイルを共有するためのシンプルな Linux ウェブサーバーの作成方法を説明します。"
meta_keywords: "linux シンプル http サーバー, シンプル http サーバー linux, シンプル linux ウェブサーバー, python http.server, python simplehttpserver とは，ファイル共有，ネットワークサーバー"
---

## Lesson Content

Python には、ネットワーク経由でファイルを共有するのに非常に便利な、Web サーバーを即座に作成できる組み込みモジュールがあります。**linux simple http server** のセットアップは、単一のコマンドで完了する簡単なプロセスです。

### Linux でシンプルな HTTP サーバーを起動する

始めるには、ターミナルを使用して共有したいディレクトリに移動します。目的のディレクトリに移動したら、Python 3 を使用している場合は次のコマンドで**simple http server linux**環境を起動できます。

```bash
python -m http.server
```

このコマンドは基本的な Web サーバーを起動し、現在のディレクトリの内容を HTTP 経由でアクセス可能にします。

### Python 2 のレガシーメソッド

まだ Python 2 を使用している古いシステムでは、コマンドが若干異なります。以前はモジュール名が `SimpleHTTPServer` でした。**what is python simplehttpserver** と疑問に思ったことがあるかもしれませんが、それは単に Python 2 における `http.server` モジュールの同等物です。次のコマンドで実行できます。

```bash
python -m SimpleHTTPServer
```

### シンプルな Linux Web サーバーへのアクセス

コマンドを実行すると、**simple linux web server** がアクティブになります。同じネットワーク上の別のマシンから共有ファイルにアクセスするには、Web ブラウザを開き、サーバーを実行しているマシンのローカル IP に `IP_ADDRESS` を置き換えて `http://IP_ADDRESS:8000` に移動します。

同じマシンでファイルを表示するには、localhost アドレス `http://localhost:8000` を使用できます。

## Exercise

練習あるのみです！ネットワーク経由でのファイル共有に不可欠なネットワーク接続と IP アドレス指定の理解を深めるための実践的なラボを以下に示します。

1. **[Linux における IP アドレスタイプと到達可能性の探索](https://labex.io/ja/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - さまざまな IP アドレスタイプを識別し、ネットワーク到達性をテストする練習をします。これは、Python HTTP サーバーがアクセス可能であることを確認するために重要です。
2. **[Linux で MAC アドレスと IP アドレスを識別する](https://labex.io/ja/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` コマンドを使用してマシンの IP アドレスを見つける方法を学びます。これは、別のデバイスから共有ファイルにアクセスする前に必要な手順です。
3. **[Linux でローカルホスト名解決を管理する](https://labex.io/ja/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - /etc/hostsファイルを編集してLinuxでローカルホスト名解決を管理する方法を学びます。これは、Web開発とネットワークテストにおける重要なスキルです。

これらのラボは、概念を実際のシナリオに適用し、Linux での基本的なネットワーク操作に自信をつけるのに役立ちます。

## Quiz Question

Python 3 では、シンプルな HTTP サーバーを作成するために使用されるモジュールの名前は何ですか？（大文字と小文字を区別して英語で回答してください）。

## Quiz Answer

http.server
