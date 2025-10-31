---
index: 5
lang: "ko"
title: "I/O 모니터링"
meta_title: "I/O 모니터링 - 프로세스 활용도"
meta_description: "iostat 명령어로 리눅스 I/O 모니터링을 마스터하세요. 이 가이드는 시스템 성능 최적화를 위해 CPU 및 디스크 사용량 지표를 분석하는 방법을 설명합니다."
meta_keywords: "i/o 모니터링, iostat, 리눅스 i/o 모니터링, cpu 사용량, 디스크 사용량, 시스템 성능, iowait, 리눅스 명령어"
---

## Lesson Content

효과적인 **I/O 모니터링**은 건강하고 반응성이 좋은 Linux 시스템을 유지하는 데 매우 중요합니다. 이 작업을 위한 강력한 명령줄 도구는 **iostat**이며, CPU 및 디스크 활동에 대한 자세한 보고서를 제공합니다.

`iostat` 명령을 실행하면 시스템 성능 메트릭의 스냅샷이 생성됩니다.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

출력은 두 가지 주요 섹션으로 나뉩니다. 각 섹션을 분석해 보겠습니다.

### CPU 메트릭 이해하기

첫 번째 보고서는 CPU 활용도를 자세히 설명하며, 프로세서가 시간을 어떻게 사용하고 있는지에 대한 통찰력을 제공합니다.

- **%user**: 사용자 수준 (애플리케이션) 프로세스를 실행하는 데 사용된 CPU 시간의 비율입니다.
- **%nice**: 수정된 (nice) 우선순위를 가진 사용자 수준 프로세스에 사용된 CPU 시간의 비율입니다.
- **%system**: 시스템 수준 (커널) 프로세스를 실행하는 데 사용된 CPU 시간의 비율입니다.
- **%iowait**: 디스크 I/O 요청이 완료되기를 기다리는 동안 CPU 가 유휴 상태였던 시간의 비율입니다. 이 값이 높으면 스토리지 병목 현상을 나타낼 수 있습니다.
- **%steal**: 가상화 환경에서 이는 하이퍼바이저가 다른 가상 프로세서에 서비스를 제공하는 동안 가상 CPU 가 실제 CPU 를 기다린 시간의 비율입니다.
- **%idle**: CPU 가 유휴 상태였으며 디스크 I/O 요청을 기다리지 않은 시간의 비율입니다.

### 디스크 활용도 분석

두 번째 보고서는 장치 수준 **I/O 모니터링**에 중점을 두며, 데이터가 스토리지 장치와 어떻게 전송되고 있는지를 보여줍니다.

- **tps**: 장치에 발행된 초당 전송 횟수입니다. 전송은 I/O 요청이며, 여러 논리적 요청이 단일 요청으로 결합될 수 있습니다.
- **kB_read/s**: 장치에서 초당 킬로바이트 단위로 표시되는 읽기 데이터 양입니다.
- **kB_wrtn/s**: 장치에 초당 킬로바이트 단위로 표시되는 쓰기 데이터 양입니다.
- **kB_read**: 마지막 재부팅 이후 장치에서 읽은 총 킬로바이트 수입니다.
- **kB_wrtn**: 마지막 재부팅 이후 장치에 기록한 총 킬로바이트 수입니다.

## Exercise

연습이 완벽함을 만듭니다! 시스템 모니터링 및 디스크 사용량에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux df 명령어: 디스크 공간 보고](https://labex.io/ko/labs/linux-linux-df-command-disk-space-reporting-219188)** - 마운트된 파일 시스템의 디스크 공간 사용량 보고를 연습합니다. 이는 모니터링의 핵심 측면입니다.
2. **[Linux du 명령어: 파일 공간 추정](https://labex.io/ko/labs/linux-linux-du-command-file-space-estimating-219190)** - 디렉터리 및 하위 디렉터리의 디스크 공간 사용량을 추정하는 방법을 알아봅니다. 이는 `iostat`의 디스크 I/O 정보와 상호 보완적입니다.
3. **[Linux top 명령어: 실시간 시스템 모니터링](https://labex.io/ko/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - CPU 메트릭을 더 넓은 맥락에서 볼 수 있도록 CPU 및 메모리 사용량을 포함한 실시간 시스템 모니터링을 탐색합니다.

## Quiz Question

I/O 및 CPU 사용량을 확인하는 데 사용할 수 있는 명령은 무엇입니까? (소문자 영어 문자만 사용하여 답변하십시오)

## Quiz Answer

iostat
