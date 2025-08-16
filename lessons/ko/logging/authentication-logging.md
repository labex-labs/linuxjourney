---
title: "인증 로깅"
description: "/var/log/auth.log를 사용하여 Linux 인증 로깅에 대해 알아보세요. 이 필수 가이드를 통해 사용자 로그인을 이해하고 액세스 문제를 해결하세요."
keywords: "Linux 인증, auth.log, Linux 로깅, 사용자 로그인, Linux 보안, 초급, 튜토리얼, 가이드"
---

## Lesson Content

로그인에 문제가 있는 경우 인증 로깅을 살펴보는 것이 매우 유용할 수 있습니다.

### /var/log/auth.log

이 파일에는 사용자 로그인 및 사용된 인증 방법과 같은 시스템 권한 부여 로그가 포함되어 있습니다.

샘플 스니펫:

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

## Exercise

몇 번의 로그인 시도 실패 후 성공적인 로그인을 수행하십시오. 그런 다음 `/var/log/auth.log` 파일을 검토하여 어떤 일이 발생했는지 확인하십시오.

## Quiz Question

사용자 인증에 사용되는 로그 파일은 무엇입니까?

## Quiz Answer

auth.log
