---
lesson_id: "web-authentication"
course_id: "web-security"
lang: "ja"
order_index: 4
title: "認証"
description: "Web サービスがユーザーの本人確認を行う方法と、二つの要素が異なる証拠になる理由を学びます。"
meta_title: "認証 - Web セキュリティ"
meta_description: "Web サービスがユーザーの本人確認を行う方法と、二つの要素が異なる証拠になる理由を学びます。"
meta_keywords: "認証, 認証要素, Web セキュリティ, サイバーセキュリティ, Linux Journey"
---

**認証**とは、ユーザーが名乗った身元を確認する手順です。ログインフォームでは、アカウント名とパスワードの入力を求めることがあります。名前はどのアカウントかを示し、パスワードはサービスが検証できる証拠になります。

## どのアカウントを使おうとしているかを確認する

ユーザーがアカウント名 `alex` を入力したとします。この名前を知っていれば、誰でも入力できます。サービスはそのアカウントの情報とポリシーに従い、提出された証拠を検証します。

:::single-choice{#web-authentication-username-claim} ユーザーがアクセスしようとしているアカウントを示す入力はどれですか？

::option[パスワードの確認結果です。]{#web-authentication-username-claim-a explanation="これは、ユーザーが名乗った身元を受け入れるかどうかの判断材料です。"}
::option[アカウント名です。]{#web-authentication-username-claim-b .correct explanation="サービスに、どのアカウントについて本人確認するかを伝えます。"}
::option[トップページの応答形式です。]{#web-authentication-username-claim-c explanation="コンテンツの種類は、ログインするアカウントとは無関係です。"}
:::

## 認証要素を比較する

**認証要素**とは、本人確認に使う証拠の種類です。パスワードは、ユーザーが知っている情報です。登録済みのセキュリティキーは、ユーザーが持っているものに基づく証拠を提供します。パスワードと別に登録されたキーを使うと、二種類の証拠が得られます。

:::single-choice{#web-authentication-independent-factors} 知っている情報と持っているものを組み合わせる例はどれですか？

::option[パスワードと登録済みのセキュリティキーです。]{#web-authentication-independent-factors-a .correct explanation="一方は知識を、もう一方はキーを使えることを確認します。"}
::option[パスワードと、別に覚えたパスワードです。]{#web-authentication-independent-factors-b explanation="どちらも、ユーザーが知っている情報です。"}
::option[ユーザー名とページのタイトルです。]{#web-authentication-independent-factors-c explanation="これらの名前は、本人であることを示す証拠にはほとんどなりません。"}
:::

## 認証の成功が意味すること

証拠を確認した後に、サービスはユーザーのセッションを開始できます。認証に成功すると、サービスはどのアカウントがログインしたかを確定します。そのアカウントが何をできるかは、リソースごとのリクエストにアクセスルールを適用して判断します。

:::single-choice{#web-authentication-auth-limit} あるアカウントがログインに成功し、管理者用のページを要求しました。次に何をするべきですか？

::option[ログイン済みのアカウントにはすべて自動でページを返します。]{#web-authentication-auth-limit-a explanation="そのページに必要な権限もアカウントに付与されている必要があります。"}
::option[最初のページのタイトルでアクセスを決めます。]{#web-authentication-auth-limit-b explanation="タイトルではユーザーの権限は分かりません。"}
::option[アプリケーションで、そのリソースに対するアカウントの権限を確認します。]{#web-authentication-auth-limit-c .correct explanation="本人確認とリソースへのアクセス判定では、確かめる内容が異なります。"}
:::

## まとめ

認証の結果から何が分かるかを説明できるようになりました。

1. ユーザーが名乗った身元と、その証拠を区別します。
2. 二つの異なる種類の認証要素を見分けます。
3. リソースごとのアクセス判断には、サービスの認可ポリシーを使います。
