---
lesson_id: "setgid-set-group-id"
course_id: "permissions"
lang: "ko"
order_index: 6
title: "Setgid"
description: "set-group-ID가 실행 파일 자격 증명과 공유 디렉터리의 그룹 상속에 영향을 주는 방식을 배웁니다."
meta_title: "Setgid - Permissions"
meta_description: "Linux SGID(Set Group ID) 권한의 작동 방식과 변경 방법을 배웁니다. 중요한 Linux 보안 개념을 이해하세요."
meta_keywords: "Linux SGID, Set Group ID, Linux 권한, chmod g+s, Linux 보안, 초보자 Linux, Linux 튜토리얼"
---

일반적으로 setgid 또는 SGID라고 부르는 set-group-ID 비트에는 중요한 용도가 두 가지 있습니다. 실행 가능한 일반 파일에서는 새 프로세스의 유효 그룹 ID를 바꿀 수 있습니다. 디렉터리에서는 새로 만든 항목이 디렉터리 그룹을 상속하게 하므로 협업 트리에 특히 유용합니다.

## 실행 파일의 Setgid

긴 목록은 그룹 실행 위치에 setgid를 표시할 수 있습니다.

```bash
$ ls -l /path/to/program
-rwxr-sr-x 1 root operators 24576 Jan 10 09:30 /path/to/program
```

소문자 `s`는 setgid와 그룹 실행이 모두 설정되어 있음을 뜻합니다. 대문자 `S`는 setgid가 설정되었지만 그룹 실행은 없다는 뜻입니다.

커널이 실행 중 이 비트를 적용하면 프로세스는 실행 파일의 그룹 소유자를 기준으로 한 유효 그룹 ID를 받습니다. `nosuid` 마운트 같은 제어가 동작을 억제할 수 있으며 모든 파일 형식이나 환경에 대한 보편적인 보장으로 다루면 안 됩니다.

:::single-choice{#setgid-executable-effect}
실행 파일의 setgid가 적용될 때 실행 파일의 그룹 소유자에서 가져오는 자격 증명은 무엇인가요?

::option[프로세스의 유효 그룹 ID]{#setgid-effective-group .correct explanation="Set-group-ID 실행은 실행 파일 소유자의 그룹을 프로세스의 유효 그룹 신원으로 설정합니다."}
::option[프로세스의 실제 사용자 ID]{#setgid-real-user explanation="이 비트는 호출자의 실제 사용자 신원이 아니라 그룹 자격 증명을 다룹니다."}
::option[프로세스가 여는 모든 파일의 소유자]{#setgid-opened-owner explanation="실행 자격 증명은 열린 파일의 소유권 메타데이터를 다시 쓰지 않습니다."}
:::

## 디렉터리의 Setgid

디렉터리의 setgid는 다른 목적을 갖습니다. 새 파일과 하위 디렉터리는 일반적으로 생성자의 기본 그룹 대신 디렉터리 그룹을 상속합니다. Linux에서는 새 하위 디렉터리도 setgid 비트를 상속하여 공유 프로젝트 트리가 일관된 그룹을 유지하도록 돕습니다.

Setgid 자체가 그룹 쓰기 접근을 부여하지는 않습니다. 디렉터리 모드, 프로세스 umask, 요청된 생성 모드, 기본 ACL 및 기타 제어가 여전히 접근을 결정합니다.

```bash
$ sudo chgrp developers /srv/project
$ sudo chmod g+s /srv/project
$ ls -ld /srv/project
drwxr-sr-x 2 root developers 4096 Jan 10 09:30 /srv/project
```

:::single-choice{#setgid-directory-inheritance}
`/srv/project`의 setgid는 일반적으로 새로 만든 파일이 무엇을 상속하게 하나요?

::option[디렉터리의 사용자 소유자]{#setgid-inherit-user explanation="디렉터리 setgid는 새 항목의 사용자 소유자가 아니라 그룹 상속에 영향을 줍니다."}
::option[디렉터리의 전체 권한 모드]{#setgid-inherit-mode explanation="생성 권한은 여전히 요청 모드, umask 및 ACL에서 계산됩니다."}
::option[디렉터리의 그룹 소유자]{#setgid-inherit-group .correct explanation="새 항목은 일반적으로 setgid 디렉터리의 그룹을 받아 일관된 공유 소유권을 지원합니다."}
:::

## Setgid 설정하고 제거하기

기호 방식으로 비트를 설정합니다.

```bash
$ sudo chmod g+s myfile
```

선행 8진수 `2`로 일반 모드 비트와 함께 설정합니다.

```bash
$ sudo chmod 2755 myfile
```

`chmod g-s myfile`로 특수 비트만 제거합니다.

:::single-choice{#setgid-octal-value}
Setgid가 선행 특수 비트 8진수 숫자에 더하는 값은 무엇인가요?

::option[`4`]{#setgid-value-four explanation="`4`는 특수 비트 숫자에서 setuid를 나타냅니다."}
::option[`1`]{#setgid-value-one explanation="`1`은 sticky 비트를 나타냅니다."}
::option[`2`]{#setgid-value-two .correct explanation="Setgid는 모드 `2755`처럼 `2`를 더합니다."}
:::

## 공유 디렉터리 안전하게 사용하기

협업 디렉터리에는 의도한 그룹 소유자, setgid, 좁게 선택한 접근 비트를 결합합니다. 대표 사용자로 생성을 시험하고 `ls -ld`로 결과를 확인하세요. 그룹 공유 문제를 해결하려고 트리를 모두에게 쓰기 가능하게 만들지 마세요. 전용 그룹, 적절한 umask나 기본 ACL, setgid 디렉터리가 일반적으로 더 명확한 제어를 제공합니다.

:::single-choice{#setgid-directory-write-access}
Setgid만 설정하면 그룹 구성원이 디렉터리에 파일을 만들 수 있나요?

::option[예. setgid는 항상 그룹 읽기, 쓰기, 실행을 추가합니다.]{#setgid-adds-rwx explanation="특수 비트는 일반 그룹 권한 비트 세 개를 자동으로 바꾸지 않습니다."}
::option[예. setgid는 그룹 구성원에 대한 모든 검사를 비활성화합니다.]{#setgid-disables-checks explanation="일반 임의 접근 검사와 추가 보안 검사는 계속 적용됩니다."}
::option[아니요. 적용되는 쓰기 및 검색 권한도 생성을 허용해야 합니다.]{#setgid-no-automatic-write .correct explanation="Setgid는 그룹 상속을 제어하고 일반 권한 및 다른 접근 제어가 디렉터리 쓰기를 지배합니다."}
:::

## 요약

이제 setgid가 실행 파일과 디렉터리에서 갖는 의미를 구분할 수 있습니다.

1. 그룹 실행 위치에서 setgid를 알아볼 수 있습니다.
2. 실행 파일 setgid를 유효 그룹 ID와 연결할 수 있습니다.
3. 디렉터리 setgid로 공유 트리의 그룹 소유권을 유지할 수 있습니다.
4. 일반 쓰기 접근과 혼동하지 않고 비트를 설정하거나 제거할 수 있습니다.
