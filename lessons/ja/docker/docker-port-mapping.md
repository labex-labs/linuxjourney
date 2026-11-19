---
lesson_id: "docker-port-mapping"
course_id: "docker"
lang: "ja"
order_index: 5
title: "ポートマッピング"
description: "コンテナのポートを公開し、手元のブラウザーがアクセスするアドレスを判断する方法を学びます。"
meta_title: "ポートマッピング - Docker"
meta_description: "Docker のポートマッピングを読み、ホスト側とコンテナ側のポートを区別して、接続先の誤りを見つけます。"
meta_keywords: "Docker ポートマッピング, ポート公開, docker run -p, ホスト側ポート, コンテナ側ポート"
---

コンテナ内で Web サーバーが動いていても、ブラウザーから接続できる経路が必要です。**ポート**は、受け取ったネットワーク通信を適切なサービスに渡すための番号です。Docker はホスト側のポートを公開し、そこに来たリクエストをコンテナ内のポートへ転送できます。

## ポートマッピングを読む

この例の Nginx は、コンテナ内のポート 80 で Web リクエストを受け付けます。前の例で作った `web` はポートを公開していません。ここでは新しいコンテナに別の名前を付け、作成時に `-p` でマッピングを指定します。

```bash
$ docker run -d --name published-web -p 127.0.0.1:8080:80 nginx:alpine
```

`8080:80` は**ホスト側ポート**の 8080 から、**コンテナ側ポート**の 80 への転送です。ブラウザーはホスト側に接続し、サーバーはコンテナ側でリクエストを受け取ります。`127.0.0.1` は、ホストが自分自身に接続するときに使うループバックアドレスにマッピングを限定します。

外部から隔離された練習環境を使ってください。Docker Engine 28.0.0 より前のバージョンでは、同じローカルネットワーク区間にある別のマシンから、localhost に公開したポートへ接続できる場合があります。 [Docker のポート公開](https://docs.docker.com/engine/network/port-publishing/)

:::single-choice{#docker-port-mapping-request-target} `127.0.0.1:9090:80` の場合、Docker ホスト上のブラウザーはどのポートに接続しますか？

::option[ホストのポート 9090。]{#docker-port-mapping-target-outer .correct explanation="真ん中の番号が、ブラウザーの接続先となるホスト側ポートです。"}
::option[ホストのポート 80。]{#docker-port-mapping-target-inner explanation="80 はコンテナ内の転送先です。"}
::option[コンテナ内のポート 9090。]{#docker-port-mapping-target-wrong-side explanation="この例では、サーバーはコンテナ内のポート 80 でリクエストを受け取ります。"}
:::

## ホストから試す

Docker がポートを公開したマシンのブラウザーで `http://127.0.0.1:8080` を開きます。Docker が別のマシンで動いている場合、ノートパソコンで `127.0.0.1` と入力しても、そのノートパソコン自身を指します。ブラウザーで利用するラボでは、ラボが案内する方法で接続してください。

:::single-choice{#docker-port-mapping-local-browser} Docker が別の練習用マシンでポート 8080 を公開しました。ノートパソコンのブラウザーに `127.0.0.1` と入力すると、どこを指しますか？

::option[別の練習用マシン。]{#docker-port-mapping-local-lab explanation="そのマシン上でこのアドレスを使った場合にだけ、練習用マシン自身を指します。"}
::option[Docker の Web コンテナ。]{#docker-port-mapping-local-container explanation="ブラウザーは自分が動くマシンのアドレスに接続します。コンテナへの転送にはポートマッピングが必要です。"}
::option[手元のノートパソコン。]{#docker-port-mapping-local-laptop .correct explanation="ループバックはブラウザーが動いているマシンを指します。"}
:::

## Docker が公開したポートを確認する

`docker ps` の `PORTS` 列でマッピングを確認できます。矢印はホスト側のアドレスとポートから、コンテナ側ポートへ向かいます。`/tcp` は、このマッピングで使用するネットワークプロトコルです。

```text
$ docker ps
STATUS         PORTS                   NAMES
Up 2 minutes   127.0.0.1:8080->80/tcp   published-web
```

行に `80/tcp` だけが表示されることもあります。ホスト側のアドレスと矢印がなければ、その行には公開済みのホスト側ポートは表示されていません。

![ホスト側のポート 8080 からコンテナ側のポート 80 への転送と HTTP 200 応答を示す LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-port-mapping/loopback-mapping.png)

この画面では `published-web` だけを表示しています。Docker ホスト上で実行した `curl` で、公開したアドレスから正常な応答が返ることを確かめています。

:::single-choice{#docker-port-mapping-read-listing} 矢印なしで `80/tcp` と表示される行があります。この表示から何が分かりますか？

::option[Docker がホスト側のポート 80 を公開した。]{#docker-port-mapping-listing-host explanation="公開済みのマッピングには、ホスト側ポートとコンテナ側への矢印が表示されます。"}
::option[その行にはコンテナ側のポートだけが表示され、ホスト側の公開ポートは表示されていない。]{#docker-port-mapping-listing-container .correct explanation="この表示が示しているのはコンテナ内のポート 80 です。ホスト側のアドレスも転送の矢印もありません。"}
::option[Docker がホスト側のポート 8080 を公開した。]{#docker-port-mapping-listing-default explanation="この表示にはホスト側ポートの情報がありません。Docker が 8080 と判断することもありません。"}
:::

## 試すアドレスを選ぶ

ページが開かないときは、入力したアドレスとマッピングの矢印の左側を比べます。`Up` と矢印は、それぞれ Docker が何を実行しているか、どこへ転送するかを示します。サーバーがページを実際に返すかは、ブラウザーでリクエストを送って確かめます。

:::single-choice{#docker-port-mapping-correct-misdirected} Docker ホストでポート 8080 にアクセスしてもページが表示されません。行には `127.0.0.1:8081->80/tcp` とあります。次に何を試しますか？

::option[`http://127.0.0.1:80` を開く。]{#docker-port-mapping-misdirected-80 explanation="ポート 80 はマッピングのコンテナ側です。"}
::option[`http://127.0.0.1:8081` を開く。]{#docker-port-mapping-misdirected-8081 .correct explanation="矢印の左側にある、ホストで公開されたポートを使います。"}
::option[`http://127.0.0.1:8080` をもう一度試す。]{#docker-port-mapping-misdirected-8080 explanation="表示上のホスト側ポートは 8081 です。8080 を試してもこのマッピングは確認できません。"}
:::

## まとめ

ポートマッピングを読んで、ブラウザーで使うアドレスを選べるようになりました。

1. ホスト側ポートとコンテナ側ポートを区別する。
2. `127.0.0.1` がどのマシンを指すかを説明する。
3. コンテナの一覧で公開済みのマッピングを見つける。
4. 公開されたホスト側ポートでサービスを試す。
