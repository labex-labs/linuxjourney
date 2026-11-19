---
lesson_id: "docker-images"
course_id: "docker"
lang: "ja"
order_index: 2
title: "イメージ"
description: "イメージの参照名を読み、対応するイメージがローカルにあるか確認する方法を学びます。"
meta_title: "イメージ - Docker"
meta_description: "Docker イメージの名前とタグを読み、レジストリとプルの意味を知り、イメージの一覧とコンテナの一覧を区別します。"
meta_keywords: "Docker イメージ, イメージタグ, イメージレジストリ, docker pull, docker image ls"
---

Docker イメージは、プログラムと必要なファイル、既定の設定をまとめたものです。Docker はこれをもとにコンテナを作ります。このレッスンでは、イメージ名を読み、どのイメージがすでに手元にあるかを調べます。

## イメージ名とタグを読む

`nginx:alpine` のうち、`nginx` がイメージ名、`alpine` が**タグ**です。タグは特定のリリースや種類を選ぶための目印です。この例では Alpine Linux を土台にした種類を選んでいます。名前とタグはコロンで区切ります。`nginx:alpine` と `nginx:latest` はイメージ名が同じでも、参照名が異なります。

:::single-choice{#docker-images-read-reference} `busybox:1.36` のどの部分がタグですか？

::option[`busybox`]{#docker-images-reference-name explanation="コロンの前の busybox は名前です。"}
::option[`busybox:1.36`]{#docker-images-reference-whole explanation="参照名全体には、イメージ名とタグの両方が含まれます。"}
::option[`1.36`]{#docker-images-reference-tag .correct explanation="コロンの後ろにあるのが、イメージを選ぶためのタグです。"}
:::

## タグを選ぶ

`nginx` のようにタグを省略すると、Docker は `latest` を使います。これは慣例で決まっているタグ名です。どのイメージを指すかは公開元が決め、後から変更することもできます。`nginx:alpine` と書けば、使いたい種類を指定できます。ただし、そのタグが指すイメージも更新されることがあります。

:::single-choice{#docker-images-default-tag} ある人がタグを付けずに `nginx` を指定し、最新版が選ばれたと思いました。実際に選ばれたのはどれですか？

::option[latest タグが指しているイメージ。]{#docker-images-default-latest .correct explanation="タグを省略すると latest を使います。そのタグがどのイメージを指すかは公開元が決めます。"}
::option[最後に公開された Nginx イメージ。]{#docker-images-default-newest explanation="Docker は latest という名前のタグを使います。公開日時でイメージを並べ替えるわけではありません。"}
::option[使える中で最も小さい Nginx イメージ。]{#docker-images-default-smallest explanation="イメージの大きさで既定のタグが決まるわけではありません。欲しい種類はタグ名で指定します。"}
:::

## イメージをダウンロードする

**レジストリ**は、イメージを保管し、ダウンロードできるようにする場所です。`nginx:alpine` のような参照名の場合、Docker は既定で Docker Hub を使います。現在接続している Docker 環境にイメージをダウンロードするには、`docker pull` を使います。この操作をイメージの**プル**と呼ぶこともあります。

```bash
$ docker pull nginx:alpine
```

コマンドが成功すると、その環境でイメージを使えるようになります。コンテナの起動は別の操作です。ターミナルの例では、`$` がプロンプトを表します。

:::single-choice{#docker-images-pull-result} イメージのプルが成功しました。Docker は何をしましたか？

::option[Web リクエストに応答するコンテナを起動した。]{#docker-images-pull-started explanation="コンテナは起動コマンドを実行したときに動きます。プルはイメージを使えるようにする操作です。"}
::option[その環境でイメージを使えるようにした。]{#docker-images-pull-available .correct explanation="ダウンロードしたイメージをもとに、コンテナを作れるようになります。"}
::option[イメージのコピーをレジストリにアップロードした。]{#docker-images-pull-uploaded explanation="プルでは、レジストリから Docker のローカルストレージへイメージを転送します。"}
:::

## ローカルのイメージを確認する

手元にあるイメージは `docker image ls` で確認できます。例では名前とタグの列だけを表示しています。Docker はイメージ名の列を `REPOSITORY` と表示します。

```text
$ docker image ls
REPOSITORY   TAG
nginx        alpine
busybox      1.36
```

最初の行は `nginx:alpine` です。この表で分かるのは、どのイメージがあるかです。イメージから作ったコンテナの状態は、別の一覧で確認します。

![docker pull と docker image ls の REPOSITORY 列および TAG 列を表示した LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-images/pull-and-list.png)

この画面では、レッスンで使った二つの参照名だけに一覧を絞っています。

:::single-choice{#docker-images-local-list} この出力では、どの参照名のイメージが利用できますか？

::option[`busybox:latest`]{#docker-images-local-busybox-latest explanation="busybox の行のタグは 1.36 です。latest タグの busybox は表示されていません。"}
::option[`busybox:1.36`]{#docker-images-local-busybox .correct explanation="REPOSITORY 列の busybox と、TAG 列の 1.36 を組み合わせます。"}
::option[`nginx:1.36`]{#docker-images-local-nginx-mixed explanation="名前とタグは同じ行から取ります。この 1.36 は busybox の行にあります。"}
:::

## まとめ

イメージの参照名を読み、ローカルの一覧にあるか確認できるようになりました。

1. 参照名の中からイメージ名とタグを見分ける。
2. タグを省略するとどうなるかを説明する。
3. `docker pull` でレジストリからイメージをダウンロードする。
4. `docker image ls` の名前とタグの列を読む。
