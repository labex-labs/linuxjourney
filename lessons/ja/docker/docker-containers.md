---
lesson_id: "docker-containers"
course_id: "docker"
lang: "ja"
order_index: 1
title: "コンテナ"
description: "Docker コンテナの中で何が動くのか、Docker を実行するマシンとコンテナがどう関係するのかを学びます。"
meta_title: "コンテナ - Docker"
meta_description: "小さな Web サーバーを例にコンテナの仕組みを知り、メインのプログラムが起動したり停止したりすると何が変わるかを確認します。"
meta_keywords: "Docker コンテナ, コンテナの基本, Docker ホスト, コンテナのプロセス, Web サーバー"
---

ブラウザーが、Docker 上で動く Web サーバーからページを受け取ります。このサーバーはどこで動いているのでしょうか。停止したらページはどうなるのでしょうか。まず、ブラウザーに応答するプログラムから考えてみましょう。

## コンテナの中で動くプログラム

**Web サーバー**は、ページを求めるリクエストに応答するプログラムです。ブラウザーと `web` という小さな Web サーバーが同じマシン上にあるとします。Docker はサーバーを**コンテナ**の中で実行します。コンテナの中から見えるファイルやリソースは、そこだけのものです。このコースには実行例が用意されているので、Docker をインストールせずに読み進められます。

:::single-choice{#docker-containers-page-request} ブラウザーがページを要求したとき、ページの内容を返すのは何ですか？

::option[コンテナで動いている Web サーバー。]{#docker-containers-page-server .correct explanation="サーバープログラムがリクエストを受け取り、ページを返します。"}
::option[コンテナの起動方法を記述したファイル。]{#docker-containers-page-files explanation="ファイルは起動時の設定に使われます。リクエストに応答するのは、動いているプログラムです。"}
::option[マシン上の Docker コンテナの一覧。]{#docker-containers-page-list explanation="一覧は Docker が何を実行しているかを示します。ページを配信する機能はありません。"}
:::

## コンテナとホスト

コンテナを実行するマシンを**ホスト**と呼びます。Linux 上の Docker で Linux コンテナを動かす場合、コンテナ内のプログラムはそのホスト上のプロセスとして動きます。**プロセス**は実行中のプログラムです。同じホストを複数のコンテナで共有していても、それぞれのコンテナから見えるリソースは限られています。Docker Desktop では、Docker が管理する Linux 仮想マシンの中で Linux コンテナが動きます。

:::single-choice{#docker-containers-shared-host} 二つの Linux コンテナが同じ Linux ホスト上で動いています。このことから何が分かりますか？

::option[両方のコンテナのプログラムから、必ず同じファイルが見えます。]{#docker-containers-host-shared-files explanation="同じホスト上でも、コンテナごとに見えるファイルは異なり得ます。"}
::option[それぞれのプログラムを、そのホスト上の別々のプロセスとして実行できます。]{#docker-containers-host-separate-processes .correct explanation="ホストを共有していても、コンテナ内のプログラムは別々に実行できます。"}
::option[コンテナごとに別の Linux マシンを起動する必要があります。]{#docker-containers-host-separate-machines explanation="コンテナごとにマシンを起動しなくても、一つのホスト上のプロセスとして Linux コンテナを実行できます。"}
:::

## イメージから始める

Docker は**イメージ**からコンテナを作ります。イメージは、プログラムと必要なファイルをまとめたものです。同じ Web サーバーのイメージから `web` と `demo` を作れます。起動すると、同じサーバープログラムがコンテナごとに別のプロセスとして動きます。片方だけを止めることもできます。

:::single-choice{#docker-containers-two-from-image} web が動いている間に demo を停止したら、web はどうなりますか？

::option[demo が再起動するまで一時停止します。]{#docker-containers-two-paused explanation="コンテナごとに別のプログラムが動きます。この例で demo を止めても、web は止まりません。"}
::option[イメージから作り直す必要があります。]{#docker-containers-two-recreate explanation="web は別のコンテナとしてすでに作られており、そのまま動き続けられます。"}
::option[それまでと同じコンテナで動き続けます。]{#docker-containers-two-independent .correct explanation="二つのコンテナは同じイメージをもとに作られましたが、互いに独立して動きます。"}
:::

## 停止の前後でサービスを確かめる

ブラウザーから `web` にリクエストを送れる状態になっているとします。コンテナを止める前はページが返ってきます。停止した後に改めてリクエストを送っても、このサーバーからはページが返りません。イメージは残っているので、別のコンテナを作れます。ページを提供するには、サーバープログラムが動いていて、ブラウザーから接続できる必要があります。コンテナにブラウザーから接続する方法は、後のレッスンで扱います。

:::single-choice{#docker-containers-stopped-server} イメージは残っていますが、web は停止しました。web 自体がもう一度応答するには何が必要ですか？

::option[コンテナのサーバープログラムを再び動かす必要があります。]{#docker-containers-stopped-program .correct explanation="イメージは必要なファイルを提供します。新しいリクエストを処理するのは実行中のサーバープログラムです。"}
::option[ページを配信できるように、イメージに新しい名前を付ける必要があります。]{#docker-containers-stopped-rename explanation="イメージの名前を変えても、停止したサーバーは起動しません。"}
::option[ブラウザーにサーバーイメージのコピーを渡す必要があります。]{#docker-containers-stopped-browser-image explanation="ブラウザーはリクエストを送り、サーバープログラムはコンテナ内で動きます。"}
:::

![コンテナ停止前の HTTP 200 応答と停止後の接続失敗を表示した LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-containers/server-response.png)

この LabEx の例では、`page-demo` というコンテナがページを配信します。最初の `curl` リクエストには HTTP 200 が返ります。コンテナを止めると、新しく送ったリクエストは失敗します。HTTP 応答を受け取れなかったため、curl は `000` と表示します。

## まとめ

コンテナがホスト上でプログラムを実行する仕組みを説明できるようになりました。

1. ブラウザーのリクエストに応答するプログラムを見分ける。
2. 複数のコンテナがホストを共有できることを説明する。
3. 一つのイメージから複数のコンテナを作れることを説明する。
4. 改めてリクエストを送り、以前は接続できたサーバーが今も応答するかを確認する。
