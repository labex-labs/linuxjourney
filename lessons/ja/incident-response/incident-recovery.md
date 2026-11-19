---
lesson_id: "incident-recovery"
course_id: "incident-response"
lang: "ja"
order_index: 5
title: "復旧"
description: "復旧完了を宣言する前に、サービスが承認済みの状態に戻ったことを確かめる方法を学びます。"
meta_title: "復旧 - インシデント対応"
meta_description: "復旧完了を宣言する前に、サービスが承認済みの状態に戻ったことを確かめる方法を学びます。"
meta_keywords: "サービス復旧, インシデント対応, サイバーセキュリティ, Linux Journey"
---

**復旧**では、サービスを期待される状態に戻し、引き続き利用できることを確認します。プロセスの起動は最初の手掛かりです。設定、依存先、利用者から見た動作が意図した状態に合っていることも、証拠をもとに確かめます。

## 復旧後の状態を特定する

復旧に使う承認済みのバージョンと設定を記録します。サービスを隔離していた場合は、引き続き制限すべきアクセスを確認します。経路を再開すると、封じ込めの範囲が変わることがあります。

:::single-choice{#incident-recovery-restore-target} 想定したバージョンに戻ったか確認できる結果はどれですか？

::option[無関係な仮想マシンに新しいタイムスタンプがあります。]{#incident-recovery-restore-target-b explanation="その時刻からは、復旧対象のサービスを識別できません。"}
::option[利用できるパッケージの一覧だけです。]{#incident-recovery-restore-target-c explanation="入手できるパッケージからは、現在リクエストを処理しているバージョンは分かりません。"}
::option[対象環境で承認済みのバージョンを識別できる応答またはデプロイ記録です。]{#incident-recovery-restore-target-a .correct explanation="稼働中のサービスを、チームが選んだバージョンと結び付けられます。"}
:::

## 報告された問題を再確認する

模擬インシデントでは、利用者が公開トップページで `503` を受け取りました。サービスを復元した後、適切な検証場所から同じパスにリクエストを送ります。期待どおりに成功することを確かめ、直近のリクエストエラーも確認します。内部プレビューの成功では、公開経路は確認できません。

:::single-choice{#incident-recovery-verify-original-path} 利用者が最初に見た症状が解消したことを確かめるには、どのテストが最適ですか？

::option[サービスの実行ファイルが存在するかだけを確認します。]{#incident-recovery-verify-original-path-a explanation="ファイルがあっても、公開リクエストを処理しているとは限りません。"}
::option[対象クライアントが使う経路から公開トップページを確認します。]{#incident-recovery-verify-original-path-b .correct explanation="最初に失敗した確認を、同じ経路で繰り返せます。"}
::option[内部プレビューだけを確認します。]{#incident-recovery-verify-original-path-c explanation="影響が出たのは別の経路です。"}
:::

## 観測を続ける

短い観測期間と、成功と判断する基準に合意しておきます。エラー、レイテンシ、アクセス拒否など、関連するシグナルを確認します。確認の限界、残っている作業、次に見直す時刻を記録します。復旧を裏付ける証拠はインシデント記録と一緒に保管します。

:::single-choice{#incident-recovery-observation-period} 最初の確認は成功しましたが、障害は断続的に起きていました。復旧確認を終える前に何をしますか？

::option[観測期間中は、合意したシグナルを引き続き確認します。]{#incident-recovery-observation-period-c .correct explanation="復旧後の動作が続いているかを裏付けられます。"}
::option[一度応答があったので、すぐに終了します。]{#incident-recovery-observation-period-a explanation="確認が一度だけでは、断続的な問題を見逃すことがあります。"}
::option[比較用のデータをすべて破棄します。]{#incident-recovery-observation-period-b explanation="改善した内容は、以前の結果と照らし合わせて確認します。"}
:::

## まとめ

復旧後に、サービスの状態と利用者から見た動作を確かめられるようになりました。

1. 承認済みのバージョンと設定を特定します。
2. 利用者が見た症状を再度テストします。
3. 復旧確認を終える前に、合意したシグナルを観測します。
