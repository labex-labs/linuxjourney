---
lang: "ja"
title: "Systemd の目標"
meta_title: "Systemd の目標 - Init"
meta_description: "systemd ユニットの基本と必須の systemctl コマンドを学びましょう。Linux でサービスを管理し、ステータスを表示し、ユニットを有効にする方法を理解します。あなたの旅を始めましょう！"
meta_keywords: "systemd, systemctl, Linux サービス，ユニットファイル，初心者，チュートリアル，ガイド，Linux コマンド"
---

## Lesson Content

systemd のユニットファイルを記述する詳細には立ち入りません。しかし、ユニットファイルの簡単な概要と、ユニットを手動で制御する方法について説明します。

基本的なサービスユニットファイルは次のとおりです：foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

これはシンプルなサービスターゲットです。ファイルの冒頭には、`[Unit]`セクションがあります。これにより、ユニットファイルに説明を付けたり、ユニットをアクティブにする順序を制御したりできます。次の部分は`[Service]`セクションです。ここには、サービスの開始、停止、再読み込みを行うことができます。そして、`[Install]`セクションは依存関係に使用されます。これは systemd ファイルの記述のほんの一部に過ぎないので、もっと知りたい場合はこの主題について調べてみることをお勧めします。

それでは、systemd ユニットで使用できるいくつかのコマンドを見ていきましょう。

### List units

```bash
systemctl list-units
```

### View status of unit

```bash
systemctl status networking.service
```

### Start a service

```bash
sudo systemctl start networking.service
```

### Stop a service

```bash
sudo systemctl stop networking.service
```

### Restart a service

```bash
sudo systemctl restart networking.service
```

### Enable a unit

```bash
sudo systemctl enable networking.service
```

### Disable a unit

```bash
sudo systemctl disable networking.service
```

繰り返しになりますが、systemd がどれほど奥深いかについてはまだ見ていませんので、もっと学びたい場合は調べてみてください。

## Exercise

ユニットのステータスを表示し、いくつかのサービスを開始および停止してください。何が観察されますか？

## Quiz Question

peanut.service という名前のサービスを開始するコマンドは何ですか？

## Quiz Answer

sudo systemctl start peanut.service
