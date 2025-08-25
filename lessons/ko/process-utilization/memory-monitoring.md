---
index: 6
lang: "ko"
title: "메모리 모니터링"
meta_title: "메모리 모니터링 - 프로세스 활용"
meta_description: "vmstat 를 사용하여 Linux 메모리 사용량을 모니터링하는 방법을 배웁니다. 시스템 성능을 위한 메모리, 스왑 및 CPU 메트릭을 이해합니다. Linux 여정을 시작하세요!"
meta_keywords: "vmstat, Linux 메모리 모니터링, 시스템 성능, Linux 튜토리얼, 메모리 사용량, 초보자 Linux, Linux 가이드"
---

## Lesson Content

CPU 모니터링 및 I/O 모니터링 외에도 **vmstat**를 사용하여 메모리 사용량을 모니터링할 수 있습니다.

```bash
pete@icebox:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 396528  38816 384036    0    0     4     2   38   79  0  0 99  0  0
```

필드는 다음과 같습니다:

### procs

- r - 런타임 프로세스 수
- b - 중단할 수 없는 절전 모드에 있는 프로세스 수

### memory

- swpd - 사용된 가상 메모리 양
- free - 사용 가능한 메모리 양
- buff - 버퍼로 사용된 메모리 양
- cache - 캐시로 사용된 메모리 양

### swap

- si - 디스크에서 스왑 인된 메모리 양
- so - 디스크로 스왑 아웃된 메모리 양

### io

- bi - 블록 장치에서 수신된 블록 양
- bo - 블록 장치로 전송된 블록 양

### system

- in - 초당 인터럽트 수
- cs - 초당 컨텍스트 스위치 수

### cpu

- us - 사용자 시간으로 보낸 시간
- sy - 커널 시간으로 보낸 시간
- id - 유휴 상태로 보낸 시간
- wa - IO 대기 시간

## Exercise

연습하면 완벽해집니다! 시스템 및 메모리 모니터링에 대한 이해를 높이기 위한 실습 랩입니다:

1. **[Linux free 명령어: 시스템 메모리 모니터링](https://labex.io/ko/labs/linux-linux-free-command-monitoring-system-memory-388496)** - 다양한 표시 형식과 총 메모리 소비를 이해하며 시스템 메모리 사용량을 모니터링하고 분석하는 방법을 배웁니다.
2. **[Linux top 명령어: 실시간 시스템 모니터링](https://labex.io/ko/labs/linux-linux-top-command-real-time-system-monitoring-388500)** - 정렬 및 필터링을 위한 다양한 옵션을 사용하여 프로세스, CPU, 메모리 사용량을 포함한 시스템 성능을 실시간으로 모니터링하는 방법을 배웁니다.

이 랩은 실제 시나리오에서 시스템 리소스 모니터링 개념을 적용하고 Linux 시스템 성능 분석에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

메모리 사용량을 확인하는 데 사용되는 도구는 무엇입니까?

## Quiz Answer

vmstat
