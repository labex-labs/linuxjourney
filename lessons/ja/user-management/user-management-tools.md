---
index: 6
lang: "ja"
title: "ユーザー管理ツール"
meta_title: "ユーザー管理ツール - ユーザー管理"
meta_description: "Linux ユーザー管理を学ぶ：useradd、userdel、passwd コマンドでユーザーの追加、削除、パスワード変更を行います。この初心者向けガイドで始めましょう！"
meta_keywords: "Linux ユーザー管理，adduser, userdel, passwd, Linux チュートリアル，初心者 Linux, ユーザーアカウント，Linux コマンド"
---

## Lesson Content

ほとんどのエンタープライズ環境では、ユーザー、アカウント、パスワードを管理するために管理システムを使用します。しかし、単一のマシンコンピュータでは、ユーザーを管理するために実行できる便利なコマンドがあります。

### ユーザーの追加

`adduser` または `useradd` コマンドを使用できます。`adduser` コマンドには、ホームディレクトリの作成など、より便利な機能が含まれています。新しいユーザーを追加するための設定ファイルがあり、デフォルトのユーザーに何を割り当てるかに応じてカスタマイズできます。

```bash
sudo useradd bob
```

上記のコマンドは、bob の `/etc/passwd` にエントリを作成し、デフォルトのグループを設定し、`/etc/shadow` ファイルにエントリを追加します。

### ユーザーの削除

ユーザーを削除するには、`userdel` コマンドを使用します。

```bash
sudo userdel bob
```

これは基本的に、`useradd` によって行われたファイル変更を元に戻すために最善を尽くします。

### パスワードの変更

```bash
passwd bob
```

これにより、自分自身または他のユーザー（root の場合）のパスワードを変更できます。

## Exercise

習うより慣れろ！ここでは、Linux でのユーザーおよびアカウント管理の理解を深めるための実践的な演習をいくつか紹介します。

1. **[useradd、usermod、および userdel で Linux ユーザーアカウントを管理する](https://labex.io/ja/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 新しいアカウントの作成と保護から、変更と削除まで、ユーザー管理の完全なライフサイクルを練習します。
2. **[groupadd、usermod、および groupdel で Linux グループを管理する](https://labex.io/ja/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - グループの追加、変更、削除を含む、グループ管理のためのコアコマンドラインユーティリティの実践的な経験を積みます。
3. **[Linux でユーザーアカウントと Sudo 権限を設定する](https://labex.io/ja/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Linux システムのセキュリティを強化するために、ユーザーアカウントと sudo 権限を管理するための重要なテクニックを学びます。

これらの演習は、実際のシナリオで概念を適用し、Linux のユーザーおよびグループ管理に自信を持つのに役立ちます。

## Quiz Question

パスワードを変更するために使用されるコマンドは何ですか？

## Quiz Answer

passwd
