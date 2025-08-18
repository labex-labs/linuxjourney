---
lang: "ja"
title: "所有権のパーミッション"
meta_description: "chown コマンドと chgrp コマンドを使用して、Linux でファイルの所有権を変更する方法を学びます。この初心者向けの Linux チュートリアルで、ユーザーとグループのパーミッションを理解しましょう。"
meta_keywords: "chown, chgrp, Linux ファイルの所有権，Linux パーミッション，Linux コマンド，初心者向け Linux, Linux チュートリアル，Linux ガイド"
---

## Lesson Content

ファイルのパーミッションを変更するだけでなく、ファイルのグループとユーザーの所有権も変更できます。

### Modify user ownership

```bash
sudo chown patty myfile
```

このコマンドは、`myfile` の所有者を `patty` に設定します。

### Modify group ownership

```bash
sudo chgrp whales myfile
```

このコマンドは、`myfile` のグループを `whales` に設定します。

### Modify both user and group ownership at the same time

ユーザーの後にコロンとグループ名を追加すると、ユーザーとグループの両方を同時に設定できます。

```bash
sudo chown patty:whales myfile
```

## Exercise

いくつかのテストファイルのグループとユーザーを変更します。その後、`ls -l` でパーミッションを確認してください。

## Quiz Question

ユーザーの所有権を変更するために使用するコマンドは何ですか？

## Quiz Answer

chown
