---
lesson_id: "listing-devices"
course_id: "devices"
lang: "ja"
order_index: 6
title: "lsusb、lspci、lsscsi"
description: "USB トポロジー、PCI 機能、SCSI 層のデバイス、それらの稼働中ドライバーを調べる方法を学びます。"
meta_title: "lsusb、lspci、lsscsi - デバイス情報"
meta_description: "Linux システムで USB、PCI、SCSI ハードウェアを一覧表示および検査する方法を発見します。このガイドでは、デバイスツリー表示のための lsusb -t などのオプションを含め、lsusb、lspci、lsscsi コマンドを解説します。"
meta_keywords: "lsusb, lspci, lsscsi, lsusb -t, USB デバイス一覧，PCI デバイス一覧，SCSI デバイス一覧，Linux ハードウェア，デバイス情報"
---

Linux には、バスやサブシステムごとのインベントリーツールがあります。各コマンドが示すビューは異なるため、一つの完全なハードウェア一覧を期待せず、識別子、トポロジー、ドライバー、sysfs パス、ログを組み合わせて確認します。

## USB デバイスを調べる

`lsusb` は USB サブシステムから見えるデバイスを一覧表示します。

```bash
$ lsusb
```

通常、出力にはバス番号とデバイス番号、ベンダー ID と製品 ID の組、ローカル USB ID データベースから得た説明が含まれます。数値のバス／デバイスアドレスは再接続や再起動後に変わり得るため、永続的な識別情報として扱ってはいけません。

コントローラー、ハブ、ポート、インターフェース、ドライバー、速度の関係は次のコマンドで表示します。

```bash
$ lsusb -t
```

詳細なディスクリプター出力も利用できますが、一部の詳細には高い読み取り権限が必要です。調査コマンドの警告を消すためだけに、USB デバイスへ広範な権限を与えてはいけません。

:::single-choice{#listing-devices-usb-tree}
USB デバイスをトポロジーツリーとして表示するコマンドはどれですか？

::option[`lspci -k`]{#listing-devices-lspci-tree explanation="これは USB トポロジーではなく、PCI 機能とカーネルドライバー情報を一覧表示します。"}
::option[`lsscsi -t`]{#listing-devices-lsscsi-tree explanation="これはここで紹介した USB ツリー用コマンドではありません。"}
::option[`lsusb -t`]{#listing-devices-lsusb-tree .correct explanation="ツリーオプションは、コントローラーとハブの下にあるデバイスを、ポートやインターフェースの関係とともに表示します。"}
:::

## PCI 機能を調べる

`lspci` は PCI および PCI Express バス上で検出された機能を一覧表示します。

```bash
$ lspci
```

内蔵または外部接続された PCIe デバイスには、グラフィックス、ネットワーク、ストレージ、USB、オーディオ、ブリッジの各コントローラーなどがあります。使用中のカーネルドライバーと候補モジュールは次のように表示します。

```bash
$ lspci -k
```

PCI コントローラーが一覧に現れても、その配下のすべてのデバイスが初期化済みで正常とは限りません。トラブルシューティングでは、ドライバーのバインドとカーネルログを確認します。

:::single-choice{#listing-devices-pci-driver}
PCI の一覧にカーネルドライバー情報を追加するコマンドはどれですか？

::option[`lspci -k`]{#listing-devices-lspci-k .correct explanation="`-k` オプションは、各 PCI デバイスで稼働中のカーネルドライバーと、処理可能なモジュールを表示します。"}
::option[`lsusb -t`]{#listing-devices-usb-not-pci explanation="これは USB の階層とインターフェースドライバーを示します。"}
::option[`lsblk -f`]{#listing-devices-lsblk-filesystem explanation="これはブロックデバイスとファイルシステムの項目を報告し、PCI ドライバーのバインドは示しません。"}
:::

## SCSI 層のデバイスを調べる

`lsscsi` は Linux の SCSI 中間層を通じて表されるデバイスを一覧表示します。

```bash
$ lsscsi
```

ネイティブ SCSI デバイスに加え、SCSI 互換層を通じて提示される SATA、USB ストレージ、仮想ディスクが含まれることがあります。NVMe 名前空間は通常、別のサブシステムに属し、`lsscsi` だけでは包括的に一覧化されません。

多くの種類のブロックデバイスを含む、ストレージ指向の階層には `lsblk` も使います。

```bash
$ lsblk -o NAME,TYPE,SIZE,MODEL,SERIAL,TRAN,FSTYPE,MOUNTPOINTS
```

:::single-choice{#listing-devices-lsscsi-scope}
`lsscsi` が主に一覧表示するものは何ですか？

::option[すべての NVMe 名前空間とコントローラーだけ。]{#listing-devices-only-nvme explanation="NVMe には独自のサブシステムとツールがありますが、関連するブロックビューが別の場所に現れることはあります。"}
::option[名前が `.scsi` で終わるファイルだけ。]{#listing-devices-scsi-extension explanation="このコマンドはファイル名の拡張子ではなく、カーネルデバイスインターフェースを問い合わせます。"}
::option[Linux の SCSI 中間層を通じて表されるデバイス。]{#listing-devices-scsi-mid-layer .correct explanation="このコマンドは SCSI ホスト、ターゲット、論理ユニット、利用可能な場合は対応するデバイスノードを報告します。"}
:::

## インベントリー結果を解釈する

説明はローカル ID データベースに由来することが多く、一般的すぎたり古かったりする場合があります。一覧にあるデバイスに動作するドライバーがないこともあり、仮想化環境ではエミュレートまたは準仮想化されたハードウェアが提示されることもあります。調査する問題と権限に応じて、結果を `udevadm info`、sysfs、`lsblk`、ネットワークツール、`journalctl -k` または `dmesg` と照合してください。

これらのユーティリティーは別々にパッケージ化され、一般には `usbutils`、`pciutils`、`lsscsi` などのパッケージで提供されます。コマンドがない場合は、出所不明の代替物をダウンロードせず、ディストリビューションのパッケージマネージャーを使ってください。

:::single-choice{#listing-devices-listed-not-working}
`lspci` にデバイスが表示されれば、ドライバーが有効で正常に動作していると証明できますか？

::option[いいえ。ドライバーのバインドと関連するカーネルメッセージも確認する。]{#listing-devices-needs-correlation .correct explanation="列挙によって分かるのは PCI 機能が見えていることだけで、上位層の初期化成功までは分かりません。"}
::option[はい。PCI の列挙では完全な機能テストを実行する。]{#listing-devices-complete-test explanation="一覧表示は、すべてのハードウェア機能を動作させたり、サービスの挙動を検証したりしません。"}
::option[はい。`lspci` が適切なドライバーを自動的にインストールする。]{#listing-devices-installs-driver explanation="このコマンドはインベントリーツールであり、ドライバーパッケージをインストールしません。"}
:::

[Linux でハードウェアデバイスを調査する](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)を利用して、一つの管理されたホスト上でこれらのサブシステムビューを比較してください。

## まとめ

対象デバイスのサブシステムに応じて、インベントリーコマンドを選べるようになりました。

1. USB の識別情報とトポロジーには `lsusb` と `lsusb -t` を使う。
2. PCI 機能とドライバーのバインドには `lspci -k` を使う。
3. SCSI 層のデバイスには `lsscsi`、ブロックトポロジーには `lsblk` を使う。
4. 列挙結果をドライバー、sysfs、カーネルメッセージと照合する。
