---
lesson_id: "deployment-rollbacks"
course_id: "deployment"
lang: "ja"
order_index: 5
title: "ロールバック"
description: "動作が確認できているバージョンを選び、アプリケーションを戻すだけで十分かを確かめる方法を学びます。"
meta_title: "ロールバック - デプロイ"
meta_description: "動作が確認できているバージョンを選び、アプリケーションを戻すだけで十分かを確かめる方法を学びます。"
meta_keywords: "ロールバック, データの互換性, デプロイ, DevOps, Linux Journey"
---

**ロールバック**は、以前に動作を確認したリリースにサービスを戻す作業です。デプロイ履歴から戻し先を選びます。戻す前に、そのリリースが共有データや設定にも変更を加えたかどうかを確認します。

## 前のリリースを選ぶ

この例では、新しいリリースの後にリクエストが失敗しました。最後に動作を確認したのはバージョン 2 です。下のラベルは、実際の記録では完全なイメージダイジェストが入る箇所を表します。

```text
08:50  version 2  digest-B  homepage and version check passed
09:10  version 3  digest-C  homepage check failed
```

現在の環境で引き続き動作するなら、バージョン 2 がロールバックの候補です。記録した成果物の参照で、そのイメージを見つけます。

:::single-choice{#deployment-rollbacks-previous-version} ロールバック先として、どのイメージを最初に調べますか？

::option[ホストのキャッシュにある最新のイメージです。]{#deployment-rollbacks-previous-version-a explanation="キャッシュの順序では、どのリリースが動作したかは分かりません。"}
::option[最後にデプロイした Digest-C です。]{#deployment-rollbacks-previous-version-c explanation="記録では、そのイメージでチェックが失敗しています。"}
::option[必要なチェックを以前に通過した Digest-B です。]{#deployment-rollbacks-previous-version-b .correct explanation="記録では、最後に動作を確認したバージョンに対応します。"}
:::

## データの互換性を確認する

アプリケーションのリリースでは、データベースや他の共有リソースにも変更を加えることがあります。古いイメージを起動しても、外部の状態は現在のままです。以前のアプリケーションで現在のデータを読めるかを確認します。データを復元する必要がある場合は、チームの復旧計画に従い、バックアップ後に生じた変更も考慮します。

:::single-choice{#deployment-rollbacks-external-state} バージョン 3 でデータベースの形式が変わりました。そのデータベースを使ってバージョン 2 を起動する前に、何を確認しますか？

::option[バージョン 2 が以前のトップページのチェックを通過したかです。]{#deployment-rollbacks-external-state-b explanation="以前のチェック結果は候補を選ぶ材料ですが、現在のデータ形式との互換性は確認できません。"}
::option[バージョン 2 が現在のデータ形式に対応しているかです。]{#deployment-rollbacks-external-state-a .correct explanation="アプリケーションのイメージを切り替えても、共有データは元に戻りません。"}
::option[データベース名がリリースノートにあるかです。]{#deployment-rollbacks-external-state-c explanation="実際に確かめたいのは、古いコードで現在のデータを使えるかです。"}
:::

## 結果を確かめる

ロールバック後は、実行中のバージョンを確かめます。失敗していた利用者向けのチェックを同じ手順で試し、重要な依存先も改めて確認します。最初の障害と復旧を区別できるように、時刻、復旧したバージョン、観察した結果を記録します。

:::single-choice{#deployment-rollbacks-rollback-proof} ロールバックのコマンドが終了しました。どの二つの結果から、サービスが復旧したと判断できますか？

::option[エンドポイントがバージョン 2 を返し、失敗していたチェックが今度は成功しました。]{#deployment-rollbacks-rollback-proof-c .correct explanation="期待したバージョンに戻り、影響を受けた動作が復旧したことを確認できます。"}
::option[イメージのダウンロードが二回成功しました。]{#deployment-rollbacks-rollback-proof-a explanation="ダウンロードでファイルは用意できますが、実行中のサービスの動作は確認できません。"}
::option[バージョン 2 の以前のスクリーンショットがあります。]{#deployment-rollbacks-rollback-proof-b explanation="スクリーンショットは過去の状態を示しています。"}
:::

## まとめ

確認結果を根拠にロールバックを計画できるようになりました。

1. 以前に動作確認済みのリリースを選びます。
2. 共有データや設定との互換性を確認します。
3. 復旧したバージョンと、影響を受けた利用者向けの動作を確かめます。
