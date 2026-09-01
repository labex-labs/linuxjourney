---
lesson_id: "tcp-ip-model"
course_id: "network-basics"
lang: "ja"
order_index: 3
title: "TCP/IPモデル"
description: "TCP/IP モデルのアプリケーション層、トランスポート層、インターネット層、リンク層が連携する仕組みを学びます。"
meta_title: "TCP/IPモデル - ネットワークの基礎"
meta_description: "現代のネットワーキングの礎である TCP/IP モデルの基本層を探ります。効果的な TCP/IP ネットワーキングのために、アプリケーション層、トランスポート層、ネットワーク層、リンク層について学びましょう。"
meta_keywords: "TCP/IPモデル, tcp ip モデルの層，tcp ip によるネットワーキング，tcp プロトコルの層，ネットワーク層，TCP, IP, Linux ネットワーキング，実世界プロトコルプロジェクト"
---

TCP/IP モデルは、インターネットホストが使うプロトコルを機能別の層へ整理します。一般的な4層形式はアプリケーション、トランスポート、インターネット、リンクです。物理媒体をリンク層から分け、5層で示す教材もあります。

## アプリケーション層

HTTP、DNS、SSH、SMTP などのサービスについて、メッセージと動作を定義します。OSI モデルが別々に扱う表現やセッションの責任も多く含みます。

:::single-choice{#tcpip-http-layer} HTTP は通常、TCP/IP のどの層に分類されますか？

::option[インターネット層。]{#tcpip-http-internet explanation="インターネット層は IP アドレスとパケット転送を扱います。"}
::option[リンク層。]{#tcpip-http-link explanation="リンク層はローカル媒体上で通信を運びます。"}
::option[アプリケーション層。]{#tcpip-http-application .correct explanation="HTTP はアプリケーションの要求と応答の意味を定義します。"}
:::

## トランスポート層

アプリケーションの端点間通信を提供します。TCP は輻輳制御とフロー制御を備えた、信頼性のある順序付きバイトストリームを提供します。UDP は TCP の接続、順序、再送保証を持たない独立したデータグラムを提供します。ポート番号はトランスポート端点の識別に役立ちますが、番号だけでは待ち受けるアプリケーションを証明できません。

:::single-choice{#tcpip-udp-property} TCP ではなく UDP の性質はどれですか？

::option[組み込みの再送保証を持たない独立したデータグラム。]{#tcpip-udp-datagrams .correct explanation="UDP を使うアプリケーションが、信頼性を追加するか、どう追加するかを決めます。"}
::option[1つのバイトストリームの順序付き配信を保証する。]{#tcpip-udp-ordered explanation="接続が成功した場合に TCP が提供する性質です。"}
::option[異なる IP ネットワーク間でパケットをルーティングする。]{#tcpip-udp-routing explanation="ネットワーク間ルーティングはインターネット層の機能です。"}
:::

## インターネット層

Internet Protocol は送信元・宛先 IP アドレスを使ってパケットを運びます。ルーターはルーティング情報を調べ、ホップ制限を減らしながら宛先へ転送します。ICMP は IP の動作に関する制御・エラー情報を伝えます。配送はベストエフォートで、必要な復旧は上位層またはアプリケーションが扱います。

:::single-choice{#tcpip-router-layer} ルーターが使う IP 宛先を提供する層はどれですか？

::option[インターネット層。]{#tcpip-router-internet .correct explanation="IP ヘッダーにルーティング転送で使うネットワーク層の宛先が含まれます。"}
::option[アプリケーション層。]{#tcpip-router-application explanation="アプリケーションメッセージは下位層のプロトコルデータ内で運ばれます。"}
::option[リンク層。]{#tcpip-router-link explanation="リンクアドレスは次のローカルホップのフレーム宛先を選びます。"}
:::

## リンク層とカプセル化

リンク層は Ethernet、Wi-Fi、ポイントツーポイントプロトコルなどを使い、1つのローカルリンク上で IP パケットを送ります。アプリケーションデータが下位へ進むと、各層は自身の範囲に必要な情報を加えます。受信側では自層のカプセル化を検証して外し、上位へ渡します。

通常、リンクヘッダーはルーターホップごとに変わり、ミドルボックスが終了または変換しない限り、トランスポートとアプリケーションの会話は端から端まで続きます。

:::single-choice{#tcpip-link-scope} リンク層フレームの通常の範囲はどこですか？

::option[1つのローカルリンクまたはホップ。]{#tcpip-one-link .correct explanation="ルーターは受信フレームを外し、次のリンク用のフレームを作ります。"}
::option[世界中のインターネット上の全アプリケーションセッション。]{#tcpip-global-frame explanation="フレームはルーティングされたネットワークを変更なしでは渡りません。"}
::option[送信元プロセスのメモリ内だけ。]{#tcpip-process-memory explanation="フレームはネットワークリンク上で送信されます。"}
:::

## まとめ

一般的なインターネット機能を TCP/IP モデルに配置できるようになりました。

1. サービスプロトコルをアプリケーション層へ対応付ける。
2. TCP ストリームと UDP データグラムを区別する。
3. IP アドレスとルーティングをインターネット層へ配置する。
4. リンクフレームをローカルホップのカプセル化として扱う。
