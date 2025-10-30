---
index: 2
lang: "ja"
title: "route"
meta_title: "route - ネットワーク設定"
meta_description: "Linux の route コマンドと ip コマンドを使用してネットワークルートを追加および削除する方法を学びます。初心者から中級者向けのルーティングテーブル管理を理解します。"
meta_keywords: "route コマンド，ip route, ルート追加，ルート削除，Linux ネットワーキング，ルーティングテーブル，Linux チュートリアル，初心者ガイド"
---

## Lesson Content

ルーティングテーブルを `route` コマンドで表示する方法については、すでに説明しました。ルートを追加または削除したい場合は、手動で行うことができます。

### 新しいルートを追加する

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### ルートを削除する

```bash
sudo route del -net 192.168.2.1/23
```

これらの変更は、**ip** コマンドでも実行できます。

### ルートを追加するには

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### ルートを削除するには

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

練習は完璧をもたらします！ネットワークルーティングと IP アドレス指定の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux での IP アドレス管理](https://labex.io/ja/labs/comptia-manage-ip-addressing-in-linux-592736)** - 静的 IP の設定、デフォルトゲートウェイの設定、`ip` コマンドを使用したネットワーク設定の確認を練習します。
2. **[Linux での ping と arp によるネットワーク層の相互作用の探索](https://labex.io/ja/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - デフォルトゲートウェイがリモートトラフィックをどのように処理するかを学び、ネットワーク層の相互作用を観察します。

これらのラボは、IP アドレス指定とルーティングの概念を実際のシナリオに適用し、Linux ネットワーキングに自信を持つために役立ちます。

## Quiz Question

ルートを削除するためのコマンドフラグは何ですか？

## Quiz Answer

del
