---
lesson_id: "link-layer"
course_id: "network-basics"
lang: "ja"
order_index: 8
title: "リンク層"
description: "Ethernet フレーム、近隣探索、スイッチ、ルーターがローカルリンク上でパケットを配送する仕組みを学びます。"
meta_title: "リンク層 - ネットワークの基礎"
meta_description: "TCP/IPのリンク層の基本を探ります。リンク層ヘッダーの構築方法、ARPによるIPアドレスからMACアドレスへの解決、ローカルネットワーク上でのパケット転送プロセスについて学びます。"
meta_keywords: "リンク層，リンク層ヘッダー, ARP, TCP/IP, MAC アドレス，ネットワーク基礎，Linux ネットワーキング，パケット転送，アドレス解決プロトコル"
---

リンク層は、1つのローカル媒体または仮想リンク上でネットワーク層パケットを運びます。Ethernet と Wi-Fi はフレームの詳細が異なりますが、どちらも IP の下でローカル配送を提供します。

## Ethernet フレーム

Ethernet フレームは、宛先・送信元 MAC アドレス、EtherType または長さフィールド、ペイロード、フレームチェックシーケンス（FCS）のトレーラーを含みます。物理伝送ではプリアンブルと開始区切りも使います。FCS はリンク上の破損を検出しますが、壊れたフレームの修復や暗号学的な保護は行いません。

:::single-choice{#link-layer-fcs-purpose} Ethernet のフレームチェックシーケンスは何に使いますか？

::option[リンク上のフレーム破損を検出する。]{#link-layer-detect-corruption .correct explanation="受信側は整合性検査に失敗したフレームを破棄できます。"}
::option[ルーティングされる全ホップでペイロードを暗号化する。]{#link-layer-fcs-encryption explanation="FCS はエラー検出符号であり、暗号化や認証ではありません。"}
::option[TCP ポートでアプリケーションを選択する。]{#link-layer-fcs-port explanation="トランスポートポートは IP ペイロード内で運ばれます。"}
:::

## スイッチとローカル配送

Ethernet スイッチは各ポートで確認した送信元 MAC アドレスを学習し、既知のユニキャストフレームを学習済みの宛先ポートへ転送します。ブロードキャストや一部の未知宛先通信はブロードキャストドメイン内へフラッディングされます。VLAN は1つのスイッチングシステムを別々の論理リンクドメインへ分けられます。

:::single-choice{#link-layer-switch-learning} Ethernet スイッチは通常、フレームから何を学習しますか？

::option[アプリケーションのパスワードと HTTP Cookie。]{#link-layer-switch-passwords explanation="基本的な転送テーブルが使うのはリンクアドレスで、アプリケーション認証情報ではありません。"}
::option[すべてのルーターが持つ完全なインターネット経路表。]{#link-layer-switch-routing-table explanation="第2層のスイッチングと世界規模の経路交換は別の機能です。"}
::option[スイッチポートに対応する送信元 MAC アドレス。]{#link-layer-switch-source .correct explanation="この学習で、後の既知ユニキャスト通信に使う転送テーブルを構築します。"}
:::

## 次ホップのアドレスを解決する

Ethernet 上の IPv4 では、Address Resolution Protocol（ARP）がリンク上の IPv4 次ホップアドレスを MAC アドレスへ対応付けます。ホストはまず近隣キャッシュを調べ、必要なら ARP 要求をブロードキャストし、所有者または許可されたプロキシが応答します。

リンク外の IP 宛先には、リモート宛先の MAC ではなく、既定または選択したゲートウェイの MAC を解決します。IPv6 は ARP ではなく ICMPv6 上の Neighbor Discovery を使います。

:::single-choice{#link-layer-remote-destination-mac} リンク外の IPv4 宛先に対して、ホストが使う MAC アドレスはどれですか？

::option[選択した次ホップルーターの MAC アドレス。]{#link-layer-gateway-mac .correct explanation="IP パケットはリモートホスト宛てのまま、ローカルフレームはルーター宛てになります。"}
::option[すべてのルーターを越えたリモートサーバーの MAC アドレス。]{#link-layer-remote-mac explanation="MAC アドレスはローカルリンク識別子で、端から端まで運ばれません。"}
::option[TCP 宛先ポートから導いた MAC アドレス。]{#link-layer-port-mac explanation="トランスポートポートはリンクアドレスを決めません。"}
:::

## 近隣状態を調べる

IPv4 ARP と IPv6 Neighbor Discovery のエントリーを表示します。

```bash
$ ip neighbor show
```

`REACHABLE`、`STALE`、`DELAY`、`PROBE`、`FAILED` などは近隣到達不能検出の状態です。`STALE` は故障を意味せず、キャッシュした到達性確認が最近のものではなく、利用時に検査できるという意味です。

:::single-choice{#link-layer-stale-neighbor} `STALE` の近隣エントリーは何を示しますか？

::option[近隣がファイアウォールで永久に遮断されている。]{#link-layer-stale-blocked explanation="この状態はファイアウォール方針を表しません。"}
::option[MAC アドレスをバックアップとしてディスクへ書き込んだ。]{#link-layer-stale-backup explanation="近隣状態は動作中のキャッシュ情報です。"}
::option[キャッシュした対応に最近の到達性確認がない。]{#link-layer-stale-confirmation .correct explanation="スタックは引き続き利用でき、必要に応じて到達性検出を行います。"}
:::

## ルーターを越えるカプセル化

送信側は IP パケットを次ホップ宛てのフレームへ入れます。ルーターは受信フレームを検証して外し、IP ヘッダーを処理し、送信経路を選び、そのリンク用の新しいフレームを作ります。受信側はカプセル化を逆順に外し、トランスポートのペイロードを適切なソケットへ渡します。

:::single-choice{#link-layer-router-reframing} ルーターで Ethernet フレームが変わる通常の転送中に、変わらないものはどれですか？

::option[NAT などのミドルボックスが変更しない限り、IP 宛先。]{#link-layer-ip-destination .correct explanation="通常のルーターはホップ内のフレームを置き換えながら、最終 IP 宛先へ向けて転送します。"}
::option[受信フレームのチェックシーケンス。]{#link-layer-same-fcs explanation="新しい送信フレームには独自のリンク整合性値が付きます。"}
::option[全リンク上の宛先 MAC アドレス。]{#link-layer-same-mac explanation="各リンクは適切な次ホップのリンクアドレスを使います。"}
:::

## まとめ

1回のローカルリンク配送で IP パケットを追跡できるようになりました。

1. 主な Ethernet フレームフィールドと整合性トレーラーを特定する。
2. スイッチがローカル転送先を学習する仕組みを説明する。
3. IPv4 の次ホップは ARP、IPv6 の近隣は NDP で解決する。
4. 近隣キャッシュの状態から過剰に障害を断定せず解釈する。
5. ルーターが送信リンクごとにフレームを再構築すると理解する。
