---
index: 1
lang: "ja"
title: "ネットワークインターフェース"
meta_title: "ネットワークインターフェース - ネットワーク設定"
meta_description: "Linux ネットワークインターフェース、ifconfig、および ip コマンドについて学びます。ネットワーク設定の構成と管理方法を理解します。Linux ネットワーキングの旅を始めましょう！"
meta_keywords: "Linux ネットワークインターフェース，ifconfig, ip コマンド，ネットワーク設定，Linux ネットワーキング，初心者，チュートリアル，ガイド"
---

## Lesson Content

ネットワークインターフェースは、カーネルがネットワークのソフトウェア側とハードウェア側をリンクする方法です。これについては、すでに例を見てきました。

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### ifconfig コマンド

**ifconfig**ツールを使用すると、ネットワークインターフェースを設定できます。ネットワークインターフェースが設定されていない場合、カーネルのデバイスドライバとネットワークは互いに通信する方法を知りません。Ifconfig は起動時に実行され、設定ファイルを通じてインターフェースを設定しますが、手動で変更することもできます。ifconfig の出力は、左側にインターフェース名、右側に詳細情報を示します。最も一般的に見られるインターフェースは、eth0（マシン内の最初のイーサネットカード）、wlan0（ワイヤレスインターフェース）、および lo（ループバックインターフェース）です。ループバックインターフェースは、コンピュータ自体を表すために使用されます。これは、デバッグやローカルで実行されているサーバーへの接続に役立ちます。

インターフェースのステータスは up または down です。ご想像のとおり、インターフェースを「オフ」にしたい場合は、down に設定できます。ifconfig の出力で最もよく見るフィールドは、HWaddr（インターフェースの MAC アドレス）、inet address（IPv4 アドレス）、および inet6（IPv6 アドレス）です。もちろん、サブネットマスクとブロードキャストアドレスも表示されます。インターフェース情報は/etc/network/interfaces でも確認できます。

### インターフェースを作成して起動する

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

これにより、eth0 インターフェースに IP アドレスとネットマスクが割り当てられ、起動されます。

### インターフェースを起動または停止する

```bash
ifup eth0
ifdown eth0
```

### ip コマンド

**ip**コマンドを使用すると、システムのネットワークスタックを操作することもできます。使用しているディストリビューションによっては、ネットワーク設定を操作するための推奨される方法である場合があります。

使用例をいくつか示します。

### すべてのインターフェースの情報を表示する

```bash
ip link show
```

### インターフェースの統計情報を表示する

```bash
ip -s link show eth0
```

### インターフェースに割り当てられた IP アドレスを表示する

```bash
ip address show
```

### インターフェースを起動および停止する

```bash
ip link set eth0 up
ip link set eth0 down
```

### インターフェースに IP アドレスを追加する

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

練習は完璧をもたらします！ネットワークインターフェースと IP アドレスの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux で MAC アドレスと IP アドレスを特定する](https://labex.io/ja/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a`コマンドを使用して、Linux システム上の MAC、IPv4、IPv6 アドレスを含むネットワークアドレス情報を特定する練習をします。
2. **[Linux で IP アドレスを管理する](https://labex.io/ja/labs/comptia-manage-ip-addressing-in-linux-592736)** - 静的および動的 IP アドレスを設定し、デフォルトゲートウェイを設定し、`ip`コマンドを使用してネットワーク設定を確認する方法を学びます。
3. **[Linux で IP アドレスの種類と到達可能性を探索する](https://labex.io/ja/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - さまざまな IP アドレスの種類（プライベート、パブリック、マルチキャスト）を探索し、`ping`と`ip a`を使用してネットワークの到達可能性をテストします。

これらのラボは、ネットワークインターフェースの識別と IP アドレスの概念を実際のシナリオに適用し、Linux ネットワークに対する自信を築くのに役立ちます。

## Quiz Question

ネットワークインターフェースを設定するコマンドは何ですか？

## Quiz Answer

ifconfig
