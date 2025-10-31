---
index: 2
lang: "ko"
title: "System V 서비스"
meta_title: "System V 서비스 - Init"
meta_description: "Linux 에서 전통적인 System V(SysV) 서비스를 관리하는 방법을 알아보세요. 이 가이드는 System V init 시스템에서 `service` 명령어를 사용하여 서비스를 나열, 시작, 중지 및 재시작하는 방법을 다룹니다."
meta_keywords: "system v, sysv init, 리눅스 서비스, service 명령어, 리눅스 서비스 관리, 서비스 시작, 서비스 중지, 서비스 재시작, 리눅스 system v"
---

## Lesson Content

**System V**(또는 SysV) 는 유닉스 계열 운영 체제의 고전적인 초기화 시스템 중 하나입니다. 많은 최신 Linux 배포판이 `systemd`와 같은 새로운 시스템으로 전환했지만, 많은 시스템이 하위 호환성을 유지하므로 **System V** 서비스를 관리하는 방법을 이해하는 것은 여전히 가치 있는 기술입니다.

### service 명령어

**System V** init 시스템에서 서비스와 상호 작용하는 주요 도구는 `service` 명령어입니다. 이 명령어는 래퍼 스크립트 역할을 하여 서비스 제어 프로세스를 단순화합니다.

### 모든 서비스 나열하기

사용 가능한 모든 서비스와 현재 상태를 확인하려면 `--status-all` 플래그를 사용할 수 있습니다. 이 명령어는 각 서비스를 나열하고 실행 중 (`+`), 중지됨 (`-`), 또는 상태를 알 수 없음 (`?`) 을 표시합니다.

```bash
service --status-all
```

### 특정 서비스 제어하기

개별 서비스를 관리하려면 서비스 이름 뒤에 `start`, `stop`, 또는 `restart`와 같은 작업을 지정합니다. 이러한 작업에는 관리자 권한이 필요하므로 일반적으로 `sudo`를 사용합니다.

네트워킹 서비스와 같이 서비스를 시작하려면:

```bash
sudo service networking start
```

실행 중인 서비스를 중지하려면:

```bash
sudo service networking stop
```

구성 변경 사항을 적용하는 데 유용한, 서비스를 중지한 다음 즉시 다시 시작하려면:

```bash
sudo service networking restart
```

이러한 명령어는 **System V** init 시스템에만 국한된 것이 아니며, Upstart 서비스 관리에도 종종 사용할 수 있습니다. Linux 배포판이 계속 발전함에 따라, `service` 명령어와 같은 호환성 계층은 기존 init 스크립트에서 전환하는 데 도움을 주기 위해 유지됩니다.

## Exercise

연습이 완벽을 만듭니다! Linux 에서 프로세스 및 작업 관리를 강화하기 위한 몇 가지 실습 랩이 있습니다. 이는 Linux 에서 서비스를 관리하는 기본 사항입니다.

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 실제 Linux 환경에서 프로세스와 상호 작용, 검사, 모니터링 및 종료하는 방법을 연습합니다.
2. **[Linux 에서 at 및 cron 으로 작업 예약](https://labex.io/ko/labs/comptia-schedule-tasks-with-at-and-cron-in-linux-590870)** - 한 번 실행되는 작업에는 `at`을, 반복되는 작업에는 `cron`을 사용하여 작업을 자동화하는 방법을 배웁니다. 이는 서비스 자동화에 핵심적인 기술입니다.

이러한 랩은 실제 시나리오에서 개념을 적용하고 시스템 운영 관리에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

System V 시스템에서 `peanut`이라는 서비스를 중지하는 전체 명령어는 무엇입니까? 대소문자를 주의하여 정확한 명령어를 영어로 제공하십시오.

## Quiz Answer

sudo service peanut stop
