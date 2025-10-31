---
index: 6
lang: "ja"
title: "yum と apt"
meta_title: "yum と apt - パッケージ管理"
meta_description: "yum と apt の主な違いを探ります。このガイドでは、RPM ベースおよび Debian ベースの Linux システムでのパッケージのインストール、削除、更新における yum と apt の使用方法を解説します。"
meta_keywords: "yum vs apt, yum apt, Linux パッケージ管理，apt, yum, Debian, Red Hat, パッケージインストール，パッケージ更新，Linux コマンド"
---

## Lesson Content

パッケージマネージャーは、Linux においてソフトウェアのインストール、更新、削除を簡素化するための不可欠なツールです。依存関係を自動的に処理し、必要なすべてのライブラリとコンポーネントが正しくインストールされることを保証します。最も著名なパッケージ管理システムは **yum** と **apt** の 2 つです。

### Yum vs Apt

これら 2 つのシステム間の主な違いは、それらが使用される Linux ディストリビューションにあります。`yum` (Yellowdog Updater, Modified) パッケージマネージャーは、Red Hat、CentOS、Fedora などの RPM ベースのディストリビューションで使用されます。対照的に、`apt` (Advanced Package Tool) は、Ubuntu を含む Debian ベースのディストリビューションの標準です。`yum` も `apt` も同じ目標を達成しますが、コマンドの構文が異なります。

### パッケージのインストールと削除

リポジトリから新しいソフトウェアをインストールするには、`install` コマンドを使用します。

```bash
Debian: $ apt install package_name
RPM: $ yum install package_name
```

パッケージを削除する場合も、コマンドは簡単です。`apt` は `remove` を使用し、`yum` は `erase` を使用します。

```bash
Debian: $ apt remove package_name
RPM: $ yum erase package_name
```

### パッケージの更新と検査

ソフトウェアのインストールやアップグレードを行う前に、ローカルのパッケージインデックスを更新することがベストプラクティスです。これにより、利用可能な最新バージョンを取得できます。

Debian システムの場合、これは 2 段階のプロセスです。`apt update` がパッケージリストを更新し、`apt upgrade` が新しいバージョンをインストールします。RPM システムの場合、`yum update` は単一のコマンドで両方の操作を処理します。

```bash
Debian: $ apt update; apt upgrade
RPM: $ yum update
```

特定のパッケージに関する詳細情報を取得する必要がある場合は、以下のコマンドを使用して、バージョン、サイズ、説明などの情報を表示できます。

```bash
Debian: $ apt show package_name
RPM: $ yum info package_name
```

## Exercise

練習あるのみです！Linux パッケージ管理の理解を深めるための実践的なラボを以下に示します。

1.  **[YUM を使用した Linux でのパッケージの照会と更新](https://labex.io/ja/labs/rhel-query-and-update-packages-with-yum-in-linux-590869)** - YUM を使用して RHEL ベースの Linux システムでソフトウェアパッケージを管理する練習をします。これには、パッケージの検査、更新、リポジトリの探索が含まれます。
2.  **[Linux でのソフトウェアインストール](https://labex.io/ja/labs/linux-software-installation-on-linux-18005)** - apt、dpkg の使用、および.deb ファイルの処理を含む、Ubuntu システムでソフトウェアをインストールおよび管理するためのさまざまな方法を学びます。
3.  **[パッケージのインストールと削除](https://labex.io/ja/labs/linux-installing-and-removing-packages-385380)** - `apt` を使用して Debian ベースのシステムでシステムの更新、パッケージのインストールと削除、ソフトウェア構成の最適化を練習します。

これらのラボは、実際のシナリオで概念を適用し、Linux パッケージ管理に対する自信を築くのに役立ちます。

## Quiz Question

Debian システムでパッケージ情報を表示するために使用されるコマンドは何ですか？大文字と小文字を区別することに注意して、英語で回答してください。

## Quiz Answer

apt show
