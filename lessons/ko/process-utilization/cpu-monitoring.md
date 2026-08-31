---
lesson_id: "cpu-monitoring"
course_id: "process-utilization"
lang: "ko"
order_index: 4
title: "CPU 모니터링"
description: "리눅스 부하 평균을 CPU 수, 사용률 및 작업 상태와 함께 해석하는 방법을 알아봅니다."
meta_title: "CPU 모니터링 - 프로세스 사용량"
meta_description: "uptime 명령을 이용한 리눅스 CPU 모니터링의 기초를 알아봅니다. 부하 평균, 프로세스 사용량 및 시스템 성능을 해석하는 방법을 설명합니다."
meta_keywords: "uptime 명령어, 리눅스 CPU 모니터링, 부하 평균, 시스템 성능, 프로세스 사용량, 리눅스 튜토리얼"
---

CPU 문제 해결은 부하, 사용률 및 응답성을 구분하는 데서 시작합니다. 숫자 하나로 병목이 확정되지는 않으므로 여러 시간 구간을 비교하고 호스트 지표를 사용자가 실제로 경험하는 작업 부하와 연결하십시오.

## uptime 읽기

`uptime`은 간결한 시작점을 제공합니다.

```text
$ uptime
 17:23:35 up 1 day, 5:59, 2 users, load average: 0.00, 0.02, 0.05
```

마지막 세 값은 약 1분, 5분 및 15분의 부하 평균입니다. 서로 비교하면 방향을 알 수 있습니다. 1분 값이 훨씬 크면 부하가 증가 중일 수 있고 15분 값이 더 크면 부하가 감소 중일 수 있습니다.

:::single-choice{#cpu-uptime-windows}
`uptime`은 부하 평균 시간 구간을 어떤 순서로 표시합니까?

::option[15초, 5초 및 1초입니다.]{#cpu-windows-seconds explanation="값은 분 단위 평균이며 가장 긴 구간부터 출력하지 않습니다."}
::option[1분, 5분 및 15분입니다.]{#cpu-windows-one-five-fifteen .correct explanation="가장 짧은 최근 구간이 먼저, 가장 긴 구간이 마지막에 나타납니다."}
::option[현재, 최소 및 최대 CPU 백분율입니다.]{#cpu-windows-percentages explanation="부하 평균은 최소 또는 최대 CPU 백분율이 아닙니다."}
:::

## 리눅스 부하 이해하기

리눅스 부하 평균은 CPU를 사용하거나 기다리는 작업을 포함한 실행 가능 작업과, 일반적으로 입출력과 관련된 인터럽트 불가 대기 상태의 작업을 셉니다. 따라서 CPU 사용률과 같지 않습니다.

부하 `4.0`은 논리 CPU가 하나인 시스템과 16개인 시스템에서 의미가 다릅니다. 시스템이 사용할 수 있는 처리 단위 수를 확인합니다.

```bash
$ nproc
```

CPU 할당량, 선호도, 가상화 및 컨테이너 제한 때문에 특정 작업 부하에 보이는 용량이 줄어들 수 있으므로 호스트 CPU 수는 시작점일 뿐입니다.

:::single-choice{#cpu-load-not-percentage}
부하 평균이 CPU 사용률 백분율이 아닌 이유는 무엇입니까?

::option[CPU 클록 주파수만 보고하기 때문입니다.]{#cpu-load-clock explanation="클록 속도는 별도의 하드웨어 또는 스케일링 지표입니다."}
::option[여유 물리 메모리만 측정하기 때문입니다.]{#cpu-load-memory explanation="메모리 가용성은 다른 지표가 보고합니다."}
::option[실행 가능한 작업과 인터럽트 불가 대기 작업을 포함하기 때문입니다.]{#cpu-load-task-count .correct explanation="부하는 경과한 CPU 시간의 백분율이 아니라 작업 수요와 대기 상태를 기반으로 합니다."}
:::

## 부하와 CPU 활동 비교하기

출력 하나에 의존하지 말고 여러 표본을 수집합니다. 유용한 보조 도구는 다음과 같습니다.

```bash
$ top
$ vmstat 1
$ mpstat -P ALL 1
```

`top`은 호스트 및 프로세스 뷰를 결합합니다. `vmstat`은 CPU 범주와 함께 실행 가능 및 차단된 작업 수를 보여 줍니다. 여러 배포판에서 `sysstat`이 제공하는 `mpstat`은 CPU별 활동을 보여 줍니다. 가용성과 정확한 필드는 다르므로 로컬 설명서를 사용하십시오.

높은 부하와 바쁜 CPU가 함께 보이면 CPU 수요를 나타낼 수 있습니다. 높은 부하와 눈에 띄는 차단 작업, 입출력 지연 또는 입출력 대기 관찰이 함께 보이면 다른 리소스가 제한됐을 수 있습니다. 낮은 평균 사용률도 포화된 CPU 하나나 짧은 지연 급증을 숨길 수 있습니다.

:::single-choice{#cpu-high-load-next-step}
높은 부하 평균을 관찰한 뒤 가장 좋은 다음 단계는 무엇입니까?

::option[CPU, 작업 상태, 입출력 및 작업 부하 측정값을 반복 수집해 비교합니다.]{#cpu-load-correlate .correct explanation="서로 연결된 표본은 부하에 대한 여러 경쟁 가설을 구분합니다."}
::option[다른 데이터를 수집하지 않고 즉시 재부팅합니다.]{#cpu-load-reboot explanation="재부팅은 증거를 없애고 원인을 식별하지 못한 채 서비스를 중단할 수 있습니다."}
::option[모든 CPU가 완전히 사용 중이라고 가정합니다.]{#cpu-load-assume explanation="부하에는 인터럽트 불가 작업이 포함될 수 있고 CPU별로 고르지 않을 수 있습니다."}
:::

## 용량과 영향 평가하기

부하가 항상 CPU 수보다 낮아야 한다는 보편적인 규칙은 없습니다. 일괄 처리 시스템은 대기열을 허용할 수 있지만 대화형 서비스는 그 이전에 지연 목표를 위반할 수 있습니다. 같은 호스트와 작업 부하의 기준선을 수립한 뒤 응답 시간, 처리량, 오류율, 포화도 및 리소스 사용을 비교하십시오.

:::single-choice{#cpu-capacity-threshold}
관찰된 부하가 허용 가능한지 결정하는 기준은 무엇입니까?

::option[값이 항상 1보다 낮아야 한다는 요구 사항입니다.]{#cpu-below-one explanation="다중 코어 용량과 작업 부하 목표 때문에 이 고정 임계값은 신뢰하기 어렵습니다."}
::option[`uptime`에 표시된 사용자 수만 사용합니다.]{#cpu-user-count explanation="로그인한 셸 사용자가 모든 작업 부하 수요를 나타내지는 않습니다."}
::option[작업 부하의 기준선과 서비스 목표입니다.]{#cpu-baseline-objectives .correct explanation="허용 여부는 보편적인 임계값이 아니라 예상 동작과 사용자에게 보이는 성능에 따라 달라집니다."}
:::

## 요약

이제 부하 평균을 CPU 조사의 한 부분으로 해석할 수 있습니다.

1. 1분, 5분 및 15분 부하 구간을 읽습니다.
2. 작업 부하와 CPU 시간 백분율을 구분합니다.
3. 부하를 사용 가능한 처리 용량과 비교합니다.
4. 반복된 호스트 측정값을 서비스 결과와 연결합니다.
