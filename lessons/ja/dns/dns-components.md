---
lesson_id: "dns-components"
course_id: "dns"
lang: "ja"
order_index: 2
title: "DNS コンポーネント"
description: "recursive resolver、authoritative server、zone、リソースレコードが DNS の責務を分担する仕組みを学びます。"
meta_title: "DNS コンポーネント - DNS"
meta_description: "DNS コンポーネントについて学びます：ネームサーバー、ゾーンファイル、リソースレコード。初心者向けに DNS の仕組みを理解します。Linux ネットワーキングの旅を始めましょう！"
meta_keywords: "DNS コンポーネント，ネームサーバー, ゾーンファイル，リソースレコード，DNS チュートリアル，Linux ネットワーキング，初心者ガイド"
---

DNS は、クライアント向けの再帰処理と権威データの公開を別の役割として扱います。この境界を理解すれば、キャッシュからの応答を zone の所有者による応答と取り違えずに済みます。

## Stub Resolver と Recursive Resolver

アプリケーションまたは OS 内の stub resolver は、設定済み recursive resolver へ問い合わせます。recursive resolver はキャッシュを使い、必要なら反復問い合わせを行って、最終回答、エラー、または referral の結果を返します。応答に authoritative-answer フラグを付けられるのは、応答サーバーがそのデータへ権威を持つ場合だけです。再帰処理を行うだけで権威サーバーになるわけではありません。

:::single-choice{#dns-components-recursive-role} recursive resolver は stub client のために何をしますか？

::option[キャッシュとほかの name server を使って、最終的な DNS 結果を取得する。]{#dns-components-recursive-result .correct explanation="クライアントは複数段階の検索作業を recursive service に委ねます。"}
::option[パケット経路上の全ネットワークルーターを置き換える。]{#dns-components-replaces-router explanation="名前解決と IP 転送は別の仕組みです。"}
::option[キャッシュした全レコードの authoritative server になる。]{#dns-components-cache-authority explanation="キャッシュ済みデータの権威は元の情報源にあり、resolver は zone の所有者ではありません。"}
:::

## Authoritative Name Server

authoritative server は、自身が権威を持つ zone データから応答します。一つの zone には、データを同期した複数の authoritative server を用意し、障害要因の独立性も考慮すべきです。authoritative-only server は、任意のクライアントに対して再帰処理を行う必要はありません。

:::single-choice{#dns-components-authoritative-role} サーバーがある zone に対して authoritative になる条件は何ですか？

::option[一度だけ公開 resolver 経由でその zone を問い合わせたこと。]{#dns-components-once-queried explanation="問い合わせやキャッシュによって権威が与えられることはありません。"}
::option[関連する委任と設定の下で、その zone データを提供すること。]{#dns-components-serves-zone .correct explanation="権威は DNS の委任とサーバーに読み込まれた zone から生じ、キャッシュコピーの所有からは生じません。"}
::option[一度の ping に最速で応答したこと。]{#dns-components-fastest-ping explanation="ICMP の応答時間は DNS の権威を定義しません。"}
:::

## Zone と Zone の保存

zone は、DNS 名前空間のうち管理上サービスを提供する部分です。zone apex から始まり、子 zone を委任できます。zone データはテキストの zone file、データベースからの生成、API からの読み込み、ソフトウェアによる合成などで提供でき、「zone file」は必須の物理実装ではありません。

zone apex には通常、SOA レコードと NS の集合があります。親側の委任データは子の authoritative server を特定し、bailiwick 内のサーバー名へ到達するための glue address レコードを伴うことがあります。

:::single-choice{#dns-components-zone-meaning} DNS zone とは何ですか？

::option[管理上サービスを提供する名前空間の一部分。]{#dns-components-admin-portion .correct explanation="保存先の実装にかかわらず、レコードと委任を含められます。"}
::option[すべてのクライアントに必須の単一テキストファイル。]{#dns-components-client-file explanation="権威サーバーは複数の保存形式を使え、クライアントが全 zone を保持するわけでもありません。"}
::option[VLAN で識別される Ethernet ブロードキャストドメイン。]{#dns-components-vlan explanation="DNS zone とリンク層セグメントは独立した概念です。"}
:::

## リソースレコードのフィールド

リソースレコードは、owner name、TTL、class、type、type 固有の RDATA を持ちます。例を示します。

```text
www.example.com.  300  IN  A  192.0.2.25
```

owner は `www.example.com.`、TTL は 300 秒、class は Internet、type は IPv4 address、RDATA はそのアドレスです。zone file 構文にはフィールドの省略と相対名の規則があるため、origin を慎重に扱う必要があります。

:::single-choice{#dns-components-mx-type} mail exchanger の優先度とホスト名を公開するレコード型はどれですか？

::option[`A`]{#dns-components-a explanation="A レコードは IPv4 アドレスを保存します。"}
::option[`NS`]{#dns-components-ns explanation="NS レコードは authoritative name server を識別します。"}
::option[`MX`]{#dns-components-mx .correct explanation="MX の RDATA には優先度と mail exchanger 名が含まれます。"}
:::

## TTL と Negative Caching

正のレコードは TTL によってキャッシュ再利用期間を制限します。存在しない名前が証明された場合などの negative answer も、SOA から導かれる規則に従ってキャッシュできます。計画変更の直前に TTL を下げても、キャッシュが低い値を観測した後に取得したレコードにしか影響しません。以前に長い TTL でキャッシュされたものは、期限まで残ります。

:::single-choice{#dns-components-lower-ttl-timing} 計画したアドレス変更より十分前に DNS TTL を下げるのはなぜですか？

::option[TTL がサーバーの Ethernet MTU を変更するから。]{#dns-components-ttl-mtu explanation="キャッシュ期間とリンク上のパケットサイズは無関係です。"}
::option[低い TTL によって新しいアプリケーションの正常性が保証されるから。]{#dns-components-ttl-health explanation="影響するのはキャッシュ動作であり、サービスの正しさではありません。"}
::option[古い長い TTL で学習したレコードが、既存キャッシュから期限切れになる時間が必要だから。]{#dns-components-old-cache-expiry .correct explanation="権威データを変更しても、すでにキャッシュされたレコードの残り時間を遡って短縮することはできません。"}
:::

## まとめ

これで、DNS の再帰処理、権威、名前空間管理、キャッシュ済みレコードを区別できます。

1. stub resolver と recursive resolver の役割を識別する。
2. 委任された zone service を通じて権威を定義する。
3. zone を必須の単一ファイルではなく、名前空間に対する責任として扱う。
4. owner、TTL、class、type、RDATA の各フィールドを読む。
5. DNS 変更前にキャッシュ期間を計画する。
