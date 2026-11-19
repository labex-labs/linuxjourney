---
lesson_id: "linux-listening-services"
course_id: "linux-hardening"
lang: "ja"
order_index: 4
title: "待ち受け中のサービス"
description: "Linux の待ち受けアドレスを読み、どこから接続できるかを確認する方法を学びます。"
meta_title: "待ち受け中のサービス - Linux の堅牢化"
meta_description: "Linux の待ち受けアドレスを読み、どこから接続できるかを確認する方法を学びます。"
meta_keywords: "待ち受けサービス, TCP, Linux の堅牢化, サイバーセキュリティ, Linux Journey"
---

サービスは、特定のアドレスとポートで接続を待つことができます。**リスナー**とは、接続を受け付けられる状態にあるソケットです。そのアドレスは、どこから接続できるかを考える手掛かりになります。

## TCP リスナーを一覧表示する

Linux の練習用ホストで、次の読み取り専用コマンドを実行します。オプションにより、`ss` は待ち受け中の TCP ソケットのアドレスとポートを数値で表示します。

```bash
$ ss -lnt
```

ローカルアドレスの列を見ます。次の例では、Web のプレビューに `127.0.0.1:8091` を使っています。ポートは 8091 です。このアドレスは**ループバック**と呼ばれ、ホスト自身を指します。

:::single-choice{#linux-listening-services-local-listener} この例で、同じホスト上のブラウザーからプレビューを見るには、どのアドレスに接続しますか？

::option[0.0.0.0:8091 です。]{#linux-listening-services-local-listener-a explanation="この表記は待ち受け方の指定に使うもので、ここで示されたローカルの接続先は別にあります。"}
::option[127.0.0.1:8091 です。]{#linux-listening-services-local-listener-b .correct explanation="サービスはそのループバックアドレスとポートで待ち受けています。"}
::option[無関係なサーバーのポート 80 です。]{#linux-listening-services-local-listener-c explanation="この例のリスナーはホスト自身のポート 8091 を使っています。"}
:::

![練習用リスナーがループバックのポート 8091 で待ち受けていることを示す LabEx の ss 出力](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-listening-services/loopback-listener.png)

## すべてのインターフェースでの待ち受けを読む

IPv4 のローカルアドレスが `0.0.0.0:8091` なら、サービスはホスト上のすべての IPv4 インターフェースで待ち受けています。別のコンピューターから到達できるインターフェースも含まれることがあります。リスナーの一覧は、プロセスがホスト上のどのアドレスで接続を受け付けるかを示します。別のコンピューターからの接続は、ファイアウォールのルールや経路によって制限されます。

:::single-choice{#linux-listening-services-all-interfaces} あるサービスのアドレスが 127.0.0.1 から 0.0.0.0 に変わりました。ポートは同じです。何が変わりましたか？

::option[より多くの IPv4 インターフェースで待ち受けられます。]{#linux-listening-services-all-interfaces-a .correct explanation="受信接続を受け付けるローカルアドレスの範囲が広がります。"}
::option[別のポートで待ち受けるようになりました。]{#linux-listening-services-all-interfaces-b explanation="ポート番号は変わりません。"}
::option[どのネットワークからもすぐにアクセスできることが保証されます。]{#linux-listening-services-all-interfaces-c explanation="どの経路で到達できるかは、引き続きネットワークのルールや経路で決まります。"}
:::

## 想定する経路から確認する

スタッフ向けの内部サービスは、一つのネットワークだけで使う場合があります。対象ネットワークからアクセスを確認します。制限が機能している証拠が必要なら、その外側にある承認済みの場所からも確認します。待ち受けと経路の両方を確かめます。ホスト上の一覧だけでは、離れたクライアントで何が起きたか分かりません。

:::single-choice{#linux-listening-services-verify-from-client} すべてのローカルインターフェースで待ち受けていることが分かりました。スタッフの端末からアクセスできるかを実際に確認するにはどうしますか？

::option[ホスト名をもう一度読み取ります。]{#linux-listening-services-verify-from-client-a explanation="ホスト名を見ても、ネットワーク経路は検証できません。"}
::option[リスナーの個数を数えます。]{#linux-listening-services-verify-from-client-b explanation="個数からはスタッフ端末からの接続可否は分かりません。"}
::option[許可されたリクエストをスタッフ用ネットワークから送ります。]{#linux-listening-services-verify-from-client-c .correct explanation="想定するアクセス経路を検証できます。"}
:::

Linux ホストで待ち受け中のサービスを調べる練習には、[Linux Security for DevSecOps](https://labex.io/courses/linux-security-for-devsecops)の「待ち受けサービスを監査する」から始めてください。

## まとめ

待ち受けアドレスから、どこで接続を確認すべきか判断できるようになりました。

1. ローカルの TCP リスナーを安全に一覧表示します。
2. ループバックと、すべての IPv4 インターフェースでの待ち受けを区別します。
3. 対象クライアントが使う場所から接続を確認します。
