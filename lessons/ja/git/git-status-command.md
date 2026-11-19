---
lesson_id: "git-status-command"
course_id: "git"
lang: "ja"
order_index: 2
title: "git status"
description: "git status で、未追跡、ステージ済み、変更済みのファイルを見分ける方法を学びます。"
meta_title: "git status - Git"
meta_description: "git status で、未追跡、ステージ済み、変更済みのファイルを見分ける方法を学びます。"
meta_keywords: "git status, git, devops, Linux Journey, 未追跡ファイル"
---

リポジトリ内で作業するとき、`git status` を使うと、作業ツリーにある変更と、次に保存するために選んだ変更を確認できます。前のレッスンで作った空の `journey-git` リポジトリを使います。

## 新しいファイルを見つける

小さなページを作ります。今回は、結果を読みやすくするために短い形式で表示します。

```bash
$ printf '%s\n' '<h1>Hello</h1>' > index.html
$ git status --short
```

ここで `>` は指定したファイルに書き込みます。同じ名前のファイルがすでにあれば、中身を上書きします。新しいファイルの場合、短い形式では `?? index.html` と表示されます。Git ではこれを**未追跡**と呼びます。ファイルは存在しますが、保存する状態にはまだ含まれていません。

:::single-choice{#git-status-command-untracked-file} 新しいファイルの横に疑問符が二つ表示されました。これは何を表していますか？

::option[前回保存した状態に含まれています。]{#git-status-command-untracked-file-a explanation="未追跡ファイルは前回保存した状態に含まれていません。"}
::option[作業ツリーから削除されています。]{#git-status-command-untracked-file-c explanation="このファイルは作業ツリーにあります。"}
::option[ファイルは存在しますが、次に保存する内容にはまだ含まれていません。]{#git-status-command-untracked-file-b .correct explanation="必要であれば、そのファイルをステージングエリアに追加できます。"}
:::

![index.html が未追跡からステージ済みに変わる様子を示した Git の短いステータス表示](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-status-command/staged-file.png)

## ステージした変更を確認する

`git add` を実行して、ファイルの現在の内容を次に保存する状態に含めます。この保存の単位を**コミット**と呼びます。保存する内容を選んで置く場所が**ステージングエリア**です。短い形式では、保存を待つ追加を示す `A` が最初の列に表示されます。

```bash
$ git add index.html
$ git status --short
```

:::single-choice{#git-status-command-staged-new} git add の後、選んだ index.html の内容はどこにありますか？

::option[すでに新しいコミットに入っています。]{#git-status-command-staged-new-a explanation="git add は次のコミットを準備する操作です。コミットそのものは作成しません。"}
::option[ステージングエリアにあります。]{#git-status-command-staged-new-c .correct explanation="Git は git add を実行した時点の内容を選びました。"}
::option[別の人のリポジトリにあります。]{#git-status-command-staged-new-b explanation="変更されるのは手元のステージングエリアだけです。"}
:::

## 二種類の変更を区別する

短い形式では、ファイル名の前に二つの列があります。一つ目の列はステージした変更を、二つ目の列はステージした後に加えた変更を表します。例えば `AM index.html` は、Git が新しいファイルをステージし、その後で作業ツリー側のファイルを変更したことを示します。見出し付きで確認したい場合は、オプションなしの `git status` で項目ごとに詳細を表示できます。

:::single-choice{#git-status-command-two-columns} index.html の横に AM と表示されました。次にコミットする前に何を確認しますか？

::option[保存したい編集内容が、ステージ済みの版に含まれているかを確認します。]{#git-status-command-two-columns-a .correct explanation="二列目の M は、作業ツリーにさらに新しい編集があることを表します。"}
::option[AM という別のファイルがリポジトリにあるかを確認します。]{#git-status-command-two-columns-b explanation="AM は index.html の状態を表す二つの記号です。"}
::option[ファイルがディスクから削除されたかを確認します。]{#git-status-command-two-columns-c explanation="M は作業ツリーでの変更を表します。"}
:::

## まとめ

Git が次にどの変更を保存するか確認できるようになりました。

1. 新しい未追跡ファイルを見分けます。
2. git add でファイルをステージします。
3. ステージ済みの変更と作業ツリーの変更を分けて読み取ります。
