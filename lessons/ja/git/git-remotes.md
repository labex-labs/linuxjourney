---
lesson_id: "git-remotes"
course_id: "git"
lang: "ja"
order_index: 6
title: "リモートリポジトリ"
description: "Git で別のリポジトリを参照し、フェッチとプッシュを使い分ける方法を学びます。"
meta_title: "リモートリポジトリ - Git"
meta_description: "Git で別のリポジトリを参照し、フェッチとプッシュを使い分ける方法を学びます。"
meta_keywords: "リモートリポジトリ, フェッチ, プッシュ, git, devops, Linux Journey"
---

**リモート**は、手元の Git リポジトリから別のリポジトリにアクセスするための、名前付きのアドレスです。接続先はホスティングサービスにも、同じマシン上のディレクトリにも置けます。この練習では別のローカルディレクトリを使うため、ホスティングサービスのアカウントは不要です。

## 接続先を追加する

練習用リポジトリから、別の**ベアリポジトリ**を作ります。ベアリポジトリには履歴や参照があり、プロジェクトの作業ツリーはありません。作業中のリポジトリからコミットを受け取れます。この練習を最初から行うには、未使用の `journey-remote.git` ディレクトリが必要です。

```bash
$ git init --bare --initial-branch=main ../journey-remote.git
$ git remote add origin ../journey-remote.git
$ git remote -v
```

リモートには `origin` という名前を付けるのが一般的です。リモートの一覧を表示すると、その名前がどのアドレスを指しているか確認できます。

:::single-choice{#git-remotes-add-address} git remote add を実行すると、一覧に origin が表示されました。Git は何をしましたか？

::option[別のリポジトリを名前付きで登録しました。]{#git-remotes-add-address-b .correct explanation="以降のコマンドでは、このアドレスを origin という名前で指定できます。"}
::option[ローカルのコミットをすべてアップロードしました。]{#git-remotes-add-address-a explanation="リモートを追加するとアドレスが登録されます。送信にはプッシュを使います。"}
::option[プロジェクト内に別の作業ツリーをクローンしました。]{#git-remotes-add-address-c explanation="既存の作業ツリーの場所は変わりません。"}
:::

## ブランチを送信する

`git push` を使ってローカルのコミットを送り、リモートにブランチの更新を依頼します。`-u` オプションを使うと、リモート側のブランチがアップストリームとして記録されます。今後のコマンドで、Git がローカルブランチと対応付けて使うブランチです。

```bash
$ git push -u origin main
```

ここでのプッシュ先は、別に作った練習用ディレクトリだけです。共有リモートの場合は権限が必要だったり、更新が拒否されたりすることもあります。出力を見て、プッシュできたことを確かめます。

:::single-choice{#git-remotes-push-direction} ローカルの main に作った新しいコミットをこのリモートに送るコマンドはどれですか？

::option[git fetch origin]{#git-remotes-push-direction-b explanation="フェッチは、リモートからローカルリポジトリに情報を取り込みます。"}
::option[git remote -v]{#git-remotes-push-direction-c explanation="このコマンドは origin の接続先アドレスを表示します。"}
::option[git push origin main]{#git-remotes-push-direction-a .correct explanation="プッシュは、リモート側に必要なコミットを送り、ブランチの更新を依頼します。"}
:::

## 更新を受け取る

`git fetch origin` を使って、リモートの履歴に関する手元の情報を更新します。Git は `origin/main` のような**リモート追跡ブランチ**に、最後に把握した状態を記録します。その履歴は `git log --oneline origin/main` で確認できます。フェッチだけなら、チェックアウト中の作業ツリーは今のローカルブランチのままです。

```bash
$ git fetch origin
$ git log --oneline origin/main
```

:::single-choice{#git-remotes-after-fetch} フェッチの後、origin/main は進みましたが、ローカルの main は変わりませんでした。何が起きましたか？

::option[フェッチが編集中のファイルを書き換えました。]{#git-remotes-after-fetch-a explanation="フェッチで更新されるのは、リモートブランチについて手元に記録した情報です。"}
::option[Git はリモートの変更を把握しました。手元のブランチへの統合は別の操作です。]{#git-remotes-after-fetch-c .correct explanation="origin/main が進んでも、ローカルのブランチは元の位置にとどまることがあります。"}
::option[フェッチ中にプッシュがリモートを更新しました。]{#git-remotes-after-fetch-b explanation="フェッチは、リモートから情報を受け取る操作です。"}
:::

## まとめ

Git のコマンドがどのリポジトリに作用するかを見分けられるようになりました。

1. リモートのアドレスを追加し、確認します。
2. ブランチをプッシュし、アップストリームを確認します。
3. チェックアウト中のファイルはそのままで、リモートの新しい履歴をフェッチします。
