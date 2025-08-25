---
index: 5
lang: "ja"
title: "/etc/group"
meta_title: "/etc/group - ユーザー管理"
meta_description: "Linux の/etc/group ファイルについて学び、グループ管理、GID、ユーザー権限を理解します。初心者向けの必須 Linux グループファイルチュートリアル。"
meta_keywords: "/etc/group, Linux グループ，グループ管理，GID, Linux 権限，Linux チュートリアル，初心者向け Linux, Linux ガイド"
---

## Lesson Content

ユーザー管理で使用されるもう 1 つのファイルは、`/etc/group`ファイルです。このファイルは、異なる権限を持つ異なるグループを許可します。

```bash
$ cat /etc/group

root:*:0:pete
```

`/etc/passwd`ファイルと非常によく似ており、`/etc/group`のフィールドは次のとおりです。

1. グループ名
2. グループパスワード - グループパスワードを設定する必要はありません。`sudo`のような昇格された権限を使用するのが標準です。デフォルト値としてアスタリスク（`*`）が配置されます。
3. グループ ID (GID)
4. ユーザーリスト - 特定のグループに入れたいユーザーを手動で指定できます

## Exercise

習うより慣れろ！Linux のユーザーとグループ管理の理解を深めるための実践的な演習をいくつか紹介します。

1. **[useradd、usermod、および userdel を使用した Linux ユーザーアカウントの管理](https://labex.io/ja/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 新しいアカウントの作成と保護から、変更と削除まで、ユーザー管理の完全なライフサイクルを練習します。
2. **[groupadd、usermod、および groupdel を使用した Linux グループの管理](https://labex.io/ja/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - `groupadd`、`usermod`、および`groupdel`を含む、グループ管理のための主要なコマンドラインユーティリティの実践的な経験を積みます。
3. **[新しいユーザーとグループの追加](https://labex.io/ja/labs/linux-add-new-user-and-group-17987)** - 新しいユーザーアカウントの作成、カスタムグループの設定、グループメンバーシップの管理により、新しいチームメンバーをサーバー環境に追加するシミュレーションを行います。

これらの演習は、実際のシナリオで概念を適用し、Linux のユーザーとグループ管理に自信を持つのに役立ちます。

## Quiz Question

root の GID は何ですか？

## Quiz Answer

0
