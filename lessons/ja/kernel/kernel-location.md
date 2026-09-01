---
lesson_id: "kernel-location"
course_id: "kernel"
lang: "ja"
order_index: 5
title: "カーネルの場所"
description: "ディストリビューションが kernel image、initramfs、設定、symbol、version 別 module を配置する場所を学びます。"
meta_title: "カーネルの場所 - カーネル"
meta_description: "Linux でカーネルがどこに保存されているかを発見してください。このガイドでは、vmlinuz や initrd などの主要なファイルを詳述しながら、/boot ディレクトリ内の Linux カーネルの場所について説明します。"
meta_keywords: "linux カーネルの場所，カーネルはどこ，カーネルの場所，カーネルはどこにありますか，linux でカーネルはどこに保存されていますか，vmlinuz, /boot ディレクトリ"
---

Linux ディストリビューションは通常、boot 可能な kernel artifact を `/boot` 以下へ保存します。ただし UEFI と Boot Loader Specification の layout では、`/boot`、`/boot/efi`、`/efi` などに mount された EFI System Partition または extended boot partition へ artifact を置く場合もあります。普遍的なパスを想定せず、mount と loader 設定を調べてください。

## `/boot` 以下の Version 付きファイル

従来のディストリビューション layout には、次のものがあります。

- `vmlinuz-KERNEL_RELEASE`：boot 可能な Linux kernel image
- `initrd.img-KERNEL_RELEASE` または `initramfs-KERNEL_RELEASE.img`：early user-space image
- `config-KERNEL_RELEASE`：package 化された kernel build に使った設定
- `System.map-KERNEL_RELEASE`：kernel build の symbol-address map

名前は環境によって異なります。現代のディストリビューションで `initrd` と名付けられた file も、initramfs archive を含む場合があります。`vmlinuz` という命名規則だけでは、内部 compression や platform boot format は分かりません。ディストリビューションのツールで調べてください。

:::single-choice{#kernel-location-vmlinuz} version 付き `vmlinuz-*` ファイルには通常何が含まれますか？

::option[boot 可能な Linux kernel image。]{#kernel-location-kernel-image .correct explanation="boot loader または firmware が、この architecture 固有 kernel artifact を読み込みます。"}
::option[インストール済み全カーネルのすべての loadable module。]{#kernel-location-all-modules explanation="module は release 固有の module tree へ別に保存されます。"}
::option[前回 boot のユーザー shell history。]{#kernel-location-shell-history explanation="boot kernel image に個人の command history は含まれません。"}
:::

## Initial RAM Filesystem と Build Metadata

initramfs には、対応するカーネルと root-storage design に必要な early module と tool が含まれていなければなりません。ファイル名が一致するだけでは不十分です。生成が古い、または失敗していると、boot entry は使えません。

`config-*` は、どの機能が built-in、modular、または省略されたかを理解する助けになります。`System.map-*` は symbolization と debugging に役立ちますが、address randomization、split debug information、distribution tooling によって使い方が変わります。これらは補助 artifact であり、代替 kernel ではありません。

:::single-choice{#kernel-location-initramfs-match} initramfs が特定の kernel release と system configuration に結び付くのはなぜですか？

::option[全 mounted filesystem の恒久的な内容を保存するから。]{#kernel-location-all-filesystems explanation="initramfs は小さな early boot environment であり、完全な system backup ではありません。"}
::option[boot のたびにユーザーへ新しい UID を割り当てるから。]{#kernel-location-user-ids explanation="account identity management は通常の役割ではありません。"}
::option[その boot path に必要な early module と tool を含むから。]{#kernel-location-early-modules .correct explanation="module ABI と必要な storage assembly component が、選択 kernel と一致する必要があります。"}
:::

## Version 別 Kernel Module

動作中 release の loadable module は通常、次の場所にあります。

```bash
$ printf '/lib/modules/%s\n' "$(uname -r)"
```

merged filesystem layout では、`/usr/lib/modules/KERNEL_RELEASE` へ解決される場合があります。インストール済みの各 kernel には、互換 module tree と dependency index が必要です。`modprobe` は release 固有 metadata を使い、disk 全体の任意の `.ko` file を検索するわけではありません。

:::single-choice{#kernel-location-module-tree} 動作中 kernel release の module を慣例的に格納する directory はどれですか？

::option[`/home/modules/current/`]{#kernel-location-home-modules explanation="ユーザーの home directory は標準的な system module tree ではありません。"}
::option[`/lib/modules/$(uname -r)/`]{#kernel-location-lib-modules .correct explanation="release component が、インストール済み kernel ごとの module ABI と dependency data を分離します。"}
::option[`/proc/modules/files/`]{#kernel-location-proc-files explanation="`/proc/modules` は loaded module を報告するもので、module binary の directory ではありません。"}
:::

## Unified Kernel Image と Firmware Path

Unified Kernel Image（UKI）は、kernel、initrd、command line、metadata を一つにまとめられる署名済み EFI executable です。UKI は通常、別々の `vmlinuz` と initramfs file ではなく、EFI からアクセス可能な boot location に保存されます。

したがって、従来の `/boot` layout が空に見えても、kernel がインストールされていないとは限りません。`findmnt`、package database、boot-manager tool、loader 設定を使い、active artifact を対応付けます。

:::single-choice{#kernel-location-uki} Unified Kernel Image が一つにまとめられるものはどれですか？

::option[GPT header 内の全ユーザー home directory。]{#kernel-location-uki-homes explanation="UKI は boot executable であり、user-data container や partition table ではありません。"}
::option[インストール済み全 package を一つにした shell script。]{#kernel-location-uki-packages explanation="まとめるのは boot component であり、OS repository 全体ではありません。"}
::option[EFI executable 内の kernel、initrd、command line、metadata。]{#kernel-location-uki-components .correct explanation="統合 artifact は、署名済み UEFI boot workflow に参加できます。"}
:::

## 安全に容量を管理する

boot filesystem が満杯なら、まず mounted boot path を対応付け、各 artifact をどの package が所有するか問い合わせます。package manager の kernel cleanup workflow を使い、動作中 kernel と既知の正常な fallback を保持し、boot entry を再生成または確認して、その後の空き容量を検証します。

古いというだけで `vmlinuz`、initramfs、UKI、module tree を手動削除しないでください。現在動作中でなくても、唯一 boot 可能な recovery entry である場合があります。

## まとめ

これで、kernel package を boot artifact と module artifact へ対応付けられます。

1. 実際の `/boot` と EFI 関連 mount を調べる。
2. kernel image、initramfs、config、symbol map を区別する。
3. module tree を正確な kernel release と一致させる。
4. Unified Kernel Image とディストリビューション固有 layout を考慮する。
5. 検証済み package と fallback plan を通じてのみ boot 容量を回収する。
