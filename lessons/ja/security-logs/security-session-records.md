---
lesson_id: "security-session-records"
course_id: "security-logs"
lang: "ja"
order_index: 4
title: "セッションの記録"
description: "セッションの開始と終了を対応付け、ログの抜粋から説明できる範囲を判断します。"
meta_title: "セッションの記録 - セキュリティログ"
meta_description: "Linux のセッション記録から開始と終了の組を探し、終了の記録がない場合に何を確かめるかを考えます。"
meta_keywords: "Linux セッション, セッション開始, セッション終了, セッション ID, ログの保存期間"
---

ログイン時の確認を通過すると、あるアカウントで認証が通ったことが分かります。**セッション**とは、ログインしてからログアウトや切断に至るまでの活動期間です。開始と終了の両方が記録されていれば、その時刻をログで確認できます。

## 開始の記録を読む

システムはマシン上のセッションを区別するために、**セッション ID** を割り当てられます。次の模擬ログでは、`web-01` の同じアカウントで二つのセッションが開始しています。このレッスンの時刻はすべて同じタイムゾーンです。

```text
t=09:14:05Z source=session host=web-01 account=alex session=42 state=opened
t=09:17:00Z source=session host=web-01 account=alex session=43 state=opened
```

一行目はセッション 42 が開始したことを示します。二行目は同じホストで別のセッション 43 が開始した記録です。

:::single-choice{#security-session-records-two-openings} 二つの開始記録から何が分かりますか？

::option[二つ目のセッションが始まった時点で、最初のセッションが終了した。]{#security-session-records-open-ended explanation="二つ目の記録は新たなセッションの開始です。最初のセッションの終了時刻は分かりません。"}
::option[別々のアカウントがホストにログインした。]{#security-session-records-open-accounts explanation="どちらの行も同じアカウントです。二つの活動期間は、セッションの項目で区別できます。"}
::option[同じアカウントで二つの別々のセッションが始まった。]{#security-session-records-open-two .correct explanation="どちらも alex で、web-01 上のセッション ID が異なります。"}
:::

## 開始と終了を対応付ける

二つの記録を結び付けるには、ホストとセッション ID を合わせて読みます。次の終了記録を先ほどの開始記録と比べてください。

```text
t=09:20:05Z source=session host=web-01 account=alex session=42 state=closed
```

`web-01` でのセッション 42 の開始と終了は、6 分離れています。この組から分かるのは記録された開始と終了の時刻です。その間に行われた操作の一覧ではありません。

![セッション 42 と 43 の模擬開始記録、および 42 の終了記録を表示した LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-session-records/session-records.png)

この画面では模擬の開始記録と終了記録をまとめて表示しています。

:::single-choice{#security-session-records-pair-ids} ホストと時刻はそのままで、終了の行が `session=43` だった場合、そのセッションが始まったのはいつですか？

::option[09:14:05。]{#security-session-records-pair-forty-two explanation="この開始記録は同じアカウントですが、セッション 42 のものです。"}
::option[09:17:00。]{#security-session-records-pair-forty-three .correct explanation="web-01 と ID 43 で二つ目の開始記録に一致します。開始は 09:17:00 です。"}
::option[09:20:05。]{#security-session-records-pair-end-time explanation="これは記録された終了時刻です。開始時刻は対応する開始記録から読みます。"}
:::

## 終了の記録がない場合

セッション 42 の元の終了記録に戻ります。抜粋は 09:21 で終わっており、セッション 43 に対応する終了はありません。抜粋が終わったとき、セッションはまだ有効だった可能性があります。終了の記録が時間範囲の外にあるか、この情報源には残っていない場合もあります。ログの**保存期間**とは、記録を保持し、確認できる期間です。

:::single-choice{#security-session-records-missing-close} この抜粋だけから、セッション 43 について何が言えますか？

::option[抜粋が終わった時点で、まだ有効だった。]{#security-session-records-missing-active explanation="その可能性はあります。ただし、終了の記録がないことだけでは状態を確定できません。"}
::option[この抜粋には、セッションの終了時刻が記録されていない。]{#security-session-records-missing-unknown .correct explanation="手元の記録についてはそう言えます。後の時刻の記録や別の情報源に終了時刻があるかもしれません。"}
::option[セッション 42 と同時に終了した。]{#security-session-records-missing-together explanation="終了が記録されたのは 42 です。ここには 43 に対応する終了記録がありません。"}
:::

## 調べたいことに合う情報源を選ぶ

過去の終了時刻が必要なら、同じホストから後の時間帯の抜粋を取得し、対応する終了を探します。セッションが今も有効か知りたいなら、そのホストで現在のセッション一覧を確認します。保存されたログと最新の一覧では、答えられる時点が異なります。

:::single-choice{#security-session-records-current-status} セッション 43 が今も有効かを知る必要があります。どの情報源が最も役立ちますか？

::option[web-01 の現在のセッション一覧。]{#security-session-records-current-list .correct explanation="ホストが今も有効と報告するセッションが分かります。"}
::option[開始記録の古いコピー。]{#security-session-records-current-opening explanation="セッションが始まったことは分かりますが、今も有効かは分かりません。"}
::option[web-01 のセッション 42 の終了記録。]{#security-session-records-current-other explanation="別のセッションの終了記録から、43 の状態は分かりません。"}
:::

## まとめ

セッションの記録を使って、記録された開始時刻と終了時刻を説明できるようになりました。

1. 開始の記録からホストとセッション ID を見つける。
2. 終了記録を該当する開始記録に対応付ける。
3. 終了の記録がないときに分からないことを明示する。
4. 問いに応じて、過去の記録か現在のセッション一覧を選ぶ。
