---
lesson_id: "network-interfaces"
course_id: "network-config"
lang: "ja"
order_index: 1
title: "ネットワークインターフェース"
description: "Linux インターフェースの状態、アドレス、統計、永続設定の管理主体を調べる方法を学びます。"
meta_title: "ネットワークインターフェース - ネットワーク設定"
meta_description: "Linux ネットワークインターフェースの包括的なガイド。ifconfig と最新の ip コマンドの使い方、および特に Debian システムにおける/etc/network/interfaces などの設定ファイルについて学びます。"
meta_keywords: "linux インターフェース，linux ネットワークインターフェース，etc network interfaces, debian ネットワークインターフェース，ifconfig, ip コマンド，ネットワーク設定，linux ネットワーキング"
---

Linux のネットワークインターフェースは、ネットワーク名前空間を物理デバイス、ループバック経路、ブリッジ、トンネル、仮想デバイスなどのリンクへ接続します。インターフェース状態、アドレス、ルート、DNS、永続設定は互いに関係しますが、別々のものです。

## インターフェースを見つける

現代的な iproute2 ツールを使います。

```bash
$ ip -brief link show
$ ip -brief address show
```

インターフェース名には、`enp1s0` のようなハードウェア由来の予測可能な名前、`eth0` のような従来名、管理者が定義した名前があります。`eth0` が必ず存在する、または特定のアダプターを示すとは決めつけないでください。

:::single-choice{#interfaces-name-assumption}
スクリプトで `eth0` を決め打ちせず、検出すべきなのはなぜですか？

::option[すべてのインターフェースは `lo` という名前でなければならないから。]{#interfaces-all-loopback explanation="ループバックは特殊なインターフェースの一つであり、全リンクの名前ではありません。"}
::option[Linux システムでは複数の命名方式が使われるから。]{#interfaces-naming-varies .correct explanation="ハードウェア由来名、仮想デバイス名、カスタム名があるため、固定した `eth0` という想定は信頼できません。"}
::option[インターフェース名は常にリモート接続用パスワードだから。]{#interfaces-name-password explanation="名前はカーネルデバイスを識別するもので、認証情報ではありません。"}
:::

## 管理状態と動作状態

`UP` は、インターフェースが管理上有効であることを意味します。`LOWER_UP` は一般に、Ethernet のキャリアなど、下位層が動作可能と報告していることを示します。どちらか一方だけでは、IP アドレス、ルート、DNS、ファイアウォール、アプリケーション経路が機能するとは証明できません。

```bash
$ ip -details link show dev enp1s0
$ ip -s link show dev enp1s0
```

統計表示からエラー、破棄、カウンターを確認できますが、値を意味のあるものにするには観測期間と基準値が必要です。

:::single-choice{#interfaces-up-limit}
管理状態が `UP` でも証明できないことはどれですか？

::option[エンドツーエンドの接続が機能すること。]{#interfaces-up-not-connectivity .correct explanation="下位層、アドレス、ルーティング、フィルタリング、名前解決、サービスの障害は残り得ます。"}
::option[管理者がインターフェースを有効にしたこと。]{#interfaces-up-does-prove explanation="それがこの状態の直接的な意味です。"}
::option[インターフェースのカーネルオブジェクトが存在すること。]{#interfaces-up-kernel-object explanation="表示された状態は、既存のカーネルインターフェースに属します。"}
:::

## 実行時の状態を変更する

実行時の操作には、次のようなコマンドがあります。

```bash
$ sudo ip link set dev enp1s0 up
$ sudo ip address add 192.0.2.10/24 dev enp1s0
```

これらは現在のカーネル状態を変更するため、後でプロファイルを再適用するネットワークマネージャーと競合する場合があります。リモート管理に使うインターフェースを停止すると、即座にアクセスを失う可能性があります。変更前に対象デバイスを確認し、コンソールアクセスを確保し、現在の状態を記録して、時間指定または検証済みのロールバックを用意してください。

:::single-choice{#interfaces-ip-address-add-persistence}
`ip address add` だけで、再起動後も設定が残ると保証できますか？

::option[いいえ。稼働中の設定システムにもその設定を保存する必要があります。]{#interfaces-manager-persistence .correct explanation="NetworkManager、systemd-networkd、ifupdown など、管理主体が永続ポリシーを適用します。"}
::option[はい。カーネルの変更は常に全管理プロファイルを編集するからです。]{#interfaces-runtime-always-persistent explanation="カーネルの実行時変更が、永続設定を一律に更新するわけではありません。"}
::option[プライベート IPv4 アドレスの場合だけ残ります。]{#interfaces-private-persistent explanation="アドレスのスコープによって、実行時コマンドが永続化されることはありません。"}
:::

## 設定の管理主体を特定する

永続設定の場所は、ディストリビューションやインストールごとに異なります。NetworkManager のプロファイル、systemd-networkd の unit、netplan の入力、`/etc/network/interfaces`、cloud-init、オーケストレーションなどが候補です。ファイルを編集する前に、どのサービスがデバイスを管理しているか確認します。

```bash
$ systemctl --type=service --state=running | grep -E 'NetworkManager|networkd|networking'
$ networkctl status
$ nmcli device status
```

特定した管理システムに存在するコマンドだけを使ってください。二つのマネージャーが同じリンクを制御すると競合し、互いの状態を上書きする場合があります。

:::single-choice{#interfaces-config-owner}
インターフェースの永続設定を変更する前に、何をすべきですか？

::option[考えられるすべてのネットワーク設定ファイルを編集する。]{#interfaces-edit-all explanation="競合する定義を作ると、再適用時の動作が予測できなくなります。"}
::option[どのネットワークマネージャーがインターフェースを管理しているか特定する。]{#interfaces-identify-owner .correct explanation="正しい設定元と適用方法は、その管理主体によって決まります。"}
::option[確認前に現在の全ルートを削除する。]{#interfaces-delete-routes explanation="破壊的な操作であり、復旧用のアクセス経路まで失う可能性があります。"}
:::

## 変更を検証する

リンク状態、割り当てアドレスと有効期間、選択されるルート、リゾルバー状態、近隣への到達性、実際のアプリケーションを確認します。永続変更の場合、復旧経路があるときに限り、制御されたサービス再起動または再起動でテストしてください。

:::single-choice{#interfaces-change-verification}
`ip address` に新しいアドレスが表示されることより、強い証拠になるのはどれですか？

::option[インターフェース名に数字が含まれていること。]{#interfaces-digit explanation="命名規則は、エンドツーエンドの検証にはなりません。"}
::option[シェルプロンプトの色が変わっていないこと。]{#interfaces-prompt-color explanation="端末の外観はネットワーク動作と無関係です。"}
::option[ルート、リゾルバー状態、目的のアプリケーションも機能すること。]{#interfaces-end-to-end .correct explanation="利用可能な設定には、経路全体とサービスの動作が必要です。"}
:::

## まとめ

これで、実行時の状態と永続ポリシーを混同せず、インターフェースを調査・変更できます。

1. 実際のインターフェース名とアドレスを検出する。
2. 管理状態と運用上の接続性を区別する。
3. 直接の `ip` 変更を現在のカーネル状態として扱う。
4. 永続設定の変更前に、稼働中の設定管理主体を特定する。
5. 変更後にルーティング、名前解決、アプリケーション動作を検証する。
