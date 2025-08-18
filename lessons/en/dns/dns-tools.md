---
index: 6
lang: "en"
title: "DNS Tools"
meta_title: "DNS Tools - DNS"
meta_description: "Learn nslookup and dig commands for DNS queries and troubleshooting on Linux. Understand how to use these essential DNS tools with our beginner-friendly guide."
meta_keywords: "nslookup, dig command, DNS tools, Linux DNS, DNS troubleshooting, Linux tutorial, beginner Linux"
---

## Lesson Content

### nslookup

The "name server lookup" tool is used to query name servers to find information about resource records. Let's find where the name server for google.com is:

```bash
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### dig

Dig (domain information groper) is a powerful tool for getting information about DNS name servers. It is more flexible than nslookup and great for troubleshooting DNS issues.

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

Read up on the manpage for dig.

## Quiz Question

What tool is used to get detailed information about DNS name servers?

## Quiz Answer

dig
