---
lesson_id: "web-http-requests-responses"
course_id: "web-security"
lang: "ja"
order_index: 1
title: "HTTP リクエストとレスポンス"
description: "HTTP のやり取りから、メソッド、パス、ステータス、コンテンツの種類を読み取る方法を学びます。"
meta_title: "HTTP リクエストとレスポンス - Web セキュリティ"
meta_description: "HTTP のやり取りから、メソッド、パス、ステータス、コンテンツの種類を読み取る方法を学びます。"
meta_keywords: "HTTP リクエスト, HTTP レスポンス, Web セキュリティ, サイバーセキュリティ, Linux Journey"
---

ブラウザーなどのクライアントは、Web サーバーに**HTTP リクエスト**を送って処理を求めます。サーバーは**HTTP レスポンス**を返します。二つのメッセージを読むと、何を要求し、サーバーが何を返したかが分かります。

## リクエストを読む

次は短い HTTP/1.1 リクエストです。`GET` はメソッドで、クライアントが求める操作を表します。`/health` はパスです。`Host` ヘッダーは、クライアントがどの Web サイトに要求しているかを示します。

```http
GET /health HTTP/1.1
Host: site.example
```

**ヘッダー**とは、メッセージに関する情報を伝える、名前付きの値です。メソッドとパスはリクエストの最初の行にあります。

:::single-choice{#web-http-requests-responses-request-path} このクライアントは、サーバーに何の取得を求めていますか？

::option[HTTP/1.1 というファイルです。]{#web-http-requests-responses-request-path-b explanation="その項目はプロトコルのバージョンを示します。"}
::option[/health にあるリソースです。]{#web-http-requests-responses-request-path-a .correct explanation="パスは最初の行で GET の後にあります。"}
::option[/site.example にあるリソースです。]{#web-http-requests-responses-request-path-c explanation="Host ヘッダーが示すのは Web サイトで、パスは別の場所に記載されます。"}
:::

## レスポンスを読む

空の練習用ディレクトリでページを作成し、ループバックで待ち受ける Python の HTTP サーバーを起動します。リダイレクトでページを書き出します。リクエストが完了するまではこの端末でサーバーを動かし続け、終わったら Ctrl+C で停止します。

```bash
$ mkdir web-demo
$ printf '%s\n' ready > web-demo/health.txt
$ python3 -m http.server 8094 --bind 127.0.0.1 --directory web-demo
```

同じマシンで二つ目の端末を開き、`curl -i` を実行します。このオプションを付けると、レスポンスの本文より先にヘッダーが表示されます。

```bash
$ curl -i http://127.0.0.1:8094/health.txt
```

レスポンスの先頭行には**ステータスコード**があります。`200` は、このリクエストが成功したことを示します。ヘッダーと本文は空行で区切られます。`Content-Type` は、プレーンテキストなど、本文をどう解釈するかをクライアントに伝えます。

:::single-choice{#web-http-requests-responses-response-parts} コンテンツをどう表示するかをクライアントが判断するとき、どの項目が役立ちますか？

::option[レスポンスの Content-Type ヘッダーです。]{#web-http-requests-responses-response-parts-b .correct explanation="レスポンス本文の種類を示します。"}
::option[元のリクエストのホスト名です。]{#web-http-requests-responses-response-parts-a explanation="クライアントがアクセスしたサイトの名前です。"}
::option[パスだけです。]{#web-http-requests-responses-response-parts-c explanation="パスはリソースを特定しますが、返されたデータの形式は示しません。"}
:::

![ステータス 200、テキストのコンテンツタイプ、ready という本文を含む LabEx の HTTP レスポンス](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-http-requests-responses/http-response.png)

## 二つの結果を比べる

`404` のレスポンスは、要求されたリソースがサーバーで見つからなかったか、サーバーがその存在を明らかにしなかったことを示します。あるパスでは 200 が返り、別のパスでは 404 が返ることがあります。結果を比較する際は、正確なメソッドとパスを使います。

:::single-choice{#web-http-requests-responses-health-scope} /health へのリクエストが 200 を返しました。/welcome について何が分かりますか？

::option[/welcome も 200 を返しました。]{#web-http-requests-responses-health-scope-a explanation="この例で確認したのは別のパスです。"}
::option[ホストに接続できませんでした。]{#web-http-requests-responses-health-scope-b explanation="ヘルスチェックにはレスポンスが返りました。"}
::option[/welcome の結果は、そのパスにリクエストを送って確かめる必要があります。]{#web-http-requests-responses-health-scope-c .correct explanation="二つのパスで動作が異なる場合があります。"}
:::

レスポンスヘッダーと接続を確認する練習には、[Linux で curl を使ってサーバーへの接続を確認する方法](https://labex.io/tutorials/linux-how-to-test-server-connectivity-with-curl-in-linux-415082)を試してください。

## まとめ

簡単な HTTP のやり取りの主な項目を読めるようになりました。

1. リクエストのメソッド、パス、ホストを確認します。
2. レスポンスのステータスとコンテンツの種類を読みます。
3. 実際に送ったリクエストを特定して、その結果を説明します。
