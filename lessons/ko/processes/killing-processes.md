---
lesson_id: "killing-processes"
course_id: "processes"
lang: "ko"
order_index: 7
title: "kill (종료)"
description: "프로세스를 식별하고 안전한 단계적 순서로 kill을 사용해 적절한 시그널을 보내는 방법을 배웁니다."
meta_title: "kill (종료) - Processes"
meta_description: "Linux kill 명령으로 프로세스를 관리하고 종료하는 방법을 익혀 보세요. kill과 terminate의 차이 및 SIGTERM, SIGKILL, SIGHUP 같은 시그널을 다룹니다."
meta_keywords: "kill 명령, kill sigterm, kill sighup, linux kill -0, kill과 terminate, kill -15 linux, SIGTERM, SIGKILL, 프로세스 관리, 프로세스 종료"
---

`kill` 명령은 프로세스나 프로세스 그룹에 시그널을 보냅니다. 이름은 역사적인 것으로 요청한 시그널은 종료, 정지, 계속 또는 애플리케이션이 정의한 동작을 일으킬 수 있습니다. 시그널을 보내기 전에 항상 정확한 대상을 확인하고 프로그램에 문서화된 시그널 동작을 이해하세요.

## 질서 있는 종료 요청하기

PID만 지정하면 `kill`은 기본적으로 `SIGTERM`을 보냅니다.

```bash
$ kill 12445
```

시그널을 명시할 때는 기호 이름을 선호합니다.

```bash
$ kill -TERM 12445
```

`SIGTERM`의 기본 동작은 종료지만 프로그램이 잡거나 무시할 수 있습니다. 잘 설계된 서비스는 핸들러로 새 작업 수락을 멈추고 적절한 상태를 저장하고 애플리케이션 자원을 해제할 수 있습니다. 이는 가능성일 뿐 즉시 또는 성공적으로 정리된다는 보장은 아닙니다.

:::single-choice{#killing-processes-default-signal}
`kill PID`가 기본적으로 요청하는 시그널은 무엇인가요?

::option[`SIGKILL`]{#killing-processes-default-kill explanation="강제적이고 잡을 수 없는 시그널은 명시적으로 선택해야 합니다."}
::option[`SIGTERM`]{#killing-processes-default-term .correct explanation="다른 시그널 피연산자가 없으면 `kill`은 표준 종료 요청을 보냅니다."}
::option[`SIGSTOP`]{#killing-processes-default-stop explanation="프로세스 정지는 `kill`이 기본으로 요청하는 동작이 아닙니다."}
:::

## 대상 검증하기

PID는 재사용될 수 있으므로 오래된 PID가 나중에 다른 프로세스를 식별할 수 있습니다. 작업 직전에 살아 있는 대상을 확인하세요.

```bash
$ ps -p 12445 -o pid,ppid,user,lstart,stat,cmd
```

사용자, 시작 시간, 명령, 부모, 서비스 소유권, 운영 역할을 확인합니다. 서비스 관리자가 프로세스를 소유한다면 가능할 때 관리자의 중지 또는 다시 불러오기 명령을 사용하여 올바른 상태를 유지하고 자식이 즉시 재시작되지 않게 하세요.

자격 증명 규칙에 따라 자신이 소유한 프로세스에 시그널을 보낼 수 있습니다. 다른 사용자의 프로세스에 시그널을 보내려면 일반적으로 적절한 권한이 필요합니다. 모든 일치 항목을 검토하기 전에 범위가 넓은 이름 기반 명령을 사용하지 마세요.

:::single-choice{#killing-processes-pid-reuse}
시그널을 보내기 직전에 PID를 검사해야 하는 이유는 무엇인가요?

::option[프로세스가 파일을 읽을 때마다 PID가 바뀝니다.]{#killing-processes-pid-read explanation="살아 있는 프로세스는 일반적으로 수명 동안 같은 PID를 유지합니다."}
::option[이전 프로세스가 종료된 뒤 커널이 PID를 재사용할 수 있습니다.]{#killing-processes-pid-reused .correct explanation="기억해 둔 숫자 PID가 나중에 다른 살아 있는 프로세스를 가리킬 수 있습니다."}
::option[`kill`은 명령 이름만 받고 숫자 식별자는 받지 않습니다.]{#killing-processes-no-numeric explanation="숫자 PID는 `kill`의 일반적인 대상 피연산자입니다."}
:::

## 시그널 0으로 권한 확인하기

시그널 번호 0은 실제 시그널을 전달하지 않고 오류 검사를 수행합니다.

```bash
$ kill -0 12445
```

성공은 해당 순간 그 PID의 프로세스가 존재하고 호출자가 시그널을 보낼 수 있음을 뜻합니다. 실패는 모호합니다. 프로세스가 없거나 호출자에게 권한이 없을 수 있습니다. 모든 실패를 “실행 중 아님”으로 해석하지 말고 오류와 종료 상태를 확인하세요. 또한 순간적인 검사일 뿐 이후 PID 재사용 경쟁을 없애지는 못합니다.

:::single-choice{#killing-processes-signal-zero}
성공한 `kill -0 PID`는 그 순간 무엇을 확인하나요?

::option[프로세스가 모든 정리를 마치고 종료했습니다.]{#killing-processes-zero-exited explanation="성공은 종료 완료가 아니라 시그널을 보낼 수 있는 살아 있는 대상이 있다는 뜻입니다."}
::option[프로세스가 해당 PID를 영구적으로 유지합니다.]{#killing-processes-zero-permanent explanation="검사는 순간적이며 종료 뒤 PID를 재사용할 수 있습니다."}
::option[프로세스가 존재하고 호출자가 시그널을 보낼 수 있습니다.]{#killing-processes-zero-permitted .correct explanation="시그널 0은 일반 시그널을 전달하지 않고 대상 존재와 권한을 확인합니다."}
:::

## 필요할 때만 단계적으로 강화하기

권한 있는 대상이 `SIGTERM` 뒤에도 종료되지 않으면 작업 부하에 맞는 시간을 기다리고 이유를 조사하세요. 강제 종료가 정당화되면 다음을 보냅니다.

```bash
$ kill -KILL 12445
```

`SIGKILL`은 잡거나 무시하거나 차단할 수 없으므로 프로그램이 애플리케이션 수준 정리를 수행할 수 없습니다. 불완전한 트랜잭션, 임시 상태 또는 다른 구성 요소가 처리할 복구 작업을 남길 수 있습니다. 일상적인 첫 단계가 아니라 단계적 강화로 사용하세요.

다른 시그널의 의미는 수신 프로그램의 계약에 따라 달라집니다. `SIGHUP`은 흔히 구성 다시 불러오기를 요청하지만 일부 프로그램은 기본 종료 동작을 유지합니다. `SIGSTOP`은 정리 없이 일시 정지하고 `SIGCONT`는 정지된 프로세스를 재개합니다.

:::single-choice{#killing-processes-kill-tradeoff}
`SIGKILL`의 주된 운영상 단점은 무엇인가요?

::option[프로세스 소유자만 처리할 수 있습니다.]{#killing-processes-kill-owner-handler explanation="어떤 대상 프로세스도 `SIGKILL` 핸들러를 설치할 수 없습니다."}
::option[프로세스를 일시 정지할 뿐 종료하지 않습니다.]{#killing-processes-kill-pauses explanation="`SIGSTOP`이 일시 정지하며 `SIGKILL`은 종료합니다."}
::option[프로그램에 애플리케이션 수준 정리 기회를 주지 않습니다.]{#killing-processes-kill-no-cleanup .correct explanation="커널은 사용자 공간 시그널 핸들러를 호출하지 않고 종료를 강제합니다."}
:::

격리된 환경에서 자신이 시작한 프로세스에만 시그널 선택을 연습하세요. [Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864) 실습은 검사와 종료를 위한 통제된 작업 흐름을 제공합니다.

## 요약

이제 의도적이고 검증 가능한 작업 흐름으로 프로세스 시그널을 보낼 수 있습니다.

1. 작업 전에 살아 있는 대상과 감독자를 확인할 수 있습니다.
2. 정상 종료 요청으로 `SIGTERM`을 사용할 수 있습니다.
3. 시그널 0을 순간적인 존재 및 권한 검사로 해석할 수 있습니다.
4. 조사 후 정당한 단계적 강화에만 `SIGKILL`을 사용할 수 있습니다.
