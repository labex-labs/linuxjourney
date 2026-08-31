---
lesson_id: "ipv6"
course_id: "subnetting"
lang: "ko"
order_index: 7
title: "IPv6"
description: "IPv6 주소, 접두사, 범위, 자동 설정 및 리눅스 라우팅 상태를 읽는 방법을 알아봅니다."
meta_title: "IPv6 - 서브넷팅"
meta_description: "초보자를 위한 IPv6 프로토콜 가이드입니다. IPv6가 만들어진 이유, IPv4와의 차이 및 현대 리눅스 네트워킹의 주소 지정 체계를 알아봅니다."
meta_keywords: "IPv6, IPv4, IP 주소, 리눅스 네트워킹, 네트워크 프로토콜, 인터넷 프로토콜, 주소 고갈"
---

IPv6는 128비트 주소를 사용하며 훨씬 큰 주소 공간과 갱신된 패킷 및 이웃 탐색 동작을 지원하도록 설계됐습니다. IPv4와 IPv6는 서로 다른 프로토콜이며 듀얼 스택 호스트는 네트워크 전환 중 둘을 함께 실행할 수 있습니다.

## IPv6 표기 읽기

IPv6 주소는 16비트 16진수 그룹 여덟 개로 씁니다.

```text
2001:0db8:0000:0000:0000:0000:0000:0025
```

각 그룹의 앞쪽 0은 생략할 수 있고 연속된 0 그룹 한 구간은 `::`로 압축할 수 있습니다.

```text
2001:db8::25
```

생략한 그룹 수가 모호해지지 않도록 `::`는 한 번만 나타날 수 있습니다. `2001:db8::/32`는 문서 예시용으로 예약되어 있습니다.

:::single-choice{#ipv6-double-colon-rule}
IPv6 주소에 `::`가 최대 한 번만 나타날 수 있는 이유는 무엇입니까?

::option[`::` 표시가 여러 개면 확장 방식이 모호해지기 때문입니다.]{#ipv6-compression-ambiguity .correct explanation="압축 표시 하나는 여덟 그룹을 채우는 데 필요한 정확한 그룹 수로 확장할 수 있습니다."}
::option[IPv6 주소에는 0비트가 하나뿐이기 때문입니다.]{#ipv6-one-zero explanation="주소에는 많은 0비트와 0 그룹이 있을 수 있습니다."}
::option[이 표시가 TCP 포트 0을 선택하기 때문입니다.]{#ipv6-port-zero explanation="주소 압축은 전송 포트와 관계없습니다."}
:::

## 주소 유형과 범위

중요한 주소와 범위는 다음과 같습니다.

- `::1/128`: 로컬 호스트의 루프백
- `fe80::/10`: 링크 로컬 유니캐스트이며 일반적으로 IPv6 인터페이스에 존재
- `2000::/3`: 현재 할당된 전역 유니캐스트 공간
- `ff00::/8`: 멀티캐스트

IPv6에는 브로드캐스트 주소가 없습니다. IPv4가 브로드캐스트로 처리하는 사용 사례를 멀티캐스트와 Neighbor Discovery가 담당합니다. 모든 링크에 같은 접두사가 있으므로 링크 로컬 목적지에는 `fe80::1%eth0` 같은 인터페이스 영역이 필요할 수 있습니다.

:::single-choice{#ipv6-link-local-scope}
`fe80::/10` 주소의 일반적인 범위는 무엇입니까?

::option[전역 인터넷의 모든 호스트입니다.]{#ipv6-global-link-local explanation="전역 유니캐스트 주소가 라우팅되는 전역 범위를 제공합니다."}
::option[DNS 영역 파일에만 해당합니다.]{#ipv6-dns-only explanation="링크 로컬 주소는 인터페이스에 할당되고 네트워크에서 사용됩니다."}
::option[하나의 로컬 링크입니다.]{#ipv6-one-link .correct explanation="라우터는 일반적인 링크 로컬 트래픽을 링크 사이에서 전달하지 않습니다."}
:::

## 접두사와 인터페이스 주소

IPv6 CIDR 표기는 `/0`부터 `/128`까지의 접두사 길이를 사용합니다. `/64`는 대부분의 LAN 서브넷에서 사용하는 표준 크기이며 SLAAC(Stateless Address Autoconfiguration)를 지원합니다. 하나의 인터페이스에 링크 로컬, 안정적인 전역, 임시 개인 정보 보호 및 기타 주소가 동시에 있을 수 있고 각 주소에는 선호 수명과 유효 수명이 있습니다.

:::single-choice{#ipv6-address-multiplicity}
하나의 인터페이스에 IPv6 주소가 여러 개 표시될 수 있는 이유는 무엇입니까?

::option[IPv6가 16진수 각 자리마다 하나의 주소를 요구하기 때문입니다.]{#ipv6-one-per-digit explanation="숫자 자리는 표현 방식이며 별도의 인터페이스 할당이 아닙니다."}
::option[서로 다른 범위와 개인 정보 보호 또는 수명 역할이 공존할 수 있기 때문입니다.]{#ipv6-several-roles .correct explanation="링크 로컬과 하나 이상의 전역 또는 임시 주소가 함께 있는 것은 정상입니다."}
::option[각 주소가 별도의 물리 네트워크 카드를 식별하기 때문입니다.]{#ipv6-separate-card explanation="하나의 인터페이스가 여러 주소를 가질 수 있습니다."}
:::

## 이웃 및 라우터 탐색

IPv6 Neighbor Discovery는 주소 확인, 중복 주소 감지, 라우터 탐색 및 연결 정보에 ICMPv6를 사용합니다. Router Advertisement는 접두사와 기본 라우터 정보를 제공할 수 있습니다. 호스트는 SLAAC와 DHCPv6를 결합해 다른 설정을 받을 수 있으며 DHCPv6는 일반적으로 기본 라우터를 제공하지 않습니다.

ICMPv6를 모두 차단하면 필수 프로토콜 동작이 망가집니다. ICMPv6를 선택 사항으로 취급하지 말고 방화벽 정책에서 적절한 범위의 필수 메시지 유형을 허용해야 합니다.

:::single-choice{#ipv6-default-router-source}
IPv6 호스트는 일반적으로 기본 라우터를 동적으로 어떻게 알아냅니까?

::option[Router Advertisement를 통해 알아냅니다.]{#ipv6-router-advertisements .correct explanation="Router Discovery는 ICMPv6 Neighbor Discovery의 일부입니다."}
::option[Ethernet 브로드캐스트 주소에서 알아냅니다.]{#ipv6-ethernet-broadcast explanation="IPv6는 IP 브로드캐스트 주소를 사용하지 않습니다."}
::option[TCP 3방향 핸드셰이크에서 알아냅니다.]{#ipv6-tcp-handshake explanation="TCP는 라우팅이 이미 가능해진 뒤 전송 상태를 수립합니다."}
:::

## IPv6 조사 및 테스트

주소, 경로 및 이웃을 독립적으로 조사합니다.

```bash
$ ip -6 address show
$ ip -6 route show
$ ip -6 neighbor show
$ ping -6 -c 3 2001:db8::25
```

표시된 문서용 주소 대신 실제 할당된 테스트 주소를 사용하십시오. 듀얼 스택 애플리케이션은 IPv6가 고장이어도 IPv4로 성공할 수 있고 그 반대도 가능하므로 각 주소 계열과 DNS `A` 또는 `AAAA` 레코드를 명시적으로 테스트합니다.

:::single-choice{#ipv6-dual-stack-test}
듀얼 스택 서비스에서 IPv4와 IPv6를 별도로 테스트해야 하는 이유는 무엇입니까?

::option[모든 IPv6 패킷이 먼저 IPv4 브로드캐스트로 변해야 하기 때문입니다.]{#ipv6-becomes-ipv4 explanation="네이티브 IPv6와 IPv4는 서로 다른 프로토콜 경로입니다."}
::option[두 주소 계열의 DNS, 경로, 필터 및 장애가 다를 수 있기 때문입니다.]{#ipv6-independent-paths .correct explanation="성공적인 대체 경로가 선호 주소 계열의 고장을 숨길 수 있습니다."}
::option[IPv6 도구가 인터페이스 상태를 표시할 수 없기 때문입니다.]{#ipv6-tools-cannot explanation="ip -6 명령은 주소, 경로 및 이웃 상태를 보여 줍니다."}
:::

## 요약

이제 일반적인 IPv6 인터페이스 및 라우팅 상태를 읽고 테스트할 수 있습니다.

1. 16진수 주소 그룹 여덟 개를 올바르게 확장하거나 압축합니다.
2. 루프백, 링크 로컬, 전역 및 멀티캐스트 범위를 구분합니다.
3. 하나의 인터페이스에 여러 IPv6 주소와 수명이 있을 수 있음을 이해합니다.
4. 필수 Neighbor Discovery 및 Router Advertisement 트래픽을 허용합니다.
5. 듀얼 스택 서비스에서 IPv4와 IPv6 경로를 독립적으로 테스트합니다.
