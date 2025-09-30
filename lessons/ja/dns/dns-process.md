---
index: 3
lang: "ja"
title: "DNS プロセス"
meta_title: "DNS プロセス - DNS"
meta_description: "DNS がどのように機能するかを、ルートサーバーから権威 DNS まで、段階的に学びます。初心者から中級者まで、DNS ルックアッププロセスを理解します。"
meta_keywords: "DNS プロセス，DNS ルックアップ，DNS の仕組み，DNS チュートリアル，初心者向け DNS, Linux DNS, TLD, ルートサーバー"
---

## Lesson Content

DNS を使ってホストがドメイン (catzontheinterwebz.com) を見つける例を見てみましょう。基本的に、そのドメインを知っている DNS サーバーに到達するまで、情報を絞り込んでいきます。

### ローカル DNS サーバー

まず、ホストは「catzontheinterwebz.com はどこですか？」と尋ねます。ローカル DNS サーバーは知らないので、ファネルの最初からルートサーバーに尋ねに行きます。ホストが catzontheinterwebz.com を直接見つけるためにこれらのリクエストを行っているわけではないことに注意してください。ほとんどのユーザーは、ISP が提供する再帰的 DNS サーバーと通信し、そのサーバーが catzontheinterwebz.com の場所を見つけるタスクを負っています。

### ルートサーバー

インターネットには 13 のルートサーバーがあります。これらはミラーリングされ、インターネットの DNS リクエストを処理するために世界中に分散されているため、実際には何百ものサーバーが稼働しています。これらは異なる組織によって管理されており、トップレベルドメインに関する情報を含んでいます。トップレベルドメインとは、.org、.com、.net などのアドレスとして知られているものです。したがって、ルートサーバーは catzontheinterwebz.com がどこにあるかを知りませんが、与えられた IP アドレスにある.com トップレベルドメイン DNS サーバーに尋ねるように指示します。

### トップレベルドメイン

次に、「.com」アドレスを知っているネームサーバーに別のリクエストを送信し、catzontheinterwebz.com がどこにあるかを知っているかどうか尋ねます。TLD はゾーンファイルに catzontheinterwebz.com を持っていませんが、catzontheinterwebz.com のネームサーバーのレコードは認識しています。そこで、そのネームサーバーの IP アドレスを教えてくれ、そこを見るように指示します。

### 権威 DNS サーバー

これで、実際に必要なレコードを持っている DNS サーバーに最終的なリクエストを送信します。ネームサーバーは、catzontheinterwebz.com のゾーンファイルを持っており、このホストの「www」のリソースレコードがあることを確認します。そして、このホストの IP アドレスを教えてくれ、ついにインターネット上で猫を見ることができるようになります。

## Exercise

練習は完璧をもたらします！DNS 解決と管理の理解を深めるための実践的なラボをいくつか紹介します。

1. **[dig と nslookup で Linux の DNS レコードをクエリする](https://labex.io/ja/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - A、PTR、MX などの DNS レコードをクエリし、デフォルトの DNS サーバーを特定する方法を学びます。これはネットワークトラブルシューティングに不可欠です。
2. **[Linux でローカル権威 DNS サーバーをセットアップする](https://labex.io/ja/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - ローカル権威 DNS サーバーをインストールおよび設定し、ゾーンを定義し、DNS 解決をテストすることで、実践的な経験を積みます。
3. **[Linux でローカルホスト名解決を管理する](https://labex.io/ja/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - `/etc/hosts`ファイルを編集してローカルホスト名解決を管理する練習をします。これは Web 開発とネットワークテストの重要なスキルです。

これらのラボは、実際のシナリオで概念を適用し、DNS に対する自信を築くのに役立ちます。

## Quiz Question

.com、.net、.org などのアドレスが見つかるネームサーバーの略語は何ですか？

## Quiz Answer

TLD
