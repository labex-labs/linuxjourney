---
lesson_id: "memory-monitoring"
course_id: "process-utilization"
lang: "ko"
order_index: 6
title: "메모리 모니터링"
description: "vmstat의 메모리, 페이징, 프로세스, I/O 및 CPU 표본을 해석하는 방법을 알아봅니다."
meta_title: "메모리 모니터링 - 프로세스 사용량"
meta_description: "vmstat 명령으로 리눅스 메모리를 모니터링하는 방법을 알아봅니다. 메모리 사용량과 시스템 성능 지표를 함께 분석하는 방법을 설명합니다."
meta_keywords: "메모리 모니터링, 메모리 사용량, vmstat, 리눅스 메모리, 시스템 성능, 리눅스 튜토리얼"
---

리눅스는 사용하지 않는 메모리를 의도적으로 캐시에 사용하므로 `free` 값이 작다는 사실만으로 메모리 압력이 증명되지는 않습니다. `vmstat`은 메모리를 실행 가능 작업, 페이징, 입출력 및 CPU 활동과 연결하는 데 도움을 줍니다.

## vmstat로 표본 수집하기

1초마다 표본 하나를 수집합니다.

```bash
$ vmstat 1
```

첫 데이터 행은 일반적으로 부팅 이후의 평균을 보고하고 이후 행은 각 구간을 다룹니다. 대표 기간을 포착한 뒤 `Ctrl-C`로 중지합니다. 단위와 사용 가능한 필드는 다르므로 `vmstat --unit`과 로컬 설명서를 확인하십시오.

:::single-choice{#vmstat-interval-rows}
`vmstat 1`에서 초 단위 변화를 관찰하기에 가장 적합한 행은 무엇입니까?

::option[초기 보고서 뒤의 이후 행입니다.]{#vmstat-later-rows .correct explanation="이후 행은 누적 기간이 아니라 요청한 각 구간을 설명합니다."}
::option[첫 데이터 행 위의 제목만 사용합니다.]{#vmstat-headings explanation="제목은 필드를 정의하지만 활동 표본은 포함하지 않습니다."}
::option[다른 호스트에서 복사한 행만 사용합니다.]{#vmstat-other-host explanation="다른 시스템은 현재 작업 부하를 나타내지 않습니다."}
:::

## 프로세스와 메모리

일반적인 프로세스 필드는 실행 가능 작업을 뜻하는 `r`과 인터럽트 불가 대기 상태로 차단된 작업을 뜻하는 `b`입니다. 메모리 필드에는 사용 중인 스왑(`swpd`), 유휴 메모리(`free`), 버퍼(`buff`) 및 캐시(`cache`)가 있습니다. 이 값들은 프로세스별 사용량이 아니라 시스템 전체 값입니다.

현재 사용 가능한 메모리를 더 쉽게 보려면 다음과 비교합니다.

```bash
$ free -h
```

회수 가능한 캐시가 새 할당을 충족할 수 있으므로 일반적으로 `available` 추정값이 `free` 하나보다 더 유용합니다.

:::single-choice{#vmstat-free-memory}
리눅스에서 `free` 값이 낮아도 정상일 수 있는 이유는 무엇입니까?

::option[이 값이 항상 전체 물리 RAM을 제외하기 때문입니다.]{#vmstat-excludes-ram explanation="메모리 필드이며 정확한 단위는 확인해야 합니다."}
::option[커널이 유휴 메모리를 회수 가능한 캐시에 사용할 수 있기 때문입니다.]{#vmstat-reclaimable-cache .correct explanation="애플리케이션에 필요할 때 캐시 메모리를 회수할 수 있는 경우가 많습니다."}
::option[낮은 여유 메모리가 CPU 전원이 꺼졌음을 증명하기 때문입니다.]{#vmstat-cpu-off explanation="메모리 할당과 CPU 전원 상태는 관련 없는 결론입니다."}
:::

## 페이징과 I/O

`si`와 `so`는 스왑 인 및 스왑 아웃 비율을 보여 줍니다. 지속적인 페이징이 지연 및 메모리 회수 활동과 함께 나타나면 압력을 나타낼 수 있지만 0이 아닌 스왑 사용량(`swpd`) 자체는 현재 문제를 증명하지 않습니다. `bi`와 `bo`는 블록 입력 및 출력 비율을 보고하며 스왑 트래픽에만 한정되지 않습니다.

:::single-choice{#vmstat-swap-pressure}
현재 메모리 압력 진단을 더 잘 뒷받침하는 증거는 무엇입니까?

::option[다른 관찰 없이 `swpd` 값이 0보다 큽니다.]{#vmstat-swpd-alone explanation="이전 압력 후에도 페이지가 스왑에 남을 수 있으므로 양만으로는 충분하지 않습니다."}
::option[지속적인 페이징이 회수 활동 및 작업 부하 지연과 함께 나타납니다.]{#vmstat-correlated-pressure .correct explanation="반복되고 연결된 증거가 메모리 동작을 현재 영향과 연결합니다."}
::option[로그인할 때 출력된 호스트 이름입니다.]{#vmstat-hostname explanation="호스트 이름은 회수나 페이징 활동을 측정하지 않습니다."}
:::

## CPU와 시스템 활동

CPU 열에는 일반적으로 사용자(`us`), 시스템(`sy`), 유휴(`id`), 입출력 대기(`wa`) 및 스틸(`st`) 백분율이 있습니다. 시스템 열에는 초당 인터럽트(`in`)와 컨텍스트 전환(`cs`)이 있습니다. 기준선과 비교해 급증을 해석하십시오. 높은 컨텍스트 전환 비율이 일부 작업 부하에서는 정상일 수 있습니다.

:::single-choice{#vmstat-r-column}
`r` 프로세스 필드는 무엇을 나타냅니까?

::option[읽기 전용으로 마운트된 파일 시스템입니다.]{#vmstat-readonly explanation="파일 시스템 마운트 플래그는 프로세스 필드에 표현되지 않습니다."}
::option[활성 셸이 있는 원격 사용자입니다.]{#vmstat-remote-users explanation="로그인 세션은 다른 도구가 보고합니다."}
::option[실행 가능하거나 CPU를 기다리는 작업입니다.]{#vmstat-runnable .correct explanation="이 수를 CPU 용량과 비교하면 CPU 수요를 식별하는 데 도움을 줄 수 있습니다."}
:::

## 요약

이제 `vmstat`을 시간에 따라 연결된 시스템 뷰로 해석할 수 있습니다.

1. 초기 누적 보고서와 구간 표본을 구분합니다.
2. 캐시를 회수 가능한 메모리로 취급합니다.
3. 페이징을 회수 및 애플리케이션 영향과 연결합니다.
4. 프로세스, 입출력, 시스템 및 CPU 필드를 함께 읽습니다.
