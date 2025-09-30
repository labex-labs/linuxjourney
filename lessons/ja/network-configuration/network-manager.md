---
index: 4
lang: "ja"
title: "Network Manager"
meta_title: "Network Manager - ネットワーク設定"
meta_description: "Linux の NetworkManager について、ネットワーク設定を自動化する方法、nm-tool および nmcli コマンドの使用方法を学びます。この初心者向けガイドで始めましょう！"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux ネットワーキング，ネットワーク設定，Linux チュートリアル，初心者向けガイド"
---

## Lesson Content

もちろん、システムのネットワークを自動的に稼働させたい場合、そのための機能がすでに用意されています。ほとんどのディストリビューションは、NetworkManager デーモンを利用してネットワークを自動的に設定します。

GUI を使用している場合、デスクトップのタスクバーのどこかにアプレットの形で NetworkManager があることに気づくでしょう。ご覧のとおり、ネットワークのハードウェアと接続情報を管理します。たとえば、起動時に NetworkManager はネットワークハードウェア情報を収集し、接続（ワイヤレス、有線など）を検索し、それらをアクティブにします。

NetworkManager と対話するためのコマンドラインツールもあります。

### nm-tool

`nm-tool`は NetworkManager の状態とそのデバイスを報告します。

```plaintext
pete@icebox:/$ nm-tool
NetworkManager Tool

State: connected (global)

- Device: eth0  [Wired connection 1] -------------------------------------------
  Type:              Wired
  Driver:            pcnet32
  State:             connected
  Default:           yes
  HW Address:        12:3D:45:56:7D:CC

  Capabilities:
    Carrier Detect:  yes

  Wired Properties
    Carrier:         on

  IPv4 Settings:
    Address:         192.168.22.1
    Prefix:          24 (255.255.255.0)
    Gateway:         192.168.22.2

    DNS:             192.168.22.2
```

### nmcli

`nmcli`コマンドを使用すると、NetworkManager を制御および変更できます。詳細については、man ページを参照してください。

## Exercise

練習は完璧をもたらします！NetworkManager はネットワーク設定の多くを自動化しますが、トラブルシューティングや高度な管理のためには、それが管理する基盤となるコマンドと概念を理解することが重要です。Linux でのネットワーク識別と管理の理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux で MAC アドレスと IP アドレスを識別する](https://labex.io/ja/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a`コマンドを使用して、Linux システム上の MAC アドレスや IP アドレスを含むネットワークアドレス情報を識別する練習をします。
2. **[Linux で IP アドレスを管理する](https://labex.io/ja/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip`コマンドと`dhclient`を使用して、静的および動的 IP アドレスを設定し、デフォルトゲートウェイを設定し、ネットワーク設定を確認する方法を学びます。
3. **[Linux で ping と arp によるネットワーク層の相互作用を探る](https://labex.io/ja/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping`と`arp`を使用して、ネットワーク層とデータリンク層がどのように相互作用するかを理解し、ARP の動作とデフォルトゲートウェイがトラフィックを処理する方法を観察します。

これらの演習は、実際のシナリオでネットワーク識別と設定の概念を適用し、Linux ネットワーキングの基礎に自信を築くのに役立ちます。

## Quiz Question

NetworkManager の情報を表示するコマンドは何ですか？

## Quiz Answer

nm-tool
