---
index: 3
lang: "ja"
title: "Upstart の概要"
meta_title: "Upstart の概要 - Init"
meta_description: "Upstart、そのイベント駆動モデル、および Linux でサービスを管理する方法について学習します。Upstart ジョブ構成とその init システムとしての役割を理解します。"
meta_keywords: "Upstart, init system, Linux サービス，Ubuntu, SysV, 初心者チュートリアル，Linux ガイド"
---

## Lesson Content

Upstart は Canonical によって開発されたため、一時期 Ubuntu の init 実装でしたが、現在の Ubuntu インストールでは systemd が使用されています。Upstart は、厳密な起動プロセスやタスクのブロッキングなど、SysV の問題を改善するために作成されました。Upstart のイベント駆動およびジョブ駆動モデルにより、イベントが発生したときにそれに応答できます。

Upstart を使用しているかどうかを確認するには、`/usr/share/upstart` ディレクトリがあるかどうかを確認するのが良い指標となります。

ジョブは Upstart が実行するアクションであり、イベントはジョブをトリガーするために他のプロセスから受信されるメッセージです。ジョブとその設定の一覧を表示するには、次のコマンドを実行します。

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

これらのジョブ構成内には、ジョブをいつどのように開始するかについての情報が含まれています。

例えば、`networking.conf` ファイルには、次のような簡単な記述があるかもしれません。

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

これは、runlevel 2、3、または 5 でネットワーキングの設定を開始し、runlevel 0 でネットワーキングを停止することを意味します。構成ファイルの書き方には多くの方法があり、利用可能なさまざまなジョブ構成を確認するとそれがわかります。

Upstart の動作方法は次のとおりです。

1. まず、`/etc/init` からジョブ構成をロードします。
2. 起動イベントが発生すると、そのイベントによってトリガーされるジョブを実行します。
3. これらのジョブが新しいイベントを生成し、それらのイベントがさらに多くのジョブをトリガーします。
4. Upstart は、必要なすべてのジョブが完了するまでこれを継続します。

## Exercise

練習あるのみです！Upstart は古い init システムですが、プロセスの管理方法やタスクのスケジューリング方法を理解することは、すべての Linux 管理者にとって非常に重要です。init システムがどのように動作するかの基礎となる、プロセス管理とタスク自動化の理解を深めるための実践的なラボを次に示します。

1. **[Manage and Monitor Linux Processes](https://labex.io/ja/labs/comptia-manage-and-monitor-linux-processes-590864)** - フォアグラウンドおよびバックグラウンドプロセスとの対話、`ps` を使用した検査、`top` を使用したリソースの監視、`kill` を使用した終了を練習します。このラボは、Upstart のような init システムが管理するプロセスのライフサイクルを理解するのに役立ちます。
2. **[Schedule Tasks with at and cron in Linux](https://labex.io/ja/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - `at` を使用した一回限りのジョブと `cron` を使用した定期的なタスクのスケジューリングについて学習します。これは、init システムがシステムサービスのために促進するタスク自動化の実際的な経験を提供します。

これらのラボは、特定の init システムが使用されているかどうかにかかわらず、Linux システムの管理に対する自信を構築するために、実際のシナリオでプロセス制御とタスク自動化の概念を適用するのに役立ちます。

## Quiz Question

Ubuntu で使用されている init 実装は何ですか？

## Quiz Answer

systemd
