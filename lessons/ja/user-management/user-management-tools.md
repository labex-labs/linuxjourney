---
lang: "ja"
title: "ユーザー管理ツール"
description: "Linux のユーザー管理を学びましょう：useradd、userdel、passwd コマンドを使って、ユーザーの追加、削除、パスワードの変更を行います。この初心者向けのガイドで始めましょう！"
keywords: "Linux ユーザー管理，adduser, userdel, passwd, Linux チュートリアル，初心者 Linux, ユーザーアカウント，Linux コマンド"
---

## Lesson Content

ほとんどのエンタープライズ環境では、ユーザー、アカウント、パスワードを管理するために管理システムを使用します。しかし、単一のマシンコンピュータでは、ユーザーを管理するために実行できる便利なコマンドがあります。

### Adding Users

`adduser` または `useradd` コマンドを使用できます。`adduser` コマンドには、ホームディレクトリの作成など、より便利な機能が含まれています。新しいユーザーを追加するための設定ファイルがあり、デフォルトユーザーに割り当てたいものに応じてカスタマイズできます。

```bash
sudo useradd bob
```

上記のコマンドは、bob の `/etc/passwd` にエントリを作成し、デフォルトグループを設定し、`/etc/shadow` ファイルにエントリを追加することを確認できます。

### Removing Users

ユーザーを削除するには、`userdel` コマンドを使用できます。

```bash
sudo userdel bob
```

これは基本的に、`useradd` によって行われたファイル変更を元に戻すために最善を尽くします。

### Changing Passwords

```bash
passwd bob
```

これにより、自分自身または他のユーザー（root の場合）のパスワードを変更できます。

## Exercise

新しいユーザーを作成し、そのパスワードを変更して、新しいユーザーとしてログインしてください。

## Quiz Question

パスワードを変更するために使用されるコマンドは何ですか？

## Quiz Answer

passwd
