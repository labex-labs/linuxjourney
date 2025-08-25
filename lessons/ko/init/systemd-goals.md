---
index: 6
lang: "ko"
title: "Systemd 목표"
meta_title: "Systemd 목표 - Init"
meta_description: "systemd 유닛의 기본 사항과 필수 systemctl 명령어를 배웁니다. Linux 에서 서비스를 관리하고, 상태를 확인하고, 유닛을 활성화하는 방법을 이해합니다. 여정을 시작하세요!"
meta_keywords: "systemd, systemctl, Linux 서비스, 유닛 파일, 초보자, 튜토리얼, 가이드, Linux 명령어"
---

## Lesson Content

systemd 유닛 파일을 작성하는 세부 사항까지 다루지는 않을 것입니다. 하지만 유닛 파일에 대한 간략한 개요와 유닛을 수동으로 제어하는 방법에 대해 살펴보겠습니다.

다음은 기본적인 서비스 유닛 파일입니다: foobar.service

```
[Unit]
Description=My Foobar
Before=bar.target

[Service]
ExecStart=/usr/bin/foobar

[Install]
WantedBy=multi-user.target
```

이것은 간단한 서비스 타겟입니다. 파일의 시작 부분에는 `[Unit]` 섹션이 있습니다. 이 섹션을 통해 유닛 파일에 설명을 제공하고 유닛을 활성화할 시점의 순서를 제어할 수 있습니다. 다음 부분은 `[Service]` 섹션입니다. 여기서는 서비스를 시작, 중지 또는 다시 로드할 수 있습니다. 그리고 `[Install]` 섹션은 의존성을 위해 사용됩니다. 이것은 systemd 파일을 작성하는 데 있어 빙산의 일각에 불과하므로, 더 자세히 알고 싶다면 이 주제에 대해 더 읽어보시길 권합니다.

이제 systemd 유닛과 함께 사용할 수 있는 몇 가지 명령어를 살펴보겠습니다:

### 유닛 나열

```bash
systemctl list-units
```

### 유닛 상태 보기

```bash
systemctl status networking.service
```

### 서비스 시작

```bash
sudo systemctl start networking.service
```

### 서비스 중지

```bash
sudo systemctl stop networking.service
```

### 서비스 재시작

```bash
sudo systemctl restart networking.service
```

### 유닛 활성화

```bash
sudo systemctl enable networking.service
```

### 유닛 비활성화

```bash
sudo systemctl disable networking.service
```

다시 말하지만, systemd 가 얼마나 깊이 들어가는지 아직 보지 못했으니, 더 배우고 싶다면 읽어보세요.

## Exercise

연습이 완벽을 만듭니다! 다음은 systemd 서비스에 의해 제어되는 프로세스 관리에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 포그라운드 및 백그라운드 프로세스와 상호 작용하고, `ps`로 검사하고, `top`으로 리소스를 모니터링하고, `renice`로 우선순위를 조정하고, `kill`로 종료하는 연습을 합니다. 이 실습은 systemd 유닛 관리의 런타임 효과에 대한 실질적인 경험을 제공할 것입니다.

이 실습들은 실제 시나리오에 개념을 적용하고 Linux 에서 프로세스 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

peanut.service 라는 서비스 시작 명령어는 무엇입니까?

## Quiz Answer

sudo systemctl start peanut.service
