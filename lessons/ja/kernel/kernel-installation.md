---
lesson_id: "kernel-installation"
course_id: "kernel"
lang: "ja"
order_index: 4
title: "カーネルのインストール"
description: "検証済み fallback を残し、distribution kernel をインストール、boot、検証、保持する方法を学びます。"
meta_title: "カーネルのインストール - カーネル"
meta_description: "Linux カーネルのインストールと管理方法を学びましょう。`uname -r`コマンドと apt コマンドを使用して、カーネルバージョンを発見しましょう。Linux カーネルの旅を始めましょう！"
meta_keywords: "Linux kernel, install kernel, uname -r, apt dist-upgrade, kernel management, Linux tutorial, beginner Linux, Linux guide"
---

ディストリビューションは、カーネルを module、initramfs integration、boot-loader update、signature、support policy とまとめて package 化します。custom kernel を意図して開発・テストし、マシンを復旧できる場合を除き、その管理された workflow を使ってください。

## 実行中カーネルとインストール済みカーネル

現在動作中カーネルの release を表示します。

```bash
$ uname -r
6.8.0-00-generic
```

これはインストール済み全カーネルを一覧表示せず、新しい package をインストールした直後にも変わりません。`uname -r` が新しい version を報告するには、その image を boot する必要があります。インストール済み package と boot entry はディストリビューション固有のツールで問い合わせてください。

:::single-choice{#kernel-installation-uname-release} `uname -r` は何を表示しますか？

::option[現在動作中カーネルの release string。]{#kernel-installation-running-release .correct explanation="disk 上の最新 image だけではなく、live kernel state を報告します。"}
::option[全 repository にあるすべての kernel package。]{#kernel-installation-all-packages explanation="repository inventory は package manager が扱います。"}
::option[接続済み全 device の firmware version。]{#kernel-installation-device-firmware explanation="kernel release と device firmware inventory は別のデータです。"}
:::

## Distribution の Tracking Package を優先する

将来の security update を受け続けられるよう、ディストリビューションが対応する kernel tracking package または meta-package をインストール・保持します。package 名は release、architecture、hardware class、kernel flavor に依存します。Ubuntu では通常 `linux-generic` がありますが、cloud、low-latency、HWE、OEM、real-time、architecture 固有の system は別 package を使います。

`uname -r` の version string をそのまま `apt install` operand にして、有効だと想定しないでください。インストール前に現在のディストリビューション文書を参照し、package manager で候補を調べます。

:::single-choice{#kernel-installation-meta-package} 対応済み kernel meta-package が役立つのはなぜですか？

::option[再起動が一切不要だと保証するから。]{#kernel-installation-no-reboot explanation="特殊な live-patching の範囲を除き、新しいカーネルはその image を boot して初めて有効になります。"}
::option[すべての out-of-tree driver を built-in code へ変換するから。]{#kernel-installation-convert-drivers explanation="external module には引き続き互換 build と signing が必要です。"}
::option[ディストリビューションが意図する kernel update の系列を追跡するから。]{#kernel-installation-update-tracking .correct explanation="update の公開に応じ、dependency が system を新しい対応済み image・module package へ移します。"}
:::

## 変更前に確認する

kernel transaction の前に次を行います。

1. 対応 repository、package signature、release lifecycle、意図する kernel flavor を確認する。
2. `/boot` または EFI System Partition の空き容量を確認する。
3. 少なくとも一つの既知の正常な kernel と、選択可能な boot entry を残す。
4. console、remote management、rescue media、encryption recovery、rollback access を確認する。
5. out-of-tree module、storage/network driver、Secure Boot signing、hibernation、virtualization compatibility を確認する。

package transaction は、対応する initramfs を生成し、ディストリビューションの hook で boot entry を更新する必要があります。すべての error を確認してください。initramfs または loader の生成に失敗したなら、package が installed と表示されても十分ではありません。

:::single-choice{#kernel-installation-initramfs-error} initramfs 生成 error があると、成功したと判断してはいけないのはなぜですか？

::option[initramfs 生成がユーザーの shell password を変更するから。]{#kernel-installation-initramfs-password explanation="boot archive の workflow は account authentication secret と無関係です。"}
::option[新カーネルに root storage へ到達する初期 module や tool が不足する可能性があるから。]{#kernel-installation-missing-early-tools .correct explanation="image が installed でも、必要な early user-space artifact がない、または古い場合があります。"}
::option[現在動作中カーネルがすでに停止したことを証明するから。]{#kernel-installation-current-stopped explanation="package hook の実行中も、古いカーネルは動作し続けられます。"}
:::

## Boot して検証する

stakeholder と active workload を考慮し、管理された reboot を予定します。default が失敗した場合に、console から古い entry を選べるようにします。boot 後に確認します。

```bash
$ uname -r
$ journalctl -k -b
$ systemctl --failed
```

非 systemd system では同等のツールを使います。storage、filesystem、networking、graphics、input、security module、external module、container、virtual machine、application health を検証します。login prompt だけでは完全な検証になりません。

:::single-choice{#kernel-installation-activation} 通常の新しい kernel package が動作中カーネルになるのはいつですか？

::option[`uname -r` を入力した直後。]{#kernel-installation-uname-activates explanation="uname は読み取り専用で、カーネルを切り替えません。"}
::option[その kernel image をマシンが boot した後。]{#kernel-installation-after-boot .correct explanation="file のインストールだけでは、memory 内ですでに実行中のカーネルを置き換えません。"}
::option[package archive を download し、install する前。]{#kernel-installation-download-activates explanation="download 済み archive は live execution へ影響しません。"}
:::

## 古いカーネルを削除する

新カーネルの検証合格後に限り、package manager が対応する cleanup workflow を使います。現在動作中カーネル、唯一の既知の正常な fallback、active tracking package が必要とする package は削除しないでください。正確な削除候補と、その後の boot entry を確認します。

`/boot` から手動削除すると、package と loader の state が不整合になります。すでに容量が尽きている場合も、任意の image を消さず、ファイル変更前に復旧計画を作ってください。

:::single-choice{#kernel-installation-old-kernel-removal} 新カーネルの初期検証中に残すべき kernel はどれですか？

::option[未テストの新カーネルだけ。]{#kernel-installation-only-new explanation="テスト前に全 fallback を削除すると、互換性問題が復旧 incident になります。"}
::option[boot path 下には kernel file を一つも残さない。]{#kernel-installation-no-kernels explanation="Linux を boot するには、読み込み可能な kernel artifact が必要です。"}
::option[boot loader から選択できる既知の正常な fallback。]{#kernel-installation-known-good-fallback .correct explanation="新カーネルが hardware または workload で失敗したとき、fallback が復旧経路になります。"}
:::

[GRUB2 ブートメニューのカスタマイズ](https://labex.io/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)ラボは、複数 entry を理解するための復旧可能な環境を提供します。

## まとめ

これで、kernel update を boot chain と互換性の変更として扱えます。

1. 動作中 release とインストール済み image を区別する。
2. 正しい distribution package で対応済み update を追跡する。
3. storage、initramfs、signature、module、recovery access を事前確認する。
4. boot して hardware と application の動作を検証する。
5. 新カーネルが実証されるまで、既知の正常な fallback を保持する。
