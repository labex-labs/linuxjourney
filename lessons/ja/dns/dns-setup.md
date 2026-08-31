---
lesson_id: "dns-setup"
course_id: "dns"
lang: "ja"
order_index: 5
title: "DNS 設定"
description: "authoritative または recursive DNS サービスを選択し、安全に設定、検証、運用する方法を学びます。"
meta_title: "DNS 設定 - DNS"
meta_description: "BIND、DNSmasq、PowerDNS など、Linux で人気のある DNS サーバーについて学びましょう。この初心者向けのガイドで、ネットワーク設定に最適な DNS サーバーを見つけてください。"
meta_keywords: "Linux DNS, BIND, DNSmasq, PowerDNS, DNS サーバー設定，Linux ネットワーキング，DNS チュートリアル，初心者"
---

DNS ソフトウェアは、普遍的な「最良のサーバー」ではなく、役割と運用要件に応じて選びます。authoritative service は zone を公開し、recursive service は名前を解決・キャッシュしてクライアントへ応答し、forwarding resolver は別の resolver へ問い合わせます。役割を組み合わせると攻撃対象領域が変わります。

## 役割と実装を選ぶ

- BIND は、幅広い標準に対応した authoritative service と recursive service を提供できる。
- Unbound は、検証を行う recursive resolver としてよく利用される。
- dnsmasq は、規模の小さい管理済みネットワーク向けに、軽量の forwarding、caching、DHCP 機能を提供する。
- PowerDNS は、複数のデータ backend に対応した別々の authoritative 製品と recursive 製品を提供する。

機能とパッケージは変化するため、インストール済みバージョンの公式文書を参照してください。必要な役割だけを配備し、意図しない recursion または zone service を無効にします。

:::single-choice{#dns-setup-authoritative-role}
自身が提供する zone の決定的なレコードを公開する役割はどれですか？

::option[Authoritative DNS server。]{#dns-setup-authoritative .correct explanation="任意の名前を再帰的に探すのではなく、設定された zone の権威データから応答します。"}
::option[Ethernet switch。]{#dns-setup-switch explanation="スイッチはリンク層フレームを転送し、DNS zone を公開しません。"}
::option[任意のクライアント問い合わせへ答える recursive resolver。]{#dns-setup-stub explanation="stub は recursive service へ問い合わせを送るもので、authoritative zone をホストしません。"}
:::

## インストール前に設計する

zone、クライアント、問い合わせ量、更新方法、DNSSEC 要件、ログ、監視、バックアップ、復旧を定義します。authoritative zone には冗長サーバーと正しく登録された委任が必要です。recursive service には、明示的なクライアントアクセス制御、キャッシュポリシー、上流または反復問い合わせ先への到達性、不正利用対策が必要です。

制限のない recursion をインターネットへ公開してはいけません。open resolver は reflection attack に悪用され、ローカルリソースも消費します。

:::single-choice{#dns-setup-open-recursion}
recursive 問い合わせを許可済みクライアントへ制限するのはなぜですか？

::option[recursive DNS はどのレコードもキャッシュできないから。]{#dns-setup-no-cache explanation="キャッシュは recursive resolver の中心的な機能です。"}
::option[authoritative delegation により、全ユーザーが root になる必要があるから。]{#dns-setup-all-root explanation="DNS の委任は OS の権限を付与しません。"}
::option[open recursion が増幅攻撃やリソース消費に悪用されるから。]{#dns-setup-recursion-abuse .correct explanation="アクセス制御によって、resolver が公開攻撃基盤として使われる危険を減らせます。"}
:::

## 設定と Zone Data を検証する

reload 前に、実装固有の構文検査・zone 検査ツールを使います。BIND での一般的な例は次のとおりです。

```bash
$ named-checkconf
$ named-checkzone example.com /etc/bind/zones/db.example.com
```

ホストに適した権限とパスで実行してください。parser が成功しても、委任、serial の伝播、DNSSEC chain、ファイアウォール越しの到達性、正しい回答は証明されないため、制御された問い合わせを続けて行います。

:::single-choice{#dns-setup-zone-validation-limit}
zone の構文検査に成功しても証明できないものはどれですか？

::option[委任とエンドツーエンドの authoritative answer が機能すること。]{#dns-setup-not-end-to-end .correct explanation="親側のデータ、サービスの有効化、ネットワークポリシー、実行時の読み込みは別々です。"}
::option[checker が zone text を解析できること。]{#dns-setup-parser-proves explanation="それが checker から直接得られる証拠です。"}
::option[ファイルにレコードの owner field があること。]{#dns-setup-record-owner explanation="有効なレコードを解析する際、構造的な要素はすでに検査されます。"}
:::

## 安全に適用してテストする

現在の設定と復旧アクセスを保持して検証し、対応していれば restart ではなく reload します。各 authoritative server へ recursion を無効にして直接問い合わせ、SOA serial、NS 集合、正のレコード、存在しない名前、UDP と TCP の両方を比較します。

```bash
$ dig @192.0.2.53 example.com SOA +norecurse
$ dig @192.0.2.53 missing.example.com A +norecurse
$ dig @192.0.2.53 example.com SOA +norecurse +tcp
```

recursion については、許可済み・拒否対象のクライアントネットワーク、DNSSEC validation、cache behavior、上流依存先の障害をテストします。

:::single-choice{#dns-setup-norecurse-test}
authoritative server へ `+norecurse` で問い合わせるのはなぜですか？

::option[recursion を要求せず、authoritative answer をテストするため。]{#dns-setup-authority-only .correct explanation="zone service と recursive behavior を分離して確認できます。"}
::option[zone からすべてのレコードを削除するため。]{#dns-setup-remove-records explanation="問い合わせは authoritative data を編集しません。"}
::option[すべての応答を HTTP 経由にするため。]{#dns-setup-force-http explanation="このオプションが制御するのは DNS の recursion-desired flag です。"}
:::

## サービスを運用する

問い合わせ失敗、遅延、キャッシュ動作、リソース使用量、zone transfer、serial の整合性、DNSSEC の期限、委任の健全性を監視します。元設定と署名用データを安全にバックアップしますが、新しいインスタンスが zone を読み込み、正しく応答できることも検証してください。対応中のバージョンへ patch を適用し、制御インターフェース、dynamic update、transfer access を制限します。

:::single-choice{#dns-setup-redundancy-verification}
authoritative DNS の冗長性テストには何を含めるべきですか？

::option[各サーバーへの問い合わせと、別サーバー停止時の動作テスト。]{#dns-setup-test-each-server .correct explanation="複数の NS レコードがあるだけでは、各独立サービスが到達可能で最新だとは証明できません。"}
::option[全サーバーのホスト名が似ていることの確認だけ。]{#dns-setup-hostname-similarity explanation="名前からデータ同期や可用性は証明できません。"}
::option[広告する全サーバーで一つのプロセスとディスクを共有すること。]{#dns-setup-shared-failure explanation="障害領域を共有すると冗長性が弱まります。"}
:::

## まとめ

これで、明確な権威または再帰の役割を中心に DNS 配備を設計できます。

1. 必要な役割を定義してからソフトウェアを選ぶ。
2. recursion と管理インターフェースを制限する。
3. reload 前に設定と zone を検証する。
4. 権威、否定応答、トランスポート、クライアントポリシーを直接テストする。
5. 冗長性、DNSSEC、データ整合性、復旧を監視する。
