---
lesson_id: "transport-layer"
course_id: "network-basics"
lang: "ja"
order_index: 6
title: "トランスポート層"
description: "TCP と UDP がポートを使い、アプリケーション端点間へ異なる配送の性質を提供する仕組みを学びます。"
meta_title: "トランスポート層 - ネットワークの基礎"
meta_description: "Linux ネットワーキングにおけるトランスポート層を探求します。このレッスンでは、TCP や UDP などの主要プロトコル、ネットワークポートの機能、データセグメンテーション、信頼性の高いデータ転送のための TCP ハンドシェイクについて解説します。"
meta_keywords: "Linux トランスポート層，TCP, UDP, TCP ハンドシェイク，ネットワークポート，データセグメンテーション，Linux ネットワーキング，ネットワークプロトコル，信頼性の高いデータ転送"
---

トランスポート層は IP ネットワークを介してアプリケーション端点を結びます。TCP と UDP はどちらも16ビットのポート番号を使いますが、アプリケーションへ提供する通信モデルと保証は異なります。

## ポートとソケット

宛先ポートは、OS が待ち受けソケットへ通信を届けるのに役立ちます。接続やフローは1つのポートだけでなく、プロトコル、送信元・宛先アドレス、送信元・宛先ポートの組み合わせで識別します。そのため同じサーバーポートで多数のクライアントを同時に扱えます。

:::single-choice{#transport-layer-many-clients}
1つの TCP サーバーポートが複数のクライアントを同時に扱えるのはなぜですか？

::option[各接続が端点アドレスとポートの異なる組み合わせを持つから。]{#transport-layer-connection-tuple .correct explanation="完全なトランスポートの組み合わせが、同じ待ち受けポートを共有する同時接続を区別します。"}
::option[サーバーが各パケットの後にポート名を永久に変更するから。]{#transport-layer-renames-port explanation="待ち受けポートは一定のまま、受け入れた接続が異なる通信相手の組み合わせを持てます。"}
::option[IP が配送前に全送信元アドレスを削除するから。]{#transport-layer-removes-source explanation="送信元アドレスは通信相手と経路の識別に関わります。"}
:::

## TCP バイトストリーム

TCP は接続が存続する間、信頼性のある順序付きバイトストリームを提供します。シーケンス番号、確認応答、再送、フロー制御、輻輳制御を使います。アプリケーションメッセージの境界は保持しません。1回の書き込みが複数回の読み取りで届いたり、複数の書き込みが1回の読み取りで返ったりするため、アプリケーション自身がフレーミングを定義します。

信頼性は絶対的な配送ではありません。タイムアウト、リセット、障害があり得て、確認応答もアプリケーションがデータを永続保存した証拠ではありません。

:::single-choice{#transport-layer-tcp-boundaries}
TCP ではアプリケーションメッセージの境界はどうなりますか？

::option[書き込み境界を保持せず、順序付きバイトストリームとして公開する。]{#transport-layer-byte-stream .correct explanation="メッセージの区切りやサイズはアプリケーションプロトコルが定義します。"}
::option[各書き込みが必ず1個の IP パケットと1回の読み取りになる。]{#transport-layer-one-write-packet explanation="分割、バッファリング、受信 API はその対応を保持しません。"}
::option[各メッセージを DNS レコードへ変換する。]{#transport-layer-tcp-dns explanation="DNS は別のアプリケーションプロトコルです。"}
:::

## TCP ハンドシェイク

通常の TCP 接続は3ウェイハンドシェイクで始まります。

1. 開始側が初期シーケンス情報を持つ `SYN` を送る。
2. 待ち受け側が自身のシーケンス情報と確認応答を持つ `SYN-ACK` を返す。
3. 開始側が `ACK` を返す。

これにより両端にトランスポート状態を確立しますが、アプリケーションサーバーの認証や、要求操作の成功までは証明しません。

:::single-choice{#transport-layer-handshake-order}
通常の TCP 3ウェイハンドシェイクの順序はどれですか？

::option[SYN、SYN-ACK、ACK。]{#transport-layer-syn-order .correct explanation="双方向の初期接続状態を同期し、確認応答します。"}
::option[ACK、ACK、SYN。]{#transport-layer-ack-ack-syn explanation="開始側が最初に同期を要求します。"}
::option[SYN、FIN、RST。]{#transport-layer-syn-fin-rst explanation="FIN と RST は通常の接続形成ではなく、状態を終了・中断します。"}
:::

## UDP データグラム

UDP はデータグラム境界を保持し、チェックサムによるエラー検出を提供しますが、TCP のような接続状態、順序、再送、フロー制御、輻輳制御は提供しません。必要な信頼性や輻輳動作はアプリケーションが追加できます。UDP が自動的に高速とは限らず、性能は設計、ワークロード、経路、実装次第です。

:::single-choice{#transport-layer-udp-boundaries}
UDP がアプリケーションへ提供する性質はどれですか？

::option[自動再送される順序付きバイトストリーム。]{#transport-layer-udp-stream explanation="これは基本 UDP ではなく TCP のようなサービスです。"}
::option[送信したデータグラム間の境界を保持すること。]{#transport-layer-udp-datagrams .correct explanation="失われない限り、受信 UDP データグラムは送信した1個のデータグラムに対応します。"}
::option[固定期限までの配送保証。]{#transport-layer-udp-deadline explanation="UDP は配送期限を保証しません。"}
:::

## トランスポート端点を調べる

状態を変えずに `ss` で待ち受け中・接続中のソケットを調べます。

```bash
$ ss -lntup
$ ss -tn state established
```

プロセス情報には権限が必要な場合があります。待ち受けソケットが証明するのはローカルのトランスポート境界での準備だけで、ファイアウォール、ルーティング、アドレスファミリー、TLS、アプリケーションの正常性は別に検査します。

:::single-choice{#transport-layer-listener-proof}
待ち受け中の TCP ソケットが確立する事実は何ですか？

::option[すべてのリモートファイアウォールが接続を許可する。]{#transport-layer-all-firewalls explanation="ローカルソケット状態から経路全体の方針は分かりません。"}
::option[アプリケーションが全ヘルスチェックに合格した。]{#transport-layer-all-health explanation="待ち受けは、アプリケーショントランザクションの成功より弱い証拠です。"}
::option[ローカルプロセスが一致する TCP 接続を受け入れる準備をしている。]{#transport-layer-local-listener .correct explanation="リモート到達性と正しいアプリケーション応答は別の問題です。"}
:::

## まとめ

TCP のストリーム動作と UDP のデータグラム動作を区別できるようになりました。

1. プロトコル、アドレス、ポートでフローを識別する。
2. TCP を、メッセージ境界を持たない信頼性のある順序付きバイトストリームとして扱う。
3. TCP ハンドシェイクが証明することと、しないことを理解する。
4. UDP の信頼性と輻輳動作をアプリケーション設計上の選択として扱う。
5. ローカルソケット状態を越えてアプリケーションの正常性を検証する。
