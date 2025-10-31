---
index: 6
lang: "ko"
title: "Systemd 목표"
meta_title: "Systemd 목표 - Init"
meta_description: "systemd 목표를 살펴보고 필수 systemctl 명령어를 사용하여 Linux 서비스를 관리하는 방법을 알아보세요. 이 가이드는 systemd 유닛 파일 기본 사항, 서비스 시작, 중지 및 활성화 방법, 상태 확인 방법을 다룹니다."
meta_keywords: "systemd, systemctl, Linux 서비스, 유닛 파일, systemd 목표, 서비스 관리, systemd 유닛, 초보자, 튜토리얼, 가이드, Linux 명령어"
---

## Lesson Content

이 레슨에서는 systemd 유닛 파일의 기본 개요와 init 시스템을 제어하는 주요 도구인 `systemctl`을 사용하여 이를 관리하는 방법을 제공합니다. 유닛 파일의 기본 구조와 Linux 서비스를 관리하기 위한 필수 명령어를 다룰 것입니다.

### Systemd 유닛 파일 이해하기

A systemd 유닛 파일은 systemd 가 관리할 수 있는 서비스, 마운트 지점, 장치 또는 기타 리소스를 설명하는 일반 텍스트 파일입니다. 다음은 `foobar.service`라는 서비스 유닛 파일의 기본 예시입니다.

```
[Unit]
Description=My Foobar Service
After=network.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

이 간단한 서비스 파일은 다음과 같이 섹션으로 나뉩니다.

- **[Unit]**: 이 섹션에는 메타데이터와 종속성 정보가 포함됩니다. `Description`은 유닛에 대한 사람이 읽을 수 있는 이름을 제공합니다. `After` 및 `Before`와 같은 지시문은 시작 순서를 제어하여 네트워크가 사용 가능해진 후에 이 유닛이 시작되도록 보장합니다.
- **[Service]**: 이 섹션은 서비스 관리 방법을 정의합니다. `ExecStart` 지시문은 서비스를 시작하기 위해 실행할 명령을 지정하므로 매우 중요합니다. `ExecStop` 및 `ExecReload`와 같은 다른 지시문은 서비스를 중지하거나 다시 로드하는 방법을 정의할 수 있습니다.
- **[Install]**: 이 섹션은 `systemctl`로 유닛을 활성화하거나 비활성화할 때의 동작을 정의합니다. `WantedBy` 지시문은 systemd 에게 이 유닛을 표준 비그래픽 부팅을 위한 `multi-user.target`과 같은 특정 대상의 일부로 시작하도록 지시합니다.

이는 systemd 유닛 파일에 대한 간략한 소개일 뿐입니다. 더 고급 구성을 위해서는 해당 주제에 대한 추가적인 조사를 강력히 권장합니다.

### 필수 Systemctl 명령어

이제 systemd 유닛과 상호 작용하고 Linux 서비스를 관리하는 데 사용할 필수 `systemctl` 명령어를 살펴보겠습니다.

### Systemd 유닛 나열하기

systemd 가 현재 관리하고 있는 모든 활성 유닛을 보려면 `list-units` 명령어를 사용합니다.

```bash
systemctl list-units
```

### 유닛 상태 확인하기

특정 유닛의 상세 상태 (활성 여부, 활성화 여부, 최신 로그 항목 포함) 를 보려면 `status` 명령어를 사용합니다.

```bash
systemctl status networking.service
```

### 서비스 상태 관리하기

`start`, `stop`, `restart`를 사용하여 서비스의 런타임 상태를 제어할 수 있습니다.

서비스를 즉시 시작하려면:

```bash
sudo systemctl start networking.service
```

실행 중인 서비스를 중지하려면:

```bash
sudo systemctl stop networking.service
```

서비스를 중지했다가 다시 시작하려면:

```bash
sudo systemctl restart networking.service
```

### 서비스 활성화 및 비활성화하기

서비스를 활성화하면 부팅 프로세스에 연결되는 심볼릭 링크가 생성되어 자동으로 시작되도록 보장합니다. 비활성화하면 해당 링크가 제거됩니다.

부팅 시 서비스가 시작되도록 활성화하려면:

```bash
sudo systemctl enable networking.service
```

부팅 시 서비스 시작을 비활성화하려면:

```bash
sudo systemctl disable networking.service
```

이러한 명령어들은 최신 Linux 시스템에서 서비스 관리를 위한 구성 요소입니다. 이를 숙달하는 것은 Linux 여정에서 중요한 단계입니다.

## Exercise

연습이 새로운 기술을 익히는 열쇠입니다. 이 실습 랩은 systemd 서비스에 의해 종종 제어되는 프로세스 관리에 대한 이해를 강화하는 데 도움이 될 것입니다.

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 전경 및 백그라운드 프로세스와 상호 작용하고, `ps`로 검사하고, `top`으로 리소스를 모니터링하고, `renice`로 우선순위를 조정하고, `kill`로 종료하는 연습을 합니다. 이 랩은 systemd 유닛 관리의 런타임 효과에 대한 실질적인 경험을 제공할 것입니다.

이 랩은 이러한 개념을 실제 시나리오에 적용하고 Linux 에서 프로세스 관리에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

peanut.service 라는 서비스를 시작하는 명령어는 무엇입니까? 답변은 영어로 하십시오. 대소문자를 구분합니다.

## Quiz Answer

sudo systemctl start peanut.service
