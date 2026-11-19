---
lesson_id: "service-alerts"
course_id: "service-monitoring"
lang: "ja"
order_index: 6
title: "サービスのアラート"
description: "アラートの条件と集計時間帯を読み取り、次に何を確認するかを学びます。"
meta_title: "サービスのアラート - サービス監視"
meta_description: "アラートの条件と集計時間帯を読み取り、次に何を確認するかを学びます。"
meta_keywords: "サービスアラート, サービス監視, DevOps, Linux Journey"
---

ダッシュボードには測定結果が表示されます。**アラート**は、対応が必要かもしれない状況を担当者に知らせます。何が起きたか、次に何を確認すべきかが分かる通知が役立ちます。

## 発報条件を読む

5 分間にトップページへのリクエストのうち 5% を超えて失敗すると知らせるルールを考えます。このサービスで判断に使える件数を確保するため、リクエストが 100 件以上あることも条件です。

```text
Window   09:10–09:15 UTC
Route    /
Requests 120
Failures 12
```

120 件中 12 件が失敗すると、エラー率は 10% です。両方の条件を満たすため、トップページで観測された失敗について通知が出ます。

:::single-choice{#service-alerts-condition-match} 10 件のリクエストのうち 1 件が失敗した場合、同じルールでアラートは出ますか？

::option[いいえ。リクエストが最低件数に達していません。]{#service-alerts-condition-match-b .correct explanation="このルールでは、率と件数がともに条件を満たす必要があります。"}
::option[はい。エラー率が 5% を超えています。]{#service-alerts-condition-match-a explanation="このルールでは、少なくとも 100 件のリクエストが必要です。"}
::option[いいえ。10 件中 1 件の失敗は 1% です。]{#service-alerts-condition-match-c explanation="10 件中 1 件は 10% ですが、このルールを適用するにはリクエストが少なすぎます。"}
:::

## 対象の時間帯を確認する

現在のダッシュボードが正常に見えても、アラートに示された時間帯を調べます。通知が少し前の状況を指していることがあるためです。指標が普段の範囲に戻ったか、利用者が主要な操作を再び行えるかを確認します。

:::single-choice{#service-alerts-alert-window} 09:16 に届いたアラートの対象は 09:10 から 09:15 でした。対応するエラーをまずどこで探しますか？

::option[前の週のレポートだけを調べます。]{#service-alerts-alert-window-b explanation="平常時の基準にはなりますが、影響が出た時間帯は含まれません。"}
::option[09:16 以降だけを調べます。]{#service-alerts-alert-window-c explanation="通知が届く時刻は、異常が観測された時刻より遅いことがあります。"}
::option[アラートに記録された時間帯を調べます。]{#service-alerts-alert-window-a .correct explanation="ルールが失敗を集計したのはその時間帯です。"}
:::

## 次に確認することを決める

トップページの失敗を知らせるアラートには、そのルートの指標や直近のログへのリンクを付けられます。利用者への影響を確認し、原因は別途調べます。すでに復旧している場合も、再発時に調査できるように状況を記録します。

:::single-choice{#service-alerts-next-check} トップページがまだエラーになるかを直接確認するには、まず何をしますか？

::option[キャッシュ内のコンテナイメージをすべて数えます。]{#service-alerts-next-check-a explanation="アラートが示しているのは、稼働中のサービスへのリクエストの結果です。"}
::option[許可されたテストリクエストを、影響を受けたルートに送ります。]{#service-alerts-next-check-c .correct explanation="新しいリクエストを送ると、そのルートで問題が続いているかを確認できます。"}
::option[ルールを無効にし、通知が出ないようにします。]{#service-alerts-next-check-b explanation="通知の設定が変わるだけで、サービスの動作を確認できません。"}
:::

## まとめ

アラートを読み、何を確認すべきか判断できるようになりました。

1. 指標、しきい値、集計に必要な最低件数を確認します。
2. アラートの対象時間帯に該当する証拠を探します。
3. 利用者が体験した症状に合った方法で確認します。
