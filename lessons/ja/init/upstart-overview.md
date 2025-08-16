---
title: "Upstart の概要"
description: "Upstart、そのイベント駆動型モデル、および Linux でのサービス管理方法について学びます。Upstart ジョブ構成とその init システムとしての役割を理解します。"
keywords: "Upstart, init system, Linux services, Ubuntu, SysV, 初心者向けチュートリアル，Linux ガイド"
---

## Lesson Content

Upstart は Canonical によって開発されたため、しばらくの間 Ubuntu の init 実装でしたが、最新の Ubuntu インストールでは現在 systemd が使用されています。Upstart は、厳格な起動プロセスやタスクのブロックなど、SysV の問題点を改善するために作成されました。Upstart のイベント駆動型およびジョブ駆動型モデルにより、イベントが発生したときにそれに応答できます。

Upstart を使用しているかどうかを確認するには、`/usr/share/upstart`ディレクトリがある場合、それはかなり良い指標です。

ジョブは Upstart が実行するアクションであり、イベントは他のプロセスからジョブをトリガーするために受信されるメッセージです。ジョブとその構成のリストを表示するには：

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

これらのジョブ構成内には、ジョブをいつどのように開始するかに関する情報があります。

たとえば、`networking.conf`ファイルには、次のような簡単な記述があるかもしれません。

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

これは、ランレベル 2、3、または 5 でネットワークのセットアップを開始し、ランレベル 0 でネットワークを停止することを意味します。構成ファイルの記述方法はたくさんあり、利用可能なさまざまなジョブ構成を見るとそれがわかるでしょう。

Upstart の動作方法は次のとおりです。

1. まず、`/etc/init`からジョブ構成をロードします。
2. 起動イベントが発生すると、そのイベントによってトリガーされたジョブを実行します。
3. これらのジョブは新しいイベントを生成し、それらのイベントがさらにジョブをトリガーします。
4. Upstart は、必要なすべてのジョブが完了するまでこれを続けます。

## Exercise

Upstart を実行している場合、`/etc/init`にあるジョブ構成を理解できるか試してみてください。

## Quiz Question

Ubuntu で使用されている init 実装は何ですか？

## Quiz Answer

upstart
