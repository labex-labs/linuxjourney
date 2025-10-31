---
index: 5
lang: "ja"
title: "/etc/group"
meta_title: "/etc/group - ユーザー管理"
meta_description: "Linux の/etc/group ファイルを調査し、グループ管理を理解します。cat /etc/groupでグループデータを表示する方法を学び、GIDやユーザーリストを含む構造を理解します。このガイドでは、etc group linux ファイルの基本を網羅します。"
meta_keywords: "/etc/group, /etc/group linux, /etc/group ファイル linux, cat /etc/group, etc group linux, グループ管理，GID, Linux 権限，Linux グループ"
---

## Lesson Content

Linux では、複数のユーザーに対する権限管理はグループを使用することで効率化されます。このための中心となるファイルが `/etc/group` であり、システム上のグループとそのメンバーを定義します。

### /etc/group ファイルとは？

Linux の `/etc/group` ファイルは、すべてのユーザーグループのリストを含むプレーンテキストファイルです。各グループにはファイルやディレクトリに対する特定の権限を割り当てることができ、管理者は複数のユーザーのアクセス権を一度に効率的に管理できます。このファイルを理解することは、あらゆる `etc group linux` 環境における適切なユーザーおよび権限管理にとって極めて重要です。

### グループ情報の表示

このファイルの内容を確認するには、簡単なコマンドを使用できます。ターミナルで `cat /etc/group` を実行すると、システム上のすべてのグループ定義が表示されます。

```bash
$ cat /etc/group

root:*:0:pete
```

### /etc/group ファイルの構造

`/etc/passwd` ファイルと同様に、`/etc/group` ファイルの各行は単一のグループを表し、コロン（`:`）で区切られた 4 つのフィールドで構成されています。

1.  **グループ名**: グループの一意の名前。
2.  **グループパスワード**: このフィールドはレガシー機能であり、ほとんど使用されません。最新のシステムでは、グループパスワードの代わりに `sudo` のようなツールが特権昇格に使用されます。通常、アスタリスク（`*`）や 'x' のようなプレースホルダーが表示されます。
3.  **グループ ID (GID)**: グループの一意の数値識別子。システムは内部的にグループ名ではなく GID を使用することがよくあります。
4.  **ユーザーリスト**: このグループのメンバーであるユーザー名のカンマ区切りリスト。

例の `root:*:0:pete` では、グループ名は `root`、パスワードはなく、GID は `0` であり、ユーザー `pete` がメンバーです。

## Exercise

練習あるのみです！Linux のユーザーおよびグループ管理の理解を深めるための実践的なラボを以下に示します。

1.  **[useradd、usermod、userdel を使用した Linux ユーザーアカウントの管理](https://labex.io/ja/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 新しいアカウントの作成と保護から、変更および削除まで、ユーザー管理のライフサイクル全体を練習します。
2.  **[groupadd、usermod、groupdel を使用した Linux グループの管理](https://labex.io/ja/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - `groupadd`、`usermod`、`groupdel` を含む、グループ管理のためのコアコマンドラインユーティリティに関する実践的な経験を積みます。
3.  **[新しいユーザーとグループの追加](https://labex.io/ja/labs/linux-add-new-user-and-group-17987)** - 新しいユーザーアカウントの作成、カスタムグループの設定、グループメンバーシップの管理を通じて、サーバー環境への新しいチームメンバーの追加をシミュレートします。

これらのラボは、概念を実際のシナリオに適用し、Linux のユーザーおよびグループ管理に対する自信を構築するのに役立ちます。

## Quiz Question

root の GID は何ですか？

## Quiz Answer

0
