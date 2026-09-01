---
lesson_id: "process-signals"
course_id: "processes"
lang: "ko"
order_index: 6
title: "시그널"
description: "Linux가 프로세스 제어와 이벤트 알림을 위해 시그널을 생성하고 차단하고 전달하고 처리하는 방법을 배웁니다."
meta_title: "시그널 - Processes"
meta_description: "프로세스 관리의 핵심 메커니즘인 Linux 시그널의 기초를 알아봅니다. SIGTERM, SIGKILL, SIGINT 같은 Linux 프로세스 시그널의 작동 방식을 배웁니다."
meta_keywords: "linux 시그널, linux 프로세스 시그널, signal 15 linux, os sig 코드, SIGKILL, SIGTERM, SIGINT, 프로세스 관리, linux 튜토리얼"
---

시그널은 프로세스나 특정 스레드에 전달되는 비동기 알림입니다. 이벤트를 보고하고 동작을 요청하지만 데이터 중심 프로세스 간 통신 메커니즘과 비교해 전달하는 정보는 제한적입니다.

## 시그널이 오는 곳

시그널은 여러 곳에서 시작될 수 있습니다.

- 터미널이 `Ctrl-C`에 `SIGINT`, `Ctrl-Z`에 `SIGTSTP`를 생성하여 포그라운드 프로세스 그룹에 보낼 수 있습니다.
- 스레드가 잘못된 메모리 참조를 만들면 커널이 `SIGSEGV` 같은 동기 시그널을 생성할 수 있습니다.
- 프로세스가 권한을 가진 다른 프로세스나 프로세스 그룹에 시그널을 보낼 수 있습니다.
- 타이머, 자식 상태 변경, 터미널 hangup이 다른 시그널을 생성할 수 있습니다.

송신자는 일반적으로 자격 증명이나 capabilities를 기준으로 한 적절한 권한이 있어야 합니다. 따라서 시그널은 임의 사용자 사이의 제한 없는 메시지가 아니라 커널이 중개하는 제어 인터페이스입니다.

:::single-choice{#process-signals-ctrl-c} 터미널은 일반적으로 `Ctrl-C`에 어떤 시그널을 생성하나요?

::option[`SIGTSTP`]{#process-signals-ctrl-c-tstp explanation="`SIGTSTP`는 일반적으로 `Ctrl-Z` 같은 터미널 일시 중단 문자와 연결됩니다."}
::option[`SIGCONT`]{#process-signals-ctrl-c-cont explanation="`SIGCONT`는 키보드 인터럽트를 나타내지 않고 정지된 프로세스를 재개합니다."}
::option[`SIGINT`]{#process-signals-ctrl-c-int .correct explanation="터미널 인터럽트 문자는 일반적으로 포그라운드 프로세스 그룹에 `SIGINT`를 생성합니다."}
:::

## 처리 방식과 기본 동작

대부분의 시그널에는 다음 세 응답 중 하나를 선택하는 프로세스 전체 처리 방식이 있습니다.

- 시그널에 정의된 기본 동작 수행
- 시그널 무시
- 사용자가 설치한 핸들러 호출

기본 동작은 서로 다릅니다. 시그널은 종료, 코어 덤프를 만들며 종료, 정지, 계속 또는 무시될 수 있습니다. `SIGTERM`을 잡으면 프로그램이 질서 있는 종료를 시작할 수 있지만 핸들러는 엄격한 비동기 시그널 안전 규칙을 따라야 하며 프로그램은 여전히 종료를 늦추거나 거부할 수 있습니다.

시그널 이름은 숫자보다 이식 가능하고 읽기 쉽습니다. 일반적인 Linux 아키텍처가 `SIGTERM`에 15를 사용하지만 관련 표준이 보장하지 않는 모든 시그널 번호가 어디서나 같다고 가정하지 마세요. `kill -l`로 로컬 매핑을 확인합니다.

:::single-choice{#process-signals-term-behavior} 프로세스가 `SIGTERM`에 정상적인 방식으로 응답할 수 있는 이유는 무엇인가요?

::option[해당 시그널에 핸들러를 설치할 수 있습니다.]{#process-signals-term-handler .correct explanation="`SIGKILL`과 달리 `SIGTERM`은 잡을 수 있어 프로그램이 자체 종료 로직을 시작할 수 있습니다."}
::option[커널이 열린 모든 문서를 항상 자동으로 저장합니다.]{#process-signals-term-kernel-save explanation="애플리케이션 정리는 프로그램 코드에 달려 있으며 커널은 임의 문서 상태를 이해하고 저장하지 않습니다."}
::option[`SIGTERM`은 기본적으로 종료를 일으킬 수 없습니다.]{#process-signals-term-no-default explanation="프로세스가 처리 방식을 바꾸지 않았다면 기본 동작은 종료입니다."}
:::

## 차단된 시그널과 대기 중 시그널

스레드에는 선택한 시그널 전달을 일시적으로 막을 수 있는 시그널 마스크가 있습니다. 생성된 차단 시그널은 표준 및 실시간 시그널 규칙에 따라 전달할 수 있을 때까지 대기 상태로 남습니다. 같은 종류의 표준 시그널은 발생할 때마다 큐에 쌓이지 않고 하나로 합쳐질 수 있습니다.

멀티스레드 프로세스에서 프로세스 대상 시그널은 차단하지 않은 적합한 스레드에 전달될 수 있고 스레드 대상 시그널은 지정된 스레드로 갑니다. 올바른 시그널 설계에는 “프로세스가 차단했는지”만 확인하는 것보다 더 많은 고려가 필요합니다.

:::single-choice{#process-signals-blocked-state} 차단 가능한 시그널이 대상에서 차단된 상태로 생성되면 일반적으로 어떻게 되나요?

::option[전달할 수 있을 때까지 대기 상태로 남습니다.]{#process-signals-pending .correct explanation="차단은 처리를 미루며 시그널을 차단 해제한 뒤 대기 시그널을 전달할 수 있습니다."}
::option[자동으로 `SIGKILL`로 변환됩니다.]{#process-signals-convert-kill explanation="커널은 일반 차단 시그널을 잡을 수 없는 시그널로 승격하지 않습니다."}
::option[대상 프로세스의 사용자 ID를 바꿉니다.]{#process-signals-change-uid explanation="시그널 마스크는 전달에 영향을 주며 프로세스 자격 증명을 바꾸지 않습니다."}
:::

## 처리할 수 없는 시그널

`SIGKILL`은 프로세스를 종료하고 `SIGSTOP`은 정지시킵니다. 두 시그널 모두 잡거나 무시하거나 차단할 수 없습니다. 커널이 최종 제어를 유지하도록 보장하지만 `SIGKILL`에는 애플리케이션 수준 정리 기회가 없습니다.

`SIGKILL`조차 관찰자 입장에서 작업을 즉시 사라지게 하지 못할 수 있습니다. 작업이 중단할 수 없는 커널 작업을 기다릴 수 있고 종료 후에도 부모가 상태를 수거해야 합니다.

:::single-choice{#process-signals-uncatchable-pair} 잡거나 무시하거나 차단할 수 없는 시그널 쌍은 무엇인가요?

::option[`SIGKILL`과 `SIGSTOP`]{#process-signals-kill-stop .correct explanation="커널은 프로세스가 기본 동작을 무시하거나 미루지 못하도록 이 두 시그널을 예약합니다."}
::option[`SIGINT`와 `SIGTERM`]{#process-signals-int-term explanation="둘 다 사용자 설치 핸들러를 가질 수 있고 차단할 수 있습니다."}
::option[`SIGHUP`과 `SIGCONT`]{#process-signals-hup-cont explanation="특수한 의미가 있지만 잡을 수 없는 시그널 쌍은 아닙니다."}
:::

## 요약

이제 Linux 시그널 처리의 주요 단계와 제약을 설명할 수 있습니다.

1. 터미널, 커널, 프로세스가 생성한 시그널을 식별할 수 있습니다.
2. 기본 동작, 무시된 시그널, 핸들러를 구분할 수 있습니다.
3. 차단을 대기 전달 및 스레드 마스크와 연결할 수 있습니다.
4. `SIGKILL`과 `SIGSTOP`을 처리하거나 차단할 수 없음을 기억할 수 있습니다.
