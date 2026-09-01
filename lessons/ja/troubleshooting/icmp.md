---
lesson_id: "icmp"
course_id: "troubleshooting"
lang: "ja"
order_index: 1
title: "ICMP"
description: "ICMP が IP のエラーを通知し、診断を支援し、IPv4 と IPv6 の重要な動作を実現する仕組みを学びます。"
meta_title: "ICMP - トラブルシューティング"
meta_description: "この Linux チュートリアルでは、ICMP プロトコルを解説し、Linux ネットワーキングを学ぶのに役立ちます。効果的なネットワークトラブルシューティングのために、ICMP メッセージタイプとコードを理解しましょう。"
meta_keywords: "ICMP, ICMP プロトコル，ネットワークトラブルシューティング，ICMP タイプ，Linux ネットワーキング，Linux 学習，Linux チュートリアル，labex linux, 初心者，ガイド"
---

Internet Control Message Protocol（ICMP）は、IP とともに制御、エラー、診断の情報を運びます。IPv4 用の ICMP と ICMPv6 は関連していますが、メッセージタイプの番号や責務が異なる別々のプロトコルです。

## タイプ、コード、チェックサム

ICMP メッセージにはタイプ、必要に応じてさらに詳しいコード、そしてチェックサムがあります。エラーメッセージには通常、送信側がエラーを通信フローと対応付けられるよう、原因となったパケットの一部が含まれます。

:::single-choice{#icmp-code-purpose} ICMP のコードは何を示しますか？

::option[報告元ルーターの永続的な DNS 名。]{#icmp-code-dns explanation="このフィールドは名前解決を目的として符号化されるものではありません。"}
::option[ICMP メッセージタイプの中で、より具体的な意味。]{#icmp-code-specific .correct explanation="たとえば Destination Unreachable のコードは、複数の失敗理由を区別します。"}
::option[過去に送られた全パケットの完全なペイロード。]{#icmp-code-all-payload explanation="エラーに引用されるのは、プロトコル規則に従って原因パケットを識別するのに十分な部分だけです。"}
:::

## Echo とエラーメッセージ

ICMPv4 では Echo Request がタイプ 8、Echo Reply がタイプ 0 です。Destination Unreachable はタイプ 3、Time Exceeded はタイプ 11 です。ICMPv6 では異なるタイプ番号を使うため、キャプチャを解釈する前に必ずアドレスファミリーを特定してください。

:::single-choice{#icmpv4-echo-request-type} ICMPv4 の Echo Request のタイプ番号はどれですか？

::option[0]{#icmp-type-zero explanation="タイプ 0 は ICMPv4 の Echo Reply です。"}
::option[11]{#icmp-type-eleven explanation="タイプ 11 は ICMPv4 の Time Exceeded です。"}
::option[8]{#icmp-type-eight .correct explanation="ping は一般に、この ICMPv4 メッセージを送って Echo 応答を要求します。"}
:::

## Path MTU と不可欠な ICMP

ICMP は、単なる任意の ping トラフィックではありません。IPv4 の fragmentation needed エラーと ICMPv6 の Packet Too Big メッセージは、Path MTU Discovery を支えます。ICMPv6 は Neighbor Discovery と Router Advertisement も運びます。そのため、ICMP をすべて遮断するとブラックホールが生じ、IPv6 の動作が壊れる場合があります。

一律に遮断するのではなく、必要なタイプ、方向、レート、スコープに基づいてフィルタリングしてください。一部の ICMP は攻撃者が偽装できるため、引用されたパケットの文脈を検証し、ローカルルートやキャプチャとも照合します。

:::single-choice{#icmp-block-all-risk} ICMP をすべて遮断すると、正当な通信が壊れる可能性があるのはなぜですか？

::option[すべての HTTP 応答が ICMP Echo Reply 内で運ばれるから。]{#icmp-http-echo explanation="HTTP は通常、ICMP Echo ではなく TCP または QUIC を使います。"}
::option[ICMP に全アプリケーションのパスワードが保存されるから。]{#icmp-passwords explanation="ICMP は認証情報データベースではありません。"}
::option[ICMP が Path MTU と IPv6 に必要な制御情報を運ぶから。]{#icmp-essential-control .correct explanation="これらのメッセージを抑止すると、適切なパケットサイズの決定や、近隣・ルーターの検出ができなくなる場合があります。"}
:::

## 応答がない場合の解釈

ICMP 応答がない原因には、フィルタリング、レート制限、非対称ルーティング、戻り経路の欠落、ホスト停止、そのメッセージに単に応答しない機器などがあります。反対に、ICMP エラーは最終宛先ではなく、中継機器が生成することもあります。

:::single-choice{#icmp-silence-meaning} Echo Reply がないという事実だけから、何が証明できますか？

::option[対象アプリケーションが確実に停止している。]{#icmp-silence-app-down explanation="Echo トラフィックが遮断または無視されていても、サービスは動作している場合があります。"}
::option[宛先ホスト名が DNS から削除されている。]{#icmp-silence-dns-deleted explanation="数値アドレスへの試行は、DNS とは無関係に無応答になることがあります。"}
::option[観測した Echo のやり取りで応答が得られなかったことだけ。]{#icmp-silence-limited .correct explanation="原因の特定には、経路、トランスポート、アプリケーション、キャプチャの追加証拠が必要です。"}
:::

## まとめ

これで、ICMP を二択の接続判定ではなく、制御に関する証拠として解釈できます。

1. 正しい IP ファミリーのタイプとコードを読む。
2. Echo、Unreachable、Time Exceeded の役割を識別する。
3. Path MTU と IPv6 の動作に必要な ICMP を維持する。
4. エラーや無応答を、ほかの経路情報と照合する。
