---
lesson_id: "docker-run-command"
course_id: "docker"
lang: "ja"
order_index: 3
title: "docker run"
description: "docker run でイメージからコンテナを作り、起動する仕組みを学びます。"
meta_title: "docker run - Docker"
meta_description: "docker run の読み方とコンテナの名前の付け方を学び、短い処理とバックグラウンドで動くサーバーを区別します。"
meta_keywords: "docker run, Docker コンテナの起動, コンテナ名, フォアグラウンド, バックグラウンド"
---

Web サーバーのイメージが手元にあります。サーバーを動かすには、`docker run` でイメージからコンテナを作り、起動します。まずはすぐ終わるコマンドを実行して、ターミナルがいつ操作できるようになるかを確認しましょう。

## 短い処理を実行する

BusyBox は、基本的な Linux コマンドを収めた小さなイメージです。下の例では `echo` がメッセージを表示します。イメージの参照名に続けて、コンテナ内で実行するコマンドを書きます。イメージがローカルになければ、通常 Docker がダウンロードします。`$` はターミナルのプロンプトです。イメージのプルが必要な場合、例の行より先にダウンロードの状況が表示されることがあります。

```text
$ docker run busybox:1.36 echo Hello
Hello
```

出力はターミナルに表示されます。`echo` が終了するとコンテナが停止し、プロンプトが戻ります。

:::single-choice{#docker-run-command-short-task} この例でコンテナの中で実行されるのは何ですか？

::option[シェルコマンドとしての `busybox:1.36`。]{#docker-run-command-short-image explanation="BusyBox はコマンドに必要なツールを含むイメージです。実行するコマンドは参照名の後ろにあります。"}
::option[イメージ内のツールを使った `echo Hello`。]{#docker-run-command-short-echo .correct explanation="イメージの参照名の後ろで echo と表示する文字列を指定しています。"}
::option[別の Docker コマンドとしての `docker run`。]{#docker-run-command-short-docker explanation="docker run は手元のターミナルで実行します。このコマンドがコンテナ内の処理を起動します。"}
:::

## コンテナに名前を付ける

後から見分けやすいように、イメージの参照名の前に `--name` を付けてコンテナに名前を付けます。このコマンドでは、短い処理を行うコンテナを `report` と名付けています。

```bash
$ docker run --name report busybox:1.36 echo Ready
```

コンテナは停止しても名前を保持します。同じ Docker 環境で別のコンテナを作るときは、まだ使われていない名前を選びます。

:::single-choice{#docker-run-command-name-choice} Report の処理は終わりましたが、コンテナは残っています。同じイメージから二つ目のコンテナを作るには、何を変えればよいですか？

::option[イメージの参照名はそのままに、コンテナに別の名前を付ける。]{#docker-run-command-name-new .correct explanation="空いている名前を使えば、同じイメージから別のコンテナを作れます。"}
::option[コンテナ名はそのままに、イメージのタグを変える。]{#docker-run-command-name-change-tag explanation="別のイメージを選んでも、元のコンテナはその名前を使い続けています。"}
::option[コンテナ名はそのままに、表示するメッセージを変える。]{#docker-run-command-name-change-message explanation="メッセージは echo への入力です。変更しても report という名前は空きません。"}
:::

## サーバーをバックグラウンドで起動する

イメージには既定のコマンドを設定できます。`nginx:alpine` では、イメージ名の後にコマンドを指定しなければ Web サーバーが起動します。`-d` で**バックグラウンド**実行にすると、サーバーが動いたままプロンプトが戻ります。

```bash
$ docker run -d --name web nginx:alpine
```

Docker は、起動したコンテナを示す長いコンテナ ID を表示します。次のレッスンで、サーバーがまだ動いているかを確認します。

![短い Docker の処理が出力した Hello と Ready、およびバックグラウンドで起動したコンテナの ID を表示した LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-run-command/foreground-and-detached.png)

短い処理はターミナルにメッセージを表示します。サーバーをバックグラウンドで起動したときは、コンテナ ID が返ります。

:::single-choice{#docker-run-command-detach-meaning} Docker が ID を表示し、プロンプトが戻りました。このモードでは何ができますか？

::option[サーバーが終了した後にだけターミナルを操作できる。]{#docker-run-command-detach-wait explanation="バックグラウンドでサーバーが動いている間も、ターミナルを使えます。"}
::option[サーバーを起動せず、イメージだけを用意できる。]{#docker-run-command-detach-skip explanation="バックグラウンドで実行しても、Docker はコンテナを起動します。"}
::option[サーバーが動いている間にターミナルを操作できる。]{#docker-run-command-detach-continue .correct explanation="コンテナを起動した後で、ターミナルに操作が戻ります。"}
:::

## 新しいコンテナを見分ける

`docker run` が成功するたびに、新しいコンテナが作られます。同じサーバーのイメージで空いている名前を指定すると、Docker は二つ目のコンテナを作ります。最初のコンテナの名前と状態は変わりません。

:::single-choice{#docker-run-command-second-instance} web が動いています。demo という名前が空いているとき、`docker run -d --name demo nginx:alpine` は何をしますか？

::option[動いている web の名前を demo に変える。]{#docker-run-command-second-rename explanation="docker run はコンテナを作るコマンドです。元の web の名前は変わりません。"}
::option[イメージに demo というタグを追加する。]{#docker-run-command-second-tag explanation="このオプションはコンテナに名前を付けます。イメージの参照名は nginx:alpine のままです。"}
::option[demo という別のコンテナを起動する。]{#docker-run-command-second-new .correct explanation="Docker はそのイメージから新しいコンテナを作り、demo と名付けます。"}
:::

コンテナの起動と出力の確認を実際に試したい方は、[はじめての Docker ラボ](https://labex.io/labs/docker-your-first-docker-lab-92719)を使ってみてください。

## まとめ

docker run の内容を読み、Docker が何を作るかを判断できるようになりました。

1. イメージと、コンテナ内で実行する任意のコマンドを見分ける。
2. `--name` で、後から見分けられる名前を付ける。
3. 短い処理が終わるとどうなるかを説明する。
4. `-d` を使い、サーバーが動いている間もプロンプトを使う。
