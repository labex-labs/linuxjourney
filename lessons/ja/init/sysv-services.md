---
index: 2
lang: "ja"
title: "System V サービス"
meta_title: "System V サービス - Init"
meta_description: "Linux における従来の System V (SysV) サービスの管理方法を学びます。このガイドでは、`service` コマンドを使用して System V init システム上のサービスの一覧表示、開始、停止、再起動について解説します。"
meta_keywords: "system v, sysv init, linux サービス，service コマンド，linux サービス管理，サービス開始，サービス停止，サービス再起動，linux system v"
---

## Lesson Content

**System V**（または SysV）は、Unix ライクなオペレーティングシステムにおける古典的な初期化システムの一つです。多くの最新の Linux ディストリビューションは`systemd`のような新しいシステムに移行していますが、多くのシステムが後方互換性を維持しているため、**System V**サービスの管理方法を理解しておくことは依然として価値のあるスキルです。

### service コマンド

**System V** init システムでサービスを操作するための主要なツールは`service`コマンドです。これはラッパースクリプトとして機能し、サービスの制御プロセスを簡素化します。

### 全てのサービスのリスト表示

利用可能なすべてのサービスとその現在のステータスを把握するには、`--status-all`フラグを使用します。このコマンドは各サービスをリストし、実行中（`+`）、停止中（`-`）、または状態が不明（`?`）であることを示します。

```bash
service --status-all
```

### 特定のサービスの制御

個々のサービスを管理するには、サービス名の後に`start`、`stop`、`restart`などのアクションを指定します。これらのアクションには管理者権限が必要なため、通常は`sudo`を使用します。

ネットワーキングサービスを開始する場合：

```bash
sudo service networking start
```

実行中のサービスを停止する場合：

```bash
sudo service networking stop
```

設定変更を適用する場合に役立つ、サービスを停止してからすぐに再起動する場合：

```bash
sudo service networking restart
```

これらのコマンドは**System V** init システム専用ではありません。Upstart サービスを管理するためにも使用できることがよくあります。Linux ディストリビューションが進化し続けるにつれて、従来の init スクリプトからの移行を円滑にするために、`service`コマンドのような互換性レイヤーが維持されています。

## Exercise

練習あるのみです！Linux におけるプロセスとタスクの管理、これらはサービス管理の基本です。理解を深めるための実践的なラボを以下に示します。

1. **[Linux プロセスの管理と監視](https://labex.io/ja/labs/comptia-manage-and-monitor-linux-processes-590864)** - 実際の Linux 環境でプロセスを操作、検査、監視、終了する練習をします。
2. **[Linux での at と cron を使用したタスクのスケジュール](https://labex.io/ja/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 一回限りのジョブには`at`を、定期的なタスクには`cron`を使用してタスクを自動化する方法を学びます。これはサービス自動化の重要なスキルです。

これらのラボは、概念を実際のシナリオに適用し、システム操作の管理に対する自信を構築するのに役立ちます。

## Quiz Question

System V システムで`peanut`という名前のサービスを停止するための完全なコマンドは何ですか？大文字と小文字に注意して、正確な英語のコマンドを提供してください。

## Quiz Answer

sudo service peanut stop
