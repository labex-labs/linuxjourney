---
index: 6
lang: "ja"
title: "systemd の目標"
meta_title: "systemd の目標 - Init"
meta_description: "systemd の目標を探り、systemctl コマンドを使用して Linux サービスを管理する方法を学びます。このガイドでは、systemd ユニットファイルの基本、サービスの起動、停止、有効化の方法、およびステータスの表示について説明します。"
meta_keywords: "systemd, systemctl, Linux サービス，ユニットファイル，systemd の目標，サービス管理，systemd ユニット，初心者，チュートリアル，ガイド，Linux コマンド"
---

## Lesson Content

このレッスンでは、init システムを制御する主要ツールである`systemctl`を使用した systemd ユニットファイルの基本的な概要と管理方法を提供します。ユニットファイルの基本構造と、Linux サービスを管理するための必須コマンドについて説明します。

### Systemd ユニットファイルの理解

Systemd ユニットファイルは、systemd が管理できるサービス、マウントポイント、デバイス、またはその他のリソースを記述するプレーンテキストファイルです。`foobar.service`という名前のサービスユニットファイルの基本例を以下に示します。

```
[Unit]
Description=My Foobar Service
After=network.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

このシンプルなサービスファイルはセクションに分かれています。

- **[Unit]**: このセクションには、メタデータと依存関係情報が含まれます。`Description`はユニットの人間が読める名前を提供します。`After`や`Before`のようなディレクティブは起動順序を制御し、ネットワークが利用可能になった後にこのユニットが起動するようにします。
- **[Service]**: このセクションでは、サービスの管理方法を定義します。`ExecStart`ディレクティブは、サービスを起動するために実行するコマンドを指定するため、非常に重要です。`ExecStop`や`ExecReload`などの他のディレクティブは、サービスを停止またはリロードする方法を定義できます。
- **[Install]**: このセクションでは、`systemctl`でユニットが有効化または無効化されたときの動作を定義します。`WantedBy`ディレクティブは、標準的な非グラフィカルブートのための`multi-user.target`など、特定のターゲットの一部としてこのサービスを起動するように systemd に指示します。

これは systemd ユニットファイルの一端にすぎません。より高度な設定については、このトピックに関するさらなる調査を強くお勧めします。

### 必須の Systemctl コマンド

次に、systemd ユニットと対話し、Linux サービスを管理するために使用する必須の`systemctl`コマンドを見ていきましょう。

### Systemd ユニットの一覧表示

systemd が現在管理しているすべての稼働中のユニットを確認するには、`list-units`コマンドを使用します。

```bash
systemctl list-units
```

### ユニットの状態確認

特定のユニットの詳細な状態（アクティブかどうか、有効になっているか、最新のログエントリなど）を表示するには、`status`コマンドを使用します。

```bash
systemctl status networking.service
```

### サービス状態の管理

`start`、`stop`、`restart`を使用して、サービスの実行時状態を制御できます。

サービスを即座に起動するには：

```bash
sudo systemctl start networking.service
```

実行中のサービスを停止するには：

```bash
sudo systemctl stop networking.service
```

サービスを停止してから再度起動するには：

```bash
sudo systemctl restart networking.service
```

### サービスの有効化と無効化

サービスを有効化すると、起動プロセスにフックするためのシンボリックリンクが作成され、自動的に起動するようになります。無効化すると、そのリンクが削除されます。

サービスをブート時に起動するように有効化するには：

```bash
sudo systemctl enable networking.service
```

サービスをブート時の起動から無効化するには：

```bash
sudo systemctl disable networking.service
```

これらのコマンドは、最新の Linux システムにおけるサービス管理の構成要素です。これらを習得することは、Linux の道のりにおける重要な一歩です。

## Exercise

実践が新しいスキルを習得する鍵となります。このハンズオンラボは、systemd サービスによって制御されることが多いプロセスの管理に関する理解を深めるのに役立ちます。

1.  **[Linux プロセスの管理と監視](https://labex.io/ja/labs/comptia-manage-and-monitor-linux-processes-590864)** - フォアグラウンドおよびバックグラウンドプロセスとの対話、`ps`を使用した検査、`top`を使用したリソースの監視、`renice`を使用した優先度の調整、`kill`を使用した終了の練習をします。このラボは、systemd ユニット管理の実行時効果に関する実践的な経験を提供します。

## Quiz Question

What is the command to start a service named peanut.service? Please answer in English. The answer is case-sensitive.

## Quiz Answer

sudo systemctl start peanut.service
