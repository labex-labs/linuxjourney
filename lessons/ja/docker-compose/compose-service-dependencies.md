---
lesson_id: "compose-service-dependencies"
course_id: "docker-compose"
lang: "ja"
order_index: 6
title: "サービスの依存関係"
description: "依存先を先に起動することと、依存先がリクエストに応答できることの違いを学びます。"
meta_title: "サービスの依存関係 - Docker Compose"
meta_description: "依存先を先に起動することと、依存先がリクエストに応答できることの違いを学びます。"
meta_keywords: "サービスの依存関係, ヘルスチェック, 起動順序, Docker Compose, DevOps, Linux Journey"
---

Web サーバーを使う補助プログラムは、正しい順番で起動しても、最初のリクエストを送るのが早すぎる場合があります。**ヘルスチェック**は、Docker が実行する小さなテストです。例えば、サービスが HTTP リクエストに応答できるかを調べます。

## 応答の準備ができたか確かめる

この例では、Web コンテナの中からヘルスチェックを実行します。コンテナ内の Web ページをリクエストし、成功すれば、その場所からサーバーが応答することを Docker が確認できます。

```yaml
services:
  web:
    image: nginx:alpine
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1/"]
      interval: 3s
      timeout: 2s
      retries: 5
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
    depends_on:
      web:
        condition: service_healthy
```

同じ練習用フォルダーに `compose.health.yaml` として保存します。一定間隔でチェックが実行され、試行ごとに制限時間があります。ここで確認するのは、Web コンテナ内での応答です。

:::single-choice{#compose-service-dependencies-check-location} このヘルスチェックでは、wget はどこで実行されますか？

::option[Web コンテナ内です。]{#compose-service-dependencies-check-location-c .correct explanation="ループバックの URL へは、このコンテナの中からアクセスします。"}
::option[ホストのブラウザーです。]{#compose-service-dependencies-check-location-a explanation="Docker は Web サービスの定義に従ってコマンドを実行します。"}
::option[ツール用コンテナ内です。]{#compose-service-dependencies-check-location-b explanation="ヘルスチェックは web の下で定義されています。"}
:::

## 依存先が正常になるまで待つ

`service_healthy` を指定すると、Compose はヘルスチェックが成功してから、そのサービスに依存するツール用コンテナを起動します。起動順序だけを指定した場合、依存先が実行中になった時点で次のコンテナが起動できます。その時点では、依存先はまだリクエストに応答できないかもしれません。

```bash
$ docker compose -p journey-health -f compose.health.yaml up -d
$ docker compose -p journey-health -f compose.health.yaml ps
```

一覧の web の行が正常を示し、ツール用コンテナが実行中であることを確認します。

:::single-choice{#compose-service-dependencies-ready-condition} Web のプロセスは起動しましたが、コンテナ内からのリクエストはまだ失敗します。ツール用コンテナの起動を待たせるには、どの条件を使いますか？

::option[起動順序だけを指定します。]{#compose-service-dependencies-ready-condition-b explanation="web が先に起動しても、応答できるまでには時間がかかることがあります。"}
::option[バックグラウンドで起動します。]{#compose-service-dependencies-ready-condition-c explanation="バックグラウンド実行では、ターミナルの待機方法が変わります。サービスの準備ができたかどうかは判断しません。"}
::option[service_healthy を指定します。]{#compose-service-dependencies-ready-condition-a .correct explanation="この条件はヘルスチェックの結果を待ちます。"}
:::

![依存先の web が正常で、ツール用コンテナが実行中であることを示す Compose の状態表示](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-dependencies/healthy-dependency.png)

## 起動後の障害に対処する

Compose の起動条件が決めるのは、起動時にサービスを開始する順序です。起動時に正常だったサービスも、後から応答しなくなることがあります。クライアントはリクエスト失敗に対処し、依存先が使えるようになったら再接続できるようにします。現在の状態と直接のリクエストで、今の動作を確認します。

:::single-choice{#compose-service-dependencies-later-failure} 二つのサービスが起動して一時間後に、リクエストが失敗しました。何を調べると役立ちますか？

::option[起動時の順序だけです。]{#compose-service-dependencies-later-failure-a explanation="その順序で分かるのは、起動時に何が起きたかです。"}
::option[現在のヘルスチェックの結果と、依存するサービスから送ったリクエストです。]{#compose-service-dependencies-later-failure-b .correct explanation="これで、サービスの現在の状態と、そのクライアントが使う経路を確認できます。"}
::option[Docker のキャッシュにあるイメージの数です。]{#compose-service-dependencies-later-failure-c explanation="イメージの数では、実行中のサービスからどんな応答が返るかは分かりません。"}
:::

## 二つの場所から確認する

コンテナ内のヘルスチェックが成功しても、分かるのは Web コンテナの内部から何にアクセスできるかです。ツール用コンテナからアクセスするには、プロジェクトのネットワークと、接続に使えるサービスのアドレスが必要です。ヘルスチェックの結果と、ツール用コンテナからのリクエストは別々に確認します。

:::single-choice{#compose-service-dependencies-final-application} ヘルスチェックは正常ですが、ツール用コンテナからのリクエストが失敗します。どの比較が原因の切り分けに役立ちますか？

::option[最初に起動した時刻だけを調べます。]{#compose-service-dependencies-final-application-b explanation="起動時刻では、今どの経路が使えるかは分かりません。"}
::option[web が正常なので、両方のリクエストが成功したと判断します。]{#compose-service-dependencies-final-application-c explanation="ヘルスチェックが示すのは、一つの場所からの結果です。"}
::option[web の中から送ったリクエストと、ツール用コンテナから web に送った同じリクエストを比較します。]{#compose-service-dependencies-final-application-a .correct explanation="サービスの内部で応答できるかと、依存する側が実際に使う経路で応答があるかを比較できます。"}
:::

## まとめ

チェックを使って、依存先が応答できる状態かどうかを判断できるようになりました。

1. ヘルスチェックで実際に何を調べているかを確認します。
2. 起動順序だけでは足りない場合は、依存先の正常性を待つ条件を選びます。
3. 起動後にサービスで障害が起きたら、現在の動作を確認します。
