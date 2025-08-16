---
lang: "ja"
title: "mount と umount"
description: "Linux の mount コマンドと umount コマンドを使ってファイルシステムを管理する方法を学びましょう。デバイスのマウント、アンマウント、UUID について初心者向けに理解を深めます。"
keywords: "Linux mount, umount command, mount filesystem, Linux UUID, beginner Linux, Linux tutorial, mount point, Linux guide"
---

## Lesson Content

ファイルシステムの内容を表示する前に、マウントする必要があります。そのためには、デバイスの場所、ファイルシステムの種類、およびマウントポイントが必要です。マウントポイントは、ファイルシステムがアタッチされるシステム上のディレクトリです。つまり、デバイスをマウントポイントにマウントしたいのです。

まず、マウントポイントを作成します。この場合は、**mkdir /mydrive** です。

```bash
sudo mount -t ext4 /dev/sdb2 /mydrive
```

これだけです！これで、/mydrive に移動すると、ファイルシステムの内容を見ることができます。**-t** はファイルシステムの種類を指定し、次にデバイスの場所、そしてマウントポイントが続きます。

マウントポイントからデバイスをアンマウントするには：

```bash
sudo umount /mydrive
```

または

```bash
sudo umount /dev/sdb2
```

カーネルはデバイスを見つけた順に名前を付けることを覚えておいてください。マウント後に何らかの理由でデバイス名が変わってしまった場合はどうでしょうか？幸いなことに、名前の代わりにデバイスの universally unique ID (UUID) を使用できます。

システム上のブロックデバイスの UUID を表示するには：

```bash
pete@icebox:~$ sudo blkid
/dev/sda1: UUID="130b882f-7d79-436d-a096-1e594c92bb76" TYPE="ext4"
/dev/sda5: UUID="22c3d34b-467e-467c-b44d-f03803c2c526" TYPE="swap"
/dev/sda6: UUID="78d203a0-7c18-49bd-9e07-54f44cdb5726" TYPE="xfs"
```

デバイス名、対応するファイルシステムの種類、およびその UUID を確認できます。これで、何かをマウントしたいときに、次のように使用できます。

```bash
sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mydrive
```

ほとんどの場合、UUID を介してデバイスをマウントする必要はありません。デバイス名を使用する方がはるかに簡単で、多くの場合、オペレーティングシステムは USB ドライブのような一般的なデバイスをマウントする方法を知っています。ただし、セカンダリハードドライブを追加した場合のように、起動時にファイルシステムを自動的にマウントする必要がある場合は、UUID を使用することになります。これについては次のレッスンで説明します。

## Exercise

`mount` と `umount` の manpage を見て、他にどのようなオプションが使えるか確認してください。

## Quiz Question

ファイルシステムをアタッチするために使用されるコマンドは何ですか？

## Quiz Answer

mount
