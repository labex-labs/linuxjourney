---
lesson_id: "docker-logs-command"
course_id: "docker"
lang: "ja"
order_index: 6
title: "docker logs"
description: "コンテナから収集された出力を読み、次に何を調べるかを決めます。"
meta_title: "docker logs - Docker"
meta_description: "実行中や終了済みのコンテナのログを読み、最近の出力に絞り、アプリケーションのエラーとコンテナの状態を区別します。"
meta_keywords: "docker logs, コンテナログ, Docker のトラブルシューティング, 起動エラー, ログの末尾"
---

`preview` というコンテナが終了しました。コンテナの一覧から状態と終了コードを確認できます。プログラムが何を報告したかを知るには、Docker がそのコンテナから収集した出力を読みます。

## コンテナを選ぶ

`docker logs` にコンテナ名を渡します。停止済みでも、コンテナが残っていて出力が保持されていれば、ログを読めます。この例では、短い処理が停止する前に `/site/title.txt` というファイルを読もうとしました。

```text
$ docker logs preview
cat: can't open '/site/title.txt': No such file or directory
```

ここでファイルを読もうとしたのは `cat` です。メッセージには、コンテナ内で見つからなかったパスが表示されています。

:::single-choice{#docker-logs-command-read-exited} preview と report は同じイメージを使いました。preview の出力を読むコマンドはどれですか？

::option[`docker logs report`]{#docker-logs-command-exited-report explanation="名前はどのコンテナを見るかを指定します。Report は別の実行を指します。"}
::option[`docker logs busybox:1.36`]{#docker-logs-command-exited-image explanation="これはイメージ名です。ログは、そのイメージから作った個々のコンテナに属します。"}
::option[`docker logs preview`]{#docker-logs-command-exited-preview .correct explanation="読みたい出力を持つコンテナの名前を指定しています。"}
:::

## メッセージを状況と合わせて読む

ログには、プログラムが出力したメッセージが残ります。起動メッセージからはリクエストの待ち受けを始めたことが分かります。エラーからは完了できなかった操作が分かることがあります。この例では、`preview` 内のパスが見つかりませんでした。次に、そのコンテナの指定位置にファイルがあるはずだったかを確かめます。メッセージは調べる場所を教えてくれます。

:::single-choice{#docker-logs-command-error-boundary} ファイルがないというメッセージから何が分かりますか？

::option[ホストのどのディレクトリにもファイルがありません。]{#docker-logs-command-error-host-path explanation="プログラムが探したのはコンテナ内のパスです。ホスト上のすべてのファイルを調べた結果ではありません。"}
::option[プログラムは preview 内で指定のファイルを見つけられませんでした。]{#docker-logs-command-error-container-path .correct explanation="このメッセージは preview で動いたプログラムがファイルを探した結果を示します。"}
::option[ホストのブラウザーは公開されていないポートを使いました。]{#docker-logs-command-error-network explanation="メッセージはファイル検索に関するものです。ブラウザーが使ったポートについては何も示していません。"}
:::

## 直近の出力を確認する

出力が多いコンテナでは、`--tail` の後に行数を指定します。Docker は収集した出力の末尾から、指定した行数までを返します。少ない行数から始め、最初のエラーがさらに上にあるときは範囲を広げます。

```bash
$ docker logs --tail 5 web
```

![preview のファイル未検出エラーと web の最後の 5 行を表示した LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-logs-command/preview-and-tail.png)

二つのコマンドは、別々のコンテナを調べています。LabEx では `preview` がファイルを見つけられなかったことを、`web` が Nginx の起動を報告しています。

:::single-choice{#docker-logs-command-tail-choice} web から得られる最新の 2 行だけを読みたいときは、どのコマンドを使いますか？

::option[`docker logs --tail 2 web`]{#docker-logs-command-tail-two .correct explanation="tail 2 を指定すると、このコンテナの出力の末尾から最大 2 行を返します。"}
::option[`docker logs --tail 5 web`]{#docker-logs-command-tail-five explanation="末尾から最大 5 行なので、2 行より多く表示されることがあります。"}
::option[`docker logs web`]{#docker-logs-command-tail-unlimited explanation="行数を指定しない場合、保持されているすべての行が表示されることがあります。"}
:::

## 何も表示されない場合

Docker が表示できるのは収集した出力です。何も出力しないコマンドもあれば、Docker が収集しないファイルにメッセージを書くプログラムもあります。`docker logs` が成功しても何も表示されない場合は、`docker ps -a` で状態を確認しましょう。ログが空というだけではコンテナの状態は分かりません。

:::single-choice{#docker-logs-command-empty-result} cleanup という処理のログは空です。まだ実行中か、すでに終了したかをどのように確認しますか？

::option[Docker に cleanup のログをもっと多く表示させる。]{#docker-logs-command-empty-more-lines explanation="行数を増やしても、何も出力しないプログラムが止まったかどうかは分かりません。"}
::option[cleanup の起動に使ったイメージを探す。]{#docker-logs-command-empty-image explanation="イメージは最初のファイルと設定を示します。コンテナの状態は一覧で確認します。"}
::option[すべてのコンテナの一覧で cleanup の状態を読む。]{#docker-logs-command-empty-container-state .correct explanation="全件の一覧には、実行中のものと、終了後も残っているコンテナの両方が表示されます。"}
:::

## まとめ

コンテナの出力をもとに、次の確認項目を選べるようになりました。

1. コンテナ名を指定し、終了済みのものも含めて収集された出力を読む。
2. プログラムのメッセージを手がかりに、報告された問題を探す。
3. `--tail` で表示する行数を制限する。
4. ログだけでは分からないことを、別の確認方法で調べる。
