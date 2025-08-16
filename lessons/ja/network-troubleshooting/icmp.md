---
title: "ICMP"
description: "ICMP プロトコルの基本、メッセージタイプ、およびネットワークトラブルシューティングのためのコードについて学びます。ICMP がネットワークの問題をデバッグするためにどのように機能するかを理解します。"
keywords: "ICMP, ICMP プロトコル，ネットワークトラブルシューティング，ICMP タイプ，Linux ネットワーキング，初心者，チュートリアル，ガイド"
---

## Lesson Content

Internet Control Message Protocol (ICMP) は TCP/IP プロトコルスイートの一部です。これは更新およびエラーメッセージを送信するために使用され、パケット配信の失敗など、ネットワークの問題をデバッグするのに非常に役立つプロトコルです。

各 ICMP メッセージには、タイプ、コード、およびチェックサムフィールドが含まれています。タイプフィールドは ICMP メッセージのタイプを示し、コードはメッセージに関する詳細情報を提供するサブタイプであり、チェックサムはメッセージの整合性に関する問題を検出するために使用されます。

いくつかの一般的な ICMP タイプを見てみましょう。

- Type 0 - Echo Reply
- Type 3 - Destination Unreachable
- Type 8 - Echo Request
- Type 11 - Time Exceeded

パケットが宛先に到達できない場合、Type 3 の ICMP メッセージが生成されます。Type 3 内には、宛先に到達できない理由をさらに詳しく説明する 16 のコード値があります。

- Code 0 - Network Unreachable
- Code 1 - Host Unreachable
  etc...etc...

これらのメッセージは、いくつかのネットワークトラブルシューティングツールを使用すると、より理解できるようになります。

## Exercise

このレッスンには演習はありません。

## Quiz Question

エコー要求の ICMP タイプは何ですか？

## Quiz Answer

8
