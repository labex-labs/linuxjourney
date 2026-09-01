---
lesson_id: "network-manager"
course_id: "network-config"
lang: "ja"
order_index: 4
title: "ネットワークマネージャー"
description: "NetworkManager がデバイス、永続的な接続プロファイル、稼働中の状態を分けて扱う仕組みを学びます。"
meta_title: "ネットワークマネージャー - ネットワーク設定"
meta_description: "最新の Linux ネットワーク管理における NetworkManager デーモンの役割を発見してください。このツールがネットワーク構成を自動化する方法と、nm-tool および強力な nmcli コマンドラインユーティリティを使用して対話する方法を学びます。"
meta_keywords: "NetworkManager, nm-tool, nmcli, ネットワークマネージャー linux, networkmanager linux, linux ネットワークマネージャー, linux ネットワーク管理，ネットワーク構成，Linux ネットワーキング"
---

NetworkManager は、多くの Linux デスクトップやサーバーでネットワークデバイスを管理し、接続プロファイルを有効化します。ただし普遍的な仕組みではないため、`nmcli` で設定を変える前に、対象インターフェースを NetworkManager が管理していることを確認してください。

## デバイスと接続

デバイスは `enp1s0` や `wlan0` などのカーネルインターフェースです。接続は、IPv4、IPv6、DNS、Wi-Fi、ルーティングなどの設定を含む保存済みプロファイルです。一つのデバイスに複数のプロファイルを持てますが、通常はその時点で適用可能な一つだけが有効になります。

```bash
$ nmcli device status
$ nmcli connection show
$ nmcli connection show --active
```

:::single-choice{#networkmanager-device-profile} NetworkManager の接続プロファイルとは何ですか？

::option[ネットワークカードにはんだ付けされた物理コネクター。]{#networkmanager-physical-connector explanation="それはハードウェアであり、NetworkManager のプロファイルではありません。"}
::option[デバイス上で有効化できる、保存済みの設定一式。]{#networkmanager-stored-settings .correct explanation="プロファイルは、カーネルのインターフェースオブジェクトとは別に永続設定を保持します。"}
::option[すべての通信フローから取得したパケット。]{#networkmanager-packet-capture explanation="プロファイルは設定を記述するもので、全トラフィックを格納しません。"}
:::

## 有効な状態を調べる

有効なプロファイルとデバイスの詳細を表示します。

```bash
$ nmcli -f GENERAL,IP4,IP6 device show enp1s0
$ nmcli connection show 'Wired connection 1'
```

プロファイル設定、実行時の DHCP 結果、カーネル状態は異なる場合があります。`ip address`、`ip route`、リゾルバーとも比較してください。非推奨の `nm-tool` を現代的な作業手順の基盤にすべきではありません。

:::single-choice{#networkmanager-active-command} 有効な NetworkManager プロファイルを一覧表示するコマンドはどれですか？

::option[`nmcli device delete --all`]{#networkmanager-delete-all explanation="これは調査用コマンドではなく、破壊的な意図を示しています。"}
::option[`nmcli connection show --active`]{#networkmanager-show-active .correct explanation="保存済み接続を、現在有効化されているものだけに絞って表示します。"}
::option[`ip route flush table all`]{#networkmanager-flush-routes explanation="これはプロファイルを一覧表示せず、ルーティング状態を削除します。"}
:::

## プロファイルを変更して有効化する

名前を明示してプロファイルを変更し、保守時間内に有効化します。

```bash
$ sudo nmcli connection modify 'Wired connection 1' ipv4.method auto
$ sudo nmcli connection up 'Wired connection 1'
```

変更操作は永続的なプロファイルデータを書き換えます。有効化すると稼働中のアドレス、ルート、DNS が置き換わる可能性があります。リモート変更では、コンソールアクセス、保存した元設定、独立した時間指定のロールバックが必要です。変更対象の接続に、その接続自身の復旧コマンドを運ばせないでください。

:::single-choice{#networkmanager-modify-versus-up} `connection modify` と `connection up` の違いは何ですか？

::option[modify はホストを再起動し、up は DNS のソースコードを編集する。]{#networkmanager-reboot-source explanation="どちらもコマンドの説明として正しくありません。"}
::option[modify はプロファイル設定を変更し、up はプロファイルを有効化する。]{#networkmanager-change-activate .correct explanation="永続設定と実行時の有効化は、関連していますが別々の操作です。"}
::option[どちらも読み取り専用の別名で、接続性には影響しない。]{#networkmanager-readonly explanation="この手順では、どちらも状態を変更し得ます。"}
:::

## 検証と秘密情報の保護

有効化後は、プロファイル状態、カーネルのアドレスとルート、DNS、両方のアドレスファミリー、目的のアプリケーションを検証します。Wi-Fi、VPN、802.1X、モバイル用のプロファイルには秘密情報が含まれる場合があります。プロファイルの権限を制限し、共有ログやシェル記録に秘密フィールドを出力しないでください。

:::single-choice{#networkmanager-verification} NetworkManager が「接続済み」と報告する以上の証拠になるものはどれですか？

::option[プロファイル名に Wired という単語が含まれること。]{#networkmanager-name-proof explanation="ラベルから、経路やサービスの健全性は確認できません。"}
::option[端末ウィンドウが開いたままであること。]{#networkmanager-terminal-open explanation="部分的なネットワーク障害があっても、端末が残る場合があります。"}
::option[目的の DNS テストとアプリケーションテストが成功すること。]{#networkmanager-end-to-end .correct explanation="マネージャーの状態は、カーネルとサービスの動作と照合する必要があります。"}
:::

## まとめ

これで、NetworkManager のプロファイルとインターフェースオブジェクトを混同せずに管理できます。

1. NetworkManager が対象デバイスを管理していることを確認する。
2. 保存済みプロファイルと稼働中の状態を区別する。
3. デバイス、全プロファイル、有効なプロファイルを別々に調べる。
4. 変更、有効化、復旧、検証を別々の手順として行う。
