---
index: 5
lang: "ja"
title: "arp"
meta_title: "arp - ネットワーク設定"
meta_description: "Linux の ARP コマンドと ARP キャッシュの表示方法について学びます。ネットワーク通信における ARP の役割を理解しましょう。ARP の初心者向けガイドです。"
meta_keywords: "Linux ARP, ARP キャッシュ，ip neighbour show, ネットワークコマンド，Linux ネットワーキング，初心者向け Linux, Linux チュートリアル"
---

## Lesson Content

ARP で MAC アドレスを検索する際、システムにローカルに保存されている ARP キャッシュを最初に確認することを思い出してください。このキャッシュは実際に表示できます。

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

ARP キャッシュは、マシンが起動した時点では実際には空です。パケットが他のホストに送信されるにつれて、情報が格納されていきます。ARP キャッシュにない宛先にパケットを送信すると、次のことが起こります。

1. 送信元ホストは、ARP リクエストパケットを含む Ethernet フレームを作成します。
2. 送信元ホストは、このフレームをネットワーク全体にブロードキャストします。
3. ネットワーク上のいずれかのホストが正しい MAC アドレスを知っている場合、その MAC アドレスを含む応答パケットとフレームを送信します。
4. 送信元ホストは、IP から MAC アドレスへのマッピングを ARP キャッシュに追加し、その後パケットの送信を続行します。

`ip`コマンドを使用して ARP キャッシュを表示することもできます。

```bash
ip neighbour show
```

## Exercise

マシンを再起動し、ネットワーク上で何かを行ったときに、ARP キャッシュに何が起こるかを観察してください。

## Quiz Question

ARP キャッシュを表示するために使用できるコマンドは何ですか？

## Quiz Answer

arp
