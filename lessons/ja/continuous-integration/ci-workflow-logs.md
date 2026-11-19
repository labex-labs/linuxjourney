---
lesson_id: "ci-workflow-logs"
course_id: "continuous-integration"
lang: "ja"
order_index: 5
title: "ワークフローのログ"
description: "失敗したワークフローのステップを見つけ、原因を調べる手掛かりになる最初のメッセージを読む方法を学びます。"
meta_title: "ワークフローのログ - 継続的インテグレーション"
meta_description: "失敗したワークフローのステップを見つけ、原因を調べる手掛かりになる最初のメッセージを読む方法を学びます。"
meta_keywords: "ワークフローのログ, エラー調査, 継続的インテグレーション, DevOps, Linux Journey"
---

ワークフローの結果には、全体の状態が表示されます。失敗の理由を知るには、失敗したジョブを開き、ステップを順番に確認します。前のステップが正常に終わらなかったために、後のステップがスキップされることがあります。

## 最初の失敗を見つける

この模擬実行では、ページを確認するジョブの各ステップの状態が表示されています。

```text
Prepare: passed
Build page: failed
Check heading: skipped
Package site: skipped
```

まず `Build page` を見ます。スキップされたチェックには、ページの確認結果がありません。失敗の原因を修正したら、改めて実行して後続のステップを確認します。

:::single-choice{#ci-workflow-logs-first-failure} どのステップの出力を最初に読みますか？

::option[最後に表示されている Package site です。]{#ci-workflow-logs-first-failure-a explanation="この実行ではアーカイブを作るコマンドがスキップされました。"}
::option[ページの内容を確認する Check heading です。]{#ci-workflow-logs-first-failure-c explanation="状態の表示では、見出しのチェックは実行されていません。"}
::option[他のステップの実行前に失敗した Build page です。]{#ci-workflow-logs-first-failure-b .correct explanation="そのログを読むと、後続のステップがスキップされた理由が分かります。"}
:::

![ビルドが失敗し、後続ステップがスキップされた模擬 CI 実行](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-workflow-logs/skipped-steps.png)

## エラーメッセージから原因を探る

失敗したステップには、次のように表示されます。

```text
Run cp index.html dist/index.html
cp: cannot create regular file 'dist/index.html': No such file or directory
Process completed with exit code 1.
```

エラーメッセージにはコピー先のパスが書かれています。親ディレクトリ `dist` がないと、そこにファイルを作成できません。前のコマンドで、コピーの前にそのディレクトリを作ったか確かめます。終了コード 1 は失敗を示し、メッセージからはどこを調べるかが分かります。

:::single-choice{#ci-workflow-logs-actionable-log} dist がない場合、報告された問題を解消する変更はどれですか？

::option[grep が調べる見出しを変更します。]{#ci-workflow-logs-actionable-log-b explanation="見出しのチェックは実行されていないので、テキストが間違っているとは判断できません。"}
::option[ファイルをコピーする前に dist を作ります。]{#ci-workflow-logs-actionable-log-a .correct explanation="コピー先のファイルを作るには、先にその親ディレクトリが必要です。"}
::option[スキップされたステップから成果物をダウンロードします。]{#ci-workflow-logs-actionable-log-c explanation="今回は、アーカイブを作るステップで成果物が生成されていません。"}
:::

## 修正後の実行を確認する

ビルドを修正したら、新しい実行のリビジョンと各ステップの状態を比べます。コピーが成功すれば、出力ファイルが作られたことを確認できます。処理全体が成功したと判断する前に、テストとパッケージ化の結果も確認します。問題を報告するときは、最初に手掛かりになるエラーとステップ名を添えます。

:::single-choice{#ci-workflow-logs-rerun-evidence} 新しい実行では Build page が成功し、Check heading が失敗しました。何が変わりましたか？

::option[ビルドが成功し、今度は調査できる見出しチェックの結果があります。]{#ci-workflow-logs-rerun-evidence-c .correct explanation="最初に残っている失敗はテストのステップに移りました。"}
::option[前のビルドが失敗したので、新しい実行は関係ありません。]{#ci-workflow-logs-rerun-evidence-a explanation="実行ごとに、そのリビジョンを確認した結果が得られます。"}
::option[ビルドが成功したので、パッケージ化も成功したはずです。]{#ci-workflow-logs-rerun-evidence-b explanation="後続のステップは、失敗したりスキップされたりすることがあります。"}
:::

## まとめ

前後のステップを踏まえて、ワークフローが失敗した理由を読めるようになりました。

1. 実行された中で、最初に失敗したステップを見つけます。
2. ログのメッセージを手掛かりに、確認すべき場所を決めます。
3. 修正したら、新しいリビジョンと後続のステップを確認します。
