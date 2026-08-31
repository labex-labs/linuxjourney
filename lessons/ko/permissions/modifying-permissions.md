---
lesson_id: "modifying-permissions"
course_id: "permissions"
lang: "ko"
order_index: 2
title: "권한 수정하기"
description: "기호 및 8진수 chmod 모드로 Linux 권한 비트를 변경하는 방법을 배웁니다."
meta_title: "권한 수정하기 - Permissions"
meta_description: "chmod 명령으로 Linux 권한을 변경하는 방법을 배웁니다. 파일과 디렉터리 접근을 안전하게 관리하기 위한 기호 방식과 숫자 방식을 모두 다룹니다."
meta_keywords: "linux 권한 변경, linux 파일 권한 변경, chmod, 파일 권한, linux 보안, 기호 권한, 숫자 권한"
---

`chmod` 명령은 파일과 디렉터리의 모드 비트를 변경합니다. 일반적으로 파일 소유자나 필요한 권한이 있는 프로세스만 변경할 수 있습니다. `chmod`를 실행하기 전후에 `ls -l`로 현재 모드를 확인하세요.

## 기호 모드 사용하기

기호 모드는 변경할 권한 클래스, 변경 방식, 관련 권한을 나타냅니다.

- `u`: 소유자 클래스
- `g`: 그룹 클래스
- `o`: 기타 사용자 클래스
- `a`: 세 클래스 모두
- `+`: 권한 추가, `-`: 권한 제거, `=`: 선택한 클래스를 정확히 설정

예를 들어 소유자에게 실행 권한을 추가합니다.

```bash
$ chmod u+x myfile
```

그룹에서 쓰기 권한을 제거합니다.

```bash
$ chmod g-w myfile
```

소유자와 그룹 모두에 쓰기 권한을 추가합니다.

```bash
$ chmod ug+w myfile
```

여러 절은 쉼표로 구분할 수 있습니다. 다음 명령은 소유자를 읽기와 쓰기, 그룹을 읽기 전용, 기타 사용자를 권한 없음으로 설정합니다.

```bash
$ chmod u=rw,g=r,o= myfile
```

`chmod +x myfile`처럼 클래스를 생략하면 프로세스 umask가 변경할 클래스에 영향을 줍니다. 클래스를 명시하면 의도한 결과를 더 쉽게 검토할 수 있습니다.

:::single-choice{#modifying-permissions-remove-group-write}
다른 그룹 비트를 바꾸지 않고 그룹 쓰기 권한을 제거하는 기호 모드는 무엇인가요?

::option[`chmod u-w myfile`]{#modifying-permissions-user-minus-write explanation="그룹이 아니라 소유자 클래스에서 쓰기 권한을 제거합니다."}
::option[`chmod g-w myfile`]{#modifying-permissions-group-minus-write .correct explanation="`g`는 그룹 클래스를 선택하고 `-`는 비트를 제거하며 `w`는 쓰기 권한을 나타냅니다."}
::option[`chmod g=w myfile`]{#modifying-permissions-group-equals-write explanation="`=` 연산자는 쓰기를 제거하지 않고 선택한 클래스를 쓰기 전용 권한으로 교체합니다."}
:::

## 8진수 모드 사용하기

8진수 모드는 각 기본 권한 묶음을 숫자 하나로 설정합니다. 각 클래스에서 다음 값을 더합니다.

- 읽기: `4`
- 쓰기: `2`
- 실행: `1`
- 권한 없음: `0`

오른쪽 세 숫자는 차례대로 소유자, 그룹, 기타 사용자를 나타냅니다. 예를 들면 다음과 같습니다.

```bash
$ chmod 755 myfile
```

`755` 모드는 다음과 같이 펼쳐집니다.

- 소유자 `7`은 `4 + 2 + 1`, 즉 `rwx`
- 그룹 `5`는 `4 + 1`, 즉 `r-x`
- 기타 사용자 `5`는 `4 + 1`, 즉 `r-x`

`+`나 `-` 기호 작업과 달리 8진수 모드는 일반 권한 집합 전체를 제공합니다. 뒤의 레슨에서 특수 모드 비트에 쓰는 선택적 선행 숫자를 다룹니다.

:::single-choice{#modifying-permissions-octal-read-value}
읽기 권한을 나타내는 8진수 값은 무엇인가요?

::option[`1`]{#modifying-permissions-value-one explanation="`1`은 실행 권한을 나타냅니다."}
::option[`2`]{#modifying-permissions-value-two explanation="`2`는 쓰기 권한을 나타냅니다."}
::option[`4`]{#modifying-permissions-value-four .correct explanation="읽기 권한은 클래스 숫자에 8진수 값 `4`를 더합니다."}
:::

:::single-choice{#modifying-permissions-mode-640}
`chmod 640 report`는 어떤 일반 권한을 설정하나요?

::option[소유자 읽기, 그룹 쓰기, 기타 사용자 실행]{#modifying-permissions-640-separated explanation="8진수 숫자는 별도의 읽기, 쓰기, 실행 열이 아니라 각 클래스의 합입니다."}
::option[소유자 읽기/실행, 그룹 쓰기, 기타 사용자 권한 없음]{#modifying-permissions-640-wrong-sums explanation="소유자 값 `6`은 읽기와 쓰기이고 그룹 값 `4`는 읽기입니다."}
::option[소유자 읽기/쓰기, 그룹 읽기, 기타 사용자 권한 없음]{#modifying-permissions-640-correct .correct explanation="숫자는 소유자 `6`(`rw-`), 그룹 `4`(`r--`), 기타 사용자 `0`(`---`)으로 펼쳐집니다."}
:::

## 변경 안전하게 적용하기

사용자와 서비스에 필요한 접근만 부여하세요. `chmod 777`을 문제 해결 단축 방법으로 사용하지 마세요. 모든 클래스에 읽기, 쓰기, 실행을 부여하여 위험을 키우면서도 소유권, 디렉터리 탐색, ACL, 서비스 정책 문제는 해결하지 못하는 경우가 많습니다.

재귀 변경은 특히 주의해야 합니다. 대상 트리를 미리 확인하고 심볼릭 링크와 마운트된 파일 시스템을 고려하며 `chmod -R`을 사용하기 전에 작은 범위에서 시험하세요. 변경 후에는 명령이 의도한 객체에 영향을 줬다고 가정하지 말고 결과 모드를 확인합니다.

:::single-choice{#modifying-permissions-least-privilege}
`chmod 777`이 접근 문제의 일반적인 해결책으로 적합하지 않은 이유는 무엇인가요?

::option[소유자의 모든 권한을 제거합니다.]{#modifying-permissions-777-removes explanation="각 `7`은 읽기, 쓰기, 실행을 부여하며 소유자 권한을 제거하지 않습니다."}
::option[소유자, 그룹, 기타 사용자 모두에게 모든 기본 권한을 부여합니다.]{#modifying-permissions-777-grants-all .correct explanation="세 클래스 모두 `rwx`를 받아 실제로 필요한 접근 범위를 흔히 초과합니다."}
::option[파일의 그룹 소유권만 변경합니다.]{#modifying-permissions-777-group explanation="`chmod`는 모드 비트를 바꾸며 그룹 소유권은 `chgrp`나 `chown` 같은 도구로 바꿉니다."}
:::

격리된 환경에서 실습하려면 [Linux 사용자 그룹과 파일 권한](https://labex.io/ko/labs/linux-linux-user-group-and-file-permissions-18002) 실습을 사용하고 각 모드를 변경하기 전후에 확인하세요.

## 요약

이제 의도적인 `chmod` 표현식으로 일반 Linux 모드 비트를 변경할 수 있습니다.

1. 기호 모드로 특정 권한을 추가하거나 제거하거나 할당할 수 있습니다.
2. 읽기 `4`, 쓰기 `2`, 실행 `1`로 8진수 숫자를 만들 수 있습니다.
3. 8진수 클래스를 소유자, 그룹, 기타 사용자 순서로 읽을 수 있습니다.
4. 변경을 검증하고 필요한 최소 권한만 적용할 수 있습니다.
