---
lesson_id: "security-events"
course_id: "security-logs"
lang: "ja"
order_index: 1
title: "セキュリティイベント"
description: "セキュリティイベント、その出来事を記録したログ、確認を促すアラートを区別します。"
meta_title: "セキュリティイベント - セキュリティログ"
meta_description: "短い Linux セキュリティログを読み、アラートと比較して、記録が足りないときに何を確かめるか判断します。"
meta_keywords: "セキュリティイベント, セキュリティログ, ログの記録, アラート, Linux ログ"
---

サーバーがログインの失敗を報告しました。何が起きて、そこから何が分かるのでしょうか。まず、マシンが記録した事実と、そこから導く結論を分けて考えます。

## イベントとログの記録

**イベント**とは、ログインの拒否など、実際に起きた出来事です。**ログの記録**は、その出来事を後から読める形で残したものです。**ログ**にはこのような記録が集まっています。このコースでは読み方を練習できるように、項目名をそろえた模擬ログを使います。実際のツールでは、項目名や保存先が異なることがあります。

```text
t=08:55:00Z source=ssh host=web-01 account=alex login=rejected
```

この記録によると、アカウント `alex` でリモートログインを試みましたが、拒否されました。試行が終わった後も、保存された記録を読めます。異なる情報源の時刻を比較する方法は後のレッスンで扱います。

![web-01 で alex の SSH ログインが拒否されたことを示す模擬ログを表示した LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-events/event-fields.png)

LabEx のターミナルには、テキストファイルに保存した同じ模擬ログを表示しています。

:::single-choice{#security-events-event-versus-record} この例のうち、イベントそのものはどれですか？

::option[拒否を記載した、保存済みの行。]{#security-events-event-line explanation="この行は、イベントの後から読める記録です。"}
::option[保存した行を後で確認すること。]{#security-events-event-review explanation="確認は後から行う作業です。この行が記録した出来事は、ログインの拒否です。"}
::option[ログインの試行が拒否されたこと。]{#security-events-event-attempt .correct explanation="サーバーで実際に起きたのは拒否です。ログの行は、その出来事を残したものです。"}
:::

## 項目を読む

**フィールド**は、一つの記録に含まれる個別の項目です。この例では、`t` が記録時刻、`host` がイベントの発生したマシン、`source` が報告元のツールを表します。`account` はアカウント名、`login` はログインの試行結果です。

:::single-choice{#security-events-field-host} 拒否されたログインを記録したのはどのマシンか調べたいとします。そのマシンを示す値はどれですか？

::option[account フィールドの `alex`。]{#security-events-field-host-account explanation="account は、試行に関係したアカウントを示します。"}
::option[host フィールドの `web-01`。]{#security-events-field-host-web .correct explanation="host はイベントが発生したマシンを示します。"}
::option[source フィールドの `ssh`。]{#security-events-field-host-tool explanation="source はイベントを報告したツールを示します。"}
:::

## アラートと検知ルール

**アラート**は、確認が必要かもしれない状況を知らせます。たとえば、同じホストの同じアカウントで、5 分以内にログインが 3 回拒否されたときにアラートを出すルールを設定できます。このルールはアカウント、ホスト、時間で記録をまとめます。アラートはその条件に当てはまったという意味です。単に誰かが何度かパスワードを打ち間違えたのかもしれません。

:::single-choice{#security-events-alert-interpretation} web-01 の alex で 3 回失敗したため、アラートが出ました。ここから何が分かりますか？

::option[記録された失敗がルールの条件を満たした。]{#security-events-alert-condition .correct explanation="アラートは調べる価値のあるパターンを示します。誰が起こしたかは、このルールでは分かりません。"}
::option[3 人がそれぞれログインを試した。]{#security-events-alert-people explanation="同じ人が 3 回試した可能性もあれば、別々の人かもしれません。ルールは記録の件数を数えています。"}
::option[誰かが 3 回試した後で、ログインに成功した。]{#security-events-alert-success explanation="このルールは拒否された試行を数えます。その後に成功したかは分かりません。"}
:::

## 次に確かめることを選ぶ

`alex` が後でログインしたかを知りたい場合は、失敗した時刻より後の `web-01` のログイン結果を探します。結論を出す前に、手元の記録がどこまでの時間をカバーしているかを確認してください。ログのエクスポートは選んだ記録のコピーなので、必要な時刻より前で終わっている場合があります。

:::single-choice{#security-events-next-record} 手元のエクスポートは 09:00 までです。09:05 に成功したログインがあったかを確認するには、何を探しますか？

::option[同じエクスポートを新しい順に並べたもの。]{#security-events-next-sort explanation="順番は変わりますが、09:00 より後の記録は追加されません。"}
::option[09:05 を含む web-01 のログイン記録。]{#security-events-next-window .correct explanation="確認するイベントに対応する情報源と、その時刻を含む記録が必要です。"}
::option[09:00 より前の失敗回数をもう一度集計したもの。]{#security-events-next-count explanation="それは、より前の時間帯の別の結果です。"}
:::

## まとめ

セキュリティログを読み、アラートを受けて次に確認することを選べるようになりました。

1. 実際のイベントと、それを記録した行を区別する。
2. サンプルからアカウント、ホスト、試行結果を見つける。
3. アラートのルールを読んで、何が観測されたかを理解する。
4. 情報源と時間範囲が、知りたいことに合っているか確かめる。
