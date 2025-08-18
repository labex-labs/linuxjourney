---
lang: "ko"
title: "Upstart 개요"
meta_description: "Upstart, 이벤트 기반 모델, 그리고 Linux 에서 서비스를 관리하는 방법에 대해 알아보세요. Upstart 작업 구성과 init 시스템으로서의 역할을 이해합니다."
meta_keywords: "Upstart, init 시스템, Linux 서비스, Ubuntu, SysV, 초보자 튜토리얼, Linux 가이드"
---

## Lesson Content

Upstart 는 Canonical 에서 개발되었으며, 한동안 Ubuntu 의 init 구현체였습니다. 하지만 최신 Ubuntu 설치에서는 이제 systemd 가 사용됩니다. Upstart 는 엄격한 시작 프로세스, 작업 차단 등 SysV 의 문제점을 개선하기 위해 만들어졌습니다. Upstart 의 이벤트 및 작업 기반 모델은 이벤트 발생 시 즉시 응답할 수 있도록 합니다.

Upstart 를 사용하고 있는지 확인하려면 `/usr/share/upstart` 디렉터리가 있는지 확인하는 것이 좋은 지표입니다.

작업 (Jobs) 은 Upstart 가 수행하는 동작이며, 이벤트 (events) 는 다른 프로세스로부터 수신되어 작업을 트리거하는 메시지입니다. 작업 목록과 해당 구성을 보려면 다음을 참조하십시오:

```plaintext
pete@icebox:~$ ls /etc/init
acpid.conf                   mountnfs.sh.conf
alsa-restore.conf            mtab.sh.conf
alsa-state.conf              networking.conf
alsa-store.conf              network-interface.conf
anacron.conf                 network-interface-container.conf
```

이러한 작업 구성 내부에는 작업을 시작하는 방법과 시기에 대한 정보가 있습니다.

예를 들어, `networking.conf` 파일에는 다음과 같이 간단하게 작성될 수 있습니다:

```plaintext
start on runlevel [235]
stop on runlevel [0]
```

이는 runlevel 2, 3, 또는 5 에서 네트워킹 설정을 시작하고 runlevel 0 에서 네트워킹을 중지한다는 의미입니다. 구성 파일을 작성하는 방법은 여러 가지가 있으며, 사용 가능한 다양한 작업 구성을 살펴보면 이를 알 수 있습니다.

Upstart 의 작동 방식은 다음과 같습니다:

1. 먼저 `/etc/init`에서 작업 구성을 로드합니다.
2. 시작 이벤트가 발생하면 해당 이벤트에 의해 트리거된 작업을 실행합니다.
3. 이 작업들은 새로운 이벤트를 생성하고, 이 이벤트들은 더 많은 작업을 트리거합니다.
4. Upstart 는 필요한 모든 작업을 완료할 때까지 이 과정을 계속합니다.

## Exercise

Upstart 를 실행 중이라면 `/etc/init`의 작업 구성을 이해할 수 있는지 확인해 보세요.

## Quiz Question

Ubuntu 에서 사용되는 init 구현체는 무엇입니까?

## Quiz Answer

upstart
