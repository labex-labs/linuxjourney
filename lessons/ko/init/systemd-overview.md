---
index: 5
lang: "ko"
title: "Systemd 개요"
meta_title: "Systemd 개요 - Init"
meta_description: "Systemd 의 기본 사항을 배우세요: 유닛, 타겟, 그리고 부팅 프로세스를 이해하세요. Systemd 가 Linux 에서 서비스와 시스템 상태를 어떻게 관리하는지 알아보세요. 지금 여정을 시작하세요!"
meta_keywords: "Systemd, Systemd 유닛, Systemd 타겟, Linux 부팅 프로세스, Linux 서비스, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

Systemd 는 점차 init 의 새로운 표준이 되고 있습니다. 만약 `/usr/lib/systemd` 디렉토리가 있다면, 당신은 systemd 를 사용하고 있을 가능성이 높습니다.

Systemd 는 시스템을 가동시키기 위해 목표 (goals) 를 사용합니다. 기본적으로, 달성하고자 하는 목표가 있고, 이 목표에는 충족되어야 할 의존성 (dependencies) 이 있습니다. Systemd 는 매우 유연하고 견고하며, 프로세스를 시작하기 위해 엄격한 순서를 따르지 않습니다. 일반적인 systemd 부팅 시 발생하는 일은 다음과 같습니다:

1. 먼저, systemd 는 일반적으로 `/etc/systemd/system` 또는 `/usr/lib/systemd/system`에 위치한 구성 파일을 로드합니다.
2. 그런 다음 부팅 목표를 결정하는데, 이는 일반적으로 `default.target`입니다.
3. Systemd 는 부팅 목표의 의존성을 파악하고 이를 활성화합니다.

SysV 런레벨과 유사하게, systemd 는 다른 목표로 부팅됩니다:

- `poweroff.target` - 시스템 종료
- `rescue.target` - 단일 사용자 모드
- `multi-user.target` - 네트워킹을 포함한 다중 사용자 모드
- `graphical.target` - 네트워킹 및 GUI 를 포함한 다중 사용자 모드
- `reboot.target` - 재시작

`default.target`의 기본 부팅 목표는 일반적으로 `graphical.target`을 가리킵니다.

systemd 가 작동하는 주요 객체는 유닛 (units) 이라고 알려져 있습니다. Systemd 는 단순히 서비스를 중지하고 시작하는 것뿐만 아니라, 파일 시스템을 마운트하고, 네트워크 소켓을 모니터링하는 등 다양한 작업을 수행할 수 있습니다. 이러한 견고성 때문에, systemd 는 다양한 유형의 유닛으로 작동합니다. 가장 일반적인 유닛은 다음과 같습니다:

- 서비스 유닛 (Service units) - 우리가 시작하고 중지해 온 서비스들입니다. 이 유닛 파일들은 `.service`로 끝납니다.
- 마운트 유닛 (Mount units) - 파일 시스템을 마운트합니다. 이 유닛 파일들은 `.mount`로 끝납니다.
- 타겟 유닛 (Target units) - 다른 유닛들을 함께 그룹화합니다. 이 파일들은 `.target`으로 끝납니다.

예를 들어, 우리가 `default.target`으로 부팅한다고 가정해 봅시다. 이 타겟은 `networking.service` 유닛, `crond.service` 유닛 등을 함께 그룹화하므로, 하나의 유닛을 활성화하면 해당 유닛 아래의 모든 것이 함께 활성화됩니다.

## Exercise

이 주제에 대한 특정 실습은 없지만, 관련 Linux 기술 및 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 탐색하는 것을 권장합니다.

## Quiz Question

다른 유닛들을 함께 그룹화하는 데 사용되는 유닛은 무엇입니까?

## Quiz Answer

target
