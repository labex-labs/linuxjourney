---
index: 7
lang: "ja"
title: "電源状態"
meta_title: "電源状態 - Init"
meta_description: "Linux システムの電源状態：シャットダウン、再起動、および停止コマンドについて学びます。Linux システムを安全に電源オフまたは再起動する方法を理解します。必須コマンドから始めましょう！"
meta_keywords: "Linux shutdown, reboot command, halt system, power off Linux, Linux commands, beginner Linux, Linux tutorial, system states"
---

## Lesson Content

コマンドラインを通じてシステムの状態を制御する方法について、まだ議論していなかったとは信じがたいことです。`init` について話すとき、システムを起動するモードだけでなく、システムを停止するモードについても議論します。

システムをシャットダウンするには：

```bash
sudo shutdown -h now
```

このコマンドはシステムを停止（電源オフ）します。いつ実行したいかを時間を指定する必要があります。分単位で時間を追加すると、その時間後にシステムがシャットダウンします。

```bash
sudo shutdown -h +2
```

これは 2 分後にシステムをシャットダウンします。`shutdown` コマンドで再起動することもできます。

```bash
sudo shutdown -r now
```

または、単に `reboot` コマンドを使用します。

```bash
sudo reboot
```

## Exercise

このトピックに関する特定のラボはありませんが、関連する Linux スキルと概念を練習するために、包括的な[Linux 学習パス](https://labex.io/ja/learn/linux)を探索することをお勧めします。

## Quiz Question

4 分後にシステムをシャットダウンするコマンドは何ですか？

## Quiz Answer

sudo shutdown -h +4
