---
lesson_id: "git-branches"
course_id: "git"
lang: "ja"
order_index: 5
title: "ブランチ"
description: "Git で作業をブランチに分け、マージして変更を main に取り込む方法を学びます。"
meta_title: "ブランチ - Git"
meta_description: "Git で作業をブランチに分け、マージして変更を main に取り込む方法を学びます。"
meta_keywords: "ブランチ, マージ, git, devops, Linux Journey"
---

**ブランチ**は、コミットを指す名前です。現在のブランチで新しいコミットを作ると、その名前が新しいコミットを指すようになります。他のブランチは、更新するまで元のコミットを指したままです。

## 別のブランチで作業を始める

練習用リポジトリの `main` から `health-page` というブランチを作成し、切り替えます。`git switch` の `-c` オプションは、ブランチを新規作成する指定です。

```bash
$ git switch -c health-page
```

最初は、二つのブランチ名が同じコミットを指しています。次のコミットでどのブランチが更新されるかは、`git branch --show-current` で確認できます。

:::single-choice{#git-branches-start-pointer} git switch -c health-page の直後に、新しいブランチはどのコミットを指していますか？

::option[コマンドによって作られた空のコミットです。]{#git-branches-start-pointer-a explanation="このコマンドは、既存のコミットを指す名前を作ります。"}
::option[別の人のリポジトリにあるコミットです。]{#git-branches-start-pointer-c explanation="作られるのは、今のリポジトリにあるローカルブランチです。"}
::option[新しいブランチの出発点となったコミットです。]{#git-branches-start-pointer-b .correct explanation="最初は、二つのブランチ名が同じコミットを指しています。"}
:::

## ブランチに変更を保存する

`health-page` に切り替えた状態で、状態を表す一行のファイルを追加し、コミットします。

```bash
$ printf '%s\n' ready > health.txt
$ git add health.txt
$ git commit -m "Add a health page"
```

トップページのコミットを A、状態を知らせるページのコミットを B とします。

```text
A (main) --- B (health-page)
```

B に進んだのは `health-page` だけです。作業ツリーに未保存の変更がない状態で `main` に戻ると、ファイルも A の状態に戻ります。

:::single-choice{#git-branches-branch-snapshot} マージする前に、状態を知らせるページのコミットを含むのはどのブランチですか？

::option[同じリポジトリにあるので、両方のブランチです。]{#git-branches-branch-snapshot-a explanation="一つのリポジトリ内でも、ブランチごとに別のコミットを指すことができます。"}
::option[health-page だけです。]{#git-branches-branch-snapshot-c .correct explanation="コミット B を作成したときに使っていたブランチです。"}
::option[最初に使っていた main だけです。]{#git-branches-branch-snapshot-b explanation="health-page でコミットしても、main の位置は変わりません。"}
:::

## main にマージする

変更を受け取るブランチに切り替えてから、マージ元のブランチ名を指定します。

```bash
$ git switch main
$ git merge health-page
```

この例では、`main` には A 以降の独自の変更がありません。そのため、Git は main を直接 B に進められます。この操作を**ファストフォワード**と呼びます。二つのブランチにそれぞれ新しいコミットがある場合は、変更を組み合わせる必要があるかもしれません。出力を読んで、マージが完了したことを確かめます。

:::single-choice{#git-branches-merge-direction} health-page の変更を main に取り込みます。どこでマージを実行しますか？

::option[main で、マージ元に health-page を指定します。]{#git-branches-merge-direction-a .correct explanation="マージの結果は、現在のブランチに取り込まれます。"}
::option[health-page で、マージ元に main を指定します。]{#git-branches-merge-direction-b explanation="その場合、更新されるのは health-page です。"}
::option[どちらでもない新しいブランチで実行します。]{#git-branches-merge-direction-c explanation="変更を受け取るまで、main の位置は変わりません。"}
:::

## まとめ

ローカルのブランチで作業した変更を main に取り込む流れが分かりました。

1. 現在のコミットを起点にブランチを作成します。
2. 目的のブランチに変更を保存します。
3. 変更を受け取るブランチにマージします。
