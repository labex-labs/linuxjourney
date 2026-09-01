---
lesson_id: "dns-process"
course_id: "dns"
lang: "ja"
order_index: 3
title: "DNS プロセス"
description: "stub resolver と recursive resolver がキャッシュ、referral、glue、権威を使って DNS 問い合わせへ応答する流れを学びます。"
meta_title: "DNS プロセス - DNS"
meta_description: "ルートサーバーから権威 DNS サーバーまでのステップバイステップの DNS 解決プロセスを探ります。Linux サーバーがドメインを見つける方法を理解することは、本番環境やドメインホスティングにとって極めて重要です。"
meta_keywords: "DNS プロセス，DNS ルックアップ，ドメイン解決，linux dns, 本番サーバー, ドメインホスティング，DNS サーバー, TLD, ルートサーバー, 権威 DNS"
---

通常のアプリケーションは OS の stub resolver へ問い合わせます。stub resolver はローカルの名前サービス方針を参照し、設定済み resolver へ再帰問い合わせを送ります。recursive resolver が階層をたどるのは、有効なキャッシュだけでは回答できない場合です。

## ローカルポリシーとキャッシュから始める

システムの resolver は、設定された順序で `/etc/hosts`、DNS などの情報源を参照できます。search suffix によって短い名前が複数の候補名へ変換される場合もあります。recursive resolver は上流へ問い合わせる前に、正と負のキャッシュエントリを確認します。

:::single-choice{#dns-process-cache-first} recursive resolver が問い合わせ時に authoritative server へ一切接続しない場合があるのはなぜですか？

::option[DNS では、すべての問い合わせがまずローカルで失敗する必要があるから。]{#dns-process-requires-failure explanation="resolver はキャッシュから直ちに回答できます。"}
::option[まだ有効な回答をキャッシュしているから。]{#dns-process-valid-cache .correct explanation="キャッシュにより、レコードの有効期間が切れるまで階層探索を繰り返さずに済みます。"}
::option[authoritative server がクライアントからの Ethernet フレームしか受け付けないから。]{#dns-process-authoritative-ethernet explanation="DNS はルーティングされたネットワークを越え、IP トランスポート上で動作します。"}
:::

## Root Server へ問い合わせる

キャッシュミス時、recursive resolver は root server へ問い合わせられます。DNS root には A から M まで 13 個の名前付きサーバー identity があり、anycast などの耐障害性を高める配置技術を使って、多数の物理インスタンスから提供されています。通常、その応答は最終的なホストアドレスではなく、該当する top-level domain の authoritative server を resolver へ紹介します。

:::single-choice{#dns-process-root-response} キャッシュにない `www.example.com` の検索に、root server は通常何を返しますか？

::option[`com` top-level-domain server への referral。]{#dns-process-root-referral .correct explanation="root に全ホストの最終レコードを保存せず、階層に沿って責任を委任します。"}
::option[`www.example.com` でホストされる Web ページ。]{#dns-process-root-webpage explanation="DNS が返すのはリソースレコードデータであり、アプリケーションの内容ではありません。"}
::option[宛先の Ethernet MAC アドレス。]{#dns-process-root-mac explanation="MAC アドレスは DNS 階層ではなく、ローカルリンク上で解決します。"}
:::

## TLD と Authoritative Referral をたどる

resolver は `com` authoritative server へ問い合わせ、`example.com` に委任された authoritative name server を受け取ります。委任された子 zone の内部に名前を持つサーバーへ到達する必要がある場合、referral に glue address レコードが含まれることがあります。その後 resolver は、要求されたレコードを authoritative server へ問い合わせます。

:::single-choice{#dns-process-glue-purpose} DNS glue はどの問題の解決に役立ちますか？

::option[DNS 解決後に HTTP ペイロードを暗号化すること。]{#dns-process-glue-http explanation="ペイロード暗号化は TLS などのアプリケーションセキュリティが扱います。"}
::option[最速の Ethernet スイッチポートを選ぶこと。]{#dns-process-glue-switch explanation="glue は委任用のアドレスデータであり、リンク転送ポリシーではありません。"}
::option[循環的な名前解決をせず、bailiwick 内のサーバーへ到達すること。]{#dns-process-glue-reachability .correct explanation="親側が、子 zone 内に名前を持つサーバーへ接続するために必要なアドレスデータを提供します。"}
:::

## 別名とレコード型をたどる

回答に CNAME alias が含まれ、別の名前をさらに検索する場合や、アプリケーション固有レコードによって追加問い合わせが必要な場合があります。`A` の問い合わせが返すのは IPv4 address レコードと関連する chain data だけです。IPv6 アドレスは別の `AAAA` 問い合わせで取得します。最終応答には `NOERROR`、`NXDOMAIN`、`SERVFAIL` など、意味の異なる status が含まれます。

:::single-choice{#dns-process-nxdomain-meaning} `NXDOMAIN` は何を報告しますか？

::option[authoritative な結果によれば、問い合わせたドメイン名が存在しない。]{#dns-process-name-does-not-exist .correct explanation="名前は存在するが要求したレコード型だけがない場合とは異なります。"}
::option[名前は存在し、常に空の A レコードを持つ。]{#dns-process-empty-a explanation="存在する名前に要求データがない場合、通常は NXDOMAIN ではなく no-data response になります。"}
::option[resolver が Ethernet フレームの最大サイズへ達した。]{#dns-process-frame-size explanation="この status が扱うのは名前の存在です。"}
:::

## 検証、キャッシュ、アプリケーションでの利用

検証を行う recursive resolver は、DNSSEC 署名と chain of trust を使って、authenticated denial またはレコードの完全性を検証できます。DNSSEC は問い合わせを暗号化せず、返されたアドレス上のアプリケーションが信頼できることも証明しません。

resolver は TTL の規則に従って結果をキャッシュし、stub へ返します。その後アプリケーションがアドレスを選び、自身のネットワーク・セキュリティプロトコルを試します。

:::single-choice{#dns-process-dnssec-limit} DNSSEC の検証が提供しないものはどれですか？

::option[署名済み DNS データの完全性と origin authentication。]{#dns-process-dnssec-does-integrity explanation="これらは DNSSEC の中心的な目的です。"}
::option[署名された存在しないデータに対する authenticated denial。]{#dns-process-authenticated-denial explanation="署名付き否定の仕組みによって、その検証を提供できます。"}
::option[DNS の問い合わせと応答の機密性。]{#dns-process-no-confidentiality .correct explanation="暗号化には DoT や DoH など、別の保護された DNS トランスポートが必要です。"}
:::

## まとめ

これで、ローカルポリシーからキャッシュ済み最終応答まで、再帰 DNS 検索を追跡できます。

1. ローカルの情報源と resolver キャッシュを最初に確認する。
2. root と top-level-domain の referral をたどる。
3. glue を使って適切な委任先サーバーへ到達する。
4. alias、no-data answer、存在しない名前を区別する。
5. DNSSEC の完全性とトランスポートの機密性を区別する。
