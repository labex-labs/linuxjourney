---
index: 7
lang: "ko"
title: "kill (종료)"
meta_title: "kill (종료) - 프로세스"
meta_description: "Linux 'kill' 명령을 사용하여 프로세스를 종료하는 방법을 배웁니다. 프로세스 관리를 위한 SIGTERM, SIGKILL 및 기타 신호를 이해합니다. 지금 학습을 시작하세요!"
meta_keywords: "kill 명령, Linux 프로세스, SIGTERM, SIGKILL, Linux 튜토리얼, 초보자, 프로세스 관리, Linux 가이드"
---

## Lesson Content

프로세스를 종료하는 신호를 보낼 수 있습니다. 이러한 명령은 적절하게 `kill` 명령이라고 불립니다.

```bash
kill 12445
```

`12445`는 종료하려는 프로세스의 PID 입니다. 기본적으로 `TERM` 신호를 보냅니다. `SIGTERM` 신호는 프로세스에 종료를 요청하기 위해 전송되며, 프로세스가 리소스를 깔끔하게 해제하고 상태를 저장할 수 있도록 합니다.

`kill` 명령으로 신호를 지정할 수도 있습니다:

```bash
kill -9 12445
```

이것은 `SIGKILL` 신호를 실행하고 프로세스를 종료합니다.

### SIGHUP, SIGINT, SIGTERM, SIGKILL, SIGSTOP 의 차이점은 무엇입니까?

이 신호들은 모두 상당히 비슷하게 들리지만, 차이점이 있습니다.

- SIGHUP - Hangup(끊김), 제어 터미널이 닫힐 때 프로세스에 전송됩니다. 예를 들어, 프로세스가 실행 중인 터미널 창을 닫으면 `SIGHUP` 신호를 받게 됩니다. 기본적으로 연결이 끊긴 것입니다.
- SIGINT - 인터럽트 신호이므로 Ctrl-C 를 사용할 수 있으며, 시스템은 프로세스를 정상적으로 종료하려고 시도합니다.
- SIGTERM - 프로세스를 종료하지만, 먼저 일부 정리를 수행하도록 허용합니다.
- SIGKILL - 프로세스를 종료합니다. 불로 죽이는 것처럼, 어떤 정리도 하지 않습니다.
- SIGSTOP - 프로세스를 중지/일시 중단합니다.

## Exercise

연습하면 완벽해집니다! 다음은 프로세스 관리 및 종료에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 이 랩에서는 Linux 시스템에서 프로세스를 관리하고 모니터링하는 데 필요한 필수 기술을 배웁니다. 포그라운드 및 백그라운드 프로세스와 상호 작용하는 방법, `ps`로 검사하는 방법, `top`으로 리소스를 모니터링하는 방법, `renice`로 우선순위를 조정하는 방법, `kill`로 종료하는 방법을 탐색합니다.

이 랩은 실제 시나리오에서 프로세스 제어 및 종료 개념을 적용하고 Linux 프로세스 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

기본 `kill` 명령의 신호 이름은 무엇입니까?

## Quiz Answer

SIGTERM
