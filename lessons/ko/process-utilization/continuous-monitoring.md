---
lesson_id: "continuous-monitoring"
course_id: "process-utilization"
lang: "ko"
order_index: 7
title: "지속적 모니터링"
description: "sysstat 수집과 sar 보고서가 과거 리눅스 성능 분석을 지원하는 방법을 알아봅니다."
meta_title: "지속적 모니터링 - 프로세스 사용량"
meta_description: "sar를 이용한 리눅스 시스템의 지속적 모니터링을 알아봅니다. 데이터 수집 활성화와 과거 리소스 사용량 분석 방법을 설명합니다."
meta_keywords: "sar, sysstat, 리눅스 모니터링, 시스템 성능, 지속적 모니터링, 과거 성능 분석"
---

대화형 도구는 지켜보는 동안 일어나는 일을 보여 줍니다. 이미 끝난 성능 저하를 조사하려면 과거 모니터링이 필요합니다. `sysstat` 모음은 주기적인 시스템 카운터를 수집하고 `sar`는 현재 카운터 또는 저장된 활동 파일을 읽습니다.

## 데이터 수집 활성화

배포판의 `sysstat` 패키지를 설치한 다음 수집기와 보존 메커니즘이 활성화됐는지 확인하십시오. 정확한 서비스, 타이머 및 설정 경로는 배포판마다 다릅니다. 패키지를 설치했다고 수집이 시작됐다고 보장할 수 없습니다.

systemd 호스트에서는 이름을 추측하지 말고 패키지가 제공한 단위를 검사합니다.

```bash
$ systemctl list-unit-files | grep sysstat
$ systemctl list-timers --all | grep sysstat
```

배포판의 sysstat 데이터 디렉터리에 새 활동 파일이 생성되는지 확인하고 권한과 보존 정책을 검토하십시오.

:::single-choice{#sar-installation-verification} `sysstat` 설치 후 무엇을 검증해야 합니까?

::option[수집이 활성화되어 활동 파일이 갱신되고 있습니다.]{#sar-collector-updating .correct explanation="패키지 설치와 활성 주기 수집은 서로 다른 조건입니다."}
::option[모든 프로세스를 수동으로 재시작했습니다.]{#sar-restart-processes explanation="모니터링 수집기를 설치한다고 모든 작업 부하를 재시작할 필요는 없습니다."}
::option[모든 과거 파일을 누구나 쓸 수 있습니다.]{#sar-world-writable explanation="모니터링 데이터에는 적절한 접근 제어를 유지해야 합니다."}
:::

## 현재 표본 읽기

`sar`에 1초 간격으로 CPU 보고서 세 개를 수집하도록 요청합니다.

```bash
$ sar -u 1 3
```

그 밖의 일반 보고서에는 실행 대기열과 부하(`-q`), 메모리(`-r`), 페이징(`-B`), 블록 장치(`-d`) 및 CPU별 활동(`-P ALL`)이 있습니다. 옵션과 필드는 sysstat 버전에 따라 다르므로 `sar --help` 또는 로컬 설명서를 확인하십시오.

:::single-choice{#sar-one-second-count} `sar -u 1 3`은 무엇을 요청합니까?

::option[1초 간격의 CPU 보고서 세 개입니다.]{#sar-three-cpu-samples .correct explanation="첫 숫자는 구간의 초 단위이고 둘째 숫자는 보고서 수입니다."}
::option[정확히 3일을 다루는 보고서 하나입니다.]{#sar-three-days explanation="피연산자는 날짜 범위가 아니라 표본 수집 구간과 횟수를 지정합니다."}
::option[저장된 CPU 파일 세 개를 삭제합니다.]{#sar-delete-files explanation="이 명령은 카운터를 읽으며 삭제를 요청하지 않습니다."}
:::

## 과거 파일 읽기

저장된 파일 위치와 이름은 서로 다르며 흔히 `/var/log/sysstat` 또는 `/var/log/sa` 아래에 있습니다. `-f`로 선택한 활동 파일을 전달합니다.

```bash
$ sar -q -f /var/log/sysstat/sa02
```

보고서 헤더에서 파일의 전체 날짜를 확인하십시오. 두 자리 접미사는 흔히 해당 월의 일자를 나타내므로 보존 기간이 겹치면 모호할 수 있습니다. 저장된 바이너리 형식에도 호환되는 sysstat 버전이 필요할 수 있습니다.

:::single-choice{#sar-historical-file-option} `sar`가 지정한 활동 파일을 읽게 하는 옵션은 무엇입니까?

::option[`-P`]{#sar-option-p explanation="입력 파일이 아니라 프로세서 보고를 선택합니다."}
::option[`-q`]{#sar-option-q explanation="대기열 및 부하 보고를 선택합니다."}
::option[`-f`]{#sar-option-f .correct explanation="파일 옵션은 읽을 저장 활동 데이터를 선택합니다."}
:::

## 사고 증거 연결하기

사고 시간과 시간대를 확정한 다음 같은 구간의 여러 신호를 비교하십시오. 부하, CPU, 실행 대기열, 페이징, 장치 활동, 네트워크 트래픽 및 애플리케이션 지연의 변화를 찾습니다. 카운터 변화는 상관관계를 보여 줄 뿐 반드시 인과 관계를 증명하지는 않습니다. 배포 기록과 애플리케이션 로그가 트리거를 설명할 수 있습니다.

공백은 호스트가 중지됐거나, 수집기가 실패했거나, 보존 정책이 데이터를 제거했다는 뜻일 수 있습니다. 사고 전에 누락된 증거를 알 수 있도록 모니터링 파이프라인 자체도 모니터링하십시오.

:::single-choice{#sar-incident-method} 사고 검토에서 과거 `sar` 데이터를 어떻게 사용해야 합니까?

::option[가장 높은 카운터 하나를 증명된 근본 원인으로 취급합니다.]{#sar-single-root explanation="상관관계 하나만으로 인과 관계가 확립되지는 않습니다."}
::option[검증된 같은 시간 구간의 여러 지표를 비교합니다.]{#sar-correlate-window .correct explanation="정렬된 신호는 가설을 구분하고 시스템 동작을 사고와 연결하는 데 도움을 줍니다."}
::option[설치 후 수집이 보장되므로 공백을 무시합니다.]{#sar-ignore-gaps explanation="수집은 실패하거나 비활성화될 수 있으므로 공백에는 설명이 필요합니다."}
:::

## 요약

이제 `sar`를 사용해 대화형 세션 밖의 성능을 조사할 수 있습니다.

1. 수집과 보존이 실제로 활성 상태인지 검증합니다.
2. 구간과 횟수를 지정해 범위가 제한된 현재 표본을 요청합니다.
3. 과거 활동 파일을 명시적으로 선택합니다.
4. 여러 지표를 사고 시간 및 작업 부하 증거와 맞춥니다.
