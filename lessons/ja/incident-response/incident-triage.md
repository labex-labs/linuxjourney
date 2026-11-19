---
lesson_id: "incident-triage"
course_id: "incident-response"
lang: "ja"
order_index: 1
title: "インシデントのトリアージ"
description: "インシデントの第一報から、初動調査の対象を絞る方法を学びます。"
meta_title: "インシデントのトリアージ - インシデント対応"
meta_description: "インシデントの第一報から、初動調査の対象を絞る方法を学びます。"
meta_keywords: "トリアージ, 初動調査, インシデント対応, サイバーセキュリティ, Linux Journey"
---

第一報では、ページが開かなかったことや、アラートが出たことが伝えられる場合があります。**トリアージ**とは、何に優先して対応するかを決めることです。対応を選ぶ前に、影響を受けたサービス、時刻、観測された動作を記録します。

## 報告を読む

チームメンバーが書いた、次の模擬報告を読みます。

```text
09:22 UTC: Visitors received 503 from the public homepage.
The staff preview still loaded during the same check.
First failure observed at approximately 09:19 UTC.
```

報告には二つの経路と、それぞれ異なる観測結果があります。公開トップページで何が起きるかを確認し、確認した時刻とアドレスを記録します。

:::single-choice{#incident-triage-affected-service} 最初の確認では、どの症状に注目しますか？

::option[スタッフ用プレビューが 503 を返すことです。]{#incident-triage-affected-service-b explanation="報告では、スタッフ用プレビューは引き続き開けています。"}
::option[公開トップページが 503 を返すことです。]{#incident-triage-affected-service-a .correct explanation="報告で影響があるとされた経路です。"}
::option[無関係なホストにページが見つからないことです。]{#incident-triage-affected-service-c explanation="その経路は報告の対象外です。"}
:::

## 影響の大きさを見積もる

影響を受けた利用者やリクエストの数と、サービスが引き続き使えるかを確認します。問題が今も続いているかも調べます。十分な証拠が得られるまでは、不確かな数値を推定値として示します。通知先は対応計画に従って決めます。

:::single-choice{#incident-triage-triage-scope} 今も緊急性が高いかを判断するのに役立つ観測結果はどれですか？

::option[障害が報告された経路の現在の確認結果と、直近のリクエストの結果です。]{#incident-triage-triage-scope-b .correct explanation="症状が続いているか、どの程度広がっているかを確認できます。"}
::option[リポジトリの最初のコミットからの経過時間です。]{#incident-triage-triage-scope-a explanation="現在の影響については分かりません。"}
::option[第一報に付いた重大度ラベルだけです。]{#incident-triage-triage-scope-c explanation="当初のラベルは参考になります。現在も対応を急ぐべきかは、現時点の影響も見て判断します。"}
:::

## 最初に取る対応を選ぶ

今のリクエストでも失敗する場合は、結果を保存し、直近のサービス変更と、影響が出た時間帯のログを調べます。同時に正常な経路があれば、問題の範囲を絞る手掛かりになります。最初に思い付いた説明は、証拠が得られるまで仮説として扱います。

:::single-choice{#incident-triage-first-next-step} 公開経路はまだ失敗し、スタッフ用プレビューは利用できます。次に何を調べますか？

::option[社内の無関係なプロジェクトをすべて調べます。]{#incident-triage-first-next-step-a explanation="報告により、対象のサービスと時間帯はすでに絞られています。"}
::option[別の日に起きた古いエラーを無作為に選んで調べます。]{#incident-triage-first-next-step-b explanation="失敗が観測された時刻に近い証拠から調べます。"}
::option[報告の時間帯における公開経路の記録を調べます。]{#incident-triage-first-next-step-c .correct explanation="経路の問題とサービス自体の障害を見分ける手掛かりになります。"}
:::

## まとめ

インシデントの報告を受け、初動調査の対象を絞れるようになりました。

1. 影響が出た経路、時刻、症状を記録します。
2. 利用者への現在の影響を確認します。
3. 影響を受けた経路について、次に確認する証拠の情報源を選びます。
