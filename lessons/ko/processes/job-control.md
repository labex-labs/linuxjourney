---
lesson_id: "job-control"
course_id: "processes"
lang: "ko"
order_index: 11
title: "작업 제어"
description: "대화형 쉘이 포그라운드, 백그라운드, 정지된 작업을 관리하는 방법을 배웁니다."
meta_title: "작업 제어 - Processes"
meta_description: "백그라운드 프로세스를 효과적으로 관리하는 Linux 작업 제어를 알아봅니다. jobs, bg, fg, kill 명령으로 쉘 멀티태스킹을 익히세요."
meta_keywords: "Linux 작업 제어, 백그라운드 프로세스, jobs 명령, bg 명령, fg 명령, kill 명령, Linux 튜토리얼, 초보자 Linux"
---

대화형 쉘은 작업 제어로 한 터미널 세션 안의 파이프라인을 조정합니다. 작업은 프로세스 하나나 전체 파이프라인을 포함할 수 있으며 일반적으로 프로세스 그룹으로 묶여 터미널과 쉘이 하나의 단위로 작동할 수 있습니다.

## 백그라운드 작업 시작하기

파이프라인을 비동기로 시작하려면 `&`를 뒤에 붙입니다.

```bash
$ sleep 1000 &
[1] 18420
```

쉘은 작업이 끝나기를 기다리지 않고 프롬프트를 반환합니다. 백그라운드 상태는 출력을 자동으로 리디렉션하거나 제어 터미널에서 분리하거나 로그아웃 뒤에도 작업이 살아남게 하지 않습니다. 필요하면 입력과 출력을 명시적으로 리디렉션하고 대화형 쉘보다 오래 살아야 하는 작업에는 서비스 관리자, 스케줄러 또는 터미널 멀티플렉서를 사용하세요.

백그라운드 작업이 제어 터미널에서 읽으려 하면 터미널의 포그라운드 프로세스 그룹이 아니므로 일반적으로 `SIGTTIN`으로 정지됩니다.

:::single-choice{#job-control-ampersand-effect} 대화형 쉘에서 뒤의 `&`는 무엇을 요청하나요?

::option[작업이 로그아웃과 시스템 재시작 뒤에도 살아남도록 보장합니다.]{#job-control-survive-restart explanation="백그라운드 실행만으로는 지속 감독이나 재시작 지속성을 제공하지 않습니다."}
::option[다음 프롬프트 전에 기다리지 않고 파이프라인을 백그라운드 작업으로 실행합니다.]{#job-control-background-job .correct explanation="쉘은 작업을 비동기로 시작하고 이후 명령을 받을 수 있는 상태로 남습니다."}
::option[작업의 표준 출력과 오류를 버립니다.]{#job-control-discard-output explanation="리디렉션하지 않으면 백그라운드 작업도 터미널에 쓸 수 있습니다."}
:::

## 쉘 작업 나열하기

`jobs` 내장 명령은 현재 쉘이 아는 작업을 나열합니다.

```text
$ jobs
[1]    Running    sleep 1000 &
[2]-   Running    sleep 1001 &
[3]+   Stopped    sleep 1002
```

대괄호 안 숫자는 PID가 아니라 쉘 작업 ID입니다. `%` 접두사는 `%1` 같은 작업 지정을 만듭니다. `+` 표시는 피연산자가 없을 때 여러 명령이 선택하는 현재 작업을 식별하고 `-`는 이전 작업을 식별합니다.

작업 테이블은 한 쉘에 속하므로 다른 터미널의 쉘은 일반적으로 자체 `jobs`, `fg`, `bg` 내장 명령으로 이 작업을 나열하거나 지정할 수 없습니다.

:::single-choice{#job-control-jobs-scope} `jobs` 내장 명령은 무엇을 나열하나요?

::option[현재 쉘 세션이 추적하는 작업]{#job-control-jobs-current-shell .correct explanation="작업 ID와 상태는 해당 작업을 시작하거나 받아들인 대화형 쉘이 유지합니다."}
::option[현재 시스템에서 보이는 모든 프로세스]{#job-control-jobs-all-processes explanation="시스템 전체 프로세스 검사는 `ps` 같은 도구의 역할이며 쉘 작업 테이블은 범위가 더 좁습니다."}
::option[시스템 부팅 중 시작된 서비스만]{#job-control-jobs-boot-services explanation="부팅 서비스는 일반적으로 대화형 쉘 작업 테이블이 아니라 서비스 관리자가 감독합니다."}
:::

## 작업 정지하고 계속하기

작업이 포그라운드에 있을 때 `Ctrl-Z`를 누르면 일반적으로 터미널이 포그라운드 프로세스 그룹에 `SIGTSTP`를 보냅니다. 작업이 정지한 뒤 쉘이 제어를 되찾습니다.

```text
$ sleep 1002
^Z
[3]+  Stopped    sleep 1002
```

현재 정지된 작업을 백그라운드에서 계속합니다.

```bash
$ bg
```

`bg`는 계속 시그널을 보내고 작업을 터미널 포그라운드 밖에 둡니다. 정지된 작업에만 유용하며 이미 백그라운드에서 실행 중인 명령은 재개할 필요가 없습니다.

:::single-choice{#job-control-bg-purpose} `bg %3`은 정지된 작업 3에 무엇을 하나요?

::option[파일을 `bg`라는 디렉터리로 옮깁니다.]{#job-control-bg-files explanation="`bg`는 쉘 작업 제어 내장 명령이며 파일 시스템 객체를 옮기지 않습니다."}
::option[백그라운드 작업으로 계속 실행합니다.]{#job-control-bg-continue .correct explanation="쉘은 선택된 정지 작업을 터미널 포그라운드로 지정하지 않고 재개합니다."}
::option[`SIGKILL`로 종료합니다.]{#job-control-bg-kill explanation="내장 명령은 작업을 종료하지 않고 계속합니다."}
:::

## 작업을 포그라운드로 옮기기

작업 지정과 함께 `fg`를 사용하여 작업을 터미널의 포그라운드 프로세스 그룹으로 만들고 기다립니다.

```bash
$ fg %1
```

피연산자가 없으면 `fg`는 일반적으로 `+`로 표시된 현재 작업을 선택합니다. 정지된 작업은 포그라운드로 들어가면서 재개됩니다.

:::single-choice{#job-control-fg-effect} `fg %1`은 무엇을 하나요?

::option[작업 1을 터미널 포그라운드에 지정하고 기다립니다.]{#job-control-fg-foreground .correct explanation="쉘은 선택된 작업을 포그라운드로 만들어 터미널과 상호작용하게 합니다."}
::option[작업 1을 PID 1로 바꿉니다.]{#job-control-fg-pid-one explanation="쉘 작업 ID는 프로세스 ID를 교체하거나 다시 쓰지 않습니다."}
::option[작업 1의 두 번째 사본을 백그라운드에서 시작합니다.]{#job-control-fg-copy explanation="`fg`는 복제본을 만들지 않고 기존 작업에 작동합니다."}
:::

## 작업에 시그널 보내기

쉘은 `kill`이 작업 지정을 받도록 합니다.

```bash
$ kill -TERM %1
```

일반적으로 파이프라인 구성원 하나가 아니라 작업의 프로세스 그룹에 시그널을 보냅니다. 먼저 선택한 작업을 검사하고 강제적 단계로 강화하기 전에 `SIGTERM`을 사용하세요. 작업 지정은 쉘 구문이며 스크립트와 외부 도구는 일반적으로 검증된 PID나 프로세스 그룹 ID를 사용합니다.

:::single-choice{#job-control-job-specification} 프로세스 ID 1이 아니라 쉘 작업 1을 가리키는 피연산자는 무엇인가요?

::option[`1`]{#job-control-plain-one explanation="`kill`의 일반 숫자 피연산자는 보통 PID로 해석됩니다."}
::option[`#1`]{#job-control-hash-one explanation="해시 접두사는 여기서 소개한 쉘 작업 ID 구문이 아닙니다."}
::option[`%1`]{#job-control-percent-one .correct explanation="퍼센트 접두사는 쉘 작업 지정을 식별합니다."}
:::

[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864) 실습에서 `sleep` 같은 무해한 명령으로 작업을 연습하세요.

## 요약

이제 쉘이 제어하는 상태 사이에서 작업을 의도적으로 이동할 수 있습니다.

1. `&`로 자동 분리 없이 백그라운드 작업을 시작할 수 있습니다.
2. `jobs`로 현재 쉘의 작업 테이블을 검사할 수 있습니다.
3. `Ctrl-Z`로 정지하고 `bg`로 백그라운드에서 계속할 수 있습니다.
4. `fg`로 선택한 작업을 터미널로 되돌릴 수 있습니다.
5. 시그널을 보낼 때 `%JOB_ID`로 쉘 작업을 지정할 수 있습니다.
