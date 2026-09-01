---
lesson_id: "routing-table"
course_id: "routing"
lang: "ja"
order_index: 2
title: "ルーティングテーブル"
description: "Linux のルートを読み、宛先に対して選択されるルートを調べる方法を学びます。"
meta_title: "ルーティングテーブル - ルーティング"
meta_description: "Linux ルーティングテーブルを理解するためのガイド。route コマンドの出力（宛先、ゲートウェイ、genmask、eth0 インターフェースなど）の解釈方法を学びます。Linux のルートテーブルの基本を習得しましょう。"
meta_keywords: "linux ルーティングテーブル，linux ルートテーブル，genmask, eth0, route コマンド，ネットワークルーティング，IP ルーティング，宛先，ゲートウェイ，サブネットマスク，linux ネットワーキング"
---

Linux のルーティング状態は、IP 宛先に対してどの次ホップ、インターフェース、送信元を利用できるか決めます。従来の `route -n` 表示を見かけることもありますが、`ip route` のほうが現代のカーネルのルーティング概念を直接表します。

## IPv4 ルートを読む

出力例は次のようになります。

```text
$ ip -4 route show
default via 192.168.224.2 dev eth0 proto dhcp src 192.168.224.10 metric 100
192.168.224.0/24 dev eth0 proto kernel scope link src 192.168.224.10 metric 100
```

接続済みの `/24` ルートは、一致する宛先を `eth0` から直接送ります。デフォルトルートは次ホップゲートウェイ `192.168.224.2` を使います。`proto` はルートが導入された方法、`src` は一致する通信で推奨される送信元を示し、metric は条件が同等のルートの順位付けに役立ちます。

:::single-choice{#routing-table-via-meaning} `via 192.168.224.2` は何を示しますか？

::option[そのルートを使える唯一のアプリケーション。]{#routing-table-application explanation="アプリケーションの認可は `via` キーワードで符号化されません。"}
::option[そのルートの次ホップゲートウェイ。]{#routing-table-next-hop .correct explanation="IP 宛先は維持したまま、その同一リンク上のルーター宛てにフレームを作ります。"}
::option[そのルートのファイルシステムマウントポイント。]{#routing-table-mount explanation="ルーティングエントリが扱うのはネットワーク転送であり、ファイルシステムではありません。"}
:::

## 接続済みルートとデフォルトルート

`scope link` で `via` の次ホップを持たないルートは、プレフィックスをそのインターフェースから直接到達可能として扱います。デフォルトルートはすべてのアドレスに一致しますが、利用可能なより具体的なルートがあれば選ばれません。

:::single-choice{#routing-table-connected-route} 接続済みの `scope link` 宛先には、通常どのように到達しますか？

::option[接続済みルートが一致してもデフォルトゲートウェイを通る。]{#routing-table-connected-default explanation="接続済みプレフィックスのほうが具体的で、ゲートウェイのオペランドを持ちません。"}
::option[宛先を DNS サーバーへ変換する。]{#routing-table-connected-dns explanation="すでに選ばれた IP ルートに名前サービスは関与しません。"}
::option[近隣解決後、指定インターフェースから直接到達する。]{#routing-table-direct .correct explanation="ホストは宛先のオンリンクアドレスを解決し、ローカルにフレームを作ります。"}
:::

## プレフィックス長とメトリック

ルート選択はポリシールールを考慮し、利用可能な最長のプレフィックスを選びます。メトリックは適切に比較可能なルート群の中で順位を付けます。数値が低いデフォルトルートでも、一致する `/24` より優先されるわけではありません。

:::single-choice{#routing-table-prefix-before-default} `192.168.224.50` に、通常より具体的に一致するルートはどれですか？

::option[`192.168.224.0/24 dev eth0`]{#routing-table-twenty-four .correct explanation="一覧内では、24 ビットの一致プレフィックスが最長です。"}
::option[`default via 192.168.224.2`]{#routing-table-default-less-specific explanation="デフォルトのプレフィックス長は 0 です。"}
::option[`192.168.0.0/16 via 192.168.224.3`]{#routing-table-sixteen explanation="このルートもアドレスを含みますが、`/24` より固定するビット数が少なくなります。"}
:::

## ポリシールールと複数テーブル

Linux は、送信元、mark、インターフェースなどのセレクターに基づく `ip rule` ポリシーに従い、複数のルーティングテーブルを参照できます。そのため main テーブルだけを見ても、実際の経路を把握できない場合があります。

```bash
$ ip rule show
$ ip route show table all
```

ネットワーク名前空間と VRF も別々の状態を持てます。影響を受けているプロセスと同じコンテキストで調べてください。

:::single-choice{#routing-table-policy-limit} `ip route show` だけではアプリケーションの経路を説明できない場合があるのはなぜですか？

::option[ポリシールールや別のネットワーク名前空間が異なるルーティング状態を選ぶ場合があるから。]{#routing-table-policy-context .correct explanation="有効な検索結果は、パケット属性とプロセスのネットワークコンテキストに依存します。"}
::option[Linux のルーティングテーブルに宛先プレフィックスがないから。]{#routing-table-no-prefixes explanation="宛先プレフィックスは基本的なルートキーです。"}
::option[アプリケーションが IP パケットを一切送らないから。]{#routing-table-apps-never explanation="アプリケーション通信はネットワークプロトコルとトランスポートプロトコルで運ばれます。"}
:::

## 有効なルートを問い合わせる

宛先と、必要に応じて送信元を指定し、カーネルに評価させます。

```bash
$ ip route get 203.0.113.10
$ ip route get 203.0.113.10 from 192.168.224.10
```

結果は、その時点のローカル検索を予測します。プローブを送信するわけではなく、近隣、下流、ファイアウォール、アプリケーションへの到達性は証明しません。

:::single-choice{#routing-table-route-get-limit} `ip route get` が行わないことはどれですか？

::option[選択されたローカルインターフェースと次ホップを表示する。]{#routing-table-get-does-interface explanation="これらは検索結果の主要フィールドです。"}
::option[宛先に対する現在のローカルルートポリシーを評価する。]{#routing-table-get-does-policy explanation="このコマンドはカーネルのルート検索を実行します。"}
::option[すべての下流ホップを通じた配送成功を証明する。]{#routing-table-get-not-probe .correct explanation="これはエンドツーエンドのネットワークプローブではなく、ローカル判断の問い合わせです。"}
:::

## まとめ

これで、Linux のルーティングエントリを読み、有効なローカル判断を問い合わせられます。

1. 接続済みルートとゲートウェイ経由のルートを区別する。
2. プレフィックス、インターフェース、プロトコル、送信元、メトリックを読む。
3. 関連するメトリックの比較前に最長プレフィックス一致を適用する。
4. ポリシーテーブル、名前空間、VRF を考慮する。
5. `ip route get` を到達性テストではなく、検索として扱う。
