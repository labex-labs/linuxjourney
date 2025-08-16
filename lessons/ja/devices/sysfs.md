---
title: "sysfs"
description: "sysfs、Linux デバイスの詳細情報と管理のための仮想ファイルシステムについて学びます。/sys と/dev の違いを理解しましょう。Linux の学習を始めましょう！"
keywords: "sysfs, /sys ディレクトリ，Linux デバイス，仮想ファイルシステム，Linux チュートリアル，初心者ガイド"
---

## Lesson Content

Sysfs は、システム上のデバイスをより適切に管理するためにずっと昔に作成されました。これは、`/dev`ディレクトリでは適切に行えなかったタスクです。Sysfs は仮想ファイルシステムであり、ほとんどの場合、`/sys`ディレクトリにマウントされます。これにより、`/dev`ディレクトリで確認できるよりも詳細な情報が得られます。`/sys`と`/dev`の両方のディレクトリは非常によく似ており、ある点ではそうですが、大きな違いがあります。基本的に、`/dev`ディレクトリはシンプルで、他のプログラムがデバイス自体にアクセスできるようにします。一方、`/sys`ファイルシステムは、情報を表示し、デバイスを管理するために使用されます。

`/sys`ファイルシステムには、基本的にシステム上のすべてのデバイスに関する情報が含まれています。例えば、製造元とモデル、デバイスがどこに接続されているか、デバイスの状態、デバイスの階層などです。ここにあるファイルはデバイスノードではないため、`/sys`ディレクトリからデバイスと直接やり取りするわけではありません。むしろ、デバイスを管理しているのです。

`/sys`ディレクトリの内容を見てみましょう。

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

## Exercise

`/sys`ディレクトリの内容を確認し、どのようなファイルがあるか見てみましょう。

## Quiz Question

デバイスの詳細情報を表示するために使用されるディレクトリは何ですか？

## Quiz Answer

/sys
