---
lesson_id: "web-https"
course_id: "web-security"
lang: "ja"
order_index: 2
title: "HTTPS"
description: "Web リクエストの経路のうち、HTTPS で保護される部分を見分ける方法を学びます。"
meta_title: "HTTPS - Web セキュリティ"
meta_description: "Web リクエストの経路のうち、HTTPS で保護される部分を見分ける方法を学びます。"
meta_keywords: "HTTPS, TLS, Web セキュリティ, サイバーセキュリティ, Linux Journey"
---

HTTP は、ブラウザーとサーバーがやり取りするメッセージを定めます。HTTPS は、その同じメッセージを **TLS** で保護して送ります。TLS は接続を保護し、ブラウザーがサーバーの識別情報を確認できるようにするプロトコルです。

## 保護された接続を見分ける

ブラウザーが `https://site.example` に接続するとします。TLS の接続が確立されると、ブラウザーとサーバーは暗号化された HTTP メッセージをやり取りできます。その通信経路を観測する第三者は、HTTP の本文をそのまま読んだり、気付かれずに書き換えたりすることができません。

```text
Browser  ===== HTTPS connection =====  Website server
```

ブラウザーは、サーバーが提示した識別情報も検証する必要があります。

:::single-choice{#web-https-protected-hop} この単純な構成で HTTPS が保護するのは何ですか？

::option[ブラウザーが表示した後のページです。]{#web-https-protected-hop-b explanation="ブラウザーはレスポンスを復号してからページを読みます。"}
::option[Web サイトが保管しているすべてのバックアップです。]{#web-https-protected-hop-c explanation="バックアップには別の保護が必要です。"}
::option[保護された接続を通る HTTP メッセージです。]{#web-https-protected-hop-a .correct explanation="TLS は、接続の両端の間で転送中のメッセージを保護します。"}
:::

## 複数の接続からなる経路を読む

プロキシは、ブラウザーからリクエストを受けて別のサーバーに転送できます。プロキシが TLS の終端なら、転送する前にリクエストを読めます。その先の接続にも別途保護が必要です。経路上の接続を一つずつ確認します。

```text
Browser  === HTTPS ===  Proxy  --- HTTP ---  Internal server
```

この図では、外側の接続に TLS を使い、内側の接続には暗号化されていない HTTP を使っています。

:::single-choice{#web-https-inner-hop} TLS で保護するために別途変更が必要なのは、どの区間ですか？

::option[ブラウザーからプロキシまでです。]{#web-https-inner-hop-a explanation="その区間はすでに HTTPS で通信しています。"}
::option[プロキシから内部サーバーまでです。]{#web-https-inner-hop-b .correct explanation="図の内側の区間は、暗号化されていない HTTP です。"}
::option[そのサイトにリクエストを送らないブラウザーのタブです。]{#web-https-inner-hop-c explanation="図には、そのタブからの接続がありません。"}
:::

## アプリケーションのアクセス権を確認する

正しく確立された安全な接続は、サーバーの識別情報を信頼するための根拠となり、転送中のメッセージを保護します。どのアカウントがページを読んだり設定を変えたりできるかは、アプリケーションが判断します。非公開ページには、強固な TLS を使っていてもアプリケーションのアクセスポリシーが必要です。

:::single-choice{#web-https-access-vs-transport} 非公開のアカウントページを返す前に、サービスは何を確認しますか？

::option[認証済みのアカウントに、そのページの閲覧権限があるかどうかです。]{#web-https-access-vs-transport-c .correct explanation="アカウントがアクセスできる範囲は、アプリケーションの認可で決まります。"}
::option[TLS を使っているかどうかだけです。]{#web-https-access-vs-transport-a explanation="HTTPS はやり取りを保護しますが、サービスではアクセスの可否も判断する必要があります。"}
::option[証明書がリクエスト先のホスト名を対象にしているかどうかだけです。]{#web-https-access-vs-transport-b explanation="証明書はサーバーの識別に役立ちます。非公開ページへのアクセスはアプリケーションが制御します。"}
:::

## まとめ

Web リクエストの経路に沿って、HTTPS がどこを保護するかを説明できるようになりました。

1. TLS が始まる場所と終わる場所を特定します。
2. プロキシがリクエストを転送する場合は、区間ごとに確認します。
3. アプリケーションでアクセス制御が必要な理由を理解します。
