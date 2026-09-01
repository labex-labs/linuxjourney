---
lesson_id: "etc-hosts"
course_id: "dns"
lang: "ja"
order_index: 4
title: "/etc/hosts"
description: "ローカルの hosts ファイルが Linux の名前解決へ参加する仕組みと、安全なテスト方法を学びます。"
meta_title: "/etc/hosts - DNS"
meta_description: "Linux の/etc/hosts ファイルの目的を探ります。このファイルがホスト名を IP アドレスにマッピングする方法、ローカル DNS 解決における役割、Debian などのシステムでの設定方法を学びます。etc hosts linux 設定ガイド。"
meta_keywords: "/etc/hosts, etc hosts linux, debian hosts, etc host linux, etc hosts, Linux ネットワーキング，ホスト名マッピング，DNS 解決"
---

`/etc/hosts` は、ローカルシステムの名前サービススタックへ静的なアドレスと名前の対応を提供します。ループバック名、起動時の依存関係、範囲を絞ったテストに便利ですが、ほかのホストへレコードを公開したり、DNS を更新したりはしません。

## ファイルを読む

各行は IPv4 または IPv6 アドレスで始まり、その後に一つ以上の名前が続きます。

```text
127.0.0.1       localhost
192.0.2.25      app-test.example.net app-test
2001:db8::25    app-test-v6.example.net app-test-v6
```

コメントは `#` で始まります。一部のツールは慣例上、最初の名前を canonical、後の名前を alias として扱いますが、アプリケーションと resolver API によって動作は異なります。同じ名前に対する重複または競合エントリは避けてください。

:::single-choice{#hosts-file-entry-order} 通常の `/etc/hosts` の対応付け行では、最初に何を書きますか？

::option[IP アドレス。]{#hosts-file-address-first .correct explanation="同じ行で、そのアドレスの後に一つ以上の名前を続けます。"}
::option[DNS レコードの TTL。]{#hosts-file-ttl-first explanation="hosts ファイルのエントリは DNS TTL フィールドを使いません。"}
::option[トランスポートのポート番号。]{#hosts-file-port-first explanation="このファイルが対応付けるのは名前とアドレスであり、アプリケーションポートではありません。"}
:::

## Resolver の参照順

通常 `/etc/nsswitch.conf` にある Name Service Switch 設定は、システムの resolver 関数が `files`、DNS、multicast system などの情報源をどのように組み合わせるか決めます。よくある行は次のとおりです。

```text
hosts: files dns
```

ポリシーを調べず、常に files が先だと想定しないでください。アプリケーションが独自の DNS library、cache、proxy、encrypted resolver を使い、システムの経路に従わない場合もあります。

:::single-choice{#hosts-file-nss-order} システム resolver が DNS より先に `/etc/hosts` を参照するかどうかは、何で決まりますか？

::option[`/etc` 内のファイル名のアルファベット順。]{#hosts-file-alphabetical explanation="ファイルシステムの一覧順は、名前サービスのポリシーを定義しません。"}
::option[Name Service Switch ポリシー内の情報源の順序。]{#hosts-file-nss-policy .correct explanation="`hosts:` データベース行が、通常の libc resolver の情報源順を制御します。"}
::option[宛先の TCP window size。]{#hosts-file-tcp-window explanation="トランスポートのフロー制御は、ローカルの名前検索と無関係です。"}
:::

## システム Resolver 経由でテストする

`getent` を使って、設定されたシステムの名前サービス経路を動かします。

```bash
$ getent ahosts app-test.example.net
```

`dig` は DNS へ直接問い合わせるため、通常 `/etc/hosts` の対応を報告しません。この違いは有用です。`getent` は成功し `dig` は成功しない場合、ローカル情報源や resolver ポリシーの違いが考えられます。

:::single-choice{#hosts-file-getent-versus-dig} 通常のシステム名前解決が hosts ファイルのエントリを認識するか調べるのに適したツールはどれですか？

::option[`dig`。常に最初に `/etc/hosts` を読むから。]{#hosts-file-dig-first explanation="dig は DNS 問い合わせを送り、hosts ファイルの検索経路を通りません。"}
::option[`getent ahosts`。設定済みの名前サービス情報源を使うから。]{#hosts-file-getent .correct explanation="多くのネイティブアプリケーションが使う resolver 経路を反映します。"}
::option[`ip route flush`。すべての名前を再構築するから。]{#hosts-file-flush-route explanation="ルート消去は破壊的であり、hosts ファイルの検索とは無関係です。"}
:::

## 安全に編集する

必要な localhost とホスト identity のエントリを維持し、意図するアドレスを確認して、復旧可能な特権 editor の手順で変更します。軽いテストのために実在する公開ドメインを上書きしてはいけません。認証情報やアプリケーション通信を予期せず別経路へ向ける可能性があります。専用のテスト名を使い、実験後にエントリを削除してください。

編集後は、アプリケーションがキャッシュを保持したり別の resolver を使ったりする可能性があるため、正確なアプリケーションをテストします。永続的な上書きは文書化し、目的を終えた後まで黙って残らないようにしてください。

:::single-choice{#hosts-file-test-name} 公開サービス名を上書きせず、専用のテスト名を使うのはなぜですか？

::option[公開名にはドットを含められないから。]{#hosts-file-public-no-dots explanation="ドメイン名は通常、ドットで区切られた複数ラベルを含みます。"}
::option[専用名によって authoritative DNS zone が自動作成されるから。]{#hosts-file-auto-zone explanation="hosts ファイルのエントリはローカルに留まり、zone を公開しません。"}
::option[実際の通信や認証情報を別経路へ向ける危険を減らせるから。]{#hosts-file-reduce-redirection .correct explanation="ローカル上書きは、その公開名を使うすべてのシステム resolver クライアントへ影響する可能性があります。"}
:::

## Resolver Server の設定

`/etc/resolv.conf` は従来 DNS resolver 設定を列挙しますが、NetworkManager、systemd-resolved、DHCP などのマネージャーによって生成されることがよくあります。symlink とファイルコメントを調べ、上書きされる生成出力ではなく、管理している設定元を変更してください。

:::single-choice{#hosts-file-resolv-owner} `/etc/resolv.conf` を編集する前に何をすべきですか？

::option[`/etc/hosts` と全ネットワークルートを削除する。]{#hosts-file-delete-state explanation="そのような破壊的変更は無関係であり、接続性を失う可能性があります。"}
::option[すべてのディストリビューションが永続設定を直接そこへ保存すると想定する。]{#hosts-file-assume-direct explanation="多くのシステムでは動的に生成されるか、管理済み stub への link になっています。"}
::option[別のサービスが生成・管理しているか特定する。]{#hosts-file-identify-resolver-owner .correct explanation="永続的な DNS server の変更は、稼働中マネージャーの設定へ行います。"}
:::

## まとめ

これで、`/etc/hosts` を管理されたローカル resolver 入力として利用できます。

1. アドレスを先に書き、意図した名前と alias を続ける。
2. Name Service Switch の順序を想定せず確認する。
3. `getent` でシステム解決を、`dig` で DNS を別々にテストする。
4. 専用の一時名を使い、実際のアプリケーションを検証する。
5. 設定管理主体を通じて resolver server を変更する。
