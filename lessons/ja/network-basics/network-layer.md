---
lesson_id: "network-layer"
course_id: "network-basics"
lang: "ja"
order_index: 7
title: "ネットワーク層"
description: "IP アドレス、プレフィックス、ルーティングテーブル、ホップ制限がネットワーク間でパケットを運ぶ仕組みを学びます。"
meta_title: "ネットワーク層 - ネットワークの基礎"
meta_description: "Linux ネットワーキングにおけるネットワーク層を探ります。このガイドでは、IP アドレスとサブネットがどのようにデータ伝送のためのパケットルーティングを可能にするかを解説します。"
meta_keywords: "ネットワーク層，IP アドレス，サブネット，Linux ネットワーキング，パケットルーティング，データ伝送，OSI 参照モデル，IP パケット"
---

ネットワーク層は、相互接続されたネットワーク間で論理アドレスとベストエフォートのパケット配送を提供します。インターネットプロトコル群では IPv4 と IPv6 がパケットを運び、ルーターが各宛先への次のホップを選びます。

## IP パケット

IP ヘッダーには送信元・宛先アドレスと、転送・プロトコル処理に必要なフィールドがあります。ペイロードは一般に TCP セグメント、UDP データグラム、ICMP メッセージを含みます。IP は到着、順序、重複がないことを保証しません。

:::single-choice{#network-layer-ip-service} IP 自体が提供する配送サービスはどれですか？

::option[アプリケーショントランザクションの確定保証。]{#network-layer-guaranteed-commit explanation="IP の配送結果ではアプリケーションの永続化を証明できません。"}
::option[ベストエフォートのパケット配送。]{#network-layer-best-effort .correct explanation="必要な復旧や順序は上位層またはアプリケーションが追加します。"}
::option[1本の物理ケーブルの永久予約。]{#network-layer-cable-reservation explanation="パケット転送は専用の物理経路を予約しません。"}
:::

## プレフィックスとサブネット

アドレスとプレフィックス長は、先頭から何ビットがネットワークプレフィックスかを定義します。ホストはこの情報と経路から、宛先がリンク上にあるか、次ホップルーターが必要かを判断します。サブネットはプレフィックスと方針に基づくアドレス範囲で、すべての別サブネットへ自動接続されるわけではありません。

:::single-choice{#network-layer-prefix-decision} IPv4 宛先がリンク上にあるかをホストが判断する助けになるものはどれですか？

::option[宛先アプリケーションのパスワード。]{#network-layer-password explanation="認証データはネットワークプレフィックスを定義しません。"}
::option[Ethernet ケーブルの色。]{#network-layer-cable-color explanation="ケーブルの外観にはアドレス上の意味がありません。"}
::option[設定済みのプレフィックスとルーティングテーブル。]{#network-layer-prefix-routes .correct explanation="ホストは接続済みプレフィックスを含む経路と宛先を比較します。"}
:::

## ルーティング判断

Linux はルーティングポリシーとテーブルを参照し、送信インターフェース、次ホップ、優先する送信元情報を選びます。ほかの条件が同じなら、最も具体的に一致するプレフィックスが通常優先されます。宛先への実際の判断を調べます。

```bash
$ ip route get 203.0.113.10
```

これはローカルの経路検索であり、下流の全ルーターに有効な経路があることや、宛先が通信を受け入れることの証明ではありません。

:::single-choice{#network-layer-longest-prefix} 同じ宛先へ到達できる経路のうち、通常どれが優先されますか？

::option[インターフェース名がアルファベット順で最初の経路。]{#network-layer-alphabetical explanation="インターフェース名の綴りは選択規則ではありません。"}
::option[プレフィックスに関係なく最も古い経路。]{#network-layer-oldest explanation="経路の古さだけでプレフィックス一致を上書きしません。"}
::option[最も具体的に一致するプレフィックスを持つ経路。]{#network-layer-most-specific .correct explanation="最長プレフィックス一致は、一致する最も狭いアドレス範囲の経路を選びます。"}
:::

## ホップ制限と転送時の変化

各 IPv4 パケットには TTL、IPv6 パケットには Hop Limit があります。ルーターは値を減らし、ゼロになるとパケットを破棄して ICMP エラーを送る場合があります。これにより転送ループが無限に続くのを防ぎます。

通常ルーターは端から端までの IP アドレスを保ちますが、NAT、トンネル、プロキシなどのミドルボックスはパケットを変換・包み込むことがあります。リンク層ヘッダーはどの場合もルーターホップごとに変わります。

:::single-choice{#network-layer-hop-limit} ルーターが TTL または Hop Limit を減らすのはなぜですか？

::option[アプリケーションのファイル権限を増やすため。]{#network-layer-hop-permissions explanation="ホップ数はファイルシステムの認可とは無関係です。"}
::option[全パケットを IPv4 から IPv6 へ変換するため。]{#network-layer-hop-convert explanation="プロトコル変換はこのフィールドの目的ではありません。"}
::option[パケットが永久にループするのを防ぐため。]{#network-layer-prevent-loop .correct explanation="有限のホップ数により、継続するルーティングループでも最終的にパケットを破棄できます。"}
:::

## まとめ

IP ホストが宛先への次の段階を選ぶ仕組みを説明できるようになりました。

1. IP 配送をベストエフォートとして扱う。
2. プレフィックスと経路で、リンク上の宛先とルーティング対象を区別する。
3. 経路選択へ最長プレフィックス一致を適用する。
4. ホップ制限が転送ループを有限にする仕組みを理解する。
