---
lesson_id: "security-event-correlation"
course_id: "security-logs"
lang: "ja"
order_index: 5
title: "イベントの相関分析"
description: "時刻、ホスト、アカウント、セッションを使って、セキュリティログを関連付けます。"
meta_title: "イベントの相関分析 - セキュリティログ"
meta_description: "短い SSH と sudo の記録を比較し、時刻をそろえて、どの証拠がイベント間のつながりを支えるかを判断します。"
meta_keywords: "イベントの相関分析, セキュリティログ, SSH ログイン, sudo の記録, 時刻, セッション ID"
---

ログインの記録には、あるマシンにログインしたことが残っています。別の記録には、コマンドが許可されたことが残っています。この二つは関係しているのでしょうか。**イベントの相関分析**では、記録を見比べて、活動同士に関連があるかを調べます。

## 二つの記録を読む

SSH を使うと別のマシンにログインできます。ログイン後は、`sudo` で別のアカウントとしてコマンドを実行する許可を求めることができます。次の二つは同じ日の模擬ログです。練習しやすいよう項目名がそろっています。本物のログでは項目名が異なったり、一部の項目がなかったりします。

```text
t=09:14:02Z      source=ssh   host=web-01 account=alex session=42 login=accepted
t=11:15:10+02:00 source=sudo  host=web-01 account=alex session=42 decision=allowed
```

`source` はイベントを報告したツール、`host` はそれが起きたマシンを示します。どちらの記録も、アカウント `alex` の活動を示しています。そのアカウントを使った人物を特定するには、別の証拠が必要です。

:::single-choice{#security-event-correlation-account-evidence} チームの人が「Alex 本人が sudo を要求した」と言っています。今の記録だけで何が確かめられますか？

::option[Alex 本人が sudo を要求した。]{#security-event-correlation-account-person explanation="アカウント名だけでは、それを使った人物を特定できません。"}
::option[二つの異なるアカウントに関する活動が記録されている。]{#security-event-correlation-account-different explanation="account はどちらも alex です。source の違いは報告元のツールの違いです。"}
::option[二つのイベントは同じアカウントに関するものだ。]{#security-event-correlation-account-shared .correct explanation="どちらの記録にも alex とあります。誰が使ったかを知るには、さらに証拠が必要です。"}
:::

## イベントの時刻を比較する

`t` には記録時刻が入っています。一つ目の `Z` は比較の基準にできる UTC を示します。二つ目の `+02:00` は、表示時刻が UTC より 2 時間進んでいるという意味です。`11:15:10` から 2 時間引くと、UTC の `09:15:10` になります。

`09:14:02` と `09:15:10` を比べると、先に記録されたのはログインです。時刻が近くても、それぞれ別のログインに関するイベントかもしれません。

:::single-choice{#security-event-correlation-time-order} 別の日に、ログインが `09:14Z`、要求が `11:13+02:00` と記録されました。どちらが先ですか？

::option[要求が 1 分先。]{#security-event-correlation-time-request-first .correct explanation="要求時刻から 2 時間引くと 09:13 UTC です。ログインは 09:14 UTC でした。"}
::option[ログインが 1 分先。]{#security-event-correlation-time-login-first explanation="要求を換算すると 09:13 UTC になり、09:14 UTC のログインより 1 分早くなります。"}
::option[ログインが 2 時間近く先。]{#security-event-correlation-time-unadjusted explanation="この答えは表示時刻をそのまま比べています。順序を決める前に、両方を UTC に換算します。"}
:::

## ホストとセッションを照合する

**セッション**は、ログインからログアウトや切断までの活動期間です。この練習では、SSH の記録に受け入れられたログインにひも付くセッション ID が含まれます。二つの情報源は、同じホストの同じログインに対して共通の ID を使っています。最初の二つの記録にある `host=web-01` と `session=42` が、ログインと要求を一つのセッションに結び付けます。

この例で、セッション番号はそのホストの内側でだけ意味を持ちます。次の記録はアカウントとセッション番号が同じで、時刻も数秒後です。

```text
t=09:15:18Z source=sudo host=web-02 account=alex session=42 decision=allowed
```

![web-01 と web-02 の模擬ログ、および 09:15:10 UTC への換算を表示した LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-event-correlation/utc-correlation.png)

ターミナルは三つの模擬記録を表示し、Ubuntu の `date` で UTC への換算を確認しています。

:::single-choice{#security-event-correlation-host-scope} 三つ目の記録は、最初の SSH セッションとどう関係しますか？

::option[アカウントが同じで時刻も近いので、同じセッションの記録だ。]{#security-event-correlation-host-scope-account explanation="別々のホストでも、同じアカウント名の活動を数秒差で記録することがあります。"}
::option[ホストが違うので、別のセッションの記録だ。]{#security-event-correlation-host-scope-machine .correct explanation="web-02 のセッション 42 はそのホストのものです。最初のログインは web-01 で行われました。"}
::option[セッション番号が同じなので、同じセッションの記録だ。]{#security-event-correlation-host-scope-session explanation="この例のセッション番号はホストごとに使われます。ここではホスト名が異なります。"}
:::

## 記録で裏付けられることを述べる

`web-01` でログインが受け入れられ、そのセッション中に `sudo` がコマンドの実行を許可しました。今の証拠が示すのはここまでです。コマンドがどう終わったかを知るには、実行結果の記録を探します。一つのセッションに複数のコマンドが含まれることがあるので、結果を該当の要求と結び付けます。一致する記録がなければ、結果は不明のままにします。

:::single-choice{#security-event-correlation-completion-evidence} そのコマンドが成功したかどうかを知るには、どんな記録が必要ですか？

::option[同じセッションで動いた別のコマンドの結果。]{#security-event-correlation-completion-other-command explanation="一つのセッションで複数のコマンドを実行できます。調べている要求に対応する結果が必要です。"}
::option[要求の許可を示すもう一つの記録。]{#security-event-correlation-completion-permission explanation="それは実行の許可を裏付けます。結果を知るには別途記録が必要です。"}
::option[その要求で指定されたコマンドの結果の記録。]{#security-event-correlation-completion-result .correct explanation="該当する結果の記録から、コマンドがどう終わったかが分かります。"}
:::

別の認証記録や sudo の記録を絞り込んで比べるには、[システムログ分析](https://labex.io/tutorials/linux-system-log-analysis-656124)を試してください。

## まとめ

複数のセキュリティログを使って判断を述べ、次に何を確認すべきかを説明できるようになりました。

1. イベントに記録されたアカウントを見つける。
2. 比較の前にタイムゾーンをそろえる。
3. ホストとセッションを組み合わせて活動を結び付ける。
4. 記録が裏付けることを述べ、残る疑問に答えるための証拠を探す。
