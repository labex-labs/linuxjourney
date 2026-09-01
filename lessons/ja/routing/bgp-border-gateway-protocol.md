---
lesson_id: "bgp-border-gateway-protocol"
course_id: "routing"
lang: "ja"
order_index: 7
title: "ボーダーゲートウェイプロトコル"
description: "BGP が自律システム間およびシステム内で、ポリシー制御された IP 到達可能性を交換する仕組みを学びます。"
meta_title: "ボーダーゲートウェイプロトコル - ルーティング"
meta_description: "インターネットルーティングの核となるプロトコル、ボーダーゲートウェイプロトコル（BGP）の基礎を探ります。BGP が自律システム間の通信をどのように促進するか、およびボーダーゲートウェイプロトコルルーティングの原則について学びます。"
meta_keywords: "BGP, ボーダーゲートウェイプロトコル，ボーダーゲートウェイプロトコルルーティング，インターネットルーティング，自律システム，Linux ネットワーキング，BGP チュートリアル，ネットワークプロトコル"
---

Border Gateway Protocol（BGP）は、インターネットの path-vector ルーティングプロトコルです。IP プレフィックスの到達可能性と経路属性を交換し、ネットワークが物理的な距離だけでルートを選ぶのではなく、管理ポリシーを適用できるようにします。

## 自律システムとセッション

自律システムは、共通のルーティング管理下にあるネットワークの集合で、BGP では autonomous system number によって識別されます。external BGP は自律システム間でルートを交換し、internal BGP は一つの AS 内で BGP の到達可能性を配布します。

BGP peer は TCP ポート 179 上でセッションを確立します。TCP セッションが機能することはトランスポートの土台にすぎず、BGP の capability、ポリシー、ルート交換も成功する必要があります。

:::single-choice{#bgp-external-session} external BGP は何を交換しますか？

::option[一つのスイッチ内の Ethernet フレームチェックサム。]{#bgp-ethernet-fcs explanation="BGP は TCP より上で動作し、ネットワーク層の到達可能性を交換します。"}
::option[Web ブラウザー間のユーザーパスワード。]{#bgp-browser-passwords explanation="アプリケーションの認証情報はルーティング属性ではありません。"}
::option[自律システム間の到達可能性と経路情報。]{#bgp-between-as .correct explanation="eBGP は別々のルーティング管理主体を接続し、ドメイン間ポリシーを適用します。"}
:::

## Path-Vector 情報

広告にはプレフィックスと属性が含まれます。`AS_PATH` は通過した自律システムを列挙し、ループ検出に役立ちます。ほかの一般的な属性には、`LOCAL_PREF`、`MED`、origin、next hop、community があります。その効果は方向、実装、ポリシーによって異なります。

:::single-choice{#bgp-as-path-loop} `AS_PATH` は AS 間ループの防止にどう役立ちますか？

::option[AS は、自身の番号をすでに含む経路を拒否できる。]{#bgp-own-as-reject .correct explanation="path vector が、広告されたプレフィックスまでに使った AS の並びを公開します。"}
::option[それらのシステムを通る全パケットを暗号化する。]{#bgp-aspath-encryption explanation="この属性はルーティング経路を記述するもので、ペイロードを暗号化しません。"}
::option[すべての AS に MAC アドレスを割り当てる。]{#bgp-aspath-mac explanation="自律システム番号とリンクアドレスは別の名前空間です。"}
:::

## ポリシーに基づく選択

BGP の「best」path は、設定された判断処理を勝ち抜いた経路です。運用者は顧客ルートを優先し、local preference を変更し、プレフィックスをフィルタリングし、community とトラフィックエンジニアリングポリシーを使えます。短い `AS_PATH` がある段階で影響しても、より優先度の高い属性を常に上回るわけではありません。

BGP が候補を選んだ後も、通常の IP 転送では最長プレフィックス一致を適用します。選択済みの `/24` は、その宛先に対して、選択済みの包含する `/16` より優先されます。

:::single-choice{#bgp-best-path-meaning} BGP の best path は何を表しますか？

::option[ローカルの属性とポリシーの判断処理を勝ち抜いたルート。]{#bgp-policy-winner .correct explanation="ドメイン間の経路選択では、管理上の意図が中心になります。"}
::option[あらゆる場合に物理ケーブル距離が最短のルート。]{#bgp-shortest-cable explanation="BGP は物理距離の完全な地図を持ちません。"}
::option[現在のアプリケーション遅延が最小であるという保証。]{#bgp-lowest-latency explanation="BGP の選択は、既定ではエンドユーザーの遅延を継続的に最適化しません。"}
:::

## 広告と到達可能性

プレフィックスの広告は、ポリシーの下で到達可能だと表明しますが、基盤となるルートを作るわけでも、復路を保証するわけでもありません。プレフィックスを originate する前に、有効な転送、集約動作、フィルター、failover、所有権の承認を確認してください。

:::single-choice{#bgp-advertisement-limit} プレフィックスを広告しても保証できないものはどれですか？

::option[peer がコントロールプレーンのルートを受信できること。]{#bgp-peers-control explanation="広告と受け入れが成功すれば、その限定的なコントロールプレーンの事実は確認できます。"}
::option[プレフィックスにアドレスビットが含まれること。]{#bgp-prefix-bits explanation="IP プレフィックスはアドレスビットと長さで定義されます。"}
::option[プレフィックス全体のパケットを配送できること。]{#bgp-data-plane-not-guaranteed .correct explanation="基盤ルート、次ホップ、フィルタリング、サービスの健全性は別途検証する必要があります。"}
:::

## ルーティングセキュリティと変更管理

route leak と hijack は、一つのルーターをはるかに超える通信へ影響し得ます。運用者は厳格な import/export フィルター、maximum-prefix 上限、peer ポリシー、監視を使い、適切な場合は Resource Public Key Infrastructure（RPKI）の origin validation を行います。RPKI origin validation は、ある AS がプレフィックスを originate する権限を持つか確認しますが、完全な AS path は検証しません。

BGP の変更には、段階的な展開、ルート差分の確認、帯域外アクセス、ロールバック、コントロールプレーンとデータプレーン双方の検証が必要です。

:::single-choice{#bgp-rpki-limit} RPKI origin validation は何を確認しますか？

::option[すべてのパケットペイロードにマルウェアがないこと。]{#bgp-payload-malware explanation="RPKI はアプリケーション内容を検査しません。"}
::option[完全な AS path の遅延が最小であること。]{#bgp-path-latency explanation="origin validation は性能選択でも、完全な経路検証でもありません。"}
::option[origin AS が権限を持つこと。]{#bgp-origin-authorized .correct explanation="検証するのは origin の承認であり、AS path 内の全 transit 関係ではありません。"}
:::

## まとめ

これで、BGP をポリシー制御された path-vector ルーティングとして説明できます。

1. external BGP と internal BGP のセッションを区別する。
2. `AS_PATH` を経路情報とループ情報として使う。
3. ローカル属性とポリシーから best path を解釈する。
4. 広告した各プレフィックスの背後にある転送を検証する。
5. フィルタリング、origin validation、監視、ロールバックを適用する。
