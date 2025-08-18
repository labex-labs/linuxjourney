---
index: 4
lang: "ja"
title: "ディスクパーティション分割"
meta_title: "ディスクパーティション分割 - ファイルシステム"
meta_description: "parted を使用して Linux でのディスクパーティション分割を学びましょう。ディスクのパーティション分割、選択、表示、サイズ変更の方法を理解します。この初心者向けのガイドで始めましょう！"
meta_keywords: "Linux ディスクパーティション分割，parted コマンド，fdisk, gparted, Linux チュートリアル，初心者向け Linux, ディスク管理，Linux ガイド"
---

## Lesson Content

USB ドライブでプロセスを実行することで、ファイルシステムに関する実践的な作業を行いましょう。USB ドライブをお持ちでなくても心配ありません。次のいくつかのレッスンは引き続き学習できます。

まず、ディスクをパーティション分割する必要があります。これには多くのツールが利用可能です。

- fdisk - 基本的なコマンドラインパーティション分割ツール。GPT をサポートしていません
- parted - MBR と GPT の両方のパーティション分割をサポートするコマンドラインツール
- gparted - parted の GUI バージョン
- gdisk - fdisk ですが、MBR はサポートせず、GPT のみをサポートします

パーティション分割には parted を使用しましょう。USB デバイスを接続し、デバイス名が /dev/sdb2 であるとします。

### Launch parted

```bash
sudo parted
```

parted ツールに入ります。ここで、デバイスをパーティション分割するためのコマンドを実行できます。

### Select the device

```bash
select /dev/sdb2
```

作業するデバイスを選択するには、デバイス名で選択します。

### View current partition table

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

ここでは、デバイス上の利用可能なパーティションが表示されます。**start** と **end** のポイントは、パーティションがハードドライブ上でスペースを占める場所です。パーティションの適切な開始位置と終了位置を見つける必要があります。

### Partition the device

```bash
mkpart primary 123 4567
```

開始点と終了点を選択し、パーティションを作成します。使用したテーブルに応じて、パーティションのタイプを指定する必要があります。

### Resize a partition

スペースがない場合は、パーティションのサイズを変更することもできます。

```bash
resize 2 1245 3456
```

パーティション番号を選択し、次にサイズ変更したい開始点と終了点を選択します。

Parted は非常に強力なツールであり、ディスクをパーティション分割する際には注意が必要です。

## Exercise

USB ドライブをパーティション分割し、ドライブの半分を ext4、残りの半分を空き領域にします。

## Quiz Question

パーティションを作成するための parted コマンドは何ですか？

## Quiz Answer

mkpart
