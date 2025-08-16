---
lang: "ja"
title: "デバイスタイプ"
description: "Linux のデバイスタイプ（character、block、pipe、socket）と、`ls -l /dev` を使用してそれらを識別する方法について学びます。メジャー/マイナーデバイス番号を理解します。初心者向けの Linux チュートリアル。"
keywords: "Linux デバイスタイプ，ls -l /dev, character device, block device, major minor device number, Linux チュートリアル，Linux ガイド，初心者"
---

## Lesson Content

デバイスの管理方法について話す前に、実際にいくつかのデバイスを見てみましょう。

```bash
$ ls -l /dev
brw-rw----   1 root disk      8,   0 Dec 20 20:13 sda
crw-rw-rw-   1 root root      1,   3 Dec 20 20:13 null
srw-rw-rw-   1 root root           0 Dec 20 20:13 log
prw-r--r--   1 root root           0 Dec 20 20:13 fdata
```

左から右への列は次のとおりです。

- Permissions
- Owner
- Group
- Major Device Number
- Minor Device Number
- Timestamp
- Device Name

`ls` コマンドでは、各行の最初のビットでファイルの種類を確認できることを覚えておいてください。デバイスファイルは次のように表記されます。

- c - character
- b - block
- p - pipe
- s - socket

### Character Device

これらのデバイスはデータを転送しますが、一度に 1 文字ずつ転送します。多くの擬似デバイス (`/dev/null`) が character device として表示されます。これらのデバイスは実際にはマシンに物理的に接続されていませんが、オペレーティングシステムに優れた機能を提供します。

### Block Device

これらのデバイスはデータを転送しますが、固定サイズの大きなブロックで転送します。ハードドライブ、ファイルシステムなど、データブロックを利用するデバイスは、ほとんどの場合 block device として表示されます。

### Pipe Device

名前付きパイプは、2 つ以上のプロセスが互いに通信することを可能にします。これらは character device に似ていますが、出力がデバイスに送信されるのではなく、別のプロセスに送信されます。

### Socket Device

Socket device は、pipe device と同様にプロセス間の通信を容易にしますが、一度に多くのプロセスと通信できます。

### Device Characterization

デバイスは、**major device number** と **minor device number** の 2 つの数値を使用して特徴付けられます。これらの数値は上記の `ls` の例で確認できます。これらはコンマで区切られています。たとえば、デバイスのデバイス番号が **8, 0** だったとします。

major device number は使用されるデバイスドライバを表し、この場合は 8 です。これは多くの場合、sd block device の major number です。minor number は、このドライバクラス内でどのユニークなデバイスであるかをカーネルに伝えます。この場合、0 は最初のデバイス (a) を表すために使用されます。

## Exercise

`/dev` ディレクトリを見て、どのような種類のデバイスがあるか調べてください。

## Quiz Question

`ls -l` コマンドで character device を表す記号は何ですか？

## Quiz Answer

c
