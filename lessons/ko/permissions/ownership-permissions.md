---
lesson_id: "ownership-permissions"
course_id: "permissions"
lang: "ko"
order_index: 3
title: "소유권 권한"
description: "Linux 파일 시스템 객체의 사용자 및 그룹 소유권을 확인하고 변경하는 방법을 배웁니다."
meta_title: "소유권 권한 - Permissions"
meta_description: "chown과 chgrp Linux 명령을 사용해 파일의 사용자 및 그룹 소유권을 변경하는 방법을 배우고 Linux 파일 소유권을 익혀 보세요."
meta_keywords: "chown, chgrp, linux 파일 소유권, 파일 소유자 변경, 파일 그룹 변경, linux 권한, linux 명령어, linux 튜토리얼, 사용자 소유권, 그룹 소유권"
---

모든 Linux 파일 시스템 객체는 사용자 소유자와 그룹 소유자를 기록합니다. 이 신원은 어느 소유자 또는 그룹 권한 묶음을 적용할지 결정하지만 그 자체로 특정 권한을 부여하지는 않습니다. `ls -l`로 소유권과 모드를 모두 확인하세요.

## 사용자 소유자 변경하기

change owner의 줄임말인 `chown`으로 다른 사용자 소유자를 지정합니다.

```bash
$ sudo chown patty myfile
```

`myfile`의 사용자 소유자를 `patty`로 바꾸고 그룹은 그대로 둡니다. 현재 파일을 소유하고 있어도 사용자 소유자를 바꾸려면 일반적으로 적절한 권한이 필요합니다. 이 제한은 사용자가 할당량이나 다른 소유권 기반 제어를 피하기 위해 파일을 넘기는 일을 막습니다.

:::single-choice{#ownership-permissions-change-user} 그룹은 바꾸지 않고 `myfile`의 사용자 소유자를 `patty`로 변경하는 명령은 무엇인가요?

::option[`chown patty myfile`]{#ownership-permissions-user-with-chown .correct explanation="`chown` 소유권 피연산자에 사용자 이름만 지정하면 사용자 소유자를 바꾸고 그룹을 보존합니다."}
::option[`chgrp patty myfile`]{#ownership-permissions-user-with-chgrp explanation="`chgrp`는 사용자 소유자가 아니라 그룹 소유자를 바꿉니다."}
::option[`chmod patty myfile`]{#ownership-permissions-user-with-chmod explanation="`chmod`는 모드 비트를 바꾸며 사용자 이름을 새 소유자로 받지 않습니다."}
:::

## 그룹 소유자 변경하기

`chgrp`로 다른 그룹 소유자를 지정합니다.

```bash
$ chgrp whales myfile
```

일반적인 시스템에서 권한이 없는 소유자는 자신이 구성원인 그룹으로만 파일 그룹을 바꿀 수 있습니다. 권한 있는 프로세스는 더 넓은 변경을 할 수 있습니다. 동등한 `chown` 형식은 콜론으로 시작합니다.

```bash
$ chown :whales myfile
```

이후 커널이 그룹 클래스를 선택하면 그룹 모드 비트가 적용됩니다. 그룹을 바꾼다고 읽기, 쓰기, 실행 비트가 자동으로 추가되지는 않습니다.

:::single-choice{#ownership-permissions-change-group} `chgrp whales myfile`은 무엇을 변경하나요?

::option[`myfile`에 기록된 사용자 소유자]{#ownership-permissions-group-not-user explanation="사용자 소유자는 `chgrp`가 아니라 `chown`으로 바꿉니다."}
::option[`whales` 그룹에 나열된 구성원]{#ownership-permissions-group-members explanation="파일 메타데이터를 변경하며 시스템 그룹 멤버십 데이터베이스를 편집하지 않습니다."}
::option[`myfile`에 기록된 그룹 소유자]{#ownership-permissions-group-owner .correct explanation="`chgrp`는 지정한 그룹을 파일 시스템 객체의 그룹 소유자로 할당합니다."}
:::

## 사용자와 그룹 함께 변경하기

`chown`에 `USER:GROUP`을 제공하면 두 필드를 한 작업으로 갱신합니다.

```bash
$ sudo chown patty:whales myfile
```

`patty`를 사용자 소유자, `whales`를 그룹 소유자로 지정합니다. 성공했다고 가정하지 말고 결과를 확인하세요.

```bash
$ ls -l myfile
```

:::single-choice{#ownership-permissions-change-both} `chown` 명령 하나에서 사용자 `patty`와 그룹 `whales`를 지정하는 소유권 표현은 무엇인가요?

::option[`patty:whales`]{#ownership-permissions-both-colon .correct explanation="결합된 소유권 표현에서 콜론이 사용자 이름과 그룹 이름을 구분합니다."}
::option[`patty/whales`]{#ownership-permissions-both-slash explanation="슬래시는 `chown` 사용자와 그룹 피연산자에 여기서 소개한 구분 기호가 아닙니다."}
::option[`patty+whales`]{#ownership-permissions-both-plus explanation="더하기 기호는 `chown`의 두 소유권 필드를 결합하는 데 쓰이지 않습니다."}
:::

## 재귀 변경 신중하게 처리하기

`-R` 옵션은 소유권을 재귀적으로 바꾸지만 넓은 재귀 명령은 예상하지 않은 디렉터리 트리를 지나거나 서비스 데이터에 영향을 줄 수 있습니다. 정확한 대상을 확인하고 구현의 심볼릭 링크 동작을 이해하며 트리를 미리 살펴보고 큰 계층을 바꾸기 전에 작은 표본을 검증하세요. 범위를 검토하지 않고 예제의 권한 소유권 명령을 실제 시스템에 복사하지 마세요.

:::single-choice{#ownership-permissions-mode-separate} 파일의 그룹 소유자를 변경한 뒤 일반 그룹 권한 비트에는 어떤 일이 생기나요?

::option[항상 자동으로 읽기와 쓰기가 됩니다.]{#ownership-permissions-mode-read-write explanation="`chgrp`는 고정된 그룹 모드를 자동으로 선택하지 않습니다."}
::option[소유자의 권한 묶음에서 복사됩니다.]{#ownership-permissions-mode-copied explanation="소유권이 바뀌어도 소유자와 그룹 묶음은 서로 독립적으로 남습니다."}
::option[별도 작업으로 바꾸지 않는 한 설정된 상태로 유지됩니다.]{#ownership-permissions-mode-unchanged .correct explanation="소유권 필드와 모드 비트는 별도 메타데이터이며 그룹을 바꾼다고 새 그룹 비트가 본질적으로 부여되지 않습니다."}
:::

격리된 환경에서 연습하려면 [Linux 사용자 그룹과 파일 권한](https://labex.io/ko/labs/linux-linux-user-group-and-file-permissions-18002) 실습에서 파일 모드와 함께 소유권 확인 및 수정을 진행해 보세요.

## 요약

이제 소유권 메타데이터와 권한 비트를 구분하고 의도적으로 변경할 수 있습니다.

1. `chown USER FILE`로 사용자 소유자를 변경할 수 있습니다.
2. `chgrp GROUP FILE` 또는 `chown :GROUP FILE`로 그룹 소유자를 변경할 수 있습니다.
3. `chown USER:GROUP FILE`로 두 필드를 설정할 수 있습니다.
4. 결과를 검증하고 재귀 변경 범위를 신중하게 다룰 수 있습니다.
