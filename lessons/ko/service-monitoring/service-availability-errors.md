---
lesson_id: "service-availability-errors"
course_id: "service-monitoring"
lang: "ko"
order_index: 3
title: "가용성과 오류"
description: "같은 시간 구간의 전체 요청 건수를 기준으로 요청 오류를 비교하는 방법을 알아봅니다."
meta_title: "가용성과 오류 - 서비스 모니터링"
meta_description: "같은 시간 구간의 전체 요청 건수를 기준으로 요청 오류를 비교하는 방법을 알아봅니다."
meta_keywords: "가용성과 오류, 서비스 모니터링, DevOps, Linux Journey"
---

대부분의 방문자에게 응답을 보내는 서비스에서도 일부 요청은 실패할 수 있습니다. 같은 시간 구간의 전체 요청 건수와 실패 건수를 사용해 관찰된 요청 중 실패한 비율을 구하세요.

## 오류율 계산하기

**오류율**은 실패한 요청 건수를 관찰한 전체 요청 건수로 나눈 값입니다. 여기에 100을 곱하면 백분율로 나타낼 수 있습니다.

```text
Window          Requests   Failures
09:00–09:05          100          2
09:05–09:10           20          2
```

첫 구간에서는 요청 100건 중 2건이 실패했으므로 오류율은 2%입니다. 다음 구간의 실패도 2건이지만 전체 요청은 20건이어서 오류율은 10%입니다.

:::single-choice{#service-availability-errors-compare-windows} 어느 구간의 실패 비율이 더 높았나요?

::option[09:05부터 09:10까지입니다.]{#service-availability-errors-compare-windows-b .correct explanation="20건 중 2건이 실패한 비율이 100건 중 2건이 실패한 비율보다 높습니다."}
::option[둘 다 2건씩 실패했으므로 비율이 같습니다.]{#service-availability-errors-compare-windows-a explanation="분모인 전체 요청 건수가 다릅니다."}
::option[트래픽이 더 많았던 09:00부터 09:05까지입니다.]{#service-availability-errors-compare-windows-c explanation="실패 건수가 같으면 전체 요청이 더 많을수록 실패 비율은 낮아집니다."}
:::

## 비교 범위 맞추기

시간 구간, 요청 경로, 실패의 정의를 함께 확인하세요. 상태 확인 엔드포인트는 정상적으로 응답하는데 의존 서비스가 필요한 페이지에서는 오류가 발생할 수 있습니다. 해당 페이지의 사용자 경험을 확인하려면 그 페이지에 대한 요청을 집계하세요.

:::single-choice{#service-availability-errors-route-scope} 상태 확인 엔드포인트는 항상 성공을 반환하지만 쇼핑객이 결제 페이지에서 오류를 보고합니다. 무엇을 살펴봐야 하나요?

::option[상태 확인 엔드포인트의 응답만 살펴봅니다.]{#service-availability-errors-route-scope-b explanation="그 응답은 별개의 동작에 관한 것입니다."}
::option[서비스 계정의 이름을 살펴봅니다.]{#service-availability-errors-route-scope-c explanation="계정 이름으로는 영향을 받은 요청 건수를 알 수 없습니다."}
::option[결제 요청과 그중 실패한 요청을 살펴봅니다.]{#service-availability-errors-route-scope-a .correct explanation="사용자가 보고한 문제는 결제 경로에서 발생했습니다."}
:::

## 트래픽이 적을 때 해석하기

요청 2건 중 1건이 실패하면 관찰된 오류율은 50%입니다. 이 수치는 해당 표본의 결과입니다. 요청이 적으면 비율이 크게 변할 수 있으므로 백분율 옆에 건수도 표시하세요. 요청이 0건이면 실제 트래픽의 오류율은 계산할 수 없습니다. 별도로 예약한 테스트를 실행하면 요청에 응답했는지 확인할 수 있습니다.

:::single-choice{#service-availability-errors-zero-traffic} 해당 구간에 방문자 요청이 없습니다. 방문자 요청의 오류율을 어떻게 보고해야 하나요?

::option[가용성이 완벽했다고 보고합니다.]{#service-availability-errors-zero-traffic-a explanation="그렇게 판단할 근거가 될 방문자 요청이 관찰되지 않았습니다."}
::option[해당 구간에 오류율을 계산할 요청 데이터가 없다고 보고합니다.]{#service-availability-errors-zero-traffic-c .correct explanation="서비스가 응답하는지 확인해야 한다면 별도의 테스트를 실행하세요."}
::option[오류율이 확실히 100%라고 보고합니다.]{#service-availability-errors-zero-traffic-b explanation="분모에 들어갈 관찰 요청이 한 건도 없습니다."}
:::

## 요약

이제 오류율과 함께 해석에 필요한 정보를 설명할 수 있습니다.

1. 같은 구간의 실패 건수와 전체 요청 건수를 비교합니다.
2. 확인할 내용에 맞게 요청 경로와 실패 기준을 정합니다.
3. 트래픽이 적을 때는 요청 건수도 함께 표시합니다.
