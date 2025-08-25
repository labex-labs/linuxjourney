---
index: 6
lang: "ja"
title: "Setgid"
meta_title: "Setgid - パーミッション"
meta_description: "Linux SGID（Set Group ID）パーミッション、その仕組み、および変更方法について学びます。この重要な Linux セキュリティ概念を理解しましょう。"
meta_keywords: "Linux SGID, Set Group ID, Linux パーミッション，chmod g+s, Linux セキュリティ，初心者 Linux, Linux チュートリアル"
---

## Lesson Content

Set user ID パーミッションビットと同様に、Set Group ID (SGID) パーミッションビットがあります。このビットにより、プログラムはそのグループのメンバーであるかのように実行できます。

例を見てみましょう。

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

これで、パーミッションビットがグループパーミッションセットにあることがわかります。

### SGID の変更

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

SGID の数値表現は 2 です。

## Exercise

練習は完璧をもたらします！Linux のユーザー、グループ、ファイルパーミッションの理解を深めるための実践的な演習をいくつか紹介します。

1. **[Linux ユーザー、グループ、ファイルパーミッション](https://labex.io/ja/labs/linux-linux-user-group-and-file-permissions-18002)** - ユーザーの作成と管理、グループメンバーシップの探索、ファイルパーミッションの理解、ファイル所有権の操作など、Linux の基本的なユーザーおよびグループ管理の概念を学びます。
2. **[新しいユーザーとグループの追加](https://labex.io/ja/labs/linux-add-new-user-and-group-17987)** - 新しいユーザーアカウントの作成、カスタムグループの設定、グループメンバーシップの管理を練習し、実際のシステム管理タスクをシミュレートします。

これらの演習は、実際のシナリオで概念を適用し、Linux のパーミッションとユーザー管理に自信をつけるのに役立ちます。

## Quiz Question

SGID を表す数字は何ですか？

## Quiz Answer

2
