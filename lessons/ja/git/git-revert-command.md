---
lesson_id: "git-revert-command"
course_id: "git"
lang: "ja"
order_index: 8
title: "git revert"
description: "git revert で、元のコミットを履歴に残したまま変更を取り消す方法を学びます。"
meta_title: "git revert - Git"
meta_description: "git revert で、元のコミットを履歴に残したまま変更を取り消す方法を学びます。"
meta_keywords: "git revert, コミットの取り消し, git, devops, Linux Journey"
---

共有済みの変更でも取り消せます。`git revert` は元の変更を打ち消す変更を新しいコミットとして記録します。履歴を見ると、何を変更し、何を取り消したかの両方が分かります。

## 取り消す変更を見つける

練習用リポジトリの `main` には、トップページと状態を知らせるページのコミットがあります。短い形式の履歴で、どちらが最新かを確かめます。以下の ID は表示例です。

```text
$ git log --oneline
3ab4501 Add a health page
a12c345 Set the homepage heading
```

`HEAD` は現在チェックアウトしているコミットを指します。それが取り消したい変更かどうかを確かめます。次に進む前に `git status` で作業ツリーに変更が残っていないことを確認します。

:::single-choice{#git-revert-command-newest-commit} この例で HEAD を取り消すと、どの変更が元に戻りますか？

::option[トップページの見出しを変えた、前の変更です。]{#git-revert-command-newest-commit-b explanation="見出しの変更は一つ前のコミットです。"}
::option[一度に両方の変更が元に戻ります。]{#git-revert-command-newest-commit-c explanation="ここで HEAD が指すのは一つのコミットです。取り消しはそのコミットに適用されます。"}
::option[状態を知らせるページの追加です。]{#git-revert-command-newest-commit-a .correct explanation="HEAD は、このブランチに表示される最新のコミットを指しています。"}
:::

## 取り消しを記録する

作業ツリーに変更が残っていない状態で、練習用リポジトリの状態ページのコミットを取り消します。この操作は作業ツリーのファイルを変更し、コミットを作成します。`--no-edit` を指定すると、Git が用意した取り消しメッセージをそのまま使えます。

```bash
$ git revert --no-edit HEAD
```

この例では、元のコミットが状態ページのファイルを追加したため、取り消すとそのファイルが削除されます。その後のコミットで同じ行を変更していた場合、Git が停止し、競合の解消を求めることがあります。続ける前にステータスを確認してください。

:::single-choice{#git-revert-command-undo-effect} 取り消しが成功すると、プロジェクトのファイルはどう変わりますか？

::option[トップページのファイルも状態ページと一緒に削除されます。]{#git-revert-command-undo-effect-a explanation="一つ前のトップページの変更は残ります。"}
::option[状態ページのファイルが削除されます。]{#git-revert-command-undo-effect-b .correct explanation="選んだコミットが追加したファイルを、取り消しによって削除します。"}
::option[状態ページがもう一度追加されます。]{#git-revert-command-undo-effect-c explanation="取り消しでは、元の変更を打ち消す操作が行われます。"}
:::

![新しい取り消しコミットと状態ページの元のコミットが並ぶ Git の履歴](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-revert-command/recorded-undo.png)

## 取り消した後の履歴を確認する

`git log --oneline` をもう一度実行します。状態ページの元のコミットより上に、新しい取り消しコミットが表示されるはずです。`git status --short` で、手元に未保存の変更が残っていないかを確認します。新しいコミットも、他の変更と同じ手順でレビューして共有できます。

:::single-choice{#git-revert-command-history-after-revert} 新しい取り消しコミットの下には、何が残っていますか？

::option[状態ページを追加した元のコミットです。]{#git-revert-command-history-after-revert-c .correct explanation="二つのコミットが、元の変更とその取り消しを記録しています。"}
::option[最初に見出しを変更したコミットだけです。]{#git-revert-command-history-after-revert-a explanation="状態ページの元のコミットも履歴に残っています。"}
::option[コミットは何も残りません。]{#git-revert-command-history-after-revert-b explanation="取り消しは既存のブランチ履歴にコミットを追加します。"}
:::

## 関係のない変更を残す

履歴に三つの独立した変更があるとします。状態ページのファイルを追加した後にトップページの誤字を直し、両方の変更を共有しました。ファイルを追加したコミットを指定して取り消せば、誤字の修正を残したままそのファイルを削除できます。取り消すコミットを選ぶ前に、履歴と変更されたファイルを確認します。

:::single-choice{#git-revert-command-final-application} 残すべき変更が残ったことは、どの確認で分かりますか？

::option[状態ページを追加したコミットが履歴から消えています。]{#git-revert-command-final-application-b explanation="取り消しても、元のコミットは履歴に残ります。"}
::option[トップページから誤字の修正も消えています。]{#git-revert-command-final-application-c explanation="誤字の修正は別の変更なので、残るはずです。"}
::option[状態ページのファイルがなくなり、トップページの修正は残っていて、履歴には取り消しが記録されています。]{#git-revert-command-final-application-a .correct explanation="取り消した変更、残した変更、新しく追加された履歴をそれぞれ確認できています。"}
:::

## まとめ

コミット済みの変更を取り消し、元の変更と取り消しの両方を記録できるようになりました。

1. 取り消すコミットを正確に特定します。
2. 作業ツリーに変更が残っていないことを確認してから取り消します。
3. 履歴に両方のコミットがあることを確認します。
