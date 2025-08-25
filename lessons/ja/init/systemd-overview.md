---
index: 5
lang: "ja"
title: "Systemd の概要"
meta_title: "Systemd の概要 - Init"
meta_description: "Systemd の基本を学びましょう：ユニット、ターゲット、起動プロセスを理解します。Systemd が Linux でサービスとシステムの状態をどのように管理するかを発見してください。あなたの旅を始めましょう！"
meta_keywords: "Systemd, Systemd ユニット，Systemd ターゲット，Linux 起動プロセス，Linux サービス，初心者，チュートリアル，ガイド"
---

## Lesson Content

Systemd は、init の新しい標準として徐々に定着しつつあります。もし`/usr/lib/systemd`ディレクトリがあるなら、おそらく systemd を使用しているでしょう。

Systemd は、システムを起動させるために「目標」を使用します。基本的に、達成したいターゲットがあり、このターゲットには満たすべき依存関係があります。Systemd は非常に柔軟で堅牢であり、プロセスを開始するための厳密な順序には従いません。典型的な systemd の起動中に何が起こるかを見てみましょう。

1. まず、systemd は通常`/etc/systemd/system`または`/usr/lib/systemd/system`にある設定ファイルを読み込みます。
2. 次に、起動目標を決定します。これは通常`default.target`です。
3. Systemd は起動ターゲットの依存関係を特定し、それらをアクティブ化します。

SysV のランレベルと同様に、systemd は異なるターゲットで起動します。

- `poweroff.target` - システムをシャットダウンする
- `rescue.target` - シングルユーザーモード
- `multi-user.target` - ネットワークを備えたマルチユーザー
- `graphical.target` - ネットワークと GUI を備えたマルチユーザー
- `reboot.target` - 再起動

`default.target`のデフォルトの起動目標は、通常`graphical.target`を指しています。

systemd が扱う主要なオブジェクトは「ユニット」として知られています。Systemd は単にサービスを停止したり開始したりするだけでなく、ファイルシステムをマウントしたり、ネットワークソケットを監視したりすることもできます。その堅牢性のため、さまざまな種類のユニットを操作します。最も一般的なユニットは次のとおりです。

- サービスユニット - これらは私たちが起動および停止してきたサービスです。これらのユニットファイルは`.service`で終わります。
- マウントユニット - これらはファイルシステムをマウントします。これらのユニットファイルは`.mount`で終わります。
- ターゲットユニット - これらは他のユニットをグループ化します。ファイルは`.target`で終わります。

例えば、`default.target`で起動するとしましょう。このターゲットは`networking.service`ユニット、`crond.service`ユニットなどをグループ化しているため、単一のユニットをアクティブ化すると、そのユニットの下にあるすべてがアクティブ化されます。

## Exercise

このトピックに関する特定のラボはありませんが、関連する Linux スキルと概念を練習するために、包括的な[Linux 学習パス](https://labex.io/ja/learn/linux)を探索することをお勧めします。

## Quiz Question

他のユニットをグループ化するために使用されるユニットは何ですか？

## Quiz Answer

target
