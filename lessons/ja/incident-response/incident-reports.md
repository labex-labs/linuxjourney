---
lesson_id: "incident-reports"
course_id: "incident-response"
lang: "ja"
order_index: 6
title: "インシデント報告"
description: "観測した証拠と未解決の問いに基づいて、簡潔な状況報告を書く方法を学びます。"
meta_title: "インシデント報告 - インシデント対応"
meta_description: "観測した証拠と未解決の問いに基づいて、簡潔な状況報告を書く方法を学びます。"
meta_keywords: "インシデント報告, 引き継ぎ, インシデント対応, サイバーセキュリティ, Linux Journey"
---

短いインシデント報告があれば、別の人が調査を最初からたどらずに作業を引き継げます。影響を受けたサービス、時刻が分かる主な観測結果、次に行う作業を記載します。

## 観測結果を報告する

次はサービスのインシデントを想定した三つの模擬記録です。

```text
09:17 UTC  Deployment record: version 3 reached production
09:22 UTC  Visitor-path check: homepage returned 503
09:31 UTC  After rollback: version 2, homepage returned 200
```

これらの記録には、変更、失敗、復旧後の確認の成功が示されています。影響が出たパスと時刻を記載し、具体的に何を確認したかも残します。

:::single-choice{#incident-reports-report-claim} 記録から直接言えるのはどれですか？

::option[トップページの確認は 09:22 に失敗し、ロールバック後に成功しました。]{#incident-reports-report-claim-b .correct explanation="観測された結果を、起きた順にまとめています。"}
::option[バージョン 3 が確実にデータベースを壊しました。]{#incident-reports-report-claim-a explanation="記録には、障害が起きた仕組みは示されていません。"}
::option[時間帯の全体を通して、すべての利用者が影響を受けました。]{#incident-reports-report-claim-c explanation="示された結果は、すべてのリクエストを測定したものではありません。"}
:::

![本番環境の変更、503 エラー、復旧確認の成功を示す模擬インシデントの証拠](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-reports/evidence-timeline.png)

## まだ分からないことを説明する

ロールバック後にリクエストが成功した場合、デプロイを調査する理由になります。原因は、証拠が得られるまで未確定として扱います。例えば保守担当者は、リクエストが失敗した時間帯について、二つのバージョンのサービスログを比較できます。

:::single-choice{#incident-reports-uncertainty-statement} 未解決の事項として記載すべき文はどれですか？

::option[調べる価値があることは何もありません。]{#incident-reports-uncertainty-statement-b explanation="リリースとエラーの記録から、次に調べる対象を絞れます。"}
::option[サービスはその後もずっと利用できませんでした。]{#incident-reports-uncertainty-statement-c explanation="後から行ったテストリクエストは成功しており、この記述と矛盾します。"}
::option[503 の原因はまだ特定できていません。]{#incident-reports-uncertainty-statement-a .correct explanation="失敗と復旧確認の証拠はありますが、原因を裏付ける証拠はまだ必要です。"}
:::

## 次の担当者に作業を引き継ぐ

次の作業を誰ができるか、どの記録を見るか、どの結果が未解決事項の答えになるかを示します。広く共有する状況報告には、秘密情報や個人情報を含めないようにします。短い報告には、許可された担当者が参照できる保護済みの証拠へのリンクを添えられます。

:::single-choice{#incident-reports-useful-handoff} この事例で次に行う作業として最も適切なのはどれですか？

::option[時刻やサービスを指定せず、誰かにスクリーンショットを撮るよう頼みます。]{#incident-reports-useful-handoff-a explanation="障害のどの証拠が必要かが示されていません。"}
::option[サービスの保守担当者に、トップページのリクエストが失敗した時間帯のバージョン 3 のログを調べるよう依頼します。]{#incident-reports-useful-handoff-c .correct explanation="未解決の問いを調べるための情報源と時間帯を指定しています。"}
::option[保守担当者に、すでに成功したバージョン 2 の確認だけを繰り返すよう頼みます。]{#incident-reports-useful-handoff-b explanation="再度復旧を確認できますが、それ以前のバージョン 3 での失敗は説明できません。"}
:::

## 復旧を確認できた範囲を記録する

報告には、復旧の観測結果と、影響範囲がまだ確定していないことの両方を記載する場合があります。ロールバック後のトップページの確認が成功すれば、テストしたパスの復旧を裏付けられます。影響を受けた利用者を推定するには、障害の時間帯のリクエスト件数など、目的に合った観測結果がさらに必要です。

:::single-choice{#incident-reports-final-application} どの引き継ぎ文が、二種類の証拠について正確に説明していますか？

::option[1 件のリクエストが 200 を返したので、すべての利用者が再び利用できるようになりました。]{#incident-reports-final-application-b explanation="成功したリクエストが確認できたのは、テストしたパスと時刻に限られます。"}
::option[復旧確認が成功したので、以前の失敗は報告から除くべきです。]{#incident-reports-final-application-c explanation="以前の失敗もインシデントの証拠の一部です。"}
::option[ロールバック後にトップページの確認は成功しましたが、影響を受けたリクエストの総数はまだ分かりません。]{#incident-reports-final-application-a .correct explanation="検証済みの復旧結果と、現時点の記録では分からない件数を区別しています。"}
:::

パケットとホストの証拠を扱う練習の後、さらに時間をかけて取り組む演習として [SOC 基礎の総復習](https://labex.io/courses/project-soc-foundations-review)を参照してください。

## まとめ

確認した事実、未確定の点、次の作業を添えて、インシデントを引き継げるようになりました。

1. 影響を受けたパスと、観測結果の時系列を記載します。
2. 考えられる原因と、確認済みの証拠を区別します。
3. 情報源と時間帯を示し、次の調査を担当者に割り当てます。
