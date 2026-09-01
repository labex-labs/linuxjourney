---
lesson_id: "filesystem-types"
course_id: "filesystem"
lang: "ja"
order_index: 2
title: "ファイルシステムの種類"
description: "Linux VFS がローカル、ネットワーク、仮想ファイルシステムを1つのインターフェースで示す仕組みを学びます。"
meta_title: "ファイルシステムの種類 - ファイルシステム"
meta_description: "ext4、Btrfs、XFS など、さまざまな Linux ファイルシステムの種類を発見してください。このガイドでは、ジャーナリングや仮想ファイルシステム（VFS）などの重要な概念を説明し、Linux で利用可能なさまざまなファイルシステムタイプを理解するのに役立ちます。"
meta_keywords: "linux ファイルシステムの種類，ファイルシステムの種類，ext4, Btrfs, XFS, ジャーナリング，VFS, linux チュートリアル"
---

Linux は、ディスク形式、ネットワークプロトコル、整合性モデル、機能、運用ツールが異なる多数のファイルシステム実装に対応します。適切な選択はディストリビューションの対応、ワークロード、復旧要件、ストレージ構成、管理者の経験次第です。

## 仮想ファイルシステム層

カーネルの Virtual Filesystem（VFS）層は、open、read、write、rename、権限検査などの共通操作を提供します。各実装はそれらを独自のデータ構造と格納先へ結び付けます。

1つのプロセスが ext4、XFS、NFS、tmpfs、procfs を共通のパス名・ファイル記述子モデルで利用できます。ただし、大文字小文字、ロック、権限、rename の保証、拡張属性、エラー処理などの機能や動作が同じになるわけではありません。

:::single-choice{#filesystem-types-vfs-role} Linux VFS の主な役割は何ですか？

::option[マウントした全ファイルシステムをディスク上で ext4 へ変換する。]{#filesystem-types-vfs-convert-ext4 explanation="抽象化は異なる実装と形式を維持します。"}
::option[アプリケーションの書き込み前に全ファイルをバックアップする。]{#filesystem-types-vfs-backup explanation="VFS は操作を振り分けますが、自動バックアップ履歴を提供しません。"}
::option[各実装へ共通のカーネルファイル操作を提供する。]{#filesystem-types-vfs-common-interface .correct explanation="アプリケーションは共通システムコールを使い、各ファイルシステムが基盤の動作を実装します。"}
:::

## ジャーナリングとクラッシュ整合性

ジャーナリングファイルシステムは選択した更新を journal へ記録し、クラッシュ後に未完了トランザクションを再生または破棄できます。主目的は、全体走査より速く構造的な整合性を回復することです。

最新のアプリケーションデータの生存、複数ファイルのトランザクションの正しさ、ストレージが全書き込みを守ったことまでは保証しません。ファイルシステムごとにデータモードと順序保証が異なり、アプリケーションも適切な flush と原子的更新を使う必要があります。journal はバックアップではなく、削除、マルウェア、デバイス故障を防ぎません。

:::single-choice{#filesystem-types-journal-scope} ファイルシステムのジャーナリングがクラッシュ後に主に回復を助けるものは何ですか？

::option[一貫したファイルシステムメタデータと記録済みトランザクション。]{#filesystem-types-journal-consistency .correct explanation="journal の再生でファイルシステム構造を一貫した状態へ戻しやすくします。"}
::option[全ユーザー文書のすべての過去版。]{#filesystem-types-journal-versions explanation="journal は版管理されたバックアップ格納庫ではありません。"}
::option[物理的に破壊されたストレージのデータ。]{#filesystem-types-journal-hardware-loss explanation="デバイス損失からの復旧には外部の冗長性やバックアップが必要です。"}
:::

## 一般的なローカルファイルシステム

- **ext4**：成熟したジャーナリングファイルシステムで、Linux ディストリビューションと復旧ツールから広く対応される。
- **XFS**：大きなファイルシステムと並列 I/O ワークロードによく選ばれる、拡張性の高いジャーナリングファイルシステム。
- **Btrfs**：チェックサム、サブボリューム、スナップショット、統合マルチデバイス機能を持つ copy-on-write ファイルシステム。

機能には運用上の文脈が必要です。同じ障害デバイス上の Btrfs スナップショットは当初、元データとストレージを共有し、独立バックアップではありません。XFS と ext4 は拡張、縮小、修復、調整能力が異なります。root 用を選択・変更する前に、導入カーネル、起動環境、復旧ツールの対応を確認します。

:::single-choice{#filesystem-types-btrfs-snapshot} 同じデバイス上の Btrfs スナップショットが完全なバックアップではないのはなぜですか？

::option[スナップショットが必ず元サブボリュームを即座に削除するから。]{#filesystem-types-snapshot-deletes explanation="別のサブボリュームビューを作り、元を必ず削除するわけではありません。"}
::option[元データと同じストレージ障害領域を共有するから。]{#filesystem-types-snapshot-failure-domain .correct explanation="デバイス損失や深刻な破損が元データとローカルスナップショットの両方へ影響できます。"}
::option[Btrfs は1ファイルより多く表せないから。]{#filesystem-types-btrfs-one-file explanation="ディレクトリツリーと多数のファイルを扱う汎用ファイルシステムです。"}
:::

## 互換、ネットワーク、仮想ファイルシステム

Linux は FAT 系、exFAT、NTFS などもマウントできますが、Unix の所有権、権限、リンク、ファイル名の意味は異なります。不足機能をどう示すかはマウントオプションとドライバー実装次第です。

NFS や SMB はサーバーとネットワークプロトコルに依存し、独自のキャッシュと識別規則を持ちます。tmpfs、procfs、sysfs は通常の永続ディスク形式を使わない仮想ファイルシステムです。tmpfs は揮発性データをメモリで支えられたページに置き、procfs と sysfs はカーネルインターフェースを公開します。

:::single-choice{#filesystem-types-procfs-category} procfs に最も合う説明はどれですか？

::option[リムーバブルメディア用の Windows 互換形式。]{#filesystem-types-procfs-windows explanation="その用途は FAT や exFAT に近く、procfs は Linux カーネル向けです。"}
::option[プロセスとカーネルのインターフェースを公開する仮想ファイルシステム。]{#filesystem-types-procfs-virtual .correct explanation="通常の永続ファイルを保存せず、実行中のカーネルビューを生成します。"}
::option[データベースボリューム向けのジャーナリングディスクファイルシステム。]{#filesystem-types-procfs-journal explanation="通常のディスク上の journal やデータボリュームの役割はありません。"}
:::

## 稼働中の種類を調べる

```bash
$ findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

ほかに、マウント済み容量には `df -T`、ブロックデバイスと検出シグネチャには `lsblk -f`、実行中カーネルが対応・認識する種類には `/proc/filesystems` を使えます。答える質問が異なり、未マウントのファイルシステムは通常のマウント一覧へ現れません。

:::single-choice{#filesystem-types-findmnt-output} ここで、マウント先、ソース、種類、オプションを直接一覧表示するコマンドはどれですか？

::option[`findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS`]{#filesystem-types-findmnt .correct explanation="findmnt がマウント表を読み、要求したフィールドを整形します。"}
::option[`lsblk -o NAME,SIZE,MODEL,SERIAL,ROTA`]{#filesystem-types-mkfs-destructive explanation="有効なマウント種類やオプションではなく、ブロックデバイスのハードウェア詳細を表示します。"}
::option[`cat /proc/filesystems | sort --unique`]{#filesystem-types-rm-proc explanation="有効なマウント元とオプションではなく、カーネル対応の種類を報告します。"}
:::

使い捨てストレージ上の [Linux パーティションとファイルシステムの管理](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845) で、種類、マウントオプション、検出方法を比較できます。

## まとめ

同じ意味だと思い込まず、ファイルシステムの分類を比較できるようになりました。

1. VFS を実装間の共通操作へ関連付ける。
2. ジャーナリングをバックアップではなくクラッシュ整合性支援として扱う。
3. ext4、XFS、Btrfs を対応操作とワークロードで比較する。
4. ローカルディスク、ネットワーク、互換、仮想ファイルシステムを区別する。
5. マウント・ブロックデバイスツールを異なる一覧質問へ使い分ける。
