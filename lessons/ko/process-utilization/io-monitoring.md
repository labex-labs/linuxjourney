---
index: 5
lang: "ko"
title: "I/O 모니터링"
meta_title: "I/O 모니터링 - 프로세스 활용"
meta_description: "Linux I/O 모니터링을 위해 iostat 를 사용하는 방법을 배웁니다. 이 필수 명령어를 사용하여 CPU 및 디스크 사용량 메트릭스를 이해합니다. 시스템 성능을 향상시키세요!"
meta_keywords: "iostat, Linux I/O 모니터링, CPU 사용량, 디스크 사용량, Linux 명령어, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

**iostat**라는 유용한 도구를 사용하여 CPU 사용량과 디스크 사용량을 모니터링할 수 있습니다.

```bash
pete@icebox:~$ iostat
Linux 3.13.0-39-lowlatency (icebox)     01/28/2016      _i686_  (1 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           0.13    0.03    0.50    0.01    0.00   99.33

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               0.17         3.49         1.92     385106     212417
```

첫 번째 부분은 CPU 정보입니다:

- **%user** - 사용자 레벨 (애플리케이션) 에서 실행되는 동안 발생한 CPU 활용률의 백분율을 보여줍니다.
- **%nice** - nice 우선순위로 사용자 레벨에서 실행되는 동안 발생한 CPU 활용률의 백분율을 보여줍니다.
- **%system** - 시스템 레벨 (커널) 에서 실행되는 동안 발생한 CPU 활용률의 백분율을 보여줍니다.
- **%iowait** - 시스템에 미결 디스크 I/O 요청이 있는 동안 CPU 가 유휴 상태였던 시간의 백분율을 보여줍니다.
- **%steal** - 하이퍼바이저가 다른 가상 프로세서를 서비스하는 동안 가상 CPU 가 비자발적으로 대기한 시간의 백분율을 보여줍니다.
- **%idle** - CPU 가 유휴 상태였고 시스템에 미결 디스크 I/O 요청이 없었던 시간의 백분율을 보여줍니다.

두 번째 부분은 디스크 사용량입니다:

- **tps** - 장치로 발행된 초당 전송 횟수를 나타냅니다. 전송은 장치에 대한 I/O 요청입니다. 여러 논리적 요청이 장치에 대한 단일 I/O 요청으로 결합될 수 있습니다. 전송은 불확정적인 크기입니다.
- **kB_read/s** - 초당 킬로바이트로 표현된 장치에서 읽은 데이터 양을 나타냅니다.
- **kB_wrtn/s** - 초당 킬로바이트로 표현된 장치에 기록된 데이터 양을 나타냅니다.
- **kB_read** - 읽은 총 킬로바이트 수.
- **kB_wrtn** - 기록된 총 킬로바이트 수.

## Exercise

연습은 완벽을 만듭니다! 시스템 모니터링 및 디스크 사용량에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux df 명령어: 디스크 공간 보고](https://labex.io/ko/labs/linux-linux-df-command-disk-space-reporting-219188)** - 모니터링의 핵심 측면인 마운트된 파일 시스템의 디스크 공간 사용량 보고를 연습합니다.
2. **[Linux du 명령어: 파일 공간 추정](https://labex.io/ko/labs/linux-linux-du-command-file-space-estimating-219190)** - `iostat`의 디스크 I/O 정보를 보완하여 디렉토리 및 하위 디렉토리의 디스크 공간 사용량을 추정하는 방법을 배웁니다.
3. **[Linux top 명령어: 실시간 시스템 모니터링](https://labex.io/ko/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - `iostat`에서 볼 수 있는 CPU 메트릭스에 대한 더 넓은 컨텍스트를 제공하는 CPU 및 메모리 사용량을 포함한 실시간 시스템 모니터링을 탐색합니다.

이 랩은 실제 시나리오에 개념을 적용하고 Linux 시스템 리소스 모니터링에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

I/O 및 CPU 사용량을 확인하는 데 사용할 수 있는 명령어는 무엇입니까?

## Quiz Answer

iostat
