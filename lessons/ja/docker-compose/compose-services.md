---
lesson_id: "compose-services"
course_id: "docker-compose"
lang: "ja"
order_index: 2
title: "Compose のサービス"
description: "Compose でサービスを起動し、各コンテナの状態を確認する方法を学びます。"
meta_title: "Compose のサービス - Docker Compose"
meta_description: "Compose でサービスを起動し、各コンテナの状態を確認する方法を学びます。"
meta_keywords: "Compose のサービス, コンテナの状態, Docker Compose, DevOps, Linux Journey"
---

前のレッスンで作った `compose.yaml` を使います。`web` と `toolbox` は、同じ Compose **プロジェクト**に属しています。プロジェクトとは、この設定でまとめて管理するリソースの集まりです。コマンドは練習用フォルダーで実行します。

## プロジェクトを起動する

ポート 8080 が使用中の場合は、`compose.yaml` でホスト側の空いているポートを選びます。例えば Docker コースの `published-web` コンテナは、実行中にポート 8080 を使います。そのコンテナを起動したままにして、8081 が空いていれば Compose の割り当てを `127.0.0.1:8081:80` に変更できます。コンテナ側はポート 80 のままにし、以降のブラウザーからのリクエストでは選んだホスト側のポートを使います。

`docker compose up -d` でサービスをバックグラウンドで起動します。Compose は必要なプロジェクトのリソースを作成し、サービスの設定に従ってコンテナを作成または更新します。

```bash
$ docker compose up -d
```

:::single-choice{#compose-services-project-start} この練習用フォルダーで up -d を実行しました。何が起動するかは、どの設定で決まりますか？

::option[Docker ホストで使えるすべてのイメージです。]{#compose-services-project-start-a explanation="ホストには、このプロジェクトに関係のないイメージも保存できます。"}
::option[すべての停止中のコンテナです。]{#compose-services-project-start-c explanation="Compose は、起動するように指定されたプロジェクトを扱います。"}
::option[指定した Compose ファイル内のサービスです。]{#compose-services-project-start-b .correct explanation="この例では web と toolbox の定義が使われます。"}
:::

## サービスの一覧を読む

`docker compose ps` を使って、このプロジェクトを確認します。サービスの列には YAML ファイルに書いた名前が表示されます。Docker はコンテナにもそれぞれ名前を付けます。コンテナ名にプロジェクト名が含まれることもあります。

```bash
$ docker compose ps
```

`web` と `toolbox` を探し、状態を確認します。コンテナが実行中であれば、確認した時点でプログラムが動いています。Web のレスポンスは、ブラウザーでリクエストを送って別に確かめます。

:::single-choice{#compose-services-compose-list} Compose に web が実行中と表示されました。期待したページが返ることを直接確認するには、何をしますか？

::option[config が表示するサービスの数を数えます。]{#compose-services-compose-list-b explanation="設定のサービス数から Web のレスポンスは分かりません。"}
::option[公開された Web アドレスにアクセスします。]{#compose-services-compose-list-a .correct explanation="リクエストを送ると、実際にページが返るかを確認できます。"}
::option[別のコンテナの名前を確認します。]{#compose-services-compose-list-c explanation="名前はコンテナを識別するもので、サービスの動作は確認できません。"}
:::

![web と toolbox が実行中で、ホストのポート 8080 が公開されている Compose の状態表示](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-services/project-status.png)

スクリーンショットは、変更前のホスト側ポート 8080 を使っています。別のポートを選んだ場合は、割り当てのホスト側にその番号が表示されます。

## 停止したサービスを確認する

ツール用コンテナは一時的に使うものです。待機時間が過ぎるか、手動で停止した場合は、`-a` を付けると Compose の一覧に停止中のコンテナも表示されます。次の例では、Web サービスを実行したまま、このプロジェクトのツール用コンテナを止めます。コースを続けるときは、そのコンテナを再び起動してください。

```bash
$ docker compose stop toolbox
$ docker compose ps -a
$ docker compose start toolbox
```

:::single-choice{#compose-services-stopped-service} toolbox を停止した後、どこで確認できますか？

::option[このプロジェクトで docker compose ps -a を実行した結果です。]{#compose-services-stopped-service-c .correct explanation="このオプションを付けると、プロジェクトの停止中のコンテナも表示されます。"}
::option[イメージの一覧だけです。]{#compose-services-stopped-service-a explanation="プログラムを止めても、コンテナは確認できる状態で残ります。"}
::option[別のプロジェクトのコンテナ一覧です。]{#compose-services-stopped-service-b explanation="toolbox はこのプロジェクトに属します。"}
:::

コンテナや Compose をさらに練習するには、[Docker コマンドの実習](https://labex.io/courses/docker-command-labs)を参照してください。

## まとめ

Compose ファイルを使って、複数のサービスを起動し、状態を確認できるようになりました。

1. 選んだプロジェクトのサービスを起動します。
2. サービス名と現在の状態を確認します。
3. プロジェクトを調べるときは、停止したサービスも表示します。
