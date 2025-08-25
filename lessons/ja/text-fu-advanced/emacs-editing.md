---
index: 12
lang: "ja"
title: "Emacs 編集"
meta_title: "Emacs 編集 - 高度なテキスト操作"
meta_description: "Emacs の編集の基本を学びましょう：テキストのナビゲート、カット、効率的なペースト。この初心者向けのガイドは、Linux で必須の Emacs コマンドを習得するのに役立ちます。"
meta_keywords: "Emacs, Emacs チュートリアル，Emacs コマンド，テキストエディタ，Linux エディタ，Emacs ナビゲーション，初心者 Emacs, Emacs ガイド"
---

## Lesson Content

### テキストナビゲーション

```
C-up arrow: move up one paragraph
C-down arrow: move down one paragraph
C-left arrow: move one word left
C-right arrow: move one word right
M->: move to the end of the buffer
```

テキストナビゲーションでは、Home、End、Page Up、Page Down、矢印キーなどの通常のテキストボタンが期待どおりに機能します。

### カット＆ペースト

Emacs でカット（キル）またはペースト（ヤンク）するには、まずテキストを選択できる必要があります。テキストを選択するには、カーソルをカットまたはペーストしたい場所に移動し、`C-space key`を押します。その後、ナビゲーションキーを使用して目的のテキストを選択できます。これで、次のようにカット＆ペーストできます。

```
C-w: cut
C-y: yank
```

## Exercise

練習は完璧を導きます！Linux のユーザーとグループ管理の理解を深めるための実践的なラボをいくつか紹介します。

1. **[useradd、usermod、および userdel を使用して Linux ユーザーアカウントを管理する](https://labex.io/ja/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 新しいアカウントの作成と保護から、変更および削除まで、ユーザー管理の完全なライフサイクルを練習します。
2. **[groupadd、usermod、および groupdel を使用して Linux グループを管理する](https://labex.io/ja/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 新しいグループの作成、ユーザーメンバーシップの変更、グループの削除など、グループ管理のためのコアコマンドラインユーティリティを実践的に体験します。
3. **[Linux でユーザーアカウントと Sudo 権限を設定する](https://labex.io/ja/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - パスワードポリシーの適用や管理権限の付与など、Linux システムのセキュリティを強化するためのユーザーアカウントと sudo 権限を管理する上で不可欠なテクニックを学びます。

これらのラボは、実際のシナリオで概念を適用し、Linux でのユーザーおよびグループ管理に自信を持つのに役立ちます。

## Quiz Question

バッファの最後に移動するにはどうすればよいですか？

## Quiz Answer

M->
