---
lesson_id: "ping"
course_id: "troubleshooting"
lang: "ja"
order_index: 2
title: "ping"
description: "回数を制限した ping テストを実行し、応答、損失、RTT、TTL、限界を解釈する方法を学びます。"
meta_title: "ping - トラブルシューティング"
meta_description: "Linux の ping コマンドを使用してネットワーク接続性をテストする方法を学びます。このガイドでは、icmp_seq、TTL、往復時間を含む ping の出力を解説します。ping シーケンスを解釈してネットワークの問題を診断する方法を理解しましょう。"
meta_keywords: "Linux ping, ネットワーク接続性，ICMP, TTL, ping コマンド，icmp_seq, ping seq, icmp seq, icmp_seq 意味，ping icmp_seq, Linux ネットワーキング"
---

`ping` は ICMP Echo Request を送信し、観測した応答を報告します。これは、あるアドレスまでの一つの制御メッセージ経路を試すものであり、TCP、UDP、DNS、認証、アプリケーションの動作を証明するものではありません。

## 回数を制限したテスト

一般的な iputils 実装で、各パケットの待ち時間を 2 秒とし、IPv4 の要求を 3 回送ります。

```bash
$ ping -4 -c 3 -W 2 example.com
```

IPv6 を選ぶには `-6` を使います。ホスト名は複数のアドレスを返し、実行ごとに異なるものが選ばれる場合があるため、解決されたアドレスを記録してください。

:::single-choice{#ping-count-option}
`-c 3` は何を指定しますか？

::option[パケットのペイロードを正確に 3 メガバイトにする。]{#ping-three-megabytes explanation="パケットサイズには別のオプションを使います。"}
::option[宛先への永続ルートを三つ作る。]{#ping-three-routes explanation="ping は通信を試すだけで、ルートを追加しません。"}
::option[Echo Request を 3 回送り、通常終了する。]{#ping-three-requests .correct explanation="有限の回数を指定すると、範囲が明確で再現可能な診断になります。"}
:::

## シーケンスと損失

`icmp_seq` は、その実行中の要求を識別します。応答が欠けると観測上の損失になり、順序が入れ替わった応答は遅延のばらつきを示す場合があります。小さな標本は変動が大きいため、回数を制限した複数の区間と、アプリケーション自身のエラー率を比較します。

損失は往路でも復路でも起こり得ます。また ICMP のレート制限により、ping の損失率がアプリケーションの損失率と異なる場合があります。

:::single-choice{#ping-sequence-gap}
`icmp_seq` の応答が一つ欠けている場合、何が考えられますか？

::option[宛先が MAC アドレスを恒久的に変更した。]{#ping-sequence-mac explanation="シーケンスの欠落だけでは、リンク層についてそのような結論は出せません。"}
::option[要求または応答の損失、フィルタリング、待ち時間を超える遅延、レート制限。]{#ping-sequence-possibilities .correct explanation="欠落から分かるのは応答を観測できなかったことだけで、方向や正確な原因までは特定できません。"}
::option[送信元ディスクの空き inode がない。]{#ping-sequence-inodes explanation="ファイルシステムの inode 状態は ICMP シーケンス応答と無関係です。"}
:::

## 往復時間

`time` フィールドは、要求の送信から応答の受信までの往復時間をミリ秒で示します。往路の遅延、相手側での処理、復路の遅延が含まれます。両端で時刻を同期して測定しない限り、片道の遅延は分かりません。

:::single-choice{#ping-rtt-meaning}
表示された `time=23.7 ms` は何を測っていますか？

::option[往路だけの片道遅延。]{#ping-outbound-only explanation="ping が測るのは、要求と応答を合わせた全区間です。"}
::option[対象システムの稼働時間。]{#ping-target-uptime explanation="この値は試行の所要時間であり、起動後の経過時間ではありません。"}
::option[その Echo の往復時間。]{#ping-round-trip .correct explanation="往路と復路、および相手側での処理が含まれます。"}
:::

## TTL または Hop Limit

表示される IPv4 の TTL または IPv6 の Hop Limit は、受信した応答に残っていた値です。送信側の初期値と復路が分からなければ、引き算で正確なホップ数を求めることはできません。値の変化は、応答元、初期値、復路の違いを反映している可能性があります。

:::single-choice{#ping-received-ttl}
IPv4 の Echo Reply に表示される TTL は何ですか？

::option[応答がローカルホストへ届いた時点の残り値。]{#ping-remaining-ttl .correct explanation="復路上の各ルーターが、送信側の初期値を一つずつ減らしています。"}
::option[往復両方向にあるルーターの正確な数。]{#ping-exact-hop-count explanation="このフィールドだけでは、初期 TTL も方向別の経路も確定しません。"}
::option[DNS レコードのキャッシュ有効期間。]{#ping-dns-ttl explanation="DNS の TTL と IP パケットの TTL は別のフィールドです。"}
:::

## 適切な層をテストする

ping が成功してもサービスが失敗する場合は、実際のポート、TLS、プロトコル、要求をテストしてください。ping が失敗した場合も、ホスト停止と断定する前に、名前解決、`ip route get`、近隣状態、ファイアウォールポリシー、キャプチャを調べます。

:::single-choice{#ping-success-limit}
ping が成功しても証明できないものはどれですか？

::option[一部の ICMP 要求・応答の経路が機能したこと。]{#ping-icmp-worked explanation="これは、応答から直接得られる証拠です。"}
::option[応答にシーケンス番号が含まれていたこと。]{#ping-sequence-present explanation="通常の出力には、応答のシーケンスが直接表示されます。"}
::option[目的のアプリケーションが要求を受け入れ、最後まで処理すること。]{#ping-app-not-proven .correct explanation="アプリケーションとトランスポートの動作は、そのアプリケーションに適した方法で別途テストする必要があります。"}
:::

## まとめ

これで、ping を明確な制限付き ICMP 測定として利用できます。

1. アドレスファミリーを選び、解決されたアドレスを記録する。
2. 再現可能なテストのため、回数と待ち時間を制限する。
3. 損失の方向や原因を決めつけずに解釈する。
4. RTT を往復値、TTL を残り値として扱う。
5. 実際のアプリケーションを別にテストする。
