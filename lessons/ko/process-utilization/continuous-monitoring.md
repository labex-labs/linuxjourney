---
index: 7
lang: "ko"
title: "지속적인 모니터링"
meta_title: "지속적인 모니터링 - 프로세스 활용"
meta_description: "sar 를 사용하여 지속적인 Linux 시스템 모니터링을 배우십시오. 설치, 데이터 수집 및 성능을 위한 과거 리소스 사용량 분석 방법을 이해하십시오. 지금 시작하십시오!"
meta_keywords: "sar, sysstat, Linux 모니터링, 시스템 성능, 지속적인 모니터링, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

이러한 모니터링 도구는 시스템에 문제가 발생했을 때 살펴보기에 좋지만, 여러분이 보고 있지 않을 때 문제가 발생하는 시스템은 어떻게 해야 할까요? 이러한 경우에는 시스템 활동 정보를 수집, 보고, 저장하는 지속적인 모니터링 도구가 필요합니다. 이 강의에서는 사용할 훌륭한 도구인 **sar**에 대해 알아보겠습니다.

### sar 설치하기

Sar 는 시스템에 대한 과거 분석을 수행하는 데 사용되는 도구입니다. 먼저, `sysstat` 패키지를 설치하여 설치되어 있는지 확인하십시오: `sudo apt install sysstat`.

### 데이터 수집 설정

일반적으로 `sysstat`을 설치하면 시스템이 자동으로 데이터 수집을 시작합니다. 그렇지 않은 경우 `/etc/default/sysstat` 파일의 `ENABLED` 필드를 수정하여 활성화할 수 있습니다.

### sar 사용하기

```bash
sudo sar -q
```

이 명령은 하루 시작부터의 세부 정보를 나열합니다.

```bash
sudo sar -r
```

이것은 하루 시작부터의 메모리 사용량 세부 정보를 나열합니다.

```bash
sudo sar -P
```

이것은 CPU 사용량 세부 정보를 나열합니다.

다른 날짜의 보기를 보려면 `/var/log/sysstat/saXX`로 이동할 수 있습니다. 여기서 `XX`는 보려는 날짜입니다.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

연습이 완벽을 만듭니다! 다음은 시스템 모니터링 및 리소스 분석에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 프로세스 관리 및 모니터링](https://labex.io/ko/labs/comptia-manage-and-monitor-linux-processes-590864)** - 포그라운드 및 백그라운드 프로세스와 상호 작용하고, `ps`로 검사하고, `top`으로 리소스를 모니터링하고, `kill`로 종료하는 연습을 합니다.
2. **[Linux top 명령어: 실시간 시스템 모니터링](https://labex.io/ko/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - `top` 명령어의 다양한 옵션을 사용하여 프로세스를 정렬하고, 업데이트 간격을 조정하고, 사용자로 필터링하고, 활성 프로세스에 집중하여 시스템 성능을 효과적으로 모니터링하는 방법을 배웁니다.
3. **[Linux df 명령어: 디스크 공간 보고](https://labex.io/ko/labs/linux-linux-df-command-disk-space-reporting-219188)** - 이 실습에서는 마운트된 파일 시스템의 디스크 공간 사용량에 대한 정보를 표시하는 유틸리티인 Linux 의 `df` 명령어를 소개하며, 이는 시스템 모니터링의 핵심 측면입니다.

이러한 실습은 실제 시나리오에서 시스템 리소스 모니터링 개념을 적용하고 시스템 활동 분석에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

시스템 리소스를 모니터링하는 데 사용하기 좋은 도구는 무엇입니까?

## Quiz Answer

sar
