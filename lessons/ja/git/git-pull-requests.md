---
lesson_id: "git-pull-requests"
course_id: "git"
lang: "ja"
order_index: 7
title: "プルリクエスト"
description: "プルリクエストの読み方と、レビューや自動チェックがどの変更を対象にしているかを確認する方法を学びます。"
meta_title: "プルリクエスト - Git"
meta_description: "プルリクエストの読み方と、レビューや自動チェックがどの変更を対象にしているかを確認する方法を学びます。"
meta_keywords: "プルリクエスト, コードレビュー, git, devops, Linux Journey"
---

**プルリクエスト**（略して PR）は、あるブランチの変更を別のブランチに取り込む提案です。Git はコミットやブランチを管理します。ホスティングサービスでは、変更をレビューするページで内容を確認したり、意見を交わしたり、チェック結果を見たりできます。

## 変更元と取り込み先を確認する

チームメイトがサイトに状態を知らせるページを追加することを提案しました。レビュー画面には `health-page → main` と表示されています。変更元のブランチは **head** とも呼ばれ、提案の変更を含んでいます。取り込み先のブランチは **base** とも呼ばれ、その変更を受け取る側です。

```text
Source: health-page at 3ab4501
Target: main
Changed file: health.txt
```

この時点でレビュー画面に表示されているのは提案です。PR がマージされると、取り込み先のブランチに変更が反映されます。

:::single-choice{#git-pull-requests-pr-direction} この PR がマージされると、どのブランチに状態を知らせるページが追加されますか？

::option[コミット ID と同じ名前のブランチです。]{#git-pull-requests-pr-direction-a explanation="その値はコミットを特定するためのもので、取り込み先を示すブランチ名とは別です。"}
::option[main です。]{#git-pull-requests-pr-direction-b .correct explanation="取り込み先は main なので、レビューした変更はそこに反映されます。"}
::option[health-page です。]{#git-pull-requests-pr-direction-c explanation="health-page は変更を提供する側のブランチです。"}
:::

## 差分を読む

変更されたファイルの一覧を開き、PR の取り込み先を基準にした差分を読みます。`health.txt` への一行の追加なら、簡単な状態ページを作るという提案に合っています。`index.html` にも差分があれば、その変更も同じ提案に含めてよいかを考えます。PR に実際に表示されるファイルを確認してください。

:::single-choice{#git-pull-requests-unexpected-file} 「状態を知らせるページを追加」という PR が、トップページも変更しています。実際の変更内容はどこで確認できますか？

::option[変更されたファイルの差分です。]{#git-pull-requests-unexpected-file-a .correct explanation="差分には、この提案で変わる行が表示されます。"}
::option[PR のタイトルだけです。]{#git-pull-requests-unexpected-file-b explanation="タイトルは目的の要約なので、細かな変更が含まれないことがあります。"}
::option[ブランチ名です。]{#git-pull-requests-unexpected-file-c explanation="ブランチ名は作業を区別するための名前なので、個々の変更までは分かりません。"}
:::

## 自動チェックの結果を読む

ホスティングサービスによっては、PR が更新されるとテストが実行されます。結果がどのコミットやリビジョンに対応しているかを確認します。テストが通った後で別のコミットがプッシュされた場合は、更新されたリビジョンにも必要なチェックが実行されたかを確認します。成功の表示が示すのは、実際に走ったチェックの結果です。

:::single-choice{#git-pull-requests-changed-revision} 3ab4501 ではテストが通りました。今の PR は 78ac900 を指しています。結果を判断材料にする前に、何を確認しますか？

::option[最初のコミットメッセージが分かりやすいかどうかです。]{#git-pull-requests-changed-revision-a explanation="コミットメッセージでは、新しいコミットがテストの対象になったかは分かりません。"}
::option[PR のタイトルが以前と同じかどうかです。]{#git-pull-requests-changed-revision-b explanation="コードが変わっても、タイトルはそのままのことがあります。"}
::option[更新されたリビジョンでチェックが実行されたかどうかです。]{#git-pull-requests-changed-revision-c .correct explanation="前の結果は別のリビジョンを対象にしています。"}
:::

## まとめ

プルリクエストの提案内容を読み取り、マージの判断に使える情報を確認できるようになりました。

1. 変更元と取り込み先のブランチを見つけます。
2. 変更されたファイルの一覧で提案の内容を確かめます。
3. 自動チェックがどのリビジョンを対象にしているかを確認します。
