---
lesson_id: "deployment-records"
course_id: "deployment"
lang: "ja"
order_index: 6
title: "デプロイの記録"
description: "短いリリースの時系列から、デプロイとロールバックの経過を読み取る方法を学びます。"
meta_title: "デプロイの記録 - デプロイ"
meta_description: "短いリリースの時系列から、デプロイとロールバックの経過を読み取る方法を学びます。"
meta_keywords: "デプロイの記録, 時系列, ロールバック, DevOps, Linux Journey"
---

デプロイの記録があれば、利用者に見えた結果を、実施した変更と結び付けて調べられます。まず時刻、環境、ソースのリビジョン、成果物を記録します。そこにチェックの結果と、その後に取った対応を書き加えます。

## 何が変わったかを記録する

次の練習用の記録は、一つのデプロイの経過を追います。識別子は読みやすいように短くしています。

```text
UTC    Target   Commit   Artifact  Observation
09:00  staging  8a61e1   digest-C  version 3, home returned 200
09:12  prod     8a61e1   digest-C  version 3, home returned 503
09:18  prod     72b110   digest-B  version 2, home returned 200
```

HTTP 200 は正常な応答を表します。HTTP 503 は、そのリクエストでサービスを利用できなかったことを示します。実際の記録には、結果とともに確認方法やアドレスも残します。

:::single-choice{#deployment-records-first-prod-change} digest-C を本番で最初に確認した結果は、どの行にありますか？

::option[09:12 prod の行です。]{#deployment-records-first-prod-change-b .correct explanation="本番へデプロイしようとしたバージョンと、失敗したチェックが記録されています。"}
::option[09:00 staging の行です。]{#deployment-records-first-prod-change-a explanation="これは別の環境で実行したチェックです。"}
::option[09:18 prod の行です。]{#deployment-records-first-prod-change-c explanation="ロールバック後の別の成果物が記録されています。"}
:::

![ステージングの成功、本番での HTTP 503、バージョン 2 へのロールバックを示す模擬リリースの時系列](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-records/release-timeline.png)

## ロールバックの経過を説明する

最後の行では、digest-B に戻っています。バージョン確認とトップページへのリクエストの結果は、ロールバック後の状態を示します。これだけでは、先に起きた障害の詳しい原因は分かりません。根拠が見つかるまでは、推測を観察結果と分けて記録します。

:::single-choice{#deployment-records-rollback-evidence} 09:18 の結果について、何が言えますか？

::option[09:12 の失敗は、データベースがなかったことが原因です。]{#deployment-records-rollback-evidence-b explanation="この記録には依存先の確認結果がありません。"}
::option[それ以降のリクエストはすべて成功しました。]{#deployment-records-rollback-evidence-c explanation="一回のチェックでは、そのリクエストの結果が分かります。"}
::option[本番はバージョン 2 に戻り、トップページへのそのリクエストは成功しました。]{#deployment-records-rollback-evidence-a .correct explanation="この行には、復旧したバージョンと観察した HTTP の応答が記録されています。"}
:::

## 記録を引き継ぐ

次に調べる人が、同じ条件で確認できるようにします。チェック方法、タイムゾーンを含む時刻、分かる場合は成果物を作ったビルドへのリンクを残します。原因が不明なら、次に調べる対象も示します。

:::single-choice{#deployment-records-handoff-detail} 次の担当者がトップページのチェックを繰り返すとき、どの情報が役立ちますか？

::option[一つ前のリリースの識別子だけです。]{#deployment-records-handoff-detail-a explanation="前のバージョンは比較に使えますが、このチェックをどこでいつ実行したかは分かりません。"}
::option[確認した対象アドレスと正確な時刻です。]{#deployment-records-handoff-detail-c .correct explanation="同じ経路を確認し、関係する時間帯の他の情報と比較できます。"}
::option[ソースのコミットが作られた時刻です。]{#deployment-records-handoff-detail-b explanation="コミット時刻はそれより前に起きた別の出来事です。再確認に必要なのは、チェックの時刻と宛先です。"}
:::

## 実際に動いたイメージを記録する

デプロイのメモにあるタグは、リリース後に参照先が変わる可能性があります。サービスがすでにバージョン 2 を返しているなら、読みやすいタグに加え、実際に動作している成果物も記録します。両方の値があれば、レジストリのタグが付け替えられても、後からリリースを比較できます。

:::single-choice{#deployment-records-final-application} リリースノートには site:2 とあります。後でより確実に比較するため、何を記録しますか？

::option[最後に site:2 をプルした人が取得したダイジェストです。]{#deployment-records-final-application-c explanation="後でプルすると、実行中のサービスとは異なる内容が返ることがあります。"}
::option[実際に実行されたイメージの完全なダイジェストです。]{#deployment-records-final-application-a .correct explanation="タグが後から別の内容を指しても、実際に使われた内容を特定できます。"}
::option[読みやすいタグを別の欄にもコピーします。]{#deployment-records-final-application-b explanation="タグを繰り返しても、参照先は特定できません。"}
:::

## まとめ

リリースの時系列を読み取り、別の担当者に引き継げるようになりました。

1. 記録から環境、リビジョン、成果物を特定します。
2. 観察した結果に基づいてロールバックを説明します。
3. 次の確認に必要な詳しさで記録を残します。
