---
lesson_id: "service-logs"
course_id: "service-monitoring"
lang: "ja"
order_index: 2
title: "サービスログ"
description: "リクエスト ID と時刻を使い、複数のサービスログから同じリクエストを追う方法を学びます。"
meta_title: "サービスログ - サービス監視"
meta_description: "リクエスト ID と時刻を使い、複数のサービスログから同じリクエストを追う方法を学びます。"
meta_keywords: "サービスログ, リクエスト ID, サービス監視, DevOps, Linux Journey"
---

利用者の画面にエラーが出たとき、サービスログを見ると、そのリクエストがどの処理で失敗したか分かることがあります。まず時刻を確認し、同じリクエストの記録に引き継がれる**リクエスト ID** を探します。

## 一つのリクエストを読む

次の例には二つのサービスが登場します。**依存先**とは、あるプログラムが処理を完了するために必要とするサービスです。ここでは Web サービスがカタログサービスに項目の一覧を求めています。

```text
09:14:02 service=web     request=r17 path=/items status=502
09:14:02 service=catalog request=r17 action=read result=timeout
09:14:03 service=catalog request=r18 action=read result=ok
```

Web サービスの行には、`r17` の応答が失敗したとあります。同じ ID のカタログの行には、タイムアウトが記録されています。時刻の近いカタログの成功記録は、`r18` に属します。

:::single-choice{#service-logs-matching-request} Web サービスの r17 の失敗に対応するカタログの結果はどれですか？

::option[r18 の成功です。]{#service-logs-matching-request-a explanation="その行は別のリクエストの記録です。"}
::option[カタログの両方の結果です。]{#service-logs-matching-request-c explanation="時刻が近くても、別々のリクエストの場合があります。"}
::option[r17 のタイムアウトです。]{#service-logs-matching-request-b .correct explanation="共通の ID で、同じリクエストの二つの記録を結び付けられます。"}
:::

## サンプルを絞り込む

上の 3 行を練習用ディレクトリに `requests.log` として保存します。`grep -F` で文字列をそのまま検索します。このサンプルでフィールドの境界まで一致させるため、ID の直後の空白も含めます。

```bash
$ grep -F 'request=r17 ' requests.log
```

`r17` の Web サービスとカタログサービスの行が表示されます。実際のログでは形式が変わったり、リクエスト ID がなかったりすることがあります。検索するフィールドがどのサービスでも同じ意味を持つことを確認してください。

:::single-choice{#service-logs-choose-filter} timeout という単語だけで検索する場合と比べ、リクエストのフィールド全体で検索する利点は何ですか？

::option[すべてのトラフィックで同じエラーが起きたと確認できます。]{#service-logs-choose-filter-b explanation="ここで絞り込めるのは一つのリクエストの記録です。"}
::option[timeout が片方にしかなくても、Web とカタログの両方から該当する記録を得られます。]{#service-logs-choose-filter-a .correct explanation="共通の ID を使うと、両方のサービスでそのリクエストを追えます。"}
::option[ログが書き換わり、後の検索で正しい結果が出るようになります。]{#service-logs-choose-filter-c explanation="grep はファイルを読み、一致する行を表示します。"}
:::

![リクエスト r17 の Web エラーとカタログのタイムアウトを対応付ける grep の出力](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-logs/request-id.png)

## 報告できる範囲を見極める

タイムアウトから、このリクエストがどこで失敗したかを絞り込めます。カタログ内部のどの要素で処理が遅れたかを知るには、依存先自身の指標や直近の記録を確認します。チームメンバーにログの抜粋を渡すときは、リクエスト ID を残し、相手に不要な秘密情報や個人データは除きます。

:::single-choice{#service-logs-evidence-limit} 最初の報告には何を記載しますか？

::option[r17 の処理中にカタログがタイムアウトしたため、カタログ側を詳しく調べる必要があります。]{#service-logs-evidence-limit-c .correct explanation="関連する記録から分かることを、原因を推測せずにまとめています。"}
::option[カタログへのリクエストはすべてタイムアウトしました。]{#service-logs-evidence-limit-a explanation="サンプルには別のカタログリクエストの成功記録があります。"}
::option[データベースの特定のディスクが故障しました。]{#service-logs-evidence-limit-b explanation="記録にはディスクに関する観測結果がありません。"}
:::

Linux ホストでサービスの記録を検索する練習には、[インシデント対応のためのログ分析](https://labex.io/labs/linux-monitoring-and-incident-response-log-analysis-594586)を試してください。

## まとめ

一つのリクエストを複数のサービスログで追跡できるようになりました。

1. 関連する記録のリクエスト ID を照合します。
2. 固定文字列で検索して、サンプルの絞り込みを行います。
3. 記録から分かることを報告し、次に調べることを決めます。
