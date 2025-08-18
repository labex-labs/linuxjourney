---
index: 1
lang: "ko"
title: "프로세스 추적: top"
meta_title: "프로세스 추적: top - 프로세스 활용"
meta_description: "Linux `top` 명령을 사용하여 시스템 리소스를 모니터링하고 프로세스를 추적하는 방법을 배웁니다. 성능 분석을 위한 CPU, 메모리 및 프로세스 세부 정보를 이해합니다."
meta_keywords: "Linux top 명령, 프로세스 모니터링, 시스템 활용, Linux 성능, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

이 과정에서는 시스템의 리소스 사용량을 읽고 분석하는 방법을 다룹니다. 이 단원에서는 프로세스가 무엇을 하고 있는지 추적해야 할 때 사용할 수 있는 훌륭한 도구들을 보여줍니다.

### top

`top`에 대해 이전에 논의했지만, 이번에는 `top`이 실제로 무엇을 표시하는지 구체적으로 살펴보겠습니다. `top`은 프로세스에 의한 시스템 사용량을 실시간으로 볼 수 있도록 사용했던 도구임을 기억하십시오:

```plaintext
top - 18:06:26 up 6 days,  4:07,  2 users,  load average: 0.92, 0.62, 0.59
Tasks: 389 total,   1 running, 387 sleeping,   0 stopped,   1 zombie
%Cpu(s):  1.8 us,  0.4 sy,  0.0 ni, 97.6 id,  0.1 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem:  32870888 total, 27467976 used,  5402912 free,   518808 buffers
KiB Swap: 33480700 total,    39892 used, 33440808 free. 19454152 cached Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
 6675 patty    20   0 1731472 520960  30876 S   8.3  1.6 160:24.79 chrome
 6926 patty    20   0  935888 163456  25576 S   4.3  0.5   5:28.13 chrome
```

이 출력의 의미를 살펴보겠습니다. 이것을 모두 외울 필요는 없지만, 참고 자료가 필요할 때 다시 돌아오십시오.

### 1st line: This is the same information you would see if you ran the `uptime` command (more to come)

필드는 왼쪽에서 오른쪽으로 다음과 같습니다:

1. 현재 시간
2. 시스템이 실행된 시간
3. 현재 로그인한 사용자 수
4. 시스템 로드 평균 (추가 설명 예정)

### 2nd line: Tasks that are running, sleeping, stopped, and zombied

### 3rd line: CPU information

1. `us`: user CPU time - nice 되지 않은 사용자 프로세스를 실행하는 데 소요된 CPU 시간의 백분율.
2. `sy`: system CPU time - 커널 및 커널 프로세스를 실행하는 데 소요된 CPU 시간의 백분율.
3. `ni`: nice CPU time - nice 된 프로세스를 실행하는 데 소요된 CPU 시간의 백분율.
4. `id`: CPU idle time - 유휴 상태로 소요된 CPU 시간의 백분율.
5. `wa`: I/O wait - I/O 를 기다리는 데 소요된 CPU 시간의 백분율. 이 값이 낮으면 디스크 또는 네트워크 I/O 문제가 아닐 가능성이 높습니다.
6. `hi`: hardware interrupts - 하드웨어 인터럽트를 처리하는 데 소요된 CPU 시간의 백분율.
7. `si`: software interrupts - 소프트웨어 인터럽트를 처리하는 데 소요된 CPU 시간의 백분율.
8. `st`: steal time - 가상 머신을 실행하는 경우, 다른 작업을 위해 당신에게서 도난당한 CPU 시간의 백분율입니다.

### 4th and 5th line: Memory Usage and Swap Usage

### Processes List that are Currently in Use

1. `PID`: 프로세스 ID
2. `USER`: 프로세스 소유자 사용자
3. `PR`: 프로세스 우선순위
4. `NI`: nice 값
5. `VIRT`: 프로세스가 사용한 가상 메모리
6. `RES`: 프로세스가 사용한 물리적 메모리
7. `SHR`: 프로세스의 공유 메모리
8. `S`: 프로세스 상태를 나타냅니다: `S`=sleep, `R`=running, `Z`=zombie, `D`=uninterruptible, `T`=stopped
9. `%CPU`: 이 프로세스가 사용한 CPU 의 백분율
10. `%MEM`: 이 프로세스가 사용한 RAM 의 백분율
11. `TIME+`: 이 프로세스의 총 활동 시간
12. `COMMAND`: 프로세스 이름

특정 프로세스만 추적하려면 프로세스 ID 를 지정할 수도 있습니다:

```bash
top -p 1
```

## Exercise

`top` 명령을 사용하여 어떤 프로세스가 가장 많은 리소스를 사용하는지 확인해 보십시오.

## Quiz Question

`top`의 첫 번째 줄과 동일한 출력을 표시하는 명령은 무엇입까?

## Quiz Answer

uptime
