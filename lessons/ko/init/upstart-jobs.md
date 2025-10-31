---
index: 4
lang: "ko"
title: "Upstart 작업"
meta_title: "Upstart 작업 - Init"
meta_description: "Linux 환경에서 Upstart 작업을 사용하여 서비스를 관리하는 가이드입니다. initctl 유틸리티를 사용하여 upstart 리눅스 시스템에서 작업을 나열, 시작, 중지 및 다시 시작하는 방법을 배웁니다."
meta_keywords: "Upstart 작업, initctl, upstart 리눅스, 리눅스 서비스, 시스템 관리, init 시스템, 리눅스 튜토리얼"
---

## Lesson Content

Upstart 는 부팅 중 및 시스템 실행 중에 서비스와 작업을 관리하기 위해 일부 **upstart linux** 배포판에서 사용되는 이벤트 기반 init 시스템입니다. 이는 작업 (jobs) 과 이벤트 (events) 시스템을 통해 작동합니다. 모든 이벤트의 출처를 추적하는 것은 복잡할 수 있으며, 종종 `/etc/init`에서 작업 구성을 탐색해야 하지만, 명령줄에서 이러한 작업을 직접 관리해야 하는 경우가 더 일반적입니다. `initctl` 유틸리티는 이 목적을 위한 일련의 명령을 제공합니다.

### 작업 상태 보기

알려진 모든 Upstart 작업과 현재 상태 목록을 보려면 `list` 명령을 사용합니다.

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

출력은 작업 이름, 목표 (goal) 및 현재 상태를 표시합니다. 예시 `shutdown stop/waiting`에서 작업 이름은 `shutdown`이고, 목표는 `stop`이며, 현재 상태는 `waiting`입니다. 작업 상태와 목표는 상호 작용함에 따라 변경됩니다.

특정 작업의 상태를 확인하려면 `status` 명령을 사용합니다.

```plaintext
initctl status networking
networking start/running
```

### 수동으로 작업 제어하기

`/etc/init`의 작업 구성 파일은 작업이 시작, 중지 및 이벤트와 상호 작용하는 방식을 정의하지만, `initctl`을 사용하여 이러한 작업을 수동으로 재정의할 수 있습니다. 이는 문제 해결이나 관리 작업을 수행할 때 유용합니다.

작업을 수동으로 시작하려면:

```bash
sudo initctl start networking
```

작업을 수동으로 중지하려면:

```bash
sudo initctl stop networking
```

작업을 수동으로 다시 시작하려면 (작업을 중지한 다음 시작하는 편리한 단축키):

```bash
sudo initctl restart networking
```

### 사용자 지정 이벤트 방출하기

Upstart 작업은 이벤트에 의해 트리거됩니다. 또한 수동으로 이벤트를 "방출 (emit)"할 수 있으며, 이는 사용자 지정 작업을 트리거하거나 테스트 목적으로 유용할 수 있습니다. `some_event`에서 시작하도록 구성된 모든 작업은 다음 명령으로 트리거됩니다.

```bash
sudo initctl emit some_event
```

## Exercise

연습이 완벽을 만듭니다! Upstart 에 대한 특정 실습은 없지만, 작업 예약 및 관리를 이해하는 것은 시스템 프로세스를 제어하는 데 중요합니다. 작업 관리 이해도를 높이기 위한 실습 랩은 다음과 같습니다.

1. **[Linux 에서 at 및 cron 으로 작업 예약하기](https://labex.io/ko/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 일회성 및 반복 작업을 생성, 관리 및 제거하는 연습은 Upstart 가 처리하는 것과 같은 Linux 환경에서 서비스 및 작업이 관리되는 방식과 관련된 기본 개념입니다.

이 랩은 실제 시나리오에서 작업 자동화 개념을 적용하고 시스템 운영 관리에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

이름이 `peanuts`인 Upstart 작업을 수동으로 다시 시작하려면 어떻게 해야 합니까? 전체 명령을 제공하십시오. (참고: 답변은 대소문자를 구분하며 영어로 제공되어야 합니다.)

## Quiz Answer

sudo initctl restart peanuts
