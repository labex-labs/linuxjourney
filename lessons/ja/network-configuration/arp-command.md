---
index: 5
lang: "ja"
title: "arp"
meta_title: "arp - ネットワーク設定"
meta_description: "Linux の ARP コマンドと ARP キャッシュの表示方法について学びます。ネットワーク通信における ARP の役割を理解します。ARP の初心者向けガイド。"
meta_keywords: "Linux ARP, ARP キャッシュ，ip neighbour show, ネットワークコマンド，Linux ネットワーキング，初心者向け Linux, Linux チュートリアル"
---

## Lesson Content

ARP で MAC アドレスを検索するとき、システムにローカルに保存されている ARP キャッシュを最初に確認することを思い出してください。このキャッシュは実際に表示できます。

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

ARP キャッシュは、マシンが起動したときは実際には空です。パケットが他のホストに送信されるにつれて、データが格納されていきます。ARP キャッシュにない宛先にパケットを送信すると、次のことが起こります。

1. 送信元ホストは、ARP リクエストパケットを含むイーサネットフレームを作成します。
2. 送信元ホストは、このフレームをネットワーク全体にブロードキャストします。
3. ネットワーク上のホストのいずれかが正しい MAC アドレスを知っている場合、MAC アドレスを含む応答パケットとフレームを送信します。
4. 送信元ホストは、IP から MAC アドレスへのマッピングを ARP キャッシュに追加し、パケットの送信を続行します。

`ip` コマンドを使用して ARP キャッシュを表示することもできます。

```bash
ip neighbour show
```

## Exercise

練習は完璧をもたらします！ARP とネットワーク層の相互作用の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux で ping と arp を使ってネットワーク層の相互作用を探る](https://labex.io/ja/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` と `arp` コマンドを使用して、IP アドレスが MAC アドレスにどのように解決されるか、およびデフォルトゲートウェイがトラフィックをどのように処理するかを観察します。
2. **[Linux で MAC アドレスと IP アドレスを特定する](https://labex.io/ja/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` コマンドを使用して、ARP を理解する上で不可欠な MAC アドレスや IP アドレスを含むネットワークアドレス情報を特定する方法を学びます。
3. **[Linux で IP アドレスを管理する](https://labex.io/ja/labs/linux-manage-ip-addressing-in-linux-592736)** - `ip` コマンドを使用して IP アドレスの管理を練習し、`arp` と `traceroute` でネットワーク設定を確認します。

これらのラボは、ARP とネットワークアドレスの概念を実際のシナリオに適用し、Linux ネットワーキングに自信をつけるのに役立ちます。

## Quiz Question

ARP キャッシュを表示するために使用できるコマンドは何ですか？

## Quiz Answer

arp
