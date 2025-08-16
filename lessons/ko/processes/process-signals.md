---
lang: "ko"
title: "시그널"
description: "Linux 시그널, 그 목적, SIGINT 및 SIGKILL 과 같은 일반적인 유형, 그리고 프로세스가 이를 처리하는 방법에 대해 알아보세요. 더 나은 Linux 제어를 위해 시그널의 기본 사항을 이해하세요."
keywords: "Linux 시그널, SIGKILL, SIGINT, 프로세스 통신, Linux 튜토리얼, Linux 초보자, Linux 가이드"
---

## Lesson Content

시그널은 어떤 일이 발생했음을 프로세스에 알리는 알림입니다.

### Why We Have Signals

시그널은 소프트웨어 인터럽트이며 다양한 용도로 사용됩니다:

- 사용자는 특수 터미널 문자 (Ctrl-C) 또는 (Ctrl-Z) 중 하나를 입력하여 프로세스를 종료, 인터럽트 또는 일시 중단할 수 있습니다.
- 하드웨어 문제가 발생할 수 있으며, 커널은 프로세스에 이를 알리기를 원합니다.
- 소프트웨어 문제가 발생할 수 있으며, 커널은 프로세스에 이를 알리기를 원합니다.
- 기본적으로 프로세스가 통신할 수 있는 방법입니다.

### Signal Process

어떤 이벤트에 의해 시그널이 생성되면, 해당 시그널은 프로세스에 전달됩니다. 전달되기 전까지는 보류 (pending) 상태로 간주됩니다. 프로세스가 실행될 때 시그널이 전달됩니다. 그러나 프로세스는 시그널 마스크를 가지고 있으며, 지정된 경우 시그널 전달을 차단하도록 설정할 수 있습니다. 시그널이 전달될 때 프로세스는 여러 가지 작업을 수행할 수 있습니다:

- 시그널을 무시합니다.
- 시그널을 "잡아서" 특정 핸들러 루틴을 수행합니다.
- 일반적인 exit 시스템 호출과 달리 프로세스가 종료될 수 있습니다.
- 시그널 마스크에 따라 시그널을 차단합니다.

### Common Signals

각 시그널은 SIGxxx 형태의 심볼릭 이름을 가진 정수로 정의됩니다. 가장 일반적인 시그널 중 일부는 다음과 같습니다:

- SIGHUP or HUP or 1: Hangup
- SIGINT or INT or 2: Interrupt
- SIGKILL or KILL or 9: Kill
- SIGSEGV or SEGV or 11: Segmentation fault
- SIGTERM or TERM or 15: Software termination
- SIGSTOP or STOP: Stop

시그널에 따라 숫자가 다를 수 있으므로, 일반적으로 이름으로 참조됩니다.

일부 시그널은 차단할 수 없습니다. 한 가지 예는 SIGKILL 시그널입니다. KILL 시그널은 프로세스를 파괴합니다.

## Exercise

No exercises for this lesson.

## Quiz Question

차단할 수 없는 시그널은 무엇입니까?

## Quiz Answer

SIGKILL
