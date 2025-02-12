# ابزار‌های DNS

## محتوای درس

### ‏nslookup

ابزار nslookup (name server lookup)‎ برای جستجوی name server‌ها و پیدا کردن
اطلاعات مربوط به ورودی منابع‌شان استفاده می‌شود. بیایید name server مربوط به
google.com را پیدا کنیم:

```
pete@icebox:~$ nslookup www.google.com
Server:         127.0.1.1
Address:        127.0.1.1#53

Non-authoritative answer:
Name:   www.google.com
Address: 216.58.192.4
```

### ‏dig

ابزار dig (domain information groper)‎ ابزاری قدرمتند برای به دست آوردن اطلاعات
مربوط به DNS name server است. انعطاف بیشتر نسبت به nslookup این ابزار
را به ابزاری قدرتمند در پیدا کردن و رفع مشکلات DNS تبدیل کرده است.

```
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

## تمرینات

صفحه‌ی راهنمای (man page) مربوط به دستور dig را مطالعه کنید.

## سوال آزمون

کدام ابزار برای به دست آوردن اطلاعات جامع مربوط به DNS name server استفاده می‌شود؟

## پاسخ آزمون

dig
