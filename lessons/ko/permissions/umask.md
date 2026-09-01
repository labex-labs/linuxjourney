---
lesson_id: "umask"
course_id: "permissions"
lang: "ko"
order_index: 4
title: "Umask"
description: "프로세스 umask가 새 파일과 디렉터리에 요청되는 권한 비트를 제한하는 방법을 배웁니다."
meta_title: "Umask - Permissions"
meta_description: "umask 명령으로 Linux 기본 파일 권한을 제어하는 방법을 배웁니다. 숫자 권한을 이해하고 새 파일 접근을 관리하세요."
meta_keywords: "umask, linux 권한, 파일 권한, linux 명령어, 초보자 linux, linux 튜토리얼, 기본 권한"
---

프로세스의 파일 생성 마스크인 umask는 해당 프로세스가 파일 시스템 객체를 만들 때 선택한 권한 비트가 설정되지 않게 합니다. 완전한 기본 모드가 아니라 마스크입니다. 애플리케이션이 먼저 모드를 요청하고 커널이 umask가 금지한 비트를 제거합니다.

개념적으로 다음과 같습니다.

```text
resulting mode = requested mode AND NOT umask
```

접근 제어 목록과 애플리케이션 동작이 세부 사항을 추가할 수 있으므로 정확한 권한이 중요할 때 결과를 확인하세요.

## Umask 확인하고 설정하기

피연산자 없이 `umask`를 실행하면 현재 쉘의 마스크를 표시하며 흔히 8진수 형식입니다.

```bash
$ umask
0022
```

현재 쉘과 이후 그 쉘에서 시작하는 프로세스에 설정합니다.

```bash
$ umask 027
```

각 8진수 위치는 소유자, 그룹, 기타 사용자에 대응합니다. 마스크 비트는 대응하는 요청 권한을 제거합니다. `2`는 쓰기, `4`는 읽기, `1`은 실행을 가립니다.

:::single-choice{#umask-command-purpose} `umask 027`은 현재 쉘에서 무엇을 변경하나요?

::option[이미 존재하는 모든 파일의 권한]{#umask-existing-files explanation="umask는 생성 요청에 영향을 주며 기존 객체에 소급해 `chmod`를 실행하지 않습니다."}
::option[이후 해당 쉘에서 시작한 명령이 상속하는 마스크]{#umask-current-shell-mask .correct explanation="쉘이 프로세스 umask를 설정하고 자식 프로세스는 일반적으로 그 값을 상속합니다."}
::option[새 파일에 저장되는 소유자 및 그룹 이름]{#umask-owner-group explanation="마스크는 권한 비트를 걸러내며 소유권 신원을 선택하지 않습니다."}
:::

## 새 파일과 디렉터리 모드 계산하기

실행 가능한 파일을 기본으로 만드는 것은 안전하지 않으므로 많은 일반 프로그램은 새 일반 파일에 `0666`을 요청합니다. 탐색에 실행 권한이 필요한 새 디렉터리에는 흔히 `0777`을 요청합니다.

umask `0022`에서는 다음과 같습니다.

```text
regular file: 0666 masked by 0022 -> 0644 (rw-r--r--)
directory:    0777 masked by 0022 -> 0755 (rwxr-xr-x)
```

umask는 요청된 비트만 제거합니다. 애플리케이션이 실행 권한을 요청하지 않았다면 추가할 수 없습니다. 애플리케이션이 더 제한적인 시작 모드를 요청하면 결과도 더 제한적일 수 있습니다.

:::single-choice{#umask-file-mode-022} 프로그램이 일반 파일에 모드 `0666`을 요청하고 umask가 `0022`이면 어떤 모드가 되나요?

::option[`0666`]{#umask-file-0666 explanation="`0666`이 요청한 그룹과 기타 사용자 쓰기 비트는 마스크 `0022`로 제거됩니다."}
::option[`0755`]{#umask-file-0755 explanation="일반 파일에 실행 비트를 요청하지 않았으므로 umask가 이를 추가할 수 없습니다."}
::option[`0644`]{#umask-file-0644 .correct explanation="`0666`에서 그룹과 기타 사용자 쓰기를 제거하면 소유자 읽기/쓰기와 그룹 및 기타 사용자 읽기만 남습니다."}
:::

:::single-choice{#umask-directory-mode-027} 프로그램이 디렉터리에 `0777`을 요청하고 umask가 `0027`이면 어떤 모드가 되나요?

::option[`0777`]{#umask-directory-0777 explanation="요청된 그룹 쓰기와 기타 사용자 권한은 0이 아닌 마스크로 걸러집니다."}
::option[`0640`]{#umask-directory-0640 explanation="이 결과는 마스크 `0027`이 소유자나 그룹에서 제거하지 않는 실행 비트도 제거합니다."}
::option[`0750`]{#umask-directory-0750 .correct explanation="마스크가 그룹 쓰기와 기타 사용자의 모든 권한을 제거하여 `rwxr-x---`를 남깁니다."}
:::

## 범위와 지속성

한 쉘에서 umask를 바꿔도 부모 프로세스나 관련 없는 세션은 바뀌지 않습니다. 값은 해당 쉘과 자식 프로세스가 이후에 만드는 객체에 적용되며 기존 파일은 모드를 유지합니다.

선호 값을 지속하려면 환경에 맞는 로그인, 쉘, PAM, 서비스 관리자 또는 애플리케이션 구성에 설정합니다. 올바른 위치는 다양하고 서비스가 자체 umask를 설정할 수 있습니다. 대화형 쉘 파일 하나를 편집하면 시스템의 모든 프로세스를 제어한다고 가정하지 마세요.

:::single-choice{#umask-existing-file-effect} 새 umask를 설정하면 기존 파일에 어떤 일이 생기나요?

::option[현재 모드가 바뀌지 않습니다.]{#umask-existing-unchanged .correct explanation="새 umask는 이후 생성 요청을 걸러내며 파일 시스템 객체에 이미 저장된 모드를 수정하지 않습니다."}
::option[모드가 `0666`을 기준으로 다시 계산됩니다.]{#umask-existing-recalculated explanation="기존 객체는 다시 생성되거나 새 마스크를 자동으로 통과하지 않습니다."}
::option[소유자가 가려진 권한을 즉시 잃습니다.]{#umask-existing-owner-loss explanation="프로세스 umask 변경은 기존 파일 메타데이터에 대한 작업이 아닙니다."}
:::

실습에서는 격리된 환경에서 서로 다른 마스크로 파일과 디렉터리를 만든 뒤 `ls -ld`로 모드를 비교해 보세요. [Linux 사용자 그룹과 파일 권한](https://labex.io/ko/labs/linux-linux-user-group-and-file-permissions-18002) 실습이 적절한 권한 작업 공간을 제공합니다.

## 요약

이제 umask가 새로 요청된 권한을 제한하는 방식을 예측할 수 있습니다.

1. `umask`로 현재 쉘의 마스크를 확인하거나 설정할 수 있습니다.
2. 애플리케이션이 요청한 모드에서 마스크된 비트를 제거할 수 있습니다.
3. 일반 파일의 흔한 `0666` 요청과 디렉터리의 `0777` 요청을 구분할 수 있습니다.
4. umask 범위와 지속성을 프로세스 및 환경별로 다룰 수 있습니다.
