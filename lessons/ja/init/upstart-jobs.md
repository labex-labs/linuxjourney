---
index: 4
lang: "ja"
title: "Upstart ジョブ"
meta_title: "Upstart ジョブ - Init"
meta_description: "Linux 環境での Upstart ジョブを使用したサービス管理ガイド。initctl ユーティリティを使用して、Upstart Linux システム上のジョブの一覧表示、開始、停止、再起動を学習します。"
meta_keywords: "Upstart ジョブ，initctl, upstart linux, Linux サービス，システム管理，init システム，Linux チュートリアル"
---

## Lesson Content

Upstart は、一部の**upstart linux**ディストリビューションで使用されるイベント駆動型の init システムであり、起動時およびシステム実行中のサービスやタスクの管理を行います。これはジョブとイベントのシステムを通じて機能します。すべてのイベントの起源を追跡するのは複雑で、`/etc/init`内のジョブ設定を調べる必要があることがよくありますが、より一般的にはコマンドラインから直接これらのジョブを管理する必要があります。`initctl`ユーティリティは、この目的のためのコマンド群を提供します。

### ジョブステータスの表示

既知のすべての Upstart ジョブとその現在の状態を確認するには、`list`コマンドを使用します。

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

出力には、ジョブ名、そのゴール、および現在のステータスが表示されます。例の`shutdown stop/waiting`では、ジョブ名は`shutdown`、ゴールは`stop`、現在のステータスは`waiting`です。ジョブを操作すると、ジョブのステータスとゴールは変化します。

特定のジョブの状態を確認するには、`status`コマンドを使用します。

```plaintext
initctl status networking
networking start/running
```

### ジョブの手動制御

`/etc/init`内のジョブ設定ファイルは、ジョブがどのように開始、停止し、イベントと相互作用するかを定義しますが、`initctl`を使用してこれらのアクションを手動で上書きできます。これはトラブルシューティングや管理タスクの実行に役立ちます。

ジョブを手動で開始するには：

```bash
sudo initctl start networking
```

ジョブを手動で停止するには：

```bash
sudo initctl stop networking
```

ジョブを再起動するには（停止してから開始する便利なショートカットです）：

```bash
sudo initctl restart networking
```

### カスタムイベントの発行

Upstart ジョブはイベントによってトリガーされます。カスタムジョブのトリガーやテスト目的で、イベントを「発行」することもできます。`some_event`で開始するように設定されているジョブは、次のコマンドによってトリガーされます。

```bash
sudo initctl emit some_event
```

## Exercise

練習あるのみです！Upstart に特化したラボはありませんが、タスクのスケジュール設定と管理方法を理解することは、システムプロセスの制御にとって極めて重要です。理解を深めるための実践的なラボを以下に示します。

1. **[Linux における at および cron を使用したタスクのスケジュール設定](https://labex.io/ja/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 一回限りのジョブと定期的なジョブの作成、管理、削除を練習します。これらは、Upstart が処理するような Linux 環境におけるサービスやタスクの管理の基本概念です。

このラボは、実際のシナリオでタスク自動化の概念を適用し、システム運用の管理に対する自信を構築するのに役立ちます。

## Quiz Question

`peanuts`という名前の Upstart ジョブを手動で再起動するにはどうすればよいですか？完全なコマンドを提供してください。（注：回答は大文字と小文字が区別され、英語である必要があります。）

## Quiz Answer

sudo initctl restart peanuts
