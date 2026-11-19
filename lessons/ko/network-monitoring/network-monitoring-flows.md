---
lesson_id: "network-monitoring-flows"
course_id: "network-monitoring"
lang: "ko"
order_index: 2
title: "네트워크 흐름"
description: "흐름 요약에서 주소, 포트, 시각, 바이트 수를 해석하는 방법을 알아봅니다."
meta_title: "네트워크 흐름 - 네트워크 모니터링"
meta_description: "흐름 요약에서 주소, 포트, 시각, 바이트 수를 해석하는 방법을 알아봅니다."
meta_keywords: "네트워크 흐름, 네트워크 모니터링, 사이버 보안, Linux Journey"
---

**흐름**은 네트워크 주소, 포트, 프로토콜 등의 속성을 공유하는 트래픽을 묶은 것입니다. 모니터링 시스템은 전체 내용을 저장하지 않고도 흐름에 포함된 바이트나 패킷의 수를 셀 수 있습니다.

## 양쪽 엔드포인트 확인하기

이 모의 요약에서 수집기는 출발지에서 목적지로 향하는 방향을 기록합니다. TCP 같은 전송 프로토콜에는 포트 번호가 포함됩니다. 받는 쪽에서 어느 포트가 연결을 기다리는지 이 번호로 파악할 수 있습니다.

```text
start=09:21:00Z protocol=TCP src=192.0.2.10:51600 dst=192.0.2.20:443 bytes=1800
start=09:21:00Z protocol=TCP src=192.0.2.20:443 dst=192.0.2.10:51600 bytes=8200
```

첫 번째 행은 443번 포트로 향하는 트래픽입니다. 두 번째 행은 반대 방향을 나타냅니다. 양방향을 함께 묶는 수집기도 있으므로 읽고 있는 기록의 형식을 확인하세요.

:::single-choice{#network-monitoring-flows-endpoint-direction} 첫 번째 행에서 기록된 트래픽을 받는 주소와 포트는 무엇인가요?

::option[192.0.2.10:51600입니다.]{#network-monitoring-flows-endpoint-direction-a explanation="첫 번째 방향에서 보내는 쪽의 엔드포인트입니다."}
::option[나열된 두 엔드포인트 모두 목적지입니다.]{#network-monitoring-flows-endpoint-direction-c explanation="이 예시에서 한 행에 기록된 방향은 하나입니다."}
::option[192.0.2.20:443입니다.]{#network-monitoring-flows-endpoint-direction-b .correct explanation="목적지 필드는 트래픽을 보낸 대상을 알려 줍니다."}
:::

## 전송량 비교하기

예시에서는 443번 포트에서 나가는 방향의 바이트 수가 더 많습니다. 웹 페이지의 응답이 더 큰 것은 정상일 수 있습니다. 전송량만으로 페이지의 내용, 계정, 전송량이 많아진 이유를 알 수는 없습니다.

:::single-choice{#network-monitoring-flows-byte-count} 두 번째 행의 8,200바이트는 무엇을 나타내나요?

::option[응답 메시지의 정확한 내용입니다.]{#network-monitoring-flows-byte-count-b explanation="흐름 요약에는 전송량이 나오며 메시지 내용은 생략됩니다."}
::option[그 방향에서 기록한 전송량입니다.]{#network-monitoring-flows-byte-count-a .correct explanation="바이트 수는 트래픽의 양을, 출발지와 목적지는 방향을 나타냅니다."}
::option[페이지가 정상적으로 열렸다는 확실한 증거입니다.]{#network-monitoring-flows-byte-count-c explanation="전송량으로는 HTTP 결과를 알 수 없습니다."}
:::

## 서비스와 시각 정보 더하기

서비스에 대해 알려진 정보와 시각을 바탕으로 관련 흐름을 골라내세요. 웹 서버가 무엇을 반환했는지 알아야 한다면 같은 시각과 연결에 해당하는 접근 로그가 있는지 확인하고 비교하세요.

:::single-choice{#network-monitoring-flows-next-source} 웹 요청의 HTTP 상태를 알고 싶습니다. 어떤 자료를 추가로 보면 좋을까요?

::option[해당 요청의 웹 접근 기록입니다.]{#network-monitoring-flows-next-source-c .correct explanation="서버의 접근 기록에 HTTP 결과가 나올 수 있습니다."}
::option[흐름의 바이트 수를 백 단위로 반올림한 값입니다.]{#network-monitoring-flows-next-source-a explanation="반올림해도 수치의 정밀도만 달라지고 응답 상태는 알 수 없습니다."}
::option[같은 엔드포인트의 두 번째 흐름 요약입니다.]{#network-monitoring-flows-next-source-b explanation="흐름 요약으로 트래픽에 관한 관찰을 더 확인할 수 있습니다. HTTP 응답 상태는 대개 들어 있지 않습니다."}
:::

## 요약

이제 흐름 요약의 주요 필드를 읽을 수 있습니다.

1. 엔드포인트의 주소와 포트를 찾습니다.
2. 기록된 방향을 기준으로 바이트 수를 해석합니다.
3. 애플리케이션의 결과가 중요할 때는 다른 출처를 선택합니다.
