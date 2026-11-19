---
lesson_id: "incident-timelines"
course_id: "incident-response"
lang: "ja"
order_index: 3
title: "インシデントのタイムライン"
description: "証拠を一つの時系列に並べ、不確かな時刻にはその旨を示す方法を学びます。"
meta_title: "インシデントのタイムライン - インシデント対応"
meta_description: "証拠を一つの時系列に並べ、不確かな時刻にはその旨を示す方法を学びます。"
meta_keywords: "タイムライン, 時刻, インシデント対応, サイバーセキュリティ, Linux Journey"
---

インシデントのタイムラインでは、異なる情報源の観測結果を時刻順に並べます。タイムゾーンをそろえ、記録には元のタイムスタンプも残します。順序が分かると、どの出来事が関係しているかを検討できます。

## タイムスタンプを変換する

この例では、Web の報告は UTC、デプロイ記録は UTC より 2 時間進んだオフセットで記録されています。

```text
Deployment record:  2026-11-19 11:17:00 +02:00
Web report:         2026-11-19 09:22:00 UTC
```

GNU 版の date を使う Linux システムでは、`-d` が指定したタイムスタンプを読み取り、`-u` が UTC での出力を指定します。`+` で始まる引数は表示形式を指定します。

```bash
$ date -u -d '2026-11-19 11:17:00+02:00' '+%Y-%m-%d %H:%M:%S UTC'
```

結果は `2026-11-19 09:17:00 UTC` です。この例では、Web の報告より 5 分早い時刻です。

:::single-choice{#incident-timelines-earlier-event} タイムゾーンをそろえた結果、どちらの記録が先ですか？

::option[デプロイ記録です。]{#incident-timelines-earlier-event-a .correct explanation="オフセットを変換すると 09:17 UTC になり、09:22 の報告より前です。"}
::option[Web の報告です。]{#incident-timelines-earlier-event-b explanation="変換前は、タイムゾーンの違いによって時の数字が小さく見えています。"}
::option[二つはまったく同じ時刻です。]{#incident-timelines-earlier-event-c explanation="タイムゾーンをそろえると、二つの時刻には 5 分の差があります。"}
:::

![GNU date でオフセット +02:00 の 11:17 を 09:17 UTC に変換した出力](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-timelines/normalize-utc.png)

## 観測時刻と推定時刻を区別する

最初の失敗が 09:19 ごろだったという報告もあります。その時刻は推定として残します。利用者が報告した時刻と、最初にリクエストが失敗した実際の時刻は別です。それぞれの行に、情報源と時刻の精度を記載します。

:::single-choice{#incident-timelines-estimated-time} チームメンバーから 09:19 ごろと聞きました。どのように記録しますか？

::option[ログで確認された正確な時刻、09:19:00 として記録します。]{#incident-timelines-estimated-time-a explanation="情報源が示しているのは推定時刻です。"}
::option[情報源を記載せずに、イベントだけを記録します。]{#incident-timelines-estimated-time-c explanation="時刻をどの程度信頼できるか判断するには、情報源が必要です。"}
::option[その報告に基づくおおよその時刻として記録します。]{#incident-timelines-estimated-time-b .correct explanation="情報源が伝えた内容と、時刻の精度を両方残せます。"}
:::

## 出来事を並べ、原因は別に調べる

デプロイの後にサービスで問題が起きても、デプロイが原因とは限りません。影響を受けたルートに変更があったか、ほかのシグナルが関連性を裏付けるかを調べます。タイムラインと一緒に、まだ答えが出ていない問いも残します。

:::single-choice{#incident-timelines-timeline-cause} 記録を時刻順に並べるだけで何が分かりますか？

::option[デプロイが公開サービスの障害を引き起こしました。]{#incident-timelines-timeline-cause-a explanation="順序は手掛かりになりますが、それだけで原因は特定できません。"}
::option[記録されたデプロイは、Web の報告より前です。]{#incident-timelines-timeline-cause-c .correct explanation="記録から、この前後関係を確認できます。"}
::option[ほかに関連するイベントはあり得ません。]{#incident-timelines-timeline-cause-b explanation="タイムラインに並べたのは、選んだ観測結果です。"}
:::

## まとめ

証拠と不確かさの両方が分かるタイムラインを作れるようになりました。

1. 記録された時刻を、一つのタイムゾーンにそろえます。
2. 各時刻の情報源を記載し、推定時刻にはその旨を示します。
3. 出来事の順序から、次に何を確認するか決めます。
