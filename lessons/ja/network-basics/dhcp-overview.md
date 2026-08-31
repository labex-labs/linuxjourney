---
lesson_id: "dhcp-overview"
course_id: "network-basics"
lang: "ja"
order_index: 9
title: "DHCP の概要"
description: "DHCPv4 が探索、選択、更新を通じ、アドレスとネットワークオプションをリースする仕組みを学びます。"
meta_title: "DHCP の概要 - ネットワークの基礎"
meta_description: "DHCP（Dynamic Host Configuration Protocol）の基本を学びましょう。このガイドでは、DHCP が IP アドレスを割り当てる方法、4 段階のプロセス（DORA）、およびネットワークの DHCP レイヤーにおける役割について解説します。Linux ネットワーキング初心者の方に最適です。"
meta_keywords: "DHCP, 動的ホスト構成プロトコル，DHCP レイヤー, IP アドレス，Linux ネットワーキング，DHCP プロセス，DORA, ネットワーク設定"
---

Dynamic Host Configuration Protocol は、クライアントへ期限付きのネットワーク設定を提供します。DHCPv4 では、ローカル方針に応じて IPv4 アドレス、サブネットマスク、既定ルーター、DNS サーバー、リース時間などを含められます。

## クライアント、サーバー、リレー

DHCP サーバーはスコープまたはアドレスプールとリース状態を管理します。すべての物理セグメントにサーバーが必要なわけではなく、DHCP リレーがサブネットと中央サーバー間の交換を転送できます。静的設定だけを使うネットワークでは DHCP を提供しない場合もあります。

DHCP は UDP 上で運ばれるアプリケーション層プロトコルです。DHCPv4 サーバーは通常 UDP 67、クライアントは UDP 68 を使います。

:::single-choice{#dhcp-relay-purpose}
DHCP リレーによって何が可能になりますか？

::option[すべてのクライアントが方針なしで任意のアドレスを選ぶ。]{#dhcp-client-any-address explanation="サーバーは引き続きスコープとリース方針を適用します。"}
::option[別サブネットのクライアントが中央の DHCP サーバーへ到達する。]{#dhcp-central-server .correct explanation="リレーがルーティング境界を越えて DHCP 交換を転送し、クライアントネットワークを示します。"}
::option[Ethernet スイッチが全 IP ルーターを置き換える。]{#dhcp-switch-router explanation="DHCP のリレーはルーティングされたネットワーク境界をなくしません。"}
:::

## 最初の DHCPv4 交換

一般的な最初の処理は DORA と呼ばれます。

1. `DHCPDISCOVER`：クライアントが利用可能なサーバーを探す。
2. `DHCPOFFER`：サーバーがアドレスとオプションを提示する。
3. `DHCPREQUEST`：クライアントが提示されたリースを選び要求する。
4. `DHCPACK`：選ばれたサーバーがリースとオプションを確定する。

ブロードキャストとユニキャストの詳細は、クライアント状態、リレー利用、サーバー機能で異なります。OFFER はまだ最終的に利用可能なリースではなく、ACK で通常の選択交換が完了します。

:::single-choice{#dhcp-dora-order}
最初の DHCPv4 の通常の順序はどれですか？

::option[OFFER、DISCOVER、ACK、REQUEST。]{#dhcp-wrong-order-one explanation="クライアントが探索してからサーバーが提示し、要求してから確認応答します。"}
::option[DISCOVER、OFFER、REQUEST、ACK。]{#dhcp-correct-order .correct explanation="探索、提示、選択、確定という順序です。"}
::option[REQUEST、ACK、DISCOVER、OFFER。]{#dhcp-wrong-order-two explanation="新しいクライアントは通常、リース選択前に探索と提示が必要です。"}
:::

## リース更新

リースは更新しなければ期限切れになります。クライアントは通常、有効期限前に更新を始め、最初は元のサーバーへ直接連絡します。成功しなければ、後に再バインドの試行範囲を広げます。正確なタイマーはプロトコルに従って提供または算出されます。

動的割り当てと表示されたアドレスが永久に続くとは限りません。変更を調査するときは、現在のリース、有効期間、サーバー、オプションを記録してください。

:::single-choice{#dhcp-lease-expiration}
正常に更新されなかった DHCP アドレスリースはどうなりますか？

::option[恒久的なハードウェア MAC アドレスになる。]{#dhcp-lease-mac explanation="IP リースはリンク層の識別情報を変えません。"}
::option[最終的に期限切れになり、クライアントは有効として扱うのをやめる。]{#dhcp-lease-expires .correct explanation="リース方式により、サーバー方針の下でアドレスとオプションを回収・変更できます。"}
::option[クライアントを権威 DNS ルートへ変換する。]{#dhcp-lease-dns-root explanation="DHCP リースは DNS 権限を付与しません。"}
:::

## 結果を調べる

DHCP 設定後はアドレスだけでなく、必要な状態をすべて検証します。

```bash
$ ip address show
$ ip route show
$ resolvectl status
```

リゾルバーのコマンドはシステムによって異なります。稼働中のネットワークマネージャーが持つリースデータとログも確認します。不正サーバー、プール内の静的割り当て、古い状態、手動設定による重複は依然起こり得ます。DHCP は間違いを減らしますが、単独で全競合を防げません。

:::single-choice{#dhcp-result-verification}
DHCP リースの受け入れ後に確認すべきものは何ですか？

::option[表示されたインターフェース名だけ。]{#dhcp-interface-name-only explanation="名前だけではアドレス、経路、名前解決を確立できません。"}
::option[キーボードが反応するかだけ。]{#dhcp-keyboard explanation="キーボード入力はネットワークリース設定と無関係です。"}
::option[アドレス、経路、DNS、リース詳細。]{#dhcp-check-complete-state .correct explanation="利用可能な設定は複数のオプションと、適用されたシステム状態に依存します。"}
:::

## DHCPv6 と IPv6 設定

IPv6 ホストは Stateless Address Autoconfiguration、DHCPv6、静的設定、または組み合わせを使えます。DHCPv6 は IPv4 の DORA 交換を使わず、既定ルーター情報は通常 DHCPv6 ではなく IPv6 Router Advertisement から得ます。

:::single-choice{#dhcp-ipv6-default-router}
IPv6 ホストは通常、既定ルーター情報をどこから得ますか？

::option[IPv6 Router Advertisement。]{#dhcp-router-advertisement .correct explanation="DHCPv6 はほかの設定を提供できますが、ルーターは Neighbor Discovery を通じて自身を通知します。"}
::option[Ethernet の FCS トレーラー。]{#dhcp-ipv6-fcs explanation="FCS はリンク破損を検出し、ルーター設定は運びません。"}
::option[IPv4 の DHCPACK だけ。]{#dhcp-ipv4-ack explanation="IPv4 DHCP メッセージは IPv6 ルーティングを設定しません。"}
:::

## まとめ

DHCPv4 がホストのネットワーク設定をリースし、更新する仕組みを説明できるようになりました。

1. DHCP サーバー、リレー、クライアントサブネットを区別する。
2. DISCOVER、OFFER、REQUEST、ACK の交換を追う。
3. アドレスとオプションを期限付きのリース状態として扱う。
4. アドレス、経路、DNS、リースメタデータをまとめて検証する。
5. DHCPv4 の動作と IPv6 自動設定を区別する。
