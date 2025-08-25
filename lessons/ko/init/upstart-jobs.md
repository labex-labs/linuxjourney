---
index: 4
lang: "ko"
title: "Upstart 작업"
meta_title: "Upstart 작업 - Init"
meta_description: "initctl 명령을 사용하여 Linux 에서 Upstart 작업을 관리하는 방법을 배웁니다. 작업 상태를 이해하고 서비스를 시작, 중지 및 재시작합니다. Linux 시스템 관리 기술을 향상시키세요."
meta_keywords: "Upstart 작업, initctl, Linux 서비스, 시스템 관리, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

Upstart 는 많은 이벤트와 작업을 트리거하여 실행할 수 있습니다. 안타깝게도 이벤트나 작업이 어디에서 시작되었는지 쉽게 확인할 수 있는 방법이 없으므로 `/etc/init`의 작업 구성을 살펴보아야 합니다. 대부분의 경우 Upstart 작업 구성 파일을 볼 필요는 없지만 특정 작업을 더 쉽게 제어하고 싶을 것입니다. Upstart 시스템에서 사용할 수 있는 유용한 명령이 많이 있습니다.

### 작업 보기

```plaintext
initctl list

shutdown stop/waiting
console stop/waiting
...
```

다양한 상태가 적용된 Upstart 작업 목록이 표시됩니다. 각 줄에서 작업 이름은 첫 번째 값이고, 두 번째 필드 (`/` 앞) 는 실제로 작업의 목표입니다. 세 번째 값 (`/` 뒤) 은 현재 상태입니다. 따라서 `shutdown` 작업은 결국 중지되기를 원하지만 현재 대기 상태에 있음을 알 수 있습니다. 작업을 시작하거나 중지하면 작업 상태와 목표가 변경됩니다.

### 특정 작업 보기

```plaintext
initctl status networking
networking start/running
```

Upstart 작업 구성 작성 방법에 대한 자세한 내용은 다루지 않겠지만, 이러한 구성에서 작업이 중지, 시작 및 재시작된다는 것을 이미 알고 있습니다. 이러한 작업은 또한 이벤트를 발생시켜 다른 작업을 시작할 수 있습니다. Upstart 작업의 수동 명령을 살펴보겠지만, 궁금하다면 `.conf` 파일을 더 자세히 살펴보아야 합니다.

### 수동으로 작업 시작

```bash
sudo initctl start networking
```

### 수동으로 작업 중지

```bash
sudo initctl stop networking
```

### 수동으로 작업 재시작

```bash
sudo initctl restart networking
```

### 수동으로 이벤트 발생

```bash
sudo initctl emit some_event
```

## Exercise

연습은 완벽을 만듭니다! Upstart 에 대한 특정 실습은 없지만, 작업을 예약하고 관리하는 방법을 이해하는 것은 시스템 프로세스를 제어하는 데 중요합니다. 다음은 작업 관리에 대한 이해를 강화하기 위한 실습입니다.

1. **[Linux 에서 at 및 cron 으로 작업 예약](https://labex.io/ko/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - Upstart 에서 처리하는 것과 같은 Linux 환경에서 서비스 및 작업이 관리되는 방식과 관련된 기본 개념인 일회성 및 반복 작업을 생성, 관리 및 제거하는 연습을 합니다.

이 실습은 실제 시나리오에서 작업 자동화 개념을 적용하고 시스템 작업 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`peanuts`라는 Upstart 작업을 수동으로 재시작하려면 어떻게 해야 합니까?

## Quiz Answer

sudo initctl restart peanuts
