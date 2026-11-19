---
lesson_id: "compose-files"
course_id: "docker-compose"
lang: "ja"
order_index: 1
title: "Compose ファイル"
description: "Compose ファイルからサービス、イメージ、コマンド、ポートを読み取る方法を学びます。"
meta_title: "Compose ファイル - Docker Compose"
meta_description: "Compose ファイルからサービス、イメージ、コマンド、ポートを読み取る方法を学びます。"
meta_keywords: "Compose ファイル, サービス, Docker Compose, DevOps, Linux Journey"
---

Web サーバーと補助プログラムを一度だけ起動するなら、それぞれ別のコマンドでも対応できます。**Compose ファイル**に設定をまとめておくと、同じサービスを後から起動できます。このコースでは、`docker compose` コマンドを使える Compose プラグイン付きの Docker 環境を前提とします。

## 二つのサービスを定義する

新しい練習用フォルダー `journey-compose` を作り、次の内容を `compose.yaml` として保存します。**サービス**は、Compose がコンテナをどのように実行するかを定義します。このファイルでは、Web サーバーと、後の確認で使うために起動したままにする小さなツール用コンテナを定義します。

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
```

インデントにはスペースを使います。`web` の下でインデントされたキーは、そのサービスに属します。`ports` の下のハイフンは、リストの項目の始まりを表します。`command` の角括弧もリストを表し、ここにはプログラム名と引数が入っています。

:::single-choice{#compose-files-service-images} どのサービスが BusyBox イメージを使いますか？

::option[web サービスです。]{#compose-files-service-images-a explanation="web のイメージ指定には nginx と書かれています。"}
::option[toolbox サービスです。]{#compose-files-service-images-c .correct explanation="toolbox の image フィールドには busybox:1.36 と書かれています。"}
::option[両方のサービスです。]{#compose-files-service-images-b explanation="サービスごとにイメージを指定しています。"}
:::

## Web サービスの設定を読む

Web サービスは、コンテナのポート 80 をホストのポート 8080 で公開します。サービスが起動したら、Docker を実行しているマシンから `http://127.0.0.1:8080` にアクセスして Nginx に接続できます。ツール用コンテナはポートを公開しません。`sleep` コマンドで、練習中の 3,600 秒間は起動したままになります。

:::single-choice{#compose-files-mapping-owner} Docker ホストのブラウザーが Nginx に接続する方法は、ファイルのどの部分で決まりますか？

::option[web の下の ports 設定です。]{#compose-files-mapping-owner-a .correct explanation="この設定は、ホストのアドレスとポートを Web コンテナに割り当てます。"}
::option[toolbox の下のイメージタグです。]{#compose-files-mapping-owner-b explanation="これはツール用コンテナのイメージを選ぶ設定です。"}
::option[toolbox の下の sleep の引数です。]{#compose-files-mapping-owner-c explanation="この引数は、そのプログラムの実行時間を決めます。"}
:::

## 読み込まれた設定を確認する

ファイルがあるフォルダーから次のコマンドを実行します。プロンプトを示す `$` より後ろを入力してください。Compose は `compose.yaml` を読み込み、解釈した設定を表示します。`web` と `toolbox` の項目を探します。短く書いた設定は、詳しい形式で表示されることがあります。

```bash
$ docker compose config
```

:::single-choice{#compose-files-config-scope} コマンドは二つのサービスをエラーなく表示しました。何を確認できましたか？

::option[両方のコンテナが起動しました。]{#compose-files-config-scope-a explanation="このコマンドは設定を読み込んで表示するだけです。"}
::option[ブラウザーが正常なレスポンスを受け取りました。]{#compose-files-config-scope-c explanation="サーバーが起動した後でリクエストを試せます。"}
::option[Compose が二つのサービス定義を読み込めました。]{#compose-files-config-scope-b .correct explanation="起動する前に、読み込まれた設定を確認できます。"}
:::

## まとめ

シンプルな Compose ファイルの各部分を見分けられるようになりました。

1. services の下にあるサービス名とイメージの指定を読み取ります。
2. サービスの設定がコンテナのどの部分に対応するかを確認します。
3. docker compose config で読み込まれた設定を確認します。
