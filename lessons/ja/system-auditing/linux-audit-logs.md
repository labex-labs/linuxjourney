---
lesson_id: "linux-audit-logs"
course_id: "system-auditing"
lang: "ja"
order_index: 2
title: "Linux の監査ログ"
description: "一つの操作を記述する Linux の監査レコードをまとめて読む方法を学びます。"
meta_title: "Linux の監査ログ - システム監査"
meta_description: "一つの操作を記述する Linux の監査レコードをまとめて読む方法を学びます。"
meta_keywords: "Linux 監査ログ, Linux Audit, システム監査, サイバーセキュリティ, Linux Journey"
---

Linux Audit は一つのイベントについて複数のレコードを書き出すことがあります。ある行は操作を説明し、別の行はパスを示します。何を示すかを判断する前に、関連する行をまとめます。

## 同じイベントの情報を読む

次は、同じホストと日付から取った練習用の簡略レコードです。監査イベントを参照する値では、コロンの後ろの番号が、タイムスタンプとイベント ID が同じレコードをまとめる手掛かりになります。この二つの行は同じイベントに属します。

```text
type=SYSCALL msg=audit(1763456400.120:42) success=yes auid=1001 euid=0
type=PATH    msg=audit(1763456400.120:42) name="/etc/journey/site.conf"
```

最初の行には、操作の結果とアカウントの情報があります。パスを示す行には、イベントに関連するファイルが記録されています。

:::single-choice{#linux-audit-logs-group-rows} この例で、操作とパスをどの情報で対応付けられますか？

::option[SYSCALL と PATH の二つのレコード種別だけです。]{#linux-audit-logs-group-rows-a explanation="種別は各行の役割を示します。同じ種別はさまざまなイベントに含まれます。"}
::option[両方の行が type で始まることです。]{#linux-audit-logs-group-rows-c explanation="イベントが異なっていても、各行に種別が付くことがあります。"}
::option[同じホストのレコードで、監査イベントを参照する値が一致することです。]{#linux-audit-logs-group-rows-b .correct explanation="その値によってイベント 42 を記述する行をまとめられます。"}
:::

![同じ監査イベントを参照する、Linux Audit の模擬 SYSCALL 行と PATH 行](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/linux-audit-logs/grouped-event.png)

## 二つのユーザー ID を読み分ける

この例で `auid` は監査用のログインユーザー ID、`euid` は操作時の実効ユーザー ID です。プログラムは、ログイン時と異なる実効ユーザーで動作する場合があります。数値の ID はホスト上のアカウントを示します。そのアカウントを使った人を特定するには、追加の記録が必要なことがあります。

:::single-choice{#linux-audit-logs-identify-login} このサンプルで、監査用のログインユーザーを示すフィールドはどれですか？

::option[euid 0 です。]{#linux-audit-logs-identify-login-b explanation="このフィールドは、イベントが起きたときのプログラムの実効ユーザーを示します。"}
::option[auid 1001 です。]{#linux-audit-logs-identify-login-a .correct explanation="auid は監査用のログインユーザー ID で、euid は実効ユーザー ID です。"}
::option[イベント番号の 42 です。]{#linux-audit-logs-identify-login-c explanation="その番号はレコードをまとめるために使い、アカウントの識別には使いません。"}
:::

## 証拠が示す範囲で判断する

結果のフィールドは、記録された操作が成功したことを示します。イベント全体を読んで、その操作を特定します。内容の変化を確かめるには、ファイルを既知の基準と比較します。

:::single-choice{#linux-audit-logs-useful-follow-up} 承認済みのファイルと内容が異なるかを判断するには、何が役立ちますか？

::option[承認済みの参照コピーや整合性の記録との比較です。]{#linux-audit-logs-useful-follow-up-c .correct explanation="ファイル自体にどのような変化があったかを確認できます。"}
::option[別の操作の成功を示す監査レコードです。]{#linux-audit-logs-useful-follow-up-a explanation="別の操作が記録されたことは分かりますが、現在の内容と承認済みコピーの比較はできません。"}
::option[同じイベントのログインアカウント ID です。]{#linux-audit-logs-useful-follow-up-b explanation="ログイン ID はどのアカウントが関係したかを調べる手掛かりですが、ファイルの内容の変化は分かりません。"}
:::

## まとめ

複数のレコードをまとめて、一つの監査イベントを読み取れるようになりました。

1. ホストと監査イベントを参照する値でレコードを照合します。
2. ログインユーザーと実効ユーザーを区別します。
3. 記録された結果だけで判断できないときは、次の確認項目を選びます。
