---
index: 4
lang: "ja"
title: "ディスクパーティション分割"
meta_title: "ディスクパーティション分割 - ファイルシステム"
meta_description: "parted を使用して Linux でディスクパーティション分割を学びましょう。ディスクのパーティション分割、選択、表示、サイズ変更の方法を理解します。この初心者向けのガイドで始めましょう！"
meta_keywords: "Linux ディスクパーティション分割，parted コマンド，fdisk, gparted, Linux チュートリアル，初心者向け Linux, ディスク管理，Linux ガイド"
---

## Lesson Content

USB ドライブで作業することで、ファイルシステムに関する実践的な内容を学びましょう。もし USB ドライブをお持ちでなくても、心配ありません。これからの数レッスンは、それに沿って学習を進めることができます。

まず、ディスクをパーティション分割する必要があります。これには多くのツールが利用できます。

- fdisk - 基本的なコマンドラインパーティション分割ツール。GPT をサポートしていません
- parted - MBR と GPT の両方のパーティション分割をサポートするコマンドラインツール
- gparted - parted の GUI バージョン
- gdisk - fdisk ですが、MBR をサポートせず、GPT のみをサポートします

パーティション分割には parted を使用しましょう。USB デバイスを接続し、デバイス名が /dev/sdb2 であるとします。

### parted を起動する

```bash
sudo parted
```

parted ツールに入ります。ここでデバイスをパーティション分割するためのコマンドを実行できます。

### デバイスを選択する

```bash
select /dev/sdb2
```

作業するデバイスを選択するには、そのデバイス名で選択します。

### 現在のパーティションテーブルを表示する

```plaintext
(parted) print
Model: Seagate (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: msdos

Number  Start   End     Size    Type      File system     Flags
 1      1049kB  6860MB  6859MB  primary   ext4            boot
 2      6861MB  21.5GB  14.6GB  extended
 5      6861MB  7380MB  519MB   logical   linux-swap(v1)
 6      7381MB  21.5GB  14.1GB  logical   xfs
```

ここでは、デバイス上の利用可能なパーティションが表示されます。**start**と**end**のポイントは、パーティションがハードドライブ上で占めるスペースを示します。パーティションに適切な開始位置と終了位置を見つける必要があります。

### デバイスをパーティション分割する

```bash
mkpart primary 123 4567
```

開始点と終了点を選択してパーティションを作成するだけです。使用したテーブルの種類に応じて、パーティションの種類を指定する必要があります。

### パーティションのサイズを変更する

スペースがない場合、パーティションのサイズを変更することもできます。

```bash
resize 2 1245 3456
```

パーティション番号を選択し、次にサイズを変更したい開始点と終了点を選択します。

Parted は非常に強力なツールであり、ディスクをパーティション分割する際には注意が必要です。

## Exercise

習うより慣れろ！Linux のディスクパーティション分割とファイルシステム管理の理解を深めるための実践的な演習です。

1. [Linux パーティションとファイルシステムを管理する](https://labex.io/ja/labs/comptia-manage-linux-partitions-and-filesystems-590845) - この演習では、Linux でディスクパーティションとファイルシステムを管理する方法を学びます。安全なセカンダリ仮想ディスク上で、fdisk を使用して新しいパーティションを作成し、ext4 でフォーマットし、マウントし、/etc/fstab で永続的なマウントを設定し、スワップパーティションを作成します。

この演習は、ディスクパーティション分割とファイルシステム管理の概念を実際のシナリオで適用し、これらの必須の Linux 管理スキルに自信をつけるのに役立ちます。

## Quiz Question

パーティションを作成するための parted コマンドは何ですか？

## Quiz Answer

mkpart
