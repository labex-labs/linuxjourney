---
lesson_id: "dns-tools"
course_id: "dns"
lang: "ja"
order_index: 6
title: "DNS ツール"
description: "getent、resolvectl、dig を使い、システムの名前解決と直接の DNS 問い合わせを比較する方法を学びます。"
meta_title: "DNS ツール - DNS"
meta_description: "nslookup や強力な dig コマンドなど、必須の Linux DNS ツールを探求します。この初心者向けの Linux チュートリアルでは、DNS クエリと DNS トラブルシューティング技術を解説します。"
meta_keywords: "nslookup, dig コマンド，DNS ツール，Linux DNS, DNS トラブルシューティング，ネームサーバー検索，Linux チュートリアル，初心者 Linux"
---

DNS のトラブルシューティングは、どの層をテストしているか特定するところから始まります。システム resolver のツールはローカルファイルとポリシーを含みますが、`dig` と `nslookup` は DNS 問い合わせを送り、特定サーバーを直接対象にできます。

## システム Resolver をテストする

通常のホスト名前サービス経路を使います。

```bash
$ getent ahosts www.example.com
```

systemd-resolved のホストでは、リンクごとのサーバー、search domain、プロトコル状態を調べます。

```bash
$ resolvectl status
$ resolvectl query www.example.com
```

アプリケーションが独自 resolver library や proxy を使う場合もあるため、出力が異なるときはアプリケーション経由でも再現してください。

:::single-choice{#dns-tools-system-resolver}
設定されたシステムの名前サービス経路を動かすコマンドはどれですか？

::option[`dig @SERVER NAME` だけ。]{#dns-tools-dig-direct explanation="dig は DNS 問い合わせを送り、通常 hosts ファイルの対応付けを読みません。"}
::option[`ip link set down`]{#dns-tools-link-down explanation="名前解決をテストせず、インターフェースを中断します。"}
::option[`getent ahosts NAME`]{#dns-tools-getent .correct explanation="`/etc/hosts`、DNS などの Name Service Switch 情報源を反映できます。"}
:::

## dig で問い合わせる

名前とレコード型を指定します。

```bash
$ dig www.example.com A
$ dig www.example.com AAAA
$ dig example.com MX
```

出力には応答サーバー、status、flag、question、answer、authority、additional data、query time、transport metadata が示されます。`+short` はスクリプトに便利ですが、診断に必要な証拠を隠します。

:::single-choice{#dns-tools-record-type}
IPv6 address レコードを要求する問い合わせはどれですか？

::option[`dig NAME AAAA`]{#dns-tools-aaaa .correct explanation="AAAA レコードは IPv6 アドレスを含みます。"}
::option[`dig NAME MX`]{#dns-tools-mx explanation="MX は mail exchanger レコードを要求します。"}
::option[forward name に対する `dig NAME PTR`。]{#dns-tools-ptr-forward explanation="PTR は通常、reverse-lookup name を使って問い合わせます。"}
:::

## サーバーを選ぶ

resolver または authoritative server を明示的に指定します。

```bash
$ dig @192.0.2.53 www.example.com A
```

cache と authority を切り分けるときは、設定済み recursive resolver、承認済みの二つ目の resolver、各 authoritative server を比較します。`NOERROR` status でも要求した answer がない場合があります。`NXDOMAIN` は問い合わせた名前が存在しないこと、`SERVFAIL` はサーバーが問い合わせを完了できなかったことを意味します。

:::single-choice{#dns-tools-noerror-empty}
`NOERROR` でも answer section が空になることはありますか？

::option[はい。名前は存在するが、要求したレコードデータがない場合です。]{#dns-tools-noerror-nodata .correct explanation="status と answer count を一緒に解釈する必要があります。"}
::option[いいえ。少なくとも一つの address レコードが必ずあります。]{#dns-tools-noerror-always-answer explanation="名前が存在しても、要求した type のデータがない場合があります。"}
::option[いいえ。空の answer は常に Ethernet 障害です。]{#dns-tools-empty-ethernet explanation="有効な no-data response は、リンクフレームではなく DNS の意味によって説明できます。"}
:::

## Recursion と Authority を確認する

問い合わせの `rd` は recursion を要求し、応答の `ra` はサーバーが recursion を提供することを示します。`aa` は answer が authoritative であることを意味します。authoritative server へは `+norecurse` で問い合わせ、recursive cache と提供中の zone data を混同しないようにします。

`dig +trace NAME` は root hint から独自に反復探索します。production resolver の cache、forwarding、policy、DNSSEC validation、network location を通らないため、その resolver とは結果が異なる場合があります。

:::single-choice{#dns-tools-aa-flag}
応答の `aa` flag は何を意味しますか？

::option[問い合わせが同じ二つの IPv4 アドレスを使った。]{#dns-tools-two-addresses explanation="この flag は answer count や address family と無関係です。"}
::option[応答がアプリケーションの認証情報で暗号化された。]{#dns-tools-aa-encrypted explanation="DNS flag は暗号化トランスポートを証明しません。"}
::option[answer が authoritative である。]{#dns-tools-authoritative-answer .correct explanation="応答サーバーは、その answer data に対して権威を持つと表明しています。"}
:::

## Reverse Query と TCP Query をテストする

`-x` を使って reverse PTR query を組み立てます。

```bash
$ dig -x 192.0.2.25
```

truncation、zone transfer、ファイアウォール差異を調べるときは、TCP 上の DNS をテストします。

```bash
$ dig +tcp @192.0.2.53 example.com SOA
```

現代の DNS は UDP または TCP のポート 53 を使えます。必要な場所では両方を許可すべきです。UDP answer に truncation flag があると、準拠クライアントは適切なトランスポートで再試行します。

:::single-choice{#dns-tools-tcp-test}
`dig +tcp` は何を変更しますか？

::option[既定の UDP 試行ではなく、TCP で DNS 問い合わせを送る。]{#dns-tools-use-tcp .correct explanation="トランスポートのフィルタリングと、大きな信頼性のある stream を要する応答を切り分けるのに役立ちます。"}
::option[TCP のサービス名レコードだけを要求する。]{#dns-tools-tcp-records explanation="要求する DNS type は別途指定します。"}
::option[サーバーの resolver 設定を恒久的に変更する。]{#dns-tools-tcp-persistent explanation="問い合わせはサーバー設定を編集しません。"}
:::

## まとめ

これで、調査対象の resolver 層に合った DNS ツールを選べます。

1. 設定済みシステム resolver の経路には `getent` を使う。
2. 明示的なレコード型とサーバーを指定して `dig` を使う。
3. status、flag、section、応答サーバーをまとめて解釈する。
4. recursive cache と authoritative data を区別する。
5. reverse query と、必要な両方の DNS transport をテストする。
