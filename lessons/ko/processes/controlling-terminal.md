---
lesson_id: "controlling-terminal"
course_id: "processes"
lang: "ko"
order_index: 2
title: "제어 터미널"
description: "제어 터미널이 세션을 대화형 입력, 시그널, 쉘 작업 제어와 연결하는 방법을 배웁니다."
meta_title: "제어 터미널 - Processes"
meta_description: "Linux 제어 터미널 개념을 알아봅니다. TTY와 PTS의 차이 및 ps TTY 출력으로 데몬처럼 제어 터미널이 없는 프로세스를 식별하는 방법을 배웁니다."
meta_keywords: "제어 터미널, ps tty, tty란, ps 사용법, TTY, PTS, Linux 터미널, 데몬 프로세스, Linux 프로세스"
---

대화형 로그인 세션에는 제어 터미널이 있을 수 있습니다. 제어 터미널은 세션과 연결된 터미널 장치로 커널이 터미널 생성 시그널과 작업 제어에 사용합니다. 프로세스 목록의 `TTY` 필드는 이 연결을 식별하는 데 도움이 됩니다.

## 터미널과 의사 터미널 장치

TTY라는 이름은 역사적인 전신 타자기에서 왔습니다. 현대 Linux에서 터미널 인터페이스는 반드시 물리 장비가 아니라 장치 추상화입니다.

시스템 가상 콘솔은 `tty1` 같은 이름으로 나타날 수 있습니다. 콘솔 전환을 위한 데스크톱 단축키 할당은 배포판마다 다르므로 가정하면 안 됩니다. 터미널 에뮬레이터, 원격 로그인, 멀티플렉서는 일반적으로 의사 터미널 쌍을 사용하며 대화형 측은 `pts/3` 같은 이름으로 표시됩니다.

현재 명령의 표준 입력에 연결된 터미널을 표시합니다.

```bash
$ tty
/dev/pts/3
```

이 결과는 더 넓은 제어 터미널 개념과 관련 있지만 완전히 같지는 않습니다. 프로세스는 제어 터미널이 있는 세션에 남으면서 표준 입력이나 출력을 리디렉션할 수 있습니다.

:::single-choice{#controlling-terminal-pts-meaning} `pts/3` 같은 이름은 일반적으로 무엇을 식별하나요?

::option[세 번째 쉘에 할당된 프로세스 ID]{#controlling-terminal-pts-pid explanation="PID는 숫자 프로세스 메타데이터이며 `pts/N` 장치 이름으로 표현되지 않습니다."}
::option[대화형 세션이 사용하는 의사 터미널 장치]{#controlling-terminal-pts-device .correct explanation="`/dev/pts` 아래 항목은 터미널 에뮬레이터와 원격 세션에서 흔히 사용하는 의사 터미널 슬레이브 장치입니다."}
::option[터미널 프로그램이 들어 있는 파일 시스템 파티션]{#controlling-terminal-pts-partition explanation="이름은 저장소 파티션이 아니라 터미널 장치 인터페이스를 식별합니다."}
:::

## 세션, 프로세스 그룹, 작업 제어

제어 터미널은 창을 연 특정 명령 하나가 아니라 세션에 속합니다. 세션 안에서 터미널은 포그라운드 프로세스 그룹을 추적합니다. 쉘은 포그라운드 파이프라인을 그 그룹에 넣어 입력을 읽고 터미널 생성 시그널을 받게 합니다.

예를 들어 `Ctrl-C`를 누르면 일반적으로 터미널 드라이버가 포그라운드 프로세스 그룹에 `SIGINT`를 보냅니다. 백그라운드 그룹이 터미널에서 읽으려 하면 `SIGTTIN`을 받을 수 있습니다. 이런 규칙으로 쉘은 포그라운드 및 백그라운드 작업을 조정합니다.

:::single-choice{#controlling-terminal-ctrl-c-target} 터미널은 일반적으로 `Ctrl-C`가 생성한 시그널을 어떤 프로세스에 보내나요?

::option[현재 사용자가 소유한 모든 프로세스]{#controlling-terminal-ctrl-c-user explanation="터미널 생성 시그널은 사용자의 모든 프로세스가 아니라 포그라운드 프로세스 그룹으로 제한됩니다."}
::option[포그라운드 작업과 관계없이 로그인 쉘만]{#controlling-terminal-ctrl-c-shell explanation="다른 작업이 포그라운드에 있으면 해당 작업 그룹이 일반적인 시그널 대상입니다."}
::option[터미널의 포그라운드 프로세스 그룹]{#controlling-terminal-ctrl-c-foreground .correct explanation="터미널 드라이버는 현재 포그라운드 프로세스 그룹에 `SIGINT`를 보냅니다."}
:::

## TTY 열 읽기

안정적인 보기가 필요하면 선택한 프로세스 필드를 명시적으로 요청합니다.

```bash
$ ps -o pid,tty,stat,cmd
```

`pts/3` 같은 터미널 이름은 해당 프로세스에 기록된 제어 터미널을 식별합니다. 물음표(`?`)는 일반적으로 프로세스에 제어 터미널이 없다는 뜻입니다.

서비스 관리자가 대화형 로그인 세션과 독립적으로 시작하므로 많은 서비스 프로세스에는 제어 터미널이 없습니다. 하지만 TTY가 없다는 사실만으로 프로세스가 데몬임을 증명하지 못하고 백그라운드 쉘 작업에도 제어 터미널이 있을 수 있습니다.

:::single-choice{#controlling-terminal-question-mark} `ps`의 `TTY` 열에 있는 `?`는 일반적으로 무엇을 뜻하나요?

::option[프로세스에 제어 터미널이 없습니다.]{#controlling-terminal-no-tty .correct explanation="물음표는 프로세스와 연결된 제어 터미널이 없을 때 사용하는 일반적인 표시입니다."}
::option[터미널이 바빠서 프로세스가 읽지 못했습니다.]{#controlling-terminal-busy-tty explanation="이 표시는 일시적인 장치 경합이 아니라 제어 터미널 부재를 나타냅니다."}
::option[프로세스는 항상 커널 스레드입니다.]{#controlling-terminal-kernel-only explanation="커널 스레드에는 흔히 터미널이 없지만 많은 사용자 공간 서비스도 마찬가지입니다."}
:::

## 터미널 종료와 Hangup

터미널 연결이 사라지면 커널이나 터미널/세션 소프트웨어가 연결된 프로세스에 `SIGHUP`을 보낼 수 있습니다. 프로세스는 종료하거나 시그널을 처리하거나 무시하거나 이미 시그널 이후에도 살아남도록 설정되어 있을 수 있습니다. `disown` 같은 쉘 기능, `nohup` 같은 유틸리티, 멀티플렉서, 서비스 관리자는 모두 수명 주기 동작에 영향을 줍니다.

따라서 터미널을 닫는다고 그곳에서 시작한 모든 명령이 종료된다고 보장할 수 없습니다. 지속성이 중요하면 프로세스 세션, 시그널 처리, 리디렉션, 감독자를 확인하세요.

:::single-choice{#controlling-terminal-close-effect} 터미널을 닫으면 그곳에서 시작한 모든 프로세스가 항상 종료된다고 말할 수 없는 이유는 무엇인가요?

::option[Linux 터미널은 닫힐 때 어떤 시그널도 생성하지 않습니다.]{#controlling-terminal-never-signals explanation="Hangup 시그널은 실제 터미널 및 세션 동작이지만 그 결과가 반드시 종료인 것은 아닙니다."}
::option[숫자 PID가 있는 프로세스만 hangup을 받을 수 있습니다.]{#controlling-terminal-pid-hangup explanation="모든 일반 프로세스에는 숫자 PID가 있으며 이 사실은 터미널 종료 후 생존 여부를 결정하지 않습니다."}
::option[프로세스가 hangup을 처리하거나 피하고 독립적으로 관리될 수 있습니다.]{#controlling-terminal-hangup-handling .correct explanation="시그널 처리 방식, 쉘 동작, 멀티플렉서, 감독자가 터미널 종료 후에도 프로세스를 계속 실행하게 할 수 있습니다."}
:::

[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864) 실습은 포그라운드 작업, 백그라운드 작업 및 `TTY` 필드를 비교할 수 있는 안전한 환경을 제공합니다.

## 요약

이제 제어 터미널을 대화형 프로세스 관리와 연결할 수 있습니다.

1. 가상 터미널과 의사 터미널을 구분할 수 있습니다.
2. 터미널 시그널을 포그라운드 프로세스 그룹과 연결할 수 있습니다.
3. `ps` 출력의 터미널 이름과 `?`를 해석할 수 있습니다.
4. 터미널 종료를 보장된 프로세스 종료가 아니라 시그널 전달로 다룰 수 있습니다.
