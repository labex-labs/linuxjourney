---
index: 4
lang: "ja"
title: "NFS"
meta_title: "NFS - ネットワーク共有"
meta_description: "Linux での NFS クライアント設定と自動マウントについて学びます。ネットワークファイル共有に接続し、シームレスなアクセスを実現するために自動マウントを使用する方法を理解します。"
meta_keywords: "NFS クライアント，automount, ネットワークファイルシステム，Linux ネットワーキング，mount コマンド，Linux チュートリアル，初心者"
---

## Lesson Content

Linux で最も標準的なネットワークファイル共有は NFS (Network File System) です。NFS を使用すると、サーバーはネットワークを介して 1 つ以上のクライアントとディレクトリやファイルを共有できます。

NFS サーバーの作成方法は複雑になる可能性があるため、ここでは詳細には触れませんが、NFS クライアントの設定について説明します。

### Setting up NFS client

```bash
sudo service nfsclient start
sudo mount server:/directory /mount_directory
```

### Automounting

NFS サーバーを頻繁に使用し、永続的にマウントしておきたいとします。通常、`/etc/fstab`ファイルを編集することを考えるかもしれませんが、サーバーへの接続が常に得られるとは限らず、起動時に問題を引き起こす可能性があります。代わりに、必要なときに NFS サーバーに接続できるように、automounting を設定することをお勧めします。これは、**automount**ツール、または最近の Linux バージョンでは**amd**を使用して行われます。指定されたディレクトリ内のファイルにアクセスすると、automount はリモートサーバーを検索し、自動的にマウントします。

## Exercise

NFS の man ページを読んで、詳細を学びましょう。

## Quiz Question

マウントポイントを自動的に管理するために使用されるツールは何ですか？

## Quiz Answer

automount
