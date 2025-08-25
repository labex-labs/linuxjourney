---
index: 6
lang: "ko"
title: "DNS 도구"
meta_title: "DNS 도구 - DNS"
meta_description: "Linux 에서 DNS 쿼리 및 문제 해결을 위한 nslookup 및 dig 명령을 배웁니다. 이 초보자 친화적인 가이드를 통해 필수 DNS 도구를 사용하는 방법을 이해합니다."
meta_keywords: "nslookup, dig command, DNS tools, Linux DNS, DNS troubleshooting, Linux tutorial, beginner Linux"
---

## Lesson Content

### nslookup

"name server lookup" 도구는 이름 서버에 쿼리하여 리소스 레코드에 대한 정보를 찾는 데 사용됩니다. google.com 의 이름 서버가 어디에 있는지 찾아봅시다:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) 는 DNS 이름 서버에 대한 정보를 얻기 위한 강력한 도구입니다. nslookup 보다 유연하며 DNS 문제 해결에 매우 유용합니다.

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

연습이 완벽을 만듭니다! 다음은 네트워크 인터페이스 설정에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 ethtool 로 네트워크 인터페이스 설정 검사](https://labex.io/ko/labs/linux-examine-network-interface-settings-with-ethtool-in-linux-592759)** - `ethtool` 명령을 사용하여 네트워크 인터페이스 설정을 검사하고 관리하는 방법을 배웁니다. 여기에는 인터페이스 속도 및 이중화 설정 보기 및 설정, 물리 계층 네트워크 문제 해결을 위한 링크 모드 분석이 포함됩니다.

이 실습은 실제 시나리오에 개념을 적용하고 네트워크 인터페이스 관리 능력을 향상시키는 데 도움이 될 것입니다.

## Quiz Question

DNS 이름 서버에 대한 자세한 정보를 얻는 데 사용되는 도구는 무엇입니까?

## Quiz Answer

dig
