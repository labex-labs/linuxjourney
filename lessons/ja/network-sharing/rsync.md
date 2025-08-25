---
index: 2
lang: "ja"
title: "rsync"
meta_title: "rsync - ネットワーク共有"
meta_description: "効率的な Linux ファイル同期とバックアップのために rsync を学びましょう。rsync コマンドとオプションを使用して、リモートおよびローカルのデータ転送を理解します。Linux スキルを向上させましょう！"
meta_keywords: "rsync, Linux ファイル転送，データバックアップ，ファイル同期，Linux チュートリアル，rsync コマンド，初心者，ガイド"
---

## Lesson Content

異なるホスト間でデータをコピーするために使用されるもう 1 つのツールは、rsync（remote synchronization の略）です。rsync は scp と非常によく似ていますが、大きな違いがあります。rsync は、コピー先のデータがすでに存在するかどうかを事前にチェックし、差分のみをコピーする特殊なアルゴリズムを使用します。たとえば、ファイルをコピーしている途中でネットワークが中断され、コピーが途中で停止したとします。rsync は、最初からすべてを再コピーするのではなく、コピーされなかった部分のみをコピーします。

また、コピーするファイルの整合性をチェックサムで検証します。これらの小さな最適化により、ファイル転送の柔軟性が向上し、rsync はリモートおよびローカルでのディレクトリ同期、データバックアップ、大容量データ転送などに最適です。

よく使われる rsync オプションの一部：

- v - 詳細な出力
- r - ディレクトリを再帰的に処理
- h - 人間が読める形式の出力
- z - 転送を容易にするために圧縮。低速接続に最適

### 同じホスト上のファイルをコピー/同期する

```bash
rsync -zvr /my/local/directory/one /my/local/directory/two
```

### リモートホストからローカルホストにファイルをコピー/同期する

```bash
rsync /local/directory username@remotehost.com:/remote/directory
```

### ローカルホストからリモートホストにファイルをコピー/同期する

```bash
rsync username@remotehost.com:/remote/directory /local/directory
```

## Exercise

このトピックに関する特定のラボはありませんが、関連する Linux スキルと概念を練習するために、包括的な[Linux 学習パス](https://labex.io/ja/learn/linux)を探索することをお勧めします。

## Quiz Question

データバックアップに役立つコマンドは何ですか？

## Quiz Answer

rsync
