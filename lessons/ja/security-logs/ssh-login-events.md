---
lesson_id: "ssh-login-events"
course_id: "security-logs"
lang: "ja"
order_index: 2
title: "SSH ログインの記録"
description: "SSH ログからログインの承認と拒否を読み取り、同じ接続の試行をまとめる方法を学びます。"
meta_title: "SSH ログインの記録 - セキュリティログ"
meta_description: "SSH ログから対象アカウント、接続元のアドレス、認証方法、結果を読み、接続 ID で試行を照合します。"
meta_keywords: "SSH ログイン, SSH ログ, ログイン成功, ログイン拒否, 認証方法"
---

**SSH** は Secure Shell の略で、ネットワーク越しに別のコンピューターへログインするために使います。接続を受けたマシンは、ログインの試行を一件ずつ記録できます。記録から、どのアカウントでログインしようとしたか、サーバーが提示された認証情報を受け入れたかが分かります。

## 結果を読む

次は SSH の模擬ログです。`login` が試行結果を表します。拒否はログイン時の確認に失敗したという意味で、承認は確認を通過したという意味です。

```text
t=09:13:48Z source=ssh host=web-01 account=alex login=rejected
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
```

最初の記録では `alex` での試行が拒否され、次の記録では同じアカウントでの試行が受け入れられています。各結果はそれぞれの試行に対応します。

:::single-choice{#ssh-login-events-outcome-order} 二つの記録からどんなことが分かりますか？

::option[後の試行はログイン時の確認を通過した。]{#ssh-login-events-outcome-later .correct explanation="二つ目には 09:14:02 に login=accepted と記録されています。"}
::option[両方の試行がログイン時の確認を通過した。]{#ssh-login-events-outcome-both explanation="最初の行には拒否された試行が記録されています。"}
::option[後の試行はログイン時の確認を通過しなかった。]{#ssh-login-events-outcome-failed explanation="拒否されたのは最初の試行です。二つ目の試行は受け入れられています。"}
:::

## アドレスと認証方法を読む

接続元のアドレスは、受け側のマシンがどこから接続を受けたかを示します。この例では `peer` に記録されています。ネットワークアドレスは共有されることがあるので、この項目だけでは誰が使ったかは分かりません。

```text
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
peer=192.0.2.10 method=publickey connection=17
```

二行目は同じ記録の続きです。`method` は、SSH が何を認証の根拠にしたかを示します。`password` の場合はパスワードを照合しました。`publickey` の場合は、接続元の機器が、そのアカウントでサーバーが認める鍵を使えると証明しました。

:::single-choice{#ssh-login-events-method-evidence} 受け入れられた試行について、どの結論を記録が裏付けていますか？

::option[サーバーはパスワードを使ったログインを受け入れた。]{#ssh-login-events-method-password explanation="パスワードの方式には別の表示があります。ここに記録されているのは公開鍵認証です。"}
::option[サーバーは、そのアドレスを使った人物を特定した。]{#ssh-login-events-method-person explanation="アドレスはホストが見た接続元を示します。実際に操作した人物は分かりません。"}
::option[サーバーは鍵を使ったログインを受け入れた。]{#ssh-login-events-method-key .correct explanation="login=accepted と method=publickey の両方が記録されています。"}
:::

## 接続ごとに試行を分ける

**接続**は、SSH がメッセージをやり取りするためのネットワーク上のつながりです。この例では、ホストが接続ごとに識別子を割り当てています。一つの接続で何度もログインを試すことができ、同じアドレスから別の接続を始めることもできます。

```text
t=09:13:48Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=rejected
t=09:13:55Z host=web-01 account=alex peer=192.0.2.10 connection=18 login=rejected
t=09:14:02Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=accepted
```

`web-01` では最初と最後の記録が、どちらも接続 17 を示しています。この識別子は、ホスト名と合わせて読みます。

![同じアドレスからの模擬 SSH 試行と接続 ID 17 および 18 を表示した LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/ssh-login-events/ssh-connections.png)

ターミナルに三つの模擬試行をまとめて表示しているので、接続番号を見比べられます。

:::single-choice{#ssh-login-events-group-connection} web-01 の接続 18 に当たるのはどの記録ですか？

::option[09:13:48 と 09:14:02 の試行。]{#ssh-login-events-group-seventeen explanation="どちらも接続番号は 17 です。"}
::option[09:13:55 の試行だけ。]{#ssh-login-events-group-eighteen .correct explanation="web-01 で接続 18 を示すのはこの行だけです。"}
::option[192.0.2.10 からの三つの試行すべて。]{#ssh-login-events-group-address explanation="同じアドレスに二つの接続番号が現れています。"}
:::

## ログイン成功後をたどる

ログインの成功は、SSH がそのアカウントの認証情報を受け入れたことを示します。その後を知るには、**セッション**の開始記録を探します。ログインセッションは認証後の活動をまとめます。ログイン成功の記録だけで分かるのは、認証が通ったことです。

:::single-choice{#ssh-login-events-after-accepted} ログインが受け入れられた後に、セッションが開始したかを知るには、どの記録が役立ちますか？

::option[同じログインを受け入れたとする別の記録。]{#ssh-login-events-after-accepted-again explanation="認証の結果を繰り返すだけです。"}
::option[別のホストで過去にそのアカウントが拒否された記録。]{#ssh-login-events-after-other-host explanation="それは別のマシンでの別の試行です。"}
::option[そのログインに対してセッションが開始したことを示す記録。]{#ssh-login-events-after-session .correct explanation="開始の記録は、ログイン成功の次に何が起きたかを示し、元のログインと関連付けられます。"}
:::

## まとめ

SSH の試行結果を読み、どの記録が同じ接続に属するか判断できるようになりました。

1. 受け入れられた試行と拒否された試行を区別する。
2. 接続元アドレスと認証方法で試行を説明する。
3. 接続 ID があるときは、ホストと接続の組み合わせで記録をまとめる。
4. セッションの記録を探し、ログイン成功の後に何が起きたかを確かめる。
