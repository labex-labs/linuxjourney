---
lesson_id: "docker-ps-command"
course_id: "docker"
lang: "ja"
order_index: 4
title: "docker ps"
description: "Docker コンテナを一覧に表示し、実行中と終了済みのコンテナを見分けます。"
meta_title: "docker ps - Docker"
meta_description: "docker ps の出力を読み、docker ps -a で停止したコンテナを探し、名前と終了コードを確認します。"
meta_keywords: "docker ps, Docker コンテナ一覧, 終了済みコンテナ, docker ps -a, コンテナの状態, 終了コード"
---

Docker で起動した Web サーバーはまだ動いているでしょうか。`docker ps` で確かめましょう。イメージはプログラムと必要なファイルをまとめたものです。コンテナは、そのイメージから作ったインスタンスです。このコマンドには、実行した時点でのコンテナの一覧が表示されます。

## 実行中のコンテナを表示する

既定の `docker ps` は実行中のコンテナを一覧にします。サンプルは用意した環境の出力から必要な列だけを抜き出したものです。Docker を用意しなくても読み進められます。ターミナルで試すときは、プロンプトの `$` より後ろのコマンドを入力してください。

```text
$ docker ps
IMAGE         STATUS         NAMES
nginx:alpine  Up 4 minutes   web
nginx:alpine  Up 30 seconds  demo
```

列見出ししか表示されない場合、実行中のコンテナの一覧は空です。同じ環境に停止したコンテナが残っていることはあります。

:::single-choice{#docker-ps-running-list} `docker ps` を実行すると列見出しだけが表示されました。この結果から何が分かりますか？

::option[コンテナの起動に使えるイメージがありません。]{#docker-ps-running-list-images explanation="一覧に出るのはコンテナです。実行中のコンテナがなくても、イメージは存在することがあります。"}
::option[実行中の一覧にコンテナがありません。]{#docker-ps-running-list-empty .correct explanation="既定の一覧には実行中のコンテナが表示されます。停止済みのものは残っている場合があります。"}
::option[調べられる停止済みコンテナはありません。]{#docker-ps-running-list-stopped explanation="既定では停止したコンテナは対象外です。一覧が空でも、停止したコンテナの有無は分かりません。"}
:::

## 名前と状態を読む

まず `NAMES` で目的のコンテナを探します。両方の行の `IMAGE` 列に、同じイメージ `nginx:alpine` が表示されています。右端で `web` を見つけ、同じ行の `STATUS` を読みます。`Up 4 minutes` は、このコンテナが約 4 分間動いているという意味です。

:::single-choice{#docker-ps-name-column} 約 30 秒間動いているコンテナはどの行ですか？

::option[名前が `demo` の行。]{#docker-ps-name-demo .correct explanation="STATUS の Up 30 seconds と同じ行の NAMES に demo があります。"}
::option[名前が `web` の行。]{#docker-ps-name-web explanation="web の行には Up 4 minutes とあります。使っているイメージは同じでも、起動した時刻は異なります。"}
::option[イメージが `nginx:alpine` の両方の行。]{#docker-ps-name-image-reference explanation="状態はコンテナごとに記録されます。同じイメージを使っても、起動時刻が同じになるわけではありません。"}
:::

## 終了済みのコンテナも表示する

あるはずのコンテナが見つからないときは、`docker ps -a` を試します。`-a` は `--all` の短縮形です。停止していても残っているコンテナを表示します。この例には、あらかじめ用意した `preview` という処理も含まれています。

```text
$ docker ps -a
IMAGE         STATUS                         NAMES
nginx:alpine  Up 4 minutes                   web
nginx:alpine  Up 30 seconds                  demo
busybox:1.36  Exited (0) 2 minutes ago       report
busybox:1.36  Exited (1) About a minute ago  preview
```

コンテナでは、Web サーバーやスクリプトなどのメインプログラムが動きます。`Exited` はそのプログラムが終了したという意味です。括弧の数値は**終了コード**で、終了時にプログラムが返した結果を表します。通常、0 は成功、0 以外はエラーを示します。`report` の `Exited (0)` は、処理が正常に終わった場合の表示です。

![実行中と終了済みのコンテナ、report の終了コード 0、preview の終了コード 1 を示す LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-ps-command/running-and-exited.png)

LabEx の画面では、例に出てくる四つのコンテナの名前と状態だけを表示しています。経過時間はコマンドを実行した時刻によって変わります。

:::single-choice{#docker-ps-exit-code-reading} 終了コードから判断して、エラーの有無をどの行で調べますか？

::option[終了しているので `report` の行。]{#docker-ps-exit-code-report explanation="短い処理は、作業が終わると終了します。終了コード 0 は多くの場合、処理が成功したという報告です。"}
::option[実行中の中で起動が最も新しいので `demo` の行。]{#docker-ps-exit-code-demo explanation="Up が示すのは稼働時間です。この行には終了コードがありません。"}
::option[終了コードが 1 なので `preview` の行。]{#docker-ps-exit-code-preview .correct explanation="preview には Exited (1) と表示されます。問題が起きた可能性があるため調べる価値がありますが、状態だけでは原因は分かりません。"}
:::

## 次に確認することを決める

終了コードは調査の手がかりです。`preview` がエラーメッセージを出したか調べるには、`docker logs` の後にコンテナ名を書きます。Docker がそのコンテナから収集した出力が表示されます。

```bash
$ docker logs preview
```

Web サーバーが動いている場合、利用者がページを開けるかどうかも確認できます。実際にアクセスする必要があるコンピューターでページを開きます。`Up` はコンテナ内のプログラムの状態です。ブラウザーからのリクエストが成功すれば、そのコンピューターからページに接続できると分かります。

:::single-choice{#docker-ps-check-visitor-access} Docker が動くコンピューターではページを開けます。同僚は別のコンピューターから開く必要があります。どの確認で判断できますか？

::option[同僚のコンピューターからページを開く。]{#docker-ps-next-check-visitor-browser .correct explanation="同僚が実際に使う接続経路をテストできます。"}
::option[Docker が動くコンピューターで `docker ps` をもう一度実行する。]{#docker-ps-next-check-status-again explanation="一覧で web の稼働は確認できます。同僚のコンピューターからの接続は、そこでリクエストを送って確かめます。"}
::option[Docker が動くコンピューターで、もう一度ページを開く。]{#docker-ps-next-check-host-browser explanation="同じ場所での確認を繰り返すだけです。同僚の接続では結果が異なる可能性があります。"}
:::

## まとめ

一覧からコンテナを見つけ、状態を読み、次に何を確認するかを決められるようになりました。

1. `docker ps` で実行中のコンテナを表示する。
2. 名前を手がかりにコンテナを探し、その状態を読む。
3. `docker ps -a` で終了済みのコンテナも表示する。
4. 状態だけで判断できないときは、ログやブラウザーのリクエストで確かめる。
