---
index: 3
lang: "ko"
title: "Upstart 개요"
meta_title: "Upstart 개요 - Init"
meta_description: "Upstart, 이벤트 기반 모델, Linux 에서 서비스 관리 방법을 알아보세요. Upstart 작업 구성과 init 시스템으로서의 역할을 이해하세요."
meta_keywords: "Upstart, init 시스템, Linux 서비스, Ubuntu, SysV, 초보자 튜토리얼, Linux 가이드"
---

## Lesson Content

Upstart 는 Canonical 에서 개발되었으며, 한동안 Ubuntu 의 init 구현이었습니다. 하지만 최신 Ubuntu 설치에서는 이제 systemd 가 사용됩니다. Upstart 는 엄격한 시작 프로세스, 작업 차단 등 SysV 의 문제점을 개선하기 위해 만들어졌습니다. Upstart 의 이벤트 및 작업 기반 모델은 이벤트 발생 시 즉시 응답할 수 있도록 합니다.

Upstart 를 사용하고 있는지 확인하려면 `/usr/share/upstart` 디렉터리가 있는지 확인하면 됩니다. 이 디렉터리가 있다면 Upstart 를 사용하고 있을 가능성이 높습니다.

작업 (Jobs) 은 Upstart 가 수행하는 동작이며, 이벤트 (events) 는 다른 프로세스로부터 수신되어 작업을 트리거하는 메시지입니다. 작업 목록과 해당 구성을 보려면 다음을 참조하십시오:

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

이러한 작업 구성 파일 내부에는 작업을 시작하는 방법과 시기에 대한 정보가 있습니다.

예를 들어, `networking.conf` 파일에는 다음과 같이 간단하게 명시될 수 있습니다:

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

이는 런레벨 2, 3, 5 에서 네트워킹 설정을 시작하고 런레벨 0 에서 네트워킹을 중지한다는 의미입니다. 구성 파일을 작성하는 방법은 다양하며, 사용 가능한 다양한 작업 구성을 살펴보면 이를 알 수 있습니다.

Upstart 의 작동 방식은 다음과 같습니다:

1. 먼저 `/etc/init`에서 작업 구성을 로드합니다.
2. 시작 이벤트가 발생하면 해당 이벤트에 의해 트리거된 작업을 실행합니다.
3. 이 작업들은 새로운 이벤트를 생성하고, 이 이벤트들은 더 많은 작업을 트리거합니다.
4. Upstart 는 필요한 모든 작업을 완료할 때까지 이 과정을 계속합니다.

## Exercise

연습은 완벽을 만듭니다! Upstart 는 오래된 init 시스템이지만, 프로세스가 관리되고 작업이 예약되는 방식을 이해하는 것은 모든 Linux 관리자에게 중요합니다. 다음은 init 시스템이 작동하는 방식의 기초가 되는 프로세스 관리 및 작업 자동화에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 포그라운드 및 백그라운드 프로세스와 상호 작용하고, `ps`로 검사하고, `top`으로 리소스를 모니터링하고, `kill`로 종료하는 연습을 합니다. 이 실습은 Upstart 와 같은 init 시스템이 관리하는 프로세스의 수명 주기를 이해하는 데 도움이 됩니다.
2. **[Linux 에서 at 및 cron 으로 작업 예약](https://labex.io/ko/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - `at`으로 일회성 작업을 예약하고 `cron`으로 반복 작업을 예약하는 방법을 배웁니다. 이는 시스템 서비스에 대해 init 시스템이 제공하는 핵심 기능인 작업 자동화에 대한 실질적인 경험을 제공합니다.

이러한 실습은 특정 init 시스템에 관계없이 Linux 시스템을 관리하는 데 자신감을 키우면서 실제 시나리오에서 프로세스 제어 및 작업 자동화 개념을 적용하는 데 도움이 될 것입니다.

## Quiz Question

Ubuntu 에서 사용되는 init 구현은 무엇입니까?

## Quiz Answer

upstart
