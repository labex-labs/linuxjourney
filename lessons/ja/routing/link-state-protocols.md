---
lesson_id: "link-state-protocols"
course_id: "routing"
lang: "ja"
order_index: 6
title: "リンクステートプロトコル"
description: "リンクステートプロトコルが adjacency を形成し、トポロジー情報をフラッディングして経路を計算する仕組みを学びます。"
meta_title: "リンクステートプロトコル - ルーティング"
meta_description: "大規模ネットワーク向けの OSPF のようなリンクステートプロトコルについて学びましょう。それらの高速な収束とルーティングテーブルの更新方法を理解してください。Linux ネットワーキングの旅を始めましょう！"
meta_keywords: "リンクステートプロトコル，OSPF, Linux ネットワーキング，ルーティングプロトコル，ネットワークトポロジ，初心者"
---

リンクステートプロトコルは、ローカルのリンクとプレフィックスを記述し、その記述をルーティングスコープ全体へ配布します。各ルーターはトポロジーデータベースから経路を計算します。OSPF と IS-IS が代表例です。

## Adjacency を形成する

ルーターは互換性のある近隣を検出し、インターフェース種別、area、タイマー、認証などのパラメータに従ってプロトコルの adjacency を形成します。hello パケットが見えても、完全な adjacency は保証されません。設定の不一致によって、状態機械が途中で止まることがあります。

:::single-choice{#link-state-hello-limit}
OSPF hello を受信しても証明できないことはどれですか？

::option[ルーター間で完全に同期した adjacency が形成されたこと。]{#link-state-not-full .correct explanation="area、タイマー、認証、MTU などの状態によって、完全なデータベース交換が妨げられる場合があります。"}
::option[近隣が少なくとも一つのプロトコルメッセージを送ったこと。]{#link-state-hello-sent explanation="hello の受信は、その限定的な事実を直接証明します。"}
::option[インターフェースがフレームを受信できたこと。]{#link-state-frame-received explanation="受信したパケットから、一部のローカル受信経路が機能したと分かります。"}
:::

## リンクステート情報をフラッディングする

各ルーターは、自身に関係する状態の広告を生成します。近隣は、新しい情報を最初の近隣ペアだけに留めず、定義された area または domain 全体へ確実にフラッディングします。シーケンスと aging の仕組みにより現在の情報を区別し、古い状態を削除します。

:::single-choice{#link-state-flooding-scope}
リンクステート情報を一つの近隣より先へフラッディングするのはなぜですか？

::option[すべてのアプリケーションが全ルーターのパスワードを必要とするから。]{#link-state-password-copy explanation="アプリケーションの認証情報はトポロジー広告ではありません。"}
::option[Ethernet がユニキャストフレームを送れないから。]{#link-state-no-unicast explanation="Ethernet はユニキャストに対応します。ここでのフラッディングはルーティングプロトコルの配布機構です。"}
::option[ルーティングスコープ内のルーターに整合したトポロジーデータベースが必要だから。]{#link-state-consistent-database .correct explanation="各ルーターは、現在のリンクステート広告の共有集合から経路を計算します。"}
:::

## 最短経路を計算する

リンクステートデータベースを構築した後、ルーターは自身を根として shortest-path-first アルゴリズム、一般には Dijkstra のアルゴリズムを実行します。OSPF はインターフェースの cost を合計し、ポリシーと equal-cost の規則が導入される結果に影響します。

「最短」とはプロトコル cost が最小という意味であり、ルーター数が最少、またはアプリケーションで測った遅延が最小とは限りません。cost の設計は運用上の意図を反映すべきです。

:::single-choice{#link-state-shortest-meaning}
リンクステートの経路計算で「最短」とは何を意味しますか？

::option[プレフィックスの文字数が最も少ないルート。]{#link-state-shortest-text explanation="テキストの長さはトポロジー cost と無関係です。"}
::option[プロトコル cost の合計が最小の経路。]{#link-state-lowest-cost .correct explanation="cost モデルが hop count や現在の遅延に直接対応するとは限りません。"}
::option[常にパケット損失が 0 の経路。]{#link-state-zero-loss explanation="計算されたルートはアプリケーション性能を保証しません。"}
:::

## Area と収束

OSPF area はトポロジーのフラッディングと計算の範囲を制限し、通常の area 間設計では Area 0 がバックボーンになります。要約と area type によって、異なるルーターが意図的に異なる詳細度のデータベースを持つことがあります。

リンク変更後、検出、広告のフラッディング、SPF 計算、ルート導入、転送回復にはそれぞれ時間がかかります。単純な距離ベクトル設計より高速に収束できる場合がありますが、すべての障害や設定で自動的にそうなるわけではありません。

:::single-choice{#link-state-convergence-stages}
OSPF の収束を調査するとき、何を測定すべきですか？

::option[管理者が端末を開いた時刻だけ。]{#link-state-terminal-time explanation="それだけではプロトコルや転送の各段階を切り分けられません。"}
::option[ルーター名のアルファベット順だけ。]{#link-state-router-names explanation="名前は収束時間を決めません。"}
::option[検出、フラッディング、計算、導入、転送回復。]{#link-state-all-stages .correct explanation="段階を分けると、収束の遅延または失敗がどこで起きたか分かります。"}
:::

## まとめ

これで、近隣検出から導入済み経路まで、リンクステートルーティングの流れを追えます。

1. hello の受信と完全な adjacency を区別する。
2. ルーティングスコープ全体への確実なフラッディングを説明する。
3. 最短経路を、設定されたプロトコル cost が最小の経路として解釈する。
4. コントロールプレーンとデータプレーンの全収束段階を測定する。
