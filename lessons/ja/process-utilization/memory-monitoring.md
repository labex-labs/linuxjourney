---
lang: "ja"
title: "メモリ監視"
description: "vmstat を使って Linux のメモリ使用量を監視する方法を学びます。システムパフォーマンスのためのメモリ、スワップ、CPU メトリクスを理解しましょう。あなたの Linux の旅を始めましょう！"
keywords: "vmstat, Linux メモリ監視，システムパフォーマンス，Linux チュートリアル，メモリ使用量，初心者 Linux, Linux ガイド"
---

## Lesson Content

CPU 監視や I/O 監視に加えて、**vmstat**を使ってメモリ使用量を監視できます。

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

各フィールドは以下の通りです。

### procs

- r - 実行中のプロセス数
- b - 割り込み不可能なスリープ状態にあるプロセス数

### memory

- swpd - 使用されている仮想メモリの量
- free - 空きメモリの量
- buff - バッファとして使用されているメモリの量
- cache - キャッシュとして使用されているメモリの量

### swap

- si - ディスクからスワップインされたメモリの量
- so - ディスクにスワップアウトされたメモリの量

### io

- bi - ブロックデバイスから受信したブロックの量
- bo - ブロックデバイスに送信したブロックの量

### system

- in - 1 秒あたりの割り込み数
- cs - 1 秒あたりのコンテキストスイッチ数

### cpu

- us - ユーザー時間で費やされた時間
- sy - カーネル時間で費やされた時間
- id - アイドル時間で費やされた時間
- wa - I/O 待ちで費やされた時間

## Exercise

vmstat でメモリ使用量を確認してください。

## Quiz Question

メモリ使用率を確認するために使用されるツールは何ですか？

## Quiz Answer

vmstat
