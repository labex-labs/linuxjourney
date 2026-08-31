---
lesson_id: "dhclient"
course_id: "network-config"
lang: "ja"
order_index: 3
title: "dhclient"
description: "システムのネットワークマネージャーと競合させずに、dhclient を使う場面と方法を学びます。"
meta_title: "dhclient - ネットワーク構成"
meta_description: "dhclient、DHCP を使用して IP アドレスを取得する方法、ネットワークリースを管理する方法について学びます。dhclient.conf および dhclient.leases ファイルを理解します。Linux 初心者ガイド。"
meta_keywords: "dhclient, DHCP, Linux ネットワーキング，IP アドレス，ネットワーク構成，Linux チュートリアル，初心者ガイド"
---

`dhclient` は、一部の Linux システムにある ISC DHCP クライアントです。現在の多くの環境では、代わりに NetworkManager、systemd-networkd などのサービスが自身の DHCP クライアントを動かします。管理済みインターフェースで二つ目のクライアントを起動すると、アドレス、ルート、DNS 設定、リース状態が競合する可能性があります。

## 稼働中のクライアントを特定する

`dhclient` を実行する前に、設定の管理主体とプロセスを調べます。

```bash
$ nmcli device status
$ networkctl status
$ ps -ef | grep '[d]hclient'
```

ホストに存在するツールを使ってください。マネージャーがインターフェースを管理しているなら、別のクライアントを起動せず、そのマネージャーを通じて DHCP を要求します。

:::single-choice{#dhclient-second-client-risk}
すでに管理されているインターフェースで `dhclient` を起動すべきでないのはなぜですか？

::option[DHCP はループバックアドレスしか割り当てられないから。]{#dhclient-loopback-only explanation="DHCP は一般に、ループバックではないネットワーク設定を割り当てます。"}
::option[二つのクライアントがアドレス、ルート、DNS、リースを巡って競合するから。]{#dhclient-competing-state .correct explanation="通常、特定した一つの設定管理主体だけがインターフェースを整合させるべきです。"}
::option[DHCP 要求を送るたびにローカルディスクが再フォーマットされるから。]{#dhclient-reformats explanation="このプロトコルが変更するのはネットワーク状態であり、ディスク形式ではありません。"}
:::

## リースを明示的に要求する

`dhclient` が管理主体となる未管理のテスト用インターフェースでは、対象を指定し、詳細出力を有効にします。

```bash
$ sudo dhclient -v enp1s0
```

インターフェースを指定せずに実行すると、複数の対象インターフェースへ作用する場合があります。設定とリースのパスはパッケージや呼び出し方によって異なります。一般的な名前には `dhclient.conf` と `dhclient.leases` がありますが、一つの固定場所を想定しないでください。

:::single-choice{#dhclient-interface-operand}
手動要求で `enp1s0` を指定するのはなぜですか？

::option[目的のネットワークインターフェースだけを対象にするため。]{#dhclient-scope-interface .correct explanation="対象を指定しないクライアント実行は、意図した以上のインターフェースを検討する場合があります。"}
::option[DHCP に TCP ポート 1 を選ぶため。]{#dhclient-tcp-port explanation="DHCP は UDP を使い、インターフェース名はポートではありません。"}
::option[リースを永続化するため。]{#dhclient-permanent explanation="DHCP 設定は、期限のあるリース状態のままです。"}
:::

## リースを解放する

`dhclient -r INTERFACE` はリースの解放を要求し、利用中の設定を取り除く場合があります。これは通信を中断する操作であり、サーバーが解放通知を受け取れるとも限りません。リースを確認するだけの目的で、特にリモート管理経路上のリースを解放してはいけません。

:::single-choice{#dhclient-release-effect}
`dhclient -r enp1s0` には、どのような運用上の危険がありますか？

::option[変更せず現在のリースを表示するだけ。]{#dhclient-release-readonly explanation="リースの解放は状態を変更する操作です。"}
::option[すべてのリースを無期限に更新する。]{#dhclient-release-renews explanation="解放と更新は反対の操作です。"}
::option[現在の DHCP 接続を失う可能性がある。]{#dhclient-release-connectivity .correct explanation="解放処理はリース状態を手放すため、リモートアクセスが切断される場合があります。"}
:::

## 適用されたリースを検証する

制御された要求を行ったら、アドレス以外も検証します。

```bash
$ ip address show dev enp1s0
$ ip route show
$ resolvectl status
```

マネージャーまたはクライアントのログとリース期間を確認し、目的の名前解決とアプリケーションをテストします。DHCPACK に誤ったオプションが含まれる場合もあり、アドレスの割り当て成功だけではゲートウェイや DNS への到達性は証明できません。

:::single-choice{#dhclient-verify-state}
リース取得後に検証すべきものはどれですか？

::option[アドレス、ルート、DNS、リース、アプリケーションの動作。]{#dhclient-complete-verify .correct explanation="リースは相互に関連する複数の要素を設定するため、それらが連携して動く必要があります。"}
::option[アドレス文字列が表示されることだけ。]{#dhclient-address-only explanation="ルート、DNS、有効期間、エンドツーエンドの動作が誤っている可能性は残ります。"}
::option[デスクトップの背景だけ。]{#dhclient-wallpaper explanation="デスクトップの外観は DHCP 状態と無関係です。"}
:::

## まとめ

これで、`dhclient` がインターフェースの意図された管理主体である場合に限って利用できます。

1. 稼働中のネットワークマネージャーと DHCP クライアントを検出する。
2. 一つのインターフェースで複数クライアントを競合させない。
3. 手動要求を名前指定したテスト用インターフェースに限定する。
4. 解放を中断を伴う操作として扱い、リース結果全体を検証する。
