---
lesson_id: "file-integrity-baselines"
course_id: "system-auditing"
lang: "ja"
order_index: 4
title: "整合性のベースライン"
description: "整合性レポートを読み、新しいベースラインをいつ承認すべきかを学びます。"
meta_title: "整合性のベースライン - システム監査"
meta_description: "整合性レポートを読み、新しいベースラインをいつ承認すべきかを学びます。"
meta_keywords: "整合性ベースライン, ファイル整合性, システム監査, サイバーセキュリティ, Linux Journey"
---

**ベースライン**とは、ある時点で期待されるファイルの属性を記録した、信頼できる基準です。後から整合性を確認するときに、現在のファイルをその基準と比べ、違いを報告できます。

## 差分レポートを読む

この模擬レポートの抜粋では、ホストを直近の承認済みの状態と比較しています。

```text
File                      Property  Previous  Current
/etc/journey/site.conf    content   hash-A    hash-B
/etc/journey/banner.txt   mode      644       640
/etc/journey/site.prev    present   yes       no
```

最初の行はファイル内容の変化を示し、2 行目はアクセス権限の変化を示します。3 行目は、以前は追跡対象だったファイルが確認時になかったことを示します。

:::single-choice{#file-integrity-baselines-report-mode} アクセス権限が変わったことを示すのはどの行ですか？

::option[site.conf の行です。]{#file-integrity-baselines-report-mode-a explanation="この行は、内容のハッシュが変わったことを示します。"}
::option[banner.txt の行です。]{#file-integrity-baselines-report-mode-b .correct explanation="モードが 644 から 640 に変わりました。"}
::option[site.prev の行です。]{#file-integrity-baselines-report-mode-c explanation="この行は、そのパスが存在したかどうかを示します。"}
:::

![ファイルの内容、アクセスモード、存在の有無を比較する模擬整合性レポート](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/file-integrity-baselines/reference-comparison.png)

## 比較に使う基準を確認する

レポートを判断に使うには、それ以前の基準が信頼できる必要があります。どの基準を使ったかと、その作成日を記録します。すでに問題が起きていた時点のファイルを基準にすると、比較結果を誤って解釈するおそれがあります。ベースラインがどの承認済み状態を表すかを確認します。

:::single-choice{#file-integrity-baselines-reference-source} 今日の設定を確認するために、最も役立つベースラインはどれですか？

::option[変更前に記録して承認されたコピーです。]{#file-integrity-baselines-reference-source-a .correct explanation="確認担当者が検証できる、由来の分かっている基準です。"}
::option[変更理由が分からない今日のファイルから作成した基準です。]{#file-integrity-baselines-reference-source-b explanation="確認前に差分が新しい基準に取り込まれてしまいます。"}
::option[比較の背景が分からない、無関係なホストの設定です。]{#file-integrity-baselines-reference-source-c explanation="ホストの役割が異なれば、想定されるファイルや権限も異なります。"}
:::

## 基準を更新する前に差分を確認する

それぞれの差分を承認済みの変更と照合し、サービスの動作を確認します。バナーのモード変更が計画どおりで、設定の変更は計画外なら、個別に調べます。許可された差分の内容が分かり、承認を得てから基準を更新します。以前の基準の記録も保管します。

:::single-choice{#file-integrity-baselines-update-timing} バナーのモード変更は承認済みですが、site.conf の変更は説明できていません。新しいベースラインを受け入れる前に何をしますか？

::option[1 行が想定どおりなので、すべてを承認します。]{#file-integrity-baselines-update-timing-a explanation="ファイルの差分はそれぞれ別の変更を表します。"}
::option[差分レポートを捨てます。]{#file-integrity-baselines-update-timing-b explanation="レポートには、まだ調べるべき項目が残っています。"}
::option[理由が分からない site.conf の変更を調査します。]{#file-integrity-baselines-update-timing-c .correct explanation="現状を確認したうえで、新しいベースラインを作ります。"}
:::

練習環境で整合性の基準を作って比較するには、[ファイル整合性監視](https://labex.io/tutorials/linux-file-integrity-monitoring-fim-656122)を試してください。

## まとめ

ベースラインを、特定の比較のための証拠として使えるようになりました。

1. レポートで、内容、モード、存在の有無を区別します。
2. 比較に使う基準が信頼できる状態を表すことを確認します。
3. 新しい基準を受け入れる前に、想定外の差分を調べます。
