---
lesson_id: "git-diff-command"
course_id: "git"
lang: "ja"
order_index: 3
title: "git diff"
description: "git diff で、作業ツリーとステージングエリアにあるファイルの内容を比較する方法を学びます。"
meta_title: "git diff - Git"
meta_description: "git diff で、作業ツリーとステージングエリアにあるファイルの内容を比較する方法を学びます。"
meta_keywords: "git diff, 差分, git, devops, Linux Journey"
---

ステータスでは、どのファイルが変わったかが分かります。変わった行を確認するには `git diff` を使います。この例では、前のレッスンで Hello という見出しを持つ `index.html` をすでにステージしています。

## ファイルをステージ済みの内容と比較する

練習用ファイルの見出しを書き換え、作業ツリーの内容とステージ済みの内容を比べます。

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
$ git diff -- index.html
```

`--` はオプションと、確認したいファイルのパスを区切ります。出力で `-` から始まるのは、変更前の内容にあった行です。`+` から始まるのは、置き換えた後の行です。以下の二行は、差分のうち今回の編集を示す部分です。

```diff
-<h1>Hello</h1>
+<h1>Welcome</h1>
```

:::single-choice{#git-diff-command-changed-heading} 現在、作業ツリーのファイルにはどの見出しがありますか？

::option[Welcome です。]{#git-diff-command-changed-heading-b .correct explanation="この比較では、プラス記号の行が作業ツリーの新しい内容です。"}
::option[Hello です。]{#git-diff-command-changed-heading-a explanation="マイナス記号の行は、以前にステージした内容です。"}
::option[両方の見出しが入っています。]{#git-diff-command-changed-heading-c explanation="二つの行は、同じ一行の変更前と変更後を表します。"}
:::

## ステージングエリアと履歴を比較する

`git diff --staged -- index.html` で、ステージ済みの内容を直近のコミットと比較できます。最初のコミットより前は、空の状態を基準に比較します。ここでは、ステージ済みの Hello という見出しが追加として表示されます。一方、オプションなしの `git diff` では、その後に Welcome に変更した差分が表示されます。

```bash
$ git diff --staged -- index.html
```

:::single-choice{#git-diff-command-preview-commit} 今すぐコミットした場合に保存される内容は、どのコマンドで確認できますか？

::option[git diff -- index.html]{#git-diff-command-preview-commit-b explanation="作業中のファイルと、ステージ済みのファイルを比較します。"}
::option[git status --short]{#git-diff-command-preview-commit-c explanation="変更された箇所の状態を表示しますが、変更した行の内容は表示しません。"}
::option[git diff --staged -- index.html]{#git-diff-command-preview-commit-a .correct explanation="選択した内容を前回保存した状態と比較します。"}
:::

![作業ツリーの Welcome とステージ済みの Hello の見出しを比較した LabEx のターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-diff-command/working-and-staged.png)

## 差分が空のときに確認すること

現在のファイルをもう一度ステージして、ステージ済みの内容を更新します。

```bash
$ git add index.html
$ git diff -- index.html
```

作業中のファイルとステージ済みの内容が一致するため、オプションなしの `git diff` は何も表示しないことがあります。コミットを待つ変更を見たい場合は、ステージ済みの差分を確認します。通常の差分表示には未追跡ファイルも含まれません。変更がどの状態にあるか分からないときは、ステータスを確認します。

:::single-choice{#git-diff-command-empty-diff} 編集内容をステージした直後、オプションなしの git diff には何も表示されませんでした。履歴に対する変更はどこで確認できますか？

::option[オプションなしの git diff をもう一度実行します。]{#git-diff-command-empty-diff-a explanation="同じ比較を繰り返しても、両方の内容が一致しているため何も表示されません。"}
::option[git diff --staged で確認します。]{#git-diff-command-empty-diff-c .correct explanation="ステージ済みの内容を、履歴上の基準と比較します。"}
::option[コミットを作成した後で確認できます。]{#git-diff-command-empty-diff-b explanation="コミットを作成する前に、保存する予定の差分を確認できます。"}
:::

## まとめ

目的に合った差分の見方を選べるようになりました。

1. 差分に表示される削除行と追加行を読み取ります。
2. 作業中のファイルとステージングエリアを比較します。
3. コミットする前にステージ済みの変更を確認します。
