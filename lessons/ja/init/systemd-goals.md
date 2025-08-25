---
index: 6
lang: "ja"
title: "Systemd の目標"
meta_title: "Systemd の目標 - Init"
meta_description: "systemd ユニットの基本と必須の systemctl コマンドを学びましょう。Linux でサービスを管理し、ステータスを表示し、ユニットを有効にする方法を理解します。あなたの旅を始めましょう！"
meta_keywords: "systemd, systemctl, Linux サービス，ユニットファイル，初心者，チュートリアル，ガイド，Linux コマンド"
---

## Lesson Content

systemd のユニットファイル作成の詳細には立ち入りません。しかし、ユニットファイルの簡単な概要と、ユニットを手動で制御する方法について説明します。

以下は基本的なサービスユニットファイルです：foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

これはシンプルなサービスターゲットです。ファイルの冒頭には`[Unit]`セクションがあります。これにより、ユニットファイルに説明を付けたり、ユニットをアクティブにする順序を制御したりできます。次の部分は`[Service]`セクションです。ここには、サービスの開始、停止、または再読み込みを行うことができます。そして、`[Install]`セクションは依存関係のために使用されます。これは systemd ファイルの作成のほんの一部に過ぎないので、さらに詳しく知りたい場合は、このテーマについて調べてみることをお勧めします。

それでは、systemd ユニットで使用できるいくつかのコマンドを見ていきましょう。

### ユニットを一覧表示する

```bash
systemctl list-units
```

### ユニットのステータスを表示する

```bash
systemctl status networking.service
```

### サービスを開始する

```bash
sudo systemctl start networking.service
```

### サービスを停止する

```bash
sudo systemctl stop networking.service
```

### サービスを再起動する

```bash
sudo systemctl restart networking.service
```

### ユニットを有効にする

```bash
sudo systemctl enable networking.service
```

### ユニットを無効にする

```bash
sudo systemctl disable networking.service
```

繰り返しになりますが、systemd がいかに奥深いか、まだその全貌は見ていません。もっと学びたい場合は、ぜひ調べてみてください。

## Exercise

習うより慣れろ！systemd サービスによって制御されることが多いプロセスの管理に関する理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux プロセスの管理と監視](https://labex.io/ja/labs/comptia-manage-and-monitor-linux-processes-590864)** - フォアグラウンドプロセスとバックグラウンドプロセスとの対話、`ps`による検査、`top`によるリソース監視、`renice`による優先度調整、`kill`による終了を練習します。この演習は、systemd ユニット管理の実行時効果に関する実践的な経験を提供します。

これらの演習は、概念を実際のシナリオに適用し、Linux でのプロセス管理に自信をつけるのに役立ちます。

## Quiz Question

peanut.service という名前のサービスを開始するコマンドは何ですか？

## Quiz Answer

sudo systemctl start peanut.service
