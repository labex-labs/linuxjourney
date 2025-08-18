---
lang: "ja"
title: "ネットワークマネージャー"
meta_description: "Linux の NetworkManager について、ネットワーク設定を自動化する方法、nm-tool と nmcli コマンドの使用方法を学びます。この初心者向けガイドで始めましょう！"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux ネットワーキング，ネットワーク設定，Linux チュートリアル，初心者向けガイド"
---

## Lesson Content

もちろん、システムのネットワークを自動的に起動して実行したい場合、そのための機能はすでに用意されています。ほとんどのディストリビューションは、NetworkManager デーモンを利用してネットワークを自動的に構成します。

GUI を使用している場合、NetworkManager はデスクトップのタスクバーのどこかにアプレットとして表示されます。ご覧のとおり、ネットワークのハードウェアと接続情報を管理します。たとえば、起動時に NetworkManager はネットワークハードウェア情報を収集し、接続（ワイヤレス、有線など）を検索して、それらをアクティブにします。

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

このレッスンには演習はありません。

## Quiz Question

NetworkManager の情報を表示するコマンドは何ですか？

## Quiz Answer

nm-tool
