---
title: "Systemd の概要"
description: "Systemd の基本を学び、ユニット、ターゲット、起動プロセスを理解します。Systemd が Linux でサービスとシステムの状態をどのように管理するかを発見します。あなたの旅を始めましょう！"
keywords: "Systemd, Systemd units, Systemd targets, Linux boot process, Linux services, 初心者，チュートリアル，ガイド"
---

## Lesson Content

Systemd は、init の新しい標準として徐々に定着しつつあります。`/usr/lib/systemd`ディレクトリがある場合、ほとんどの場合 systemd を使用しています。

Systemd は、システムを起動するために「目標」を使用します。基本的に、達成したいターゲットがあり、このターゲットには満たすべき依存関係があります。Systemd は非常に柔軟で堅牢であり、プロセスを開始するために厳密な順序には従いません。典型的な systemd の起動時に何が起こるかは次のとおりです。

1. まず、systemd は通常`/etc/systemd/system`または`/usr/lib/systemd/system`にある設定ファイルをロードします。
2. 次に、起動目標を決定します。これは通常`default.target`です。
3. Systemd は起動ターゲットの依存関係を特定し、それらをアクティブ化します。

SysV のランレベルと同様に、systemd は異なるターゲットで起動します。

- `poweroff.target` - システムをシャットダウン
- `rescue.target` - シングルユーザーモード
- `multi-user.target` - ネットワークありのマルチユーザー
- `graphical.target` - ネットワークと GUI ありのマルチユーザー
- `reboot.target` - 再起動

`default.target`のデフォルトの起動目標は、通常`graphical.target`を指します。

systemd が扱う主要なオブジェクトは「ユニット」として知られています。Systemd は単にサービスを停止したり開始したりするだけでなく、ファイルシステムをマウントしたり、ネットワークソケットを監視したりすることもできます。その堅牢性のため、さまざまな種類のユニットを操作します。最も一般的なユニットは次のとおりです。

- Service units - これらは私たちが起動および停止してきたサービスです。これらのユニットファイルは`.service`で終わります。
- Mount units - これらはファイルシステムをマウントします。これらのユニットファイルは`.mount`で終わります。
- Target units - これらは他のユニットをグループ化します。ファイルは`.target`で終わります。

たとえば、`default.target`で起動するとします。このターゲットは、`networking.service`ユニット、`crond.service`ユニットなどをグループ化するため、1 つのユニットをアクティブ化すると、そのユニットの下にあるすべてがアクティブ化されます。

## Exercise

No exercises for this lesson.

## Quiz Question

他のユニットをグループ化するために使用されるユニットは何ですか？

## Quiz Answer

target
