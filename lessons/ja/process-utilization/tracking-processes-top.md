---
title: "プロセスの追跡：top"
description: "Linux の`top`コマンドを使用して、システムリソースを監視し、プロセスを追跡する方法を学びます。パフォーマンス分析のために、CPU、メモリ、およびプロセスの詳細を理解します。"
keywords: "Linux top コマンド，プロセス監視，システム利用率，Linux パフォーマンス，初心者，チュートリアル，ガイド"
---

## Lesson Content

このコースでは、システムのリソース使用率を読み取り、分析する方法を学びます。このレッスンでは、プロセスが何をしているかを追跡する必要があるときに役立つ優れたツールを紹介します。

### top

以前にも `top` について説明しましたが、今回はそれが実際に何を表示しているのか、その詳細を掘り下げていきます。`top` は、プロセスによるシステム使用率をリアルタイムで確認するために使用したツールであることを思い出してください。

```plaintext
top - 18:06:26 up 6 days,  4:07,  2 users,  load average: 0.92, 0.62, 0.59
Tasks: 389 total,   1 running, 387 sleeping,   0 stopped,   1 zombie
%Cpu(s):  1.8 us,  0.4 sy,  0.0 ni, 97.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  32870888 total, 27467976 used,  5402912 free,   518808 buffers
KiB Swap: 33480700 total,    39892 used, 33440808 free. 19454152 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 6675 patty    20   0 1731472 520960  30876 S   8.3  1.6 160:24.79 chrome
 6926 patty    20   0  935888 163456  25576 S   4.3  0.5   5:28.13 chrome
```

この出力が何を意味するのかを見ていきましょう。これをすべて覚える必要はありませんが、参照が必要なときにここに戻ってきてください。

### 1st line: This is the same information you would see if you ran the `uptime` command (more to come)

フィールドは左から右へ：

1. 現在時刻
2. システムが稼働している時間
3. 現在ログインしているユーザー数
4. システムのロードアベレージ（後述）

### 2nd line: Tasks that are running, sleeping, stopped, and zombied

### 3rd line: CPU information

1. `us`: user CPU time - niced されていないユーザープロセスを実行するのに費やされた CPU 時間の割合。
2. `sy`: system CPU time - カーネルおよびカーネルプロセスを実行するのに費やされた CPU 時間の割合。
3. `ni`: nice CPU time - niced されたプロセスを実行するのに費やされた CPU 時間の割合。
4. `id`: CPU idle time - アイドル状態に費やされた CPU 時間の割合。
5. `wa`: I/O wait - I/O を待機するのに費やされた CPU 時間の割合。この値が低い場合、問題はディスクまたはネットワーク I/O ではない可能性が高いです。
6. `hi`: hardware interrupts - ハードウェア割り込みの処理に費やされた CPU 時間の割合。
7. `si`: software interrupts - ソフトウェア割り込みの処理に費やされた CPU 時間の割合。
8. `st`: steal time - 仮想マシンを実行している場合、これは他のタスクのためにあなたから奪われた CPU 時間の割合です。

### 4th and 5th line: Memory Usage and Swap Usage

### Processes List that are Currently in Use

1. `PID`: プロセスの ID
2. `USER`: プロセスの所有者であるユーザー
3. `PR`: プロセスの優先度
4. `NI`: nice 値
5. `VIRT`: プロセスが使用する仮想メモリ
6. `RES`: プロセスが使用する物理メモリ
7. `SHR`: プロセスの共有メモリ
8. `S`: プロセスのステータスを示します：`S`=sleep, `R`=running, `Z`=zombie, `D`=uninterruptible, `T`=stopped
9. `%CPU`: このプロセスが使用する CPU の割合
10. `%MEM`: このプロセスが使用する RAM の割合
11. `TIME+`: このプロセスの活動の合計時間
12. `COMMAND`: プロセスの名前

特定のプロセスのみを追跡したい場合は、プロセス ID を指定することもできます。

```bash
top -p 1
```

## Exercise

`top` コマンドを試して、どのプロセスが最も多くのリソースを使用しているかを確認してください。

## Quiz Question

`top` の最初の行と同じ出力を表示するコマンドは何ですか？

## Quiz Answer

uptime
