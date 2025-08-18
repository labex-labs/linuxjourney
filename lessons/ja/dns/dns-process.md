---
index: 3
lang: "ja"
title: "DNS プロセス"
meta_title: "DNS プロセス - DNS"
meta_description: "ルートサーバーから権威 DNS まで、DNS がどのように機能するかを段階的に学びます。初心者および中級者向けの DNS ルックアッププロセスを理解します。"
meta_keywords: "DNS プロセス，DNS ルックアップ，DNS の仕組み，DNS チュートリアル，初心者向け DNS, Linux DNS, TLD, ルートサーバー"
---

## Lesson Content

ホストが DNS でドメイン (catzontheinterwebz.com) を見つける方法の例を見てみましょう。基本的に、そのドメインを知っている DNS サーバーに到達するまで、情報を絞り込んでいきます。

### Local DNS Server

まず、ホストは「catzontheinterwebz.com はどこですか？」と尋ねます。ローカル DNS サーバーは知らないため、Root Servers に尋ねるために、情報の最上位から開始します。ホストが catzontheinterwebz.com を直接見つけるためにこれらのリクエストを行っているわけではないことに注意してください。ほとんどのユーザーは ISP が提供する再帰的 DNS サーバーと通信し、そのサーバーが catzontheinterwebz.com の場所を見つけるタスクを負っています。

### Root Servers

インターネットには 13 の Root Servers があります。これらはミラーリングされ、インターネットの DNS リクエストを処理するために世界中に分散されているため、実際には何百ものサーバーが稼働しています。これらは異なる組織によって管理されており、Top-Level Domains に関する情報を含んでいます。トップレベルドメインとは、.org、.com、.net などのアドレスとして知られているものです。したがって、Root Server は catzontheinterwebz.com がどこにあるかを知りませんが、提供された IP アドレスにある.com Top-Level Domain DNS Server に尋ねるように指示します。

### Top-Level Domain

次に、「.com」アドレスを知っているネームサーバーに別のリクエストを送信し、catzontheinterwebz.com がどこにあるかを知っているかどうかを尋ねます。TLD はゾーンファイルに catzontheinterwebz.com を持っていませんが、catzontheinterwebz.com のネームサーバーのレコードは認識しています。そのため、そのネームサーバーの IP アドレスを提供し、そこを調べるように指示します。

### Authoritative DNS Server

これで、実際に必要なレコードを持っている DNS サーバーに最後のリクエストを送信します。ネームサーバーは、catzontheinterwebz.com のゾーンファイルを持っており、このホストの「www」のリソースレコードがあることを確認します。そして、このホストの IP アドレスを提供し、ついにインターネット上で猫を見ることができるようになります。

## Exercise

No exercises for this lesson.

## Quiz Question

.com、.net、.org などのアドレスが見つかるネームサーバーの略語は何ですか？

## Quiz Answer

TLD
