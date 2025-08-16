---
lang: "ja"
title: "rpm と dpkg"
description: "rpm コマンドと dpkg コマンドを使用して、パッケージのインストール、削除、リスト表示を行う方法を学びます。.deb ファイルと.rpm ファイルの直接パッケージ管理を理解します。Linux の学習を始めましょう！"
keywords: "rpm, dpkg, Linux パッケージ管理，.deb, .rpm, Linux チュートリアル，初心者向けガイド，パッケージのインストール"
---

## Lesson Content

このコースのほとんどはパッケージ管理システム（パッケージ管理のバットマン）についてですが、ロビンたちのことも忘れてはなりません。彼らは非常に便利で信頼性がありますが、あの素晴らしいバットモービルやユーティリティベルトは持っていません。

`.exe` が単一の実行可能ファイルであるように、`.deb` と `.rpm` も同様です。通常、パッケージリポジトリを使用している場合はこれらを見ることはありませんが、パッケージを直接ダウンロードする場合は、これらの一般的な形式で入手することがほとんどです。明らかに、これらはそれぞれのディストリビューション専用です。`.deb` は Debian ベース、`.rpm` は Red Hat ベースです。

これらの直接パッケージをインストールするには、パッケージ管理コマンドである `rpm` と `dpkg` を使用できます。これらのツールはパッケージファイルをインストールするために使用されますが、パッケージの依存関係はインストールしません。したがって、パッケージに 10 個の依存関係がある場合、それらのパッケージを個別にインストールし、次にそれらの依存関係をインストールするといった具合になります。ご覧のとおり、これが後で説明する本格的な管理システムが生まれた理由の 1 つです。

これらのツールのいずれかを使用してパッケージをインストール、クエリ、または検証する必要がある countless times があることを覚えておいてください。したがって、これらのコマンドを覚えておきましょう。

### Install a package

```bash
Debian: $ dpkg -i some_deb_package.deb
RPM: $ rpm -i some_rpm_package.rpm
```

`i` は install を意味します。より長い形式の `--install` も使用できます。

### Remove a package

```bash
Debian: $ dpkg -r some_deb_package.deb
RPM: $ rpm -e some_rpm_package.rpm
```

Debian: `r` for remove
RPM: `e` for erase

### List installed packages

```bash
Debian: $ dpkg -l
RPM: $ rpm -qa
```

Debian: `l` for list
RPM: `q` for query and `a` for all

## Exercise

Google Chrome のように、システムにインストールしたいプログラムを見つけて、これらのコマンドのいずれかを使用してインストールしてください。

## Quiz Question

`.deb` ファイル用のパッケージ管理ツールは何ですか？

## Quiz Answer

dpkg
