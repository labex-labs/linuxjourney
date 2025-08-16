---
title: "System V 개요"
description: "System V init, 런레벨, 그리고 Linux 에서 프로세스를 관리하는 방법에 대해 알아보세요. 초보자와 중급 사용자를 위한 SysV 기본 사항을 이해합니다."
keywords: "System V, SysV init, Linux 런레벨, init 시스템, Linux 튜토리얼, 초보자 가이드, 프로세스 관리"
---

## Lesson Content

init 의 주요 목적은 시스템에서 필수 프로세스를 시작하고 중지하는 것입니다. Linux 에는 System V, Upstart, systemd 의 세 가지 주요 init 구현이 있습니다. 이 강의에서는 가장 전통적인 init 버전인 System V init 또는 Sys V('System Five'로 발음) 에 대해 살펴보겠습니다.

Sys V init 구현을 사용하고 있는지 확인하려면 `/etc/inittab` 파일을 확인하십시오. 이 파일이 존재하면 Sys V 를 실행하고 있을 가능성이 높습니다.

Sys V 는 프로세스를 순차적으로 시작하고 중지합니다. 예를 들어, `foo-a`라는 서비스를 시작하려면 `foo-a`가 이미 실행 중이어야 `foo-b`가 작동할 수 없습니다. Sys V 는 스크립트를 사용하여 이를 수행합니다. 이 스크립트들은 서비스를 시작하고 중지합니다. 우리는 우리만의 스크립트를 작성할 수도 있고, 대부분의 경우 운영 체제에 이미 내장되어 있고 필수 서비스를 로드하는 데 사용되는 스크립트를 사용할 수 있습니다.

이 init 구현을 사용하는 장점은 `foo-a`가 `foo-b`보다 먼저 온다는 것을 알기 때문에 의존성을 해결하기가 비교적 쉽다는 것입니다. 그러나 한 번에 하나의 작업만 시작되거나 중지되기 때문에 성능은 좋지 않습니다.

Sys V 를 사용할 때, 머신의 상태는 0 에서 6 까지 설정되는 런레벨 (runlevels) 에 의해 정의됩니다. 이러한 다른 모드는 배포판에 따라 다를 수 있지만, 대부분 다음과 같이 보일 것입니다:

- 0: Shutdown
- 1: Single User Mode
- 2: Multiuser mode without networking
- 3: Multiuser mode with networking
- 4: Unused
- 5: Multiuser mode with networking and GUI
- 6: Reboot

시스템이 시작되면, 어떤 런레벨에 있는지 확인하고 해당 런레벨 구성 내에 있는 스크립트를 실행합니다. 스크립트는 **/etc/rc.d/rc[runlevel number].d/** 또는 **/etc/init.d**에 있습니다. S(start) 로 시작하는 스크립트와 K(kill) 로 시작하는 스크립트는 각각 시작 시와 종료 시에 실행됩니다. 이 문자 옆의 숫자는 실행 순서를 나타냅니다.

예시:

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

런레벨 0 또는 종료 모드로 전환할 때, 우리 머신은 업데이트 서비스를 종료하고 OpenVPN 을 종료하는 스크립트를 실행하려고 시도할 것입니다. 머신이 어떤 런레벨로 부팅되는지 확인하려면 `/etc/inittab` 파일에서 기본 런레벨을 확인할 수 있습니다. 이 파일에서 기본 런레벨을 변경할 수도 있습니다.

한 가지 유의할 점: System V 는 천천히 대체되고 있습니다. 오늘 당장은 아니더라도 몇 년 후에는 대체될 수 있습니다. 그러나 다른 init 구현에서도 런레벨이 나타날 수 있습니다. 이는 주로 System V init 스크립트만을 사용하여 시작되거나 중지되는 서비스를 지원하기 위함입니다.

## Exercise

System V 를 실행 중이라면, 머신의 기본 런레벨을 다른 것으로 변경하고 어떤 일이 발생하는지 확인하십시오.

## Quiz Question

어떤 런레벨이 일반적으로 종료에 사용됩니까?

## Quiz Answer

0
