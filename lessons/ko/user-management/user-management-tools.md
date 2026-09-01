---
lesson_id: "user-management-tools"
course_id: "user-management"
lang: "ko"
order_index: 6
title: "사용자 관리 도구"
description: "명시적인 옵션으로 로컬 계정을 만들고 수정하고 보호하고 검증하고 제거하는 방법을 배웁니다."
meta_title: "사용자 관리 도구 - User Management"
meta_description: "핵심 명령줄 도구로 Linux 사용자 관리를 익혀 보세요. useradd, userdel, passwd를 사용해 Linux 계정을 관리하는 방법을 다룹니다."
meta_keywords: "linux 사용자 관리, linux 계정 관리 명령줄 도구, useradd, userdel, passwd, linux 계정, linux 사용자 관리"
---

Linux 배포판은 일반적으로 shadow 유틸리티 모음의 계정 도구를 제공하지만 기본값과 상위 수준 래퍼는 다양합니다. 로컬 계정을 바꾸기 전에 중앙에서 관리되지 않는지 확인하고 해당 명령의 로컬 매뉴얼을 검토하며 복구 경로를 유지하세요.

이 레슨의 명령은 인증과 소유권 상태를 바꿉니다. 운영 호스트가 아니라 승인된 일회용 환경에서만 연습하세요.

## 계정 생성 기본값 검토하기

`useradd`는 명령 옵션과 사이트 기본값을 사용하여 로컬 계정을 만듭니다. 컴파일 및 구성된 기본값을 확인합니다.

```bash
$ useradd -D
```

`/etc/default/useradd`, `/etc/login.defs`, 스켈레톤 내용 같은 파일이 동작에 영향을 줄 수 있지만 역할은 배포판마다 다릅니다. 상위 수준 `adduser` 명령이 있을 수 있지만 인터페이스는 모든 Linux 시스템에서 표준화되어 있지 않습니다.

## 로컬 계정 명시적으로 만들기

통제된 환경에서는 알 수 없는 기본값에 의존하지 말고 중요한 속성을 지정합니다.

```bash
$ sudo useradd -m -s /bin/bash -c "Bob Example" bob
```

- `-m`: 홈 디렉터리 생성 요청
- `-s /bin/bash`: 해당 경로가 허용되고 설치되어 있는지 확인한 뒤 로그인 쉘 선택
- `-c`: GECOS/설명 필드 제공

새 계정은 일반적으로 사용 가능한 로컬 비밀번호를 설정하기 전에는 인증할 수 없지만 정확한 초기 비밀번호 및 잠금 상태는 로컬 도구와 정책에 따라 달라집니다. 가정하지 말고 레코드를 확인하세요.

```bash
$ getent passwd bob
$ sudo passwd -S bob
$ id bob
```

:::single-choice{#user-tools-create-home} 새 계정의 홈 디렉터리 생성을 명시적으로 요청하는 `useradd` 옵션은 무엇인가요?

::option[`-M`]{#user-tools-no-home-option explanation="대문자 `-M`은 일반적인 `useradd` 구현에 홈 디렉터리를 만들지 말라고 명시적으로 지시합니다."}
::option[`-s`]{#user-tools-shell-option explanation="`-s` 옵션은 로그인 쉘을 선택하며 그 자체로 홈 디렉터리를 만들지 않습니다."}
::option[`-m`]{#user-tools-home-option .correct explanation="소문자 `-m` 옵션은 로컬 기본값에 따라 홈 디렉터리를 만들고 채우도록 `useradd`에 요청합니다."}
:::

## 비밀번호 설정하거나 변경하기

일반 사용자는 다음 명령의 대화형 요청을 통해 자신의 로컬 비밀번호를 바꿉니다.

```bash
$ passwd
```

승인된 관리자는 다른 로컬 계정의 비밀번호를 설정할 수 있습니다.

```bash
$ sudo passwd bob
```

비밀번호는 명령 인자, 쉘 기록, 레슨 노트, 채팅이 아니라 보호된 요청에만 입력하세요. PAM 정책은 약하거나 재사용된 비밀번호를 거부할 수 있습니다. 디렉터리 관리 계정에는 다른 도구가 필요할 수 있습니다.

:::single-choice{#user-tools-change-own-password} 현재 사용자가 대화형 요청을 통해 자신의 비밀번호를 바꿀 때 일반적으로 사용하는 명령은 무엇인가요?

::option[`useradd`]{#user-tools-add-not-password explanation="`useradd`는 계정 레코드를 만들며 일반적인 대화형 비밀번호 변경 명령이 아닙니다."}
::option[`userdel`]{#user-tools-delete-not-password explanation="`userdel`은 로컬 계정을 제거하며 호출자의 비밀번호 변경과 관련이 없습니다."}
::option[`passwd`]{#user-tools-passwd-self .correct explanation="사용자 이름 피연산자가 없으면 `passwd`는 PAM 정책에 따라 호출 사용자의 로컬 비밀번호에 작동합니다."}
:::

## 계정 속성과 그룹 수정하기

`usermod`는 로컬 계정 필드를 바꿉니다. 예는 다음과 같습니다.

```bash
$ sudo usermod -s /bin/zsh bob
$ sudo usermod -d /srv/home/bob -m bob
$ sudo usermod -aG developers bob
```

홈을 옮기기 전에 대상, 소유권, 사용 가능한 공간, 실행 중인 프로세스, 마운트, 서비스를 확인하세요. 보조 그룹에서 `-aG`는 현재 목록에 추가한다는 뜻입니다. `-a` 없이 `-G`를 사용하면 전체 보조 그룹 목록을 교체하여 예기치 않게 접근을 제거할 수 있습니다.

그룹 변경은 일반적으로 이전 자격 증명 집합으로 이미 실행 중인 프로세스가 아니라 새 로그인 세션에 적용됩니다.

:::single-choice{#user-tools-append-group} `bob`의 다른 보조 멤버십을 교체하지 않고 보조 그룹 `developers`에 추가하는 명령은 무엇인가요?

::option[`usermod -G developers bob`]{#user-tools-replace-groups explanation="`-a`가 없으면 `-G`가 보조 그룹 목록을 교체하여 기존 멤버십을 제거할 수 있습니다."}
::option[`usermod -aG developers bob`]{#user-tools-append-groups .correct explanation="`-a` 옵션은 `-G`가 지정한 그룹을 추가하여 다른 보조 멤버십을 보존합니다."}
::option[`groupdel developers bob`]{#user-tools-delete-group explanation="`groupdel`은 그룹 정의를 제거하며 사용자 멤버십을 추가하지 않습니다."}
:::

## 로컬 비밀번호 잠그기

관리자는 `passwd -l USER`로 로컬 비밀번호 해시를 잠그고 `passwd -S USER`로 상태를 확인할 수 있습니다. 잠금 이유와 유효한 해시가 남아 있는지 검토한 뒤에만 `passwd -u USER`로 잠금을 해제하세요.

비밀번호 잠금이 SSH 키, 토큰, 예약 작업, 이미 실행 중인 프로세스 또는 서비스별 인증을 반드시 막지는 않습니다. 계정을 포괄적으로 비활성화하려면 위협과 접근 경로를 정의한 뒤 계정 만료, 로그인 쉘, 서비스 접근, 키, 세션 종료를 포함할 수 있는 조정된 정책을 적용하세요.

:::single-choice{#user-tools-password-lock-scope} `passwd -l bob`이 주로 잠그는 것은 무엇인가요?

::option[계정의 모든 가능한 인증 및 실행 경로]{#user-tools-lock-everything explanation="키, 토큰, 작업, 서비스, 기존 세션은 별도 제어가 필요할 수 있습니다."}
::option[현재 Bob의 UID가 소유한 모든 파일]{#user-tools-lock-files explanation="비밀번호 상태는 파일 시스템 소유권을 바꾸거나 소유 데이터에 자동으로 접근할 수 없게 만들지 않습니다."}
::option[비밀번호 인증에 쓰이는 로컬 Unix 비밀번호 해시]{#user-tools-lock-local-password .correct explanation="명령은 로컬 비밀번호 해시 앞에 표시를 붙이거나 다른 방식으로 비활성화하여 해당 경로의 정상 검증을 막습니다."}
:::

## 로컬 계정 신중하게 제거하기

일반 `userdel bob`은 로컬 계정 레코드를 제거하지만 보통 홈 디렉터리를 남깁니다. `userdel -r bob`은 홈 디렉터리와 메일 스풀도 제거하려 하므로 파괴적인 작업입니다.

제거하기 전에 다음을 수행합니다.

1. `getent passwd bob`과 `id bob`으로 정확한 계정을 확인합니다.
2. 실행 중인 프로세스, 예약 작업, 서비스, 키, 위임된 접근을 식별합니다.
3. 의도한 파일 시스템 전체에서 해당 UID가 소유한 파일을 조사합니다.
4. 데이터를 이전, 보관, 유지 또는 안전하게 삭제할지 결정합니다.
5. 고아 파일이 남아 있는 동안 UID를 재할당하지 않을지 확인합니다.

`userdel -r`은 구성된 홈 및 메일 위치 밖의 파일 제거를 보장하지 않습니다. 계정 삭제 후에도 파일의 숫자 소유권, 데이터베이스 권한, 애플리케이션 신원, 원격 디렉터리 레코드가 남을 수 있습니다.

:::single-choice{#user-tools-userdel-r-scope} 일반적인 `userdel -r bob`은 `userdel bob`과 비교해 어떤 추가 제거를 요청하나요?

::option[마운트된 모든 파일 시스템에서 Bob의 UID를 가진 모든 파일]{#user-tools-delete-all-owned explanation="도구가 모든 저장소에서 UID 소유 파일을 보편적으로 찾아 지우지는 않습니다."}
::option[사용자 이름이 `bob`인 모든 원격 계정]{#user-tools-delete-remote explanation="`userdel`은 해당 로컬 계정 데이터베이스에 작동하며 관련 없는 디렉터리 서비스 신원을 삭제하지 않습니다."}
::option[계정 레코드와 함께 Bob의 홈 디렉터리와 로컬 메일 스풀]{#user-tools-delete-home-mail .correct explanation="재귀 계정 제거 옵션은 구성된 홈과 메일 스풀을 대상으로 하지만 Bob이 다른 곳에서 소유할 수 있는 모든 객체는 아닙니다."}
:::

격리된 환경에서 계정 수명 주기를 연습하려면 다음 실습을 진행해 보세요.

1. **[useradd, usermod, userdel로 Linux 사용자 계정 관리하기](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성과 보안 설정부터 수정 및 삭제까지 사용자 관리 수명 주기를 연습합니다.
2. **[groupadd, usermod, groupdel로 Linux 그룹 관리하기](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 그룹 추가, 수정, 삭제에 필요한 핵심 명령줄 도구를 연습합니다.
3. **[Linux 사용자 계정과 Sudo 권한 구성하기](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Linux 보안을 높이는 사용자 계정 및 sudo 권한 관리 기법을 배웁니다.

## 요약

이제 명확한 범위와 검증으로 로컬 계정을 관리할 수 있습니다.

1. 생성 전에 `useradd` 기본값을 검토할 수 있습니다.
2. 홈, 쉘, 메타데이터 설정을 명시적으로 요청할 수 있습니다.
3. 보호된 요청을 통해서만 비밀번호를 바꿀 수 있습니다.
4. 기존 목록을 교체하지 않고 보조 그룹을 추가할 수 있습니다.
5. 파괴적인 제거 전에 신원 의존성을 조사할 수 있습니다.
