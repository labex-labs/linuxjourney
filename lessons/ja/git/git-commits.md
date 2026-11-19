---
lesson_id: "git-commits"
course_id: "git"
lang: "ja"
order_index: 4
title: "コミット"
description: "ステージした内容を保存し、Git の履歴からそのコミットを見つける方法を学びます。"
meta_title: "コミット - Git"
meta_description: "ステージした内容を保存し、Git の履歴からそのコミットを見つける方法を学びます。"
meta_keywords: "コミット, git, devops, Linux Journey"
---

**コミット**には、ステージングエリアで選んだファイルの状態が記録されます。メッセージ、作成者、過去のコミットとのつながりも記録されます。Git が割り当てた識別子を使えば、そのコミットを履歴から正確に見つけられます。

## 練習用リポジトリに作成者情報を設定する

Git はコミットに名前とメールアドレスを記録します。このリポジトリに限って、練習用の値を設定します。これらの値は履歴に記録するためのもので、リモートサービスへのアクセス権とは関係ありません。

```bash
$ git config --local user.name "Journey Learner"
$ git config --local user.email "learner@example.com"
```

`index.html` をステージした練習用リポジトリを使います。コミットに含まれるファイルを確認したいときは `git status` を実行してください。

:::single-choice{#git-commits-identity-scope} ここで --local を指定すると、どうなりますか？

::option[共有のホスティングサービスにサインインします。]{#git-commits-identity-scope-b explanation="名前とメールアドレスはコミットに記録される情報です。リモートへの認証は別に行います。"}
::option[このリポジトリに作成者情報を設定します。]{#git-commits-identity-scope-a .correct explanation="ローカル設定は現在のリポジトリに適用されます。"}
::option[すでにあるすべてのコミットの作成者を変更します。]{#git-commits-identity-scope-c explanation="この設定は、これから作るコミットに使われます。"}
:::

## ステージした内容を保存する

保存したい内容をステージした後で `git commit` を実行します。`-m` オプションを使うと、コマンドラインでメッセージを指定できます。

```bash
$ git commit -m "Set the homepage heading"
```

コミットにはステージ済みのファイルの内容が保存されます。ステージした後で作業ツリーのファイルを再び編集した場合、その編集はもう一度ステージするまでコミットに含まれません。

:::single-choice{#git-commits-staged-snapshot} Welcome をステージした後、ファイルを Hi に書き換えました。その後はステージしていません。コミットにはどの見出しが入りますか？

::option[ステージした時点の Welcome です。]{#git-commits-staged-snapshot-c .correct explanation="コミットは、ステージ済みの内容を読み取って保存します。"}
::option[ディスク上で最新の Hi です。]{#git-commits-staged-snapshot-a explanation="最新の作業ファイルの内容は、ステージ済みの内容と異なる場合があります。"}
::option[Git は編集を自動で保存するので、両方です。]{#git-commits-staged-snapshot-b explanation="各ファイルで保存されるのは、ステージングエリアにある一つの版です。"}
:::

## 短い形式で履歴を読む

`git log --oneline` で、履歴を短い形式で表示できます。各行には、短縮されたコミット ID と、そのコミットのメッセージが順に並びます。実際に表示される ID は例と異なります。

```text
$ git log --oneline
a12c345 Set the homepage heading
```

異なるコミットに同じメッセージを付けることもできるため、特定のコミットを指すときは ID を使います。通常は、現在の履歴で最も新しいコミットが上に表示されます。

:::single-choice{#git-commits-identify-snapshot} メッセージがどちらも Set the homepage heading という二つのコミットがあります。それぞれをどう見分けますか？

::option[二つに共通のコミットメッセージで見分けます。]{#git-commits-identify-snapshot-a explanation="同じメッセージを複数のコミットに付けることができます。"}
::option[両方で変更されたファイル名で見分けます。]{#git-commits-identify-snapshot-c explanation="同じファイルが複数のコミットに含まれることがあります。"}
::option[コミット ID で見分けます。]{#git-commits-identify-snapshot-b .correct explanation="ID を使うと、履歴の特定の項目を指せます。"}
:::

ブラウザーのターミナルでステージングとコミットを練習するには、[はじめての Git ラボ](https://labex.io/tutorials/git-your-first-git-lab-92739)をお試しください。

## まとめ

ステージした作業を保存し、履歴から見つけられるようになりました。

1. 練習用リポジトリでコミットの作成者情報を設定します。
2. 変更内容が分かるメッセージを付けて、ステージ済みの内容をコミットします。
3. 短い形式の履歴から、目的のコミットを見つけます。
