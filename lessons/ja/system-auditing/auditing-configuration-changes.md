---
lesson_id: "auditing-configuration-changes"
course_id: "system-auditing"
lang: "ja"
order_index: 5
title: "設定変更"
description: "承認済みの変更、ファイルの差分、監査イベントを照らし合わせる方法を学びます。"
meta_title: "設定変更 - システム監査"
meta_description: "承認済みの変更、ファイルの差分、監査イベントを照らし合わせる方法を学びます。"
meta_keywords: "設定変更, 差分, システム監査, サイバーセキュリティ, Linux Journey"
---

変更チケットには予定された作業が記録されます。ファイルを比較すると、現在どこに差があるか分かります。監査イベントは、監査の対象範囲で観測された操作を示します。この三つを用いて、設定変更について何が言えるかを整理します。

## 想定された変更と照合する

次の模擬保守記録を確認します。

```text
Approved: change banner.txt mode to 640
Window: 09:00–09:30 UTC
Host: web-01
```

どのファイルのどの属性の変更が承認されたかが示されています。同じ時間帯に生じた差分でも、対象が異なれば別の説明が必要です。

:::single-choice{#auditing-configuration-changes-approve-scope} 記載された承認内容に一致する変更はどれですか？

::option[web-01 で site.conf の内容が変わりました。]{#auditing-configuration-changes-approve-scope-b explanation="その設定ファイルは承認の対象外です。"}
::option[別のホストから banner.txt が消えました。]{#auditing-configuration-changes-approve-scope-c explanation="報告された操作もホストも承認内容と異なります。"}
::option[web-01 で banner.txt のモードが 640 になりました。]{#auditing-configuration-changes-approve-scope-a .correct explanation="ファイル、属性、ホスト、変更後の状態のすべてが承認記録と一致します。"}
:::

## 観測結果を比較する

比較の結果、バナーのモードが変わり、`site.conf` の内容も変わったことが分かりました。別の監査イベントには、09:15 に `web-01` 上の `site.conf` に書き込みがあったと記録されています。監査イベントのおかげで調査すべき時刻が分かります。承認の有無を判断するには、別の情報が必要です。

:::single-choice{#auditing-configuration-changes-source-comparison} site.conf に関する二つの観測から、どの結論を導けますか？

::option[書き込みは保守時間帯に行われたので承認済みです。]{#auditing-configuration-changes-source-comparison-a explanation="チケットに記載されているのは別の操作です。"}
::option[書き込みの記録と内容の差分があるため、このファイルは詳しく確認する価値があります。]{#auditing-configuration-changes-source-comparison-b .correct explanation="ファイルの比較で差分が分かり、監査イベントで時刻を絞れます。"}
::option[バナーの変更が書き込みの原因です。]{#auditing-configuration-changes-source-comparison-c explanation="この観測から、一方の操作が他方を引き起こしたとは判断できません。"}
:::

## 調査メモを書く

どの差分が計画どおりで、どれがまだ説明できないかを書きます。ファイル、ホスト、時刻、参照した記録を含めます。次の手順として、現行の設定を承認済みのコピーと比べ、別の承認済み変更に該当するかを確認します。

:::single-choice{#auditing-configuration-changes-useful-review} site.conf について、引き継ぎには何を書きますか？

::option[差分を明記し、観測された書き込みを引用し、その書き込みの承認記録を確認するよう依頼します。]{#auditing-configuration-changes-useful-review-c .correct explanation="証拠と未解決の確認事項がメモに残ります。"}
::option[承認済みと記し、パスは省略します。]{#auditing-configuration-changes-useful-review-a explanation="変更対象が分からなくなり、記録にない承認を仮定することになります。"}
::option[バナーを変更した担当者の操作として記録します。]{#auditing-configuration-changes-useful-review-b explanation="記録からは、その担当者の操作だと確認できません。"}
:::

## 二つの保守記録を比較する

別のチケットで、それより後の site.conf の編集が承認されています。調査を終える前に、観測された時刻、対象ホスト、ファイルをチケットと照合します。対象ファイルが正しくても、後の承認でそれより前のイベントを説明できるとは限りません。

:::single-choice{#auditing-configuration-changes-final-application} チケットは 09:40 から 10:00 の web-01 上の site.conf を対象としています。09:15 に記録された書き込みについて、何が未確認ですか？

::option[チケット管理システムとは別に site.conf が存在するかどうかです。]{#auditing-configuration-changes-final-application-b explanation="ファイルの比較ですでに設定ファイルの存在が確認されています。"}
::option[後から発行されたチケットで、それまでの書き込みをすべて説明できるかどうかです。]{#auditing-configuration-changes-final-application-c explanation="承認は指定された操作と時間帯に適用されます。"}
::option[先に行われた書き込みに別の承認があるかどうかです。]{#auditing-configuration-changes-final-application-a .correct explanation="ホストとパスは一致しますが、記録された時刻は承認時間帯の外です。"}
:::

## まとめ

設定変更について何が分かっているかを、記録から組み立てられるようになりました。

1. 承認済みの変更から予定された範囲を読み取ります。
2. 差分と監査イベントから、観測された事実を説明します。
3. 証拠が足りない箇所を明確にし、次に何を確認するかを決めます。
