---
title: "Systemd 목표"
description: "systemd 유닛의 기본 사항과 필수 systemctl 명령어를 배우세요. Linux 에서 서비스를 관리하고, 상태를 확인하고, 유닛을 활성화하는 방법을 이해하세요. 여정을 시작하세요!"
keywords: "systemd, systemctl, Linux 서비스, 유닛 파일, 초보자, 튜토리얼, 가이드, Linux 명령어"
---

## Lesson Content

systemd 유닛 파일 작성에 대한 자세한 내용은 다루지 않을 것입니다. 하지만 유닛 파일에 대한 간략한 개요와 유닛을 수동으로 제어하는 방법을 살펴보겠습니다.

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

이것은 간단한 서비스 타겟입니다. 파일의 시작 부분에 `[Unit]` 섹션이 있습니다. 이 섹션을 통해 유닛 파일에 설명을 제공하고 유닛을 활성화할 순서를 제어할 수 있습니다. 다음 부분은 `[Service]` 섹션입니다. 이 섹션 아래에서 서비스를 시작, 중지 또는 다시 로드할 수 있습니다. 그리고 `[Install]` 섹션은 종속성에 사용됩니다. 이것은 systemd 파일 작성의 빙산의 일각에 불과하므로, 더 자세히 알고 싶다면 이 주제에 대해 읽어보시길 권합니다.

이제 systemd 유닛과 함께 사용할 수 있는 몇 가지 명령어를 살펴보겠습니다:

### List units

```bash
systemctl list-units
```

### View status of unit

```bash
systemctl status networking.service
```

### Start a service

```bash
sudo systemctl start networking.service
```

### Stop a service

```bash
sudo systemctl stop networking.service
```

### Restart a service

```bash
sudo systemctl restart networking.service
```

### Enable a unit

```bash
sudo systemctl enable networking.service
```

### Disable a unit

```bash
sudo systemctl disable networking.service
```

다시 말하지만, systemd 가 얼마나 깊이 들어가는지 아직 보지 못했으니, 더 배우고 싶다면 읽어보세요.

## Exercise

유닛 상태를 확인하고 몇 가지 서비스를 시작 및 중지하십시오. 무엇을 관찰하셨습니까?

## Quiz Question

peanut.service 라는 서비스을 시작하는 명령어는 무엇입니까?

## Quiz Answer

sudo systemctl start peanut.service
