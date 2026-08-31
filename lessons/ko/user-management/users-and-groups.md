---
lesson_id: "users-and-groups"
course_id: "user-management"
lang: "ko"
order_index: 1
title: "사용자와 그룹"
description: "Linux가 사용자와 그룹을 식별하고 프로세스 자격 증명이 접근 결정에 영향을 주는 방식을 배웁니다."
meta_title: "사용자와 그룹 - User Management"
meta_description: "Linux 기초의 핵심인 사용자 및 그룹 관리를 배웁니다. Linux 사용자와 그룹, root 슈퍼사용자, sudo 명령을 사용한 권한 상승을 다룹니다."
meta_keywords: "linux 사용자와 그룹, linux 기초, sudo, root 사용자, UID, GID, 사용자 관리, linux 튜토리얼, linux 고급 학습"
---

Linux는 사용자와 그룹 신원을 사용하여 프로세스에 레이블을 붙이고 파일 시스템 객체의 소유권을 정하며 접근 제어 결정을 내립니다. 사람이 읽을 수 있는 이름은 관리자를 돕고 커널은 주로 숫자 식별자와 프로세스 자격 증명을 사용합니다.

## UID로 사용자 식별하기

각 계정에는 **UID**라는 숫자 사용자 ID가 있습니다. 사용자 이름은 시스템 계정 데이터베이스를 통해 UID에 매핑됩니다. 파일은 숫자 소유권을 저장하고 도구는 일반적으로 대응하는 이름으로 표시합니다.

`id`를 실행하여 현재 프로세스 신원 정보를 확인합니다.

```bash
$ id
uid=1000(alice) gid=1000(alice) groups=1000(alice),27(sudo)
```

값은 시스템마다 다릅니다. 사람의 로그인 계정은 흔히 `/home/alice` 같은 홈 디렉터리를 갖지만 다른 경로나 일반적인 홈이 전혀 없는 계정도 있습니다. 서비스 계정은 대화형 로그인을 제공하기보다 제한된 신원으로 소프트웨어를 실행하기 위해 존재하는 경우가 많습니다.

:::single-choice{#users-uid-purpose}
커널이 사용자 신원을 나타내는 데 주로 사용하는 식별자는 무엇인가요?

::option[홈 디렉터리 경로]{#users-home-path explanation="홈 경로는 계정 구성으로 달라지거나 없을 수 있으며 커널의 사용자 식별자가 아닙니다."}
::option[숫자 UID]{#users-numeric-uid .correct explanation="계정 데이터베이스는 이름을 프로세스 자격 증명과 소유권 레코드에 쓰이는 숫자 UID에 매핑합니다."}
::option[터미널 창 번호]{#users-terminal-number explanation="터미널 장치와 세션은 숫자 사용자 신원과 별개입니다."}
:::

## 그룹으로 접근 구성하기

그룹에는 **GID**라는 숫자 그룹 ID가 있습니다. 계정은 일반적으로 기본 그룹 하나를 가지며 보조 그룹에도 속할 수 있습니다. 그룹 멤버십을 사용하면 계정마다 권한을 하나씩 부여하지 않고 사용자 집합에 접근 권한을 줄 수 있습니다.

다음 명령으로 멤버십을 확인합니다.

```bash
$ id alice
$ groups alice
```

이 명령들은 구성되거나 해석된 신원 정보를 보고합니다. 디렉터리 서비스와 캐시도 관여할 수 있으므로 `/etc/group`을 직접 읽는 것만으로는 완전한 유효 멤버십을 항상 확인할 수 없습니다.

:::single-choice{#users-primary-supplementary-groups}
한 Linux 계정은 일반적으로 그룹에 어떻게 참여하나요?

::option[전체 수명 동안 정확히 한 그룹에만 속할 수 있습니다.]{#users-single-group explanation="Linux 프로세스는 기본 그룹과 보조 그룹 목록을 함께 가질 수 있습니다."}
::option[읽을 수 있는 파일이 속한 모든 그룹의 구성원이 됩니다.]{#users-readable-groups explanation="파일 가독성은 권한과 자격 증명을 따르며 자동으로 그룹 멤버십을 만들지 않습니다."}
::option[기본 그룹 하나를 가지며 보조 그룹에도 속할 수 있습니다.]{#users-group-memberships .correct explanation="기본 GID는 계정 레코드의 일부이고 보조 멤버십은 추가 그룹 신원을 제공합니다."}
:::

## 프로세스 자격 증명 이해하기

프로세스에는 실제 및 유효 UID와 GID, 보조 그룹 같은 자격 증명이 있습니다. 유효 자격 증명은 여러 권한 검사의 중심입니다. 사용자가 시작한 프로세스는 보통 부모의 자격 증명을 상속하지만 통제된 메커니즘으로 이를 바꿀 수 있습니다.

이는 프로세스가 항상 “시작한 사용자로만” 실행된다는 설명보다 정확합니다. set-user-ID 실행 파일, 서비스 관리자, 컨테이너, 네임스페이스, 권한 변경 시스템 호출은 특정 문맥에서 보이거나 유효한 신원에 영향을 줄 수 있습니다.

:::single-choice{#users-process-access-identity}
커널이 프로세스를 파일 권한과 비교할 때 일반적으로 고려하는 정보는 무엇인가요?

::option[프로세스의 유효 UID, 유효 GID, 보조 그룹]{#users-effective-credentials .correct explanation="일반적인 임의 접근 검사에서 이 자격 증명을 소유권 및 권한 데이터와 비교합니다."}
::option[프로세스를 시작한 터미널의 색상 테마]{#users-terminal-theme explanation="표시 환경 설정은 파일 시스템 권한 검사와 관련이 없습니다."}
::option[계정 사용자 이름의 글자 수]{#users-username-length explanation="커널은 숫자 자격 증명을 사용하며 사용자 이름 길이는 접근 권한을 부여하지 않습니다."}
:::

## Root 신원 이해하기

전통적으로 `root`라는 이름의 계정은 UID 0을 갖습니다. UID 0은 여러 Linux 권한 메커니즘에서 특별하게 취급되며 광범위한 관리 권한을 가집니다. 현대 Linux는 기능, 네임스페이스, 강제 접근 제어, 서비스 격리로 권한을 나눌 수도 있으므로 “모든 문맥에서 무제한 권한”이라는 설명은 지나치게 단순합니다.

일상적인 작업에는 권한이 없는 계정을 사용하세요. 관리 권한은 경로 실수, 신뢰할 수 없는 명령, 침해된 소프트웨어의 영향을 키웁니다.

:::single-choice{#users-root-uid}
전통적으로 root 계정을 식별하는 숫자 UID는 무엇인가요?

::option[`0`]{#users-uid-zero .correct explanation="Linux와 Unix 계열 시스템은 전통적으로 UID 0을 슈퍼사용자 신원에 예약합니다."}
::option[`1000`]{#users-uid-thousand explanation="많은 배포판이 첫 번째 일반 사용자 계정에 1000 근처 값을 할당하지만 root UID는 아닙니다."}
::option[`1`]{#users-uid-one explanation="UID 1은 시스템 계정에 속할 수 있으며 전통적인 슈퍼사용자 신원이 아닙니다."}
:::

## 정책에 따라 sudo 사용하기

`sudo`는 구성된 정책에 호출 사용자가 대상 사용자로 명령을 실행할 수 있는지 묻습니다. 기본 대상은 흔히 root이지만 정책이나 `-u USER`로 다른 계정을 선택할 수 있습니다. 인증 요청과 로깅도 구성에 따라 달라집니다.

현재 계정이 실행할 수 있는 명령을 나열합니다.

```bash
$ sudo -l
```

작업에 필요하고 효과를 이해할 때만 허용된 관리 명령을 사용하세요. 권한 오류를 숨기기 위해 `sudo`를 사용하지 말고 `/etc/shadow` 같은 비밀번호 해시 데이터베이스를 가벼운 연습으로 표시하지 마세요.

:::single-choice{#users-sudo-policy}
`sudo`는 요청한 명령을 실행하기 전에 무엇을 하나요?

::option[요청한 대상 신원을 사용할 권한이 있는지 구성된 정책을 확인합니다.]{#users-sudo-policy-check .correct explanation="`sudo`는 정책에 따라 권한을 부여하고 허용되면 구성된 대상 자격 증명을 설정합니다."}
::option[모든 로컬 사용자에게 항상 제한 없는 root 접근을 부여합니다.]{#users-sudo-always-root explanation="권한 부여는 정책으로 제어되며 거부된 사용자나 명령은 포괄적인 root 접근을 받지 않습니다."}
::option[호출 계정의 영구 UID를 0으로 바꿉니다.]{#users-sudo-permanent-uid explanation="`sudo`는 대상 자격 증명으로 명령을 실행하며 호출자의 계정 신원을 영구적으로 다시 쓰지 않습니다."}
:::

통제된 환경에서 계정과 그룹 관리를 연습하려면 다음 실습을 진행해 보세요.

1. **[useradd, usermod, userdel로 Linux 사용자 계정 관리하기](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성과 보안 설정부터 수정 및 삭제까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod, groupdel로 Linux 그룹 관리하기](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 새 그룹 생성, 사용자 멤버십 수정, 그룹 제거에 필요한 핵심 명령줄 도구를 연습합니다.
3. **[Linux 사용자 계정과 Sudo 권한 구성하기](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 관리 권한 부여를 포함해 Linux 보안을 높이는 사용자 계정 및 `sudo` 권한 관리 기법을 배웁니다.

## 요약

이제 Linux가 신원을 나타내고 관리 명령을 위임하는 방식을 설명할 수 있습니다.

1. 계정은 UID로, 그룹은 GID로 식별할 수 있습니다.
2. 기본 그룹과 보조 그룹 멤버십을 구분할 수 있습니다.
3. 프로세스 자격 증명을 접근 검사와 연결할 수 있습니다.
4. UID 0을 전통적인 root 신원으로 이해할 수 있습니다.
5. `sudo`를 정책으로 제어되는 위임 도구로 다룰 수 있습니다.
