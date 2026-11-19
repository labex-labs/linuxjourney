---
lesson_id: "deployment-health-checks"
course_id: "deployment"
lang: "ja"
order_index: 4
title: "ヘルスチェック"
description: "デプロイ後にプロセス、サービス、クライアントからの実際の応答を確認する方法を学びます。"
meta_title: "ヘルスチェック - デプロイ"
meta_description: "デプロイ後にプロセス、サービス、クライアントからの実際の応答を確認する方法を学びます。"
meta_keywords: "ヘルスチェック, バージョン確認, デプロイ, DevOps, Linux Journey"
---

起動したばかりのプログラムは、実行中でもまだリクエストに応答できないことがあります。何を確認できたかが分かるように、サービスを段階ごとに確認します。

## プロセスを確認する

コンテナの一覧から、メインのプログラムが実行中かどうかを確認できます。デプロイ後にまず確認する大事な点です。初期化が完了したか、ブラウザーが接続できるかは、別に調べる必要があります。

:::single-choice{#deployment-health-checks-process-scope} 新しいコンテナに Up と表示されています。何が分かりますか？

::option[利用者に新しいページが確実に表示されています。]{#deployment-health-checks-process-scope-a explanation="コンテナの状態だけでは、利用者が送ったリクエストの結果は分かりません。"}
::option[確認時点で、コンテナのメインプログラムが実行中です。]{#deployment-health-checks-process-scope-b .correct explanation="Up はプロセスの状態を示します。"}
::option[すべての依存先がチェックに合格しました。]{#deployment-health-checks-process-scope-c explanation="ここには、依存先のチェック結果は表示されていません。"}
:::

## サービスのエンドポイントを確認する

**エンドポイント**は、サービスがリクエストを受け付けるアドレスとパスの組み合わせです。確認したい動作に合うパスを選びます。手元で試すには、空の練習用フォルダーを使います。リダイレクトでバージョンファイルを書き出します。このターミナルで Python サーバーをループバックアドレスで起動したままにし、練習後に Ctrl+C で停止します。

```bash
$ mkdir site
$ printf '%s\n' 2 > site/version.txt
$ python3 -m http.server 8091 --bind 127.0.0.1 --directory site
```

別のターミナルからバージョンファイルをリクエストします。curl の `-f` は HTTP エラーレスポンスを失敗として扱います。`-sS` は進行状況の表示を抑え、エラーは引き続き表示します。

```bash
$ curl -fsS http://127.0.0.1:8091/version.txt
```

この練習の期待値は `2` です。バージョンファイルへのリクエストで確認できるのは、サイト全体の動作の一部です。

:::single-choice{#deployment-health-checks-endpoint-mismatch} リクエストが成功し、1 が表示されました。何を調べますか？

::option[そのアドレスで、どのバージョンが応答しているかです。]{#deployment-health-checks-endpoint-mismatch-a .correct explanation="接続には成功しましたが、返されたバージョンが想定と異なります。"}
::option[curl が接続できない理由です。]{#deployment-health-checks-endpoint-mismatch-b explanation="値が返っているので、接続でき、レスポンスも受け取れています。"}
::option[サービス名に数字が含まれるかです。]{#deployment-health-checks-endpoint-mismatch-c explanation="サービス名では、返されたバージョンは分かりません。"}
:::

![LabEx の練習用サーバーのループバック上にあるバージョン用エンドポイントが 2 を返した例](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-health-checks/version-response.png)

## クライアントと同じ場所から確認する

サービスのホストからのリクエストが成功したら、次は利用者が普段アクセスする場所から、安全に実行できるチェックを繰り返します。ロードバランサー、プロキシ、ネットワークルールによって、接続経路が変わることがあります。調べたアドレスと応答を記録します。結果がリリースと一致しない場合は、デプロイの調査を続けます。

:::single-choice{#deployment-health-checks-user-path} ローカルのリクエストは 2 を返し、公開テスト用アドレスは 1 を返しました。次に何を確認すると役立ちますか？

::option[ローカルのリクエストの出力行数を数えます。]{#deployment-health-checks-user-path-a explanation="行数では、公開アドレスでどのサービスが応答するかは分かりません。"}
::option[同じローカルチェックだけを繰り返します。]{#deployment-health-checks-user-path-b explanation="ローカルの経路からは、すでにバージョン 2 が返っています。"}
::option[公開経路からどのバージョンのサービスに接続するかを調べます。]{#deployment-health-checks-user-path-c .correct explanation="二つの経路からは異なる結果が返りました。"}
:::

## まとめ

デプロイ後の各チェックで何が確認できるかを説明できるようになりました。

1. メインプログラムが実行中であることを確認します。
2. 期待するバージョンを返すエンドポイントにリクエストします。
3. 利用者が使うアクセス経路を別に確認します。
