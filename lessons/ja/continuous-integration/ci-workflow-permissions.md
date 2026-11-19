---
lesson_id: "ci-workflow-permissions"
course_id: "continuous-integration"
lang: "ja"
order_index: 7
title: "ワークフローの権限"
description: "日常的な CI チェックに、必要なリポジトリの権限だけを与える方法を学びます。"
meta_title: "ワークフローの権限 - 継続的インテグレーション"
meta_description: "日常的な CI チェックに、必要なリポジトリの権限だけを与える方法を学びます。"
meta_keywords: "ワークフローの権限, 読み取り, 継続的インテグレーション, DevOps, Linux Journey"
---

CI ジョブはコマンドを実行でき、認証情報を受け取る場合もあります。**権限**は、その認証情報で何を読み取ったり変更したりできるかを決めます。ページのチェックだけを行うジョブなら、通常はソースファイルの読み取り権限で足ります。

## チェックに読み取り権限を与える

この GitHub Actions の設定では、ワークフローに標準で付与されるトークンを、リポジトリの内容の読み取りに限定します。

```yaml
permissions:
  contents: read
```

チェックアウトとローカルのテストでは、リポジトリを読み取れます。パッケージを公開するジョブには、別のリソースに対する別の操作権限が必要です。公開の権限は、それを必要とするジョブだけに与えます。

:::single-choice{#ci-workflow-permissions-choose-permission} あるジョブではページを読み、grep を実行します。リポジトリの内容に対して、どの権限が必要ですか？

::option[テスト結果をターミナルに出力するので、書き込み権限です。]{#ci-workflow-permissions-choose-permission-a explanation="ターミナルへの出力に、リポジトリの内容を変更する権限は必要ありません。"}
::option[読み取り権限です。]{#ci-workflow-permissions-choose-permission-c .correct explanation="ジョブはリポジトリの内容を取得できればよく、書き換える操作はありません。"}
::option[ソースが Git リポジトリにあるので、書き込み権限です。]{#ci-workflow-permissions-choose-permission-b explanation="このチェックには、ソースファイルの読み取りで十分です。"}
:::

## 秘密情報を扱う

非公開のトークンなどの機密値を**シークレット**と呼びます。承認済みのジョブで必要になった場合は、プラットフォームのシークレット管理機能を使います。一般的なページ設定とシークレットは分けて管理します。ローカルのサンプルを定期的にチェックするだけなら、公開用の認証情報を使わずに実行できるようにします。

:::single-choice{#ci-workflow-permissions-secret-needed} アクセスを制限したシークレット管理機能で扱うべきものはどれですか？

::option[パッケージをアップロードするための非公開の認証情報です。]{#ci-workflow-permissions-secret-needed-a .correct explanation="認証情報は、別のシステムへのアクセスに使えることがあります。"}
::option[テストで使う Welcome という文字列です。]{#ci-workflow-permissions-secret-needed-b explanation="これは公開のサンプルに含まれるテキストです。"}
::option[出力ディレクトリの名前 dist です。]{#ci-workflow-permissions-secret-needed-c explanation="ディレクトリ名は一般的な設定値です。"}
:::

## 調査に役立つログを残す

ワークフローのログは、他の人と共有されることがあります。操作とその結果を、シークレットの値を出力せずに記録します。例えば、必要な認証情報を取得できなかった、あるいはアクセスが拒否されたと書けます。管理者が調査できるようにジョブ名とリビジョンを添え、認証情報そのものはメッセージに含めません。

:::single-choice{#ci-workflow-permissions-safe-diagnostic} 公開ジョブで認証できません。認証情報を公開せずに、調査に役立つメッセージはどれですか？

::option[コピーできるように認証情報をすべて表示します。]{#ci-workflow-permissions-safe-diagnostic-a explanation="ログを読める人なら誰でも認証情報を見られてしまいます。"}
::option[ジョブの状態を伝えるため、環境変数をすべて表示します。]{#ci-workflow-permissions-safe-diagnostic-c explanation="環境変数をまとめて出力すると、機密値が含まれる可能性があります。"}
::option[失敗した公開ステップと、アクセスの試行結果を伝えます。]{#ci-workflow-permissions-safe-diagnostic-b .correct explanation="調査する人は、失敗した場所を見つけ、設定されているアクセス権を別途確認できます。"}
:::

## 新しいジョブをレビューする

提案されたワークフローは、プルリクエストでページをチェックし、パッケージを公開するジョブを追加します。この二つのジョブに必要な権限は異なります。チェックに与える権限は必要な読み取りに限り、承認された公開権限は実際に公開するジョブだけに与えます。

:::single-choice{#ci-workflow-permissions-final-application} 二つのジョブの要件を最もよく満たす修正はどれですか？

::option[両方のジョブにリポジトリへの書き込み権限を与えます。]{#ci-workflow-permissions-final-application-b explanation="チェックではソースの読み取りだけが必要です。パッケージ公開には別の権限が必要な場合もあります。"}
::option[再実行しても同じように動くように、全ステップでアップロード用の認証情報を共有します。]{#ci-workflow-permissions-final-application-c explanation="アップロード用の認証情報が必要なのは公開ジョブだけです。"}
::option[チェックは読み取り専用のままにし、公開ジョブにだけ必要なパッケージの権限を与えます。]{#ci-workflow-permissions-final-application-a .correct explanation="どちらのジョブも必要な操作ができ、それ以外の権限を減らせます。"}
:::

## まとめ

小さな CI パイプラインに必要な権限を判断できるようになりました。

1. ジョブの作業に合わせて、リポジトリの権限を設定します。
2. 非公開の認証情報は、アクセスが制限された場所に保管します。
3. 認証情報の値を含めず、調査に役立つエラーを記録します。
