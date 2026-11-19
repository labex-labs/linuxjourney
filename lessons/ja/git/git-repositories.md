---
lesson_id: "git-repositories"
course_id: "git"
lang: "ja"
order_index: 1
title: "リポジトリ"
description: "Git リポジトリに何が保存されるかを学び、小さな Web サイト用に空のリポジトリを作ります。"
meta_title: "リポジトリ - Git"
meta_description: "Git リポジトリに何が保存されるかを学び、小さな Web サイト用に空のリポジトリを作ります。"
meta_keywords: "リポジトリ, git, devops, Linux Journey"
---

Web サイトは数個のファイルから始まります。Git を使うと、ある時点でそれらのファイルがどのような状態だったかを記録できます。プロジェクトのファイルとその履歴を合わせたものが、手元の Git 作業環境です。

## リポジトリを作る

新しいフォルダーを作成できる練習用ディレクトリで始めます。次のコマンドを一度実行してください。ドル記号はシェルのプロンプトを表します。

```bash
$ mkdir journey-git
$ cd journey-git
$ git init --initial-branch=main
```

新しいフォルダーは**作業ツリー**です。プロジェクトのファイルはここで編集します。Git は履歴と設定を保存するために、その中に隠しディレクトリ `.git` を作ります。新しいリポジトリには、まだ保存された変更はありません。最初の作業の流れには `main` という名前を付けます。

:::single-choice{#git-repositories-empty-history} index.html があるディレクトリでリポジトリを初期化すると、このファイルの履歴はどうなりますか？

::option[Git は最初のコミットとして、すぐにファイルを記録します。]{#git-repositories-empty-history-b explanation="初期化しただけでは、プロジェクトのファイルは記録されません。"}
::option[今後のコミットでファイルを記録できます。]{#git-repositories-empty-history-a .correct explanation="初期化はリポジトリを準備する操作です。その時点の状態を保存するには、別の操作が必要です。"}
::option[Git はファイルを隠しディレクトリに移動します。]{#git-repositories-empty-history-c explanation="プロジェクトのファイルは、編集できるように作業ツリーに残ります。"}
:::

![空の Git リポジトリを初期化し、練習用フォルダーがルートとして表示された LabEx のターミナル](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-repositories/init-and-root.png)

## 作業ツリーを見分ける

`git rev-parse --show-toplevel` を使うと、現在のリポジトリのルートを表示できます。練習用フォルダー内で実行すると、末尾が `journey-git` のパスが表示されます。作業ツリーの中にあるフォルダーは、その中に独立したリポジトリがない限り、同じリポジトリに含まれます。

```bash
$ git rev-parse --show-toplevel
```

:::single-choice{#git-repositories-find-root} journey-git の中にある images サブディレクトリに移動しました。Git はどのディレクトリを最上位として表示しますか？

::option[journey-git ディレクトリです。]{#git-repositories-find-root-b .correct explanation="Git は現在のディレクトリより上にあるリポジトリのルートを見つけます。"}
::option[images サブディレクトリです。]{#git-repositories-find-root-a explanation="シェルがサブディレクトリにあっても、表示されるのはリポジトリの最上位です。"}
::option[隠しディレクトリの .git です。]{#git-repositories-find-root-c explanation="このコマンドは、プロジェクトのファイルを置く作業ツリーのルートを表示します。"}
:::

## 既存の履歴を使って始める

既存のリポジトリをコピーするときは `git clone` を使います。通常のクローンでは、ローカルに新しい作業ツリーが作られ、リポジトリの履歴も取り込まれます。手元で新たに履歴を作り始めるプロジェクトには `git init` を使います。この先のレッスンでも `journey-git` を使います。

:::single-choice{#git-repositories-choose-start} チームメイトからリポジトリのアドレスを受け取り、その履歴が必要です。まず何をしますか？

::option[空のフォルダーを作り、初期化します。]{#git-repositories-choose-start-a explanation="新しいリポジトリにはチームメイトの履歴がありません。"}
::option[目に見える Web サイトのファイルだけをコピーします。]{#git-repositories-choose-start-b explanation="ファイルだけをコピーすると、ある時点の状態は手に入りますが、履歴は含まれません。"}
::option[チームメイトのリポジトリをクローンします。]{#git-repositories-choose-start-c .correct explanation="クローンすると共有リポジトリの履歴がコピーされ、手元に作業ツリーができます。"}
:::

## まとめ

目的に応じて、ローカルの Git リポジトリを用意する方法を選べるようになりました。

1. 作業ツリーと Git の隠しディレクトリを見分けましょう。
2. サブディレクトリからリポジトリのルートを確認しましょう。
3. 履歴を作り始めるときは初期化し、既存の履歴が必要なときはクローンします。
