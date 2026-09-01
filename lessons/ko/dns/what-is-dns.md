---
lesson_id: "what-is-dns"
course_id: "dns"
lang: "ko"
order_index: 1
title: "DNS란?"
description: "DNS가 분산된 이름과 형식이 지정된 리소스 레코드를 구성하고 확인하는 방법을 알아봅니다."
meta_title: "DNS란? - DNS"
meta_description: "DNS가 무엇인지, 도메인 이름을 IP 주소로 변환하는 방법 및 인터넷의 핵심 이름 시스템인 이유를 알아봅니다."
meta_keywords: "DNS, Domain Name System, IP 주소, 호스트 이름, 리눅스 네트워킹"
---

DNS(Domain Name System)는 분산된 계층형 데이터베이스이자 쿼리 프로토콜입니다. 클라이언트가 주소, 메일 라우팅, 권위 서버, 서비스 데이터 및 검증 레코드 등 이름과 연결된 형식별 정보를 검색할 수 있게 합니다.

## 이름과 리소스 레코드

DNS는 호스트 이름 하나를 IP 주소 하나로 변환하는 것 이상을 수행합니다. `A` 레코드는 IPv4 주소, `AAAA`는 IPv6 주소, `MX`는 메일 라우팅 데이터, `NS`는 권위 서버 이름을 담으며 그 밖의 많은 유형이 서로 다른 데이터를 운반합니다. 하나의 이름에 여러 레코드가 있거나 주소 레코드가 전혀 없을 수 있습니다.

:::single-choice{#dns-purpose-beyond-address} DNS가 단순한 호스트 이름-주소 목록 이상인 이유는 무엇입니까?

::option[모든 Ethernet 프레임에 MAC 주소를 영구적으로 할당합니다.]{#dns-mac-frames explanation="링크 계층 이웃 탐색은 DNS를 이런 방식으로 사용하지 않습니다."}
::option[여러 종류의 서비스 및 위임 데이터를 형식이 지정된 레코드로 저장합니다.]{#dns-typed-records .correct explanation="주소, 메일, 권위, 별칭 및 정책 관련 레코드에는 서로 다른 의미가 있습니다."}
::option[이름이 있는 모든 애플리케이션의 정상 상태를 보장합니다.]{#dns-health-guarantee explanation="목적지 서비스를 사용할 수 없어도 DNS 데이터는 확인될 수 있습니다."}
:::

## 계층형 이름

정규화된 도메인 이름(FQDN)은 DNS 트리의 경로를 식별합니다. `www.example.com.`에서 마지막 점은 루트를 나타내고, `com`은 그 아래에, `example`은 `com` 아래에, `www`는 해당 도메인 안의 이름입니다. 사용자 인터페이스에서는 후행 점을 자주 생략하지만 설정에서 절대 이름과 로컬 상대 이름을 구분할 때 중요합니다.

:::single-choice{#dns-trailing-dot} `www.example.com.`의 마지막 점은 무엇을 나타냅니까?

::option[DNS 루트와 절대 이름을 나타냅니다.]{#dns-root-dot .correct explanation="점은 이름이 지정된 노드부터 루트까지의 완전한 경로를 끝냅니다."}
::option[모든 최상위 도메인의 와일드카드입니다.]{#dns-dot-wildcard explanation="와일드카드는 루트 종결자가 아니라 * 같은 레이블을 사용합니다."}
::option[IPv4만 사용하라는 지시입니다.]{#dns-dot-ipv4 explanation="요청하는 주소 계열은 레코드 유형이 제어합니다."}
:::

## 분산된 권위

DNS 권위는 계층 아래로 위임됩니다. 루트 서버는 확인자를 최상위 도메인 서버로 안내하고, 이 서버는 다시 위임된 영역의 권위 서버로 안내합니다. 조직은 전체 전역 네임스페이스를 하나의 중앙 서버에 저장하지 않고 자체 권위 데이터를 관리합니다.

:::single-choice{#dns-authoritative-data} 위임된 DNS 영역의 확정 데이터를 제공하는 주체는 누구입니까?

::option[이전에 사이트를 방문한 모든 브라우저입니다.]{#dns-browser-authority explanation="브라우저 캐시는 영역의 권위 서버가 아닙니다."}
::option[영역에 설정된 권위 네임 서버입니다.]{#dns-authoritative-servers .correct explanation="위임은 권위 있게 응답할 책임이 있는 서버를 식별합니다."}
::option[주소로 패킷을 운반하는 모든 라우터입니다.]{#dns-router-authority explanation="패킷 전달과 DNS 권위는 서로 다른 역할입니다."}
:::

## 확인과 캐싱

호스트의 스텁 확인자는 일반적으로 재귀 확인자에 쿼리를 보냅니다. 재귀 확인자는 유효한 캐시에서 응답하거나 클라이언트를 대신해 계층을 조회할 수 있습니다. 레코드 TTL은 정상적으로 캐시 항목을 재사용할 수 있는 시간을 제한해 확장성을 높이지만 캐시가 갱신될 때까지 변경 노출을 지연합니다.

DNS 성공은 경로, 전송, TLS 또는 애플리케이션 상태를 입증하지 않습니다. `/etc/hosts`, 검색 접미사, 로컬 캐시 또는 이름 서비스 정책이 시스템 확인자에 영향을 주므로 외부 쿼리 전에 DNS가 실패할 수도 있습니다.

:::single-choice{#dns-cache-ttl-role} DNS 레코드 TTL이 주로 제어하는 것은 무엇입니까?

::option[IP 패킷이 통과할 수 있는 라우터 수입니다.]{#dns-ip-hop-limit explanation="IP TTL 또는 Hop Limit은 다른 프로토콜 필드입니다."}
::option[애플리케이션이 정상 상태를 유지해야 하는 시간입니다.]{#dns-app-health-time explanation="DNS 캐싱은 서비스 가용성을 보장하지 않습니다."}
::option[정상 규칙에 따라 확인자가 레코드를 캐시할 수 있는 시간입니다.]{#dns-cache-lifetime .correct explanation="짧거나 긴 캐싱은 쿼리 부하와 변경 전파에 영향을 줍니다."}
:::

## 요약

이제 DNS를 형식이 지정되고 캐시되며 계층적인 데이터 시스템으로 설명할 수 있습니다.

1. DNS 리소스 레코드 유형을 목적에 따라 구분합니다.
2. 루트부터 정규화된 이름을 읽습니다.
3. 위임과 권위 책임을 식별합니다.
4. 이름 확인과 애플리케이션 연결을 구분합니다.
