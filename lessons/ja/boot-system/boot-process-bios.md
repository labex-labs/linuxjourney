---
index: 2
lang: "ja"
title: "起動プロセス：BIOS"
meta_title: "起動プロセス：BIOS - システムを起動する"
meta_description: "Linux の起動プロセス、BIOS、MBR について学びましょう。この初心者向けのガイドで、システムの起動方法を理解しましょう。UEFI の概念も探求します！"
meta_keywords: "Linux 起動プロセス，BIOS, MBR, UEFI, Linux チュートリアル，ブートローダー, 初心者 Linux, システム起動"
---

## Lesson Content

### BIOS

Linux の起動プロセスにおける最初のステップは BIOS であり、システム整合性チェックを実行します。BIOS は、今日の主要なコンピュータである IBM PC 互換コンピュータで最も一般的なファームウェアです。おそらく、ハードドライブの起動順序を変更したり、システム時刻やマシンの MAC アドレスを確認したりするために BIOS ファームウェアを使用したことがあるでしょう。BIOS の主な目的は、システムブートローダーを見つけることです。

BIOS がハードドライブを起動すると、システムを起動する方法を把握するためにブートブロックを検索します。ディスクのパーティション分割方法に応じて、マスターブートレコード（MBR）または GPT を参照します。MBR はハードドライブの最初のセクター、最初の 512 バイトにあります。MBR には、ディスク上のどこかにある別のプログラムをロードするためのコードが含まれており、このプログラムが実際にブートローダーをロードします。

ディスクを GPT でパーティション分割した場合、ブートローダーの場所は少し変わります。

### UEFI

BIOS を使用する代わりにシステムを起動する別の方法として、UEFI（「Unified Extensible Firmware Interface」の略）があります。UEFI は BIOS の後継として設計されました。今日のほとんどのハードウェアには UEFI ファームウェアが内蔵されています。Macintosh マシンは何年も前から EFI ブートを使用しており、Windows もほとんどのものを UEFI ブートに移行しています。GPT 形式は EFI での使用を目的としていました。GPT ディスクを起動する場合でも、必ずしも EFI が必要なわけではありません。GPT ディスクの最初のセクターは、「保護 MBR」のために予約されており、BIOS ベースのマシンを起動できるようにしています。

UEFI は、起動に関するすべての情報を`.efi`ファイルに保存します。このファイルは、ハードウェア上の EFI システムパーティションと呼ばれる特別なパーティションに保存されます。このパーティション内にはブートローダーが含まれます。UEFI は従来の BIOS ファームウェアから多くの改善点があります。しかし、私たちは Linux を使用しているため、私たちのほとんどは BIOS を使用しています。したがって、これらのレッスンはすべてその前提に沿って進められます。

## Exercise

練習は完璧をもたらします！Linux のユーザーとグループ管理の理解を深めるための実践的なラボをいくつか紹介します。

1. **[useradd、usermod、および userdel で Linux ユーザーアカウントを管理する](https://labex.io/ja/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 新しいアカウントの作成と保護から、変更と削除まで、ユーザー管理の完全なライフサイクルを練習します。
2. **[groupadd、usermod、および groupdel で Linux グループを管理する](https://labex.io/ja/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 新しいグループの作成、ユーザーメンバーシップの変更、グループの削除など、グループ管理のためのコマンドラインユーティリティを実践的に体験します。
3. **[Linux でユーザーアカウントと Sudo 権限を設定する](https://labex.io/ja/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Linux システムのセキュリティを強化するために、ユーザーアカウントと sudo 権限を管理するための重要なテクニックを学びます。

これらのラボは、実際のシナリオで概念を適用し、Linux でのユーザーとグループ管理に自信をつけるのに役立ちます。

## Quiz Question

BIOS は何をロードしますか？

## Quiz Answer

bootloader
