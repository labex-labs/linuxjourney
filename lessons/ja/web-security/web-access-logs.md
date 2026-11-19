---
lesson_id: "web-access-logs"
course_id: "web-security"
lang: "ja"
order_index: 7
title: "Web アクセスログ"
description: "認証情報を漏らさずに HTTP アクセスログを読み、サービスが何を返したかを調べる方法を学びます。"
meta_title: "Web アクセスログ - Web セキュリティ"
meta_description: "認証情報を漏らさずに HTTP アクセスログを読み、サービスが何を返したかを調べる方法を学びます。"
meta_keywords: "Web アクセスログ, HTTP, Web セキュリティ, サイバーセキュリティ, Linux Journey"
---

Web サーバーは、リクエストごとに 1 件の**アクセスログ**を残せます。ログには時刻、パス、応答コード、リクエスト ID などが含まれることがあります。調査で知りたいことに必要な項目だけを使います。

## リクエストの結果を読む

この模擬ログの抜粋では、各項目に名前が付いています。二つのリクエストは異なるパスに送られました。

```text
t=09:18:01Z request=r31 method=GET path=/health status=200
t=09:18:04Z request=r32 method=GET path=/staff status=403
```

`403` は、サービスがリクエストを拒否したことを示します。その応答を別の記録と照合する前に、正確なパスとリクエスト ID を確認します。

:::single-choice{#web-access-logs-log-result} 拒否された理由を調べるために、どのリクエストを追いますか？

::option[/health への r31 です。]{#web-access-logs-log-result-a explanation="この行は、ヘルスチェックの成功を示しています。"}
::option[/staff への r32 です。]{#web-access-logs-log-result-b .correct explanation="ステータスは 403 で、この抜粋で拒否されたリクエストです。"}
::option[両方を同じリクエストとして扱います。]{#web-access-logs-log-result-c explanation="ID とパスで二つを区別できます。"}
:::

## アクセス判定の記録を探す

アクセスログからはサーバーが何を返したかが分かります。なぜその権限判定になったかまでは記録されない場合があります。アプリケーションが認可の判定も記録しているなら、リクエスト ID と時刻を照合します。この例では、どのルールが適用されたかを確認できます。

:::single-choice{#web-access-logs-refusal-reason} アクセスログに 403 とあります。理由を知るために最も役立つ追加の記録はどれですか？

::option[r32 に対するアプリケーションの権限判定です。]{#web-access-logs-refusal-reason-a .correct explanation="対応する記録に、どのルールが適用されたかが記載されていることがあります。"}
::option[別のサイトの成功応答です。]{#web-access-logs-refusal-reason-b explanation="この拒否との関連はありません。"}
::option[以前のヘルスチェック用パスへのリクエストです。]{#web-access-logs-refusal-reason-c explanation="別の操作とその結果の記録です。"}
:::

## 認証情報をログに残さない

完全なセッション Cookie や認可トークンなど、他人のセッションを使える値はログに記録しないようにします。トラブルシューティングには、リクエスト ID と応答ステータスを使えます。ログのサンプルを共有する際は機密項目を除き、調査に必要な情報だけを残します。

:::single-choice{#web-access-logs-safe-fields} 認証情報をコピーせず、拒否されたリクエストを追跡するのに役立つ組み合わせはどれですか？

::option[完全なセッション Cookie とアカウントのパスワードです。]{#web-access-logs-safe-fields-a explanation="どちらも機密情報であり、共有ログに含めないようにします。"}
::option[認可トークンと公開パスです。]{#web-access-logs-safe-fields-b explanation="パスは調査に役立ちますが、トークンは秘密にすべき認証情報です。"}
::option[リクエスト ID とその応答ステータスです。]{#web-access-logs-safe-fields-c .correct explanation="セッションの値を明かさずに、関連する記録と照合できます。"}
:::

## 必要な部分だけを共有する

確認担当者が拒否されたリクエストの背景を知りたいとします。時刻、ID、メソッド、機密情報を除いたパス、ステータスで足りるなら、それらだけを残します。パスのクエリ文字列に非公開の値が含まれる場合があります。共有前に抜粋を確認します。

:::single-choice{#web-access-logs-final-application} この確認に最も適した抜粋はどれですか？

::option[常にリクエスト全体とすべてのヘッダーを含む抜粋です。]{#web-access-logs-final-application-b explanation="リクエストには認証情報や、調査に不要な個人データが含まれることがあります。"}
::option[すべての識別子を除いたステータスコードだけです。]{#web-access-logs-final-application-c explanation="コードだけでは対応するポリシーの記録を探しにくくなります。"}
::option[機密情報を除いたパス、リクエストの時刻と ID、応答ステータスを含む抜粋です。]{#web-access-logs-final-application-a .correct explanation="セッションの値を共有せず、記録の照合に必要な項目を残せます。"}
:::

## まとめ

基本的なアクセスログを読み、必要な情報を安全に残せるようになりました。

1. リクエスト ID、パス、応答を照合します。
2. 理由を知る必要がある場合は、対応するポリシー判定の記録を探します。
3. 収集するログや共有するログに認証情報を含めないようにします。
