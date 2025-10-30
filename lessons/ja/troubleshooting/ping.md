---
index: 2
lang: "ja"
title: "ping"
meta_title: "ping - トラブルシューティング"
meta_description: "Linux の ping コマンドを使用してネットワーク接続をテストし、問題をトラブルシューティングする方法を学びます。効果的なネットワーク診断のために ICMP、TTL、および往復時間を理解します。"
meta_keywords: "Linux ping, ネットワーク接続，ICMP, TTL, Linux ネットワーキング，Linux 初心者，Linux チュートリアル，ping コマンド"
---

## Lesson Content

最もシンプルなネットワークツールの一つである **ping** は、パケットがホストに到達できるかどうかをテストするために使用されます。これは、ICMP エコー要求（タイプ 8）パケットを宛先ホストに送信し、ICMP エコー応答（タイプ 0）を待つことによって機能します。ホストが要求パケットを送信し、ターゲットから応答を受信すると、ping は成功です。例を見てみましょう。

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

この例では、`www.google.com` に到達できるかを確認するために ping を使用しています。`-c` フラグ（カウント）は、指定されたカウントに達した後、エコー要求パケットの送信を停止するために使用されます。

最初の部分は、64 バイトのパケットを 74.125.239.112 (google.com) に送信していることを示しており、残りの部分は通信の詳細を示しています。デフォルトでは、1 秒あたり 1 つのパケットを送信します。

### icmp_seq

`icmp_seq` フィールドは、送信されたパケットのシーケンス番号を示すために使用されます。この場合、3 つのパケットを送信し、3 つのパケットが戻ってきたことがわかります。ping を実行して、いくつかのシーケンス番号が欠落している場合、それは何らかの接続の問題が発生しており、すべてのパケットが通過していないことを意味します。シーケンス番号が順不同の場合、パケットがデフォルトの 1 秒を超えているため、接続が非常に遅い可能性があります。

### ttl

Time To Live (TTL) フィールドは、ホップカウンターとして使用されます。ホップするたびにカウンターが 1 つ減少し、ホップカウンターが 0 になると、パケットは消滅します。これはパケットに寿命を与えることを目的としており、パケットが永遠に移動し続けることを望んでいません。

### time

エコー要求パケットを送信してからエコー応答を受信するまでの往復時間です。

## Exercise

練習は完璧をもたらします！ネットワーク接続と `ping` コマンドの理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux で ping と arp を使ってネットワーク層の相互作用を探る](https://labex.io/ja/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` と `arp` を使用して、ネットワーク層とデータリンク層の相互作用を探り、デフォルトゲートウェイがリモートトラフィックをどのように処理するかを観察します。
2. **[Linux で IP アドレスの種類と到達可能性を探る](https://labex.io/ja/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping` と `ip a` を利用して、ローカルの TCP/IP スタックをテストし、パブリックインターネット接続を確認し、ネットワークの到達可能性を探ります。
3. **[Linux でネットワーク層の接続をシミュレートする](https://labex.io/ja/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - `ip addr` で静的 IP アドレスを割り当て、同じサブネットと異なるサブネットで `ping` を使って接続をテストする方法を学びます。

これらの演習は、ネットワークの到達可能性と `ping` コマンドの概念を実際のシナリオに適用し、Linux でのネットワーク診断に自信をつけるのに役立ちます。

## Quiz Question

往復時間の測定単位は何ですか？

## Quiz Answer

ms
