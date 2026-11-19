---
lesson_id: "network-traffic-baselines"
course_id: "network-monitoring"
lang: "ja"
order_index: 5
title: "トラフィックのベースライン"
description: "トラフィックの変化を異常と判断する前に、条件の似た時間帯を比較する方法を学びます。"
meta_title: "トラフィックのベースライン - ネットワーク監視"
meta_description: "トラフィックの変化を異常と判断する前に、条件の似た時間帯を比較する方法を学びます。"
meta_keywords: "トラフィックベースライン, 通信量, ネットワーク監視, サイバーセキュリティ, Linux Journey"
---

**ベースライン**は、条件を決めたうえで普段どのような値が観測されるかを示す基準です。トラフィック監視では、同じサービスの同じ時刻における標準的な件数や範囲を使うことがあります。

## 比較できる時間帯を選ぶ

公開ページは勤務時間中にアクセスが増えることがあります。変化を見つけるには、利用状況が似た時間帯を比較します。この例では、一つのサービスへのリクエストを 5 分間ずつ集計しています。

```text
Window                 Requests
Typical weekdays 09:00  90–120
Today 09:00                230
Typical nights 02:00       2–8
```

230 件は平日の朝の通常範囲から外れています。深夜の範囲では、この比較の基準として条件が合いません。

:::single-choice{#network-traffic-baselines-baseline-fit} 今日の 09:00 の時間帯と比べるには、どの行が適切なベースラインになりますか？

::option[通常の夜間の 02:00 です。]{#network-traffic-baselines-baseline-fit-b explanation="その行は異なるトラフィックの傾向を示します。"}
::option[今日観測された 230 件だけです。]{#network-traffic-baselines-baseline-fit-c explanation="現在の値だけでは、何が変わったかを判断できません。比較対象が必要です。"}
::option[通常の平日の 09:00 です。]{#network-traffic-baselines-baseline-fit-a .correct explanation="確認対象の時刻とサービスが一致しています。"}
:::

## 変化の背景を調べる

告知バナーの掲載や定期ジョブで変化を説明できることがあります。追加調査が必要かを判断する前に、アクセスされたルートや時刻、承認済みの変更を確認します。ベースラインは違いを示し、何を調べ始めるかの手掛かりになります。

:::single-choice{#network-traffic-baselines-baseline-explain} 事前に告知した公開の後にトラフィックが倍になりました。何を確認しますか？

::option[この差を、アカウントが侵害された証拠とみなします。]{#network-traffic-baselines-baseline-explain-a explanation="件数だけでは、原因やアカウントに関するイベントは分かりません。"}
::option[実際の時刻とアクセス先を、公開で見込まれた時刻やアクセス先と比較します。]{#network-traffic-baselines-baseline-explain-b .correct explanation="関連する観測結果から、考えられる説明を検証できます。"}
::option[公開があれば急増は必ず説明できるので、変化は無視します。]{#network-traffic-baselines-baseline-explain-c explanation="想定どおりの変化と無関係な活動は同時に起こることがあります。"}
:::

## 測定の条件を確認する

収集ツールを変更すると、実際の通信量が変わらなくても件数が変わることがあります。昨日から監視対象に別のネットワークを追加した場合は、各時間帯にどのトラフィックが含まれているかを確認します。比較結果には、サービス、観測地点、時刻、単位を添えます。

:::single-choice{#network-traffic-baselines-changed-coverage} 収集ツールが 2 番目のサイトも記録するようになりました。次の比較を有効にするにはどうしますか？

::option[同じサイトと同じ収集範囲の件数を比較します。]{#network-traffic-baselines-changed-coverage-c .correct explanation="範囲をそろえると、トラフィックの変化と収集範囲の変更を区別しやすくなります。"}
::option[対象範囲を確認せずに、二つの合計件数を比較します。]{#network-traffic-baselines-changed-coverage-a explanation="収集範囲が変わったため、単純には比較できません。"}
::option[集計時間を長くし、新しい合計を昨日の合計と比較します。]{#network-traffic-baselines-changed-coverage-b explanation="時間を延ばしても、集計に含めるサイトや情報源をそろえなければ、異なる範囲が混ざります。"}
:::

## まとめ

ネットワークの比較に使えるベースラインかどうか判断できるようになりました。

1. サービス、時刻、単位をそろえます。
2. 差を解釈する前に、予定された変更がなかったかを調べます。
3. データの収集範囲が変わったかを確認します。
