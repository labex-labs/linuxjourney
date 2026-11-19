---
lesson_id: "network-monitoring-records"
course_id: "network-monitoring"
lang: "ja"
order_index: 1
title: "ネットワークの記録"
description: "監視で知りたいことに合ったネットワーク記録の選び方を学びます。"
meta_title: "ネットワークの記録 - ネットワーク監視"
meta_description: "監視で知りたいことに合ったネットワーク記録の選び方を学びます。"
meta_keywords: "ネットワーク記録, DNS ログ, パケットキャプチャ, ネットワーク監視, サイバーセキュリティ, Linux Journey"
---

ネットワークの観測結果は、ある場所で一つのツールが確認できた通信を表します。まず、何を知りたいか考えます。同じ通信でも、情報源が違えば見える部分が異なります。

## 記録の種類を選ぶ

**フロー記録**は、ネットワーク上のエンドポイント間の通信を集計したものです。**DNS ログ**には、リゾルバーが観測した名前解決が記録されます。**パケットキャプチャ**では、取得地点で観測できた個々のパケットのコピーを保存します。エンドポイントとは通信の一方の端で、アドレスとポートで識別されることがよくあります。

:::single-choice{#network-monitoring-records-choose-dns} リゾルバーが site.example にどのように応答したかを知りたい場合、最適な情報源はどれですか？

::option[稼働中の Web ワーカーの数です。]{#network-monitoring-records-choose-dns-b explanation="ワーカー数と名前解決は無関係です。"}
::option[そのリゾルバーの DNS ログです。]{#network-monitoring-records-choose-dns-a .correct explanation="リゾルバーは、処理した問い合わせと応答を記録できます。"}
::option[通信量だけを示すフロー集計です。]{#network-monitoring-records-choose-dns-c explanation="フロー集計には DNS の問い合わせと応答が含まれないことがあります。"}
:::

## どこで観測した記録かを確認する

ノートパソコンのキャプチャに入るのは、そのパソコンで選んだインターフェースから見えるパケットです。サーバーのログには、サーバーに届いた通信や、サーバーが記録した動作が残ります。例えば、利用者のリクエストがサーバーに届く前に失敗する場合もあります。知りたいことに対して適切な位置で得られた記録を使います。

:::single-choice{#network-monitoring-records-capture-scope} 別のコンピューターで取得したキャプチャには、対象のリクエストが見つかりませんでした。結論を出す前に何を確認しますか？

::option[取得に使ったインターフェースで、該当する時刻に対象の経路を観測できたかです。]{#network-monitoring-records-capture-scope-b .correct explanation="パケットが見つからないのは、その観測地点から見えなかったためかもしれません。"}
::option[無関係なパケットがキャプチャに含まれているかです。]{#network-monitoring-records-capture-scope-a explanation="無関係な通信が見えれば、取得が行われたことは分かります。対象の経路や時刻を観測できたかは未確認のままです。"}
::option[同じ時刻に別のホストがキャプチャを取得していたかです。]{#network-monitoring-records-capture-scope-c explanation="別のホストが同時に取得していても、このインターフェースで何が見えたかまでは分かりません。"}
:::

## 必要な通信だけを含むサンプルを使う

パケットキャプチャには、公開を意図していない情報が含まれることがあります。パケットの読み方を学ぶときは、安全な練習用の通信だけを含む、用意されたキャプチャを使います。抜粋を共有する際は、観測した時間帯と使ったフィルターも示すと、相手が記録の範囲を理解できます。

:::single-choice{#network-monitoring-records-choosing-evidence} DNS 応答の見分け方を学ぶのに最適なサンプルはどれですか？

::option[無関係な従業員の通信を長時間記録したキャプチャです。]{#network-monitoring-records-choosing-evidence-a explanation="不要なデータが増え、個人情報が漏れる可能性があります。"}
::option[名前解決を示すフィールドがない集計です。]{#network-monitoring-records-choosing-evidence-b explanation="学習者が読むべき証拠がありません。"}
::option[練習用の問い合わせと応答を収めた、小さなキャプチャです。]{#network-monitoring-records-choosing-evidence-c .correct explanation="問いに答えるために必要なやり取りが入っています。"}
:::

## まとめ

ネットワーク記録を選び、その記録で何が観測できたかを説明できるようになりました。

1. フロー集計、DNS ログ、パケットキャプチャを区別します。
2. 通信経路に合った観測地点を選びます。
3. 調査に適した、対象を絞ったサンプルを使います。
