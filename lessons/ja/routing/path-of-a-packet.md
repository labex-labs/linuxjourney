---
lesson_id: "path-of-a-packet"
course_id: "routing"
lang: "ja"
order_index: 3
title: "パケットの経路"
description: "ルート、近隣探索、フレーム、ルーターが IP パケットを経路上で運ぶ仕組みを学びます。"
meta_title: "パケットの経路 - ルーティング"
meta_description: "ローカルネットワーク内およびインターネットを横断するデータの完全なパケット経路を探ります。Linux で IP アドレス、MAC アドレス、ARP、ルーティングテーブルがどのように連携してネットワーク通信を成功させるかを学びます。"
meta_keywords: "パケット経路，ネットワーク通信，ARP, IP アドレス，MAC アドレス，ルーティングテーブル，デフォルトゲートウェイ，Linux ネットワーキング，パケット転送"
---

パケットの経路は、各地点でのローカルな判断の連続です。送信元ホスト、各ルーター、宛先は、それぞれ独自のルーティング、近隣、フィルタリング、プロトコル状態を適用します。通常、一つのエンドポイントが内部の全判断を事前に知っているわけではありません。

## 同一リンク上の宛先へ送る

接続済みルートに含まれる宛先の場合、送信元はインターフェースと送信元 IP を選びます。次に宛先のリンクアドレスを解決し、IP パケットを運ぶフレームを送ります。Ethernet 上の IPv4 では ARP、IPv6 では Neighbor Discovery を使います。スイッチは IP ホップになることなくフレームを転送できます。

:::single-choice{#packet-path-switch-hop}
通常の Ethernet スイッチは IP ルーティングのホップとして数えますか？

::option[いいえ。IP のホップフィールドを減らさず、ローカルフレームを転送します。]{#packet-path-switch-not-hop .correct explanation="ルーティングされたホップは、ルーターが IP パケットを処理して転送するときに発生します。"}
::option[はい。すべてのスイッチが IP 宛先を書き換えます。]{#packet-path-switch-replaces-ip explanation="レイヤー 2 の転送は通常、IP 宛先を書き換えません。"}
::option[はい。すべてのケーブルコネクターも IP ホップです。]{#packet-path-cable-hop explanation="物理部品は IP ルーティングを行いません。"}
:::

## ゲートウェイ経由で送る

リンク外の宛先の場合、選択されたルートが次ホップルーターを示します。IP 宛先はリモートエンドポイントのままですが、ローカルフレームの宛先はゲートウェイのリンクアドレスになります。ホストがローカルリンク上で解決するのは、リモートサーバーではなくゲートウェイです。

:::single-choice{#packet-path-gateway-mac}
リンク外のサーバーへ送る最初の Ethernet フレームでは、誰の MAC アドレスを使いますか？

::option[すべての中継ネットワークの先にあるリモートサーバー。]{#packet-path-remote-mac explanation="リモートリンクのアドレスは、送信元 LAN 上では意味を持ちません。"}
::option[サーバーの DNS 名から計算した値。]{#packet-path-dns-mac explanation="DNS 名に、ローカル次ホップの MAC は符号化されていません。"}
::option[選択されたローカルゲートウェイ。]{#packet-path-local-gateway .correct explanation="IP ヘッダーは最終エンドポイントを宛先にしたまま、フレームは次ホップへ配送されます。"}
:::

## 各ルーターでの処理

ルーターは受信したリンクフレームを外し、IP ヘッダーを検証・処理し、TTL または Hop Limit を減らして宛先を検索し、ポリシーを適用して、送信リンク用の新しいフレームを作ります。IPv4 では TTL の変更に応じてヘッダーチェックサムも処理します。ホップフィールドが 0 になるとパケットを破棄し、ICMP time-exceeded メッセージを返すことがあります。

:::single-choice{#packet-path-router-change}
通常のルーティングされた各ホップで変更される IP フィールドはどれですか？

::option[アプリケーションのユーザー名。]{#packet-path-username explanation="基本的な転送に、ルーターはアプリケーションのアカウント情報を必要としません。"}
::option[IPv4 の TTL または IPv6 の Hop Limit。]{#packet-path-hop-field .correct explanation="各ルーターがこのフィールドを減らし、ルーティングループを有限にします。"}
::option[すべての場合のトランスポート宛先ポート。]{#packet-path-port explanation="通常のルーティングはトランスポートのエンドポイントを維持します。NAT は別の変換です。"}
:::

## ミドルボックスと MTU を考慮する

通常のルーティングは送信元と宛先の IP アドレスを維持しますが、NAT は書き換えることがあり、トンネルは元のパケットを包むことがあります。ファイアウォールは通信を無言で破棄したり、拒否応答を返したりします。リンクごとに MTU も異なります。IPv4 ルーターはパケットを断片化できる場合がありますが、IPv6 ルーターは転送パケットを断片化せず、Path MTU Discovery に依存します。

:::single-choice{#packet-path-address-change-exception}
経路の途中でエンドツーエンドの IP アドレスが変わる場合があるのはいつですか？

::option[Ethernet スイッチが送信元 MAC を学習するたび。]{#packet-path-switch-learning-ip explanation="スイッチの学習が影響するのはリンクの転送テーブルであり、IP エンドポイントアドレスではありません。"}
::option[NAT ポリシーがパケットヘッダーを変換するとき。]{#packet-path-nat-change .correct explanation="変換は、通常のルート転送を超えたミドルボックス機能です。"}
::option[DNS キャッシュエントリの期限が切れるたび。]{#packet-path-dns-expiry explanation="すでに存在するパケットには数値アドレスが入っています。"}
:::

## 復路をたどる

宛先は応答のために独自のルート検索を行います。ルーティングポリシー、負荷分散、障害によって、復路が別のルーターを通る場合があります。ステートフルファイアウォールと NAT は観測した通信フローを考慮する必要があるため、IP としては許される非対称性でも運用上問題になることがあります。

:::single-choice{#packet-path-return-symmetry}
応答は同じルーターを逆順に通る必要がありますか？

::option[はい。IP は全パケットに完全な往路を記録するからです。]{#packet-path-records-route explanation="通常の IP パケットは、必須の完全な逆経路を保持しません。"}
::option[はい。送信元と宛先が同じホスト名を持つ場合を除きます。]{#packet-path-hostname-symmetry explanation="名前は経路の対称性を強制しません。"}
::option[いいえ。各方向は独立してルーティングされます。]{#packet-path-independent-return .correct explanation="ポリシーとトポロジーにより、非対称でも有効な経路になり得ます。"}
:::

## まとめ

これで、ルーティングされた IP パケットを囲むリンク状態の変化を追跡できます。

1. 最終ホストが同一リンク上にある場合だけ、そのホストを解決する。
2. リンク外の通信は、選択されたローカルゲートウェイ宛てのフレームにする。
3. 各ルーターでルート検索とホップ上限処理を追う。
4. NAT、フィルタリング、トンネル、MTU 制約を考慮する。
5. 復路を独立したルートとして扱う。
