---
index: 2
lang: "ja"
title: "ping"
meta_title: "ping - トラブルシューティング"
meta_description: "Linux の ping コマンドを使用してネットワーク接続性をテストする方法を学びます。このガイドでは、icmp_seq、TTL、往復時間を含む ping の出力を解説します。ping シーケンスを解釈してネットワークの問題を診断する方法を理解しましょう。"
meta_keywords: "Linux ping, ネットワーク接続性，ICMP, TTL, ping コマンド，icmp_seq, ping seq, icmp seq, icmp_seq 意味，ping icmp_seq, Linux ネットワーキング"
---

## Lesson Content

ping\*\*コマンドは、リモートホストが IP ネットワーク経由で到達可能かどうかをテストするために使用される、最も基本的なネットワーキングユーティリティの 1 つです。これは、ターゲットホストに ICMP（Internet Control Message Protocol）の「エコーリクエスト」パケットを送信し、ICMP の「エコーリプライ」を待機することで機能します。リクエストパケットが送信され、応答が受信された場合に、ping は成功したと見なされます。

典型的な`ping`コマンドの動作を見てみましょう。

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

この例では、`ping`を使用して`www.google.com`への接続性を確認しています。`-c 3`オプションは、`ping`に正確に 3 つのエコーリクエストパケットを送信し、その後停止するように指示します。デフォルトでは、`ping`は 1 秒に 1 パケットを送信します。

### Ping 出力の理解

`ping icmp_seq`コマンドの出力は、貴重な診断情報を提供します。主要な構成要素を分解してみましょう。

### ICMP シーケンス (icmp_seq)

`icmp_seq`フィールドは、各 ICMP パケットのシーケンス番号を表示します。私たちの例では 3 つのパケットを送信し、出力はすべて（`icmp_seq=1`、`icmp_seq=2`、`icmp_seq=3`）正常に返されたことを示しています。`ping seq`はパケットロスを診断するために非常に重要です。シーケンス番号の欠落に気づいた場合、それは一部のパケットが宛先に到達していないか、返ってきていない接続の問題を示しています。`icmp seq`番号が順不同で表示される場合、パケットが往復完了するのにデフォルトの 1 秒間隔よりも時間がかかっていることを示唆しており、ネットワークの輻輳や遅延が原因である可能性があります。`icmp_seq meaning`を理解することがトラブルシューティングの鍵となります。

### タイム・トゥ・リブ (TTL)

Time To Live (TTL) フィールドは、パケットのホップカウンターとして機能します。パケットがルーター（「ホップ」）を通過するたびに、TTL 値は 1 ずつ減少します。パケットが宛先に到達する前にカウンターがゼロに達すると、パケットは破棄されます。このメカニズムにより、パケットがネットワーク上で無限に循環するのを防ぎます。

### 時間 (Time)

`time`フィールドは往復時間、つまりパケットがあなたのマシンからターゲットホストへ移動し、エコーリプライが戻ってくるまでにかかった時間を測定します。この値は通常ミリ秒（ms）で測定され、ネットワーク遅延の主要な指標となります。

## Exercise

ネットワーク診断を習得するには実践が不可欠です。これらのハンズオンラボは、`ping`コマンドの理解を深めるのに役立ちます。

1.  **[Linux における ping と arp を使用したネットワーク層の相互作用の探求](https://labex.io/ja/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping`と`arp`を使用してネットワーク層とデータリンク層の相互作用を探り、デフォルトゲートウェイがリモートトラフィックをどのように処理するかを観察します。
2.  **[Linux における IP アドレスタイプと到達可能性の探求](https://labex.io/ja/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping`と`ip a`を利用してローカル TCP/IP スタックをテストし、パブリックインターネット接続を確認し、ネットワーク到達可能性を探ります。
3.  **[Linux におけるネットワーク層接続のシミュレーション](https://labex.io/ja/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - `ip addr`で静的 IP アドレスを割り当て、同じサブネット内および異なるサブネット内での`ping`による接続性をテストする方法を学びます。

これらのラボは、ネットワーク到達可能性と`ping`コマンドの概念を実世界のシナリオに応用するのに役立ち、Linux でのネットワーク診断に対する自信を構築します。

## Quiz Question

往復時間の測定単位は何ですか？大文字と小文字を区別して、英語で回答してください。

## Quiz Answer

ms
