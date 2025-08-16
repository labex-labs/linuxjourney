---
lang: "ja"
title: "ネットワークインターフェース"
description: "Linux のネットワークインターフェース、ifconfig、および ip コマンドについて学びます。ネットワーク設定の構成と管理方法を理解します。Linux ネットワーキングの旅を始めましょう！"
keywords: "Linux ネットワークインターフェース，ifconfig, ip コマンド，ネットワーク設定，Linux ネットワーキング，初心者，チュートリアル，ガイド"
---

## Lesson Content

ネットワークインターフェースは、カーネルがネットワーキングのソフトウェア側とハードウェア側をリンクする方法です。これについては、すでに例を見てきました。

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### The ifconfig command

**ifconfig** ツールを使用すると、ネットワークインターフェースを設定できます。ネットワークインターフェースが設定されていない場合、カーネルのデバイスドライバとネットワークは互いに通信する方法を知りません。ifconfig は起動時に実行され、設定ファイルを通じてインターフェースを設定しますが、手動で変更することもできます。ifconfig の出力は、左側にインターフェース名、右側に詳細情報が表示されます。最も一般的に見られるインターフェース名は、eth0 (マシン内の最初のイーサネットカード)、wlan0 (ワイヤレスインターフェース)、および lo (ループバックインターフェース) です。ループバックインターフェースは、コンピュータ自身を表すために使用され、自分自身にループバックします。これは、デバッグやローカルで実行されているサーバーへの接続に役立ちます。

インターフェースの状態は up または down になります。ご想像のとおり、インターフェースを「オフ」にしたい場合は、down に設定できます。ifconfig の出力で最もよく見るフィールドは、HWaddr (インターフェースの MAC アドレス)、inet address (IPv4 アドレス)、および inet6 (IPv6 アドレス) です。もちろん、サブネットマスクとブロードキャストアドレスも表示されます。インターフェース情報は /etc/network/interfaces でも確認できます。

### To create an interface and bring it up

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

これは、eth0 インターフェースに IP アドレスと netmask を割り当て、それを up にします。

### To bring up or down an interface

```bash
ifup eth0
ifdown eth0
```

### The ip command

**ip** コマンドも、システムのネットワーキングスタックを操作できます。使用しているディストリビューションによっては、ネットワーク設定を操作するための推奨される方法である場合があります。

以下に、その使用例をいくつか示します。

### To show interface information for all interfaces

```bash
ip link show
```

### To show the statistics of an interface

```bash
ip -s link show eth0
```

### To show IP addresses allocated to interfaces

```bash
ip address show
```

### To bring interfaces up and down

```bash
ip link set eth0 up
ip link set eth0 down
```

### To add an IP address to an interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

ネットワークインターフェースの状態を up または down に変更してみて、何が起こるか観察してください。

ifconfig コマンドと ip コマンドの両方でネットワークインターフェースを変更できますか？

## Quiz Question

ネットワークインターフェースを設定するコマンドは何ですか？

## Quiz Answer

ifconfig
