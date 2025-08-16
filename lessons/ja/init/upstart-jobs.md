---
title: "Upstart ジョブ"
description: "initctl コマンドを使用して Linux で Upstart ジョブを管理する方法を学びます。ジョブのステータス、サービスの開始、停止、再起動を理解します。Linux システム管理スキルを向上させましょう。"
keywords: "Upstart ジョブ，initctl, Linux サービス，システム管理，Linux チュートリアル，初心者向けガイド"
---

## Lesson Content

Upstart は多くのイベントやジョブの実行をトリガーできます。残念ながら、イベントやジョブがどこから発生したかを簡単に見る方法がないため、`/etc/init`にあるジョブ設定を詳しく調べる必要があります。ほとんどの場合、Upstart ジョブ設定ファイルを見る必要はありませんが、特定のジョブをより簡単に制御したいと思うでしょう。Upstart システムで使用できる便利なコマンドはたくさんあります。

### View jobs

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

Upstart ジョブのリストが、それぞれ異なるステータスで表示されます。各行で、ジョブ名が最初の値であり、2 番目のフィールド（`/`の前）は実際にはジョブの目標です。3 番目の値（`/`の後）は現在のステータスです。したがって、`shutdown`ジョブは最終的に停止したいが、現在は待機状態にあることがわかります。ジョブのステータスと目標は、ジョブを開始または停止するにつれて変化します。

### View specific job

```plaintext
initctl status networking
networking start/running
```

Upstart ジョブ設定の書き方の詳細には触れませんが、これらの設定でジョブが停止、開始、再起動されることはすでに知っています。これらのジョブはイベントも発行するため、他のジョブを開始できます。Upstart 操作の手動コマンドについて説明しますが、興味があれば、`.conf`ファイルをさらに深く掘り下げるべきです。

### Manually start a job

```bash
sudo initctl start networking
```

### Manually stop a job

```bash
sudo initctl stop networking
```

### Manually restart a job

```bash
sudo initctl restart networking
```

### Manually emit an event

```bash
sudo initctl emit some_event
```

## Exercise

Upstart ジョブのリストを観察してください。次に、今日学んだコマンドのいずれかを使用してジョブの状態を変更してください。その後、何に気づきますか？

## Quiz Question

`peanuts`という Upstart ジョブを手動で再起動するにはどうすればよいですか？

## Quiz Answer

sudo initctl restart peanuts
