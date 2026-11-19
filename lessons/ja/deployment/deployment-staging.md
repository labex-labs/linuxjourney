---
lesson_id: "deployment-staging"
course_id: "deployment"
lang: "ja"
order_index: 3
title: "ステージング"
description: "ステージングで何を確認できるか、同じ成果物でも環境によって動きが異なる理由を学びます。"
meta_title: "ステージング - デプロイ"
meta_description: "ステージングで何を確認できるか、同じ成果物でも環境によって動きが異なる理由を学びます。"
meta_keywords: "ステージング, 検証環境, デプロイ, DevOps, Linux Journey"
---

リリースの準備が整いつつあります。成果物を**ステージング**で動かします。ステージングは、利用者が使う本番のサービスに近づけた検証環境です。本番のトラフィックを受ける前に、本番に近い設定でリリースを確認できます。

## 同じ成果物を次の環境に移す

テストを通過し、承認されたイメージを使います。依存関係が変わった状態でビルドし直すと、異なる成果物ができる場合があります。デプロイのたびに、イメージの完全な参照を記録します。

```text
Environment  Artifact      Page configuration
staging      site@digest-A Internal preview
production   site@digest-A Public website
```

例のダイジェストは説明用の値です。両環境で同じ成果物を使い、設定だけが異なります。

:::single-choice{#deployment-staging-same-artifact} 同じパッケージのコードを本番に移せることは、何を見れば分かりますか？

::option[両方のデプロイ記録で成果物の参照が一致しています。]{#deployment-staging-same-artifact-b .correct explanation="正確な参照によって、二つの環境が同じビルドを使っていることが分かります。"}
::option[両方の環境で同じポート名を使っています。]{#deployment-staging-same-artifact-a explanation="一つの設定が一致しても、成果物が同じだとは分かりません。"}
::option[両方とも同じ日にデプロイしています。]{#deployment-staging-same-artifact-c explanation="日時だけでは、デプロイしたものを特定できません。"}
:::

## 本番を想定した確認項目を選ぶ

ステージングでは、ページの読み込みやテスト用の依存先からのデータ読み取りなど、重要な動作を試せるようにします。許可されたテスト用のアカウントとデータを使います。チェックが成功すれば、試したシナリオで動作するという根拠が得られます。本番に移した後は、トラフィック、データ、設定の違いが影響する可能性があります。

:::single-choice{#deployment-staging-staging-scope} ステージングではテスト用のデータベースを使ってページが読み込めました。本番にデプロイした後、何を確認しますか？

::option[成果物にバージョンの記録が不要になったことです。]{#deployment-staging-staging-scope-b explanation="バージョンの記録は確認や復旧にも役立ちます。"}
::option[本番のすべてのリクエストが成功することです。]{#deployment-staging-staging-scope-c explanation="少数のテストでは、今後のすべての結果までは分かりません。"}
::option[本番のアクセス経路で、承認された設定のまま動作することです。]{#deployment-staging-staging-scope-a .correct explanation="ステージングへのリクエストでは、本番環境での動作は確認していません。"}
:::

## 変更前に対象を確認する

デプロイする前に、対象の名前とアドレスを読みます。デプロイ後は、同じアドレスで新しいバージョンと重要な動作を確認します。どの結果がどの環境のものか分かるように、メモではステージングと本番を明記します。

:::single-choice{#deployment-staging-correct-target} ステージングにデプロイするつもりですが、コマンドに本番のアドレスが表示されています。最初に何をしますか？

::option[続行し、後から結果をステージングとして記録します。]{#deployment-staging-correct-target-a explanation="コマンドに指定したアドレスが、変更を受けるサービスを決めます。"}
::option[いったん止めて、対象がどの環境かを確かめます。]{#deployment-staging-correct-target-c .correct explanation="こうすれば、誤った環境に変更を適用せずに済みます。"}
::option[デプロイ後に別のブラウザーから確認します。]{#deployment-staging-correct-target-b explanation="変更が始まる前に、正しい対象を指定する必要があります。"}
:::

CI/CD の実習例は、[ステージングへの継続的デプロイ](https://labex.io/tutorials/cd-deployment-to-staging-636593)を参照してください。

## まとめ

承認された成果物を次の環境に移す前に、ステージングで確認できるようになりました。

1. 環境が変わっても、同じ成果物を使います。
2. 利用者にとって重要な動作を代表するチェックを選びます。
3. 変更する前に対象環境を確認します。
