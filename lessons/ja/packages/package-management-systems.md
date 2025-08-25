---
index: 6
lang: "ja"
title: "yum と apt"
meta_title: "yum と apt - パッケージ"
meta_description: "Linux パッケージ管理のために yum と apt を学びましょう。この初心者向けチュートリアルで、Debian/RPM システムにソフトウェアをインストール、削除、更新しましょう。今日から始めましょう！"
meta_keywords: "yum, apt, Linux パッケージ管理，apt チュートリアル，yum チュートリアル，Linux コマンド，初心者ガイド，パッケージインストール"
---

## Lesson Content

パッケージ管理のバットマンたち！これらのシステムには、パッケージのインストール、削除、変更を容易にするためのあらゆる機能が備わっており、パッケージの依存関係のインストールも含まれます。最も人気のある管理システムのうち 2 つは、**yum**と**apt**です。yum は Red Hat ファミリー専用であり、apt は Debian ファミリー専用です。

### リポジトリからパッケージをインストールする

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### パッケージを削除する

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### リポジトリのパッケージを更新する

パッケージをインストールおよび更新する前に、パッケージリポジトリを最新の状態に更新することは常に最善のプラクティスです。

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### インストールされているパッケージの情報を取得する

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

練習は完璧をもたらします！Linux パッケージ管理の理解を深めるための実践的なラボをいくつか紹介します。

1. **[Linux で YUM を使用してパッケージをクエリおよび更新する](https://labex.io/ja/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - YUM を使用して、RHEL ベースの Linux システムでソフトウェアパッケージを管理する練習をします。これには、リポジトリの検査、更新、探索が含まれます。
2. **[Linux でのソフトウェアインストール](https://labex.io/ja/labs/linux-software-installation-on-linux-18005)** - apt、dpkg の使用、.deb ファイルの処理など、Ubuntu システムでソフトウェアをインストールおよび管理するさまざまな方法を学びます。
3. **[パッケージのインストールと削除](https://labex.io/ja/labs/linux-installing-and-removing-packages-385380)** - `apt`を使用して、Debian ベースのシステムでシステムを更新し、パッケージをインストールおよび削除し、ソフトウェア構成を最適化する練習をします。

これらのラボは、実際のシナリオで概念を適用し、Linux パッケージ管理に自信を持つために役立ちます。

## Quiz Question

Debian システムでパッケージ情報を表示するために使用されるコマンドは何ですか？

## Quiz Answer

apt show
