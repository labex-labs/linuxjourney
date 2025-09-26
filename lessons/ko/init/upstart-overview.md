---
index: 3
lang: "ko"
title: "Upstart 개요"
meta_title: "Upstart 개요 - Init"
meta_description: "Upstart, 이벤트 기반 모델 및 Linux 에서 서비스를 관리하는 방법을 알아봅니다. Upstart 작업 구성과 init 시스템으로서의 역할을 이해합니다."
meta_keywords: "Upstart, init 시스템, Linux 서비스, Ubuntu, SysV, 초보자 튜토리얼, Linux 가이드"
---

## Lesson Content

Upstart 는 Canonical 에서 개발했기 때문에 한동안 Ubuntu 의 init 구현이었지만, 최신 Ubuntu 설치에서는 현재 systemd 가 사용됩니다. Upstart 는 엄격한 시작 프로세스, 작업 차단 등 SysV 의 문제점을 개선하기 위해 만들어졌습니다. Upstart 의 이벤트 및 작업 기반 모델을 통해 이벤트가 발생하는 즉시 응답할 수 있습니다.

Upstart 를 사용하고 있는지 확인하려면 `/usr/share/upstart` 디렉터리가 있는지 확인하는 것이 좋은 지표입니다.

Job 은 Upstart 가 수행하는 작업이며, Event 는 Job 을 트리거하기 위해 다른 프로세스로부터 수신되는 메시지입니다. Job 목록과 해당 구성을 보려면 다음을 확인하십시오.

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

이러한 Job 구성 내부에서 Job 을 시작하는 방법과 시기에 대한 정보를 찾을 수 있습니다.

예를 들어, `networking.conf` 파일에는 다음과 같이 간단하게 작성될 수 있습니다.

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

이는 runlevel 2, 3 또는 5 에서 네트워킹 설정을 시작하고 runlevel 0 에서 네트워킹을 중지함을 의미합니다. 구성 파일을 작성하는 방법에는 여러 가지가 있으며, 사용 가능한 다양한 Job 구성을 살펴보면 이를 알 수 있습니다.

Upstart 가 작동하는 방식은 다음과 같습니다.

1. 먼저 `/etc/init`에서 Job 구성을 로드합니다.
2. 시작 이벤트가 발생하면 해당 이벤트로 트리거된 Job 을 실행합니다.
3. 이러한 Job 은 새로운 이벤트를 생성하고, 그러면 해당 이벤트가 더 많은 Job 을 트리거합니다.
4. Upstart 는 필요한 모든 Job 을 완료할 때까지 이 작업을 계속합니다.

## Exercise

연습이 완벽을 만듭니다! Upstart 는 이전 init 시스템이지만, 프로세스가 관리되고 작업이 예약되는 방식을 이해하는 것은 모든 Linux 관리자에게 중요합니다. init 시스템이 작동하는 방식의 기초가 되는 프로세스 관리 및 작업 자동화에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Manage and Monitor Linux Processes](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 포그라운드 및 백그라운드 프로세스와 상호 작용하고, `ps`로 검사하고, `top`으로 리소스를 모니터링하고, `kill`로 종료하는 연습을 합니다. 이 랩은 Upstart 와 같은 init 시스템이 관리하는 프로세스 수명 주기를 이해하는 데 도움이 됩니다.
2. **[Schedule Tasks with at and cron in Linux](https://labex.io/ko/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - `at`을 사용하여 일회성 작업을 예약하고 `cron`을 사용하여 반복 작업을 예약하는 방법을 배웁니다. 이는 init 시스템이 시스템 서비스를 위해 촉진하는 작업 자동화의 핵심 기능에 대한 실질적인 경험을 제공합니다.

이러한 랩은 실제 시나리오에서 프로세스 제어 및 작업 자동화 개념을 적용하는 데 도움이 되며, 사용 중인 특정 init 시스템에 관계없이 Linux 시스템을 관리하는 데 자신감을 심어줄 것입니다.

## Quiz Question

Ubuntu 에서 사용되는 init 구현은 무엇입니까?

## Quiz Answer

systemd
