---
index: 4
lang: "ja"
title: "ネットワークマネージャー"
meta_title: "ネットワークマネージャー - ネットワーク設定"
meta_description: "最新の Linux ネットワーク管理における NetworkManager デーモンの役割を発見してください。このツールがネットワーク構成を自動化する方法と、nm-tool および強力な nmcli コマンドラインユーティリティを使用して対話する方法を学びます。"
meta_keywords: "NetworkManager, nm-tool, nmcli, ネットワークマネージャー linux, networkmanager linux, linux ネットワークマネージャー, linux ネットワーク管理，ネットワーク構成，Linux ネットワーキング"
---

## Lesson Content

システムのネットワーキングが自動的に設定されるためには、通常、すでにサービスが導入されています。ほとんどの最新の Linux ディストリビューションでは、この目的のために NetworkManager デーモンが利用されており、これが**Linux ネットワーク管理**の要となっています。

### Linux におけるネットワークマネージャーとは？

グラフィカルユーザーインターフェース（GUI）を使用している場合、デスクトップのタスクバーに**Network Manager Linux**サービスのアプレットとして表示されていることに気づくでしょう。このツールは、ネットワークハードウェアと接続情報を管理します。例えば、起動時に NetworkManager はネットワークハードウェアに関する情報を収集し、利用可能な接続（ワイヤレスや有線ネットワークなど）を検索して、オンラインにするためにそれらをアクティブ化します。

### コマンドラインでの操作

GUI アプレットは便利ですが、**networkmanager linux**サービスと対話するための強力なコマンドラインツールも存在します。これらはサーバー管理やスクリプト作成に不可欠です。

### nm-tool の使用

`nm-tool` コマンドは、NetworkManager の現在の状態と管理対象デバイスのリストを報告します。多くの最新システムでは、`nmcli` のために `nm-tool` は非推奨と見なされていることに注意してください。

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

### 最新の nmcli ツール

`nmcli` コマンドは、**Linux Network Manager**を制御および変更するための主要なコマンドラインユーティリティです。これにより、ターミナルから直接ステータスの表示、接続の管理、ネットワークデバイスの設定が可能になります。その機能の完全なリストについては、マニュアルページ（`man nmcli`）を参照してください。

## Exercise

練習あるのみです！NetworkManager はネットワーク設定の多くを自動化しますが、それが管理する基盤となるコマンドと概念を理解することは、トラブルシューティングと高度な管理にとって極めて重要です。ネットワークの識別と管理に関する理解を深めるための実践的なラボを以下に示します。

1. **[Linux で MAC アドレスと IP アドレスを識別する](https://labex.io/ja/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` コマンドを使用して、Linux システム上の MAC アドレスと IP アドレスを含むネットワークアドレッシング情報を識別する練習をします。
2. **[Linux で IP アドレッシングを管理する](https://labex.io/ja/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip` コマンドと `dhclient` を使用して、静的および動的 IP アドレスの設定、デフォルトゲートウェイの設定、ネットワーク構成の検証を学習します。
3. **[Linux で ping と arp を使用したネットワーク層の相互作用を探る](https://labex.io/ja/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` と `arp` を使用して、ネットワーク層とデータリンク層がどのように相互作用するかを理解し、ARP の動作とデフォルトゲートウェイがトラフィックを処理する方法を観察します。

これらのラボは、ネットワーク識別と構成の概念を実際のシナリオに応用し、Linux ネットワーキングの基礎に対する自信を築くのに役立ちます。

## Quiz Question

レッスンに示されているように、NetworkManager の状態とデバイスの概要を表示するためのコマンドは何ですか？回答には、英語のコマンド名を小文字のみを使用してください。

## Quiz Answer

nm-tool
