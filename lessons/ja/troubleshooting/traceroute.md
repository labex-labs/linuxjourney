---
lesson_id: "traceroute"
course_id: "troubleshooting"
lang: "ja"
order_index: 3
title: "traceroute"
description: "traceroute が応答するホップを検出する仕組みと、欠落、時間、経路変化の解釈方法を学びます。"
meta_title: "traceroute - トラブルシューティング"
meta_description: "traceroute Linux コマンドを習得し、ネットワーク経路の追跡と接続問題のトラブルシューティングを行いましょう。このチュートリアルでは、traceroute が TTL を使用してパケットが宛先に到達するまでの経路をマッピングする方法を解説します。"
meta_keywords: "traceroute, traceroute linux, Linux ネットワーキング，ネットワークトラブルシューティング，TTL, パケットルーティング，Linux コマンド，初心者，チュートリアル"
---

`traceroute` は、IPv4 の TTL または IPv6 の Hop Limit を徐々に増やしながらプローブを送ります。その値が尽きたルーターは Time Exceeded メッセージを返すことがあり、往路上で応答した地点の一部が明らかになります。

## ホップ検出の仕組み

プローブはホップ上限 1 から始まり、順に増えていきます。最初のルーターが値を一つ減らして 0 にすると、ICMP エラーを返せます。上限 2 なら二番目のルーターで尽きます。この処理を、宛先が応答するか最大値に達するまで続けます。

:::single-choice{#traceroute-expiring-field} 連続するプローブを、より先のルーターで順に期限切れにするフィールドはどれですか？

::option[宛先名に対する DNS キャッシュの TTL。]{#traceroute-dns-ttl explanation="DNS レコードの有効期間は、パケットが転送されるホップ数を制御しません。"}
::option[Ethernet の送信元 MAC アドレス。]{#traceroute-source-mac explanation="リンクアドレスには、終端間のホップカウンターはありません。"}
::option[IPv4 の TTL または IPv6 の Hop Limit。]{#traceroute-hop-field .correct explanation="この上限付き転送回数を増やすことで、応答するルーティング済みホップを明らかにします。"}
:::

## プローブ方式

従来の Linux traceroute は、通常、高い宛先ポートへ UDP プローブを送ります。宛先は ICMP Port Unreachable を返して到達を知らせられます。オプションを使えば ICMP Echo や TCP SYN プローブに変更でき、フィルタリングの通過状況が異なる場合があります。

```bash
$ traceroute -n example.com
$ traceroute -I -n example.com
$ traceroute -T -p 443 -n example.com
```

必要な権限と対応オプションは環境ごとに異なります。対象に対して許可された方式だけを使い、結果を比較するときは方式も記録してください。

:::single-choice{#traceroute-default-destination-response} 従来の Linux UDP traceroute は、一般に何を受け取ると終了しますか？

::option[宛先からの ICMP Port Unreachable 応答。]{#traceroute-port-unreachable .correct explanation="高い UDP ポートは通常未使用なので、宛先はこのエラーによって自身への到達を知らせられます。"}
::option[全ルーターからの必須 HTTP 200 応答。]{#traceroute-http-every-router explanation="ルーターが返すのはネットワーク制御エラーであり、HTTP 応答ではありません。"}
::option[インターネット全体へ届く宛先からの Ethernet ブロードキャスト。]{#traceroute-ethernet-broadcast explanation="リンク層のブロードキャストは、ルーティングされた経路を越えません。"}
:::

## アスタリスクの解釈

アスタリスクは、そのプローブに対応する応答をタイムアウトまでに観測できなかったことを意味します。ルーターが通過トラフィックを転送しながら、診断応答をフィルタリングまたはレート制限している場合もあります。後続ホップが応答したなら、無応答のホップも少なくとも一部のプローブを転送したことは明らかです。

:::single-choice{#traceroute-asterisk-meaning} あるホップの `*` だけから何が証明できますか？

::option[そのルーターが全通過パケットを恒久的に破棄したこと。]{#traceroute-star-all-drop explanation="後続の応答があれば、転送が続いていたことを確認できます。"}
::option[タイムアウトまでに一致する応答が届かなかったことだけ。]{#traceroute-star-no-response .correct explanation="フィルタリング、レート制限、損失、復路の問題のいずれでも無応答になり得ます。"}
::option[宛先に IP アドレスがないこと。]{#traceroute-star-no-address explanation="プローブはすでにアドレスを対象としており、一つの無応答ホップでそのアドレスが消えるわけではありません。"}
:::

## 時間と経路の変化

各ホップの時間は制御応答までの往復時間であり、隣り合う表示行の間のリンクが加えた遅延ではありません。ルーターがコントロールプレーンの応答を低優先度にすることもあります。負荷分散によって各プローブが別経路を通る場合があり、名前解決も表示を遅らせます。`-n` を使えば逆引きを避けられます。

各 ICMP 応答の復路が往路と異なる場合もあります。ボトルネックを特定する前にテストを繰り返し、エンドポイントでのアプリケーション時間と照合してください。

:::single-choice{#traceroute-hop-rtt-limit} 隣接ホップの RTT 値を引いて正確なリンク遅延とすべきでないのはなぜですか？

::option[traceroute の時間はミリ秒ではなく、すべてバイト単位だから。]{#traceroute-times-bytes explanation="表示されるプローブ時間は、通常ミリ秒単位です。"}
::option[応答が異なる復路を通り、コントロールプレーン処理も異なり得るから。]{#traceroute-rtt-asymmetry .correct explanation="各測定値は始点から各ホップまでの別々の往復時間であり、同期された片道リンク測定ではありません。"}
::option[すべてのルーターの時計が送信元と同じだから。]{#traceroute-router-clock explanation="この測定は、リモートの時計の同期に依存しません。"}
:::

## アプリケーションとの比較

traceroute が宛先へ到達してもサービスが遮断されている場合があり、反対に中継ルーターが応答を隠していてもサービスは動作し得ます。アプリケーションと同じアドレスファミリー、宛先、トランスポートプロトコル、ポートをテストし、traceroute は経路を裏付ける証拠として使ってください。

:::single-choice{#traceroute-service-proof} traceroute が完了すれば、HTTPS サービスが正常だと証明できますか？

::option[はい。各ホップがサーバー証明書を検証するためです。]{#traceroute-validates-cert explanation="ルーターはクライアントに代わって TLS 検証をしません。"}
::option[いいえ。トランスポート、TLS、HTTP の動作は別々にテストする必要があります。]{#traceroute-not-app-proof .correct explanation="経路検出とアプリケーションの健全性は、異なる診断層です。"}
::option[はい。ただし逆引き DNS 名が表示される場合だけです。]{#traceroute-rdns-proof explanation="名前が表示されても、アプリケーションの動作は確認できません。"}
:::

## まとめ

これで、traceroute を完全な経路を知る万能手段ではなく、ホップ上限付きの連続プローブとして解釈できます。

1. TTL または Hop Limit の期限切れによるホップ検出を説明する。
2. UDP、ICMP、TCP のどのプローブを使ったか記録する。
3. アスタリスクを障害の証明ではなく、応答欠落として扱う。
4. 隣接ホップの RTT から正確なリンク遅延を算出しない。
5. 経路の証拠を実際のアプリケーションと照合する。
