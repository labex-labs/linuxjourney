---
index: 9
lang: "ja"
title: "DHCP の概要"
meta_title: "DHCP の概要 - ネットワークの基本"
meta_description: "Linux における DHCP (Dynamic Host Configuration Protocol) について学びます。DHCP がどのように IP アドレスを割り当てるか、そしてその 4 段階のプロセスを理解します。Linux ネットワーキングの旅を始めましょう！"
meta_keywords: "DHCP, Dynamic Host Configuration Protocol, Linux ネットワーキング，IP アドレス，DHCP チュートリアル，初心者，ガイド"
---

## Lesson Content

まだ説明していない重要なネットワーク概念に DHCP (Dynamic Host Configuration Protocol) があります。

DHCP は、IP アドレス、サブネットマスク、およびゲートウェイをマシンに割り当てます。例えば、携帯電話を持っていて、他の人と話すために携帯電話番号を取得したいとします。電話会社に電話をかけると、番号が与えられます。料金を支払い続ける限り、電話を使い続けることができます。この場合、DHCP は電話会社のようなもので、他の IP アドレスと通信できるように IP アドレスを提供します。IP アドレスもリースされます。これらは一定期間有効で、リース設定に応じて更新されます。

DHCP は多くの理由で優れています。ネットワーク管理者が IP アドレスの割り当てについて心配する必要がなくなり、重複する IP アドレスを設定するのを防ぐこともできます。すべての物理ネットワークには独自の DHCP サーバーが必要であり、ホストが IP アドレスを要求できるようにします。一般的な家庭環境では、ルーターが DHCP サーバーとして機能します。

DHCP がすべての動的なホスト情報を取得する方法は次のとおりです。

1. DHCP DISCOVER - このメッセージは、DHCP サーバーを検索するためにブロードキャストされます。
2. DHCP OFFER - ネットワーク内の DHCP サーバーがオファーメッセージで応答します。このオファーには、DHCP リース時間、サブネットマスク、IP アドレスなどを含むパケットが含まれています。
3. DHCP REQUEST - クライアントは、どのオファーを受け入れたかをすべての DHCP サーバーに知らせるために、別のブロードキャストを送信します。
4. DHCP ACK - サーバーから確認応答が送信されます。

DHCP はこれよりも複雑ですが、これがその要点です。

## Exercise

このレッスンには演習はありません。

## Quiz Question

DHCP リクエストのステップは何ですか？

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
