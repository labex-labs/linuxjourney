---
index: 2
lang: "ja"
title: "System V サービス"
meta_title: "System V サービス - Init"
meta_description: "コマンドラインツールを使用して System V サービスを管理する方法を学びます。この初心者向けの Linux チュートリアルで、サービスの一覧表示、開始、停止、再起動の方法を発見してください。"
meta_keywords: "System V サービス，Linux サービス，service コマンド，SysV init, Linux チュートリアル，初心者 Linux, サービス管理，Linux ガイド"
---

## Lesson Content

Sys V サービスを管理するために使用できるコマンドラインツールはたくさんあります。

### サービスを一覧表示する

```bash
service --status-all
```

### サービスを開始する

```bash
sudo service networking start
```

### サービスを停止する

```bash
sudo service networking stop
```

### サービスを再起動する

```bash
sudo service networking restart
```

これらのコマンドは Sys V init システムに固有のものではありません。Upstart サービスを管理するためにも使用できます。Linux は従来の Sys V init スクリプトから移行しようとしているため、その移行を支援するための仕組みがまだ残っています。

## Exercise

練習は完璧をもたらします！Linux でサービスを管理するための基本であるプロセスとタスク管理の理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux プロセスの管理と監視](https://labex.io/ja/labs/comptia-manage-and-monitor-linux-processes-590864)** - 実際の Linux 環境でプロセスと対話し、検査し、監視し、終了させる練習をします。
2. **[Linux で at と cron を使用してタスクをスケジュールする](https://labex.io/ja/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - サービス自動化の重要なスキルである、1 回限りのジョブには `at` を、定期的なタスクには `cron` を使用してタスクを自動化する方法を学びます。

これらの演習は、実際のシナリオで概念を適用し、システム操作の管理に自信をつけるのに役立ちます。

## Quiz Question

Sys V で `peanut` という名前のサービスを停止するコマンドは何ですか？

## Quiz Answer

sudo service peanut stop
