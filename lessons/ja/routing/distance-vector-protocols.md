---
lesson_id: "distance-vector-protocols"
course_id: "routing"
lang: "ja"
order_index: 5
title: "距離ベクトルプロトコル"
description: "距離ベクトルプロトコルが近隣の広告からルートを導き、ループを抑える仕組みを学びます。"
meta_title: "距離ベクトルプロトコル - ルーティング"
meta_description: "ネットワークルーティングにおける距離ベクトルプロトコルの初心者向けガイド。このチュートリアルでは、RIP などのプロトコルがホップカウントを使用して経路を決定する方法を説明し、最新の Linux ネットワーキングにおけるそれらの制限について解説します。"
meta_keywords: "距離ベクトルプロトコル，ネットワークルーティング，RIP, ルーティング情報プロトコル，ホップカウント，Linux ネットワーキング，初心者ガイド，チュートリアル"
---

距離ベクトルルーティングは、到達可能な宛先と、その距離を表すメトリックを近隣へ伝えます。ルーターは、近隣の広告とその近隣までのコストを組み合わせ、自身の候補経路を導きます。

## 近隣を通じて学習する

ルーター A があるプレフィックスまでの距離を 3 と広告し、ルーター B から A までのコストが 1 なら、B は A 経由の距離を 4 と導けます。この情報は方向とメトリックを表すもので、完全なトポロジーマップではありません。そのため、この方法は routing by rumor と呼ばれることがあります。

:::single-choice{#distance-vector-derived-distance}
近隣がメトリック 3 を広告し、リンクコストが 1 の場合、その近隣経由で導かれるメトリックはいくつですか？

::option[2]{#distance-vector-two explanation="リンクコストは引くのではなく、加えます。"}
::option[31]{#distance-vector-thirty-one explanation="値はメトリックであり、10 進数字として連結しません。"}
::option[4]{#distance-vector-four .correct explanation="近隣までの距離とローカルリンクコストを組み合わせて候補経路を求めます。"}
:::

## ループと Count to Infinity

障害後、近隣同士が誤って相手から戻ってくるルートを広告し合い、メトリックが徐々に増えることがあります。プロトコルは有限の infinity 値、split horizon、route poisoning、poison reverse、triggered update、タイマーによってこれを緩和します。これらは問題を減らしますが、すべてのトポロジー変更を瞬時に収束させるものではありません。

:::single-choice{#distance-vector-split-horizon}
split horizon は何を減らすための仕組みですか？

::option[すべての IPv4 アドレスのビット数。]{#distance-vector-ip-bits explanation="IPv4 アドレスの大きさは、ルーティング更新とは独立して固定されています。"}
::option[アプリケーションペイロードの暗号化オーバーヘッド。]{#distance-vector-encryption explanation="この手法が扱うのはルート広告の方向です。"}
::option[学習したルートを、受け取った近隣へ送り返す広告。]{#distance-vector-no-return .correct explanation="その方向への広告を抑止すると、単純なフィードバックループを防ぎやすくなります。"}
:::

## RIP のメトリックと制限

RIP は hop count を使います。メトリック 16 のルートは到達不能なので、利用可能な最大メトリックは 15 です。これによってループ時の増加に上限ができますが、ネットワーク直径も制限されます。ホップが少なくても、遅延が小さい、または帯域幅が大きいとは限りません。

RIPv2 は定期更新と triggered update を使い、CIDR 情報に対応します。あらゆる状況でテーブル全体をブロードキャストするのではなく、通常は更新をマルチキャストします。認証とフィルタリングは、引き続き意図して設定する必要があります。

:::single-choice{#distance-vector-rip-infinity}
RIP のメトリック 16 は何を表しますか？

::option[16 本の並列リンクを持つ最速経路。]{#distance-vector-fastest-16 explanation="RIP はこの値を到達不能として扱います。"}
::option[infinity、つまり宛先へ到達不能。]{#distance-vector-unreachable .correct explanation="RIP で利用できる経路の上限は 15 ホップです。"}
::option[BGP から学習したルート。]{#distance-vector-bgp-route explanation="この数値は RIP 固有の意味を持ちます。"}
:::

## 学習したルートを評価する

近隣状態、受信・広告プレフィックス、メトリック、次ホップ、ルート導入、データプレーンの到達性を確認します。RIP 内では有効なルートでも、ローカルの優先ポリシーによって別のルート情報源に負ける場合があります。

:::single-choice{#distance-vector-fewest-hop-limit}
RIP が選んだ最少ホップ経路でも、性能が悪い場合があるのはなぜですか？

::option[hop count はリンクの帯域幅、遅延、損失、混雑を表さないから。]{#distance-vector-hop-limited .correct explanation="ホップ数が多い経路でも、リンクやアプリケーション性能が良い場合があります。"}
::option[RIP は常に最もホップ数の多いルートを選ぶから。]{#distance-vector-most-hops explanation="RIP のメトリックは、利用可能な小さい hop count を優先します。"}
::option[hop count をディスク容量のバイト数で測るから。]{#distance-vector-disk-bytes explanation="数えるのはストレージではなく、ルーティングされた転送回数です。"}
:::

## まとめ

これで、距離ベクトルルーティングの単純さと制限の両方を説明できます。

1. 近隣の広告から候補距離を導く。
2. ループと count-to-infinity の動作を認識する。
3. RIP の利用可能な 15 ホップ上限とメトリック 16 を説明する。
4. ルート導入とデータプレーンの結果を別々に検証する。
