---
index: 6
lang: "ja"
title: "Setgid"
meta_title: "Setgid - パーミッション"
meta_description: "Linux SGID (Set Group ID) パーミッション、その仕組み、および変更方法について学びます。この重要な Linux セキュリティ概念を理解しましょう。"
meta_keywords: "Linux SGID, Set Group ID, Linux permissions, chmod g+s, Linux security, beginner Linux, Linux tutorial"
---

## Lesson Content

Set user ID パーミッションビットと同様に、Set Group ID (SGID) パーミッションビットがあります。このビットにより、プログラムはそのグループのメンバーであるかのように実行できます。

例を見てみましょう。

```bash
$ ls -l /usr/bin/wall
-rwxr-sr-x 1 root tty 19024 Dec 14 11:45 /usr/bin/wall
```

これで、パーミッションビットがグループパーミッションセットにあることがわかります。

### Modifying SGID

```bash
sudo chmod g+s myfile
sudo chmod 2555 myfile
```

SGID の数値表現は 2 です。

## Exercise

No exercises for this lesson.

## Quiz Question

SGID を表す数字は何ですか？

## Quiz Answer

2
