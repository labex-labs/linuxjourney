---
index: 4
lang: "ja"
title: "sysfs"
meta_title: "sysfs - デバイス"
meta_description: "sysfs とは何か、また Linux の sys システムにおけるその役割を探ります。このガイドでは、デバイス情報のための仮想ファイルシステムである Linux の/sys ディレクトリについて解説し、/dev との違いを対比します。"
meta_keywords: "sysfs, sysfs とは，/sys, linux /sys, linux sys, sys システム，仮想ファイルシステム，linux デバイス，/dev"
---

## Lesson Content

sysfs ファイルシステムは、/dev ディレクトリが完全には対応できなかった Linux システム上のデバイスを管理するためのより良い方法を提供するために導入されました。**Linux で/sys とは何か**を理解することは、現代のシステム管理の鍵となります。

### sysfs とは？

`sysfs`は通常`/sys`にマウントされる仮想ファイルシステムであり、カーネルのデバイスモデルからユーザー空間へカーネルオブジェクト、ハードウェアデバイス、およびドライバに関する情報をエクスポートします。物理ディスク上のファイルとは異なり、`/sys`内のファイルとディレクトリはオンザフライで生成され、**sys system**の現在の状態を表します。

### linux /sys ディレクトリの役割

**linux /sys**ディレクトリの主な目的は、システム上のすべてのデバイスの構造化されたビューを提供することです。ここには、製造元とモデル、デバイスがどこに接続されているか、現在の状態、デバイス階層内の位置など、詳細情報が含まれています。

ここで見るファイルは、`/dev`内のデバイスノードのようなものではありません。`/sys`を通じてデバイス自体に直接アクセスするのではなく、デバイスの属性を表示および管理するために使用します。

### sysfs と/dev の比較

`/sys`と`/dev`はどちらもデバイスに関連していますが、異なる機能を果たします。

- `/dev`ディレクトリは、プログラムがデバイス自体にアクセスできるようにする特殊ファイルであるデバイスノードを提供します。
- `/sys`ファイルシステムは、デバイスに関する情報を表示し、デバイスを管理するために使用されます。これは基盤となるデバイスモデルを公開します。

例えば、`/sys`内のブロックデバイスディレクトリの内容を調べてみましょう。

```bash
pete@icebox:~$ ls /sys/block/sda
alignment_offset  discard_alignment  holders   removable  sda6       trace
bdi               events             inflight  ro         size       uevent
capability        events_async       power     sda1       slaves
dev               events_poll_msecs  queue     sda2       stat
device            ext_range          range     sda5       subsystem
```

この出力は、`sda`ハードドライブに関連するさまざまな属性とサブディレクトリを示しており、`/dev/sda`単独よりもはるかに詳細なビューを提供します。

## Exercise

練習あるのみです！Linux でのハードウェアデバイス探索に関する理解を深めるための実践的なラボを以下に示します。

1. **[Linux でハードウェアデバイスを探索する](https://labex.io/ja/labs/comptia-explore-hardware-devices-in-linux-590861)** - `/sys`ファイルシステムがデバイス情報を提供するのと同様に、Linux 環境内でハードウェアデバイスを識別し検査する練習をします。

このラボは、システムハードウェアの理解とその Linux での表現という概念を適用し、デバイス探索への自信を深めるのに役立ちます。

## Quiz Question

デバイスに関する詳細情報を表示するために使用されるディレクトリはどれですか？回答は英語でお願いします。

## Quiz Answer

/sys
