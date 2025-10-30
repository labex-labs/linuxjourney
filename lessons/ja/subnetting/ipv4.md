---
index: 1
lang: "ja"
title: "IPv4"
meta_title: "IPv4 - サブネット化"
meta_description: "IPv4 アドレスを理解して Linux ネットワーキングを学ぶ最良の方法を発見しましょう。この初心者向けガイドでは、IP の構造とコマンドラインを使用して IP を見つける方法を解説します。"
meta_keywords: "IPv4, IP アドレス，Linux 初心者，Linux 学習の最良の方法，初心者向け Linux コマンドライン，ifconfig, ip addr, ネットワーク基礎"
---

## Lesson Content

ネットワークに接続されているすべてのデバイスには、IP（インターネットプロトコル）アドレスとして知られる固有のアドレスがあります。このコースでは、最も一般的に遭遇するタイプの IPv4 アドレスに焦点を当てます。これらを理解することは、Linux でネットワーキングを学ぶための核となる部分です。

IPv4 アドレスは 32 ビットの数値であり、通常、次のような人間が読みやすい形式で表されます。

```
204.23.124.23
```

このアドレスには、デバイスが属する特定のネットワークを識別する**ネットワーク部**と、そのネットワーク上の特定のデバイスを識別する**ホスト部**という、2 つの明確な部分が含まれています。

### IP アドレスの構造

IPv4 アドレスは、ピリオドで区切られた 4 つのセクションに分割されます。各セクションは**オクテット**と呼ばれます。コンピュータサイエンスでは、オクテットは 8 ビットのグループであり、8 ビットは 1 バイトに等しいため、IPv4 アドレスは 4 バイト長です。この構造は基本的であり、これを習得することは、ネットワーキングにおける`beginner linux command line for beginners`を学ぶための最良のリソースの 1 つです。

### Linux で IP アドレスを見つける

すべての`beginner linux`ユーザーにとって、最初のタスクの 1 つはシステムの IP アドレスを見つけることです。これはコマンドラインツールを使用して実行できます。

このための従来のコマンドは`ifconfig`です。多くのシステムにはまだ存在していますが、レガシー（旧式）ツールと見なされています。

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

上記の出力では、IPv4 アドレスは`192.168.1.129`です。

### ip addr による最新のアプローチ

今日の Linux ネットワーキングを学ぶための`best way to learn linux`は、最新の`ip`コマンドを使用することです。`ip addr`コマンドは`ifconfig`に取って代わり、ほとんどの最新の Linux ディストリビューションで標準となっています。

```bash
pete@icebox:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 1d:3a:32:24:4d:ce brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.129/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 85646sec preferred_lft 85646sec
```

ここでは、`eth0`インターフェースの`inet`の横に、同じ IPv4 アドレス`192.168.1.129`が見つかります。

## Exercise

IP アドレス指定と Linux でのネットワーク識別に関する理解を深めるために、これらの実践的なラボでスキルを練習してください。

1. **[Linux で MAC アドレスと IP アドレスを識別する](https://labex.io/ja/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a`コマンドを使用して、Linux システム上の IPv4 および IPv6 アドレスを含むネットワークアドレス情報を識別する練習をします。
2. **[Linux で IP アドレスタイプと到達可能性を探索する](https://labex.io/ja/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping`や`ip a`などのコマンドを使用して、さまざまな IP アドレスタイプとネットワーク到達可能性をテストします。
3. **[Linux ターミナルで IP サブネット分割と 2 進数変換を実行する](https://labex.io/ja/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - IP アドレスとネットワークがビットレベルでどのように構成されているかをより深く理解するために不可欠な、IP サブネット分割と 2 進数変換を習得します。

これらのラボは、実際のシナリオで IP アドレス指定の概念を適用し、Linux でのネットワーク構成とトラブルシューティングに対する自信を構築するのに役立ちます。

## Quiz Question

IPv4 アドレスは何バイトで構成されていますか？

## Quiz Answer

4
