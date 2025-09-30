---
index: 3
lang: "ja"
title: "traceroute"
meta_title: "traceroute - トラブルシューティング"
meta_description: "Linux の traceroute コマンドを使用して、ネットワークルートをトレースし、接続の問題をトラブルシューティングする方法を学びます。初心者向けに TTL とパケットルーティングを理解します。"
meta_keywords: "traceroute, Linux ネットワーキング，ネットワークトラブルシューティング，TTL, Linux コマンド，初心者，チュートリアル"
---

## Lesson Content

`traceroute`コマンドは、パケットがどのようにルーティングされるかを確認するために使用されます。これは、TTL（Time To Live）値を 1 から始めて徐々に増やしながらパケットを送信することで機能します。したがって、最初のルーターはパケットを受信し、TTL 値を 1 つ減らしてパケットを破棄します。ルーターは ICMP Time Exceeded メッセージを私たちに送り返します。次に、次のパケットは TTL が 2 になり、最初のルーターを通過しますが、2 番目のルーターに到達すると TTL は 0 になり、別の ICMP Time Exceeded メッセージを返します。Traceroute はこのように機能します。パケットを送信および破棄するにつれて、最終的に目的地に到達し、ICMP Echo Reply メッセージを受信するまで、パケットが通過するルーターのリストを構築します。

以下は traceroute の短いスニペットです。

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

各行は、あなたとターゲットの間にあるルーターまたはマシンを表します。ターゲットの名前とその IP アドレスが表示され、最後の 3 つの列は、そのルーターに到達するためのパケットの往復時間に対応します。デフォルトでは、ルートに沿って 3 つのパケットが送信されます。

## Exercise

練習は完璧をもたらします！ネットワークパスの発見とトラブルシューティングの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux での IP アドレス管理](https://labex.io/ja/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip`コマンドを使用してネットワーク設定を構成し、`traceroute`で接続を確認する練習をします。
2. **[Linux で ping と arp によるネットワーク層の相互作用を探る](https://labex.io/ja/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping`と`arp`がどのように機能するかを学び、`traceroute`がどのように動作するかの基礎となるネットワーク層の相互作用を理解します。

これらのラボは、実際のシナリオでネットワーク診断の概念を適用し、Linux ネットワークツールに自信を持つのに役立ちます。

## Quiz Question

ネットワークをホップする際に 1 つずつ減っていくものは何ですか？

## Quiz Answer

TTL
