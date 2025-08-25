---
index: 4
lang: "ko"
title: "/etc/shadow"
meta_title: "/etc/shadow - 사용자 관리"
meta_description: "Linux 의 /etc/shadow 파일, 필드 및 사용자 암호 보안 방법에 대해 알아보세요. 초보자를 위한 Linux 인증을 이해합니다."
meta_keywords: "/etc/shadow, Linux 보안, 사용자 인증, 암호 관리, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

`/etc/shadow` 파일은 사용자 인증에 대한 정보를 저장하는 데 사용됩니다. 이 파일은 슈퍼유저 읽기 권한이 필요합니다.

```bash
$ sudo cat /etc/shadow

root:MyEPTEa$6Nonsense:15000:0:99999:7:::
```

`/etc/passwd` 파일의 내용과 매우 유사하게 보이지만, 암호 필드에는 암호화된 암호가 표시됩니다. 필드는 콜론으로 구분되며 다음과 같습니다:

1. 사용자 이름
2. 암호화된 암호
3. 마지막 암호 변경 날짜 - 1970 년 1 월 1 일 이후의 일수로 표시됩니다. 0 이면 사용자가 다음에 로그인할 때 암호를 변경해야 함을 의미합니다.
4. 최소 암호 사용 기간 - 사용자가 암호를 다시 변경하기 전에 기다려야 하는 일수입니다.
5. 최대 암호 사용 기간 - 사용자가 암호를 변경해야 하는 최대 일수입니다.
6. 암호 경고 기간 - 암호가 만료되기 전의 일수입니다.
7. 암호 비활성 기간 - 암호가 만료된 후 해당 암호로 로그인을 허용하는 일수입니다.
8. 계정 만료 날짜 - 사용자가 로그인할 수 없는 날짜입니다.
9. 향후 사용을 위해 예약된 필드입니다.

오늘날 대부분의 배포판에서 사용자 인증은 `/etc/shadow` 파일에만 의존하지 않습니다. PAM(Pluggable Authentication Modules) 과 같이 인증을 대체하는 다른 메커니즘이 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 에서 사용자 인증 및 암호 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[useradd, usermod 및 userdel 을 사용하여 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - `useradd` 및 `passwd`를 사용하여 새 계정을 생성하고 보호하는 것부터 수정하고 삭제하는 것까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 암호 정책을 적용하고 계정을 보호하는 것을 포함하여 사용자 계정 및 sudo 권한을 관리하기 위한 필수 기술을 배웁니다.

이러한 랩은 실제 시나리오에서 사용자 및 암호 관리 개념을 적용하고 Linux 시스템 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

질문이 없습니다. 계속 진행하세요!

## Quiz Answer
