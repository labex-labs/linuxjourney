---
index: 3
lang: "ja"
title: "シンプルな HTTP サーバー"
meta_title: "シンプルな HTTP サーバー - ネットワーク共有"
meta_description: "Python の http.server モジュールを使用してシンプルな HTTP サーバーを作成する方法を学びます。この初心者向けの Linux チュートリアルで、ネットワーク上のファイルを素早く共有しましょう。"
meta_keywords: "http.server, SimpleHTTPServer, Python ウェブサーバー, ファイル共有，Linux チュートリアル，初心者向けガイド"
---

## Lesson Content

Python には、HTTP 経由でファイルを配信するための非常に便利なツールがあります。これは、ネットワーク上の他のマシンがアクセスできるクイックネットワーク共有を作成したい場合に非常に便利です。そのためには、共有したいディレクトリに移動して、以下を実行するだけです。

```bash
python -m http.server
```

または、まだ Python 2 を使用している場合は、次のようになります。

```bash
python -m SimpleHTTPServer
```

これにより、localhost アドレスを介してアクセスできる基本的な Web サーバーがセットアップされます。したがって、これを実行したマシンの IP アドレスを取得し、別のマシンでブラウザで `http://IP_ADDRESS:8000` を使用してアクセスします。自分のマシンでは、Web ブラウザで `http://localhost:8000` と入力することで、利用可能なファイルを表示できます。

## Exercise

練習は完璧をもたらします！ここでは、ネットワーク経由でファイルを共有するために不可欠な、ネットワーク接続と IP アドレスの理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux での IP アドレスの種類と到達可能性を探索する](https://labex.io/ja/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 異なる IP アドレスの種類を特定し、ネットワークの到達可能性をテストする練習をします。これは、Python HTTP サーバーがアクセス可能であることを確認するために重要です。
2. **[Linux で MAC アドレスと IP アドレスを特定する](https://labex.io/ja/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` コマンドを使用してマシンの IP アドレスを見つける方法を学びます。これは、別のデバイスから共有ファイルにアクセスする前に必要な手順です。
3. **[Linux でローカルホスト名の解決を管理する](https://labex.io/ja/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - /etc/hosts ファイルを編集して Linux でローカルホスト名の解決を管理する方法を学びます。これは、Web 開発とネットワークテストのための重要なスキルです。

これらの演習は、実際のシナリオで概念を適用し、Linux での基本的なネットワーク操作に自信をつけるのに役立ちます。

## Quiz Question

Python でシンプルな HTTP サーバーを作成するために使用できるツールは何ですか？

## Quiz Answer

http.server
