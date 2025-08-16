---
lang: "ja"
title: "ネットワーク層"
description: "Linux の Network layer、IP アドレスがサブネット間でパケットをルーティングする方法、およびデータ伝送におけるその役割について学びます。Linux ネットワーキングの旅を始めましょう！"
keywords: "Network layer, IP addresses, subnets, Linux networking, packet routing, beginner, tutorial, guide"
---

## Lesson Content

Network layer は、送信元ホストから宛先ホストへのパケットのルーティングを決定します。幸いなことに、この例では、パケットは同じネットワーク内を移動するだけですが、インターネットは多くのネットワークで構成されています。インターネットを構成するこれらの小さなネットワークは、subnets として知られています。すべての subnets は何らかの形で相互に接続されているため、<https://www.google.com>が独自のネットワーク上にあるにもかかわらず、アクセスすることができます。subnets に特化したコース全体があるため、詳細には触れませんが、Network layer に関しては、IP addresses が異なる subnets への移動ルールを定義していることを知っておいてください。

Network layer では、Transport layer から来る segment を受け取り、この segment を IP packet にカプセル化し、送信元ホストの IP address と宛先ホストの IP address を packet header に付加します。この時点で、パケットにはどこへ行くのか、どこから来たのかという情報が含まれています。次に、パケットを物理ハードウェア層に送信します。

## Exercise

No exercises for this lesson.

## Quiz Question

インターネットを構成するより小さなネットワークは何と呼ばれますか？

## Quiz Answer

subnets
