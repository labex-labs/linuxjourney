---
index: 5
lang: "ja"
title: "Systemd の概要"
meta_title: "Systemd の概要 - Init"
meta_description: "Systemd の基本を学びましょう：ユニット、ターゲット、ブートプロセスを理解します。Systemd が Linux でサービスとシステム状態をどのように管理しているかを発見してください。あなたの旅を始めましょう！"
meta_keywords: "Systemd, Systemd ユニット，Systemd ターゲット，Linux ブートプロセス，Linux サービス，初心者，チュートリアル，ガイド"
---

## Lesson Content

Systemd は、ほとんどの最新の Linux ディストリビューションにおける標準の init システムです。`/usr/lib/systemd`ディレクトリがある場合、あなたはほとんどの場合 systemd を使用しています。

Systemd はシステムを起動・実行するためにゴール（目標）を使用します。基本的に、達成したいターゲットがあり、そのターゲットには満たされるべき依存関係があります。Systemd は非常に柔軟で堅牢であり、プロセスを開始するために厳密なシーケンスに従いません。典型的な systemd のブート中に起こることは次のとおりです：

1. まず、systemd は通常`/etc/systemd/system`または`/usr/lib/systemd/system`に配置されている設定ファイルをロードします。
2. 次に、ブートゴールを決定します。これは通常`default.target`です。
3. Systemd はブートターゲットの依存関係を特定し、それらをアクティブ化します。

SysV のランレベルと同様に、systemd は異なるターゲットにブートします：

- `poweroff.target` - システムをシャットダウン
- `rescue.target` - シングルユーザーモード
- `multi-user.target` - ネットワーキング付きマルチユーザー
- `graphical.target` - ネットワーキングと GUI 付きマルチユーザー
- `reboot.target` - 再起動

`default.target`のデフォルトのブートゴールは、通常`graphical.target`を指します。

Systemd が操作する主要なオブジェクトはユニットとして知られています。Systemd はサービスを停止・開始するだけでなく、ファイルシステムのマウントやネットワークソケットの監視なども行います。その堅牢性のため、操作するユニットにはさまざまなタイプがあります。最も一般的なユニットは次のとおりです：

- Service units - これらは私たちが開始・停止してきたサービスであり、これらのユニットファイルは`.service`で終わります。
- Mount units - これらはファイルシステムをマウントし、これらのユニットファイルは`.mount`で終わります。
- Target units - これらは他のユニットをグループ化し、ファイルは`.target`で終わります。

例えば、`default.target`にブートすると仮定します。このターゲットは`networking.service`ユニットや`crond.service`ユニットなどをグループ化しているため、単一のユニットをアクティブ化すると、そのユニット以下のすべてがアクティブ化されます。

## Exercise

このトピックに関する特定のラボはありませんが、関連する Linux スキルと概念を練習するために、包括的な[Linux 学習パス](https://labex.io/ja/learn/linux)を探求することをお勧めします。

## Quiz Question

他のユニットをグループ化するために使用されるユニットは何ですか？

## Quiz Answer

target
