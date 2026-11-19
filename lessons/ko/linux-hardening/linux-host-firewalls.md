---
lesson_id: "linux-host-firewalls"
course_id: "linux-hardening"
lang: "ko"
order_index: 5
title: "호스트 방화벽"
description: "간단한 호스트 방화벽 정책을 읽고 관련 위치에서 수행할 검사를 계획하는 방법을 알아봅니다."
meta_title: "호스트 방화벽 - Linux 보안 강화"
meta_description: "간단한 호스트 방화벽 정책을 읽고 관련 위치에서 수행할 검사를 계획하는 방법을 알아봅니다."
meta_keywords: "호스트 방화벽, Linux 보안 강화, 사이버 보안, Linux Journey"
---

**호스트 방화벽**은 출발지 주소, 프로토콜, 목적지 포트 등에 따라 들어오는 네트워크 트래픽을 허용하거나 차단할 수 있습니다. 먼저 서비스에 필요한 트래픽을 정하세요.

## 예시 정책 읽기

아래는 호스트 하나에 적용한 간단한 정책입니다. `192.0.2.0/24`에서 슬래시 뒤의 값은 IPv4 주소 범위를 정합니다. 이 예시에서 `192.0.2.44`는 범위 안에 있고 `198.51.100.8`은 범위 밖에 있습니다.

```text
Allow TCP port 443 from any source.
Allow TCP port 22 from 192.0.2.0/24.
Deny other new inbound connections.
```

443번 포트는 공개 사이트에 사용합니다. 22번 포트는 유지보수 네트워크 전용입니다. 기본 정책은 두 허용 규칙에 해당하지 않는 연결을 어떻게 처리할지 정합니다.

:::single-choice{#linux-host-firewalls-match-trusted-network} 어떤 새 연결에 유지보수 규칙이 적용되나요?

::option[198.51.100.8에서 TCP 22번 포트로의 연결입니다.]{#linux-host-firewalls-match-trusted-network-b explanation="포트는 일치하지만 출발지가 관리 네트워크 밖에 있습니다."}
::option[192.0.2.44에서 TCP 443번 포트로의 연결입니다.]{#linux-host-firewalls-match-trusted-network-c explanation="이 연결에는 공개 웹 규칙이 적용됩니다."}
::option[192.0.2.44에서 TCP 22번 포트로의 연결입니다.]{#linux-host-firewalls-match-trusted-network-a .correct explanation="목적지 포트와 출발지 범위가 모두 일치합니다."}
:::

![공개 HTTPS와 제한된 유지보수 접근을 보여 주는 모의 호스트 방화벽 정책](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-host-firewalls/sample-policy.png)

## 방화벽 정책과 수신 소켓 확인하기

허용된 연결이라도 해당 포트에서 연결을 기다리는 프로그램이 없으면 실패할 수 있습니다. 프로그램이 정상적으로 연결을 기다리고 있어도 방화벽이 해당 경로를 차단하면 도달할 수 없습니다. 방화벽 정책과 수신 소켓을 각각 확인하세요.

:::single-choice{#linux-host-firewalls-allowed-but-failed} 규칙이 443번 포트를 허용하지만 호스트에 해당 포트의 수신 소켓이 없습니다. 무엇을 확인해야 하나요?

::option[클라이언트가 유지보수용 SSH를 사용해야 하는지 확인합니다.]{#linux-host-firewalls-allowed-but-failed-a explanation="SSH는 별개의 서비스입니다."}
::option[공개 웹 서비스가 예상한 포트에서 연결을 기다리는지 확인합니다.]{#linux-host-firewalls-allowed-but-failed-b .correct explanation="방화벽에서 포트를 허용해도 수신 소켓이 생기지는 않습니다."}
::option[요청이 유지보수 네트워크에서 왔는지 확인합니다.]{#linux-host-firewalls-allowed-but-failed-c explanation="이 예시에서 공개 웹 규칙은 모든 출발지를 허용합니다."}
:::

## 안전한 검증 계획 세우기

관리 절차에 따라 변경을 검토할 때는 승인된 유지보수 경로를 이용할 수 있는 상태로 두세요. 유지보수 네트워크에서 허용된 경로를 검사합니다. 그 네트워크 밖에 있는 승인된 위치에서는 연결이 차단되는지 확인합니다. 검사마다 출발지, 대상, 예상 결과를 기록하세요.

:::single-choice{#linux-host-firewalls-verification-pair} SSH 제한이 의도대로 적용되었는지 어떻게 확인하나요?

::option[유지보수 네트워크 안팎에서 각각 승인된 22번 포트 검사를 수행합니다.]{#linux-host-firewalls-verification-pair-c .correct explanation="이렇게 하면 정책의 허용과 차단을 모두 확인할 수 있습니다."}
::option[허용된 같은 장비에서 SSH 요청을 두 번 보냅니다.]{#linux-host-firewalls-verification-pair-a explanation="허용되는 경우만 두 번 확인하게 됩니다."}
::option[브라우저에서 공개 홈페이지에 두 번 요청을 보냅니다.]{#linux-host-firewalls-verification-pair-b explanation="이 요청은 공개 포트를 사용하므로 유지보수 접근을 검사할 수 없습니다."}
:::

## 요약

이제 호스트 방화벽 규칙을 서비스 상태와 함께 살펴볼 수 있습니다.

1. 규칙의 프로토콜, 목적지, 출발지를 확인합니다.
2. 허용된 서비스가 연결을 기다리고 있는지 확인합니다.
3. 기대하는 접근과 제한이 모두 적용되었는지 검증합니다.
