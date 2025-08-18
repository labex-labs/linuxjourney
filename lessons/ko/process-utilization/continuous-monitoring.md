---
lang: "ko"
title: "지속적인 모니터링"
meta_title: "지속적인 모니터링 - 프로세스 활용"
meta_description: "sar 를 사용하여 지속적인 Linux 시스템 모니터링을 배우세요. 설치, 데이터 수집, 그리고 성능을 위한 과거 자원 사용량 분석 방법을 이해하세요. 지금 시작하세요!"
meta_keywords: "sar, sysstat, Linux 모니터링, 시스템 성능, 지속적인 모니터링, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

이러한 모니터링 도구는 시스템에 문제가 발생했을 때 살펴보기에 좋지만, 여러분이 보고 있지 않을 때 문제가 발생하는 시스템은 어떻게 해야 할까요? 이러한 경우에는 지속적인 모니터링 도구가 필요합니다. 시스템 활동 정보를 수집하고, 보고하며, 저장하는 도구 말이죠. 이 강의에서는 사용할 훌륭한 도구인 **sar**에 대해 알아보겠습니다.

### Installing sar

sar 는 시스템의 과거 데이터를 분석하는 데 사용되는 도구입니다. 먼저, `sysstat` 패키지를 설치하여 sar 가 설치되어 있는지 확인하세요: `sudo apt install sysstat`.

### Setting up data collection

일반적으로 `sysstat`를 설치하면 시스템이 자동으로 데이터 수집을 시작합니다. 만약 그렇지 않다면, `/etc/default/sysstat` 파일의 `ENABLED` 필드를 수정하여 활성화할 수 있습니다.

### Using sar

```bash
sudo sar -q
```

이 명령어는 하루의 시작부터의 세부 정보를 나열합니다.

```bash
sudo sar -r
```

이것은 하루의 시작부터의 메모리 사용량 세부 정보를 나열합니다.

```bash
sudo sar -P
```

이것은 CPU 사용량 세부 정보를 나열합니다.

다른 날짜의 보기를 보려면 `/var/log/sysstat/saXX`로 이동할 수 있습니다. 여기서 `XX`는 보려는 날짜입니다.

```bash
sar -q /var/log/sysstat/sa02
```

## Exercise

시스템에 sar 를 설치하고 시스템 자원 활용도를 수집 및 분석하기 시작하세요.

## Quiz Question

시스템 자원을 모니터링하는 데 사용하기 좋은 도구는 무엇입

## Quiz Answer

sar
