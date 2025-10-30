---
index: 3
lang: "ja"
title: "所有権パーミッション"
meta_title: "所有権パーミッション - パーミッション"
meta_description: "chown および chgrp コマンドを使用して Linux でファイルの所有権を変更する方法を学びます。この初心者向けの Linux チュートリアルで、ユーザーとグループのパーミッションを理解しましょう。"
meta_keywords: "chown, chgrp, Linux ファイルの所有権，Linux パーミッション，Linux コマンド，初心者向け Linux, Linux チュートリアル，Linux ガイド"
---

## Lesson Content

ファイルのパーミッションを変更するだけでなく、ファイルのグループとユーザーの所有権も変更できます。

### ユーザー所有権の変更

```bash
sudo chown patty myfile
```

このコマンドは、`myfile` の所有者を `patty` に設定します。

### グループ所有権の変更

```bash
sudo chgrp whales myfile
```

このコマンドは、`myfile` のグループを `whales` に設定します。

### ユーザーとグループの所有権を同時に変更する

ユーザーの後にコロンとグループ名を追加すると、ユーザーとグループの両方を同時に設定できます。

```bash
sudo chown patty:whales myfile
```

## Exercise

練習は完璧をもたらします！ファイル所有権とパーミッションの理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux ユーザーグループとファイルパーミッション](https://labex.io/ja/labs/linux-linux-user-group-and-file-permissions-18002)** - ファイルパーミッションの理解やファイル所有権の操作など、Linux のユーザーとグループ管理の重要な概念を学びます。このラボでは、マルチユーザーLinux 環境を保護するための実践的な経験を提供します。
2. **[新しいユーザーとグループの追加](https://labex.io/ja/labs/linux-add-new-user-and-group-17987)** - このチャレンジでは、新しいユーザーアカウントの作成、カスタムグループの設定、グループメンバーシップの管理を通じて、サーバー環境に新しいチームメンバーを追加するシミュレーションを行います。これにより、Linux のユーザーとグループ管理のスキルが試されます。

これらのラボは、実際のシナリオで概念を適用し、Linux でのファイル所有権とパーミッションの管理に自信を持つのに役立ちます。

## Quiz Question

ユーザー所有権を変更するために使用するコマンドは何ですか？

## Quiz Answer

chown
