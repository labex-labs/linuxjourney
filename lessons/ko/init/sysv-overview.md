---
index: 1
lang: "ko"
title: "System V 개요"
meta_title: "System V 개요 - Init"
meta_description: "SysV 또는 init v 라고도 알려진 전통적인 System V init 시스템을 살펴보세요. 이 가이드는 systemv 가 프로세스를 관리하는 방법, 순차적 시작, Linux 에서 런레벨의 역할을 다룹니다. 클래식 initv 프로세스의 기본 사항을 알아보세요."
meta_keywords: "System V, systemv, SysV init, systemv init, init v, initv, Linux 런레벨, init 시스템, 프로세스 관리, Linux 튜토리얼"
---

## Lesson Content

init 시스템의 주요 역할은 필수 프로세스를 시작하고 중지하는 것입니다. Linux 에서는 System V, Upstart, systemd 라는 세 가지 주요 init 구현이 있었습니다. 이 레슨에서는 가장 전통적인 버전인 **System V init**에 중점을 두며, 이는 종종 **SysV** 또는 단순히 **systemv**(발음: '시스템 파이브') 라고 불립니다.

시스템이 **systemv** 구현을 사용하는지 확인하려면 `/etc/inittab` 파일이 있는지 확인하십시오. 이 파일이 존재한다면, SysV 기반 배포판을 사용하고 있을 가능성이 높습니다.

### System V 가 프로세스를 관리하는 방법

**systemv init** 프로세스는 서비스를 순차적으로 시작하고 중지합니다. 예를 들어, `foo-b`라는 서비스가 `foo-a`에 의존한다면, `foo-a`가 완전히 실행될 때까지 `foo-b`는 시작될 수 없습니다. **initv** 시스템은 셸 스크립트를 사용하여 이를 수행합니다. 이 스크립트들은 특정 디렉토리에 위치하며 서비스의 시작과 중지를 처리합니다. 사용자 지정 스크립트를 작성할 수도 있지만, 대부분의 시스템은 필수 OS 서비스를 관리하는 사전 패키징된 스크립트에 의존합니다.

### 장점과 단점

이 순차적 접근 방식의 주요 장점은 단순성과 예측 가능성입니다. `foo-a`가 항상 `foo-b`보다 먼저 시작된다는 것을 알기 때문에 종속성 문제 해결이 간단합니다. 그러나 **init v** 모델의 주요 단점은 성능입니다. 서비스가 일반적으로 한 번에 하나씩 시작되어 최신 병렬 시스템에 비해 부팅 시간이 느려지기 때문입니다.

### System V 에서 런레벨 이해하기

**systemv** 환경에서 시스템의 상태는 0 에서 6 까지 번호가 매겨진 **런레벨 (runlevels)**로 정의됩니다. 이 모드는 Linux 배포판마다 약간 다를 수 있지만, 일반적으로 다음 표준 규칙을 따릅니다.

- 0: 시스템 종료 (Shutdown)
- 1: 단일 사용자 모드 (Single User Mode)
- 2: 네트워킹 없는 다중 사용자 모드 (Multiuser mode without networking)
- 3: 네트워킹을 사용하는 다중 사용자 모드 (Multiuser mode with networking)
- 4: 사용되지 않음 (Unused)
- 5: 네트워킹 및 GUI 를 사용하는 다중 사용자 모드 (Multiuser mode with networking and GUI)
- 6: 재부팅 (Reboot)

### Init 스크립트 및 디렉토리

시스템이 부팅될 때 구성된 런레벨을 확인하고 해당 스크립트를 실행합니다. 이러한 스크립트는 일반적으로 **/etc/rc.d/rc[런레벨].d/**와 같은 디렉토리나 중앙 **/etc/init.d** 디렉토리 내에서 발견됩니다. `S`(Start) 로 시작하는 스크립트는 시작 시 실행되고, `K`(Kill) 로 시작하는 스크립트는 종료 시 실행됩니다. `S` 또는 `K` 뒤에 오는 숫자는 실행 순서를 결정합니다.

예를 들면 다음과 같습니다.

```bash
pete@icebox:/etc/rc.d/rc0.d$ ls
K10updates  K80openvpn
```

이 예에서 런레벨 0(종료) 으로 전환되면 업데이트 서비스 (updates) 를 먼저 종료하는 스크립트가 실행된 다음 OpenVPN 스크립트가 실행됩니다. 시스템의 기본 런레벨은 `/etc/inittab` 파일에서 찾을 수 있으며, 여기서 런레벨을 변경할 수도 있습니다.

**System V**는 대부분의 최신 Linux 배포판에서 `systemd`로 대체되었다는 점에 유의하는 것이 중요합니다. 그러나 최신 init 시스템에서는 레거시 서비스 지원을 위해 호환성 계층을 제공하는 경우가 많으므로 런레벨 개념을 여전히 접할 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 init 시스템 작동 방식의 기초가 되는 Linux 프로세스 관리 및 시스템 구성에 대한 이해를 강화하기 위한 실습 랩입니다.

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 포그라운드 및 백그라운드 프로세스와 상호 작용하고, `ps`로 검사하고, `top`으로 리소스를 모니터링하고, `kill`로 종료하는 연습을 합니다. 이는 init 의 '필수 프로세스 시작 및 중지' 측면과 직접적으로 관련이 있습니다.
2. **[Linux 에서 at 및 cron 으로 작업 예약](https://labex.io/ko/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 일회성 및 반복 작업을 예약하는 방법을 배우며, 이는 init 스크립트가 서비스를 관리하는 방식과 유사한 자동 실행 개념을 기반으로 합니다.
3. **[Linux 에서 파일 및 디렉토리 권한 관리](https://labex.io/ko/labs/comptia-manage-file-and-directory-permissions-in-linux-590844)** - 파일 및 디렉토리 권한을 관리하는 방법을 이해합니다. 이는 `/etc/init.d`에서 발견되는 시스템 구성 파일 및 스크립트를 다룰 때 중요한 기술입니다.

이 랩들은 실제 시나리오에서 개념을 적용하고 기본 Linux 시스템 관리 작업에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

일반적으로 시스템 종료에 사용되는 런레벨은 무엇입니까?

## Quiz Answer

0
