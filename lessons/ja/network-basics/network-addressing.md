---
lesson_id: "network-addressing"
course_id: "network-basics"
lang: "ja"
order_index: 4
title: "ネットワークアドレッシング"
description: "リンクアドレス、IP アドレス、ホスト名がネットワーク通信の異なる部分を識別する仕組みを学びます。"
meta_title: "ネットワークアドレッシング - ネットワークの基礎"
meta_description: "ネットワークアドレッシングの基本を学びましょう。このガイドでは、Linux ネットワーキングにおけるデバイス間の通信を理解するための重要な概念である MAC アドレス、IP アドレス、ホスト名について解説します。"
meta_keywords: "ネットワークアドレッシング，MAC アドレス，IP アドレス，ホスト名，ネットワーク識別子，Linux ネットワーキング，ネットワーク基礎，初心者，チュートリアル，ガイド"
---

ネットワーク通信は、範囲ごとに異なる識別子を使います。リンク層アドレスはローカルリンクでフレームを配送し、IP アドレスはルーティングされた配送を支え、名前は人やアプリケーションがサービスを選ぶのに役立ちます。

## リンク層アドレス

Ethernet の MAC アドレスは48ビットで、通常 `00:c4:b5:45:b2:43` のような6つの16進オクテットで表します。送信元アドレスは現在のリンク上のインターフェースを識別し、宛先はユニキャスト、マルチキャスト、ブロードキャストになれます。

MAC アドレスは恒久的または世界で一意とは限りません。ソフトウェアがローカル管理アドレスを割り当て、仮想インターフェースがアドレスを生成し、Wi-Fi のプライバシー機能がランダム化する場合があります。ルーターは通常ホップごとに Ethernet フレームを置き換えるため、リモートサーバーは元のローカル Ethernet 送信元アドレスを受け取りません。

:::single-choice{#network-addressing-mac-scope} パケット配送における Ethernet MAC アドレスの通常の範囲はどこですか？

::option[現在のローカルリンク。]{#network-addressing-local-link .correct explanation="ルーターは後続ホップ用に新しいリンク層フレームを作ります。"}
::option[最終的なインターネットサーバーまでの全ルーターホップ。]{#network-addressing-all-hops explanation="元のフレームは変更なしでルーターを通過しません。"}
::option[アプリケーションのテキスト符号化だけ。]{#network-addressing-text-encoding explanation="MAC アドレスはリンク層フレームに属します。"}
:::

## IP アドレスとプレフィックス

IPv4 は32ビット（4オクテット）、IPv6 は128ビットです。通常 IP アドレスはインターフェースへ割り当て、`192.0.2.10/24` や `2001:db8::10/64` のようなプレフィックス長とともに解釈します。プレフィックスは、先頭から何ビットがネットワークを表すかを示します。

1つのインターフェースが複数の IP アドレスを持て、DHCP、プライバシーアドレス、フェイルオーバー、管理操作で変わる場合があります。プライベート IPv4 は別々のネットワークで再利用でき、外部到達性は公開ルーティングと NAT の方針で決まります。

:::single-choice{#network-addressing-ipv4-size} IPv4 アドレスの大きさはどれですか？

::option[4オクテットの32ビット。]{#network-addressing-thirty-two .correct explanation="表示される各10進要素が8ビットを表します。"}
::option[1つの16進数字の4ビット。]{#network-addressing-four-bits explanation="4ビットで表せるのは16進数字1桁だけです。"}
::option[16オクテットの128ビット。]{#network-addressing-128-octets explanation="IPv6 は128ビットであり、128オクテットではありません。"}
:::

## ホスト名と名前解決

ホスト名は名前であり、アドレスではありません。ホストの名前サービス設定に従い、`/etc/hosts`、DNS、マルチキャスト方式などを参照できます。1つの名前が複数のアドレスへ解決されたり、複数の名前が1つのサービスを指したりします。

アプリケーションが見る可能性の高い結果を調べるには、システムリゾルバーの経路を使います。

```bash
$ getent ahosts example.com
```

DNS 応答は変化・キャッシュされることがあり、名前解決の成功はサービス到達性を証明しません。

:::single-choice{#network-addressing-getent-purpose} 名前解決の確認で `getent ahosts` を使う理由は何ですか？

::option[返されたアドレスを全インターフェースへ永久に割り当てる。]{#network-addressing-getent-assign explanation="データベースを照会するだけで、インターフェースを設定しません。"}
::option[システムで設定された名前サービス経路へアドレスを問い合わせる。]{#network-addressing-system-resolver .correct explanation="ホストの方針に従い、ローカルファイルや DNS などを含められます。"}
::option[返された全ホスト上でアプリケーションが正常だと保証する。]{#network-addressing-getent-health explanation="名前検索とアプリケーションの正常性は別のテストです。"}
:::

## Linux ホストを調べる

リンク設定と IP 設定を分けて表示します。

```bash
$ ip -brief link
$ ip -brief address
```

到達性を診断するときは、さらに経路と近隣状態を調べます。名前だけから正しい送信元インターフェースやアドレスを推測してはいけません。経路選択、ポリシールール、名前空間、トンネルで経路が変わる場合があります。

:::single-choice{#network-addressing-ip-link-versus-address} 割り当て済み IP アドレスを中心に表示するコマンドはどれですか？

::option[`ip -brief address`]{#network-addressing-address-view .correct explanation="address オブジェクトはインターフェースの IPv4・IPv6 割り当てを表示します。"}
::option[`ip -brief link` だけ。]{#network-addressing-link-only explanation="link ビューはインターフェースとリンク層の状態を中心に表示します。"}
::option[`pwd`]{#network-addressing-pwd explanation="pwd はシェルの作業ディレクトリを表示します。"}
:::

## まとめ

ネットワーク上の範囲に応じて名前とアドレスを区別できるようになりました。

1. MAC アドレスを、変化し得るローカルリンク識別子として扱う。
2. IPv4・IPv6 アドレスをプレフィックス長とともに読む。
3. インターフェースが複数の論理アドレスを持てると理解する。
4. 設定済みのシステムリゾルバーを通じてホスト名を照会する。
