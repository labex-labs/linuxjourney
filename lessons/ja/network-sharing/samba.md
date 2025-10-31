---
index: 5
lang: "ja"
title: "Samba"
meta_title: "Samba - ネットワーク共有"
meta_description: "Linux での Samba ネットワーク共有の設定方法を学びます。このガイドでは、Samba プロトコル、インストール、設定、および smb クライアントを使用した共有への接続について解説します。"
meta_keywords: "Samba, smb linux, linux smb, samba ネットワーク，samba プロトコル，smb samba, ファイル共有，smb.conf, cifs, smbclient, linux チュートリアル"
---

## Lesson Content

長年にわたり、Windows と Linux マシン間でファイルを共有することは、混在 OS 環境における主要な課題でした。この問題に対する解決策として登場したのが、Server Message Block (SMB) プロトコルです。元々 Windows 向けに開発されましたが、**samba protocol** は後に Common Internet File System (CIFS) と呼ばれる方言に洗練されました。現在、最新のシステムは新しいバージョンの SMB を使用していますが、これらの用語はしばしば一緒に使われます。

Samba は、Linux およびその他の Unix 系システム上で**SMB/CIFS**プロトコルを実装する強力なソフトウェアスイートです。これは**smb linux**統合の鍵であり、Linux サーバーが Windows、macOS、その他の Linux クライアントに対してファイルサーバーおよびプリントサーバーとして機能することを可能にし、シームレスな**samba network**を構築します。

### Linux への Samba のインストール

まず、Samba パッケージをインストールする必要があります。コマンドは使用している Linux ディストリビューションのパッケージマネージャーによって異なります。Ubuntu のような Debian ベースのシステムでは、以下を使用します。

```bash
sudo apt update
sudo apt install samba
```

### Samba 共有の設定

Samba のメイン設定ファイルは `/etc/samba/smb.conf` にあります。このファイルは、どのディレクトリが共有されるか、誰がそれにアクセスできるか、およびその権限を決定します。デフォルトファイルにはコメントアウトされた多くの例が含まれており、優れたリファレンスとなります。

基本的な共有を設定する手順を見ていきましょう。

まず、テキストエディタで設定ファイルを開きます。

```bash
sudo nano /etc/samba/smb.conf
```

ファイルの一番下で、共有の新しいセクションを追加します。角括弧内の名前が、ネットワーク上で表示される共有名になります。

```ini
[myshare]
    comment = My First Samba Share
    path = /my/directory/to/share
    read only = no
    browsable = yes
```

次に、設定で指定したディレクトリを作成します。

```bash
mkdir -p /my/directory/to/share
```

最後に、Samba アクセス用の特定パスワードを設定する必要があります。Samba は独自のパスワードデータベースを維持しており、これはシステムのユーザーパスワードとは別物です。

```bash
sudo smbpasswd -a [username]
```

`[username]` をシステム上の既存の Linux ユーザーに置き換えてください。Samba アクセス用の新しいパスワードを作成するように求められます。

### Samba サービスの管理

`smb.conf` ファイルに変更を加えた後、変更を有効にするために Samba サービスを再起動する必要があります。

```bash
sudo service smbd restart
```

### Samba 共有へのアクセス

共有が設定されると、ネットワーク上のクライアントがそれにアクセスできます。

**Windows から：**
実行プロンプト (Win + R) またはファイルエクスプローラーを開き、ネットワークパスを入力します：`\HOST\sharename`。ここで `HOST` は Linux マシンの IP アドレスまたはホスト名です。

**Linux から：**
Samba パッケージには **smbclient** と呼ばれるコマンドラインツールが含まれており、これにより任意の**linux smb**または Windows 共有と対話できます。

```bash
smbclient //HOST/myshare -U username
```

接続後、`ls`、`get`、`put` などのコマンドを使用してファイルを管理できる `smb: \>` プロンプトが表示されます。

### Samba 共有のマウント

より永続的なアクセスを実現するために、ネットワーク共有をファイルシステムに直接マウントし、ローカルディレクトリのように見せることができます。

```bash
sudo mount -t cifs //SERVER/sharename /mnt/mountpoint -o user=username,pass=password
```

このコマンドは `cifs` ファイルシステムタイプを使用して、リモート共有をローカルのマウントポイントにアタッチします。

## Exercise

ご自身の Linux マシン上にシンプルな Samba 共有を設定してみてください。ディレクトリを作成し、`smb.conf`で設定し、同じマシンから`smbclient`を使用してアクセスを試み、設定をテストします。より実践的な練習のために、関連する Linux スキルと概念を練習できる包括的な[Linux 学習パス](https://labex.io/ja/learn/linux)を探ってみてください。

## Quiz Question

ファイル共有のために開発された、SMB の初期の方言であるプロトコルの名前は何ですか？大文字と小文字に注意して、英語で回答してください。

## Quiz Answer

CIFS
