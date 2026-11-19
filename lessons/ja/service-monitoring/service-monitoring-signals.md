---
lesson_id: "service-monitoring-signals"
course_id: "service-monitoring"
lang: "ja"
order_index: 1
title: "監視のシグナル"
description: "Web サービスで知りたいことに合った監視シグナルの選び方を学びます。"
meta_title: "監視のシグナル - サービス監視"
meta_description: "Web サービスで知りたいことに合った監視シグナルの選び方を学びます。"
meta_keywords: "監視シグナル, サービス監視, DevOps, Linux Journey"
---

利用者からページが遅いと言われたら、まずどのような症状だったかを把握し、それを表せる測定方法を選びます。**シグナル**とは、件数、測定値、記録されたイベントなど、状況の手掛かりになる観測結果です。

## 利用者の体験を確認する

**可用性**は、サービスが期待された処理を行えるかどうかを表します。例えば、トップページを要求し、正常な応答が返るかを確認できます。**レイテンシ**はリクエストにかかる時間です。正常に開くページでも、表示までに数秒かかることがあります。

:::single-choice{#service-monitoring-signals-slow-page} 利用者はページを受け取れますが、数秒かかります。症状を最も直接的に表すシグナルはどれですか？

::option[サーバー上のコンテナ数です。]{#service-monitoring-signals-slow-page-b explanation="その数では利用者の待ち時間を測れません。"}
::option[ページを受け取るまでの時間です。]{#service-monitoring-signals-slow-page-a .correct explanation="レイテンシは、リクエストにかかった時間を表します。"}
::option[ソースリポジトリのバイト数です。]{#service-monitoring-signals-slow-page-c explanation="リポジトリのサイズからは、リクエストの所要時間が分かりません。"}
:::

## リクエストとエラーを数える

**トラフィック**とは、1 分当たりのリクエスト件数などで表される、サービスへの需要です。失敗した件数と一緒に総数も記録します。1,000 件中 5 件のエラーと、10 件中 5 件のエラーでは影響の大きさが異なります。

:::single-choice{#service-monitoring-signals-count-context} 二つの時間帯でそれぞれ 5 件の失敗がありました。利用者への影響を比べるのに役立つのは何ですか？

::option[各時間帯の総リクエスト数です。]{#service-monitoring-signals-count-context-b .correct explanation="エラー率の比較には、両方の時間帯で分母となる総数が必要です。"}
::option[ダッシュボードの名前です。]{#service-monitoring-signals-count-context-a explanation="グラフの場所は分かりますが、トラフィック量は分かりません。"}
::option[サービスが一覧に並ぶ順番です。]{#service-monitoring-signals-count-context-c explanation="一覧の順番からは影響を受けたリクエストの件数は分かりません。"}
:::

## リソースに余裕があるかを確認する

**飽和度**は、リソースの処理能力にどれだけ余裕があるかを示します。Web プロセスが動いていても、データベースで処理を待つリクエストがたまることがあります。判断する前に、利用者が見た症状とリソースのシグナルを比較します。

:::single-choice{#service-monitoring-signals-saturation-check} 待ち行列が伸びたときに、リクエストも遅くなりました。次に何を調べるのが妥当ですか？

::option[待ち行列が根本原因だと断定します。]{#service-monitoring-signals-saturation-check-a explanation="同時に起きた変化は手掛かりになります。原因と判断するには追加の証拠が必要です。"}
::option[ホストに保存されたイメージを数え直します。]{#service-monitoring-signals-saturation-check-b explanation="イメージを利用できるかどうかでは、リクエストが順番を待っている理由は分かりません。"}
::option[待っている処理を担当するリソースを調べます。]{#service-monitoring-signals-saturation-check-c .correct explanation="そのリソースを調べると、処理が追いついているかを確認できます。"}
:::

## まとめ

利用者が気付いた症状に合うシグナルを選べるようになりました。

1. 可用性とレイテンシを区別します。
2. 失敗件数をリクエスト総数とあわせて読み取ります。
3. 飽和度から処理能力の余裕を把握します。
