---
lesson_id: "compose-service-discovery"
course_id: "docker-compose"
lang: "ja"
order_index: 3
title: "サービスディスカバリ"
description: "Compose のサービス同士が名前で接続する仕組みと、ホストから公開ポートで接続する方法を学びます。"
meta_title: "サービスディスカバリ - Docker Compose"
meta_description: "Compose のサービス同士が名前で接続する仕組みと、ホストから公開ポートで接続する方法を学びます。"
meta_keywords: "サービスディスカバリ, Compose ネットワーク, Docker Compose, DevOps, Linux Journey"
---

Docker ホストのブラウザーは、公開されたアドレスから Web サービスに接続します。プロジェクト内の別のコンテナは、異なる経路を使います。通常、Compose は同じプロジェクトのサービスを共通のネットワークにつなぐので、その中ではサービス名で互いを見つけられます。

## ツール用コンテナからページをリクエストする

`compose.yaml` がある練習用フォルダーに戻ります。前のレッスン以降にツール用コンテナが停止した場合は、`docker compose start toolbox` で再起動します。両方のサービスが起動したら、`docker compose exec` で既存のツール用コンテナ内からコマンドを実行します。BusyBox の `wget` コマンドでページをリクエストします。`-q` は進行状況の表示を抑え、`-O -` はページの内容をターミナルに出力します。

```bash
$ docker compose exec -T toolbox wget -q -O - http://web:80/
```

`-T` オプションは、対話型ターミナルを割り当てない指定です。URL には Web サービス名とコンテナ内のポートが含まれます。成功すると Nginx のページの HTML が返ります。

:::single-choice{#compose-service-discovery-sibling-url} 同じ Compose ネットワークにある別のサービスは、どのアドレスで Web コンテナに接続しますか？

::option[http://web:80/]{#compose-service-discovery-sibling-url-c .correct explanation="共有ネットワークでは web が対象のサービスに解決され、ポート 80 で待ち受けるプログラムに届きます。"}
::option[http://127.0.0.1:8080/]{#compose-service-discovery-sibling-url-a explanation="リクエストを送る側から見たループバックアドレスは、そのサービス自身のネットワーク環境を指します。"}
::option[http://web:8080/]{#compose-service-discovery-sibling-url-b explanation="この例の Web サーバーがネットワーク内で待ち受けるのは、ポート 80 です。"}
:::

![サービス名で Web サービスにリクエストした結果、ツール用コンテナに返った HTML](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-discovery/internal-request.png)

## ホストから使うアドレスを選ぶ

最初のポート割り当てを変えていなければ、Docker ホストで `http://127.0.0.1:8080/` を開きます。前のレッスンでホスト側のポートを変更した場合は、ブラウザーのアドレスにもそのポートを指定します。ツール用コンテナは引き続き `http://web:80/` を使います。Compose ネットワーク内から接続するため、サービス名 `web` が使えるからです。

:::single-choice{#compose-service-discovery-host-url} ホスト側のポートを 8081 に変更したとします。どのアドレスも変更する必要がありますか？

::option[ツール用コンテナがポート 80 の web に接続する URL です。]{#compose-service-discovery-host-url-b explanation="この接続は引き続きコンテナの待ち受けポートに直接届きます。"}
::option[例のアドレスを両方とも変えます。]{#compose-service-discovery-host-url-c explanation="変わったのはホスト側のポートだけです。"}
::option[ホストのブラウザーで使うアドレスです。]{#compose-service-discovery-host-url-a .correct explanation="ブラウザーは、ホストで新たに公開したポートを使って接続します。"}
:::

## 同じサービス名を使い続ける

コンテナを入れ替えると、そのネットワークアドレスが変わることがあります。Compose のサービス名は変わりません。クライアントは同じ名前で改めてアドレスを調べ、再接続できます。入れ替え前のコンテナとの接続は切れることがあります。

:::single-choice{#compose-service-discovery-replacement} 作り直した Web コンテナのアドレスが変わりました。ツール用コンテナは次のリクエストで何を使えますか？

::option[元のコンテナから控えておいた古いアドレスです。]{#compose-service-discovery-replacement-a explanation="新しいコンテナには別のネットワークアドレスが割り当てられることがあります。"}
::option[同じ Web サービス名とコンテナ側のポートです。]{#compose-service-discovery-replacement-b .correct explanation="プロジェクトのネットワーク内で名前を解決すれば、現在のコンテナにアクセスできます。"}
::option[ツール用コンテナ自身のサービス名です。]{#compose-service-discovery-replacement-c explanation="それは、リクエストを送るコンテナを表す名前です。"}
:::

## まとめ

リクエストを送る場所に応じて、使うアドレスを選べるようになりました。

1. プロジェクトのネットワーク内では、サービス名とコンテナ側のポートを使います。
2. ホストのブラウザーでは、公開されたアドレスを使います。
3. コンテナが入れ替わったら、サービス名で改めてアドレスを調べます。
