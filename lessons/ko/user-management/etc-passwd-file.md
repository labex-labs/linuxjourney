---
lesson_id: "etc-passwd-file"
course_id: "user-management"
lang: "ko"
order_index: 3
title: "/etc/passwd"
description: "로컬 passwd 레코드를 읽고 완전한 NSS 계정 보기와 구분하는 방법을 배웁니다."
meta_title: "/etc/passwd - User Management"
meta_description: "Linux /etc/passwd 파일 종합 가이드입니다. 사용자 데이터 필드를 해석하고 UID를 이해하며 root:x:0:0:root:/root:/bin/bash 같은 예제를 살펴봅니다."
meta_keywords: "/etc/passwd, linux /etc/passwd, root:x:0:0:root:/root:/bin/bash, 사용자 ID, UID, 사용자 관리, Linux 튜토리얼"
---

`/etc/passwd`는 로컬 계정 레코드를 콜론으로 구분된 텍스트 형식으로 저장합니다. 로그인 이름을 숫자 UID에 매핑하고 기본 GID, 설명 필드, 홈 경로, 로그인 프로그램을 기록합니다.

## 로컬 레코드와 해석된 계정 구분하기

읽기 전용 명령으로 로컬 파일을 표시합니다.

```bash
$ cat /etc/passwd
```

시스템이 아는 모든 계정이 반드시 이 파일에 있는 것은 아닙니다. 이름 서비스 스위치(NSS)는 파일, 디렉터리 서비스, 시스템 데이터베이스 또는 구성된 다른 출처에서 계정을 해석할 수 있습니다. 해석된 passwd 데이터베이스를 질의하려면 `getent`를 사용합니다.

```bash
$ getent passwd
$ getent passwd root
```

첫 번째 명령은 계정 이름과 메타데이터를 노출할 수 있으므로 공개적으로 공유하기 전에 출력을 검토하세요.

:::single-choice{#passwd-query-resolved-database} 로컬 파일만 읽지 않고 NSS로 해석된 passwd 데이터베이스를 질의하는 명령은 무엇인가요?

::option[`cat /etc/passwd`]{#passwd-cat-local explanation="로컬 파일만 표시하며 다른 NSS 출처에서만 제공되는 계정을 포함하지 않습니다."}
::option[`cat /etc/shadow`]{#passwd-cat-shadow explanation="shadow 파일에는 보호된 로컬 비밀번호 만료 데이터가 있으며 이 목적으로 표시해서는 안 됩니다."}
::option[`getent passwd`]{#passwd-getent-all .correct explanation="`getent`는 NSS를 통해 구성된 passwd 데이터베이스 출처를 확인합니다."}
:::

## 일곱 필드 읽기

일반적인 로컬 레코드는 다음과 같습니다.

```text
root:x:0:0:root:/root:/bin/bash
```

콜론으로 구분된 일곱 필드는 다음과 같습니다.

1. **로그인 이름**: `root` 같은 사람이 읽을 수 있는 계정 이름
2. **비밀번호 필드**: shadow 비밀번호 시스템에서는 보통 `x`이며 보호된 비밀번호 데이터가 별도로 저장됨을 나타냄
3. **UID**: 숫자 사용자 신원. UID 0은 전통적으로 슈퍼사용자로 취급됨
4. **기본 GID**: 계정 기본 그룹의 숫자 ID
5. **GECOS/설명**: 설명용 계정 정보로 내부적으로 쉼표로 구분되는 경우가 많음
6. **홈 디렉터리**: 계정의 홈 설정으로 쓰이는 경로. 디스크에 없을 수도 있음
7. **로그인 쉘/프로그램**: `/bin/bash`나 로그인 불가 프로그램처럼 해당 로그인 세션에 요청되는 프로그램

커널은 잘못되었거나 의도적으로 중복된 레코드에서 UID 값이 고유할 것을 강제하지 않지만 같은 UID를 공유하는 계정은 여러 소유권 및 권한 결정에서 구분되지 않습니다. 관리자는 일반적으로 계정 UID를 고유하게 유지해야 합니다.

:::single-choice{#passwd-uid-field} `root:x:0:0:root:/root:/bin/bash`에서 UID가 들어 있는 필드는 무엇인가요?

::option[두 번째 필드 `x`]{#passwd-second-password explanation="두 번째 필드는 숫자 사용자 신원이 아니라 비밀번호 자리 표시자입니다."}
::option[네 번째 필드인 두 번째 `0`]{#passwd-fourth-gid explanation="필드 4는 UID가 아니라 기본 GID입니다."}
::option[세 번째 필드인 첫 번째 `0`]{#passwd-third-uid .correct explanation="필드 3이 UID이므로 첫 번째 0은 이 레코드를 UID 0으로 식별합니다."}
:::

:::single-choice{#passwd-primary-gid-field} passwd 레코드에서 계정의 기본 GID를 저장하는 필드는 무엇인가요?

::option[필드 5]{#passwd-gecos-five explanation="다섯 번째 필드는 GECOS 또는 설명 필드입니다."}
::option[필드 4]{#passwd-gid-four .correct explanation="콜론으로 구분된 네 번째 필드가 기본 그룹을 숫자로 식별합니다."}
::option[필드 7]{#passwd-shell-seven explanation="일곱 번째 필드는 로그인 쉘이나 프로그램을 지정합니다."}
:::

## 비밀번호 자리 표시자 해석하기

일반적인 shadow 비밀번호 시스템에서 필드 2의 `x`는 비밀번호 인식 도구에 보호된 `/etc/shadow` 데이터를 확인하도록 지시합니다. `*`나 `!` 같은 값은 유효한 비밀번호 해시가 아니며 일반적으로 해당 항목을 통한 Unix 비밀번호 인증을 막습니다.

그렇다고 계정이 모든 방식으로 인증할 수 없다는 뜻은 아닙니다. SSH 키, 인증서, 토큰 또는 서비스별 메커니즘은 별개일 수 있습니다. 빈 비밀번호 필드도 인증 스택에 따라 보안에 민감한 동작을 하므로 직접 만들거나 “고치지” 마세요.

:::single-choice{#passwd-x-placeholder} 로컬 `/etc/passwd` 레코드의 필드 2에서 `x`는 일반적으로 무엇을 뜻하나요?

::option[계정에 인증 방법이 전혀 없음을 보장합니다.]{#passwd-no-auth-guarantee explanation="자리 표시자는 가능한 모든 인증 방법을 설명하지 않으며 그 자체로 계정을 사용할 수 없다는 뜻도 아닙니다."}
::option[계정의 홈 디렉터리가 삭제되었습니다.]{#passwd-home-deleted explanation="홈 디렉터리 정보는 필드 6에 저장되며 `x` 자리 표시자와 관련이 없습니다."}
::option[보호된 비밀번호 데이터가 shadow 데이터베이스에 보관됩니다.]{#passwd-shadow-placeholder .correct explanation="공개 passwd 레코드에는 자리 표시자가 있고 비밀번호 해시와 만료 필드는 보호된 shadow 데이터에 있습니다."}
:::

## 서비스 계정 알아보기

많은 레코드는 사람이 아니라 서비스를 나타냅니다. 별도의 서비스 신원은 파일과 프로세스를 한 데몬에 필요한 권한으로 제한하는 데 도움이 됩니다. 홈 경로가 일반적이지 않거나 존재하지 않을 수 있고 로그인 프로그램이 `/usr/sbin/nologin`, `/bin/false` 또는 다른 제한된 프로그램일 수 있습니다.

배포판 정책을 확인하지 않고 UID 범위만으로 계정 목적을 추론하지 마세요. 할당 범위는 다양하며 중앙 관리 계정은 다른 규칙을 따를 수 있습니다.

:::single-choice{#passwd-nologin-shell} 필드 7에서 `/usr/sbin/nologin` 같은 로그인 프로그램의 일반적인 목적은 무엇인가요?

::option[서비스가 멈출 때마다 계정 파일을 삭제합니다.]{#passwd-nologin-delete explanation="로그인 프로그램은 소유 데이터를 자동으로 제거하거나 서비스 종료 파일을 관리하지 않습니다."}
::option[해당 필드를 따르는 로그인 경로를 통한 일반 대화형 쉘을 막습니다.]{#passwd-nologin-purpose .correct explanation="로그인 불가 프로그램은 일반 로그인을 통해 대화형 쉘을 받아서는 안 되는 서비스 계정에 흔히 사용됩니다."}
::option[계정에 UID 0과 같은 권한을 부여합니다.]{#passwd-nologin-root explanation="대화형 로그인을 제한해도 계정 권한이 높아지거나 숫자 UID가 바뀌지 않습니다."}
:::

## 계정 레코드 안전하게 수정하기

`useradd`, `usermod`, `userdel` 같은 계정 관리 도구를 선호하세요. 관련 레코드를 조정하고 시스템 기본값을 적용합니다. 정확한 동작은 배포판 설정에 따라 달라지므로 계정을 바꾸기 전에 옵션을 검토하세요.

로컬 passwd 데이터베이스를 정말 수동으로 복구해야 한다면 일반 편집기 대신 `vipw`를 사용하세요. 동시 편집을 막기 위한 잠금을 적용합니다. `pwck` 같은 도구로 데이터베이스를 검증하고 원격 인증 파일을 바꾸기 전에 복구 세션을 유지하세요.

통제된 환경에서 사용자와 그룹 레코드를 연습하려면 다음 실습을 진행해 보세요.

1. **[useradd, usermod, userdel로 Linux 사용자 계정 관리하기](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성과 보안 설정부터 수정 및 삭제까지 사용자 관리 수명 주기를 연습합니다.
2. **[groupadd, usermod, groupdel로 Linux 그룹 관리하기](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 새 그룹 생성과 사용자 멤버십 수정에 필요한 핵심 명령줄 도구를 연습합니다.

## 요약

이제 로컬 passwd 레코드를 완전한 신원 데이터베이스로 오해하지 않고 해석할 수 있습니다.

1. `getent passwd`로 NSS에서 해석된 계정을 질의할 수 있습니다.
2. 콜론으로 구분된 passwd 필드 일곱 개를 읽을 수 있습니다.
3. UID와 기본 GID 필드를 찾을 수 있습니다.
4. 로그인 상태를 과장하지 않고 비밀번호 자리 표시자를 해석할 수 있습니다.
5. 일반 편집기 대신 계정 도구나 `vipw`를 사용할 수 있습니다.
