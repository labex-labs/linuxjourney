---
lang: "ja"
title: "rsync"
description: "効率的な Linux ファイル同期とバックアップのために rsync を学びましょう。rsync コマンドとオプションを使用して、リモートおよびローカルのデータ転送を理解します。Linux スキルを向上させましょう！"
keywords: "rsync, Linux ファイル転送，データバックアップ，ファイル同期，Linux チュートリアル，rsync コマンド，初心者，ガイド"
---

## Lesson Content

異なるホスト間でデータをコピーするために使用されるもう 1 つのツールは、rsync（remote synchronization の略）です。Rsync は scp と非常によく似ていますが、大きな違いがあります。Rsync は、コピー先のデータがすでに存在するかどうかを事前にチェックし、差分のみをコピーする特別なアルゴリズムを使用します。たとえば、ファイルをコピーしている途中でネットワークが中断され、コピーが途中で停止したとします。rsync は、最初からすべてを再コピーするのではなく、コピーされなかった部分のみをコピーします。

また、コピーするファイルの整合性をチェックサムで検証します。これらの小さな最適化により、ファイル転送の柔軟性が向上し、rsync はリモートおよびローカルでのディレクトリ同期、データバックアップ、大容量データ転送などに最適です。

よく使われる rsync のオプション：

- v - 詳細な出力
- r - ディレクトリを再帰的に処理
- h - 人間が読める形式の出力
- z - 転送を容易にするために圧縮（低速な接続に最適）

### Copy/sync files on the same host

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### Copy/sync files to local host from a remote host

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### Copy/sync files to a remote host from a local host

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

rsync を使用して、あるディレクトリを別のディレクトリに同期させます。重要なディレクトリを上書きしないように注意してください！

## Quiz Question

データバックアップに役立つコマンドは何ですか？

## Quiz Answer

rsync
