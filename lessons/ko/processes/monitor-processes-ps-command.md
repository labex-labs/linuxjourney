---
lesson_id: "monitor-processes-ps-command"
course_id: "processes"
lang: "ko"
order_index: 1
title: "ps (프로세스)"
description: "ps로 프로세스 스냅샷을 만들고 top으로 변하는 활동을 모니터링하는 방법을 배웁니다."
meta_title: "ps (프로세스) - Processes"
meta_description: "Linux ps 명령 종합 가이드입니다. ps -ef와 다른 옵션으로 실행 중인 프로세스를 보고 PID를 이해하며 시스템 작업을 관리하는 방법을 배웁니다."
meta_keywords: "ps 명령, ps -ef linux, ps -ef 명령, linux ps -ef, ps -e linux, Linux 프로세스, 프로세스 ID, PID, top 명령, linux journey"
---

프로세스는 프로그램이 실행 중인 인스턴스이며 메모리, 자격 증명, 열린 자원, 실행 상태를 함께 포함합니다. Linux는 살아 있는 각 프로세스를 PID라는 숫자 프로세스 ID로 식별합니다. PID는 같은 시점에 존재하는 프로세스 사이에서 고유하지만 프로세스가 종료된 뒤 커널이 재사용할 수 있습니다.

## 기본 스냅샷 만들기

옵션 없이 `ps`를 실행하면 구현의 기본값으로 선택된 스냅샷을 볼 수 있습니다. 일반적으로 현재 터미널 및 사용자와 연결된 프로세스입니다.

```text
$ ps
    PID TTY          TIME CMD
  41230 pts/4    00:00:00 bash
  51224 pts/4    00:00:00 ps
```

일반적인 필드는 다음과 같습니다.

- `PID`: 프로세스 ID
- `TTY`: 제어 터미널. 연결된 터미널이 없으면 `?`
- `TIME`: 경과한 실제 시간이 아니라 누적 CPU 시간
- `CMD`: 선택한 형식에 따른 명령 이름 또는 명령줄

정확한 열과 선택 기본값은 `ps` 구현과 환경에 따라 다릅니다.

:::single-choice{#ps-command-pid-meaning} `PID` 열은 무엇을 식별하나요?

::option[프로세스의 현재 디렉터리 번호]{#ps-command-pid-directory explanation="현재 디렉터리는 파일 시스템 참조이며 PID로 표현되지 않습니다."}
::option[누적 CPU 시간(초)]{#ps-command-pid-cpu explanation="CPU 사용량은 `TIME` 같은 별도 필드에 표시됩니다."}
::option[커널이 할당한 프로세스 ID]{#ps-command-pid-kernel .correct explanation="PID는 살아 있는 프로세스를 가리키는 데 쓰이는 숫자 식별자입니다."}
:::

## BSD 형식 옵션으로 프로세스 나열하기

Linux `ps`는 여러 옵션 형식을 받습니다. BSD 형식 옵션은 흔히 선행 하이픈 없이 씁니다.

```bash
$ ps aux
```

이 조합에서 다음 의미를 갖습니다.

- `a`: 터미널이 있는 다른 사용자 소유 프로세스까지 선택 확대
- `x`: 제어 터미널이 없는 프로세스도 포함하고 `a`와 결합할 때 선택 확대
- `u`: `USER`, `%CPU`, `%MEM`, `VSZ`, `RSS` 같은 필드를 가진 사용자 중심 출력 형식 선택

옵션 의미가 상호작용할 수 있으므로 각 문자를 독립적인 명령으로 보지 말고 전체 조합을 해석하세요.

:::single-choice{#ps-command-aux-user-format} `ps aux`에서 사용자 중심 출력 형식을 요청하는 옵션은 무엇인가요?

::option[`u`]{#ps-command-aux-u .correct explanation="BSD 형식 `u` 옵션은 사용자 중심의 출력 열 집합을 선택합니다."}
::option[`x`]{#ps-command-aux-x explanation="`x` 옵션은 특히 제어 터미널이 없는 프로세스 등 프로세스 선택에 영향을 줍니다."}
::option[`a`]{#ps-command-aux-a explanation="`a` 옵션은 현재 사용자의 터미널 프로세스만 보던 선택 범위를 넓힙니다."}
:::

## 표준 형식 옵션 사용하기

널리 쓰이는 표준 형식 명령 `ps -ef`는 선행 하이픈과 함께 옵션을 씁니다.

```bash
$ ps -ef
```

- `-e`: 호출자에게 보이는 모든 프로세스 선택
- `-f`: 전체 형식 목록 요청

출력에는 일반적으로 `UID`, `PID`, `PPID`, 시작 시간, 명령 정보가 포함됩니다. `PPID`는 부모 프로세스 ID입니다. 이 목록은 본질적으로 계층적이지 않습니다. 부모-자식 배치가 중요하면 지원되는 경우 `--forest` 같은 옵션이나 `pstree` 같은 전용 트리 보기를 사용하세요.

:::single-choice{#ps-command-ef-selection} `ps -ef`에서 `-e`는 무엇을 요청하나요?

::option[중단할 때까지 매초 갱신]{#ps-command-e-refresh explanation="`ps`는 스냅샷을 만듭니다. 지속 갱신은 `top` 같은 도구의 기능입니다."}
::option[호출자에게 보이는 모든 프로세스를 포함하는 선택]{#ps-command-e-every .correct explanation="표준 형식 `-e` 옵션은 선택 가능한 모든 프로세스로 스냅샷 범위를 넓힙니다."}
::option[명령이 오류로 끝난 프로세스만 선택]{#ps-command-e-errors explanation="프로세스 선택은 명령의 최종 종료 상태를 기준으로 하지 않습니다."}
:::

## 시간에 따른 활동 모니터링하기

`ps`는 스냅샷 하나를 만든 뒤 종료합니다. 주기적으로 갱신되는 대화형 보기에는 `top`을 사용합니다.

```bash
$ top
```

`top`은 변하는 CPU 및 메모리 소비자를 식별하는 데 도움이 되지만 값은 표본이므로 흔들릴 수 있습니다. 여러 번 관찰하여 의심되는 문제를 확인하고 백분율을 시스템의 CPU 수, 메모리 계산, 작업 부하와 연결하세요.

:::single-choice{#ps-command-snapshot-versus-top} 여기서 소개한 도구 중 기본적으로 프로세스 표시를 주기적으로 갱신하는 것은 무엇인가요?

::option[`top`]{#ps-command-top-refresh .correct explanation="`top`은 일정 간격으로 표시를 갱신하는 대화형 모니터입니다."}
::option[`ps -ef`]{#ps-command-ps-ef-snapshot explanation="전체 형식 프로세스 스냅샷을 출력한 뒤 종료합니다."}
::option[`ls -l`]{#ps-command-ls-files explanation="`ls -l`은 실시간 프로세스 모니터가 아니라 파일 시스템 항목을 표시합니다."}
:::

실습에서는 [Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)으로 스냅샷과 대화형 모니터를 비교하거나 [Linux top 명령](https://labex.io/ko/labs/linux-linux-top-command-real-time-system-monitoring-388500) 실습에서 정렬과 필터링을 살펴보세요.

## 요약

이제 프로세스 보기를 선택하고 기본 식별자를 해석할 수 있습니다.

1. PID를 현재 살아 있는 프로세스에 대한 재사용 가능한 식별자로 다룰 수 있습니다.
2. 일반 `ps`로 작은 기본 스냅샷을 만들 수 있습니다.
3. `ps aux` 또는 `ps -ef`로 더 넓은 선택과 풍부한 열을 볼 수 있습니다.
4. 시간에 따른 변화가 중요할 때 `top`을 사용할 수 있습니다.
