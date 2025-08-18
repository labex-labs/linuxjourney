---
lang: "ko"
title: "DNS 도구"
meta_description: "Linux 에서 DNS 쿼리 및 문제 해결을 위한 nslookup 및 dig 명령을 배웁니다. 이 초보자 친화적인 가이드를 통해 필수 DNS 도구를 사용하는 방법을 이해합니다."
meta_keywords: "nslookup, dig command, DNS tools, Linux DNS, DNS troubleshooting, Linux tutorial, beginner Linux"
---

## Lesson Content

### nslookup

"name server lookup" 도구는 네임 서버에 쿼리하여 리소스 레코드에 대한 정보를 찾는 데 사용됩니다. google.com 의 네임 서버가 어디에 있는지 찾아봅시다:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) 는 DNS 네임 서버에 대한 정보를 얻기 위한 강력한 도구입니다. 이는 nslookup 보다 유연하며 DNS 문제 해결에 매우 유용합니다.

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

dig 의 manpage 를 읽어보세요.

## Quiz Question

DNS 네임 서버에 대한 자세한 정보를 얻는 데 사용되는 도구는 무엇입니까?

## Quiz Answer

dig
