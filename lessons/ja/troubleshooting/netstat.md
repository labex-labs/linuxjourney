---
lesson_id: "netstat"
course_id: "troubleshooting"
lang: "ja"
order_index: 4
title: "netstat"
description: "`ss` を使って Linux のソケット、リスナー、キュー、TCP 状態を調べる方法を学びます。"
meta_title: "netstat - トラブルシューティング"
meta_description: "Linux の netstat コマンドを習得し、ネットワーク接続、ポート、ソケットを分析します。このガイドでは、SYN_SENT や netstat close_wait などの一般的な状態をカバーし、効果的なトラブルシューティングを支援します。"
meta_keywords: "linux netstat, netstat, netstat コマンド，syn_sent netstat, netstat close_wait, ネットワーク接続，linux ネットワーキング，ネットワーク分析，linux チュートリアル"
---

従来の `netstat` ツールは、ソケット、ルート、インターフェース統計を表示します。現代の Linux では、カーネルのソケット状態を効率よく公開し、iproute2 とともに保守されている `ss` が、ソケット調査に推奨されます。

## 待ち受けソケットの一覧

TCP と UDP の待ち受けソケットを数値で表示し、権限があれば所有プロセスも表示します。

```bash
$ sudo ss -lntup
```

`-l` はリスナー、`-n` は名前検索の抑止、`-t` と `-u` は TCP と UDP、`-p` はプロセス情報を指定します。UDP はコネクションレスなので、接続されていないバインド済みソケットに TCP のような `LISTEN` ハンドシェイクはありません。

:::single-choice{#netstat-ss-numeric}
ソケットのトラブルシューティングで `-n` を使うのはなぜですか？

::option[新しいネットワーク名前空間を作るため。]{#netstat-new-namespace explanation="このオプションが制御するのは、出力時の名前解決です。"}
::option[アドレス名とポート名の検索を行わないため。]{#netstat-numeric-output .correct explanation="数値表示なら、サービス名の対応付けを観測したプロトコルそのものと取り違えずに済みます。"}
::option[待ち受けていない全ソケットを閉じるため。]{#netstat-close-sockets explanation="状態を調べても、ソケットは終了しません。"}
:::

## ポート、エンドポイント、サービス

ローカルソケットのエンドポイントは、アドレス、トランスポートプロトコル、ポートの組み合わせです。TCP 接続は、プロトコルと、送信元・宛先それぞれのアドレスおよびポートで区別されます。`/etc/services` は慣例的な名前と番号を対応付けますが、現在どのプロセスがポートを所有しているか、どのアプリケーションプロトコルを話すかは証明しません。

:::single-choice{#netstat-services-file-limit}
`/etc/services` の `https 443/tcp` というエントリは何を示しますか？

::option[正常な HTTPS サーバーが現在待ち受けていること。]{#netstat-healthy-listener explanation="静的な名前データベースから実行時の状態は証明できません。"}
::option[そのポートに対する慣例的なサービス名の対応。]{#netstat-conventional-name .correct explanation="ソケットの所有者と実際のプロトコル動作は、実行時の調査とテストで確認する必要があります。"}
::option[ポート 443 の全通信が正しく暗号化されること。]{#netstat-all-encrypted explanation="ポート番号だけでは TLS の動作を検証できません。"}
:::

## TCP 状態を読む

代表的な状態は次のとおりです。

- `SYN-SENT`：ローカルエンドポイントが接続要求を送り、進展を待っている。
- `ESTAB`：TCP 接続が確立している。
- `CLOSE-WAIT`：相手側は送信を閉じたが、ローカルアプリケーションがまだソケットを閉じていない。
- `TIME-WAIT`：能動的に閉じたエンドポイントが、遅延セグメントの期限切れと最終交換の安全な処理を待っている。

`CLOSE-WAIT` が大量に存在し増え続ける場合、ローカルアプリケーションの後始末に問題があることがよくあります。`TIME-WAIT` は正常なプロトコル状態であり、運用上の問題かどうかは量とリソースへの影響で判断します。

:::single-choice{#netstat-close-wait-owner}
`CLOSE-WAIT` のソケットを、まだ閉じる必要があるのはどちら側ですか？

::option[インターネット上のすべてのルーター。]{#netstat-all-routers-close explanation="ルーターはエンドポイントのソケットを所有しません。"}
::option[DNS の権威サーバー。]{#netstat-dns-close explanation="名前サービスは、ローカル TCP の終了処理とは無関係です。"}
::option[ローカルアプリケーション。]{#netstat-local-close .correct explanation="TCP は相手の FIN を受け取り、ローカルプロセスが自分側を閉じるのを待っています。"}
:::

## キューの解釈

`Recv-Q` と `Send-Q` の意味は、状態とプロトコルによって異なります。確立済み TCP ソケットでは、アプリケーションによる受信待ち、または送信確認待ちのデータを示す場合があります。待ち受けソケットのキューフィールドは、同じ意味のアプリケーションペイロード量ではなく、接続バックログの状態を表します。

一回のスナップショットだけで、リークやボトルネックは確定できません。時間を追って測定し、プロセス動作、アプリケーション遅延、再送、リソース上限と照合します。

:::single-choice{#netstat-queue-snapshot}
一度だけ観測した大きなソケットキューでは、診断に不十分なのはなぜですか？

::option[Linux はソケットキューにデータを保存しないから。]{#netstat-no-queues explanation="カーネルのネットワーク処理は、送受信キューを利用します。"}
::option[すべてのキュー値がファイルシステム権限だから。]{#netstat-queue-permission explanation="これらのフィールドはネットワーク状態を示します。"}
::option[影響の判断には状態、傾向、ワークロードの文脈が必要だから。]{#netstat-queue-context .correct explanation="一時的な集中と、継続するアプリケーションまたはネットワークのボトルネックは異なります。"}
:::

## 調査対象を絞り込む

対象のプロトコル、状態、エンドポイント、プロセスだけに出力を限定します。

```bash
$ ss -tn state established
$ ss -ltn 'sport = :443'
```

リスナーが証明するのはローカルのトランスポート準備だけであり、リモートから到達できることやアプリケーションが正常なことではありません。症状に応じて、経路、ファイアウォール、パケット、TLS、アプリケーションを続けてテストしてください。

:::single-choice{#netstat-listener-limit}
ポート 443 の TCP リスナーが存在しても証明できないものはどれですか？

::option[ローカルソケットが bind と listen 操作を受け入れたこと。]{#netstat-listen-local explanation="それこそが表示されているローカル状態です。"}
::option[リモートクライアントが有効な HTTPS 要求を完了できること。]{#netstat-not-remote-proof .correct explanation="経路ポリシー、TLS、アプリケーションの動作はまだテストされていません。"}
::option[TCP に数値のポートフィールドがあること。]{#netstat-port-field explanation="リスナーの出力にその値が直接含まれています。"}
:::

## まとめ

これで、ポートとアプリケーションを混同せず、`ss` でソケット状態を調査できます。

1. プロセス情報付きのリスナーを数値で一覧表示する。
2. 慣例的なサービス名と実行時の所有者を区別する。
3. ローカルエンドポイントの視点で TCP の終了状態を解釈する。
4. ワークロードの文脈とともに、時間を追ってキューを測定する。
5. ローカルリスナーだけでなく、リモートでのアプリケーション動作も確認する。
