---
lesson_id: "web-certificates"
course_id: "web-security"
lang: "ja"
order_index: 3
title: "証明書"
description: "TLS 証明書に記載された名前、有効期間、発行者の確認方法を学びます。"
meta_title: "証明書 - Web セキュリティ"
meta_description: "TLS 証明書に記載された名前、有効期間、発行者の確認方法を学びます。"
meta_keywords: "TLS 証明書, 有効期間, Web セキュリティ, サイバーセキュリティ, Linux Journey"
---

ブラウザーは、URL が示す Web サイトに接続できたことを確かめる必要があります。TLS の**証明書**には、サーバーの識別情報と公開鍵が含まれます。ブラウザーは、その識別情報を信頼する前に複数の項目を確認します。

## 証明書の名前を確認する

GitHub で[公開されている練習用証明書](https://github.com/labex-labs/linuxjourney/blob/master/examples/web-security/site-cert.pem)のページを開き、ファイルを `site-cert.pem` として保存します。これは学習用の自己署名証明書です。OpenSSL で発行者、有効期間、サブジェクト代替名を表示します。`-noout` オプションで、エンコードされた証明書本体の表示を省略できます。

```bash
$ openssl x509 -in site-cert.pem -noout -issuer -dates -ext subjectAltName
```

**サブジェクト代替名**の欄には、この証明書の対象となる DNS 名が並びます。`DNS:site.example` を探します。ブラウザーは、URL のホスト名を証明書の名前と照合します。

:::single-choice{#web-certificates-wrong-name} 記載された名前は site.example だけです。どの URL がこの名前に一致しますか？

::option[`https://site.example/`]{#web-certificates-wrong-name-b .correct explanation="証明書の DNS 名が URL のホストと一致します。"}
::option[`https://other.example/`]{#web-certificates-wrong-name-a explanation="練習用の証明書に記載されているのは別の名前です。"}
::option[`https://preview.site.example/`]{#web-certificates-wrong-name-c explanation="証明書で対象となっていない限り、サブドメインは別の名前として扱われます。"}
:::

![練習用証明書の発行者、有効期間、DNS 名 site.example を示す OpenSSL の出力](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-certificates/dns-name-and-validity.png)

## 有効期間を確認する

`notBefore` と `notAfter` は、証明書を使える期間を示します。この日付をテスト時の時刻と比較します。時計に問題があると、確認結果にも影響することがあります。有効期間は、証明書の検証で確認する項目の一つです。

:::single-choice{#web-certificates-validity-period} 現在時刻が notAfter を過ぎています。何を確認しますか？

::option[証明書に正しい DNS 名があるかどうかです。]{#web-certificates-validity-period-b explanation="名前はサーバーの識別に重要です。名前が一致していても、期限切れの証明書は有効期間外です。"}
::option[あるユーザーのパスワードが変わったかどうかです。]{#web-certificates-validity-period-c explanation="アプリケーションへのログインと、証明書の有効期間は別の問題です。"}
::option[証明書の期限が切れ、更新が必要かどうかです。]{#web-certificates-validity-period-a .correct explanation="接続先は、記載された有効期間を過ぎた証明書を提示しています。"}
:::

## 証明書の信頼性を確認する

**発行者**は証明書に署名した主体です。ブラウザーは通常、信頼する認証局につながる証明書チェーンに沿って署名を検証します。OpenSSL が表示する発行者名は、その証明書の項目として確認できます。チェーンの検証には別の操作が必要です。練習用の証明書は、ラボ内だけで使うことを想定している場合があります。

:::single-choice{#web-certificates-trust-check} 名前と有効期間は合っていますが、ブラウザーは署名者を信頼していません。何が足りませんか？

::option[証明書の有効期間の複製です。]{#web-certificates-trust-check-a explanation="有効期間が一致しても、その身元を誰が保証するかは分かりません。"}
::option[この接続で使える、信頼された認証局につながる有効な証明書チェーンです。]{#web-certificates-trust-check-c .correct explanation="ブラウザーは、名前の一致、有効期間内であること、チェーンの信頼性を確認する必要があります。"}
::option[Web サイトの別のユーザー名です。]{#web-certificates-trust-check-b explanation="証明書の信頼性は、通常のアプリケーション認証より先に判断されます。"}
:::

## まとめ

証明書の確認で役立つ三つの項目を読めるようになりました。

1. URL のホスト名と、証明書の対象名を照合します。
2. 現在時刻を証明書の有効期間と比較します。
3. 証明書チェーンの信頼性は別途確認します。
