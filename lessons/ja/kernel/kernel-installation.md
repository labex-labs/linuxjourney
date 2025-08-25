---
index: 4
lang: "ja"
title: "カーネルのインストール"
meta_title: "カーネルのインストール - カーネル"
meta_description: "Linux カーネルのインストールと管理方法を学びましょう。`uname -r`コマンドと apt コマンドを使用して、カーネルバージョンを発見しましょう。Linux カーネルの旅を始めましょう！"
meta_keywords: "Linux kernel, install kernel, uname -r, apt dist-upgrade, kernel management, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

さて、退屈な話はこれくらいにして、実際にカーネルをインストールして変更する方法について話しましょう。システムには複数のカーネルをインストールできます。ブートプロセスのレッスンを覚えていますか？GRUB メニューで、どのカーネルを起動するかを選択できます。

システムにインストールされているカーネルのバージョンを確認するには、次のコマンドを使用します。

```bash
$ uname -r
3.19.0-43-generic
```

`uname`コマンドはシステム情報を表示します。`-r`オプションはカーネルリリースバージョンを表示します。

Linux カーネルはさまざまな方法でインストールできます。ソースパッケージをダウンロードしてソースからコンパイルするか、パッケージ管理ツールを使用してインストールできます。

```bash
sudo apt install linux-generic-lts-vivid
```

そして、インストールしたカーネルで再起動するだけです。簡単でしょう？まあ、ある程度は。`linux-headers`、`linux-image-generic`などの他の Linux パッケージもインストールする必要があります。バージョン番号を指定することもできるので、上記のコマンドは次のようになります。**`sudo apt install 3.19.0-43-generic`**

あるいは、更新されたカーネルバージョンが必要な場合は、`dist-upgrade`を使用するだけです。これはシステム上のすべてのパッケージをアップグレードします。

```bash
sudo apt dist-upgrade
```

さまざまなカーネルバージョンがあります。一部は LTS（Long Term Support）として使用され、一部は最新かつ最高のものです。カーネルバージョン間で互換性が大きく異なる場合があるため、さまざまなカーネルを試してみることをお勧めします。

## Exercise

練習は完璧を導きます！Linux カーネル管理と関連するシステム管理タスクの理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux で GRUB2 ブートメニューをカスタマイズする](https://labex.io/ja/labs/comptia-customize-the-grub2-boot-menu-in-linux-590859)** - 複数のカーネルバージョンを管理し、起動するカーネルを選択する際に不可欠な GRUB2 ブートメニューの変更を練習します。
2. **[Linux でカーネルモジュールを管理する](https://labex.io/ja/labs/comptia-manage-kernel-modules-in-linux-590865)** - カーネルモジュールを一覧表示、検査、ロード、アンロードする方法を学びます。これはカーネル管理の基本的な側面であり、ハードウェアがシステムとどのように相互作用するかを理解するのに役立ちます。
3. **[Linux でのソフトウェアインストール](https://labex.io/ja/labs/linux-software-installation-on-linux-18005)** - パッケージマネージャーの使用を含む、ソフトウェアをインストールおよび管理するさまざまな方法の実践的な経験を積みます。これはカーネルをインストールおよび更新する一般的な方法です。

これらの演習は、カーネル管理、ブートプロセス、パッケージ管理の概念を実際のシナリオに適用し、システム管理の自信を築くのに役立ちます。

## Quiz Question

システムのカーネルバージョンを確認するにはどうすればよいですか？

## Quiz Answer

uname -r
