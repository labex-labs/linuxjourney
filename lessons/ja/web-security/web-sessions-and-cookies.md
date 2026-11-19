---
lesson_id: "web-sessions-and-cookies"
course_id: "web-security"
lang: "ja"
order_index: 5
title: "セッションと Cookie"
description: "Cookie がブラウザーのリクエストを Web セッションに結び付ける仕組みを学びます。"
meta_title: "セッションと Cookie - Web セキュリティ"
meta_description: "Cookie がブラウザーのリクエストを Web セッションに結び付ける仕組みを学びます。"
meta_keywords: "セッション, Cookie, Web セキュリティ, サイバーセキュリティ, Linux Journey"
---

ログインに成功した後も、ブラウザーは続けてリクエストを送ります。**セッション**を使うと、アプリケーションはそれらのリクエストをログイン済みのアカウントに結び付けられます。よく使われる方法の一つは、短い識別子をブラウザーの Cookie に保存することです。

## Cookie のやり取りを追う

次はやり取りを簡略化した例です。レスポンスは `session` という Cookie を送ります。値には説明用の架空のトークンを使っています。

```http
Set-Cookie: session=sample-token; Secure; HttpOnly; SameSite=Lax
```

その後ブラウザーは、Cookie を送る条件に合うリクエストに、その Cookie を含めることができます。

```http
Cookie: session=sample-token
```

サーバーはそのトークンを使って、以前に作成したセッションを探します。

:::single-choice{#web-sessions-and-cookies-direction} 送信条件に合うリクエストで、Cookie の値をサーバーに送り返すヘッダーはどれですか？

::option[Set-Cookie です。]{#web-sessions-and-cookies-direction-a explanation="サーバーは、Cookie を設定するためにレスポンスでこのヘッダーを送ります。"}
::option[Content-Type です。]{#web-sessions-and-cookies-direction-c explanation="このヘッダーはメッセージ本文の形式を示します。"}
::option[Cookie です。]{#web-sessions-and-cookies-direction-b .correct explanation="条件が合うと、ブラウザーはリクエストにこのヘッダーを含めます。"}
:::

## 属性を読む

`Secure` は、通常の Cookie 送信を HTTPS に制限します。`HttpOnly` があると、ページ内のスクリプトは通常の Cookie API でその値を読めません。`SameSite` は、別のサイトから開始されたリクエストにブラウザーが Cookie を含める条件を制御します。各属性は、ブラウザーの異なる動作に作用します。

:::single-choice{#web-sessions-and-cookies-secure-attribute} この Cookie の送信を HTTPS に制限するようブラウザーに指示する属性はどれですか？

::option[HttpOnly です。]{#web-sessions-and-cookies-secure-attribute-b explanation="これは、ページ内のスクリプトによる Cookie へのアクセスを制限します。"}
::option[Secure です。]{#web-sessions-and-cookies-secure-attribute-a .correct explanation="この属性は、Cookie を送信する際の通信経路の保護に関係します。"}
::option[session という名前です。]{#web-sessions-and-cookies-secure-attribute-c explanation="Cookie の名前は、アプリケーションが付けるラベルです。"}
:::

## セッションを終了する

ユーザーがログアウトすると、サービスはサーバー側でセッションを無効化し、保存済みの Cookie を削除するようブラウザーに指示できます。ブラウザーに以前の値がしばらく残る可能性があるため、サーバー側での無効化が重要です。本物のセッショントークンは認証情報として扱い、スクリーンショットや共有ログに含めないようにします。

:::single-choice{#web-sessions-and-cookies-after-sign-out} 無効化されたセッションのトークンが再びサーバーに届いた場合、どう処理しますか？

::option[サーバーは、認証されていないリクエストとして扱います。]{#web-sessions-and-cookies-after-sign-out-c .correct explanation="その値に対応するサーバー側のセッションは、すでに無効です。"}
::option[サーバーは、以前のセッションを自動で復元します。]{#web-sessions-and-cookies-after-sign-out-a explanation="以前のセッションは終了しています。"}
::option[Cookie にまだ名前があるので、サーバーは受け入れます。]{#web-sessions-and-cookies-after-sign-out-b explanation="Cookie に名前があっても、その値が有効になるわけではありません。"}
:::

## まとめ

ブラウザーとサービスの間で、セッション Cookie のやり取りを追えるようになりました。

1. Cookie を設定するヘッダーと、サーバーに送り返すヘッダーを見分けます。
2. よく使われる Cookie 属性の目的を説明します。
3. サーバー側の無効化でセッションが終了する仕組みを説明します。
