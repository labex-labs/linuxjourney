---
lesson_id: "ci-workflow-triggers"
course_id: "continuous-integration"
lang: "ja"
order_index: 2
title: "ワークフローのトリガー"
description: "イベントとブランチのフィルターから、GitHub Actions のワークフローがいつ実行されるかを読み取ります。"
meta_title: "ワークフローのトリガー - 継続的インテグレーション"
meta_description: "イベントとブランチのフィルターから、GitHub Actions のワークフローがいつ実行されるかを読み取ります。"
meta_keywords: "ワークフローのトリガー, ブランチフィルター, 継続的インテグレーション, DevOps, Linux Journey"
---

ワークフローは、何らかのきっかけで実行されます。GitHub Actions では、`on` セクションに実行のきっかけとなるイベントを指定します。**イベント**には、ブランチへのプッシュやプルリクエストの変更など、GitHub が対応する操作があります。

## プッシュの条件を読む

ワークフローのこの部分を読んでみましょう。YAML ではインデントを見ると、`branches` が `push` の設定だと分かります。

```yaml
on:
  push:
    branches:
      - main
```

ワークフローが有効で、ほかの必要な条件も満たされていれば、`main` ブランチにコミットをプッシュしたときに実行されます。手元のターミナルでコミットしただけでは、変更は GitHub に送られていません。この設定が監視するのはプッシュです。

:::single-choice{#ci-workflow-triggers-push-filter} このプッシュのトリガーに当てはまる操作はどれですか？

::option[main でローカルコミットを作ります。]{#ci-workflow-triggers-push-filter-a explanation="トリガーが監視するのは、GitHub 上のリポジトリで起きるイベントです。"}
::option[draft というブランチにコミットをプッシュします。]{#ci-workflow-triggers-push-filter-b explanation="ブランチのフィルターで選ばれているのは main です。"}
::option[main にコミットをプッシュします。]{#ci-workflow-triggers-push-filter-c .correct explanation="push イベントとブランチのフィルターの両方に当てはまります。"}
:::

## プルリクエストの条件を読む

別のイベントを使うと、変更案をマージする前に確認できます。この例では、ブランチのフィルターがプルリクエストの取り込み先に適用されます。

```yaml
on:
  pull_request:
    branches:
      - main
```

`health-page` から `main` への提案は、このフィルターに当てはまります。デフォルトのアクティビティの種類では、プルリクエストを開いたときや、変更元のブランチにコミットを追加でプッシュしたときなどにワークフローが実行されます。

:::single-choice{#ci-workflow-triggers-pr-target} notes の変更を main に取り込むプルリクエストがあります。このフィルターではどの名前が使われますか？

::option[変更元の notes です。]{#ci-workflow-triggers-pr-target-b explanation="notes には提案する変更が含まれています。"}
::option[取り込み先の main です。]{#ci-workflow-triggers-pr-target-a .correct explanation="プルリクエストのブランチフィルターは、変更を受け取る base ブランチに適用されます。"}
::option[提案で編集したファイル名です。]{#ci-workflow-triggers-pr-target-c explanation="この設定ではブランチ名で絞り込みます。"}
:::

## 複数のトリガーを読む

同じ `on` キーの下に両方のイベントを設定できます。プルリクエストで実行すると、提案された統合内容を確認できます。マージで `main` が更新されると、プッシュによる実行でそのブランチの新しい状態を確認できます。結果はそれぞれの実行画面に表示されるイベントとリビジョンに対応します。

:::single-choice{#ci-workflow-triggers-after-merge} ワークフローに上の二つのトリガーが設定されています。マージで main が更新されたとき、どのイベントが当てはまりますか？

::option[main へのプッシュです。]{#ci-workflow-triggers-after-merge-b .correct explanation="取り込み先のブランチが更新され、プッシュのフィルターに当てはまります。"}
::option[新しいブランチでプルリクエストが開かれることです。]{#ci-workflow-triggers-after-merge-a explanation="ここで起きたのはマージ後の main の更新です。"}
::option[リモートを更新しないローカルコミットです。]{#ci-workflow-triggers-after-merge-c explanation="この例では、GitHub 上の main がすでに更新されています。"}
:::

## まとめ

リポジトリのイベントがどのワークフローのトリガーに当てはまるかを判断できるようになりました。

1. プッシュイベントと、そのブランチフィルターを読み取ります。
2. プルリクエストのフィルターが適用される取り込み先ブランチを見つけます。
3. ワークフローの結果と、実行のきっかけになったイベントを対応付けます。
