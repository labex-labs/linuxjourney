---
index: 1
lang: "ja"
title: "ネットワークインターフェース"
meta_title: "ネットワークインターフェース - ネットワーク設定"
meta_description: "Linux ネットワークインターフェースの包括的なガイド。ifconfig と最新の ip コマンドの使い方、および特に Debian システムにおける/etc/network/interfaces などの設定ファイルについて学びます。"
meta_keywords: "linux インターフェース，linux ネットワークインターフェース，etc network interfaces, debian ネットワークインターフェース，ifconfig, ip コマンド，ネットワーク設定，linux ネットワーキング"
---

## Lesson Content

A **Linux ネットワークインターフェース**は、カーネルのソフトウェアネットワーキングスタックと物理ネットワークハードウェア間の重要な接続点です。これにより、オペレーティングシステムはネットワーク経由でデータを送受信できます。設定済みの`linux interface`がどのようなものか、すでに例を見てきました。

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### ネットワークインターフェースの理解

ネットワーク設定を表示すると、`eth0`（最初のイーサネットカード）、`wlan0`（ワイヤレスインターフェース）、または`lo`（ループバックインターフェース）のような名前のインターフェースが表示されます。ループバックインターフェースは、自身のコンピュータを表す特別な仮想インターフェースであり、ローカルで実行されているサービスへの接続を可能にします。

インターフェースは「up」（稼働中）または「down」（停止中）の状態をとることができます。「up」状態は、アクティブでありデータ送信の準備ができていることを意味し、「down」はそれを非アクティブにします。各インターフェースに表示される重要な情報には、`HWaddr`（一意の MAC アドレス）、`inet`アドレス（IPv4 アドレス）、`inet6`アドレス（IPv6 アドレス）のほか、サブネットマスクとブロードキャストアドレスが含まれます。

### 従来の ifconfig コマンド

**ifconfig**コマンドは、`linux network interface`を設定するための古典的なツールです。システム起動時に、通常は設定ファイルに基づいてインターフェースを設定するために実行されます。多くのシステムでまだ利用可能ですが、現在ではレガシー（従来型）ツールと見なされています。

`ifconfig`を使用して、手動で IP アドレスを割り当て、インターフェースを起動できます。

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

関連する`ifup`および`ifdown`コマンドを使用して、インターフェースを簡単にアクティブ化または非アクティブ化することもできます。

```bash
ifup eth0
ifdown eth0
```

### 最新の ip コマンド

**ip**コマンドは、`ifconfig`の最新かつより強力な代替手段です。ほとんどの最新の Linux ディストリビューションでネットワークスタックを管理するための推奨される方法です。

以下に、その使用法の一般的な例をいくつか示します。

**すべてのインターフェースの情報を表示：**

```bash
ip link show
```

**特定のインターフェースの詳細な統計情報を表示：**

```bash
ip -s link show eth0
```

**インターフェースに割り当てられている IP アドレスを表示：**

```bash
ip address show
```

**インターフェースの起動または停止：**

```bash
ip link set eth0 up
ip link set eth0 down
```

**インターフェースに IP アドレスを追加：**

```bash
ip address add 192.168.1.1/24 dev eth0
```

### ネットワーク設定ファイル

`ip`や`ifconfig`のようなコマンドはインターフェースのライブ状態を設定しますが、これらの変更は永続的ではなく、再起動すると失われます。設定を永続化するには、設定ファイルを編集する必要があります。

これらのファイルの一般的な場所は`/etc/network/interfaces`です。`etc network interfaces`ファイルは、特に Ubuntu のような Debian ベースのシステムで普及しています。このファイルを介して**debian network interfaces**を管理することで、静的 IP アドレス、ゲートウェイ、および起動時に自動的に適用されるその他の設定を定義できます。`debian network/interfaces`内の構造は単純で、よく文書化されています。

## Exercise

これらのハンズオンラボで知識を実践に移しましょう。これらは、ネットワークインターフェースと IP アドレス指定の理解を深めるのに役立ちます。

1. **[Linux で MAC アドレスと IP アドレスを識別する](https://labex.io/ja/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a`コマンドを使用して、Linux システム上の MAC アドレス、IPv4 アドレス、IPv6 アドレスを含むネットワークアドレッシング情報を識別する練習をします。
2. **[Linux で IP アドレス指定を管理する](https://labex.io/ja/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip`コマンドを使用して、静的および動的 IP アドレスの設定、デフォルトゲートウェイの設定、ネットワーク構成の検証を学習します。
3. **[Linux で IP アドレスタイプと到達可能性を探索する](https://labex.io/ja/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - プライベート、パブリック、マルチキャストなどの異なる IP アドレスタイプを探索し、`ping`と`ip a`を使用してネットワーク到達性をテストします。

これらのラボは、ネットワークインターフェースの識別と IP アドレス指定の概念を実際のシナリオに適用し、Linux ネットワーキングへの自信を構築するのに役立ちます。

## Quiz Question

Linux ネットワークインターフェースを設定するために使用されるレガシーコマンドは何ですか？回答は英語で、すべて小文字を使用してください。

## Quiz Answer

ifconfig
