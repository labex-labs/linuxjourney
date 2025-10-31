---
index: 6
lang: "ja"
title: "DNS ツール"
meta_title: "DNS ツール - DNS"
meta_description: "nslookup や強力な dig コマンドなど、必須の Linux DNS ツールを探求します。この初心者向けの Linux チュートリアルでは、DNS クエリと DNS トラブルシューティング技術を解説します。"
meta_keywords: "nslookup, dig コマンド，DNS ツール，Linux DNS, DNS トラブルシューティング，ネームサーバー検索，Linux チュートリアル，初心者 Linux"
---

## Lesson Content

Linux では、ネットワーク診断のためにいくつかのコマンドラインユーティリティが利用可能です。ドメインネームシステム（DNS）の問題に関しては、`nslookup`と`dig`という 2 つの主要な**DNS ツール**が際立っています。これらをどのように使用するかを理解することは、**Linux DNS**サーバーまたはクライアントでのあらゆる**DNS トラブルシューティング**にとって極めて重要です。

### 基本的な DNS クエリのための nslookup の使用

`nslookup`（ネームサーバー検索）ツールは、DNS サーバーにクエリを実行してドメイン名または IP アドレスのマッピング情報を取得するための古典的なユーティリティです。単純なルックアップには素早く簡単なツールですが、`dig`に取って代わられることもあります。

`www.google.com`のようなドメインの IP アドレスを見つけるには、以下を実行できます。

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

この出力では、`Server`と`Address`がクエリに応答した DNS サーバーを示しています。`Non-authoritative answer`は、サーバーが権威ソースに直接問い合わせるのではなく、キャッシュされた結果を提供したことを意味します。`Name`と`Address`は、ドメインに対して解決された IP アドレスを示します。

### dig による高度な DNS トラブルシューティング

`dig`（ドメイン情報検索）コマンドは、DNS ネームサーバーを調査するための強力で柔軟なツールです。これは`nslookup`よりも詳細な情報を提供するため、本格的な**DNS トラブルシューティング**で好まれる選択肢です。

**dig コマンド**を使用した例を次に示します。

```bash
pete@icebox:~$ dig www.google.com

; <<>> DiG 9.9.5-3-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42376
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
;; QUESTION SECTION:
;www.google.com.                        IN      A

;; ANSWER SECTION:
www.google.com.         5       IN      A       74.125.239.147
www.google.com.         5       IN      A       74.125.239.144
www.google.com.         5       IN      A       74.125.239.146
www.google.com.         5       IN      A       74.125.239.145
www.google.com.         5       IN      A       74.125.239.148

;; Query time: 27 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Feb 07 10:14:00 PST 2016
;; MSG SIZE  rcvd: 123
```

`dig`の出力はセクションに整理されています。

- **QUESTION SECTION**: 送信されたクエリを示します。ここでは、`www.google.com`の`A`（アドレス）レコードを要求しました。
- **ANSWER SECTION**: DNS サーバーから受信した回答を表示します。この場合、Google にはドメインに関連付けられた複数の IP アドレスがあります。
- **Statistics**: 最後のセクションでは、クエリ時間や応答したサーバーなど、クエリに関するメタデータを提供します。

その詳細な出力と柔軟性から、`dig`は Linux でネットワークサービスを管理またはトラブルシューティングする人にとって不可欠なユーティリティです。

## Exercise

Linux ネットワーキングユーティリティでの経験を積むために、次のハンズオンラボを試すことを検討してください。

1. **[Linux で ethtool を使用してネットワークインターフェイス設定を確認する](https://labex.io/ja/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - `ethtool`コマンドを使用して、インターフェイス速度とデュプレックスの表示と設定、リンクモードの分析など、ネットワークインターフェイスの設定を確認および管理する方法を学び、物理層のネットワークの問題をトラブルシューティングします。

このラボは、概念を実際のシナリオに適用し、ネットワークインターフェイスの管理に対する自信を構築するのに役立ちます。

## Quiz Question

DNS ネームサーバーに関する詳細情報を取得するために使用されるツールは何ですか？回答には小文字の英字のみを使用してください。

## Quiz Answer

dig
