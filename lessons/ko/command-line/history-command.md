---
lesson_id: "history-command"
course_id: "command-line"
lang: "ko"
order_index: 9
title: "history"
description: "Bash에서 명령어 히스토리를 확인하고 검색하며 재사용하고 관리하는 방법을 배웁니다."
meta_title: "history - 명령어 히스토리"
meta_description: "명령어 히스토리를 확인하고 재실행하는 방법, 역방향 검색, 항목 삭제, 터미널 초기화 등 Linux history 명령어 사용법을 예제와 함께 배워보세요."
meta_keywords: "리눅스 history 명령어, bash history, history -c, history -d, history -w, Ctrl-R, 명령어 히스토리, clear 명령어"
---

대화형 쉘은 입력한 명령어를 기록할 수 있습니다. 이 강의에서는 `history` 내장 명령어로 그 기록을 표시하고 관리하는 Bash를 다룹니다. 다른 쉘은 단축키, 파일 또는 설정이 다를 수 있습니다.

## Bash 히스토리 보기

사용한 명령어 목록을 보려면 `history`를 입력하세요.

```bash
$ history
  101  pwd
  102  ls -la
  103  cat notes.txt
```

각 줄에는 히스토리 번호와 명령어가 표시됩니다.

:::single-choice{#show-command-history}
현재의 번호가 매겨진 Bash 히스토리 목록을 표시하는 명령어는 무엇인가요?

::option[`clear`]{#clear-display explanation="`clear`는 보이는 터미널 영역을 새로 고치며 이전 명령어를 표시하지 않습니다."}
::option[`history -w`]{#write-history explanation="`history -w`는 현재 목록을 히스토리 파일에 씁니다. 목록 표시가 아니라 저장이 목적입니다."}
::option[`history`]{#show-history .correct explanation="`history` 내장 명령어는 현재 히스토리 목록의 명령어를 보통 히스토리 번호와 함께 출력합니다."}
:::

## 이전 명령어 재사용하기

쉘은 명령어를 다시 실행하기 쉽게 여러 단축키를 제공합니다.

- **위쪽 화살표**: 방금 실행한 명령어를 다시 실행하고 싶나요? 위쪽 화살표 키를 눌러 히스토리를 거꾸로 탐색할 수 있습니다.
- **`!!` 단축키**: 가장 최근 명령어를 다시 실행하려면 `!!`를 사용하세요. 예를 들어, 방금 `cat file1`을 실행했다면 `!!`를 입력하고 Enter를 누르면 `cat file1`이 다시 실행됩니다.
- **번호로 실행하기**: `!102`를 사용하면 히스토리 번호 102번 명령어를 실행합니다.
- **접두어로 실행하기**: `!cat`을 사용하면 `cat`으로 시작하는 가장 최근 명령어를 실행합니다.

`!`로 시작하는 히스토리 확장은 Enter를 누르는 즉시 명령어를 실행할 수 있습니다. 확신이 없다면, 특히 관리자 권한을 추가하거나 중요한 파일을 다루기 전에는 일치하는 명령어를 먼저 확인하세요.

:::single-choice{#repeat-most-recent-command}
가장 최근에 실행한 명령어를 반복하는 Bash 히스토리 확장은 무엇인가요?

::option[`!102`]{#event-number explanation="히스토리 번호 102인 명령어를 선택하므로 반드시 가장 최근 명령어인 것은 아닙니다."}
::option[`!cat`]{#event-prefix explanation="`cat`으로 시작하는 가장 최근 명령어를 선택할 뿐, 종류와 관계없는 가장 최근 명령어를 뜻하지 않습니다."}
::option[`!!`]{#previous-event .correct explanation="Bash에서 `!!`는 이전 명령어로 확장되며 줄을 제출하면 실행됩니다."}
:::

## 히스토리를 대화형으로 검색하기

가장 강력한 히스토리 단축키 중 하나는 `Ctrl-R`입니다. 역방향 검색을 시작합니다. `Ctrl-R`을 누른 후 찾고자 하는 명령어의 일부를 입력하면 쉘이 가장 최근에 일치하는 명령어를 보여줍니다. `Ctrl-R`을 반복해서 누르면 더 오래된 일치 항목들을 순환할 수 있습니다. 원하는 명령어를 찾으면 Enter를 눌러 실행하세요.

찾은 명령어를 실행 전에 수정하고 싶다면 Enter 대신 오른쪽 화살표 키나 왼쪽 화살표 키를 누르세요.

:::single-choice{#search-before-executing}
이전에 실행한 Bash 명령어 일부가 기억나 대화형으로 찾으려면 먼저 무엇을 눌러야 하나요?

::option[`Ctrl+D`]{#end-input explanation="`Ctrl+D`는 여러 터미널 환경에서 입력 끝을 알리고 대기 중인 쉘을 종료할 수도 있지만 히스토리 검색을 시작하지 않습니다."}
::option[`Ctrl+C`]{#cancel-input explanation="`Ctrl+C`는 보통 현재 작업을 중단하거나 취소하며 명령어 히스토리를 검색하지 않습니다."}
::option[`Ctrl+R`]{#reverse-search .correct explanation="`Ctrl+R`은 명령어 히스토리의 역방향 증분 검색을 시작하며 문자를 더 입력할수록 일치 범위가 좁아집니다."}
:::

## 히스토리 목록 관리하기

히스토리를 보는 것뿐 아니라 직접 관리할 수도 있습니다.

- **현재 히스토리 목록 지우기**: `history -c`는 메모리 내 히스토리 목록을 모두 제거합니다.
- **히스토리를 파일에 저장하기**: `history -w`는 현재 세션의 히스토리를 보통 `~/.bash_history` 파일에 저장합니다.
- **특정 항목 삭제하기**: `history -d <offset>`는 히스토리 번호로 특정 명령어를 삭제합니다.

예시:

```bash
$ history -d 101
$ history -w
```

메모리 목록을 지워도 이전 명령어가 모든 파일, 백업, 다른 활성 쉘에서 사라진다고 보장되지는 않습니다. 히스토리 동작은 Bash 설정과 세션이 파일을 읽고 쓰는 시점에도 좌우됩니다.

:::single-choice{#save-current-history-list}
현재 Bash 히스토리 목록을 설정된 히스토리 파일에 쓰는 명령어는 무엇인가요?

::option[`history -c`]{#clear-current-list explanation="`-c`는 메모리의 목록을 지울 뿐 현재 목록을 저장하도록 요청하지 않습니다."}
::option[`history -d 101`]{#delete-one-entry explanation="`-d`는 선택한 히스토리 항목 하나를 제거하며 전체 목록을 저장하는 작업이 아닙니다."}
::option[`history -w`]{#write-current-list .correct explanation="`-w`는 현재 히스토리 목록을 설정된 히스토리 파일에 씁니다."}
:::

## 화면 지우기와 이름 완성하기

터미널 창이 가득 차면 화면을 깨끗이 하고 싶을 수 있습니다. `clear` 명령어를 사용하면 화면을 지우고 새로 시작할 수 있습니다.

```bash
$ clear
```

이 명령어는 Bash 히스토리 목록을 지우지 않습니다. 터미널에 따라 이전 화면 내용은 스크롤백에 남을 수도 있습니다.

탭 완성도 다시 입력하는 수고를 줄여 줍니다. 명령어, 파일 이름 또는 디렉터리 이름의 시작 부분을 입력하고 Tab을 누르면, Bash가 일치 항목이 하나일 때 완성하거나 여러 항목을 보여 줄 수 있습니다.

명령줄은 히스토리에 저장될 수 있으므로 더 안전한 입력 방법이 있다면 비밀번호, 토큰 또는 비밀 값을 명령어에 직접 넣지 마세요.

:::single-choice{#distinguish-clear-from-history-clear}
메모리의 명령어 히스토리를 삭제하지 않고 보이는 터미널만 새로 고치려면 어떤 명령어를 실행해야 하나요?

::option[`clear`]{#clear-visible-area .correct explanation="`clear`는 Bash의 메모리 내 히스토리 목록을 유지하면서 보이는 터미널 영역만 새로 고칩니다."}
::option[`history -c`]{#clear-memory explanation="현재 메모리의 히스토리 항목을 제거하므로 화면만 새로 고치는 작업이 아닙니다."}
::option[`history -d 1`]{#delete-first-entry explanation="선택한 히스토리 항목을 삭제하도록 요청하며 보이는 터미널 영역을 지우지 않습니다."}
:::

## 요약

이제 히스토리를 의도적으로 관리하면서 Bash 명령어를 찾아 재사용할 수 있습니다.

1. 현재의 번호가 매겨진 히스토리 목록을 표시할 수 있습니다.
2. 이전 명령어를 주의해서 불러오거나 확장할 수 있습니다.
3. `Ctrl+R`로 히스토리를 대화형 검색할 수 있습니다.
4. 히스토리 항목을 삭제하거나 지우거나 파일에 쓸 수 있습니다.
5. 명령어 히스토리와 터미널 화면을 구분할 수 있습니다.
