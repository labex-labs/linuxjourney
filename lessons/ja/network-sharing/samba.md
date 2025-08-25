---
index: 5
lang: "ja"
title: "Samba"
meta_title: "Samba - ネットワーク共有"
meta_description: "Windows および macOS 向けに Linux で Samba ファイル共有を設定する方法を学びます。この初心者向けガイドでは、インストール、設定、共有へのアクセスについて説明します。さあ、始めましょう！"
meta_keywords: "Samba, Linux ファイル共有，smb.conf, CIFS, smbclient, Linux チュートリアル，初心者ガイド"
---

## Lesson Content

コンピューティングの初期には、Windows マシンが Linux マシンとファイルを共有する必要が生じました。こうして Server Message Block (SMB) プロトコルが誕生しました。SMB は Windows オペレーティングシステム間でファイルを共有するために使用され（macOS も SMB でファイル共有を行います）、後に Common Internet File System (CIFS) プロトコルの形で整理され、最適化されました。

Samba は、Linux 上で CIFS を扱うための Linux ユーティリティの総称です。ファイル共有に加えて、プリンターなどのリソースも共有できます。

### Samba でネットワーク共有を作成する

Windows マシンがアクセスできるネットワーク共有を作成するための基本的な手順を見ていきましょう。

### Samba をインストールする

```bash
sudo apt update
sudo apt install samba
```

### smb.conf をセットアップする

Samba の設定ファイルは`/etc/samba/smb.conf`にあります。このファイルは、共有するディレクトリ、そのアクセス権限、その他のオプションをシステムに指示するものです。デフォルトの`smb.conf`には、すでに多くのコメント付きコードが含まれており、それらを例として独自の構成を記述できます。

```bash
sudo vi /etc/samba/smb.conf
```

### Samba のパスワードを設定する

```bash
sudo smbpasswd -a [username]
```

### 共有ディレクトリを作成する

```bash
mkdir /my/directory/to/share
```

### Samba サービスを再起動する

```bash
sudo service smbd restart
```

### Windows 経由で Samba 共有にアクセスする

Windows では、ファイル名を指定して実行プロンプトに`\\HOST\sharename`と入力するだけです。

### Linux 経由で Samba/Windows 共有にアクセスする

```bash
smbclient //HOST/directory -U user
```

Samba パッケージには、Windows または Samba サーバーにアクセスするために使用できる**smbclient**というコマンドラインツールが含まれています。共有に接続すると、ファイルをナビゲートしたり転送したりできます。

### Samba 共有をシステムにアタッチする

ファイルを一つずつ転送する代わりに、ネットワーク共有をシステムにマウントするだけで済みます。

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

このトピックに関する特定のラボはありませんが、関連する Linux スキルと概念を練習するために、包括的な[Linux 学習パス](https://labex.io/ja/learn/linux)を探索することをお勧めします。

## Quiz Question

Windows と Linux 間のファイル転送に使用される最新のプロトコルは何ですか？

## Quiz Answer

CIFS
