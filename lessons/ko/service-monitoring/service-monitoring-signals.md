---
lesson_id: "service-monitoring-signals"
course_id: "service-monitoring"
lang: "ko"
order_index: 1
title: "모니터링 신호"
description: "웹 서비스에서 확인하려는 사항에 맞는 모니터링 신호를 고르는 방법을 알아봅니다."
meta_title: "모니터링 신호 - 서비스 모니터링"
meta_description: "웹 서비스에서 확인하려는 사항에 맞는 모니터링 신호를 고르는 방법을 알아봅니다."
meta_keywords: "모니터링 신호, 서비스 모니터링, DevOps, Linux Journey"
---

방문자가 페이지가 느리다고 말합니다. 먼저 방문자가 겪은 일을 파악하고 그 현상을 설명할 수 있는 측정값을 고르세요. 건수, 측정값, 기록한 이벤트처럼 관찰한 정보를 **신호**라고 합니다.

## 사용자 경험 확인하기

**가용성**은 서비스가 기대한 작업을 수행할 수 있는지를 나타냅니다. 예를 들어 홈페이지에 요청을 보내 정상 응답이 돌아오는지 확인할 수 있습니다. **지연 시간**은 요청이 끝나기까지 걸리는 시간입니다. 페이지가 정상적으로 열려도 몇 초가 걸릴 수 있습니다.

:::single-choice{#service-monitoring-signals-slow-page} 방문자에게 페이지가 표시되지만 몇 초가 걸립니다. 어떤 신호가 이 증상을 가장 직접적으로 설명하나요?

::option[서버의 컨테이너 수입니다.]{#service-monitoring-signals-slow-page-b explanation="컨테이너 수는 방문자가 기다리는 시간을 측정하지 않습니다."}
::option[페이지를 받는 데 걸리는 시간입니다.]{#service-monitoring-signals-slow-page-a .correct explanation="지연 시간은 요청에 걸린 시간을 나타냅니다."}
::option[소스 저장소의 바이트 수입니다.]{#service-monitoring-signals-slow-page-c explanation="저장소의 크기로는 요청에 걸린 시간을 알 수 없습니다."}
:::

## 요청과 오류 집계하기

**트래픽**은 분당 요청 수와 같이 서비스에 들어오는 작업량을 나타냅니다. 전체 요청 건수와 실패 건수를 함께 기록하세요. 1,000건 중 5건이 실패했을 때와 10건 중 5건이 실패했을 때는 의미가 다릅니다.

:::single-choice{#service-monitoring-signals-count-context} 두 시간 구간에서 각각 5건이 실패했습니다. 사용자에게 미친 영향을 비교하려면 무엇이 필요한가요?

::option[각 구간의 전체 요청 건수입니다.]{#service-monitoring-signals-count-context-b .correct explanation="오류율을 비교하려면 각 구간의 분모가 필요합니다."}
::option[대시보드의 이름입니다.]{#service-monitoring-signals-count-context-a explanation="이름을 보면 차트가 어디 있는지는 알 수 있지만 트래픽을 측정할 수는 없습니다."}
::option[목록에 표시된 서비스의 순서입니다.]{#service-monitoring-signals-count-context-c explanation="목록의 순서는 영향을 받은 요청의 수를 나타내지 않습니다."}
:::

## 리소스에 부하가 걸렸는지 확인하기

**포화도**는 리소스 사용량이 처리 한도에 얼마나 가까운지를 나타냅니다. 웹 프로세스가 실행 중이어도 데이터베이스의 처리를 기다리는 작업이 있을 수 있습니다. 결론을 내리기 전에 사용자에게 보이는 동작과 리소스 신호를 비교하세요.

:::single-choice{#service-monitoring-signals-saturation-check} 대기 중인 작업이 쌓이면서 요청 처리가 느려집니다. 다음에 무엇을 확인하면 좋을까요?

::option[대기 작업이 쌓인 것이 확실한 근본 원인이라고 판단합니다.]{#service-monitoring-signals-saturation-check-a explanation="두 변화는 조사의 단서입니다. 인과관계를 확인하려면 증거가 더 필요합니다."}
::option[호스트에 저장된 이미지를 다시 셉니다.]{#service-monitoring-signals-saturation-check-b explanation="이미지의 보관 여부로는 대기 중인 요청을 설명할 수 없습니다."}
::option[대기 중인 작업을 처리하는 리소스를 확인합니다.]{#service-monitoring-signals-saturation-check-c .correct explanation="해당 리소스가 들어오는 작업을 제때 처리하는지 확인할 수 있습니다."}
:::

## 요약

이제 사용자가 겪은 현상에 맞는 신호를 고를 수 있습니다.

1. 가용성과 지연 시간을 구분합니다.
2. 실패 건수를 전체 요청량과 함께 해석합니다.
3. 포화도를 처리 여유를 파악하는 단서로 삼습니다.
