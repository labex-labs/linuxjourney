---
lesson_id: "service-resource-saturation"
course_id: "service-monitoring"
lang: "ja"
order_index: 5
title: "リソースの飽和"
description: "使用率と待ち行列から、サービスがどこで処理能力の限界に近づいているかを見極めます。"
meta_title: "リソースの飽和 - サービス監視"
meta_description: "使用率と待ち行列から、サービスがどこで処理能力の限界に近づいているかを見極めます。"
meta_keywords: "リソース飽和, 使用率, 待ち行列, サービス監視, DevOps, Linux Journey"
---

あるリソースにすぐ処理できる量を超えた仕事が来ると、リクエストは順番を待つことがあります。待ち時間が続くと、待ち行列の増加や応答の遅れとして現れます。

## 処理能力と需要を読み取る

**使用率**は、リソースがどれだけ使われているかを示します。例えば、ワーカープールでは 4 件の仕事を同時に処理できるとします。4 個のワーカーすべてが稼働していれば、その時点で空きはありません。追加の仕事は、ワーカーが空くまで待ち行列に入ります。

:::single-choice{#service-resource-saturation-worker-capacity} 4 個のワーカーが稼働し、3 件の仕事が順番を待っています。何が分かりますか？

::option[ちょうど 7 個のワーカーが稼働しています。]{#service-resource-saturation-worker-capacity-b explanation="3 件の仕事はまだ処理枠に入っておらず、順番を待っています。"}
::option[すべてのリクエストがすでに失敗しました。]{#service-resource-saturation-worker-capacity-c explanation="待機中の仕事は、ワーカーが空けば完了できる場合があります。"}
::option[すべての処理枠が使用中で、一部の仕事が待っています。]{#service-resource-saturation-worker-capacity-a .correct explanation="ワーカー数は現在の使用状況を示し、待ち行列はすぐには処理できなかった需要を示します。"}
:::

## 時間とともにどう変化するかを比べる

一時的にリクエストが集中する場合と、測定を重ねるたびに待ち行列が伸びる場合では状況が異なります。同じ時間帯の待ち行列、レイテンシ、トラフィックを比較します。

```text
Time   Busy workers   Queued jobs   Typical response
09:10       2 / 4           0             80 ms
09:11       4 / 4           5            300 ms
09:12       4 / 4          14            640 ms
```

この例では、ワーカーに空きがなく待ち行列も伸びているため、仕事が完了するより速く新しい仕事が届いていると考えられます。ワーカーが何の処理に時間を使っているかを調べます。

:::single-choice{#service-resource-saturation-sustained-pressure} 負荷が続いていることを最も強く示すのはどれですか？

::option[09:10 に 2 個のワーカーが稼働しています。]{#service-resource-saturation-sustained-pressure-a explanation="その行では処理枠に空きがあり、待機中の仕事もありません。"}
::option[すべてのワーカーが稼働したまま、待ち行列が伸びています。]{#service-resource-saturation-sustained-pressure-b .correct explanation="処理枠が埋まったまま、待機中の仕事がたまっています。"}
::option[待ち行列が空のまま、1 件の応答だけ遅くなりました。]{#service-resource-saturation-sustained-pressure-c explanation="1 件の遅い応答も調査の手掛かりになります。処理枠が埋まった状態で測定するたびに待ち行列が伸びる方が、負荷が続いていることを強く示します。"}
:::

![全処理枠が使用され、待ち行列が伸びていることを示す模擬ワーカー指標](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-resource-saturation/worker-queue.png)

## 原因を調べる

ワーカーが埋まる理由には、リクエストの到着が速くなったこと、依存先が遅くなったこと、最近の変更で個々の処理が長引くようになったことなどがあります。リクエスト件数、処理にかかる時間、依存先の観測結果を比較します。別のシグナルも確認すると、対応を選びやすくなります。

:::single-choice{#service-resource-saturation-next-observation} リクエスト量は変わらず、処理に時間がかかるようになりました。待ち行列が伸びた理由を調べるには何が役立ちますか？

::option[仕事の所要時間と依存先の応答時間をあわせて確認します。]{#service-resource-saturation-next-observation-c .correct explanation="仕事が処理枠を長く占有する原因を絞り込むのに役立ちます。"}
::option[これ以上の証拠を集める前に処理能力を変更します。]{#service-resource-saturation-next-observation-a explanation="依存先で処理が止まっている場合は、処理能力を増やしても解決しないことがあります。"}
::option[リポジトリ内のロールを数えます。]{#service-resource-saturation-next-observation-b explanation="ロールを数えても、ワーカーが何を待っているかは分かりません。"}
:::

## まとめ

一時的に忙しいリソースと、待機する仕事がたまり続ける状態を区別できるようになりました。

1. ワーカーの稼働数をプール全体の処理能力と照らし合わせます。
2. 待ち行列とリクエストの挙動を時系列で比較します。
3. 余裕のないリソースをどの処理が占めているか調べます。
