---
lesson_id: "sudo-events"
course_id: "security-logs"
lang: "ja"
order_index: 3
title: "sudo の記録"
description: "誰がどのアカウントでコマンドを実行しようとして、許可されたかどうかを sudo の記録から読み取ります。"
meta_title: "sudo の記録 - セキュリティログ"
meta_description: "sudo の記録を読み、要求元のアカウント、実行先のアカウント、コマンド、許可の判断を区別します。"
meta_keywords: "sudo の記録, sudo ログ, 実行権限, 実行先アカウント, Linux の権限"
---

一般のアカウントでログインした後に、より強い権限が必要な作業が出てくることがあります。`sudo` を使うシステムでは、利用者が別のアカウントとしてコマンドを実行するよう求められます。その要求の記録を読むと、何が求められ、システムがどう判断したかが分かります。

## 二つのアカウントを見つける

次の模擬ログでは、要求したアカウントを `account`、実行に使う予定のアカウントを `target` で示します。`root` アカウントにはシステム管理権限があります。`sudo` では `backup` のように、別の実行先アカウントも指定できます。

```text
t=09:15:10Z source=sudo host=web-01 account=alex target=root
command=systemctl status nginx decision=allowed session=42
```

二行目は同じ記録の続きです。この例では `alex` が `root` としてコマンドを実行するよう求めました。

:::single-choice{#sudo-events-account-target} `account=sam target=backup` とある場合、誰がどのアカウントでコマンドを実行するよう求めましたか？

::option[backup が sam として実行するよう求めた。]{#sudo-events-target-swapped explanation="account は要求元、target は実行に使う予定のアカウントです。"}
::option[sam が backup として実行するよう求めた。]{#sudo-events-target-backup .correct explanation="account で要求元を、target でコマンドが使うアカウントを確認します。"}
::option[sam が root として実行するよう求めた。]{#sudo-events-target-root explanation="root は指定できるアカウントの一つです。この記録が示すのは backup です。"}
:::

## 要求されたコマンドを読む

`command` は、何のコマンドを実行しようとしたかを示します。例の `systemctl status nginx` は、Nginx の Web サービスの現在の状態を表示する要求です。別の記録に `systemctl restart nginx` とあれば、そのサービスを停止して起動し直す要求です。どちらも同じサービスを指定していますが、操作は異なります。

:::single-choice{#sudo-events-command-scope} Web サービスの稼働状態を変えるよう求めているのはどれですか？

::option[`systemctl restart nginx`]{#sudo-events-command-restart .correct explanation="restart は、サービスを停止して起動し直す操作です。稼働状態が変わることがあります。"}
::option[`systemctl status nginx`]{#sudo-events-command-status explanation="status はサービスの情報を表示します。再起動を求めるものではありません。"}
::option[どちらも nginx を指定しているので、両方。]{#sudo-events-command-both explanation="サービス名は同じです。何を求めているかは操作名で分かります。"}
:::

## 許可の判断を読む

**ポリシー**とは、`sudo` が要求を許可するか決めるためのルールです。この例では、`decision=allowed` はポリシーが要求を許可したこと、`decision=denied` は `sudo` が拒否したことを示します。

```text
t=09:16:00Z source=sudo host=web-01 account=alex target=root
command=systemctl restart nginx decision=denied session=42
```

許可の判断は、実行してよいことを示すものです。コマンドの結果を知りたい場合は、システムが提供する結果の記録を探してください。

![ステータス確認の許可と再起動の拒否を示す模擬 sudo ログを表示した LabEx ターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/sudo-events/sudo-decisions.png)

二つの模擬記録で、要求されたコマンドと許可の判断を比べてください。

:::single-choice{#sudo-events-denied-request} 二つ目の例では、再起動の要求はどうなりましたか？

::option[sudo が再起動の要求を拒否した。]{#sudo-events-denied-refused .correct explanation="コマンドは要求された操作、denied は許可の判断を示しています。"}
::option[サービスの再起動が成功した。]{#sudo-events-denied-success explanation="この記録は拒否を示します。再起動が成功した証拠はありません。"}
::option[前の状態確認も拒否された。]{#sudo-events-denied-earlier explanation="許可の判断は要求ごとに行われます。前の記録では allowed です。"}
:::

## ログインしたアカウントにも注目する

両方の例が要求元として `alex` を示し、`session=42` を含んでいます。この番号はログインセッション、つまりログイン後の活動の期間を指します。前後のログイン記録を探すときの手がかりになります。各例の実行先はその要求一つに限って当てはまります。要求を説明するときは、要求元と実行先を合わせて読みます。

:::single-choice{#sudo-events-session-interpretation} 最初の例に合う説明はどれですか？

::option[root が直接ログインし、セッション 42 を開始した。]{#sudo-events-session-root-login explanation="これは sudo の記録です。実行先フィールドは別のログインを示すものではありません。"}
::option[Alex がセッション内のすべてのコマンドを root 権限で実行するよう求めた。]{#sudo-events-session-all-commands explanation="記録はコマンド一つを指定しています。セッション内のすべてのコマンドには当てはまりません。"}
::option[Alex がセッション 42 で、指定した一つのコマンドを root として実行するよう求めた。]{#sudo-events-session-one-command .correct explanation="要求元、実行先、コマンド、セッションの各項目が、この説明を裏付けています。"}
:::

## まとめ

sudo の記録を読み、実行が許可されたこととコマンドの結果を区別できるようになりました。

1. 要求元と実行先のアカウントを見つける。
2. コマンドの項目から具体的な要求を説明する。
3. 要求が許可されたか、拒否されたかを見分ける。
4. 要求の説明にログインセッションの情報も含める。
