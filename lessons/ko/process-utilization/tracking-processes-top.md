---
lesson_id: "tracking-processes-top"
course_id: "process-utilization"
lang: "ko"
order_index: 1
title: "프로세스 추적: top"
description: "top을 사용해 시스템 부하, CPU, 메모리 및 프로세스별 활동을 해석하는 방법을 알아봅니다."
meta_title: "프로세스 추적: top - 프로세스 사용량"
meta_description: "top 명령으로 시스템 리소스를 모니터링하고 프로세스를 추적하는 방법을 알아봅니다. 부하 평균, CPU 범주, VIRT 및 RES 같은 지표를 설명합니다."
meta_keywords: "리눅스 top 명령어, 프로세스 모니터링, 시스템 사용량, 리눅스 성능, top VIRT RES, 프로세스 관리"
---

`top`은 시스템 활동과 실행 중인 프로세스를 반복해서 갱신하는 뷰를 제공합니다. 성능 가설을 세우는 데 유용하지만 바쁜 표본 하나만으로 문제 원인이 증명되지는 않습니다. 여러 갱신 결과를 비교하고 로그 및 작업 부하별 지표와 연결하십시오.

## 시스템 요약 읽기

일반적인 화면은 요약 줄로 시작하고 그 뒤에 프로세스 표가 이어집니다.

```text
top - 18:06:26 up 6 days, 4:07, 2 users, load average: 0.92, 0.62, 0.59
Tasks: 389 total, 1 running, 387 sleeping, 0 stopped, 1 zombie
%Cpu(s): 1.8 us, 0.4 sy, 0.0 ni, 97.6 id, 0.1 wa, 0.0 hi, 0.0 si, 0.0 st
MiB Mem : 32099.0 total, 5276.3 free, 7031.2 used, 19791.5 buff/cache
MiB Swap: 32700.0 total, 32661.0 free, 39.0 used
```

첫 줄에는 현재 시간, 가동 시간, 로그인한 사용자 수 및 1분, 5분, 15분 부하 평균이 있습니다. 작업 줄은 프로세스 상태를 셉니다. 부하 평균은 직접적인 CPU 백분율이 아닙니다. 리눅스에서는 실행 가능한 작업과 인터럽트할 수 없는 대기 상태의 작업을 반영하므로 CPU 수, 입출력 활동 및 지연과 함께 해석하십시오.

:::single-choice{#top-load-average-periods} `top`의 세 부하 평균 값은 무엇을 나타냅니까?

::option[1분, 5분 및 15분 동안의 평균 부하입니다.]{#top-one-five-fifteen .correct explanation="값은 점차 더 긴 최근 시간 구간을 요약합니다."}
::option[가장 바쁜 세 프로세스의 CPU 사용량입니다.]{#top-three-processes explanation="프로세스별 CPU는 이 세 요약 값이 아니라 프로세스 표에 나타납니다."}
::option[메가바이트 단위의 여유 메모리, 캐시 및 스왑입니다.]{#top-three-memory-values explanation="메모리와 스왑에는 별도의 요약 줄이 있습니다."}
:::

## CPU 시간 해석하기

일반적인 CPU 필드는 다음과 같습니다.

- `us`: 사용자 공간 실행 시간
- `sy`: 커널 실행 시간
- `ni`: nice 값이 적용된 작업의 사용자 공간 시간
- `id`: 유휴 시간
- `wa`: 처리되지 않은 입출력 요청이 있는 동안의 유휴 시간
- `hi` 및 `si`: 하드웨어 및 소프트웨어 인터럽트 처리
- `st`: 하이퍼바이저가 다른 게스트에 사용한 가상 CPU 시간

`wa` 값이 높으면 입출력 대기 가설을 뒷받침할 수 있지만 어느 장치인지 식별하거나 저장 장치가 유일한 병목임을 증명하지는 않습니다. 결론을 내리기 전에 장치 지연과 애플리케이션 동작을 검사하십시오.

:::single-choice{#top-cpu-wa-meaning} `wa` CPU 필드가 보고하는 것은 무엇입니까?

::option[일반 사용자 코드 실행에 사용된 시간입니다.]{#top-wa-user explanation="사용자 공간 실행은 `us`에 보고됩니다."}
::option[부팅 후 스왑에 기록된 메모리 페이지입니다.]{#top-wa-swap explanation="스왑 활동은 CPU 시간 범주가 아닙니다."}
::option[처리되지 않은 입출력 요청이 있는 동안의 유휴 CPU 시간입니다.]{#top-wa-io .correct explanation="이 필드는 입출력 대기 시간이며 진단에는 장치 증거가 추가로 필요합니다."}
:::

## 프로세스 표 읽기

중요한 열에는 일반적으로 다음 항목이 있습니다.

- `PID`, `USER` 및 `COMMAND`: 식별 정보와 소유권
- `S`: 실행 중(`R`), 대기(`S`), 인터럽트 불가 대기(`D`), 중지(`T`), 좀비(`Z`) 같은 상태
- `%CPU` 및 `%MEM`: 표본 CPU 활동과 물리 메모리 점유율
- `TIME+`: 누적 CPU 시간
- `VIRT`: 작업과 연결된 전체 가상 주소 공간
- `RES`: 현재 작업에 귀속된 상주 비스왑 물리 메모리
- `SHR`: 다른 프로세스와 공유될 수 있는 상주 메모리

`VIRT`는 소비한 물리 RAM의 양이 아닙니다. 매핑된 파일, 공유 라이브러리, 예약된 주소 공간 및 스왑된 페이지를 포함할 수 있습니다. `RES`도 공유 페이지 때문에 귀속 방식이 복잡하므로 신중하게 해석해야 합니다.

:::single-choice{#top-res-versus-virt} 프로세스의 현재 상주 물리 메모리에 더 가까운 필드는 무엇입니까?

::option[`TIME+`]{#top-time-field explanation="이 필드는 메모리가 아니라 CPU 시간을 누적합니다."}
::option[`VIRT`]{#top-virt-field explanation="가상 크기에는 RAM에 상주하지 않아도 되는 주소 공간이 포함됩니다."}
::option[`RES`]{#top-res-field .correct explanation="상주 크기는 공유 관련 주의 사항이 있지만 현재 프로세스에 상주하는 물리 페이지를 반영합니다."}
:::

## 집중 및 정렬

알려진 PID를 직접 모니터링합니다.

```bash
$ top -p 1234,5678
```

일반적인 procps-ng 구현에서 `top` 안의 `P`는 CPU 순 정렬, `M`은 메모리 순 정렬, `1`은 CPU별 줄 전환, `q`는 종료입니다. 구현마다 키와 필드가 다를 수 있으므로 `h`를 눌러 로컬 대화형 도움말을 확인하십시오.

작업하기 전에 PID, 명령, 타임스탬프 및 여러 표본을 기록하십시오. 잠깐 목록 위로 올라온 프로세스는 정상일 수 있으며 종료하면 데이터 손실이나 서비스 중단이 생길 수 있습니다.

:::single-choice{#top-monitor-known-pid} 화면을 PID 1234로 제한하는 명령은 무엇입니까?

::option[`top -u 1234`]{#top-user-filter explanation="`-u` 형태는 값을 PID가 아니라 사용자로 취급하여 필터링합니다."}
::option[`top -d 1234`]{#top-delay-filter explanation="일반 구현에서 `-d` 옵션은 갱신 지연을 제어합니다."}
::option[`top -p 1234`]{#top-pid-filter .correct explanation="`-p` 옵션은 모니터링할 프로세스 ID 하나 이상을 선택합니다."}
:::

## 요약

이제 `top`을 사용해 시스템 성능 가설을 세우고 검증할 수 있습니다.

1. 부하 평균을 CPU 백분율이 아니라 시간 구간별 부하로 읽습니다.
2. 여러 표본에서 CPU 범주를 비교합니다.
3. 가상 주소 공간과 상주 메모리를 구분합니다.
4. 알려진 PID에 집중하고 작업 전에 증거를 검증합니다.
