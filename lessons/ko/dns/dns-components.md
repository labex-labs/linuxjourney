---
lesson_id: "dns-components"
course_id: "dns"
lang: "ko"
order_index: 2
title: "DNS 구성 요소"
description: "재귀 확인자, 권위 서버, 영역 및 리소스 레코드가 DNS 책임을 나누는 방법을 알아봅니다."
meta_title: "DNS 구성 요소 - DNS"
meta_description: "네임 서버, 영역 및 리소스 레코드 같은 DNS 구성 요소와 역할을 알아봅니다."
meta_keywords: "DNS 구성 요소, 네임 서버, 영역 파일, 리소스 레코드, DNS 튜토리얼, 리눅스 네트워킹"
---

DNS는 클라이언트 대상 재귀 역할과 권위 있는 게시 역할을 구분합니다. 이 경계를 이해하면 캐시된 응답을 영역 소유자로 잘못 생각하는 일을 막을 수 있습니다.

## 스텁 및 재귀 확인자

애플리케이션이나 운영체제의 스텁 확인자는 설정된 재귀 확인자에 쿼리를 보냅니다. 재귀 확인자는 캐시를 사용하고 필요하면 반복 쿼리를 수행한 뒤 최종 응답, 오류 또는 위임 결과를 반환합니다. 응답 서버가 데이터에 대한 권위 서버일 때만 응답에 권위 응답 플래그가 있을 수 있습니다. 재귀 기능만으로 권위 서버가 되지는 않습니다.

:::single-choice{#dns-components-recursive-role}
재귀 확인자는 스텁 클라이언트를 위해 무엇을 합니까?

::option[캐시와 다른 네임 서버를 사용해 최종 DNS 결과를 얻습니다.]{#dns-components-recursive-result .correct explanation="클라이언트가 여러 단계의 조회 작업을 재귀 서비스에 위임합니다."}
::option[패킷 경로의 모든 네트워크 라우터를 대체합니다.]{#dns-components-replaces-router explanation="이름 확인과 IP 전달은 서로 별개입니다."}
::option[캐시하는 모든 레코드의 권위 서버가 됩니다.]{#dns-components-cache-authority explanation="캐시된 데이터의 권위는 소스에 있으며 확인자는 영역 소유자가 아닙니다."}
:::

## 권위 네임 서버

권위 서버는 권한을 가진 영역 데이터에서 응답합니다. 하나의 영역에는 동기화된 데이터와 독립적인 장애 고려 사항을 가진 여러 권위 서버가 있어야 합니다. 권위 전용 서버는 임의 클라이언트에 재귀 기능을 제공할 필요가 없습니다.

:::single-choice{#dns-components-authoritative-role}
서버가 영역에 대한 권위를 갖게 하는 것은 무엇입니까?

::option[공용 확인자를 통해 영역을 한 번 조회했습니다.]{#dns-components-once-queried explanation="조회나 캐싱은 권위를 부여하지 않습니다."}
::option[관련 위임과 설정 아래에서 영역 데이터를 제공합니다.]{#dns-components-serves-zone .correct explanation="권위는 캐시 사본 보유가 아니라 DNS 위임과 서버에 불러온 영역에서 옵니다."}
::option[ping 한 번에 가장 빠르게 응답했습니다.]{#dns-components-fastest-ping explanation="ICMP 시간은 DNS 권위를 정의하지 않습니다."}
:::

## 영역과 영역 저장소

영역은 DNS 네임스페이스에서 관리상 제공되는 부분입니다. 영역 정점에서 시작하며 하위 영역을 위임할 수 있습니다. 영역 데이터는 텍스트 영역 파일, 데이터베이스, API 또는 소프트웨어 합성으로 제공될 수 있습니다. “영역 파일”이 필수 물리 구현은 아닙니다.

영역 정점에는 일반적으로 SOA 레코드와 NS 집합이 있습니다. 상위 영역의 위임 데이터는 하위 권위 서버를 식별하며, 영역 내부 서버 이름에 도달하는 데 필요한 글루 주소 레코드가 함께 올 수 있습니다.

:::single-choice{#dns-components-zone-meaning}
DNS 영역이란 무엇입니까?

::option[네임스페이스에서 관리상 제공되는 부분입니다.]{#dns-components-admin-portion .correct explanation="저장 백엔드와 관계없이 레코드와 위임을 포함할 수 있습니다."}
::option[모든 클라이언트에 필수인 하나의 텍스트 파일입니다.]{#dns-components-client-file explanation="권위 구현은 여러 저장 형식을 사용할 수 있고 클라이언트는 모든 영역을 보관하지 않습니다."}
::option[VLAN으로 식별되는 Ethernet 브로드캐스트 도메인입니다.]{#dns-components-vlan explanation="DNS 영역과 링크 계층 세그먼트는 독립적인 개념입니다."}
:::

## 리소스 레코드 필드

리소스 레코드에는 소유자 이름, TTL, 클래스, 유형 및 유형별 RDATA가 있습니다.

```text
www.example.com.  300  IN  A  192.0.2.25
```

소유자는 `www.example.com.`, TTL은 300초, 클래스는 Internet, 유형은 IPv4 주소, RDATA는 그 주소입니다. 영역 파일 구문에서 필드 생략과 상대 이름 규칙을 사용할 때 origin을 신중하게 처리해야 합니다.

:::single-choice{#dns-components-mx-type}
메일 교환기 선호도와 호스트 이름을 게시하는 레코드 유형은 무엇입니까?

::option[`A`]{#dns-components-a explanation="A 레코드는 IPv4 주소를 저장합니다."}
::option[`NS`]{#dns-components-ns explanation="NS 레코드는 권위 네임 서버를 식별합니다."}
::option[`MX`]{#dns-components-mx .correct explanation="MX RDATA에는 선호도와 메일 교환기 이름이 포함됩니다."}
:::

## TTL과 부정 캐싱

긍정 레코드는 TTL로 캐시 재사용을 제한합니다. 존재하지 않는 이름이 입증된 것과 같은 부정 응답도 SOA에서 파생된 규칙에 따라 캐시될 수 있습니다. 계획된 변경 직전에 TTL을 낮추면 캐시가 더 낮은 값을 관찰한 뒤 가져온 레코드에만 영향을 줍니다. 이전의 긴 TTL로 이미 캐시된 레코드는 만료될 때까지 남습니다.

:::single-choice{#dns-components-lower-ttl-timing}
계획된 주소 변경보다 훨씬 전에 DNS TTL을 낮추는 이유는 무엇입니까?

::option[TTL이 서버의 Ethernet MTU를 수정합니다.]{#dns-components-ttl-mtu explanation="캐싱 수명과 링크 패킷 크기는 관계없습니다."}
::option[낮은 TTL이 새 애플리케이션의 정상 상태를 보장합니다.]{#dns-components-ttl-health explanation="서비스 정확성이 아니라 캐싱 동작에 영향을 줍니다."}
::option[기존 캐시가 이전의 긴 TTL로 학습한 레코드를 만료시킬 시간이 필요합니다.]{#dns-components-old-cache-expiry .correct explanation="권위 데이터 변경은 이미 캐시된 레코드의 남은 수명을 소급해 줄일 수 없습니다."}
:::

## 요약

이제 DNS 재귀, 권위, 네임스페이스 관리 및 캐시된 레코드를 구분할 수 있습니다.

1. 스텁 및 재귀 확인자의 역할을 식별합니다.
2. 위임된 영역 서비스를 통해 권위를 정의합니다.
3. 영역을 하나의 필수 파일이 아니라 네임스페이스 책임으로 다룹니다.
4. 소유자, TTL, 클래스, 유형 및 RDATA 필드를 읽습니다.
5. DNS 변경 전에 캐시 수명을 계획합니다.
