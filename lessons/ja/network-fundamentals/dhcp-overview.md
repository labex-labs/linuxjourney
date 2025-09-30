---
index: 9
lang: "ja"
title: "DHCP の概要"
meta_title: "DHCP の概要 - ネットワークの基本"
meta_description: "Linux における DHCP（Dynamic Host Configuration Protocol）について学びましょう。DHCP が IP アドレスを割り当てる方法とその 4 段階のプロセスを理解します。Linux ネットワーキングの旅を始めましょう！"
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, Linux ネットワーキング，IP アドレス，DHCP チュートリアル，初心者，ガイド"
---

## Lesson Content

まだ説明していない重要なネットワーク概念に DHCP (Dynamic Host Configuration Protocol) があります。

DHCP は、IP アドレス、サブネットマスク、およびゲートウェイをマシンに割り当てます。たとえば、携帯電話を持っていて、人々と話し始めるために携帯電話番号を取得したいとします。電話会社に電話をかけると、番号が与えられます。料金を支払い続ける限り、電話を使い続けることができます。この場合、DHCP は電話会社であり、他の IP アドレスと話せるように IP アドレスを提供します。また、IP アドレスはリースされます。これらは一定期間有効で、リース設定に応じて更新されます。

DHCP は多くの理由で優れています。ネットワーク管理者が IP アドレスの割り当てについて心配する必要がなくなり、重複する IP アドレスを設定するのを防ぐこともできます。すべての物理ネットワークには独自の DHCP サーバーがあり、ホストが IP アドレスを要求できるようにする必要があります。通常の家庭環境では、ルーターが通常 DHCP サーバーとして機能します。

DHCP がすべての動的ホスト情報を取得する方法は次のとおりです。

1. DHCP DISCOVER - このメッセージは DHCP サーバーを検索するためにブロードキャストされます。
2. DHCP OFFER - ネットワーク内の DHCP サーバーがオファーメッセージで応答します。オファーには、DHCP リース時間、サブネットマスク、IP アドレスなどを含むパケットが含まれています。
3. DHCP REQUEST - クライアントは、どのオファーを受け入れたかをすべての DHCP サーバーに知らせるために、別のブロードキャストを送信します。
4. DHCP ACK - サーバーから確認応答が送信されます。

DHCP はこれよりも複雑ですが、これがその要点です。

## Exercise

練習は完璧をもたらします！動的 IP アドレス割り当てとネットワーク設定の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux での IP アドレス管理](https://labex.io/ja/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip` コマンドを使用してインターフェースを検査し、特に `dhclient` を使用して動的 IP アドレスを取得する練習をすることで、DHCP の知識を直接適用します。
2. **[Linux での MAC および IP アドレスの特定](https://labex.io/ja/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` コマンドを使用して、DHCP によって割り当てられた IP アドレスを含むネットワークアドレス情報を特定し、ネットワークインターフェースを検査する方法を学びます。
3. **[Linux での IP アドレスの種類と到達可能性の探索](https://labex.io/ja/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping` と `ip a` を使用して IP アドレスとネットワーク到達可能性を探索し、動的に割り当てられた IP がネットワーク内でどのように機能するかを理解するのに役立ちます。

これらのラボは、動的 IP 割り当てとネットワーク設定の概念を実際のシナリオに適用し、Linux ネットワーキングに自信をつけるのに役立ちます。

## Quiz Question

DHCP リクエストのステップは何ですか？

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
