---
index: 4
lang: "ja"
title: "NFS"
meta_title: "NFS - ネットワーク共有"
meta_description: "Linux での NFS クライアント設定と自動マウントについて学びます。ネットワークファイル共有に接続し、シームレスなアクセスに自動マウントを使用する方法を理解します。"
meta_keywords: "NFS クライアント，自動マウント，ネットワークファイルシステム，Linux ネットワーキング，mount コマンド，Linux チュートリアル，初心者"
---

## Lesson Content

Linux で最も標準的なネットワークファイル共有は NFS（Network File System）です。NFS を使用すると、サーバーはネットワークを介して 1 つ以上のクライアントとディレクトリやファイルを共有できます。

NFS サーバーの作成方法は複雑になる可能性があるため、ここでは詳しく説明しません。ただし、NFS クライアントの設定については説明します。

### NFS クライアントの設定

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### 自動マウント

NFS サーバーを頻繁に使用し、永続的にマウントしておきたいとします。通常、`/etc/fstab`ファイルを編集することを考えるかもしれませんが、常にサーバーへの接続が得られるとは限らず、起動時に問題を引き起こす可能性があります。代わりに、必要なときに NFS サーバーに接続できるように、自動マウントを設定することをお勧めします。これは、**automount**ツール、または最近の Linux バージョンでは**amd**を使用して行われます。指定されたディレクトリ内のファイルにアクセスすると、automount はリモートサーバーを検索し、自動的にマウントします。

## Exercise

このトピックに関する特定のラボはありませんが、関連する Linux スキルと概念を練習するために、包括的な[Linux 学習パス](https://labex.io/ja/learn/linux)を探索することをお勧めします。

## Quiz Question

マウントポイントを自動的に管理するために使用されるツールは何ですか？

## Quiz Answer

automount
