---
index: 1
lang: "ja"
title: "IPv4"
meta_title: "IPv4 - サブネット化"
meta_description: "完全な Linux チュートリアルで IPv4 アドレスの学習を始めましょう。初心者向け Linux ユーザーのためのこのガイドは、IP 構造と ip addr などの必須コマンドラインツールを網羅した、Linux ネットワーキングを学ぶ最良の方法です。"
meta_keywords: "IPv4, IP アドレス，初心者 Linux, Linux 学習の最良の方法，完全 Linux チュートリアル，無料オンライン Linux コース，無料 Linux 認定コース，Linux ネットワーキング，ifconfig, ip addr"
---

## Lesson Content

ネットワーク上のすべてのデバイスには、IP（インターネットプロトコル）アドレスという一意の識別子があります。このレッスンは、`complete linux tutorial`の重要な一部であり、最も一般的に遭遇する IPv4 アドレスに焦点を当てています。ネットワークの世界に足を踏み入れるすべての`beginner linux`ユーザーにとって、IPv4 を理解することは極めて重要な第一歩です。

### IPv4 が不可欠な理由

システム管理やネットワーク管理に真剣に取り組む人にとって、IPv4 について学ぶことは基本です。これはほとんどのネットワーク通信の基盤を形成します。このガイドは、Linux ネットワーキングをゼロから学ぶための`best way to learn linux`を提供します。これは`free linux certification courses`のいずれではありませんが、これらの基礎を習得することは、専門的な認定資格に向けた重要なステップです。

### IPv4 アドレスの構造

IPv4 アドレスは 32 ビットの数値ですが、通常、次のような人間が読みやすい形式で表示されます。

```
204.23.124.23
```

このアドレスには主に 2 つの部分があります。ネットワークを識別する**ネットワーク部**と、そのネットワーク上の特定のデバイスを識別する**ホスト部**です。アドレスはピリオドで区切られた 4 つのセクションに分割され、各セクションは**オクテット**と呼ばれます。オクテットは 8 ビットのグループであり、IPv4 アドレスが 4 バイト（32 ビット）であることを意味します。この構造を理解することは、ネットワーク設定とトラブルシューティングにとって極めて重要です。

### IP アドレスの確認方法

すべての Linux ユーザーが行うべき最初のタスクの 1 つは、システムの IP アドレスを見つけることです。これは簡単なコマンドラインツールを使用して実行できます。このための従来のコマンドは`ifconfig`です。多くのシステムにはまだ存在しますが、レガシー（旧式）ツールと見なされています。

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

上記の出力では、IPv4 アドレスは`192.168.1.129`です。

### ip addr コマンドの使用

現代的で推奨される方法は、`ip`コマンドを使用することです。`ip addr`コマンドは`ifconfig`に取って代わり、ほとんどの最新の Linux ディストリビューションで標準となっています。より詳細な情報を提供し、学習に注力すべきツールです。

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

ここでは、`eth0`インターフェースの`inet`の横に、同じ IPv4 アドレス`192.168.1.129`を見つけることができます。

## Exercise

IP アドレッシングと Linux でのネットワーク識別に関する理解を深めるために、これらの実践的なラボでスキルを磨きましょう。

1. **[Linux で MAC アドレスと IP アドレスを識別する](https://labex.io/ja/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a`コマンドを使用して、Linux システム上の IPv4 および IPv6 アドレスを含むネットワークアドレッシング情報を識別する練習をします。
2. **[Linux で IP アドレスタイプと到達可能性を探索する](https://labex.io/ja/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping`や`ip a`などのコマンドを使用して、さまざまな IP アドレスタイプを調査し、ネットワーク到達性をテストします。
3. **[Linux ターミナルで IP サブネット化と 2 進数変換を実行する](https://labex.io/ja/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - IP アドレスとネットワークがビットレベルでどのように構成されているかをより深く理解するために不可欠な、IP サブネット化と 2 進数変換を習得します。

これらのラボは、実際のシナリオで IP アドレッシングの概念を適用し、Linux でのネットワーク設定とトラブルシューティングに対する自信を構築するのに役立ちます。

## Quiz Question

IPv4 アドレスは何バイトで構成されていますか？

## Quiz Answer

4
