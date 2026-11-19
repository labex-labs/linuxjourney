---
lesson_id: "linux-least-privilege"
course_id: "linux-hardening"
lang: "ja"
order_index: 3
title: "最小権限"
description: "サービスの作業に必要なファイル権限と管理権限の選び方を学びます。"
meta_title: "最小権限 - Linux の堅牢化"
meta_description: "サービスの作業に必要なファイル権限と管理権限の選び方を学びます。"
meta_keywords: "最小権限, ファイル権限, Linux の堅牢化, サイバーセキュリティ, Linux Journey"
---

**最小権限**とは、作業に必要な範囲の権限をアカウントに与えることです。まず、どんな操作が必要かを考えます。あるファイルを読む、別のファイルに書き込むといった操作は必要でも、管理作業は不要かもしれません。

## 作業に合わせて権限を選ぶ

Web ワーカーは `index.html` を読む必要があります。ファイルを更新するのはデプロイ用アカウントです。この二つの作業には異なる権限を設定できます。ワーカーには読み取り、デプロイ用アカウントには書き込みを許可します。

:::single-choice{#linux-least-privilege-read-only-page} この例で、ワーカーにはページへのどの権限が必要ですか？

::option[読み取り権限です。]{#linux-least-privilege-read-only-page-a .correct explanation="ファイルを配信するには、その内容を読む必要があります。"}
::option[書き込み権限です。]{#linux-least-privilege-read-only-page-b explanation="ページを変更するのはデプロイ用アカウントです。"}
::option[無関係なサービスを管理する権限です。]{#linux-least-privilege-read-only-page-c explanation="Web ワーカーの担当範囲外の作業です。"}
:::

## パス全体の権限を確認する

ファイルの権限は確認項目の一つです。Linux では、そのファイルに至る各ディレクトリを通過する権限も必要です。ディレクトリの実行権限があると、名前が分かっている項目に向けてそのディレクトリをたどれます。ファイル自体に読み取り権限があっても、途中のディレクトリを通過できなければワーカーはファイルにアクセスできません。

:::single-choice{#linux-least-privilege-path-boundary} ファイルのモードではワーカーが index.html を読めますが、親ディレクトリに入れません。何を見直しますか？

::option[ページのファイルサイズが大きくなっているかを確認します。]{#linux-least-privilege-path-boundary-a explanation="サイズはディレクトリへのアクセス権限に影響しません。"}
::option[誰でもページを書き換えられるようにするかを検討します。]{#linux-least-privilege-path-boundary-c explanation="書き込み権限を与えても、パスをたどれない問題は解決しません。"}
::option[そのワーカーにディレクトリの通過権限があるかを確認します。]{#linux-least-privilege-path-boundary-b .correct explanation="ファイルへの権限と、そのパスをたどるための権限の両方が必要です。"}
:::

## 特別な操作を制限する

`sudo` などの管理ツールを使うと、許可されたユーザーが特定の保守作業を実行できます。どの操作を誰に許可し、新しいアクセスをどう検証するかを決めます。同じポリシーで、許可した保守作業は行えて、無関係な管理操作は引き続き制限されることを確認します。

:::single-choice{#linux-least-privilege-policy-test} 保守担当のロールでは、サービスの状態を確認できる必要があります。想定した権限を検証するのに最適な計画はどれですか？

::option[すべての管理コマンドが成功することを確認します。]{#linux-least-privilege-policy-test-a explanation="その権限は、記載された作業範囲を超えています。"}
::option[状態を確認でき、無関係な特権操作は引き続き制限されることを確認します。]{#linux-least-privilege-policy-test-c .correct explanation="必要なアクセスと、想定した権限の境界をともに検証できます。"}
::option[ユーザー名が存在することだけを確認します。]{#linux-least-privilege-policy-test-b explanation="アカウントが存在しても、その権限までは分かりません。"}
:::

## まとめ

作業ごとに必要な最小限のアクセスを判断できるようになりました。

1. 読み取り、書き込み、管理操作を区別します。
2. パス上の各ディレクトリを通過できるかを確認します。
3. ロールで許可される操作と制限される操作を両方確認します。
