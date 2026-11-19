---
lesson_id: "network-monitoring-dns-logs"
course_id: "network-monitoring"
lang: "ja"
order_index: 3
title: "DNS ログ"
description: "DNS の問い合わせ、その応答、後続のアプリケーションの接続を区別する方法を学びます。"
meta_title: "DNS ログ - ネットワーク監視"
meta_description: "DNS の問い合わせ、その応答、後続のアプリケーションの接続を区別する方法を学びます。"
meta_keywords: "DNS ログ, 名前解決, ネットワーク監視, サイバーセキュリティ, Linux Journey"
---

サービスに名前で接続する前に、クライアントは DNS にアドレスを問い合わせることがあります。クライアントに代わって名前を調べる仕組みを**リゾルバー**と呼びます。リゾルバーは問い合わせとその結果を記録できます。

## 問い合わせの内容を特定する

DNS の記録には、時刻、クライアントアドレス、名前、要求されたレコード種別が含まれることがあります。`A` の問い合わせは IPv4 アドレスを要求します。

```text
09:21:00Z client=192.0.2.10 query=site.example type=A result=NOERROR answer=192.0.2.20
09:21:03Z client=192.0.2.10 query=preview.example type=A result=NXDOMAIN
```

最初の結果には、`site.example` のアドレスが含まれます。二つ目は、この問い合わせで `preview.example` に一致する名前が見つからなかったことを示します。

:::single-choice{#network-monitoring-dns-logs-lookup-name} 要求された名前について IPv4 アドレスが返されたのはどの行ですか？

::option[site.example の問い合わせです。]{#network-monitoring-dns-logs-lookup-name-a .correct explanation="この行の応答には IPv4 アドレスが含まれます。"}
::option[preview.example の問い合わせです。]{#network-monitoring-dns-logs-lookup-name-b explanation="NXDOMAIN は、この問い合わせの範囲では、指定された名前が存在しないことを示しています。"}
::option[クライアントが同じなので、両方の行です。]{#network-monitoring-dns-logs-lookup-name-c explanation="クライアントは同じですが、問い合わせの結果は異なります。"}
:::

## 問い合わせの結果を読む

`NOERROR` は、DNS のやり取りでプロトコルエラーが報告されなかったことを示します。応答の内容を示すフィールドも確認します。`NOERROR` でも、要求された種類のアドレスレコードが返らない場合があります。名前解決の失敗は、クライアント側のタイムアウトなど別の結果として記録されることもあります。

:::single-choice{#network-monitoring-dns-logs-no-answer} DNS の行に NOERROR とありますが、応答にアドレスがありません。何を報告しますか？

::option[クライアントは確実に IPv4 アドレスを受け取りました。]{#network-monitoring-dns-logs-no-answer-a explanation="この例で返されたアドレスは、応答のフィールドで分かります。"}
::option[サイトがブラウザーからの接続を確実に拒否しました。]{#network-monitoring-dns-logs-no-answer-c explanation="この行に記録されているのは DNS の結果です。"}
::option[プロトコルエラーはありませんでしたが、この行にアドレスは記録されていません。]{#network-monitoring-dns-logs-no-answer-b .correct explanation="結果と応答のフィールドは、それぞれ異なる情報を示します。"}
:::

## その後の接続を別に調べる

クライアントは名前を調べた後に接続することがあります。実際に接続したかを確かめるには、対応するフローや接続の記録を探し、通信相手と時刻を比較します。DNS の結果はキャッシュされる場合があるため、利用可能なログに新しい問い合わせがないまま接続することもあります。

:::single-choice{#network-monitoring-dns-logs-dns-vs-flow} 後でクライアントが返されたアドレスに接続したかを確認するには、どの記録が最適ですか？

::option[DNS の応答だけを別の方法で表示したものです。]{#network-monitoring-dns-logs-dns-vs-flow-a explanation="DNS の応答には、クライアントが使えるアドレスが示されます。"}
::option[接続先が分かる、該当する接続記録またはフロー記録です。]{#network-monitoring-dns-logs-dns-vs-flow-c .correct explanation="名前解決とは別に、その後の通信を追えます。"}
::option[同じクライアントからの 2 回目の DNS 問い合わせです。]{#network-monitoring-dns-logs-dns-vs-flow-b explanation="名前解決が繰り返されたことは確認できますが、その後にアプリケーションが接続したかは確認できません。"}
:::

## まとめ

DNS ログと、その後の通信の記録を区別して読めるようになりました。

1. クライアント、問い合わせた名前、要求したレコード種別を確認します。
2. 結果と応答の内容をあわせて読み取ります。
3. 後続の接続は、別の記録を探して確認します。
