---
lesson_id: "system-audit-events"
course_id: "system-auditing"
lang: "ja"
order_index: 1
title: "監査イベント"
description: "保護されたファイルについて知りたいことに合わせて、監査対象のイベントを選ぶ方法を学びます。"
meta_title: "監査イベント - システム監査"
meta_description: "保護されたファイルについて知りたいことに合わせて、監査対象のイベントを選ぶ方法を学びます。"
meta_keywords: "監査イベント, 監査レコード, システム監査, サイバーセキュリティ, Linux Journey"
---

サービスログには、ページが読み込まれたといった情報が残ります。**監査レコード**には、サービス設定への書き込みなど、システムが観測するよう設定された操作が記録されます。まず、どの操作を確認したいか、その確認に何の情報が必要かを決めます。

## 監査で確かめたいことを決める

Web サービスの設定で、誰がプレビューを開けるかを制御しているとします。このファイルの変更を調べるには、対象、操作、時刻、関係するアカウント、結果が記録されていると役立ちます。それぞれの情報から、操作の一部分を再現できます。

:::single-choice{#system-audit-events-choose-object} この調査のため、監査レコードでは何を特定できる必要がありますか？

::option[その日の Web リクエストの件数だけです。]{#system-audit-events-choose-object-b explanation="リクエスト件数が示すのは別の活動です。"}
::option[操作の対象となった設定ファイルです。]{#system-audit-events-choose-object-a .correct explanation="対象が分かれば、ほかのファイルへの書き込みと区別できます。"}
::option[書き込みなど、操作の種類だけです。]{#system-audit-events-choose-object-c explanation="操作の種類からは何を試みたかが分かります。その操作が調査に関係するかは、対象ファイルを確認して判断します。"}
:::

## 操作の結果を読む

レコードには、書き込みが成功したことも、試みが失敗したことも記録されます。操作と結果を一緒に確認します。書き込みが拒否された記録も、試みがあったことを示す証拠になります。書き込みが成功した場合とは、導ける結論が異なります。

:::single-choice{#system-audit-events-operation-result} レコードには、設定への書き込みと、結果が拒否だったことが記録されています。何が分かりますか？

::option[記録された書き込みの試みが拒否されました。]{#system-audit-events-operation-result-b .correct explanation="操作と結果をあわせて読むと、何が観測されたかが分かります。"}
::option[ファイルが確実に置き換えられました。]{#system-audit-events-operation-result-a explanation="拒否の結果は、変更が成功したことを示しません。"}
::option[目的のページが HTTP 200 を返しました。]{#system-audit-events-operation-result-c explanation="ここにはページへのリクエストは記録されていません。"}
:::

## 監査の対象範囲を確認する

監査システムで記録できるのは、監査の仕組みとポリシーで観測できるイベントです。検索結果が空であることを根拠にする前に、ポリシーが必要なパス、操作、時間帯を対象にしていたか確認します。調べた情報源も記録します。

:::single-choice{#system-audit-events-empty-audit} 選んだログに書き込みの記録がありません。書き込みがなかったと結論を出す前に、何を確認すると役立ちますか？

::option[インストール済みのエディターの数を数えます。]{#system-audit-events-empty-audit-a explanation="インストール済みのソフトウェアからは監査の対象範囲は分かりません。"}
::option[同じ時間帯を別のアカウント名だけで検索します。]{#system-audit-events-empty-audit-b explanation="記録が確実に収集されていれば、追加の検索は役立ちます。まず対象のイベントが記録され得たかを確認します。"}
::option[監査ポリシーと、利用できる記録の時間範囲を確認します。]{#system-audit-events-empty-audit-c .correct explanation="監査の範囲から外れていると、実際に操作が行われても該当する記録が残らないことがあります。"}
:::

## まとめ

保護されたリソースについて、どの監査証拠が役立つかを選べるようになりました。

1. 確認したい操作と対象を特定します。
2. 何が試みられたかと、その結果をあわせて読みます。
3. 検索結果が空であることを証拠とする前に、監査の対象範囲を確認します。
