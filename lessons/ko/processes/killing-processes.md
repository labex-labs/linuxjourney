---
title: "kill (종료)"
description: "Linux 'kill' 명령어를 사용하여 프로세스를 종료하는 방법을 배웁니다. 프로세스 관리를 위한 SIGTERM, SIGKILL 및 기타 신호를 이해합니다. 지금 학습을 시작하세요!"
keywords: "kill 명령어, Linux 프로세스, SIGTERM, SIGKILL, Linux 튜토리얼, 초보자, 프로세스 관리, Linux 가이드"
---

## Lesson Content

프로세스를 종료하는 신호를 보낼 수 있습니다. 이러한 명령어는 적절하게 `kill` 명령어라고 불립니다.

```bash
kill 12445
```

`12445`는 종료하려는 프로세스의 PID 입니다. 기본적으로 `TERM` 신호를 보냅니다. `SIGTERM` 신호는 프로세스에 종료를 요청하여 리소스를 깔끔하게 해제하고 상태를 저장할 수 있도록 합니다.

`kill` 명령어로 신호를 지정할 수도 있습니다:

```bash
kill -9 12445
```

이것은 `SIGKILL` 신호를 실행하고 프로세스를 종료합니다.

### SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP 의 차이점은 무엇인가요?

이 신호들은 모두 상당히 비슷하게 들리지만, 차이점이 있습니다.

- SIGHUP - Hangup(끊김), 제어 터미널이 닫힐 때 프로세스에 전송됩니다. 예를 들어, 프로세스가 실행 중인 터미널 창을 닫으면 `SIGHUP` 신호를 받게 됩니다. 즉, 연결이 끊긴 것입니다.
- SIGINT - 인터럽트 신호이므로 Ctrl-C 를 사용할 수 있으며, 시스템은 프로세스를 정상적으로 종료하려고 시도합니다.
- SIGTERM - 프로세스를 종료하지만, 먼저 일부 정리를 수행하도록 허용합니다.
- SIGKILL - 프로세스를 종료합니다. 즉시 종료하며, 어떤 정리 작업도 수행하지 않습니다.
- SIGSTOP - 프로세스를 중지/일시 중단합니다.

## Exercise

다른 신호를 사용하여 일부 프로세스를 종료합니다.

## Quiz Question

기본 `kill` 명령어의 신호 이름은 무엇입니까?

## Quiz Answer

SIGTERM
