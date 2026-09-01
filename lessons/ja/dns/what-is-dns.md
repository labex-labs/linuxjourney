---
lesson_id: "what-is-dns"
course_id: "dns"
lang: "ja"
order_index: 1
title: "DNS とは？"
description: "DNS が分散された名前と型付きリソースレコードを体系化し、解決する仕組みを学びます。"
meta_title: "DNS とは？ - DNS"
meta_description: "Linux ネットワーキングを学ぶなら、DNS の理解は不可欠です。このガイドでは、ドメインネームシステム（DNS）の概要、ドメイン名を IP アドレスに変換する仕組み、そしてなぜそれがインターネットの必須のアドレス帳なのかを解説します。Linux 学習を始める方に最適です。"
meta_keywords: "DNS, ドメインネームシステム，IP アドレス，Linux 学習，Linux, ホスト名，Linux ネットワーキング，初心者，チュートリアル，ガイド，labex linux"
---

Domain Name System（DNS）は、分散型の階層データベースであり、問い合わせプロトコルでもあります。クライアントは名前に関連付けられた型付き情報を取得でき、そこにはアドレス、メールルーティング、権威サーバー、サービスデータ、検証レコードなどが含まれます。

## 名前とリソースレコード

DNS は、一つのホスト名を一つの IP アドレスへ変換するだけではありません。`A` レコードは IPv4 アドレス、`AAAA` は IPv6 アドレス、`MX` はメールルーティング情報、`NS` は権威サーバー名を保持し、ほかにもさまざまな型が別種のデータを運びます。一つの名前に複数レコードがある場合も、アドレスレコードがない場合もあります。

:::single-choice{#dns-purpose-beyond-address} DNS が単なるホスト名とアドレスの一覧ではないのはなぜですか？

::option[すべての Ethernet フレームへ MAC アドレスを恒久的に割り当てるから。]{#dns-mac-frames explanation="リンク層の近隣探索は、そのような方法で DNS を使いません。"}
::option[複数種類のサービス情報や委任情報を型付きレコードとして保存するから。]{#dns-typed-records .correct explanation="アドレス、メール、権威、別名、ポリシー関連のレコードには、それぞれ異なる意味があります。"}
::option[名前を持つすべてのアプリケーションの正常性を保証するから。]{#dns-health-guarantee explanation="宛先サービスが利用できなくても、DNS データは正常に解決できる場合があります。"}
:::

## 階層化された名前

Fully Qualified Domain Name（FQDN）は、DNS ツリー内の経路を識別します。`www.example.com.` では、最後のドットが root、その下が `com`、さらにその下が `example`、`www` はそのドメイン内の名前です。末尾のドットはユーザーインターフェースで省略されることが多いものの、設定内で絶対名とローカル相対名を区別するときに重要です。

:::single-choice{#dns-trailing-dot} `www.example.com.` の最後のドットは何を表しますか？

::option[DNS root と絶対名。]{#dns-root-dot .correct explanation="このドットが、名前付きノードから root までの完全な経路を終端します。"}
::option[すべてのトップレベルドメインに対するワイルドカード。]{#dns-dot-wildcard explanation="ワイルドカードは root 終端記号ではなく、`*` などのラベルを使います。"}
::option[IPv4 だけを使うという指示。]{#dns-dot-ipv4 explanation="要求するアドレスファミリーはレコード型で制御します。"}
:::

## 分散された権威

DNS の権威は階層に沿って下位へ委任されます。root server は resolver を top-level-domain server へ導き、そこから委任済み zone の authoritative server へ導きます。組織は、一つの中央サーバーへ全世界の名前空間を保存せず、自組織の権威データを管理できます。

:::single-choice{#dns-authoritative-data} 委任済み DNS zone の決定的なデータを提供するのは誰ですか？

::option[以前そのサイトを訪れた任意のブラウザー。]{#dns-browser-authority explanation="ブラウザーのキャッシュは、その zone に対して権威を持ちません。"}
::option[その zone に設定された authoritative name server。]{#dns-authoritative-servers .correct explanation="委任によって、権威を持って応答する責任のあるサーバーが特定されます。"}
::option[そのアドレスへパケットを運ぶすべてのルーター。]{#dns-router-authority explanation="パケット転送と DNS の権威は別の役割です。"}
:::

## 名前解決とキャッシュ

ホストの stub resolver は通常、recursive resolver へ問い合わせを送ります。その resolver は有効なキャッシュから応答するか、クライアントに代わって階層へ問い合わせます。レコードの TTL は、通常キャッシュエントリを再利用できる期間を制限します。規模を拡大しやすくする一方、キャッシュが更新されるまで変更が見えにくくなります。

DNS の成功は、経路、トランスポート、TLS、アプリケーションの正常性を証明しません。また、`/etc/hosts`、search suffix、ローカルキャッシュ、名前サービスのポリシーがシステムの resolver に影響するため、外部へ問い合わせる前に DNS 解決が失敗することもあります。

:::single-choice{#dns-cache-ttl-role} DNS レコードの TTL が主に制御するものは何ですか？

::option[IP パケットが通過できるルーター数。]{#dns-ip-hop-limit explanation="IP の TTL または Hop Limit は別のプロトコルフィールドです。"}
::option[アプリケーションが正常でなければならない期間。]{#dns-app-health-time explanation="DNS キャッシュはサービスの可用性を保証しません。"}
::option[通常の規則で resolver がレコードをキャッシュできる期間。]{#dns-cache-lifetime .correct explanation="キャッシュ期間の長短は、問い合わせ負荷と変更の伝播に影響します。"}
:::

## まとめ

これで、DNS を型付き・キャッシュ付き・階層型のデータシステムとして説明できます。

1. DNS リソースレコードの型を目的別に区別する。
2. Fully Qualified Domain Name を root から下向きに読む。
3. 委任と権威を持つ責任主体を特定する。
4. 名前解決とアプリケーション接続性を区別する。
