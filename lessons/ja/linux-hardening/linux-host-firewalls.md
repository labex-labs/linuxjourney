---
lesson_id: "linux-host-firewalls"
course_id: "linux-hardening"
lang: "ja"
order_index: 5
title: "ホストファイアウォール"
description: "ホストファイアウォールの簡単なポリシーを読み、適切な場所から接続を確認する方法を学びます。"
meta_title: "ホストファイアウォール - Linux の堅牢化"
meta_description: "ホストファイアウォールの簡単なポリシーを読み、適切な場所から接続を確認する方法を学びます。"
meta_keywords: "ホストファイアウォール, Linux の堅牢化, サイバーセキュリティ, Linux Journey"
---

**ホストファイアウォール**は、送信元アドレス、プロトコル、宛先ポートなどに基づいて、受信トラフィックを許可または拒否できます。まず、サービスにどの通信が必要かを決めます。

## ポリシーの例を読む

次は、あるホストのポリシーを簡略化した例です。`192.0.2.0/24` のスラッシュ以降は IPv4 アドレスの範囲を表します。この例では `192.0.2.44` は範囲内で、`198.51.100.8` は範囲外です。

```text
Allow TCP port 443 from any source.
Allow TCP port 22 from 192.0.2.0/24.
Deny other new inbound connections.
```

ポート 443 は公開サイト用です。ポート 22 は保守ネットワーク用に確保されています。デフォルトの扱いは、二つの許可ルールのどちらにも当てはまらない接続に適用されます。

:::single-choice{#linux-host-firewalls-match-trusted-network} どの新規接続が保守用のルールに一致しますか？

::option[198.51.100.8 から TCP ポート 22 への接続です。]{#linux-host-firewalls-match-trusted-network-b explanation="ポートは一致しますが、送信元は管理用ネットワークの範囲外です。"}
::option[192.0.2.44 から TCP ポート 443 への接続です。]{#linux-host-firewalls-match-trusted-network-c explanation="この接続は公開 Web 用のルールに一致します。"}
::option[192.0.2.44 から TCP ポート 22 への接続です。]{#linux-host-firewalls-match-trusted-network-a .correct explanation="宛先ポートと送信元の範囲がともに一致します。"}
:::

![公開 HTTPS と制限された保守アクセスを示す、模擬ホストファイアウォールのポリシー](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-host-firewalls/sample-policy.png)

## ポリシーと待ち受けの両方を調べる

許可された接続でも、そのポートでプログラムが待ち受けていなければ失敗します。待ち受けが正常でも、ファイアウォールが拒否する経路からは接続できません。ポリシーを読み、待ち受け状態は別途確認します。

:::single-choice{#linux-host-firewalls-allowed-but-failed} ルールではポート 443 を許可していますが、ホスト上でそのポートを待ち受けるプログラムが動いていません。何を確認しますか？

::option[クライアントが保守用 SSH を使うべきかどうかです。]{#linux-host-firewalls-allowed-but-failed-a explanation="SSH は別のサービスです。"}
::option[公開 Web サービスが想定したポートで待ち受けているかどうかです。]{#linux-host-firewalls-allowed-but-failed-b .correct explanation="ファイアウォールで許可しても、サービスが待ち受けを開始するわけではありません。"}
::option[リクエストが保守ネットワークから来たかどうかです。]{#linux-host-firewalls-allowed-but-failed-c explanation="この例の公開 Web 用ルールは、すべての送信元を許可します。"}
:::

## 確認を安全に行う計画を立てる

管理された変更を検証する間は、正当な保守経路を確保します。保守ネットワークから許可された経路をテストします。次に、そのネットワークの外にある承認済みの検証場所からは接続できないことを確かめます。各テストの送信元、接続先、期待する結果を記録します。

:::single-choice{#linux-host-firewalls-verification-pair} 想定した SSH の制限を確かめるには、どの二つのテストを行いますか？

::option[許可を得て、保守ネットワークの内側と外側からポート 22 を確認します。]{#linux-host-firewalls-verification-pair-c .correct explanation="これらの接続で、許可と拒否の両方を確認できます。"}
::option[同じ許可済みマシンから SSH 接続を 2 回試します。]{#linux-host-firewalls-verification-pair-a explanation="許可される場合を 2 回確認することになります。"}
::option[ブラウザーから公開のトップページに 2 回アクセスします。]{#linux-host-firewalls-verification-pair-b explanation="確認できるのは公開用ポートへのアクセスです。"}
:::

## まとめ

ホストファイアウォールのルールとサービスの状態をあわせて判断できるようになりました。

1. プロトコル、宛先、送信元がルールに合うかを確認します。
2. 許可を受けたサービスが待ち受けているかを確認します。
3. 想定したアクセスと制限の両方を検証します。
