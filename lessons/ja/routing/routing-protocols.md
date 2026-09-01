---
lesson_id: "routing-protocols"
course_id: "routing"
lang: "ja"
order_index: 4
title: "ルーティングプロトコル"
description: "動的ルーティングプロトコルが到達可能性を交換し、利用可能な転送経路へ収束する仕組みを学びます。"
meta_title: "ルーティングプロトコル - ルーティング"
meta_description: "Linux ネットワーキングにおけるルーティングプロトコルの基礎を探ります。このガイドでは、距離ベクトル型とリンクステート型のプロトコル、ネットワークコンバージェンス、ルーターがルーティングテーブルを構築・維持する方法について解説します。初心者向けの完全なチュートリアルです。"
meta_keywords: "ルーティングプロトコル，ネットワークコンバージェンス，距離ベクトル，リンクステート，Linux ネットワーキング，ルーティングテーブル，ネットワークチュートリアル，初心者ガイド，ルーター通信"
---

静的ルートは直接設定しますが、動的ルーティングプロトコルは到達可能性とトポロジーの情報を交換し、ルーターが変化へ適応できるようにします。動的学習は手作業を減らす一方、監視すべきプロトコル状態、信頼境界、タイマー、障害モードを増やします。

## コントロールプレーンと転送プレーン

ルーティングプロトコルは、自身のデータベースへ候補を学習します。ルーターはルーティング情報ベースへ入れるルートを選び、利用可能な次ホップを転送テーブルへ導入します。その後、ハードウェアまたはカーネルがそのテーブルに基づいてパケットを転送します。

プロトコルの adjacency が確立していても、目的のプレフィックスが学習、選択、導入され、転送ポリシーで許可されたことまでは証明できません。

:::single-choice{#routing-protocols-adjacency-limit} ルーティングの adjacency が確立していても証明できないものはどれですか？

::option[目的の全ルートが導入され、正常に転送されていること。]{#routing-protocols-not-full-proof .correct explanation="ルートの広告、選択、導入、フィルタリング、データプレーン動作は別々の段階です。"}
::option[二つのプロトコル話者が何らかの制御メッセージを交換したこと。]{#routing-protocols-no-messages explanation="adjacency の確立には通常、プロトコル通信が必要です。"}
::option[コントロールプレーンが存在すること。]{#routing-protocols-no-control explanation="adjacency 自体がコントロールプレーンの状態です。"}
:::

## 内部ルーティングと外部ルーティング

Interior gateway protocol は一つの管理ルーティングドメイン内で動作します。RIP、OSPF、IS-IS などが該当します。BGP は自律システム内および自律システム間でポリシー制御された到達可能性を交換し、インターネットの exterior routing protocol として機能します。

メトリックの意味はプロトコルごとに異なります。OSPF の cost、RIP の hop count、BGP の属性集合を、一つの共通数値尺度のように比較することはできません。実装は、プロトコル固有の選択前または選択と並行して、route preference や administrative distance により情報源間を選びます。

:::single-choice{#routing-protocols-metric-comparison} RIP の hop count と OSPF の cost を直接比較できますか？

::option[はい。すべてのルーティングメトリックは同じ単位だからです。]{#routing-protocols-universal-metric explanation="各プロトコルが独自のメトリックと選択処理を定義します。"}
::option[はい。ただし両方の値が 0 の場合だけです。]{#routing-protocols-zero-metric explanation="表示値にかかわらず、意味は異なります。"}
::option[いいえ。プロトコル固有の意味を持つからです。]{#routing-protocols-specific-metric .correct explanation="異なる情報源間の選択は、異種メトリックを一つの尺度とせず、実装のポリシーを使います。"}
:::

## 距離ベクトルとリンクステート

距離ベクトルプロトコルは近隣を通じて到達可能性と距離を広告し、近隣の報告から経路を導きます。リンクステートプロトコルは adjacency を形成し、スコープ内にリンクステート情報をフラッディングし、トポロジーデータベースを構築して最短経路木を計算します。現代的なプロトコルには多くの改良があり、単純な分類だけでは説明しきれない場合があります。

:::single-choice{#routing-protocols-link-state-input} リンクステートルーターは、経路計算に何を使いますか？

::option[デフォルトゲートウェイのホスト名だけ。]{#routing-protocols-hostname-only explanation="トポロジー計算にはリンクとプレフィックスの情報が必要です。"}
::option[ルーティングスコープ内のリンクを記述する同期済みデータベース。]{#routing-protocols-link-database .correct explanation="ルーターは学習したトポロジー上で最短経路アルゴリズムを実行します。"}
::option[全ホストのアプリケーション層パスワード。]{#routing-protocols-passwords explanation="ルーティングトポロジーの交換に、エンドユーザーの認証情報は必要ありません。"}
:::

## 収束

トポロジーまたはポリシーの変更後、ルーターは変化を検出し、制御情報を伝播し、経路を計算して転送状態を更新します。収束とは、影響を受ける宛先についてネットワークが安定した相互利用可能なルーティングへ到達するまでの過程と結果です。すべてのルーターが完全に同じテーブルを持つ必要はなく、役割やポリシーによって意図的に異なる場合があります。

収束中は、一時的な損失、ループ、ブラックホールが発生することがあります。検出、伝播、計算、導入を別々に測定し、データプレーンのプローブでも検証してください。

:::single-choice{#routing-protocols-convergence} ルーティングの収束とは何ですか？

::option[変更後に安定した利用可能なルーティングへ到達する過程。]{#routing-protocols-stable-routing .correct explanation="制御情報の伝播と、その結果としての転送更新が含まれます。"}
::option[すべてのルーターが同一のグローバルテーブルを持つという要件。]{#routing-protocols-identical-table explanation="ポリシー、area、役割によって意図的な差が生まれます。"}
::option[起こり得るすべてのルーティング障害を永久に防ぐこと。]{#routing-protocols-no-failure explanation="収束済みネットワークにも、ポリシーや容量の問題は起こり得ます。"}
:::

## まとめ

これで、動的ルーティング情報をプロトコル交換から転送までの流れに位置付けられます。

1. 学習した候補、選択済みルート、転送エントリを区別する。
2. 内部ルーティングと BGP のポリシー交換を区別する。
3. メトリックは各プロトコルの意味の範囲内でのみ比較する。
4. コントロールプレーンとデータプレーンの両方で収束を検証する。
