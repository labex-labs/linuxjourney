---
title: "/etc/group"
description: "Linux の/etc/group ファイルについて学び、グループ管理、GID、ユーザー権限を理解します。初心者向けの必須の Linux グループファイルチュートリアル。"
keywords: "/etc/group, Linux groups, group management, GID, Linux permissions, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

ユーザー管理で使用されるもう 1 つのファイルは、`/etc/group`ファイルです。このファイルは、異なる権限を持つ異なるグループを可能にします。

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

`groups`コマンドを実行してください。何が見えますか？

## Quiz Question

root の GID は何ですか？

## Quiz Answer

0
