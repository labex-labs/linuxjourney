---
lang: "ko"
title: "/etc/shadow"
description: "Linux 의 /etc/shadow 파일, 해당 필드, 그리고 사용자 암호를 보호하는 방법에 대해 알아보세요. 초보자를 위한 Linux 인증을 이해합니다."
keywords: "/etc/shadow, Linux 보안, 사용자 인증, 암호 관리, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

`/etc/shadow` 파일은 사용자 인증에 대한 정보를 저장하는 데 사용됩니다. 이 파일은 슈퍼유저 읽기 권한이 필요합니다.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

`/etc/passwd` 파일의 내용과 매우 유사하게 보이지만, 암호 필드에는 암호화된 암호가 표시됩니다. 필드는 다음과 같이 콜론으로 구분됩니다:

1. 사용자 이름 (Username)
2. 암호화된 암호 (Encrypted password)
3. 마지막 암호 변경일 - 1970 년 1 월 1 일 이후 경과된 일수로 표시됩니다. 0 이면 사용자가 다음에 로그인할 때 암호를 변경해야 함을 의미합니다.
4. 최소 암호 사용 기간 (Minimum password age) - 사용자가 암호를 다시 변경하기 전에 기다려야 하는 일수입니다.
5. 최대 암호 사용 기간 (Maximum password age) - 사용자가 암호를 변경해야 하는 최대 일수입니다.
6. 암호 경고 기간 (Password warning period) - 암호가 만료되기 전의 일수입니다.
7. 암호 비활성 기간 (Password inactivity period) - 암호가 만료된 후 해당 암호로 로그인을 허용하는 일수입니다.
8. 계정 만료일 (Account expiration date) - 사용자가 로그인할 수 없게 되는 날짜입니다.
9. 향후 사용을 위해 예약된 필드 (Reserved field for future use).

오늘날 대부분의 배포판에서 사용자 인증은 `/etc/shadow` 파일에만 의존하지 않습니다. PAM (Pluggable Authentication Modules) 과 같이 인증을 대체하는 다른 메커니즘이 있습니다.

## Exercise

`/etc/shadow` 파일을 살펴보세요.

## Quiz Question

질문이 없습니다. 다음으로 넘어가세요!

## Quiz Answer
