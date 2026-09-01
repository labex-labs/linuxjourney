---
lesson_id: "process-niceness"
course_id: "processes"
lang: "ko"
order_index: 8
title: "Niceness"
description: "nice 값이 일반 Linux 프로세스의 CPU 스케줄링 가중치에 영향을 주는 방식을 배웁니다."
meta_title: "niceness - Processes"
meta_description: "Linux의 niceness와 프로세스 우선순위에 미치는 영향을 알아봅니다. nice와 renice 명령으로 CPU 스케줄링을 관리하는 방법을 배웁니다."
meta_keywords: "niceness linux, linux niceness, linux niceness란, linux 프로세스 niceness, 프로세스 niceness, 프로세스 우선순위, nice 명령, renice 명령, CPU 스케줄링"
---

Linux는 서로 다른 CPU 코어에서 스레드를 동시에 실행하고 한 번에 실행할 수 있는 수보다 많은 실행 가능 스레드가 있을 때 코어 시간을 나눌 수 있습니다. 스케줄러는 스케줄링 정책, 우선순위, 선호도, 작업 부하에 따라 선택합니다. nice 값은 일반 시분할 정책의 입력 중 하나입니다.

## Nice 값 해석하기

관례적인 nice 범위는 `-20`부터 `19`입니다.

- 값이 낮으면 비교 가능한 작업보다 더 큰 스케줄링 가중치를 받습니다.
- 값이 높으면 상대 가중치를 덜 받아 더 “nice”해집니다.
- 기본값은 흔히 `0`입니다.

Niceness는 CPU 백분율을 예약하거나 즉시 실행을 보장하지 않습니다. 비교 가능한 실행 가능 작업이 CPU 시간을 놓고 경쟁할 때 효과가 가장 잘 보입니다. 실시간 정책, cgroups, CPU 선호도, 입출력 대기, 다른 제어가 관찰된 동작을 지배할 수 있습니다.

:::single-choice{#process-niceness-lower-value} 같은 일반 스케줄링 정책에서 상대적인 CPU 가중치가 더 큰 nice 값은 무엇인가요?

::option[`10`]{#process-niceness-value-ten explanation="양수 값은 더 nice하며 일반적으로 0이나 음수보다 가중치가 작습니다."}
::option[`19`]{#process-niceness-value-nineteen explanation="관례적인 범위에서 가장 nice한 끝이며 상대 가중치가 낮습니다."}
::option[`-5`]{#process-niceness-value-minus-five .correct explanation="낮은 nice 값은 비교 가능한 일반 작업 사이에서 더 큰 상대 가중치에 대응합니다."}
:::

## Niceness 확인하기

`top`에서 `NI` 열이 nice 값을 표시합니다. `ps`에서도 요청할 수 있습니다.

```bash
$ ps -o pid,ni,pri,stat,cmd -p 3245
```

`NI`는 사용자가 보는 nice 값입니다. `PRI`나 비슷한 열은 계산된 스케줄러 우선순위일 수 있고 척도가 도구와 스케줄링 클래스에 따라 다르므로 두 열을 서로 바꿔 쓸 수 있다고 가정하지 마세요.

:::single-choice{#process-niceness-top-column} 일반적으로 `top`에서 nice 값을 표시하는 열은 무엇인가요?

::option[`PID`]{#process-niceness-column-pid explanation="`PID`는 스케줄링 조정이 아니라 프로세스를 식별합니다."}
::option[`TTY`]{#process-niceness-column-tty explanation="`TTY`는 제어 터미널 연결을 식별합니다."}
::option[`NI`]{#process-niceness-column-ni .correct explanation="`NI`는 프로세스나 스레드의 nice 값을 나타내는 관례적인 약어입니다."}
:::

## nice로 명령 시작하기

`nice`로 조정된 값을 가진 새 명령을 시작합니다.

```bash
$ nice -n 5 long-computation
```

요청 조정값과 허용되는 구문은 로컬 매뉴얼에서 확인할 수 있습니다. 권한이 없는 사용자는 일반적으로 값을 높여 명령을 더 nice하게 만들 수 있습니다. nice 값을 낮춰 더 유리한 스케줄링 가중치를 주려면 적절한 권한이나 구성된 자원 제한이 필요합니다.

:::single-choice{#process-niceness-nice-command} `nice -n 5 long-computation`은 무엇을 하나요?

::option[허용되면 nice 값 5로 명령을 시작합니다.]{#process-niceness-start-five .correct explanation="`nice`는 요청한 스케줄링 조정값으로 새 명령을 시작합니다."}
::option[PID 5를 가능한 가장 낮은 nice 값으로 바꿉니다.]{#process-niceness-pid-five explanation="`-n` 뒤의 피연산자는 PID 대상이 아니라 nice 값입니다."}
::option[명령에 CPU 하나의 정확히 5%를 보장합니다.]{#process-niceness-five-percent explanation="Nice 값은 상대 가중치를 나타내며 고정 CPU 백분율을 예약하지 않습니다."}
:::

## renice로 기존 프로세스 변경하기

이미 실행 중인 프로세스에는 `renice`를 사용합니다.

```bash
$ renice -n 10 -p 3245
```

PID `3245`에 nice 값 `10`을 요청합니다. PID를 재사용할 수 있으므로 먼저 대상을 검증하고 결과 값을 확인하세요. 권한은 소유권, privilege, 자원 제한, 시스템 정책에 따라 달라집니다. 자신이 소유한 프로세스의 nice 값을 높이는 것은 보통 허용되지만 권한 없이 그 변경을 되돌리지 못할 수 있습니다.

:::single-choice{#process-niceness-renice-purpose} 기존 프로세스의 nice 값을 변경하는 도구는 무엇인가요?

::option[`nice`]{#process-niceness-tool-nice explanation="`nice`는 주로 조정된 값으로 새 명령을 시작합니다."}
::option[`kill`]{#process-niceness-tool-kill explanation="`kill`은 시그널을 보내며 일반 niceness 편집 도구가 아닙니다."}
::option[`renice`]{#process-niceness-tool-renice .correct explanation="`renice`는 옵션에 따라 기존 PID, 프로세스 그룹 또는 사용자를 대상으로 합니다."}
:::

[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864) 실습은 nice 값을 보고 변경할 수 있는 통제된 환경을 제공합니다. 유휴 시스템에서 눈에 띄는 차이를 기대하지 말고 경쟁하는 CPU 중심 작업을 비교하세요.

## 요약

이제 niceness를 CPU 보장으로 오해하지 않고 해석하고 조정할 수 있습니다.

1. 낮은 nice 값을 더 큰 상대 스케줄링 가중치로 읽을 수 있습니다.
2. `NI`를 계산된 우선순위 필드와 구분해 확인할 수 있습니다.
3. 명령을 시작할 때 `nice`를 사용할 수 있습니다.
4. 검증된 기존 프로세스에 `renice`를 사용할 수 있습니다.
