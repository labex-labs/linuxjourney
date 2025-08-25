---
index: 1
lang: "ja"
title: "IPv4"
meta_title: "IPv4 - サブネット化"
meta_description: "IPv4 アドレス、その構造、および ifconfig を使用して IP を見つける方法について学びます。Linux 初心者向けのネットワークの基本を理解します。"
meta_keywords: "IPv4, IP アドレス，ifconfig, ネットワークの基本，Linux ネットワーキング，初心者，チュートリアル，ガイド"
---

## Lesson Content

ネットワークホストには、それらを見つけることができる一意のアドレスがあることがわかっています。これらのアドレスは IP アドレスとして知られています。IPv4 アドレスは次のようになります。

```
204.23.124.23
```

このアドレスは実際には 2 つの部分を含んでいます。それがどのネットワーク上にあるかを示すネットワーク部分と、そのネットワーク上のどのホストであるかを示すホスト部分です。このコースでは、主に IPv4 アドレスについて説明します。これは、IP アドレスを参照するときに一般的に目にするものです。

IP アドレスはピリオドによってオクテットに区切られています。したがって、IPv4 アドレスには 4 つのオクテットがあります。コンピュータサイエンスを少し知っていれば、オクテットは 8 ビットであり、8 ビットは実際には 1 バイトに等しいので、IPv4 アドレスは 4 バイトを持つとも言います。サブネットと IP アドレスを扱う際には、ビットを頻繁に使用します。

`ifconfig -a` コマンドで IP アドレスを表示できます。

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

ご覧のとおり、私の IPv4 アドレスは 192.168.1.129 です。

## Exercise

練習は完璧をもたらします！Linux での IP アドレス指定とネットワーク識別の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux で MAC アドレスと IP アドレスを特定する](https://labex.io/ja/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` コマンドを使用して、Linux システム上の IPv4 および IPv6 アドレスを含むネットワークアドレス情報を特定する練習をします。
2. **[Linux で IP アドレスの種類と到達可能性を探索する](https://labex.io/ja/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping` や `ip a` などのコマンドを使用して、さまざまな IP アドレスの種類を探索し、ネットワークの到達可能性をテストします。
3. **[Linux ターミナルで IP サブネット化とバイナリ変換を実行する](https://labex.io/ja/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - IP アドレスとネットワークがビットレベルでどのように構成されているかをより深く理解するために不可欠な、IP サブネット化とバイナリ変換を習得します。

これらのラボは、実際のシナリオで IP アドレス指定の概念を適用し、Linux でのネットワーク構成とトラブルシューティングに自信を持つのに役立ちます。

## Quiz Question

IPv4 アドレスには何バイトありますか？

## Quiz Answer

4
