---
lesson_id: "setuid-set-user-id"
course_id: "permissions"
lang: "ko"
order_index: 5
title: "Setuid"
description: "set-user-ID 모드 비트가 실행 프로그램에 영향을 주는 방식과 신중한 보안 검토가 필요한 이유를 배웁니다."
meta_title: "Setuid - Permissions"
meta_description: "Linux Setuid(SUID) 권한의 작동 방식과 변경 방법을 배웁니다. Linux에서 안전한 파일 접근을 위한 SUID를 이해하세요."
meta_keywords: "Linux Setuid, SUID, Linux 권한, chmod, passwd 명령, Linux 보안, 초보자 Linux, Linux 튜토리얼"
---

일부 프로그램은 호출자가 일반적으로 갖지 못하는 접근을 좁은 범위에서 통제하며 사용해야 합니다. 실행 가능한 일반 파일에서 set-user-ID 비트는 새 프로세스가 파일 소유자의 사용자 ID를 유효 사용자 ID로 받게 할 수 있습니다. 그러면 프로그램은 호출자 정보를 유지하면서 해당 신원에 허용된 작업을 수행할 수 있습니다.

Setuid는 “root로 실행”하라는 일반적인 지시가 아닙니다. 효과는 실행 파일의 소유자, 운영체제, 파일 시스템 및 마운트 옵션, 프로그램이 자격 증명을 관리하는 방식에 따라 달라집니다.

## Setuid 알아보기

setuid `passwd` 실행 파일을 사용하는 시스템에서 긴 목록은 다음과 비슷할 수 있습니다.

```bash
$ ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 68248 Jan 10 09:30 /usr/bin/passwd
```

소유자 실행 위치의 소문자 `s`는 setuid와 소유자 실행이 모두 설정되었음을 뜻합니다. setuid는 있지만 소유자 실행이 없으면 `ls -l`은 그 위치에 대문자 `S`를 표시합니다.

모든 배포판이 같은 모드나 인증 설계를 사용한다고 가정하지 마세요. 예제에 의존하지 말고 실제 시스템을 확인합니다.

:::single-choice{#setuid-lowercase-s}
소유자 실행 위치의 소문자 `s`는 무엇을 나타내나요?

::option[Setuid는 설정되었지만 소유자 실행은 없습니다.]{#setuid-s-without-execute explanation="이 조합은 소문자 `s`가 아니라 대문자 `S`로 표시됩니다."}
::option[파일에 sticky 비트와 그룹 실행이 있습니다.]{#setuid-sticky-group explanation="sticky 비트는 기타 사용자 실행 위치에 나타나고 setuid는 소유자 위치에 나타납니다."}
::option[Setuid와 소유자 실행이 모두 설정되어 있습니다.]{#setuid-s-with-execute .correct explanation="소문자 `s`는 setuid 비트와 일반 소유자 실행 비트가 함께 있음을 나타냅니다."}
:::

## 자격 증명 변경 이해하기

커널이 실행 중 setuid를 적용하면 새 프로세스는 일반적으로 실행 파일 소유자를 기준으로 한 유효 사용자 ID를 받습니다. root 소유 프로그램이라면 root에 허용된 접근을 제공할 수 있지만 프로그램이 실행되는 동안 코드가 수행하는 작업에만 해당합니다.

이 메커니즘은 신중하게 작성된 프로그램이 요청을 검증하고 보호된 상태에 제한된 변경을 수행하도록 할 수 있습니다. 예를 들어 로컬 비밀번호 변경 유틸리티는 일반 사용자가 직접 편집할 수 없는 인증 데이터에 통제된 접근이 필요할 수 있습니다. 현대 구현은 PAM, 파일 잠금, 정책 및 다른 보호 장치에도 의존하므로 setuid만으로 전체 작업 흐름을 설명할 수 없습니다.

:::single-choice{#setuid-effective-identity}
Setuid 실행 파일이 적용될 때 파일 소유자에서 주로 가져오는 신원은 무엇인가요?

::option[`/etc/passwd`에 저장된 로그인 이름]{#setuid-login-name explanation="파일 실행은 호출자의 계정 레코드나 로그인 이름을 다시 쓰지 않습니다."}
::option[프로세스의 유효 사용자 ID]{#setuid-effective-user .correct explanation="set-user-ID 실행 메커니즘은 여러 권한 검사에 쓰이는 유효 사용자 신원을 바꿉니다."}
::option[열린 모든 파일의 그룹 소유자]{#setuid-opened-file-group explanation="Setuid는 관련 없는 파일의 소유권 메타데이터가 아니라 프로세스 자격 증명에 영향을 줍니다."}
:::

## 비트 설정하고 제거하기

기호 방식으로 setuid를 설정합니다.

```bash
$ sudo chmod u+s myfile
```

8진수 표기에서 setuid는 선행 특수 비트 숫자에 `4`를 더합니다.

```bash
$ sudo chmod 4755 myfile
```

선행 `4`는 setuid를 설정하고 `755`는 일반 소유자, 그룹, 기타 사용자 비트를 설정합니다. 다른 모드를 바꾸지 않고 setuid를 제거하려면 `chmod u-s myfile`을 사용합니다.

:::single-choice{#setuid-octal-value}
Setuid 특수 비트를 나타내는 선행 8진수 값은 무엇인가요?

::option[`4`]{#setuid-octal-four .correct explanation="Setuid는 선행 특수 비트 숫자에 값 `4`를 더합니다."}
::option[`1`]{#setuid-octal-one explanation="선행 `1`은 sticky 비트를 나타냅니다."}
::option[`2`]{#setuid-octal-two explanation="선행 `2`는 setgid 비트를 나타냅니다."}
:::

## Setuid를 보안에 민감하게 다루기

권한 있는 setuid 프로그램의 결함은 권한 상승 경로가 될 수 있습니다. 이런 프로그램은 입력을 검증하고 신뢰하는 환경과 파일 경로를 통제하며 안전하지 않은 하위 프로세스 동작을 피하고 권한 코드를 최소화하며 가능한 빨리 높은 자격 증명을 내려놓아야 합니다.

Linux는 일반적으로 해석형 스크립트의 setuid를 적용하지 않습니다. 안전하게 처리하기 어려운 경쟁 조건과 인터프리터 관련 문제가 있기 때문입니다. `nosuid`로 마운트한 파일 시스템도 setuid와 setgid 효과를 억제합니다. 요구 사항에 맞으면 서비스 중개 작업, 신중하게 제한된 `sudo` 정책 또는 capabilities 같은 더 좁은 메커니즘을 선호하세요.

공유 시스템에서 임의의 쉘, 인터프리터 또는 복사한 프로그램에 실험으로 setuid를 추가하지 마세요. 기존 setuid 파일을 감사하고 격리된 일회용 환경에서만 연습합니다.

:::single-choice{#setuid-nosuid-mount}
`nosuid`로 파일 시스템을 마운트하는 목적은 무엇인가요?

::option[파일 시스템의 파일에 저장된 모든 실행 비트 제거]{#setuid-nosuid-remove-execute explanation="이 옵션은 파일 메타데이터의 일반 실행 비트를 다시 쓰지 않습니다."}
::option[해당 파일 시스템에서 setuid 및 setgid 실행 효과 억제]{#setuid-nosuid-suppress .correct explanation="`nosuid` 마운트 옵션은 이 특수 모드 비트가 일반적인 자격 증명 변경 실행 동작을 부여하지 못하게 합니다."}
::option[파일 시스템의 모든 파일 소유자를 root로 변경]{#setuid-nosuid-root-owner explanation="`nosuid` 마운트는 사용자나 그룹 소유권 필드를 바꾸지 않습니다."}
:::

## 요약

이제 setuid를 알아보고 자격 증명 및 보안에 미치는 영향을 설명할 수 있습니다.

1. 소유자 실행 위치에서 `s` 또는 `S`를 찾을 수 있습니다.
2. Setuid 실행을 실행 파일 소유자의 유효 사용자 신원과 연결할 수 있습니다.
3. 기호 또는 8진수 `chmod` 모드로 비트를 설정하거나 제거할 수 있습니다.
4. 모든 권한 실행 파일을 보안에 민감한 코드로 다룰 수 있습니다.
