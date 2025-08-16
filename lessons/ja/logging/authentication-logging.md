---
title: "認証ロギング"
description: "Linux の認証ロギングについて、/var/log/auth.log を使って学びましょう。この重要なガイドで、ユーザーログインを理解し、アクセス問題をトラブルシューティングしましょう。"
keywords: "Linux 認証，auth.log, Linux ロギング，ユーザーログイン，Linux セキュリティ，初心者，チュートリアル，ガイド"
---

## Lesson Content

認証ロギングは、ログインに問題がある場合に確認すると非常に役立ちます。

### /var/log/auth.log

このファイルには、ユーザーログインや使用された認証方法など、システム認証ログが含まれています。

サンプルスニペット：

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

ログインに数回失敗した後、成功するログインを試行してください。その後、何が起こったかを確認するために `/var/log/auth.log` ファイルを調べます。

## Quiz Question

ユーザー認証にはどのログファイルが使用されますか？

## Quiz Answer

auth.log
