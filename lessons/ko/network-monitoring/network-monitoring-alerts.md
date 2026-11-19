---
lesson_id: "network-monitoring-alerts"
course_id: "network-monitoring"
lang: "ko"
order_index: 6
title: "네트워크 알림"
description: "네트워크 알림을 다음 방어 조치의 판단에 필요한 증거와 연결하는 방법을 알아봅니다."
meta_title: "네트워크 알림 - 네트워크 모니터링"
meta_description: "네트워크 알림을 다음 방어 조치의 판단에 필요한 증거와 연결하는 방법을 알아봅니다."
meta_keywords: "네트워크 알림, 네트워크 모니터링, 사이버 보안, Linux Journey"
---

네트워크 알림은 모니터링 조건이 충족되었음을 알려 줍니다. 무슨 일이 있었는지 판단하기 전에 알림 조건과 데이터 출처를 읽으세요. 알림은 예상하지 못한 트래픽, 반복되는 실패, 수집되지 않은 관찰값 등을 나타낼 수 있습니다.

## 알림의 범위 읽기

아래 모의 알림은 DNS 기록에 기반합니다. 5분 동안 발생한 실패를 클라이언트별로 묶습니다.

```text
Window: 09:20–09:25 UTC
Client: 192.0.2.10
Condition: at least 10 failed name lookups
Observed: 12 failures
```

이 알림을 바탕으로 이름 조회와 그 결과를 살펴볼 수 있습니다. 어느 프로그램이 이름을 조회했는지는 따로 확인해야 합니다.

:::single-choice{#network-monitoring-alerts-alert-scope} 알림에서 직접 확인할 수 있는 사실은 무엇인가요?

::option[해당 구간에 기록된 클라이언트의 이름 조회가 12번 실패했습니다.]{#network-monitoring-alerts-alert-scope-b .correct explanation="알림에 표시된 건수와 관찰 범위입니다."}
::option[데이터 손실이 확인되었습니다.]{#network-monitoring-alerts-alert-scope-a explanation="이 규칙은 실패한 이름 조회의 횟수를 셉니다."}
::option[서로 다른 클라이언트 12대가 조회했습니다.]{#network-monitoring-alerts-alert-scope-c explanation="알림은 클라이언트 주소 하나에 대한 기록을 묶습니다."}
:::

## 관련 호스트 기록 찾기

실패 대부분이 `preview.example` 조회에서 발생했다고 가정해 보세요. 클라이언트의 서비스 로그를 보면 오래된 설정 때문에 재시도가 반복되었음을 알 수도 있습니다. 요청을 보냈을 것으로 예상되는 프로그램의 같은 시간대 기록을 찾으세요. 어느 호스트의 활동인지 판단하기 전에 모니터링에 표시된 호스트 이름을 확인하세요.

:::single-choice{#network-monitoring-alerts-evidence-choice} 서비스 하나가 조회를 재시도했는지 확인하는 데 어떤 기록이 도움이 되나요?

::option[나중에 다른 호스트에서 공개 페이지를 열었다는 기록입니다.]{#network-monitoring-alerts-evidence-choice-b explanation="접속 대상과 시간이 조사하는 패턴과 다릅니다."}
::option[활동 시각이 없는 설치 앱 목록입니다.]{#network-monitoring-alerts-evidence-choice-c explanation="설치된 소프트웨어 목록만으로는 어떤 프로그램이 조회했는지 알 수 없습니다."}
::option[알림 구간에 실패한 조회가 기록된 해당 서비스의 로그입니다.]{#network-monitoring-alerts-evidence-choice-a .correct explanation="조회 패턴을 그 프로그램과 연결할 수 있습니다."}
:::

## 다음 판단을 기록하기

서비스 로그가 일치하면 원인을 기록하고 승인된 설정을 바로잡은 뒤 대표적인 조회를 검증하세요. 증거가 충분하지 않다면 어떤 정보가 빠졌는지 적으세요. 알림, 근거 기록, 검사 결과를 함께 보관합니다.

:::single-choice{#network-monitoring-alerts-uncertainty} DNS 알림은 있지만 알림에 대응하는 호스트 기록은 없습니다. 무엇을 보고해야 하나요?

::option[어느 프로그램인지 정확히 식별했습니다.]{#network-monitoring-alerts-uncertainty-a explanation="DNS 증거만으로는 프로세스를 식별하지 못했습니다."}
::option[조회 패턴은 확인했으며 어느 프로그램이 조회했는지는 모릅니다.]{#network-monitoring-alerts-uncertainty-c .correct explanation="관찰한 사실과 여전히 확인해야 할 부분을 모두 남깁니다."}
::option[알림에서는 아무것도 알 수 없습니다.]{#network-monitoring-alerts-uncertainty-b explanation="알림은 리졸버에서 관찰한 조건을 보여 줍니다."}
:::

## 예정된 재시도 패턴 확인하기

팀이 테스트용 호스트 이름의 주소를 반복 조회하는 작업을 예약했다고 가정해 보세요. 예약 시각, DNS 기록의 이름, 작업 자체의 로그를 비교하세요. 여러 필드가 일치하면 그 작업이 원인이라는 설명을 뒷받침할 수 있습니다. 일치하지 않는 실패는 계속 검토하세요.

:::single-choice{#network-monitoring-alerts-final-application} 예약 작업으로 설명할 수 있다는 가장 확실한 근거는 무엇인가요?

::option[다른 예약 작업도 실행하는 호스트에서 알림이 발생했습니다.]{#network-monitoring-alerts-final-application-c explanation="호스트 정보만으로는 어떤 프로그램이 조회했는지 알 수 없습니다."}
::option[작업 로그에 같은 호스트 이름과 알림 구간의 재시도가 나옵니다.]{#network-monitoring-alerts-final-application-a .correct explanation="이름과 시각이 일치하면 관찰한 패턴을 해당 작업과 연결할 근거가 됩니다."}
::option[작업이 그날 중 어느 시각에 예약되어 있었습니다.]{#network-monitoring-alerts-final-application-b explanation="대략적인 날짜만으로는 알림 구간과 조회한 이름을 확인할 수 없습니다."}
:::

## 요약

이제 네트워크 알림을 바탕으로 다음에 확인할 사항을 구체적으로 정할 수 있습니다.

1. 탐지 규칙과 그 범위를 파악합니다.
2. 가능한 설명을 검증할 관련 기록을 고릅니다.
3. 관찰 결과와 아직 모르는 부분을 기록합니다.
