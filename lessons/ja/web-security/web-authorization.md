---
lesson_id: "web-authorization"
course_id: "web-security"
lang: "ja"
order_index: 6
title: "認可"
description: "認証済みユーザーのリクエストを、アプリケーションのアクセスポリシーと照合する方法を学びます。"
meta_title: "認可 - Web セキュリティ"
meta_description: "認証済みユーザーのリクエストを、アプリケーションのアクセスポリシーと照合する方法を学びます。"
meta_keywords: "認可, アクセスポリシー, Web セキュリティ, サイバーセキュリティ, Linux Journey"
---

ユーザーはログインできても、特定の操作を行う権限がない場合があります。**認可**とは、あるアカウントが対象のリソースに対して操作を行えるかを判断することです。

## ポリシーを読む

**ロール**とは、名前を付けた権限のまとまりです。次はプレビューサービスの練習用ポリシーです。

```text
Role       View published page   Edit draft
Reader    Yes                   No
Editor    Yes                   Yes
```

ユーザーのロールに対応する行と、要求された操作に対応する列を見ます。編集者は公開済みページを閲覧し、下書きを編集できます。閲覧者は公開済みページを閲覧できます。

:::single-choice{#web-authorization-read-policy} ログイン済みの閲覧者が下書きの編集を要求しました。表ではどうなっていますか？

::option[Reader にはその操作が許可されていません。]{#web-authorization-read-policy-b .correct explanation="Reader の行では、Edit draft の列が No です。"}
::option[ログインしているアカウントなら、どれでも操作できます。]{#web-authorization-read-policy-a explanation="要求された操作には、ロールごとの設定があります。"}
::option[編集権限を得るには HTTPS に切り替える必要があります。]{#web-authorization-read-policy-c explanation="通信を保護しても、アプリケーション内の権限は付与されません。"}
:::

## 操作の対象を確認する

多くのシステムでは、リソースごとに異なる権限を設定できます。例えば編集者でも、自分のプロジェクトでは下書きを編集でき、別のプロジェクトではページを閲覧するだけの場合があります。確認する際は、操作と対象リソースの両方を特定します。

:::single-choice{#web-authorization-target-resource} Maya はプロジェクト A を編集できます。プロジェクト B も編集できるかを判断するには何を確認しますか？

::option[プロジェクト A のタイトルです。]{#web-authorization-target-resource-b explanation="タイトルからは別のプロジェクトの権限は分かりません。"}
::option[Maya がログインに成功したことです。]{#web-authorization-target-resource-c explanation="認証では Maya のアカウントを確認します。リソースへのアクセスは別途判断します。"}
::option[Maya とプロジェクト B に適用される権限ポリシーです。]{#web-authorization-target-resource-a .correct explanation="先に確認した権限は、特定のリソースを対象としていました。"}
:::

## サービス側で確認する

ユーザーインターフェースでは、閲覧者に編集ボタンを表示しないようにできます。サーバー側でも、リクエストを受けるたびにポリシーを適用する必要があります。練習用サービスで承認された通常の操作を行い、想定どおりに許可と拒否が行われるかを確認します。

:::single-choice{#web-authorization-decision-location} あるアプリケーションでは、閲覧者に「編集」ボタンが表示されません。アクセス制御は、ほかにどこで適用する必要がありますか？

::option[ボタンの表示を決めるときにブラウザーだけで適用します。]{#web-authorization-decision-location-a explanation="ブラウザーは画面表示を制御できます。受け取ったリクエストを許可するかはサービスが判断します。"}
::option[要求された操作を受け取るサービスで適用します。]{#web-authorization-decision-location-c .correct explanation="サービスは、アカウント、操作、対象リソースを毎回確認できます。"}
::option[ロールを一覧表示するページだけで適用します。]{#web-authorization-decision-location-b explanation="ロール名を表示しても、制限された操作は防げません。"}
:::

## まとめ

アプリケーションがアクセスをどう判断するかを考えられるようになりました。

1. アカウントのロールを、要求された操作に照らし合わせます。
2. 確認には、具体的な対象リソースも含めます。
3. サービスが受け取ったリクエストにポリシーを適用することを確かめます。
