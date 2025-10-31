---
index: 5
lang: "ko"
title: "Systemd 개요"
meta_title: "Systemd 개요 - 초기화 시스템"
meta_description: "systemd 초기화 시스템의 기본 사항을 알아보세요. 이 가이드는 systemd(또는 system d) 가 유닛과 타겟을 사용하여 Linux 부팅 프로세스와 시스템 서비스를 관리하는 방법을 다룹니다. Linux 초기화의 현대 표준 핵심 개념을 이해하세요."
meta_keywords: "systemd, system d, 초기화 시스템, systemd 유닛, systemd 타겟, 리눅스 부팅 프로세스, 리눅스 서비스, 시스템 관리, 입문, 튜토리얼"
---

## Lesson Content

### systemd 란 무엇인가?

Systemd 는 대부분의 최신 Linux 배포판에서 기본 init 시스템 및 서비스 관리자입니다. 커널이 로드된 후 시스템을 올바른 순서로 초기화하는 역할을 합니다. 시스템에서 systemd 를 사용하는지 확인하는 간단한 방법은 `/usr/lib/systemd` 디렉터리가 존재하는지 확인하는 것입니다. 존재한다면, **systemd**에 의해 관리되는 시스템을 실행하고 있을 가능성이 높습니다.

### systemd 부팅 프로세스

엄격한 순차적 스크립트 대신, **systemd**는 시스템을 기능적인 상태로 만들기 위해 "목표 (goals)" 개념을 사용합니다. 이는 주 목표, 즉 `target`을 식별하고 해당 종속성을 충족시키기 위해 작동합니다. 이 접근 방식은 시작 시 더 큰 유연성과 병렬화를 허용합니다. **systemd**가 관리하는 일반적인 부팅 프로세스는 다음 단계를 따릅니다.

1. **systemd**는 먼저 `/etc/systemd/system` 및 `/usr/lib/systemd/system`과 같은 디렉터리에서 구성 파일을 로드합니다.
2. 그런 다음 기본 부팅 목표를 식별하는데, 이는 일반적으로 `default.target`이라는 심볼릭 링크입니다.
3. 마지막으로, **systemd**는 이 목표에 대한 모든 종속성을 해결하고 원하는 시스템 상태를 달성하기 위해 필요한 유닛을 활성화합니다.

### systemd 타겟 이해하기

**systemd**의 타겟은 이전 SysV init 시스템의 런레벨과 유사합니다. 이는 시스템이 가질 수 있는 다른 상태를 나타냅니다. 일반적인 타겟은 다음과 같습니다.

- `poweroff.target`: 시스템을 종료합니다.
- `rescue.target`: 유지 관리를 위해 단일 사용자 셸로 부팅합니다.
- `multi-user.target`: 그래픽 인터페이스 없이 네트워킹이 가능한 표준 다중 사용자 환경입니다.
- `graphical.target`: 네트워킹 및 그래픽 사용자 인터페이스 (GUI) 가 있는 완전한 다중 사용자 환경입니다.
- `reboot.target`: 시스템을 다시 시작합니다.

The `default.target`은 시스템이 기본적으로 부팅될 타겟을 가리키는 심볼릭 링크이며, 데스크톱 시스템에서는 종종 `graphical.target`입니다.

### 핵심 개념: systemd 유닛

**systemd**가 관리하는 기본 객체를 "유닛 (units)"이라고 합니다. 유닛은 리소스나 서비스를 설명하는 구성 파일입니다. **system d** 아키텍처의 강력함은 서비스뿐만 아니라 다양한 유형의 리소스를 관리할 수 있다는 점에 있습니다. 각 유닛 유형은 파일 확장자로 식별됩니다. 가장 일반적인 유형은 다음과 같습니다.

- **서비스 유닛 (`.service`):** 웹 서버나 데이터베이스와 같은 시스템 데몬 또는 서비스를 관리합니다.
- **마운트 유닛 (`.mount`):** 파일 시스템 마운트 지점을 제어합니다.
- **타겟 유닛 (`.target`):** 다른 유닛들을 그룹화하여 부팅 시 동기화 지점을 만드는 데 사용됩니다.

예를 들어, 시스템이 `graphical.target`으로 부팅될 때, 해당 타겟 유닛은 `multi-user.target` 및 `network.service`와 같은 다양한 서비스 유닛과 같은 모든 종속성이 먼저 시작되도록 보장합니다.

## Exercise

이 주제에 대한 특정 실습은 없지만, 관련 Linux 기술 및 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 살펴보는 것을 권장합니다.

## Quiz Question

다른 유닛들을 그룹화하는 데 사용되는 유닛은 무엇입니까? 하나의 소문자 영어 단어로 답하십시오.

## Quiz Answer

target
