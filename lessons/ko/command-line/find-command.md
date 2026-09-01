---
lesson_id: "find-command"
course_id: "command-line"
lang: "ko"
order_index: 14
title: "find"
description: "디렉터리 트리를 이름, 유형, 크기, 시간으로 검색하고 확인한 결과에 작업하는 방법을 배웁니다."
meta_title: "find - 명령줄 명령어"
meta_description: "이름, 유형, 크기, 수정 시간으로 검색하고 일치하는 파일에 작업을 실행하는 Linux find 명령어를 예제와 함께 배워보세요."
meta_keywords: "리눅스 find 명령어, find 명령어, 리눅스에서 파일 찾기, 이름으로 찾기, 유형으로 찾기, 크기로 찾기, mtime으로 찾기, find exec"
---

시스템에 수많은 파일이 있을 때 특정 파일을 찾는 것은 어려울 수 있습니다. `find` 명령어는 이름, 유형, 크기, 수정 시간과 같은 기준을 사용하여 디렉터리 트리를 검색합니다.

## 검색 시작 위치 선택하기

기본 구문은 다음과 같습니다:

```bash
find [PATH] [EXPRESSION]
```

경로는 시작점을 선택하고 표현식은 그 아래 항목을 선택하거나 항목에 작업을 수행합니다.

예를 들어 `/home` 디렉터리와 그 하위 디렉터리에서 `puppies.jpg`라는 파일을 찾으려면 다음과 같이 사용합니다:

```bash
$ find /home -name puppies.jpg
```

검색은 기본적으로 재귀적입니다. 현재 디렉터리 트리를 검색하려면 시작 경로로 `.`을 사용합니다.

:::single-choice{#search-current-tree} 현재 디렉터리와 그 하위에서 이름이 `notes.txt`인 항목을 찾는 명령어는 무엇인가요?

::option[`find . -name notes.txt`]{#find-current-notes .correct explanation="점은 현재 디렉터리를 시작 경로로 선택하고 `-name`은 각 항목의 기본 이름을 검사합니다."}
::option[`find / -name notes.txt`]{#find-root-notes explanation="시작 경로 `/`는 현재 디렉터리 트리보다 훨씬 넓은 파일 시스템 루트부터 검색합니다."}
::option[`find notes.txt .`]{#find-operands-reversed explanation="`find`는 표현식보다 시작 경로를 먼저 받으므로 이 순서는 요청한 검색을 나타내지 않습니다."}
:::

## 이름과 유형 일치시키기

`find`의 가장 일반적인 용도 중 하나는 파일 이름으로 검색하는 것입니다. `-name` 옵션은 이름을 정확히 일치시키거나 셸 스타일 패턴으로 일치시킵니다.

```bash
$ find . -name "*.txt"
```

와일드카드 패턴은 현재 쉘이 먼저 확장하지 않고 `find`에 그대로 전달하도록 따옴표로 묶습니다. 대소문자를 무시하려면 `-name` 대신 `-iname`을 사용합니다.

검색하려는 항목의 유형을 지정할 수도 있습니다. `-type` 옵션이 이 용도로 사용됩니다. 예를 들어, 파일 대신 디렉터리를 찾으려면 `d`를 사용할 수 있습니다.

```bash
$ find /home -type d -name MyFolder
```

이 명령어에서는 유형을 디렉터리인 `d`로 설정하고 `MyFolder`라는 이름의 항목을 찾고 있습니다. 일반 파일만 검색하려면 `-type f`를 사용합니다.

:::single-choice{#find-text-regular-files} 현재 디렉터리 아래에서 이름이 `.txt`로 끝나는 일반 파일을 찾는 명령어는 무엇인가요?

::option[`find . -type f -name "*.txt"`]{#text-files .correct explanation="`-type f`는 일반 파일을 선택하고 따옴표로 묶은 `-name` 패턴은 `find`가 각 항목에 평가합니다."}
::option[`find . -type d -name "*.txt"`]{#text-directories explanation="패턴은 올바르게 묶였지만 `-type d`는 일반 파일이 아니라 디렉터리를 선택합니다."}
::option[`find . -type f -name *.txt`]{#unquoted-text-files explanation="따옴표 없는 와일드카드는 `find`가 실행되기 전에 현재 쉘이 확장해 표현식을 바꿀 수 있습니다."}
:::

## 크기와 수정 시간 일치시키기

파일 크기로 검색할 수 있습니다:

```bash
$ find . -type f -size +10M
$ find . -type f -size -1k
```

대문자 `M`은 1,048,576바이트 단위이고 소문자 `k`는 1,024바이트 단위입니다. `find`는 숫자를 비교하기 전에 크기를 선택한 단위로 올림합니다.

수정 시간으로도 검색할 수 있습니다:

```bash
$ find . -type f -mtime -7
$ find . -type f -mtime +30
```

`-mtime`은 수정된 뒤 지난 완전한 24시간 단위 수를 검사합니다. `-mtime -7`은 7보다 작은 값, `-mtime +30`은 30보다 큰 값과 일치하며 달력의 자정 경계를 기준으로 하지 않습니다.

:::single-choice{#find-recent-regular-files} `.` 아래에서 수정된 지 완전한 24시간 단위로 7보다 적은 일반 파일을 찾는 명령어는 무엇인가요?

::option[`find . -type f -mtime -7`]{#recent-files .correct explanation="`-type f`는 일반 파일을, `-mtime -7`은 수정 경과 시간이 완전한 24시간 단위로 7보다 작은 항목을 선택합니다."}
::option[`find . -type f -mtime +7`]{#older-than-seven explanation="더하기 기호는 7단위보다 큰 값을 선택하므로 최근 파일이 아니라 더 오래된 파일을 찾습니다."}
::option[`find . -type d -mtime -7`]{#recent-directories explanation="시간 조건은 최근 항목을 찾지만 `-type d`가 결과를 일반 파일이 아닌 디렉터리로 제한합니다."}
:::

## 일치 항목 출력 및 작업하기

기본적으로 `find`는 일치하는 경로를 출력합니다. `-print`, `-delete`, `-exec`와 같은 작업을 추가할 수 있습니다.

일치 항목을 명시적으로 출력하기:

```bash
$ find . -name "*.log" -print
```

각 일치 항목에 대해 `ls -l` 실행하기:

```bash
$ find . -name "*.log" -exec ls -l {} \;
```

`\;` 형식에서 `{}`는 명령어를 실행할 때마다 현재 일치 경로로 바뀝니다. 세미콜론은 `-exec` 작업의 끝이며 쉘이 `find`에 전달하도록 이스케이프합니다.

`-delete`나 파일을 변경하는 `-exec` 같은 파괴적 작업 전에는 같은 조건에 `-print`를 붙여 모든 결과를 확인하세요. 좁은 시작 경로와 `-maxdepth N`으로 범위를 제한할 수도 있습니다.

:::single-choice{#verify-before-delete} 나중에 오래된 `.log` 파일을 삭제할 수도 있는 `find` 명령어를 작성 중입니다. 먼저 무엇을 해야 하나요?

::option[즉시 `-delete`를 붙이고 어떤 파일이 사라지는지 확인합니다.]{#delete-first explanation="삭제는 안전한 미리보기가 아니며 실행 취소도 없습니다. 추가하기 전에 전체 일치 집합을 확인해야 합니다."}
::option[같은 조건을 `-print`로 실행하고 모든 일치 항목을 확인합니다.]{#print-first .correct explanation="읽기 전용 목록으로 시작 경로와 조건을 검증한 뒤 파괴적 작업을 도입할 수 있습니다."}
::option[로그 파일을 놓치지 않도록 `/`부터 검색합니다.]{#root-first explanation="`/`부터 시작하면 범위가 넓어져 관련 없는 경로나 보호된 경로까지 포함할 수 있으므로 가능한 가장 좁은 시작점을 사용합니다."}
:::

:::single-choice{#run-ls-for-each-match} `find . -name "*.log" -exec ls -l {} \;`에서 `{}`는 무엇을 나타내나요?

::option[`ls -l`에 전달되는 현재 일치 경로입니다.]{#match-placeholder .correct explanation="이 `-exec` 형식에서 `find`는 `ls -l`을 실행하기 전에 `{}`를 현재 일치 항목으로 바꿉니다."}
::option[`find` 명령어를 시작한 디렉터리입니다.]{#starting-placeholder explanation="시작 디렉터리는 명령 앞부분의 점이며 중괄호는 `-exec` 안에서 다른 역할을 합니다."}
::option[`-exec` 표현식을 끝내는 세미콜론입니다.]{#terminator-placeholder explanation="이스케이프된 세미콜론이 작업을 끝내며 중괄호는 경로 자리 표시자입니다."}
:::

권한 거부 메시지는 보통 현재 계정이 트리 일부를 검색할 수 없음을 뜻합니다. 관련 있는 더 좁은 시작 경로를 선택하고, 확장된 접근을 이해하고 의도하기 전에는 관리자 권한을 추가하지 마세요.

검색 표현식을 만드는 방법은 다음 실습으로 연습해 보세요.

1. **[Linux find Command: File Searching](https://labex.io/ko/labs/linux-linux-find-command-file-searching-219191)** - 이 실습은 다양한 기준으로 파일과 디렉터리를 검색하는 다용도 유틸리티인 `find` 명령어 소개를 제공합니다. 특정 파일을 찾는 연습을 하게 됩니다.
2. **[Discover Critical System Resources](https://labex.io/ko/labs/linux-discover-critical-system-resources-388032)** - `find`를 포함한 필수 Linux 명령어를 배우고 파일 시스템을 효율적으로 탐색하며 중요한 시스템 리소스를 발견하는 연습을 합니다.

## 요약

이제 범위가 뚜렷한 `find` 표현식을 만들고 작업 전에 결과를 검증할 수 있습니다.

1. 유용한 범위에서 가장 좁은 시작 경로를 선택할 수 있습니다.
2. 이름 패턴을 따옴표로 묶고 유형 검사와 결합할 수 있습니다.
3. 크기 또는 완전한 24시간 수정 기간으로 필터링할 수 있습니다.
4. 필요할 때 재귀 깊이를 제한할 수 있습니다.
5. 파괴적 작업 전에 일치 항목을 출력하고 확인할 수 있습니다.
