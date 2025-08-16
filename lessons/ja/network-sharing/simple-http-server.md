---
title: "シンプルな HTTP サーバー"
description: "Python の http.server モジュールを使用してシンプルな HTTP サーバーを作成する方法を学びます。この初心者向けの Linux チュートリアルで、ネットワーク上でファイルを素早く共有しましょう。"
keywords: "http.server, SimpleHTTPServer, Python web server, ファイル共有，Linux チュートリアル，初心者向けガイド"
---

## Lesson Content

Python には、HTTP 経由でファイルを配信するための非常に便利なツールがあります。これは、ネットワーク上の他のマシンがアクセスできるクイックネットワーク共有を作成したい場合に非常に便利です。そのためには、共有したいディレクトリに移動して、以下を実行するだけです。

```bash
python -m http.server
```

または、まだ Python 2 を使用している場合は、以下を実行します。

```bash
python -m SimpleHTTPServer
```

これにより、localhost アドレスを介してアクセスできる基本的な Web サーバーがセットアップされます。したがって、これを実行したマシンの IP アドレスを取得し、別のマシンでブラウザで `http://IP_ADDRESS:8000` を使用してアクセスします。自分のマシンでは、Web ブラウザで `http://localhost:8000` と入力することで、利用可能なファイルを表示できます。

## Exercise

`http.server` をセットアップしてみてください！

## Quiz Question

Python でシンプルな HTTP サーバーを作成するために使用できるツールは何ですか？

## Quiz Answer

http.server
