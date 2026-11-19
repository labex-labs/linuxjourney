---
lesson_id: "network-monitoring-flows"
course_id: "network-monitoring"
lang: "ja"
order_index: 2
title: "ネットワークフロー"
description: "フローの集計から、アドレス、ポート、時刻、バイト数を読み取る方法を学びます。"
meta_title: "ネットワークフロー - ネットワーク監視"
meta_description: "フローの集計から、アドレス、ポート、時刻、バイト数を読み取る方法を学びます。"
meta_keywords: "ネットワークフロー, 通信量, ネットワーク監視, サイバーセキュリティ, Linux Journey"
---

**フロー**とは、ネットワークアドレス、ポート、プロトコルなどの条件が共通する通信のまとまりです。監視システムは通信の中身を丸ごと保存しなくても、フローのバイト数やパケット数を記録できます。

## 通信の両端を読み取る

この模擬集計では、収集ツールが送信元から宛先への方向を記録します。TCP などのトランスポートプロトコルにはポート番号があり、受信側のリスナーを特定する手掛かりになります。

```text
start=09:21:00Z protocol=TCP src=192.0.2.10:51600 dst=192.0.2.20:443 bytes=1800
start=09:21:00Z protocol=TCP src=192.0.2.20:443 dst=192.0.2.10:51600 bytes=8200
```

最初の行はポート 443 に向かう通信です。2 行目は反対方向の通信です。収集ツールによっては両方向をまとめるので、読んでいる記録の形式を確認します。

:::single-choice{#network-monitoring-flows-endpoint-direction} 最初の行で、記録された通信を受け取るアドレスとポートはどれですか？

::option[192.0.2.10:51600 です。]{#network-monitoring-flows-endpoint-direction-a explanation="これは最初の方向の送信元です。"}
::option[記載された両方のアドレスとポートが宛先です。]{#network-monitoring-flows-endpoint-direction-c explanation="この例では、各行に一方向の通信が記録されています。"}
::option[192.0.2.20:443 です。]{#network-monitoring-flows-endpoint-direction-b .correct explanation="宛先フィールドに、通信が送られた先が示されています。"}
:::

## 通信量を比較する

この例では、ポート 443 を送信元とする方向のバイト数が多くなっています。Web ページでは応答の方が大きくても不思議ではありません。バイト数だけでは、ページの内容、アカウント、通信量が多い理由は分かりません。

:::single-choice{#network-monitoring-flows-byte-count} 2 行目の 8,200 バイトは何を表しますか？

::option[応答メッセージの正確な本文です。]{#network-monitoring-flows-byte-count-b explanation="フローの集計が示すのは通信量で、メッセージの中身は含まれません。"}
::option[その方向で記録された通信量です。]{#network-monitoring-flows-byte-count-a .correct explanation="バイト数は通信量を表し、送信元と宛先が通信の方向を示します。"}
::option[ページが正常に読み込まれたことの保証です。]{#network-monitoring-flows-byte-count-c explanation="通信量からは HTTP の結果は分かりません。"}
:::

## サービスの情報と照合する

把握しているサービスの情報と時刻を使って、どのフローが関係するかを判断します。Web サーバーの応答を知りたい場合は、利用できる範囲で同じ時間帯と接続のアクセスログを照合します。

:::single-choice{#network-monitoring-flows-next-source} Web リクエストの HTTP ステータスを知りたいときは、どの情報を追加で調べるとよいですか？

::option[対応する Web アクセスログの記録です。]{#network-monitoring-flows-next-source-c .correct explanation="サーバーのアクセスログには HTTP の結果が記録されることがあります。"}
::option[フローのバイト数を 100 バイト単位に丸めた値です。]{#network-monitoring-flows-next-source-a explanation="丸めると精度が変わりますが、応答ステータスは分かりません。"}
::option[同じ通信相手の組み合わせについての、別のフロー集計です。]{#network-monitoring-flows-next-source-b explanation="フロー集計で通信を追加確認できますが、通常は HTTP の応答ステータスは分かりません。"}
:::

## まとめ

一つのフロー集計の主なフィールドを読めるようになりました。

1. 通信の両端のアドレスとポートを特定します。
2. 記録された方向のバイト数を読み取ります。
3. アプリケーションの処理結果が必要なら、別の情報源を選びます。
