---
index: 4
lang: "ja"
title: "sysfs"
meta_title: "sysfs - デバイス"
meta_description: "sysfs、詳細な Linux デバイス情報と管理のための仮想ファイルシステムについて学びます。/sys と/dev の違いを理解します。Linux の旅を始めましょう！"
meta_keywords: "sysfs, /sys ディレクトリ，Linux デバイス，仮想ファイルシステム，Linux チュートリアル，初心者ガイド"
---

## Lesson Content

Sysfs は、システム上のデバイスをより適切に管理するためにずっと前に作成されました。これは、`/dev`ディレクトリが適切に行えなかったタスクです。Sysfs は仮想ファイルシステムであり、ほとんどの場合、`/sys`ディレクトリにマウントされます。これにより、`/dev`ディレクトリで確認できるよりも詳細な情報が得られます。`/sys`と`/dev`の両方のディレクトリは非常によく似ており、ある点ではそうですが、大きな違いがあります。基本的に、`/dev`ディレクトリは単純です。他のプログラムがデバイス自体にアクセスできるようにしますが、`/sys`ファイルシステムは情報を表示し、デバイスを管理するために使用されます。

`/sys`ファイルシステムには、製造元やモデル、デバイスが接続されている場所、デバイスの状態、デバイスの階層など、システム上のすべてのデバイスに関するすべての情報が含まれています。ここにあるファイルはデバイスノードではないため、`/sys`ディレクトリからデバイスと直接やり取りすることはありません。むしろ、デバイスを管理しています。

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

練習は完璧をもたらします！Linux でのハードウェアデバイスの探索に関する理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux でハードウェアデバイスを探索する](https://labex.io/ja/labs/comptia-explore-hardware-devices-in-linux-590861)** - `/sys`ファイルシステムがデバイス情報を提供するのと同様に、Linux 環境内でハードウェアデバイスを特定し、検査する練習をします。

この演習は、システムハードウェアとその Linux での表現を理解するという概念を適用し、デバイス探索に自信を持つのに役立ちます。

## Quiz Question

デバイスに関する詳細情報を表示するために使用されるディレクトリは何ですか？

## Quiz Answer

/sys
