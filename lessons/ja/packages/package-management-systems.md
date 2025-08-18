---
lang: "ja"
title: "yum と apt"
meta_title: "yum と apt - パッケージ"
meta_description: "Linux パッケージ管理のための yum と apt を学びましょう。この初心者向けチュートリアルで、Debian/RPM システムでのソフトウェアのインストール、削除、更新を始めましょう。今日から始めましょう！"
meta_keywords: "yum, apt, Linux パッケージ管理，apt チュートリアル，yum チュートリアル，Linux コマンド，初心者ガイド，パッケージインストール"
---

## Lesson Content

ああ、パッケージ管理のバットマンたち！これらのシステムには、パッケージの依存関係のインストールを含め、パッケージのインストール、削除、変更を容易にするためのあらゆる機能が備わっています。最も人気のある 2 つの管理システムは、**yum**と**apt**です。yum は Red Hat ファミリー専用であり、apt は Debian ファミリー専用です。

### Install a package from a repository

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

### Remove a package

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### Updating packages for a repository

パッケージをインストールおよび更新する前に、パッケージリポジトリを最新の状態に更新しておくことが常に最善の方法です。

```bash
Debian: apt update; apt upgrade
RPM: yum update
```

### Get information about an installed package

```bash
Debian: apt show package_name
RPM: yum info package_name
```

## Exercise

これらのパッケージコマンドをそれぞれ実行し、受け取る出力を確認してください。

## Quiz Question

Debian システムでパッケージ情報を表示するために使用されるコマンドは何ですか？

## Quiz Answer

apt show
