---
lesson_id: "incident-containment"
course_id: "incident-response"
lang: "ja"
order_index: 4
title: "封じ込め"
description: "承認を受けた封じ込めの選択肢を、目的、影響、保全すべき証拠に照らして比較する方法を学びます。"
meta_title: "封じ込め - インシデント対応"
meta_description: "承認を受けた封じ込めの選択肢を、目的、影響、保全すべき証拠に照らして比較する方法を学びます。"
meta_keywords: "封じ込め, インシデント対応, サイバーセキュリティ, Linux Journey"
---

**封じ込め**は、チームが調査する間に被害の拡大を抑えるための短期的な措置です。どの措置が適切かは、影響の範囲と、利用者に引き続き必要なアクセスによって変わります。

## 制限する範囲を決める

内部向けのプレビュー画面に公開経路からアクセスできる一方、トップページは公開を続ける必要があるとします。プレビューへの経路を制限する方法と、より広い措置としてサイト全体を停止する方法があります。それぞれで何が変わるかを比較します。

:::single-choice{#incident-containment-narrow-action} 公開のプレビューアクセスをなくし、トップページは利用できる状態に保つには、どの措置が適切ですか？

::option[用途に関係なく、すべての公開経路を無効にします。]{#incident-containment-narrow-action-b explanation="トップページにもアクセスできなくなります。"}
::option[影響のあるプレビュー経路を制限し、両方の経路を確認します。]{#incident-containment-narrow-action-a .correct explanation="報告された公開範囲に絞って対処し、必要なサービスが使えることも確かめます。"}
::option[プレビューサービスのラベルを変更します。]{#incident-containment-narrow-action-c explanation="ラベルを変更してもリクエストの到達は防げません。"}
:::

## 証拠の保全とアクセスを計画する

対応計画を確認し、変更を行う権限を持つ担当者に相談します。承認者、措置を続ける予定の期間、状況が許す場合に事前に保全する証拠を記録します。措置によってサービスログの記録や対応担当者のアクセスが途切れないかを考えます。

:::single-choice{#incident-containment-action-impact} 隔離措置を取ると、調査担当者が記録を取得できなくなるおそれがあります。チームで何を確認しますか？

::option[何を保全するかと、許可された対応担当者のアクセスをどう確保するかです。]{#incident-containment-action-impact-b .correct explanation="封じ込めの目的と調査に必要な作業の両方を考慮できます。"}
::option[設定ファイルの名前が短いかどうかだけです。]{#incident-containment-action-impact-a explanation="ファイル名を確認しても、記録やアクセスの保全にはなりません。"}
::option[全員が再接続できるように認証情報を公開するかどうかです。]{#incident-containment-action-impact-c explanation="認証情報を保護し、アクセスは引き続き制御する必要があります。"}
:::

## 封じ込めの結果を確認する

想定外の経路が閉じたことを確認します。想定どおりの経路は個別にテストし、変更の副作用を確かめます。変更を行った時刻と、チームが再評価する予定時刻を記録します。封じ込めが成功しても、根本原因の調査は続くことがあります。

:::single-choice{#incident-containment-containment-success} 公開のプレビュー経路は閉じ、トップページは引き続き利用できます。どの説明が確認結果に沿っていますか？

::option[根本原因は確実に解消されました。]{#incident-containment-containment-success-a explanation="確認できたのはアクセス範囲です。修復が完了したかは別途調べる必要があります。"}
::option[プレビューへの経路として考えられるものはすべてテスト済みです。]{#incident-containment-containment-success-b explanation="確認の対象は、実際にテストした経路です。"}
::option[テストした公開プレビュー経路は遮断され、必要なトップページは利用できます。]{#incident-containment-containment-success-c .correct explanation="検証した範囲の結果を報告しています。"}
:::

## まとめ

短期的な封じ込め措置を評価できるようになりました。

1. 措置で制限する経路やアクセスを明記します。
2. 承認、保全すべき証拠、想定される影響を確認します。
3. 意図した制限と、必要なサービスの動作を個別に検証します。
