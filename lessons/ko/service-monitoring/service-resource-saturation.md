---
lesson_id: "service-resource-saturation"
course_id: "service-monitoring"
lang: "ko"
order_index: 5
title: "리소스 포화도"
description: "사용률과 대기열을 보며 서비스가 어디에서 처리 한도에 다다르는지 파악하는 방법을 알아봅니다."
meta_title: "리소스 포화도 - 서비스 모니터링"
meta_description: "사용률과 대기열을 보며 서비스가 어디에서 처리 한도에 다다르는지 파악하는 방법을 알아봅니다."
meta_keywords: "리소스 포화도, 서비스 모니터링, DevOps, Linux Journey"
---

서비스에 들어온 작업을 리소스가 곧바로 처리할 수 없으면 요청이 대기할 수 있습니다. 대기가 계속되면 대기열이 생기고 응답이 느려질 수 있습니다.

## 처리 용량과 작업량 살펴보기

**사용률**은 리소스가 얼마나 사용되고 있는지를 나타냅니다. 예를 들어 워커 풀에서 작업 네 개를 동시에 처리할 수 있다고 합시다. 워커 네 개가 모두 작업 중이라면 그 순간에는 여유가 없습니다. 새 작업이 들어오면 워커가 빌 때까지 대기열에서 기다릴 수 있습니다.

:::single-choice{#service-resource-saturation-worker-capacity} 워커 네 개가 모두 작업 중이고 작업 세 개가 대기 중입니다. 무엇을 알 수 있나요?

::option[정확히 일곱 개의 워커가 작업 중입니다.]{#service-resource-saturation-worker-capacity-b explanation="작업 세 개는 워커를 할당받기 위해 기다리고 있습니다."}
::option[모든 요청이 이미 실패했습니다.]{#service-resource-saturation-worker-capacity-c explanation="워커가 비면 대기 중인 작업을 마칠 수 있습니다."}
::option[모든 작업 슬롯이 사용 중이고 일부 작업이 기다리고 있습니다.]{#service-resource-saturation-worker-capacity-a .correct explanation="워커 수는 현재 사용량을, 대기열은 당장 처리할 수 없는 작업량을 보여 줍니다."}
:::

## 시간에 따른 변화 비교하기

잠깐 작업이 몰리는 상황과 여러 차례 관찰할 때 대기열이 계속 늘어나는 상황을 구분하세요. 같은 구간의 대기열, 요청 지연 시간, 트래픽을 비교합니다.

```text
Time   Busy workers   Queued jobs   Typical response
09:10       2 / 4           0             80 ms
09:11       4 / 4           5            300 ms
09:12       4 / 4          14            640 ms
```

이 예시에서는 워커가 모두 사용 중이고 대기열도 길어집니다. 완료되는 작업보다 들어오는 작업이 많다는 단서입니다. 워커가 처리 중인 작업을 확인하세요.

:::single-choice{#service-resource-saturation-sustained-pressure} 부하가 계속된다는 가장 뚜렷한 단서는 무엇인가요?

::option[09:10에 워커 두 개가 작업 중입니다.]{#service-resource-saturation-sustained-pressure-a explanation="해당 행에서는 처리 여유가 있었고 대기 중인 작업도 없었습니다."}
::option[워커가 계속 모두 사용 중이고 대기열은 길어집니다.]{#service-resource-saturation-sustained-pressure-b .correct explanation="모든 슬롯이 사용되는 동안 대기 작업이 누적되고 있습니다."}
::option[대기열이 비어 있는 동안 응답이 한 번 느려집니다.]{#service-resource-saturation-sustained-pressure-c explanation="응답이 한 번 느려져도 추가로 살펴볼 수 있습니다. 모든 슬롯이 사용된 상태에서 대기열이 계속 길어지면 부하가 지속된다는 근거가 더 강해집니다."}
:::

![사용률 100%와 길어지는 대기열을 보여 주는 모의 워커 지표](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/service-monitoring/service-resource-saturation/worker-queue.png)

## 원인 확인하기

요청이 더 빠르게 들어오거나 의존 서비스가 느려지거나 최근 변경으로 작업 하나에 더 오래 걸리면 워커가 계속 사용 중일 수 있습니다. 요청량, 처리 시간, 의존 서비스의 관찰 결과를 비교하세요. 신호를 추가로 확인하면 어떤 조치를 취할지 판단하는 데 도움이 됩니다.

:::single-choice{#service-resource-saturation-next-observation} 요청량은 그대로인데 작업 시간이 늘어났습니다. 대기열이 길어진 이유를 파악하려면 무엇을 확인하면 좋을까요?

::option[작업 소요 시간과 의존 서비스의 응답 시간을 함께 확인합니다.]{#service-resource-saturation-next-observation-c .correct explanation="작업이 슬롯을 더 오래 점유하게 된 이유를 좁힐 수 있습니다."}
::option[추가 증거를 수집하기 전에 처리 용량부터 바꿉니다.]{#service-resource-saturation-next-observation-a explanation="의존 서비스를 기다리는 작업은 처리 용량을 늘려도 해결되지 않을 수 있습니다."}
::option[저장소에 있는 역할의 수를 셉니다.]{#service-resource-saturation-next-observation-b explanation="역할의 수는 워커가 무엇을 기다리는지 보여 주지 않습니다."}
:::

## 요약

이제 리소스가 바쁜 상태와 대기 작업이 계속 쌓이는 상태를 구분할 수 있습니다.

1. 작업 중인 워커 수를 워커 풀의 용량과 비교합니다.
2. 시간에 따라 대기열과 요청 처리 결과가 어떻게 변하는지 비교합니다.
3. 처리 여유가 부족한 리소스에서 어떤 작업을 수행하는지 조사합니다.
