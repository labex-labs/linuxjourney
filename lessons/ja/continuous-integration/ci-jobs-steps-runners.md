---
lesson_id: "ci-jobs-steps-runners"
course_id: "continuous-integration"
lang: "ja"
order_index: 3
title: "ジョブ、ステップ、ランナー"
description: "短い GitHub Actions のファイルから、ジョブ、ステップ、ランナーを見つける方法を学びます。"
meta_title: "ジョブ、ステップ、ランナー - 継続的インテグレーション"
meta_description: "短い GitHub Actions のファイルから、ジョブ、ステップ、ランナーを見つける方法を学びます。"
meta_keywords: "ジョブ, ステップ, ランナー, 継続的インテグレーション, DevOps, Linux Journey"
---

ワークフローは自動処理の全体です。**ジョブ**は作業をひとまとまりにしたものです。作業を実行するマシンや環境を**ランナー**と呼びます。**ステップ**はジョブの中で行う一つの操作です。

## 短いワークフローを読む

この例は、GitHub がホストする Ubuntu ランナーで一つのジョブを実行します。このようなワークフローは、GitHub リポジトリの `.github/workflows/` に置きます。

```yaml
name: Page check
on: push
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Get the repository
        uses: actions/checkout@v6
      - name: Find the heading
        run: grep -q '<h1>Welcome</h1>' index.html
```

ジョブの ID は `check` です。`runs-on` フィールドは実行環境を選びます。`uses` は再利用可能なアクションを呼び出します。この例ではリポジトリのファイルを使えるようにします。`run` はランナーでコマンドを実行します。

:::single-choice{#ci-jobs-steps-runners-job-fields} どのフィールドが check ジョブの実行環境を選びますか？

::option[runs-on です。]{#ci-jobs-steps-runners-job-fields-a .correct explanation="ジョブで使うランナーの種類を指定します。"}
::option[uses です。]{#ci-jobs-steps-runners-job-fields-b explanation="このステップではチェックアウトのアクションを呼び出します。"}
::option[name です。]{#ci-jobs-steps-runners-job-fields-c explanation="ワークフローに名前を付けます。"}
:::

## ステップを順に追う

通常、一つのジョブのステップは記載された順に実行されます。チェックではリポジトリのファイルを読むため、先にチェックアウトします。同じジョブ内では、前のステップが書き込んだファイルを後のステップで使えます。

:::single-choice{#ci-jobs-steps-runners-step-order} 新しいランナーで、grep の後にチェックアウトするよう変えた場合、grep のステップには何が足りませんか？

::option[ジョブの名前です。]{#ci-jobs-steps-runners-step-order-a explanation="ワークフローはすでにジョブを選んでいます。"}
::option[Ubuntu ランナー自体です。]{#ci-jobs-steps-runners-step-order-c explanation="ランナーはステップの実行前に選ばれます。"}
::option[読み込む必要があるプロジェクトのファイルです。]{#ci-jobs-steps-runners-step-order-b .correct explanation="先にチェックアウトすることで、チェックの前にリポジトリのファイルが使えるようになります。"}
:::

## ジョブごとに実行環境が分かれることを知る

別々のジョブは同時に実行されることがあります。GitHub がホストするランナーはジョブごとに用意されるので、あるジョブで書き込んだファイルを別のジョブで使うには、ワークフローで転送します。あるジョブが別のジョブの成功を待つ必要があるなら、`needs` で依存関係を宣言し、必要に応じてアーティファクトでファイルを渡します。

:::single-choice{#ci-jobs-steps-runners-separate-jobs} ビルドジョブが site.tar.gz を作ります。後のジョブは別のホスト型ランナーで実行されます。ファイルはどう渡しますか？

::option[同じ作業ディレクトリに残っていると考えます。]{#ci-jobs-steps-runners-separate-jobs-a explanation="別のホスト型ランナーは、独自のファイルシステムを使います。"}
::option[ファイルをアーティファクトとして転送します。]{#ci-jobs-steps-runners-separate-jobs-c .correct explanation="ワークフローで、一方のジョブからアップロードし、もう一方のジョブでダウンロードできます。"}
::option[needs を設定して、二番目のジョブがビルドを待つようにします。]{#ci-jobs-steps-runners-separate-jobs-b explanation="needs は実行順を決めます。ビルドしたファイルはランナー間で別に転送する必要があります。"}
:::

GitHub リポジトリでワークフローを書いて実行するには、[初めての GitHub Actions](https://labex.io/courses/github-actions-for-beginners)をお試しください。この実習コースでは GitHub アカウントが必要です。

## まとめ

CI ワークフローの主な部分を読めるようになりました。

1. ジョブと、そのジョブを実行するランナーを見つけます。
2. 再利用可能なアクションと、シェルコマンドを実行するステップを区別します。
3. ジョブ間で依存関係やファイル転送が必要な場面を見分けます。
