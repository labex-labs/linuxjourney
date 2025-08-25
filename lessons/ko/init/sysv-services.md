---
index: 2
lang: "ko"
title: "System V 서비스"
meta_title: "System V 서비스 - Init"
meta_description: "명령줄 도구를 사용하여 System V 서비스를 관리하는 방법을 배웁니다. 이 초보자용 Linux 튜토리얼을 통해 서비스를 나열, 시작, 중지 및 재시작하는 방법을 알아보세요."
meta_keywords: "System V 서비스, Linux 서비스, service 명령, SysV init, Linux 튜토리얼, 초보자 Linux, 서비스 관리, Linux 가이드"
---

## Lesson Content

Sys V 서비스를 관리하는 데 사용할 수 있는 많은 명령줄 도구가 있습니다.

### 서비스 나열

```bash
service --status-all
```

### 서비스 시작

```bash
sudo service networking start
```

### 서비스 중지

```bash
sudo service networking stop
```

### 서비스 재시작

```bash
sudo service networking restart
```

이러한 명령은 Sys V init 시스템에만 국한되지 않습니다. Upstart 서비스도 관리하는 데 사용할 수 있습니다. Linux 는 기존의 Sys V init 스크립트에서 벗어나려고 노력하고 있지만, 이러한 전환을 돕기 위한 기능들이 여전히 존재합니다.

## Exercise

연습하면 완벽해집니다! 다음은 Linux 에서 서비스를 관리하는 데 필수적인 프로세스 및 작업 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 실제 Linux 환경에서 프로세스와 상호 작용하고, 검사하고, 모니터링하고, 종료하는 연습을 합니다.
2. **[Linux 에서 at 및 cron 으로 작업 예약](https://labex.io/ko/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 일회성 작업을 위한 `at`과 반복 작업을 위한 `cron`을 사용하여 작업을 자동화하는 방법을 배웁니다. 이는 서비스 자동화를 위한 핵심 기술입니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 시스템 운영 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

Sys V 를 사용하여 `peanut`이라는 서비스를 중지하는 명령은 무엇입니까?

## Quiz Answer

sudo service peanut stop
