---
lesson_id: "bgp-border-gateway-protocol"
course_id: "routing"
lang: "ko"
order_index: 7
title: "Border Gateway Protocol"
description: "BGP가 자율 시스템 사이와 내부에서 정책으로 제어된 IP 연결 가능성을 교환하는 방법을 알아봅니다."
meta_title: "Border Gateway Protocol - 라우팅"
meta_description: "인터넷 라우팅의 핵심 프로토콜인 BGP의 기초를 살펴봅니다. 자율 시스템 간 통신과 BGP 라우팅 원리를 설명합니다."
meta_keywords: "BGP, Border Gateway Protocol, 인터넷 라우팅, 자율 시스템, 리눅스 네트워킹, 네트워크 프로토콜"
---

BGP(Border Gateway Protocol)는 인터넷의 경로 벡터 라우팅 프로토콜입니다. IP 접두사 연결 가능성과 경로 속성을 교환해 네트워크가 물리적 거리만으로 경로를 선택하지 않고 관리 정책을 적용하도록 합니다.

## 자율 시스템과 세션

자율 시스템은 하나의 라우팅 관리 아래 있는 네트워크 집합이며 BGP에서는 자율 시스템 번호로 식별합니다. 외부 BGP는 자율 시스템 사이에서 경로를 교환하고, 내부 BGP는 하나의 AS 안에서 BGP 연결 가능성을 배포합니다.

BGP 피어는 TCP 포트 179를 통해 세션을 수립합니다. 작동하는 TCP 세션은 전송 기반일 뿐이며 BGP 기능, 정책 및 경로 교환도 성공해야 합니다.

:::single-choice{#bgp-external-session}
외부 BGP는 무엇을 교환합니까?

::option[하나의 스위치 안에서 Ethernet 프레임 체크섬을 교환합니다.]{#bgp-ethernet-fcs explanation="BGP는 TCP 위에서 작동하며 네트워크 계층 연결 가능성을 교환합니다."}
::option[웹 브라우저 사이에서 사용자 암호를 교환합니다.]{#bgp-browser-passwords explanation="응용 자격 증명은 라우팅 속성이 아닙니다."}
::option[자율 시스템 사이에서 연결 가능성과 경로 정보를 교환합니다.]{#bgp-between-as .correct explanation="eBGP는 서로 다른 라우팅 관리를 연결하고 도메인 간 정책을 적용합니다."}
:::

## 경로 벡터 정보

광고에는 접두사와 속성이 포함됩니다. `AS_PATH`는 통과한 자율 시스템을 나열해 루프 감지에 도움을 줍니다. 그 밖의 일반적인 속성에는 `LOCAL_PREF`, `MED`, origin, next hop 및 community가 있습니다. 속성의 효과는 방향, 구현 및 정책에 따라 달라집니다.

:::single-choice{#bgp-as-path-loop}
`AS_PATH`는 AS 간 루프를 막는 데 어떻게 도움이 됩니까?

::option[AS가 자체 번호를 이미 포함한 경로를 거부할 수 있습니다.]{#bgp-own-as-reject .correct explanation="경로 벡터는 광고된 접두사에 도달하는 데 사용된 AS 순서를 보여 줍니다."}
::option[그 시스템을 통과하는 모든 패킷을 암호화합니다.]{#bgp-aspath-encryption explanation="이 속성은 라우팅 경로를 설명하며 페이로드 암호화를 제공하지 않습니다."}
::option[모든 AS에 MAC 주소를 할당합니다.]{#bgp-aspath-mac explanation="자율 시스템 번호와 링크 주소는 별도의 네임스페이스입니다."}
:::

## 정책 기반 선택

BGP의 “최적” 경로는 설정된 결정 과정에서 이긴 경로입니다. 운영자는 고객 경로를 선호하고, 로컬 선호도를 바꾸고, 접두사를 필터링하고, community를 사용하며, 트래픽 엔지니어링 정책을 적용할 수 있습니다. 더 짧은 `AS_PATH`가 한 단계에서 중요할 수 있지만 더 높은 우선순위 속성을 항상 이기는 것은 아닙니다.

BGP가 후보를 선택한 뒤에는 일반적인 IP 전달에 여전히 최장 접두사 일치가 적용됩니다. 선택된 `/24`는 이를 포함하는 선택된 `/16` 대신 해당 목적지에 사용됩니다.

:::single-choice{#bgp-best-path-meaning}
BGP 최적 경로는 무엇을 나타냅니까?

::option[로컬 속성과 정책 결정 과정에서 이긴 경로입니다.]{#bgp-policy-winner .correct explanation="관리 의도가 도메인 간 경로 선택의 핵심입니다."}
::option[모든 경우 물리 케이블 길이가 가장 짧은 경로입니다.]{#bgp-shortest-cable explanation="BGP에는 완전한 물리 거리 지도가 없습니다."}
::option[현재 애플리케이션 지연 시간이 가장 낮다는 보장입니다.]{#bgp-lowest-latency explanation="BGP 선택은 기본적으로 최종 사용자 지연 시간을 계속 최적화하지 않습니다."}
:::

## 광고와 연결 가능성

접두사 광고는 정책 아래 연결 가능성을 주장하지만 하위 경로를 만들거나 반환 경로를 보장하지 않습니다. 접두사를 생성하기 전에 유효한 전달, 집계 동작, 필터, 장애 조치 및 소유권 승인을 확인하십시오.

:::single-choice{#bgp-advertisement-limit}
접두사 광고만으로 보장할 수 없는 것은 무엇입니까?

::option[피어가 제어 평면 경로를 받을 수 있습니다.]{#bgp-peers-control explanation="성공적인 광고와 수락은 그 제한적인 제어 평면 사실을 확립할 수 있습니다."}
::option[접두사에 주소 비트가 포함됩니다.]{#bgp-prefix-bits explanation="IP 접두사는 주소 비트와 길이로 정의됩니다."}
::option[전체 접두사의 패킷을 전달할 수 있습니다.]{#bgp-data-plane-not-guaranteed .correct explanation="하위 경로, 다음 홉, 필터링 및 서비스 상태를 별도로 검증해야 합니다."}
:::

## 라우팅 보안과 변경 제어

경로 누출과 하이재킹은 하나의 라우터를 훨씬 넘어 트래픽에 영향을 줄 수 있습니다. 운영자는 엄격한 가져오기 및 내보내기 필터, 최대 접두사 제한, 피어 정책, 모니터링 및 적절한 경우 RPKI(Resource Public Key Infrastructure) 원본 검증을 사용합니다. RPKI 원본 검증은 AS가 접두사를 생성할 권한이 있는지 확인하며 전체 AS 경로를 검증하지 않습니다.

BGP 변경에는 단계적 배포, 경로 차이 검토, 대역 외 접근, 되돌리기 및 제어·데이터 평면 검증이 필요합니다.

:::single-choice{#bgp-rpki-limit}
RPKI 원본 검증은 무엇을 확인합니까?

::option[모든 패킷 페이로드에 악성 코드가 없는지 확인합니다.]{#bgp-payload-malware explanation="RPKI는 응용 콘텐츠를 조사하지 않습니다."}
::option[전체 AS 경로의 지연 시간이 가장 낮은지 확인합니다.]{#bgp-path-latency explanation="원본 검증은 성능 선택이나 전체 경로 검증이 아닙니다."}
::option[원본 AS에 권한이 있는지 확인합니다.]{#bgp-origin-authorized .correct explanation="AS 경로의 모든 전송 관계가 아니라 원본 권한을 검증합니다."}
:::

## 요약

이제 BGP를 정책으로 제어되는 경로 벡터 라우팅으로 설명할 수 있습니다.

1. 외부 BGP와 내부 BGP 세션을 구분합니다.
2. `AS_PATH`를 경로 및 루프 정보로 사용합니다.
3. 로컬 속성과 정책을 통해 최적 경로를 해석합니다.
4. 광고된 모든 접두사 뒤의 전달을 검증합니다.
5. 필터링, 원본 검증, 모니터링 및 되돌리기를 적용합니다.
