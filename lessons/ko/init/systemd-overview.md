---
index: 5
lang: "ko"
title: "Systemd 개요"
meta_title: "Systemd 개요 - Init"
meta_description: "Systemd 기본 사항을 알아보세요: 유닛, 타겟 및 부팅 프로세스를 이해합니다. Systemd 가 Linux 에서 서비스와 시스템 상태를 관리하는 방법을 확인하세요. 여정을 시작하세요!"
meta_keywords: "Systemd, Systemd 유닛, Systemd 타겟, Linux 부팅 프로세스, Linux 서비스, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

Systemd 는 대부분의 최신 Linux 배포판에서 표준 init 시스템입니다. `/usr/lib/systemd` 디렉토리가 있다면, Systemd 를 사용하고 있을 가능성이 높습니다.

Systemd 는 시스템을 가동하고 실행하기 위해 목표 (goal) 를 사용합니다. 기본적으로 달성하고자 하는 타겟이 있으며, 이 타겟에는 충족되어야 할 종속성 (dependencies) 이 있습니다. Systemd 는 매우 유연하고 강력하며, 프로세스를 시작하기 위해 엄격한 순서를 따르지 않습니다. 일반적인 systemd 부팅 중에 발생하는 일은 다음과 같습니다.

1. 먼저, systemd 는 보통 `/etc/systemd/system` 또는 `/usr/lib/systemd/system`에 위치한 구성 파일을 로드합니다.
2. 그런 다음 부팅 목표 (boot goal) 를 결정하며, 이는 보통 `default.target`입니다.
3. Systemd 는 부팅 타겟의 종속성을 파악하고 이를 활성화합니다.

SysV 런레벨과 유사하게, systemd 는 다른 타겟으로 부팅됩니다.

- `poweroff.target` - 시스템 종료
- `rescue.target` - 단일 사용자 모드
- `multi-user.target` - 네트워킹을 사용하는 다중 사용자 모드
- `graphical.target` - 네트워킹 및 GUI 를 사용하는 다중 사용자 모드
- `reboot.target` - 재시작

The default boot goal of `default.target` usually points to the `graphical.target`.

Systemd 가 작업하는 주요 객체는 유닛 (units) 으로 알려져 있습니다. Systemd 는 단순히 서비스를 시작하고 중지하는 것 외에도 파일 시스템을 마운트하거나 네트워크 소켓을 모니터링하는 등의 작업을 수행할 수 있습니다. 이러한 강력함 때문에, Systemd 가 작동하는 데는 다양한 유형의 유닛이 있습니다. 가장 일반적인 유닛은 다음과 같습니다.

- Service units - 우리가 시작하고 중지해 온 서비스들입니다. 이 유닛 파일들은 `.service`로 끝납니다.
- Mount units - 파일 시스템을 마운트합니다. 이 유닛 파일들은 `.mount`로 끝납니다.
- Target units - 다른 유닛들을 그룹화합니다. 파일들은 `.target`으로 끝납니다.

예를 들어, `default.target`으로 부팅한다고 가정해 봅시다. 이 타겟은 `networking.service` 유닛, `crond.service` 유닛 등을 그룹화하므로, 단일 유닛을 활성화하면 그 아래의 모든 것이 활성화됩니다.

## Exercise

이 주제에 대한 구체적인 실습은 없지만, 관련 Linux 기술 및 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 탐색해 보시기를 권장합니다.

## Quiz Question

다른 유닛들을 그룹화하는 데 사용되는 유닛은 무엇입니까?

## Quiz Answer

target
