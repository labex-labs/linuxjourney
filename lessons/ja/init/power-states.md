---
lang: "ja"
title: "電源状態"
description: "Linux システムの電源状態、シャットダウン、再起動、停止コマンドについて学びます。Linux システムを安全に電源オフまたは再起動する方法を理解します。必須コマンドから始めましょう！"
keywords: "Linux シャットダウン，reboot コマンド，halt システム，Linux 電源オフ，Linux コマンド，初心者 Linux, Linux チュートリアル，システム状態"
---

## Lesson Content

コマンドラインを通じてシステムの状態を制御する方法について、まだ議論していなかったとは信じがたいことです。`init` について話すとき、システムを起動するモードだけでなく、システムを停止するモードについても議論します。

システムをシャットダウンするには：

```bash
sudo shutdown -h now
```

このコマンドはシステムを停止（電源オフ）します。いつ実行するか時間を指定する必要があります。システムをその時間でシャットダウンする分数を追加できます。

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

マシンをシャットダウンするとき、`init` で何が起こっていると思いますか？

## Quiz Question

4 分後にシステムをシャットオフするコマンドは何ですか？

## Quiz Answer

sudo shutdown -h +4
