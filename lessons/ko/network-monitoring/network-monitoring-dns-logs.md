---
lesson_id: "network-monitoring-dns-logs"
course_id: "network-monitoring"
lang: "ko"
order_index: 3
title: "DNS 로그"
description: "DNS 질의, 응답, 이후의 애플리케이션 연결을 구분하는 방법을 알아봅니다."
meta_title: "DNS 로그 - 네트워크 모니터링"
meta_description: "DNS 질의, 응답, 이후의 애플리케이션 연결을 구분하는 방법을 알아봅니다."
meta_keywords: "DNS 로그, 네트워크 모니터링, 사이버 보안, Linux Journey"
---

클라이언트가 이름으로 서비스에 연결하려면 그 이름의 주소를 DNS에 물어볼 수 있습니다. **리졸버**는 클라이언트 대신 이름을 조회하는 구성 요소입니다. 리졸버는 질의와 결과를 기록할 수 있습니다.

## 질의 확인하기

DNS 기록에는 시각, 클라이언트 주소, 질의한 이름, 요청한 레코드 유형을 포함할 수 있습니다. `A` 질의는 IPv4 주소를 요청합니다.

```text
09:21:00Z client=192.0.2.10 query=site.example type=A result=NOERROR answer=192.0.2.20
09:21:03Z client=192.0.2.10 query=preview.example type=A result=NXDOMAIN
```

첫 번째 결과에는 `site.example`의 주소가 있습니다. 두 번째 결과는 이번 조회에서 DNS가 `preview.example`과 일치하는 이름을 찾지 못했다고 보고합니다.

:::single-choice{#network-monitoring-dns-logs-lookup-name} 요청한 이름의 IPv4 주소를 반환한 행은 무엇인가요?

::option[site.example을 조회한 행입니다.]{#network-monitoring-dns-logs-lookup-name-a .correct explanation="이 행의 응답에는 IPv4 주소가 들어 있습니다."}
::option[preview.example을 조회한 행입니다.]{#network-monitoring-dns-logs-lookup-name-b explanation="NXDOMAIN은 해당 조회 범위에 질의한 이름이 존재하지 않음을 나타냅니다."}
::option[클라이언트가 같으므로 두 행 모두 해당합니다.]{#network-monitoring-dns-logs-lookup-name-c explanation="클라이언트는 같지만 조회 결과는 다릅니다."}
:::

## 결과 읽기

`NOERROR`는 DNS 통신에서 프로토콜 오류가 보고되지 않았다는 뜻입니다. 응답 필드도 확인하세요. 응답 코드가 `NOERROR`여도 요청한 유형의 주소 레코드가 없을 수 있습니다. 조회 실패는 클라이언트가 기록한 시간 초과처럼 다른 결과로 나타나기도 합니다.

:::single-choice{#network-monitoring-dns-logs-no-answer} DNS 기록에 NOERROR가 있지만 응답에 주소가 없습니다. 무엇을 보고해야 하나요?

::option[클라이언트가 반드시 IPv4 주소를 받았습니다.]{#network-monitoring-dns-logs-no-answer-a explanation="이 예시에서 어떤 주소가 반환되었는지는 응답 필드에 나옵니다."}
::option[사이트에서 브라우저의 연결을 거부한 것이 확실합니다.]{#network-monitoring-dns-logs-no-answer-c explanation="이 행에는 DNS 결과가 기록되어 있습니다. 브라우저 요청은 별도로 확인해야 합니다."}
::option[프로토콜 오류 없이 응답이 돌아왔으며 이 행에는 주소가 없습니다.]{#network-monitoring-dns-logs-no-answer-b .correct explanation="결과 필드와 응답 필드에서 확인할 수 있는 정보는 서로 다릅니다."}
:::

## 이후 연결을 별도로 추적하기

클라이언트가 이름을 조회한 다음 연결을 시도할 수 있습니다. 실제로 연결했는지 확인하려면 일치하는 흐름이나 연결 기록을 찾아보세요. 엔드포인트와 시각을 비교합니다. DNS 결과를 캐시에 저장할 수 있으므로 일부 연결의 경우 남아 있는 로그에 새 조회가 표시되지 않습니다.

:::single-choice{#network-monitoring-dns-logs-dns-vs-flow} 클라이언트가 나중에 반환된 주소로 연결했음을 가장 잘 보여 주는 것은 무엇인가요?

::option[DNS 응답만 다른 화면에서 다시 확인합니다.]{#network-monitoring-dns-logs-dns-vs-flow-a explanation="DNS 응답에는 클라이언트가 사용할 수 있는 주소가 나옵니다."}
::option[목적지가 표시된 해당 연결 또는 흐름 기록을 확인합니다.]{#network-monitoring-dns-logs-dns-vs-flow-c .correct explanation="조회 후 발생한 트래픽을 별도로 추적할 수 있습니다."}
::option[같은 클라이언트의 두 번째 DNS 조회를 확인합니다.]{#network-monitoring-dns-logs-dns-vs-flow-b explanation="이름 조회가 반복되었음은 알 수 있지만 이후의 애플리케이션 연결은 확인할 수 없습니다."}
:::

## 요약

이제 DNS 로그와 이후 네트워크 활동을 구분할 수 있습니다.

1. 클라이언트, 질의한 이름, 요청한 레코드 유형을 찾습니다.
2. 결과 코드와 응답 내용을 함께 해석합니다.
3. 이후에 발생한 연결의 기록을 별도로 찾습니다.
