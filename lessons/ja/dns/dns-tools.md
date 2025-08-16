---
title: "DNS ツール"
description: "Linux での DNS クエリとトラブルシューティングのために、nslookup と dig コマンドを学びましょう。これらの必須 DNS ツールの使い方を、初心者向けのガイドで理解してください。"
keywords: "nslookup, dig command, DNS tools, Linux DNS, DNS troubleshooting, Linux tutorial, beginner Linux"
---

## Lesson Content

### nslookup

「name server lookup」ツールは、ネームサーバーにクエリを実行してリソースレコードに関する情報を見つけるために使用されます。google.com のネームサーバーがどこにあるかを見てみましょう。

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) は、DNS ネームサーバーに関する情報を取得するための強力なツールです。nslookup よりも柔軟で、DNS の問題をトラブルシューティングするのに優れています。

```bash
pete@icebox:~$ dig www.google.com

; <<>> DiG 9.9.5-3-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 42376
;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; MBZ: 0005 , udp: 512
;; QUESTION SECTION:
;www.google.com.                        IN      A

;; ANSWER SECTION:
www.google.com.         5       IN      A       74.125.239.147
www.google.com.         5       IN      A       74.125.239.144
www.google.com.         5       IN      A       74.125.239.146
www.google.com.         5       IN      A       74.125.239.145
www.google.com.         5       IN      A       74.125.239.148

;; Query time: 27 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Feb 07 10:14:00 PST 2016
;; MSG SIZE  rcvd: 123
```

## Exercise

dig の manpage を読んでください。

## Quiz Question

DNS ネームサーバーに関する詳細情報を取得するために使用されるツールは何ですか？

## Quiz Answer

dig
