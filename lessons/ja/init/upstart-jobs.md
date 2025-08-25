---
index: 4
lang: "ja"
title: "Upstart ジョブ"
meta_title: "Upstart ジョブ - Init"
meta_description: "initctl コマンドを使用して Linux で Upstart ジョブを管理する方法を学びます。ジョブのステータス、サービスの開始、停止、再起動を理解します。Linux システム管理スキルを向上させます。"
meta_keywords: "Upstart ジョブ，initctl, Linux サービス，システム管理，Linux チュートリアル，初心者向けガイド"
---

## Lesson Content

Upstart は多くのイベントやジョブをトリガーして実行できます。残念ながら、イベントやジョブがどこから発生したのかを簡単に見つける方法がないため、`/etc/init`にあるジョブ設定を調べる必要があります。ほとんどの場合、Upstart ジョブの設定ファイルを見る必要はありませんが、特定のジョブをより簡単に制御したいと思うでしょう。Upstart システムでは、多くの便利なコマンドを使用できます。

### ジョブの表示

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

異なるステータスが適用された Upstart ジョブのリストが表示されます。各行で、ジョブ名が最初の値であり、2 番目のフィールド（`/`の前）は実際にはジョブの目標です。3 番目の値（`/`の後）は現在のステータスです。したがって、`shutdown`ジョブは最終的に停止したいが、現在は待機状態にあることがわかります。ジョブのステータスと目標は、ジョブを開始または停止すると変化します。

### 特定のジョブの表示

```plaintext
initctl status networking
networking start/running
```

Upstart ジョブの設定方法については詳しく説明しませんが、これらの設定でジョブが停止、開始、再起動されることはすでにわかっています。これらのジョブはイベントも発行するため、他のジョブを開始できます。Upstart 操作の手動コマンドについて説明しますが、興味があれば、`.conf`ファイルをさらに深く掘り下げるべきです。

### ジョブを手動で開始する

```bash
sudo initctl start networking
```

### ジョブを手動で停止する

```bash
sudo initctl stop networking
```

### ジョブを手動で再起動する

```bash
sudo initctl restart networking
```

### イベントを手動で発行する

```bash
sudo initctl emit some_event
```

## Exercise

練習は完璧をもたらします！Upstart に特定のラボはありませんが、タスクのスケジュールと管理方法を理解することは、システムプロセスを制御するために不可欠です。タスク管理の理解を深めるための実践的なラボを以下に示します。

1. **[Linux で at と cron を使用してタスクをスケジュールする](https://labex.io/ja/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Upstart によって処理されるような Linux 環境でサービスやタスクがどのように管理されるかに関連する基本的な概念である、1 回限りのジョブと定期的なジョブの作成、管理、削除を練習します。

このラボは、実際のシナリオでタスク自動化の概念を適用し、システム操作の管理に自信をつけるのに役立ちます。

## Quiz Question

`peanuts`という Upstart ジョブを手動で再起動するにはどうすればよいですか？

## Quiz Answer

sudo initctl restart peanuts
