---
lesson_id: "network-traffic-baselines"
course_id: "network-monitoring"
lang: "ko"
order_index: 5
title: "트래픽 기준선"
description: "변화를 이상 징후로 판단하기 전에 비슷한 조건의 트래픽 구간을 비교하는 방법을 알아봅니다."
meta_title: "트래픽 기준선 - 네트워크 모니터링"
meta_description: "변화를 이상 징후로 판단하기 전에 비슷한 조건의 트래픽 구간을 비교하는 방법을 알아봅니다."
meta_keywords: "트래픽 기준선, 네트워크 모니터링, 사이버 보안, Linux Journey"
---

**기준선**은 정해진 조건에서 평소에 관찰되는 동작을 나타냅니다. 트래픽을 모니터링할 때는 같은 서비스와 시간대에서 일반적으로 관찰하는 건수나 범위를 기준선으로 삼을 수 있습니다.

## 비교할 시간 구간 고르기

공개 페이지는 근무 시간에 더 많은 트래픽을 받을 수 있습니다. 변화를 감지하려면 평소 이용 패턴이 비슷한 구간끼리 비교하세요. 이 예시에서는 한 서비스에 들어온 요청을 5분 단위로 집계합니다.

```text
Window                 Requests
Typical weekdays 09:00  90–120
Today 09:00                230
Typical nights 02:00       2–8
```

요청 230건은 평일 아침의 일반적인 범위를 벗어납니다. 심야의 요청 범위와 비교하면 해석하기 어렵습니다.

:::single-choice{#network-traffic-baselines-baseline-fit} 오늘 09:00 구간을 비교하는 데 적합한 기준선은 어느 행인가요?

::option[평소 새벽 02:00의 수치입니다.]{#network-traffic-baselines-baseline-fit-b explanation="다른 트래픽 패턴을 보여 줍니다."}
::option[오늘 관찰한 요청 230건 자체입니다.]{#network-traffic-baselines-baseline-fit-c explanation="현재 건수 하나로 무엇이 바뀌었는지 알려면 비교 대상이 필요합니다."}
::option[평일 09:00의 일반적인 수치입니다.]{#network-traffic-baselines-baseline-fit-a .correct explanation="검토하는 서비스와 시간대가 일치합니다."}
:::

## 관련 상황 확인하기

배너로 알린 공지나 예약된 작업 때문에 트래픽이 달라질 수 있습니다. 더 조사할지 결정하기 전에 요청 경로와 시각, 승인된 변경 사항을 살펴보세요. 기준선은 무엇이 평소와 달라졌는지 보여 주고 조사할 실마리를 제공합니다.

:::single-choice{#network-traffic-baselines-baseline-explain} 예고한 출시 이후 트래픽이 두 배가 되었습니다. 무엇을 확인해야 하나요?

::option[이 차이를 계정이 침해되었다는 증거로 봅니다.]{#network-traffic-baselines-baseline-explain-a explanation="요청 건수만으로는 변화의 원인이나 계정에서 일어난 일을 알 수 없습니다."}
::option[요청 시각과 경로가 출시 후 예상한 패턴과 일치하는지 비교합니다.]{#network-traffic-baselines-baseline-explain-b .correct explanation="관련 관찰 결과로 가능성 있는 설명을 검증합니다."}
::option[출시만으로 모든 급증을 설명할 수 있으므로 변화를 무시합니다.]{#network-traffic-baselines-baseline-explain-c explanation="예상한 변화와 관련 없는 활동이 동시에 일어날 수 있습니다."}
:::

## 측정 범위 검토하기

수집기를 변경하면 실제 트래픽 변화 없이도 집계 건수가 달라질 수 있습니다. 어제부터 모니터링 범위에 새 네트워크를 추가했다면 각 구간에 어떤 트래픽이 포함되는지 확인하세요. 비교 결과와 함께 서비스, 관찰 지점, 시간, 단위를 기록합니다.

:::single-choice{#network-traffic-baselines-changed-coverage} 수집기에서 두 번째 사이트도 기록하기 시작했습니다. 다음 비교의 정확성을 높이려면 무엇을 해야 하나요?

::option[같은 사이트와 같은 출처 범위에서 수집한 건수를 비교합니다.]{#network-traffic-baselines-changed-coverage-c .correct explanation="범위를 일치시키면 트래픽이 바뀌었는지, 수집 범위가 바뀌었는지 구분하기 쉽습니다."}
::option[두 집계의 범위를 확인하지 않고 합계만 비교합니다.]{#network-traffic-baselines-changed-coverage-a explanation="수집 범위가 달라져 두 합계를 그대로 비교하기 어렵습니다."}
::option[시간 구간만 늘려 새 합계를 어제의 합계와 비교합니다.]{#network-traffic-baselines-changed-coverage-b explanation="구간을 늘려도 합계에 포함된 사이트와 출처를 맞추지 않으면 범위가 서로 다릅니다."}
:::

## 요약

이제 네트워크 트래픽을 비교할 때 기준선을 사용할 수 있는지 판단할 수 있습니다.

1. 서비스, 시간, 단위를 일치시킵니다.
2. 차이를 해석하기 전에 예상된 변경이 있었는지 확인합니다.
3. 수집 범위가 바뀌었는지 확인합니다.
