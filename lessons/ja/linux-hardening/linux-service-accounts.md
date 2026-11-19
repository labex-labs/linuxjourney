---
lesson_id: "linux-service-accounts"
course_id: "linux-hardening"
lang: "ja"
order_index: 2
title: "サービスアカウント"
description: "Linux プロセスを実行しているアカウントを特定し、そのアクセス権限を考える方法を学びます。"
meta_title: "サービスアカウント - Linux の堅牢化"
meta_description: "Linux プロセスを実行しているアカウントを特定し、そのアクセス権限を考える方法を学びます。"
meta_keywords: "サービスアカウント, プロセス, Linux の堅牢化, サイバーセキュリティ, Linux Journey"
---

Web サーバーを起動すると、プロセスとして動作します。Linux は各プロセスをアカウントに関連付け、そのプログラムが何を読んだり変更したりできるかの判断に使います。**サービスアカウント**とは、プログラムの実行用に用意されたアカウントです。

## プロセスの実行ユーザーを調べる

通常の端末では、`$$` でシェルのプロセス ID を取得できます。これを使って、自分のシェルの実行ユーザーを確認します。`-p` オプションでそのプロセスを選び、`-o` で表示する列を選びます。等号を付けると列の見出しを省略できます。

```bash
$ ps -p "$$" -o user=,comm=
```

LabEx の端末では、アカウントは `labex` になっていることがあります。コマンドの列にはシェルプログラムの名前が表示されます。サービスのプロセスについて同じ列を見れば、起動した人にかかわらず、実行に使われているアカウントが分かります。

:::single-choice{#linux-service-accounts-process-user} 選んだプロセスに関連付けられたアカウントは、どのフィールドで分かりますか？

::option[-p に渡したプロセス ID です。]{#linux-service-accounts-process-user-a explanation="プロセス ID は稼働中の一つのプロセスを選ぶために使われます。"}
::option[最後の列にあるコマンド名です。]{#linux-service-accounts-process-user-c explanation="そこで分かるのは実行中のプログラム名です。"}
::option[ps が表示するユーザーのフィールドです。]{#linux-service-accounts-process-user-b .correct explanation="ユーザーのフィールドには、そのプロセスの実行ユーザーが表示されます。"}
:::

![LabEx のシェルプロセスと実行ユーザー labex を示す ps の出力](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-service-accounts/shell-identity.png)

## 専用アカウントを選ぶ

ページを読み取り、自身のログに書き込むだけの Web サービスを考えます。専用の `site-web` アカウントに、この二つの権限を与えられます。幅広い権限を持つ管理者として実行すると、そのプログラムは必要以上にホストを変更できるようになります。

:::single-choice{#linux-service-accounts-isolate-service} そのサービスの作業に合う権限の与え方はどれですか？

::option[site-web が全ユーザーのファイルを編集できるようにします。]{#linux-service-accounts-isolate-service-b explanation="サービスの作業にそこまで広い権限は必要ありません。"}
::option[site-web がページを読み、自分のログに書き込めるようにします。]{#linux-service-accounts-isolate-service-a .correct explanation="二つの権限が、説明された二つの作業に対応しています。"}
::option[site-web がすべてのリクエストを管理者として処理できるようにします。]{#linux-service-accounts-isolate-service-c explanation="ほとんどのリクエストは、サービス用の限定された権限で処理できます。"}
:::

## 複数のプロセスを確認する

サービスによっては、役割ごとに異なるプロセスを使います。適用される権限を説明する前に、実際にリクエストを処理するプロセスを調べます。実行ユーザーを変更したら、サービスが引き続き入力を読み、必要な対象にだけ書き込めるか確認します。

:::single-choice{#linux-service-accounts-verify-identity} 保守ツールによると、管理プロセスは root として動作しています。Web リクエストを処理するアカウントは、どうすれば分かりますか？

::option[リクエストを処理するワーカープロセスの実行ユーザーを確認します。]{#linux-service-accounts-verify-identity-c .correct explanation="対象プロセスを調べると、アカウントと実際の処理を対応付けられます。"}
::option[サービス設定のファイル名だけを確認します。]{#linux-service-accounts-verify-identity-a explanation="ファイル名からは、稼働中のワーカーの実行ユーザーは分かりません。"}
::option[端末を開いた人の名前を確認します。]{#linux-service-accounts-verify-identity-b explanation="端末のユーザーとサービスの実行ユーザーは異なる場合があります。"}
:::

## まとめ

Linux プロセスと、その実行に使われるアカウントを対応付けられるようになりました。

1. ps の出力でプロセスのユーザーを確認します。
2. サービスの作業に合う権限を選びます。
3. 複数のプロセスがあるサービスでは、対象の作業を担当するプロセスを調べます。
