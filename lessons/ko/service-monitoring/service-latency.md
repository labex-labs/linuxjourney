---
lesson_id: "service-latency"
course_id: "service-monitoring"
lang: "ko"
order_index: 4
title: "지연 시간"
description: "일반적인 요청 처리 시간과 가장 느린 요청의 처리 시간을 비교하는 방법을 알아봅니다."
meta_title: "지연 시간 - 서비스 모니터링"
meta_description: "일반적인 요청 처리 시간과 가장 느린 요청의 처리 시간을 비교하는 방법을 알아봅니다."
meta_keywords: "지연 시간, 서비스 모니터링, DevOps, Linux Journey"
---

**지연 시간**은 요청을 처리하는 데 걸리는 시간입니다. 숫자 하나로는 사용자마다 겪은 차이를 놓칠 수 있습니다. 같은 경로와 시간 구간에서 일반적인 요청과 느린 요청을 비교하세요.

## 작은 표본 읽기

아래 다섯 값의 단위는 밀리초입니다. 요청 네 건은 100밀리초 미만에 끝났고 한 건에는 2초가 걸렸습니다.

```text
40  50  60  70  2000
```

**중앙값**은 50번째 백분위수라고도 하며, 표본을 정렬했을 때 가운데에 놓이는 값입니다. 여기서는 60밀리초입니다. 가장 느린 요청에는 2,000밀리초가 걸렸습니다. 다섯 값의 합을 5로 나눈 평균은 444밀리초입니다.

:::single-choice{#service-latency-sample-median} 정렬된 이 표본에서 가운데 요청에 걸린 시간은 얼마인가요?

::option[444밀리초입니다.]{#service-latency-sample-median-a explanation="느린 요청의 값도 계산에 반영된 평균입니다."}
::option[60밀리초입니다.]{#service-latency-sample-median-b .correct explanation="정렬한 다섯 값 중 세 번째가 중앙값입니다."}
::option[2,000밀리초입니다.]{#service-latency-sample-median-c explanation="관찰한 값 중 가장 큰 값입니다."}
:::

## 느린 요청 살펴보기

**백분위수**는 관찰값을 크기순으로 나열했을 때 일정 비율에 해당하는 위치의 값입니다. 흔히 p95로 표시하는 95번째 백분위 지연 시간은 큰 표본에서 느린 쪽에 가까운 경곗값을 나타냅니다. 대시보드에서 사용하는 계산 기준을 일관되게 적용하세요. 표본이 너무 작으면 느린 쪽의 값을 안정적으로 추정하기 어렵습니다.

:::single-choice{#service-latency-slow-end} 중앙값은 거의 그대로인데 방문자들이 가끔 느려진다고 보고합니다. 어떤 정보를 보면 도움이 될까요?

::option[지연 시간이 긴 쪽의 분포와 요청 건수입니다.]{#service-latency-slow-end-a .correct explanation="가운데 값이 비슷하게 유지되어도 느린 응답에는 변화가 생길 수 있습니다."}
::option[중앙값만 다시 확인합니다.]{#service-latency-slow-end-b explanation="일부 방문에만 영향을 주는 변화를 놓칠 수 있습니다."}
::option[로그 파일의 전체 크기입니다.]{#service-latency-slow-end-c explanation="파일 크기는 요청에 걸린 시간을 보여 주지 않습니다."}
:::

## 비슷한 요청끼리 비교하기

트래픽이 비슷한 조건에서 같은 경로를 비교하세요. 다운로드에 간단한 상태 확인보다 오래 걸리는 것은 자연스럽습니다. 특히 느린 경로가 있다면 같은 시간 구간의 요청 로그와 의존 서비스 상태를 살펴보세요. 지표로 문제의 범위를 좁히고 다른 증거를 통해 원인을 조사합니다.

:::single-choice{#service-latency-compare-route} 같은 홈페이지가 릴리스 이후 느려졌는지 확인하려면 무엇을 비교해야 하나요?

::option[오늘의 홈페이지 응답과 지난달의 다운로드를 비교합니다.]{#service-latency-compare-route-a explanation="처리하는 작업과 시간대가 다르므로 결과를 해석하기 어렵습니다."}
::option[시간 구간에 대한 정보 없이 릴리스당 요청 한 건만 비교합니다.]{#service-latency-compare-route-b explanation="측정값 하나로는 요청 간의 차이를 알 수 없습니다."}
::option[릴리스 전후의 비슷한 시간 구간에서 홈페이지 지연 시간을 비교합니다.]{#service-latency-compare-route-c .correct explanation="요청 경로와 작업 부하가 비슷하면 변화를 해석하기 쉽습니다."}
:::

## 요약

이제 일반적인 요청과 느린 요청의 처리 시간을 함께 살펴볼 수 있습니다.

1. 정렬된 작은 표본에서 중앙값을 찾습니다.
2. 느린 쪽의 값과 요청 건수를 함께 봅니다.
3. 비슷한 요청을 비교한 뒤 차이의 원인을 조사합니다.
