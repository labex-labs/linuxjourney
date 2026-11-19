---
lesson_id: "service-troubleshooting"
course_id: "service-monitoring"
lang: "ja"
order_index: 7
title: "サービスのトラブルシューティング"
description: "サービスの停止、依存先のエラー、リクエストの遅延について、次に何を確認するかを学びます。"
meta_title: "サービスのトラブルシューティング - サービス監視"
meta_description: "サービスの停止、依存先のエラー、リクエストの遅延について、次に何を確認するかを学びます。"
meta_keywords: "トラブルシューティング, サービス監視, DevOps, Linux Journey"
---

トップページへのリクエストが失敗したなど、具体的な症状を一つ選びます。次に、同じ時刻の前後に、利用者にとって意味のある場所から得られた観測結果を比較します。

## サーバーが停止したとき

最初の例では、ブラウザーが接続を拒否されたと表示し、サービスのコンテナは `Exited (1)` と表示されています。この二つの情報を手掛かりに、保存されているログからプログラムが停止した理由を調べます。ほかのイベントと比較するときは、終了時刻を確認します。

:::single-choice{#service-troubleshooting-stopped-case} 停止したプロセスの状況を説明する手掛かりとして、最も有力なものはどれですか？

::option[同じトップページに再度リクエストを送り、最新の状態を確認します。]{#service-troubleshooting-stopped-case-a explanation="再試行では症状を確認できます。プログラムが終了した理由は、残っているログに記録されていることがあります。"}
::option[コンテナに残っている最後のログを読みます。]{#service-troubleshooting-stopped-case-b .correct explanation="起動時や終了時のメッセージで、プログラムがどこで止まったか分かることがあります。"}
::option[同じイメージを使う別の稼働中のコンテナのログを確認します。]{#service-troubleshooting-stopped-case-c explanation="別のコンテナは実行履歴が異なり、同じ障害が起きていないかもしれません。"}
:::

## 依存先でエラーが起きたとき

二つ目の例では、Web プロセスは稼働中ですが、ページはサーバーエラーを返します。ログには、リクエスト `r17` の処理中にカタログへの問い合わせがタイムアウトしたとあります。そこで依存先から同じリクエストの記録を探します。最初に接続するサービスが正常でも、後続のサービスに問題がある場合があります。

:::single-choice{#service-troubleshooting-dependency-case} r17 について、次にどの証拠を探しますか？

::option[そのリクエストと時刻に対応するカタログの記録です。]{#service-troubleshooting-dependency-case-a .correct explanation="依存先への呼び出しで何が起きたかを確認できます。"}
::option[保存された Docker イメージのサイズです。]{#service-troubleshooting-dependency-case-b explanation="稼働中のサービスへの呼び出しで何が起きたかは分かりません。"}
::option[昨日行った、別のトップページのチェックの成功結果です。]{#service-troubleshooting-dependency-case-c explanation="異なる時刻のチェックなので、このリクエストの説明には使えません。"}
:::

## リクエストが遅くなったとき

三つ目の例では、大半の応答は成功していますが、利用者から遅延が報告されています。ワーカーの待ち行列が伸びた時間帯に、レイテンシも上昇しています。原因を決める前に、リクエスト量とワーカーの動きを確認します。変更を加えたら、利用者に近い条件で同じ確認を繰り返し、同じシグナルを見直します。

:::single-choice{#service-troubleshooting-slow-case} この例で、変更の効果を確認するには何を比較するのが最適ですか？

::option[変更前後のソースリポジトリのスクリーンショットです。]{#service-troubleshooting-slow-case-a explanation="スクリーンショットからは、リクエスト時間も待ち行列も測れません。"}
::option[キャッシュのサイズとデプロイ済みのブランチ数です。]{#service-troubleshooting-slow-case-b explanation="どちらからも報告された待ち時間については分かりません。"}
::option[変更前後の同程度の条件での利用者のリクエスト時間と、ワーカーの待ち行列です。]{#service-troubleshooting-slow-case-c .correct explanation="発端となった症状と、原因と考えられる処理能力の制約の両方を確認できます。"}
:::

## 確認結果が食い違うとき

ホスト上のチェックは成功するのに、利用者にはエラーが出続ける場合を考えます。それぞれのチェックが通った経路を記録します。ホスト上のチェックではプロセスがそこで応答すると分かり、クライアントからのリクエストではホストまでの経路の問題が見つかることがあります。

:::single-choice{#service-troubleshooting-final-application} 影響を受けた利用者について追加調査を行うとき、どの結果を手掛かりにしますか？

::option[利用者と同じ場所や経路から行ったチェックです。]{#service-troubleshooting-final-application-a .correct explanation="報告された症状が発生したサービスの範囲を観測できます。"}
::option[ホスト上だけで確認した結果です。]{#service-troubleshooting-final-application-b explanation="問題が起きている範囲を絞る手掛かりになりますが、外部からの経路は確認できません。"}
::option[イメージレジストリの現在の容量です。]{#service-troubleshooting-final-application-c explanation="レジストリでイメージを配信できても、利用者向けの経路には別の問題があり得ます。"}
:::

## まとめ

得られた証拠に合わせて、次に何を確認すべきかを選べるようになりました。

1. プロセスの状態とログから停止の理由を調べます。
2. 失敗したリクエストを依存先まで追跡します。
3. 利用者が当初見た症状を基準に、改善したかを確認します。
