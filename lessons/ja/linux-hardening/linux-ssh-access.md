---
lesson_id: "linux-ssh-access"
course_id: "linux-hardening"
lang: "ja"
order_index: 6
title: "SSH アクセス"
description: "SSH サーバーの識別、ユーザー認証、ログインを許可するポリシーの違いを学びます。"
meta_title: "SSH アクセス - Linux の堅牢化"
meta_description: "SSH サーバーの識別、ユーザー認証、ログインを許可するポリシーの違いを学びます。"
meta_keywords: "SSH アクセス, ホスト鍵, Linux の堅牢化, サイバーセキュリティ, Linux Journey"
---

保守で SSH を使う場合、接続の両端で確認が行われます。クライアントは、接続先が目的のサーバーであるかを確認します。サーバーは、そのアカウントにログインが許されているかを確認します。

## サーバーの識別情報を確認する

SSH サーバーは**ホスト鍵**を提示します。クライアントは、そのホストについて記録済みの識別情報と照合できます。鍵が予期せず変わった場合は、チームのホスト台帳や、信頼できる連絡経路で連絡を取った保守担当者など、承認済みの独立した情報源で新しい鍵を確かめます。

:::single-choice{#linux-ssh-access-unexpected-key} クライアントがサーバーのホスト鍵が変わったと表示しました。まず何を確認しますか？

::option[信頼できる情報源で、本来使われるはずの新しいホスト鍵を確認します。]{#linux-ssh-access-unexpected-key-b .correct explanation="その接続を信頼する前に、サーバーの識別情報を検証できます。"}
::option[ログインできるまでいくつかのユーザー名を試します。]{#linux-ssh-access-unexpected-key-a explanation="ユーザー名では、サーバーを識別できません。"}
::option[保存済みのホスト鍵をすべて削除して先に進みます。]{#linux-ssh-access-unexpected-key-c explanation="変更の理由が分かる前に、記録済みの識別情報を失うことになります。"}
:::

## ユーザーのアクセス権を確認する

クライアントはユーザー鍵を使い、アカウントを使う権限があることを証明できます。ホスト鍵はサーバーの識別に使います。サーバーのポリシーでは、受け付けるアカウントや認証方法を制限できます。この練習例では、`ops` が鍵認証でログインします。

:::single-choice{#linux-ssh-access-distinguish-keys} サーバーが ops のユーザー鍵を検証するとき、誰の認証を行っていますか？

::option[公開 Web ページの名前です。]{#linux-ssh-access-distinguish-keys-b explanation="Web コンテンツと SSH 認証は別の仕組みです。"}
::option[サーバーが自身の身元を証明しています。]{#linux-ssh-access-distinguish-keys-c explanation="その確認では、クライアントがホスト鍵を使います。"}
::option[ops としてログインしようとするクライアントです。]{#linux-ssh-access-distinguish-keys-a .correct explanation="ユーザー認証では、クライアントが使おうとしているアカウントを確認します。"}
:::

## 保守用の経路を確保する

承認済みの SSH ポリシー変更を行う前に、対象アカウントとアクセス方法について合意しておきます。別のテスト接続を使い、想定した方法でログインできるまで、確立済みの復旧経路を使える状態に保ちます。変更後も既存のセッションが残る一方、新規ログインが失敗する場合があります。

:::single-choice{#linux-ssh-access-test-new-login} ポリシー変更後も既存のセッションは開いたままです。保守担当者が引き続きログインできることを、どう確認しますか？

::option[ping の応答だけを確認します。]{#linux-ssh-access-test-new-login-a explanation="ネットワークから応答があっても、SSH 認証が成功するかは分かりません。"}
::option[想定したアカウントと方法で、承認済みの新規 SSH セッションを開始します。]{#linux-ssh-access-test-new-login-c .correct explanation="今後のログインに適用されるポリシーを直接確認できます。"}
::option[以前のセッションが何もしていない状態で残っていることを確認します。]{#linux-ssh-access-test-new-login-b explanation="そのセッションは以前の条件で認証されています。"}
:::

## まとめ

SSH で保守する際に、どの認証情報とアクセス条件を確認すべきか分かりました。

1. ホスト鍵でサーバーの識別情報を検証します。
2. サーバーの識別とユーザー認証の違いを理解します。
3. 変更後は承認済みの新規接続で確認します。
