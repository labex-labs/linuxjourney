---
lesson_id: "service-availability-errors"
course_id: "service-monitoring"
lang: "ja"
order_index: 3
title: "可用性とエラー"
description: "時間帯とリクエスト総数をそろえて、エラー率を比較する方法を学びます。"
meta_title: "可用性とエラー - サービス監視"
meta_description: "時間帯とリクエスト総数をそろえて、エラー率を比較する方法を学びます。"
meta_keywords: "可用性, エラー率, サービス監視, DevOps, Linux Journey"
---

多くの利用者に応答できていても、一部のリクエストは失敗することがあります。同じ時間帯のリクエスト総数と失敗件数を使って、観測されたリクエストのうちどれだけが失敗したかを求めます。

## エラー率を計算する

**エラー率**は、失敗件数を観測した全リクエストの件数で割った値です。100 を掛けるとパーセントで表せます。

```text
Window          Requests   Failures
09:00–09:05          100          2
09:05–09:10           20          2
```

最初の時間帯では 100 件中 2 件が失敗したので 2% です。次の時間帯でも失敗は 2 件ですが、総数は 20 件なので 10% です。

:::single-choice{#service-availability-errors-compare-windows} 失敗の割合が高かったのはどちらの時間帯ですか？

::option[09:05 から 09:10 までです。]{#service-availability-errors-compare-windows-b .correct explanation="20 件中 2 件は、100 件中 2 件よりも大きな割合です。"}
::option[どちらも 2 件の失敗なので同じです。]{#service-availability-errors-compare-windows-a explanation="割合の分母になる総数が異なります。"}
::option[トラフィックが多かった 09:00 から 09:05 までです。]{#service-availability-errors-compare-windows-c explanation="失敗件数が同じなら、総数が多いほど割合は小さくなります。"}
:::

## 比較の範囲をそろえる

時間帯、ルート、失敗とみなす条件をそろえます。別のサービスに依存するページがエラーでも、ヘルスチェック用のエンドポイントは正常に応答する場合があります。そのページの利用者への影響を調べるなら、そのページへのリクエストを数えます。

:::single-choice{#service-availability-errors-route-scope} ヘルスチェック用のエンドポイントは常に成功しますが、購入者から決済画面でエラーになるとの報告がありました。何を調べますか？

::option[ヘルスチェック用のエンドポイントの応答だけを調べます。]{#service-availability-errors-route-scope-b explanation="その応答が示すのは別の操作の結果です。"}
::option[サービスアカウントの名前を調べます。]{#service-availability-errors-route-scope-c explanation="影響を受けたリクエストの件数は分かりません。"}
::option[決済画面へのリクエストと、その失敗件数を調べます。]{#service-availability-errors-route-scope-a .correct explanation="報告された問題が起きているのは決済画面のルートです。"}
:::

## トラフィックが少ない場合の読み方

2 件のリクエストのうち 1 件が失敗すると、観測したエラー率は 50% です。これはそのときのサンプルについての結果です。少数のリクエストでは割合が大きくぶれるため、パーセントと件数を併記します。リクエストが 0 件なら、実トラフィックのエラー率は定義できません。別途スケジュールされたテストを使えば、リクエストが成功したかを確認できます。

:::single-choice{#service-availability-errors-zero-traffic} ある時間帯に利用者からのリクエストがありませんでした。利用者のエラー率をどう報告しますか？

::option[完全に利用可能だったことが分かります。]{#service-availability-errors-zero-traffic-a explanation="その判断に使える利用者のリクエストは観測されていません。"}
::option[この時間帯にはエラー率を求めるためのリクエストデータがありません。]{#service-availability-errors-zero-traffic-c .correct explanation="サービスが応答するかを確かめたい場合は、別のテストを使います。"}
::option[確実に 100% です。]{#service-availability-errors-zero-traffic-b explanation="分母にできるリクエストが観測されていません。"}
:::

## まとめ

条件を添えてエラー率を説明できるようになりました。

1. 同じ時間帯の失敗件数と総リクエスト数を使います。
2. 調査の目的に合わせて、対象ルートと失敗の定義を選びます。
3. トラフィックが少ない場合は件数も示します。
