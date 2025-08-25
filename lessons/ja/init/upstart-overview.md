---
index: 3
lang: "ja"
title: "Upstart の概要"
meta_title: "Upstart の概要 - Init"
meta_description: "Upstart、そのイベント駆動型モデル、および Linux でのサービス管理方法について学びます。Upstart ジョブ設定とその init システムとしての役割を理解します。"
meta_keywords: "Upstart, init システム，Linux サービス，Ubuntu, SysV, 初心者向けチュートリアル，Linux ガイド"
---

## Lesson Content

Upstart は Canonical によって開発されたため、しばらくの間 Ubuntu の init 実装でした。しかし、最新の Ubuntu インストールでは、現在 systemd が使用されています。Upstart は、厳格な起動プロセスやタスクのブロックなど、SysV の問題点を改善するために作成されました。Upstart のイベント駆動型モデルとジョブ駆動型モデルにより、イベントが発生したときにそれに応答できます。

Upstart を使用しているかどうかを確認するには、`/usr/share/upstart`ディレクトリがあるかどうかが良い指標になります。

ジョブは Upstart が実行するアクションであり、イベントは他のプロセスからジョブをトリガーするために受信されるメッセージです。ジョブとその設定のリストを表示するには：

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

これらのジョブ設定内には、ジョブを開始する方法とタイミングに関する情報があります。

たとえば、`networking.conf`ファイルには、次のような簡単な記述がある場合があります。

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

これは、ランレベル 2、3、または 5 でネットワークの設定を開始し、ランレベル 0 でネットワークを停止することを意味します。設定ファイルの記述方法はたくさんあり、利用可能なさまざまなジョブ設定を見るとそれがわかります。

Upstart の動作は次のとおりです。

1. まず、`/etc/init`からジョブ設定をロードします。
2. 起動イベントが発生すると、そのイベントによってトリガーされたジョブを実行します。
3. これらのジョブは新しいイベントを作成し、それらのイベントがさらにジョブをトリガーします。
4. Upstart は、必要なすべてのジョブが完了するまでこれを続けます。

## Exercise

練習は完璧をもたらします！Upstart は古い init システムですが、プロセスの管理方法とタスクのスケジューリング方法を理解することは、Linux 管理者にとって非常に重要です。ここでは、init システムの動作の基礎となるプロセス管理とタスク自動化の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux プロセスの管理と監視](https://labex.io/ja/labs/comptia-manage-and-monitor-linux-processes-590864)** - フォアグラウンドプロセスとバックグラウンドプロセスとの対話、`ps`での検査、`top`でのリソース監視、`kill`での終了を練習します。このラボは、Upstart のような init システムが管理するプロセスのライフサイクルを理解するのに役立ちます。
2. **[Linux で at と cron を使用してタスクをスケジュールする](https://labex.io/ja/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - `at`で 1 回限りのジョブを、`cron`で定期的なタスクをスケジュールする方法を学びます。これは、init システムがシステムサービスのために促進するコア機能であるタスク自動化の実践的な経験を提供します。

これらのラボは、使用している特定の init システムに関係なく、実際のシナリオでプロセス制御とタスク自動化の概念を適用し、Linux システムの管理に自信を築くのに役立ちます。

## Quiz Question

Ubuntu で使用されている init の実装は何ですか？

## Quiz Answer

upstart
