---
lesson_id: "io-monitoring"
course_id: "process-utilization"
lang: "ko"
order_index: 5
title: "I/O 모니터링"
description: "iostat 표본으로 CPU 및 블록 장치 활동을 조사하는 방법을 알아봅니다."
meta_title: "I/O 모니터링 - 프로세스 사용량"
meta_description: "iostat 명령으로 리눅스 I/O를 모니터링하는 방법을 알아봅니다. CPU와 디스크 사용 지표를 분석하고 지연, 대기열 및 사용률을 해석합니다."
meta_keywords: "I/O 모니터링, iostat, 리눅스 I/O 모니터링, CPU 사용량, 디스크 사용량, 시스템 성능, iowait"
---

일반적으로 `sysstat` 패키지가 제공하는 `iostat`은 CPU와 블록 장치 활동을 보고합니다. 반복 표본을 애플리케이션 지연과 함께 사용하십시오. 처리량이나 사용률만으로 저장 장치가 사용자에게 보이는 문제의 원인임을 확정할 수 없습니다.

## 유용한 표본 수집하기

1초 간격으로 확장 장치 통계를 실행합니다.

```bash
$ iostat -xz 1
```

일반적인 구현에서 첫 보고서는 부팅 이후의 평균을 포함하고 이후 보고서는 각 구간을 다룹니다. `-x` 옵션은 확장 필드를 추가하고 `-z`는 비활성 장치를 숨깁니다. 정상 구간과 문제 구간을 포착하도록 여러 구간을 관찰하십시오.

:::single-choice{#iostat-first-report}
첫 번째 `iostat` 보고서는 일반적으로 무엇을 나타냅니까?

::option[명령의 마지막 1초 동안의 작업만 나타냅니다.]{#iostat-final-second explanation="초기 누적 보고서를 설명하지 않습니다."}
::option[시스템 부팅 이후의 활동 평균입니다.]{#iostat-since-boot .correct explanation="이후 보고서는 일반적으로 구간별이므로 첫 보고서는 별도로 해석해야 합니다."}
::option[내일의 장치 사용률 예측입니다.]{#iostat-forecast explanation="이 도구는 미래 수요가 아니라 관찰된 통계를 보고합니다."}
:::

## CPU 필드 읽기

CPU 섹션에는 일반적으로 사용자(`%user`), 시스템(`%system`), 유휴(`%idle`), 입출력 대기(`%iowait`) 및 가상 머신 스틸(`%steal`) 시간이 포함됩니다. 입출력 대기는 처리되지 않은 입출력 요청이 있는 동안의 CPU 유휴 시간이며 디스크가 바쁜 시간의 백분율이 아닙니다.

:::single-choice{#iostat-iowait-meaning}
`%iowait`가 설명하는 것은 무엇입니까?

::option[이미 채워진 디스크 용량의 백분율입니다.]{#iostat-capacity explanation="파일 시스템 용량과 CPU 시간은 서로 다른 측정값입니다."}
::option[처리되지 않은 입출력 요청이 있는 동안의 CPU 유휴 시간입니다.]{#iostat-iowait-cpu .correct explanation="CPU 시간 범주이므로 그 자체로 장치를 식별할 수 없습니다."}
::option[삭제를 기다리는 파일 수입니다.]{#iostat-delete-queue explanation="파일 삭제 수는 이 필드에 표현되지 않습니다."}
:::

## 장치 필드 읽기

필드 이름은 sysstat 버전에 따라 다르지만 유용한 개념은 다음과 같습니다.

- 초당 읽기 및 쓰기 작업이나 데이터는 작업 부하 속도를 표시
- `await`는 대기열 및 서비스 시간을 포함한 평균 요청 지연을 보고
- 평균 대기열 크기 필드는 기다리거나 처리 중인 요청을 표시
- `%util`은 경과 시간 중 장치에서 입출력이 진행 중이었던 백분율을 보고

단순한 직렬 장치에서 높은 `%util`은 포화를 나타낼 수 있지만 병렬 저장 장치, 배열 또는 가상 장치의 성능 용량으로 직접 변환되지는 않습니다. 지연을 장치 설계, 작업 부하 패턴 및 서비스 목표와 비교하십시오.

:::single-choice{#iostat-await-purpose}
평균 입출력 요청 지연과 가장 직접적으로 관련된 필드는 무엇입니까?

::option[장치 이름입니다.]{#iostat-device-name explanation="이름은 장치를 식별하지만 요청 시간을 측정하지 않습니다."}
::option[`await`]{#iostat-await .correct explanation="await는 대기열 및 서비스 시간을 포함한 요청의 평균 시간을 반영합니다."}
::option[`%idle`]{#iostat-idle explanation="장치 요청 지연이 아니라 CPU 필드입니다."}
:::

## 증거 연결하기

결론을 내리기 전에 장치 이름을 마운트 및 기반 장치에 매핑합니다.

```bash
$ lsblk -o NAME,TYPE,SIZE,FSTYPE,MOUNTPOINTS
$ findmnt
```

그런 다음 `iostat` 구간을 애플리케이션 응답 시간, 데이터베이스 또는 파일 시스템 지표 및 프로세스 수준 입출력과 연결합니다. 장치 매퍼, RAID, 컨테이너 및 네트워크 기반 저장 장치는 고유 도구가 필요한 계층을 추가할 수 있습니다.

:::single-choice{#iostat-high-util-conclusion}
장치에서 높은 `%util`을 본 뒤 무엇을 해야 합니까?

::option[모든 파일 시스템에 여유 공간이 없다고 가정합니다.]{#iostat-assume-full explanation="바쁜 시간은 파일 시스템 용량을 보고하지 않습니다."}
::option[마운트된 작업 부하를 식별하기 전에 파일을 삭제합니다.]{#iostat-delete-first explanation="삭제는 입출력 병목을 증명하는 것과 관련 없는 상태 변경 작업입니다."}
::option[지연과 작업 부하 동작을 저장 장치 설계와 연결합니다.]{#iostat-correlate .correct explanation="장치 병렬성과 작업 부하 목표에 따라 관찰 결과가 해로운지 결정됩니다."}
:::

## 요약

이제 `iostat`을 입출력 조사의 증거로 사용할 수 있습니다.

1. 확장 통계 구간을 여러 번 수집합니다.
2. CPU 입출력 대기와 장치 바쁜 시간을 구분합니다.
3. 지연, 대기열, 처리량 및 사용률을 함께 해석합니다.
4. 장치를 작업 부하에 매핑하고 애플리케이션 영향을 검증합니다.
