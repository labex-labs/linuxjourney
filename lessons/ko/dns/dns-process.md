---
lesson_id: "dns-process"
course_id: "dns"
lang: "ko"
order_index: 3
title: "DNS 과정"
description: "스텁 및 재귀 확인자가 캐시, 위임, 글루 및 권위를 사용해 DNS 쿼리에 응답하는 방법을 알아봅니다."
meta_title: "DNS 과정 - DNS"
meta_description: "루트 서버부터 권위 DNS 서버까지 단계별 DNS 확인 과정을 살펴봅니다. 리눅스 서버가 도메인을 찾는 방법을 설명합니다."
meta_keywords: "DNS 과정, DNS 조회, 도메인 확인, 리눅스 DNS, DNS 서버, TLD, 루트 서버, 권위 DNS"
---

일반 애플리케이션은 운영체제의 스텁 확인자에 요청합니다. 스텁 확인자는 로컬 이름 서비스 정책을 조회하고 설정된 확인자에 재귀 쿼리를 보냅니다. 재귀 확인자는 유효한 캐시로 질문에 응답할 수 없을 때만 계층을 따라 조회합니다.

## 로컬 정책과 캐시에서 시작하기

시스템 확인자는 설정된 순서에 따라 `/etc/hosts`, DNS 및 다른 소스를 조회할 수 있습니다. 검색 접미사는 짧은 이름을 여러 후보 이름으로 바꿀 수 있습니다. 재귀 확인자는 상위 트래픽을 보내기 전에 긍정 및 부정 캐시 항목을 확인합니다.

:::single-choice{#dns-process-cache-first}
재귀 확인자가 쿼리를 위해 권위 서버에 전혀 연락하지 않을 수 있는 이유는 무엇입니까?

::option[DNS가 모든 쿼리에 먼저 로컬 실패를 요구하기 때문입니다.]{#dns-process-requires-failure explanation="확인자는 캐시에서 즉시 응답할 수 있습니다."}
::option[아직 유효한 캐시 응답이 있기 때문입니다.]{#dns-process-valid-cache .correct explanation="캐싱은 레코드 수명이 만료될 때까지 계층 조회 반복을 피합니다."}
::option[권위 서버가 클라이언트의 Ethernet 프레임만 받기 때문입니다.]{#dns-process-authoritative-ethernet explanation="DNS는 라우팅 네트워크의 IP 전송 위에서 작동합니다."}
:::

## 루트 서버 조회하기

캐시 미스가 발생하면 재귀 확인자가 루트 서버에 요청할 수 있습니다. DNS 루트에는 A부터 M까지 이름이 지정된 13개 서버 신원이 있고, 애니캐스트와 기타 복원력 있는 배포 기법으로 많은 물리 인스턴스가 이를 제공합니다. 응답은 보통 최종 호스트 주소를 반환하는 대신 관련 최상위 도메인의 권위 서버로 확인자를 안내합니다.

:::single-choice{#dns-process-root-response}
캐시되지 않은 `www.example.com` 조회에 루트 서버는 일반적으로 무엇을 반환합니까?

::option[`com` 최상위 도메인 서버 방향의 위임을 반환합니다.]{#dns-process-root-referral .correct explanation="루트에 모든 최종 호스트 레코드를 저장하는 대신 계층이 책임을 위임합니다."}
::option[`www.example.com`에 호스팅된 웹 페이지를 반환합니다.]{#dns-process-root-webpage explanation="DNS는 응용 콘텐츠가 아니라 리소스 레코드 데이터를 반환합니다."}
::option[목적지의 Ethernet MAC 주소를 반환합니다.]{#dns-process-root-mac explanation="MAC 주소는 DNS 계층이 아니라 로컬 링크에서 확인합니다."}
:::

## TLD 및 권위 위임 따라가기

확인자는 `com` 권위 서버에 요청하고, 이 서버는 `example.com`에 위임된 권위 네임 서버를 반환합니다. 위임에는 위임된 하위 영역 안에 이름이 있는 서버에 도달해야 할 때 글루 주소 레코드가 포함될 수 있습니다. 그런 다음 확인자가 요청한 레코드를 권위 서버에 조회합니다.

:::single-choice{#dns-process-glue-purpose}
DNS 글루는 어떤 문제를 해결하는 데 도움이 됩니까?

::option[DNS 확인 후 HTTP 페이로드를 암호화합니다.]{#dns-process-glue-http explanation="TLS나 다른 응용 보안이 페이로드 암호화를 처리합니다."}
::option[가장 빠른 Ethernet 스위치 포트를 선택합니다.]{#dns-process-glue-switch explanation="글루는 링크 전달 정책이 아니라 위임 주소 데이터입니다."}
::option[순환 확인 없이 하위 영역 내부 이름의 서버에 도달합니다.]{#dns-process-glue-reachability .correct explanation="상위 영역이 하위 영역 안에 이름이 있는 서버에 연락하는 데 필요한 주소 데이터를 제공합니다."}
:::

## 별칭과 레코드 유형 따라가기

응답에 다른 이름 조회가 필요한 CNAME 별칭이나 추가 쿼리로 이어지는 애플리케이션별 레코드가 포함될 수 있습니다. `A` 쿼리는 IPv4 주소 레코드와 관련 체인 데이터만 반환하고 별도의 `AAAA` 쿼리가 IPv6 주소를 검색합니다. 최종 응답에는 `NOERROR`, `NXDOMAIN` 또는 `SERVFAIL` 같은 서로 다른 의미의 상태가 있습니다.

:::single-choice{#dns-process-nxdomain-meaning}
`NXDOMAIN`은 무엇을 보고합니까?

::option[권위 결과에 따르면 조회한 도메인 이름이 존재하지 않습니다.]{#dns-process-name-does-not-exist .correct explanation="이름은 존재하지만 요청한 레코드 유형만 없는 경우와 다릅니다."}
::option[이름이 존재하며 항상 빈 A 레코드가 있습니다.]{#dns-process-empty-a explanation="요청한 데이터가 없는 기존 이름은 일반적으로 NXDOMAIN이 아니라 데이터 없음 응답을 만듭니다."}
::option[확인자가 최대 Ethernet 프레임 크기에 도달했습니다.]{#dns-process-frame-size explanation="상태는 이름의 존재 여부와 관련됩니다."}
:::

## 검증, 캐싱 및 애플리케이션 사용

검증하는 재귀 확인자는 DNSSEC 서명과 신뢰 체인을 사용해 인증된 부재 또는 레코드 무결성을 확인할 수 있습니다. DNSSEC는 쿼리를 암호화하거나 반환된 주소의 애플리케이션이 신뢰할 수 있음을 입증하지 않습니다.

확인자는 TTL 규칙 안에서 결과를 캐시하고 스텁에 반환합니다. 애플리케이션은 주소를 선택하고 자체 네트워크 및 보안 프로토콜을 시도합니다.

:::single-choice{#dns-process-dnssec-limit}
DNSSEC 검증이 제공하지 않는 것은 무엇입니까?

::option[서명된 DNS 데이터의 무결성과 출처 인증입니다.]{#dns-process-dnssec-does-integrity explanation="DNSSEC의 핵심 목표입니다."}
::option[서명된 존재하지 않는 데이터에 대한 인증된 부재입니다.]{#dns-process-authenticated-denial explanation="서명된 부재 메커니즘이 이 검증을 제공할 수 있습니다."}
::option[DNS 쿼리와 응답의 기밀성입니다.]{#dns-process-no-confidentiality .correct explanation="암호화에는 DoT나 DoH 같은 별도의 보호된 DNS 전송이 필요합니다."}
:::

## 요약

이제 로컬 정책부터 캐시된 최종 응답까지 재귀 DNS 조회를 추적할 수 있습니다.

1. 로컬 소스와 확인자 캐시를 먼저 확인합니다.
2. 루트 및 최상위 도메인 위임을 따라갑니다.
3. 글루를 사용해 적절한 위임 서버에 도달합니다.
4. 별칭, 데이터 없음 응답 및 존재하지 않는 이름을 구분합니다.
5. DNSSEC 무결성과 전송 기밀성을 구분합니다.
