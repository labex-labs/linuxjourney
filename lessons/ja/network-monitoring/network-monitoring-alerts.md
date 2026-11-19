---
lesson_id: "network-monitoring-alerts"
course_id: "network-monitoring"
lang: "ja"
order_index: 6
title: "ネットワークアラート"
description: "ネットワークアラートを読み、次の防御判断に必要な証拠を選ぶ方法を学びます。"
meta_title: "ネットワークアラート - ネットワーク監視"
meta_description: "ネットワークアラートを読み、次の防御判断に必要な証拠を選ぶ方法を学びます。"
meta_keywords: "ネットワークアラート, DNS, ネットワーク監視, サイバーセキュリティ, Linux Journey"
---

ネットワークアラートは、監視条件が満たされたことを知らせます。何が起きたかを判断する前に、その条件と情報源を読みます。アラートの対象には、想定外の通信、繰り返す失敗、観測データの欠落などがあります。

## アラートの対象範囲を読む

次の模擬アラートは DNS の記録に基づいています。5 分間に発生した失敗をクライアントごとに集計しています。

```text
Window: 09:20–09:25 UTC
Client: 192.0.2.10
Condition: at least 10 failed name lookups
Observed: 12 failures
```

問い合わせとその結果を詳しく調べるきっかけになります。どのプログラムが問い合わせたかは、アラートだけでは分かりません。

:::single-choice{#network-monitoring-alerts-alert-scope} アラートが直接観測したことは何ですか？

::option[記録されたクライアントで、その時間帯に名前解決が 12 件失敗しました。]{#network-monitoring-alerts-alert-scope-b .correct explanation="これがアラートに記載された件数と対象範囲です。"}
::option[データが失われたことが確認されました。]{#network-monitoring-alerts-alert-scope-a explanation="このルールが集計するのは、名前解決の失敗です。"}
::option[12 台の異なるクライアントがありました。]{#network-monitoring-alerts-alert-scope-c explanation="アラートは一つのクライアントアドレスの記録を集計しています。"}
:::

## 関連するホストの記録を探す

大半の失敗が `preview.example` への問い合わせだったとします。クライアントのサービスログに、古い設定を使って再試行を繰り返したことが残っているかもしれません。問い合わせを行ったと考えられるプログラムについて、同じ時刻の前後の記録を探します。活動の発生元を判断する前に、監視記録でホストを識別するラベルを確認します。

:::single-choice{#network-monitoring-alerts-evidence-choice} あるサービスが名前解決を再試行していたかを調べるには、どの記録が役立ちますか？

::option[別のホストで後から行われた公開ページの閲覧記録です。]{#network-monitoring-alerts-evidence-choice-b explanation="通信の相手と時刻が、調査対象のパターンと一致しません。"}
::option[活動時刻がないインストール済みアプリケーションの一覧です。]{#network-monitoring-alerts-evidence-choice-c explanation="インストール済みソフトウェアの一覧だけでは、問い合わせの実行元は分かりません。"}
::option[アラートの時間帯に、該当する名前解決の失敗が記録されたサービスログです。]{#network-monitoring-alerts-evidence-choice-a .correct explanation="問い合わせのパターンとそのプログラムを結び付けられる可能性があります。"}
:::

## 次の判断を記録する

サービスログが一致する場合は、原因を記録します。承認を得て設定を修正したら、代表的な名前解決が成功するかを確かめます。証拠が足りなければ、何が不足しているかを明記します。アラート、裏付けとなる記録、確認結果をまとめて保管します。

:::single-choice{#network-monitoring-alerts-uncertainty} DNS アラートはありますが、対応するホストの記録がありません。何を報告しますか？

::option[どのプログラムが実行したか特定しました。]{#network-monitoring-alerts-uncertainty-a explanation="DNS の証拠だけでは、プロセスを特定できませんでした。"}
::option[問い合わせのパターンは確認できましたが、実行元のプログラムは不明です。]{#network-monitoring-alerts-uncertainty-c .correct explanation="観測できたことと、まだ分からないことの両方が残ります。"}
::option[このアラートからは何も分かりません。]{#network-monitoring-alerts-uncertainty-b explanation="リゾルバーが観測した状況は分かります。"}
:::

## 想定された再試行かを確かめる

あるチームが、テスト用ホスト名を繰り返し名前解決するジョブを予定していたとします。予定の時刻、DNS の記録にある名前、ジョブ自身のログを比べます。複数の項目が一致すれば、その説明の裏付けになります。一致しない失敗は、引き続き調査の対象にします。

:::single-choice{#network-monitoring-alerts-final-application} 予定されたジョブが原因だという説明を最も強く裏付けるのはどれですか？

::option[アラートが、ほかにも定期ジョブを実行するホストから出ました。]{#network-monitoring-alerts-final-application-c explanation="そのホストの情報だけでは、どのプログラムが問い合わせたかは分かりません。"}
::option[ジョブのログに、同じホスト名とアラートの時間帯の再試行が記録されています。]{#network-monitoring-alerts-final-application-a .correct explanation="名前と時刻が一致するため、観測したパターンを既知のジョブと結び付ける根拠になります。"}
::option[ジョブはその日のうちのどこかで実行される予定でした。]{#network-monitoring-alerts-final-application-b explanation="日単位の予定だけでは、アラートの時間帯も問い合わせた名前も確認できません。"}
:::

## まとめ

ネットワークアラートを手掛かりに、次の調査対象を絞れるようになりました。

1. 検知ルールと、その対象範囲を特定します。
2. 考えられる説明を検証するために、関連する記録を選びます。
3. 観測結果と、まだ分からないことを記録します。
