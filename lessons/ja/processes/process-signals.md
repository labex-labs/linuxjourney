---
lang: "ja"
title: "シグナル"
meta_description: "Linux シグナル、その目的、SIGINT や SIGKILL などの一般的なタイプ、およびプロセスがそれらをどのように処理するかについて学びます。Linux をよりよく制御するために、シグナルの基本を理解してください。"
meta_keywords: "Linux シグナル，SIGKILL, SIGINT, プロセス間通信，Linux チュートリアル，Linux 初心者，Linux ガイド"
---

## Lesson Content

シグナルとは、何かが起こったことをプロセスに通知するものです。

### Why We Have Signals

これらはソフトウェア割り込みであり、多くの用途があります。

- ユーザーは、特殊な端末文字 (Ctrl-C) または (Ctrl-Z) を入力して、プロセスを強制終了、中断、または一時停止できます。
- ハードウェアの問題が発生し、カーネルがプロセスに通知したい場合があります。
- ソフトウェアの問題が発生し、カーネルがプロセスに通知したい場合があります。
- これらは基本的に、プロセスが通信できる方法です。

### Signal Process

何らかのイベントによってシグナルが生成されると、それはプロセスに配信されます。配信されるまで、保留状態と見なされます。プロセスが実行されると、シグナルが配信されます。ただし、プロセスにはシグナルマスクがあり、指定された場合、シグナル配信をブロックするように設定できます。シグナルが配信されると、プロセスはさまざまなことを実行できます。

- シグナルを無視する。
- シグナルを「キャッチ」し、特定のハンドラルーチンを実行する。
- 通常の終了システムコールとは異なり、プロセスが終了する。
- シグナルマスクに応じて、シグナルをブロックする。

### Common Signals

各シグナルは、SIGxxx の形式のシンボリック名を持つ整数によって定義されます。最も一般的なシグナルの一部は次のとおりです。

- SIGHUP or HUP or 1: Hangup
- SIGINT or INT or 2: Interrupt
- SIGKILL or KILL or 9: Kill
- SIGSEGV or SEGV or 11: Segmentation fault
- SIGTERM or TERM or 15: Software termination
- SIGSTOP or STOP: Stop

シグナルによって番号は異なる場合があるため、通常は名前で参照されます。

一部のシグナルはブロックできません。一例は SIGKILL シグナルです。KILL シグナルはプロセスを破壊します。

## Exercise

No exercises for this lesson.

## Quiz Question

ブロックできないシグナルは何ですか？

## Quiz Answer

SIGKILL
