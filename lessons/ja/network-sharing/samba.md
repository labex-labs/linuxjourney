---
index: 5
lang: "ja"
title: "Samba"
meta_title: "Samba - ネットワーク共有"
meta_description: "Windows および macOS 向けに Linux 上で Samba ファイル共有を設定する方法を学びます。この初心者向けガイドでは、インストール、設定、共有へのアクセスについて説明します。さあ、始めましょう！"
meta_keywords: "Samba, Linux ファイル共有，smb.conf, CIFS, smbclient, Linux チュートリアル，初心者ガイド"
---

## Lesson Content

コンピューティングの初期には、Windows マシンが Linux マシンとファイルを共有する必要が生じ、そこで Server Message Block (SMB) プロトコルが誕生しました。SMB は Windows オペレーティングシステム間でファイルを共有するために使用され（macOS も SMB でファイル共有を行います）、後に Common Internet File System (CIFS) プロトコルの形で整理され、最適化されました。

Samba は、Linux 上で CIFS を扱うための Linux ユーティリティの総称です。ファイル共有に加えて、プリンターなどのリソースも共有できます。

### Create a network share with Samba

Windows マシンがアクセスできるネットワーク共有を作成するための基本的な手順を見ていきましょう。

### Install Samba

```bash
sudo apt update
sudo apt install samba
```

### Setup smb.conf

Samba の設定ファイルは `/etc/samba/smb.conf` にあります。このファイルは、どのディレクトリを共有するか、そのアクセス権限、その他のオプションをシステムに指示します。デフォルトの `smb.conf` には、すでに多くのコメント付きコードが含まれており、それらを例として独自の構成を記述できます。

```bash
sudo vi /etc/samba/smb.conf
```

### Set up a password for Samba

```bash
sudo smbpasswd -a [username]
```

### Create a shared directory

```bash
mkdir /my/directory/to/share
```

### Restart the Samba service

```bash
sudo service smbd restart
```

### Accessing a Samba share via Windows

Windows では、ファイル名を指定して実行プロンプトに `\\HOST\sharename` と入力するだけです。

### Accessing a Samba/Windows share via Linux

```bash
smbclient //HOST/directory -U user
```

Samba パッケージには、Windows または Samba サーバーにアクセスするために使用できる **smbclient** と呼ばれるコマンドラインツールが含まれています。共有に接続すると、ナビゲートしてファイルを転送できます。

### Attach a Samba share to your system

ファイルを一つずつ転送する代わりに、ネットワーク共有をシステムにマウントするだけで済みます。

```bash
sudo mount -t cifs servername:directory mountpoint -o user=username,pass=password
```

## Exercise

Samba 共有を設定します。もし持っていない場合は、`smb.conf` を開いて、設定ファイル内のオプションに慣れてください。

## Quiz Question

Windows と Linux 間でファイル転送に使用される最新のプロトコルは何ですか？

## Quiz Answer

CIFS
