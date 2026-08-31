---
lesson_id: "arp-command"
course_id: "network-config"
lang: "ja"
order_index: 5
title: "arp"
description: "Linux の IPv4 ARP と IPv6 近隣キャッシュの状態を調べ、解釈する方法を学びます。"
meta_title: "arp - ネットワーク設定"
meta_description: "Linux の ARP コマンドと ARP キャッシュの表示方法について学びます。ネットワーク通信における ARP の役割を理解します。ARP の初心者向けガイド。"
meta_keywords: "Linux ARP, ARP キャッシュ，ip neighbour show, ネットワークコマンド，Linux ネットワーキング，初心者向け Linux, Linux チュートリアル"
---

Linux は、最近解決した次ホップのリンクアドレスを近隣テーブルに保存します。Ethernet 上の IPv4 では ARP によってエントリを学習し、IPv6 では Neighbor Discovery を使います。従来の `arp` コマンドが表示するのはこの状態の一部だけですが、`ip neighbor` は両方のアドレスファミリーに対応します。

## 近隣エントリを表示する

すべてのエントリ、または一つのインターフェースを調べます。

```bash
$ ip neighbor show
$ ip neighbor show dev enp1s0
```

エントリには IP アドレス、リンク層アドレス、デバイス、到達可能性の状態が含まれます。ブート直後のテーブルは空の場合があり、ローカルの次ホップを必要とする通信に応じて追加されます。

:::single-choice{#arp-command-modern-view}
現代の Linux で近隣テーブルの状態を表示するコマンドはどれですか？

::option[`pwd neighbor`]{#arp-command-pwd explanation="pwd はシェルの作業ディレクトリを表示します。"}
::option[`ip neighbor show`]{#arp-command-ip-neighbor .correct explanation="IPv4 の ARP 由来エントリと IPv6 の Neighbor Discovery エントリをどちらも表示します。"}
::option[`route --passwords`]{#arp-command-route-passwords explanation="ルート調査で認証情報を公開するようなコマンドはありません。"}
:::

## IPv4 近隣を解決する

同一リンク上の IPv4 アドレスに対応する情報がない場合、ホストは対象アドレスの所有者を尋ねる ARP Request をブロードキャストします。対象、または proxy ARP を明示的に行うルーターが応答します。送信側は対応関係をキャッシュし、待機中のフレームを送信します。

リモート IP 宛ての場合、ホストはリモートホストの MAC アドレスではなく、選択されたゲートウェイのアドレスを解決します。

:::single-choice{#arp-command-remote-target}
リンク外の宛先へ送るとき、ホストが解決する IPv4 近隣はどれですか？

::option[すべてのルーターの先にある最終リモートサーバー。]{#arp-command-final-server explanation="その MAC アドレスは送信元リンク上では意味を持ちません。"}
::option[リゾルバー設定に列挙された全 DNS サーバー。]{#arp-command-all-dns explanation="近隣解決はリゾルバー一覧ではなく、選択されたルートに従います。"}
::option[選択された同一リンク上のゲートウェイ。]{#arp-command-gateway .correct explanation="ローカルの Ethernet フレームは、IP パケットを転送するルーター宛てになります。"}
:::

## 状態を解釈する

代表的な状態には `REACHABLE`、`STALE`、`DELAY`、`PROBE`、`INCOMPLETE`、`FAILED` があります。`STALE` は最近の到達確認が期限切れになった状態で、必要に応じてプローブしながらキャッシュ済みアドレスをまだ使えます。`FAILED` は解決または到達性検出に失敗したことを示しますが、原因にはリンク、VLAN、アドレス、ルート、フィルタリング、相手の停止などが考えられます。

:::single-choice{#arp-command-stale-state}
`STALE` は、その近隣へ到達不能だと判明したことを意味しますか？

::option[いいえ。最近の確認がなく、使用時にプローブできる状態です。]{#arp-command-stale-probe .correct explanation="この状態は `FAILED` と同じではありません。"}
::option[はい。そのエントリは二度と使えません。]{#arp-command-stale-dead explanation="STALE のエントリも候補として残り、到達性確認後に別状態へ遷移できます。"}
::option[はい。DNS レコードの期限が切れたからです。]{#arp-command-stale-dns explanation="近隣状態と DNS キャッシュは別の仕組みです。"}
:::

## 近隣状態を慎重に変更する

静的エントリの設定やキャッシュ消去は状態を変える操作であり、動作中の通信を中断したり、元の証拠を消したりする可能性があります。まず現在のルート、パケットカウンター、近隣状態を記録してください。インターフェース全体を消去する前に、許可されたテストネットワークで対象を絞ったプローブとパケットキャプチャを行います。

ARP には組み込みの認証がないため、アドレス重複や偽装応答によって対応関係が汚染されることがあります。スイッチの保護機能、セグメンテーション、監視、上位層の認証が影響の軽減に役立ちます。

:::single-choice{#arp-command-flush-first}
最初の診断手順として近隣テーブル全体を消去すべきでないのはなぜですか？

::option[近隣エントリが DNS ルートサーバーにしか保存されないから。]{#arp-command-neighbors-dns explanation="近隣エントリはローカルのネットワークスタックが管理します。"}
::option[消去するとインターフェースのハードウェアが恒久的に削除されるから。]{#arp-command-flush-hardware explanation="削除されるのはキャッシュエントリであり、物理デバイスではありません。"}
::option[証拠を変え、正常に動作していた次ホップを中断する可能性があるから。]{#arp-command-flush-disrupts .correct explanation="読み取り専用の調査と対象を絞ったテストなら、原因診断に必要な状態を保持できます。"}
:::

## まとめ

これで、すべてのキャッシュ状態を障害とみなさずに近隣解決を調べられます。

1. IPv4 と IPv6 の状態確認に `ip neighbor` を使う。
2. 宛先が同一リンク上にある場合だけ、その宛先を解決する。
3. リンク外の IP 通信ではゲートウェイを解決する。
4. 対象を絞った状態変更の前に、キャッシュの証拠を保存する。
