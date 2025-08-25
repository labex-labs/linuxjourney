---
index: 6
lang: "ja"
title: "メモリ監視"
meta_title: "メモリ監視 - プロセス利用率"
meta_description: "vmstat で Linux のメモリ使用量を監視する方法を学びます。システムパフォーマンスのためのメモリ、スワップ、CPU メトリックを理解します。Linux の旅を始めましょう！"
meta_keywords: "vmstat, Linux メモリ監視，システムパフォーマンス，Linux チュートリアル，メモリ使用量，初心者 Linux, Linux ガイド"
---

## Lesson Content

CPU 監視や I/O 監視に加えて、**vmstat**を使用してメモリ使用量を監視できます。

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

各フィールドは以下の通りです。

### procs

- r - 実行中のプロセス数
- b - 割り込み不可能なスリープ状態のプロセス数

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
- bo - ブロックデバイスに送信されたブロックの量

### system

- in - 1 秒あたりの割り込み数
- cs - 1 秒あたりのコンテキストスイッチ数

### cpu

- us - ユーザー時間で費やされた時間
- sy - カーネル時間で費やされた時間
- id - アイドル時間で費やされた時間
- wa - I/O 待ちで費やされた時間

## Exercise

練習あるのみ！システムおよびメモリ監視の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux free コマンド：システムメモリの監視](https://labex.io/ja/labs/linux-linux-free-command-monitoring-system-memory-388496)** - システムメモリの使用状況を監視および分析し、さまざまな表示形式と総メモリ消費量を理解する方法を学びます。
2. **[Linux top コマンド：リアルタイムシステム監視](https://labex.io/ja/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - プロセス、CPU、メモリ使用量を含むシステムパフォーマンスをリアルタイムで監視し、ソートとフィルタリングのためのさまざまなオプションを使用する方法を学びます。

これらのラボは、実際のシナリオでシステムリソース監視の概念を適用し、Linux システムパフォーマンスの分析に自信をつけるのに役立ちます。

## Quiz Question

メモリ使用率を表示するために使用されるツールは何ですか？

## Quiz Answer

vmstat
