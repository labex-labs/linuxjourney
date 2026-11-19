---
lesson_id: "incident-evidence-preservation"
course_id: "incident-response"
lang: "ja"
order_index: 2
title: "証拠の保全"
description: "練習用の記録、コピー、チェックサムを、後で確認できる状態で保存する方法を学びます。"
meta_title: "証拠の保全 - インシデント対応"
meta_description: "練習用の記録、コピー、チェックサムを、後で確認できる状態で保存する方法を学びます。"
meta_keywords: "証拠保全, チェックサム, インシデント対応, サイバーセキュリティ, Linux Journey"
---

対応中に何が起きたかを説明するのに、ログの抜粋が役立つことがあります。元の記録や承認済みのエクスポートを、別の確認担当者が内容を理解するために必要な情報と一緒に保全します。

## 記録の背景を残す

ホスト、情報源、タイムゾーン、対象時間帯を記録します。誰が収集し、どのフィルターを使ったかも残します。こうした情報がないと、コピーした 1 行が別のマシンの同じ文面と区別できない場合があります。

:::single-choice{#incident-evidence-preservation-context-fields} 同僚に届いたログの 1 行には、09:22 という時刻しか分かる情報がありません。何を補いますか？

::option[コピーを手元に保存したパスです。]{#incident-evidence-preservation-context-fields-b explanation="保存先が分かればコピーを探せますが、元の情報源や時刻の背景は分かりません。"}
::option[推測した原因です。]{#incident-evidence-preservation-context-fields-c explanation="収集に関する情報は、記録の解釈とは別に残します。"}
::option[収集元ホスト、タイムゾーン、収集対象の時間帯です。]{#incident-evidence-preservation-context-fields-a .correct explanation="確認担当者は、その行を正しい時系列に置けるようになります。"}
:::

## コピーを比較する

新しい練習用ディレクトリに無害なサンプルを 1 行保存し、コピーを作り、両方のファイルの SHA-256 値を計算します。使用するのは練習用ファイルだけです。書き込みを行うと、このディレクトリにある同名のファイルが置き換わります。

```bash
$ printf '%s\n' '09:22 UTC public homepage returned 503' > sample.log
$ cp sample.log review-copy.log
$ sha256sum sample.log review-copy.log
```

最初の列は内容のハッシュです。二つの値は一致するはずです。これで、確認した時点でコピーのバイト列が元のファイルと一致していることを確かめられます。元のイベントが正確に記録されたかどうかは、この確認では分かりません。

:::single-choice{#incident-evidence-preservation-copy-meaning} ハッシュが一致すれば何を裏付けられますか？

::option[元の記録のタイムスタンプは正確です。]{#incident-evidence-preservation-copy-meaning-a explanation="ハッシュで確認できるのはファイルの内容であり、時計の正確さは検証できません。"}
::option[確認用コピーのバイト列が、測定上サンプルと一致しています。]{#incident-evidence-preservation-copy-meaning-b .correct explanation="両方のハッシュは同じアルゴリズムで計算されています。"}
::option[コピーは一般公開を承認されています。]{#incident-evidence-preservation-copy-meaning-c explanation="承認で決まるのは誰がファイルを見られるかです。ハッシュからは分かりません。"}
:::

![練習用ファイルと確認用コピーでハッシュが一致したことを示す LabEx のチェックサム出力](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-evidence-preservation/matching-copy-hashes.png)

## 安全に共有できる確認用コピーを作る

元の記録には手を加えず、アクセスを制限します。別のチームに一部の項目だけが必要なら、別途抜粋を作り、そこから機密情報を取り除きます。情報を絞ったことを明記し、保護された元の記録を参照できるようにします。

:::single-choice{#incident-evidence-preservation-redact-copy} 共有のために機密情報を取り除く対象は、どのファイルですか？

::option[別途作った確認用の抜粋です。]{#incident-evidence-preservation-redact-copy-c .correct explanation="元の記録を保全しつつ、共有する内容を必要な範囲に絞れます。"}
::option[保護された元の記録です。すべてのコピーに変更を反映します。]{#incident-evidence-preservation-redact-copy-a explanation="保全すべき証拠が変わってしまいます。"}
::option[ファイルを変更しても同じに見えるよう、チェックサムのテキストを編集します。]{#incident-evidence-preservation-redact-copy-b explanation="測定した値と、その値に対応するファイルを保存します。"}
:::

## まとめ

別の確認担当者が内容を理解できる形で証拠を用意できるようになりました。

1. どこで、いつ資料を集めたかを記録します。
2. コピーのバイト列が元のファイルと一致することを確認します。
3. 共有時は別途作った抜粋から機密情報を取り除きます。
