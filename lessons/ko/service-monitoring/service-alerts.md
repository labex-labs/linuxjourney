---
lesson_id: "service-alerts"
course_id: "service-monitoring"
lang: "ko"
order_index: 6
title: "서비스 알림"
description: "알림의 조건, 집계 구간, 다음 조치를 파악하는 방법을 알아봅니다."
meta_title: "서비스 알림 - 서비스 모니터링"
meta_description: "알림의 조건, 집계 구간, 다음 조치를 파악하는 방법을 알아봅니다."
meta_keywords: "서비스 알림, 서비스 모니터링, DevOps, Linux Journey"
---

대시보드에서는 측정값을 볼 수 있습니다. **알림**은 대응이 필요할 수 있는 상태를 담당자에게 알려 줍니다. 알림을 읽고 무슨 일이 있었는지와 무엇을 확인해야 하는지 파악할 수 있어야 합니다.

## 알림 조건 읽기

5분 동안 홈페이지 요청의 5%를 초과하는 비율이 실패했는지 확인하는 규칙이 있다고 가정해 보세요. 이 서비스에 의미 있는 표본을 확보하기 위해 요청이 100건 이상이어야 한다는 조건도 있습니다.

```text
Window   09:10–09:15 UTC
Route    /
Requests 120
Failures 12
```

요청 120건 중 12건이 실패하면 실패율은 10%입니다. 규칙의 두 조건을 모두 충족합니다. 알림은 홈페이지에서 관찰한 요청 실패를 가리킵니다.

:::single-choice{#service-alerts-condition-match} 같은 규칙에서 요청 10건 중 1건이 실패하면 알림이 발생하나요?

::option[아니요. 최소 요청 건수를 충족하지 못했습니다.]{#service-alerts-condition-match-b .correct explanation="이 규칙에서는 실패율과 요청 건수가 모두 조건을 충족해야 합니다."}
::option[예. 오류율이 5%를 넘습니다.]{#service-alerts-condition-match-a explanation="이 규칙에서는 요청이 100건 이상이어야 합니다."}
::option[아니요. 10건 중 1건이 실패하면 오류율은 1%입니다.]{#service-alerts-condition-match-c explanation="10건 중 1건은 10%입니다. 다만 이 규칙을 적용하기에는 요청이 너무 적습니다."}
:::

## 집계 구간 확인하기

현재 대시보드가 정상으로 보여도 알림에 표시된 구간을 확인하세요. 이전에 발생한 상태를 알리는 것일 수 있습니다. 지표가 평소 범위로 돌아왔는지, 사용자가 주요 기능을 다시 이용할 수 있는지도 확인하세요.

:::single-choice{#service-alerts-alert-window} 09:16에 도착한 알림이 09:10부터 09:15까지의 상황을 설명합니다. 관련 오류를 어디에서 먼저 찾아야 하나요?

::option[지난주 보고서에서만 찾습니다.]{#service-alerts-alert-window-b explanation="지난주 보고서는 평소 수치를 파악하는 데 도움이 될 수 있지만 문제가 발생한 구간을 보여 주지는 않습니다."}
::option[09:16 이후에만 찾습니다.]{#service-alerts-alert-window-c explanation="알림이 전달되기까지 시간이 걸리므로 오류를 관찰한 구간이 더 앞설 수 있습니다."}
::option[알림에 기록된 집계 구간에서 찾습니다.]{#service-alerts-alert-window-a .correct explanation="이 구간의 오류를 집계해 규칙을 적용했기 때문입니다."}
:::

## 다음 조치 선택하기

홈페이지 요청 실패를 알리는 알림에는 해당 경로의 지표와 최근 로그를 볼 수 있는 링크를 넣을 수 있습니다. 사용자에게 어떤 영향이 있었는지 확인하고, 원인은 별도로 조사하세요. 서비스가 복구되었다면 같은 알림이 다시 발생했을 때 조사할 수 있도록 상황을 기록해 두세요.

:::single-choice{#service-alerts-next-check} 홈페이지에서 여전히 오류가 발생하는지 직접 확인하는 첫 조치는 무엇인가요?

::option[캐시에 있는 컨테이너 이미지를 모두 셉니다.]{#service-alerts-next-check-a explanation="알림은 실제 서비스에서 처리한 요청의 결과를 설명합니다."}
::option[문제가 발생한 경로로 승인된 테스트 요청을 보냅니다.]{#service-alerts-next-check-c .correct explanation="새 요청을 보내면 보고된 문제가 해당 경로에 여전히 영향을 주는지 확인할 수 있습니다."}
::option[알림이 뜨지 않도록 규칙을 끕니다.]{#service-alerts-next-check-b explanation="알림 설정만 바뀌고 서비스의 동작은 확인할 수 없습니다."}
:::

## 요약

이제 알림을 읽고 무엇을 확인할지 결정할 수 있습니다.

1. 측정 지표, 임계값, 최소 표본 크기를 확인합니다.
2. 알림의 집계 구간에 해당하는 증거를 찾습니다.
3. 사용자에게 나타난 증상을 적절한 검사로 확인합니다.
