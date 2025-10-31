---
index: 3
lang: "ko"
title: "DNS 프로세스"
meta_title: "DNS 프로세스 - DNS"
meta_description: "루트 서버부터 권한 있는 DNS 서버까지 단계별 DNS 확인 프로세스를 살펴보세요. Linux 서버가 도메인을 찾는 방법을 이해하는 것은 프로덕션 환경 및 도메인 호스팅에 매우 중요합니다."
meta_keywords: "DNS 프로세스, DNS 조회, 도메인 확인, 리눅스 dns, 프로덕션 서버, 도메인 호스팅, dns 서버, TLD, 루트 서버, 권한 있는 dns"
---

## Lesson Content

이제 `Linux 서버`와 같은 컴퓨터가 DNS 를 사용하여 `catzontheinterwebz.com`과 같은 `도메인`을 찾는 방법을 살펴보겠습니다. 이 프로세스는 깔때기처럼 작동하여 검색 범위를 좁혀 최종적으로 정답을 보유한 특정 `DNS 서버`에 도달합니다.

### 초기 쿼리

먼저, 호스트는 구성된 재귀적 DNS 서버에 "`catzontheinterwebz.com`은 어디에 있습니까?"라고 묻습니다. 이 재귀적 서버는 일반적으로 ISP 에서 제공하며 직접적인 답을 모를 가능성이 높습니다. 따라서 가장 높은 권한을 가진 루트 서버에 연락하여 확인 프로세스를 시작합니다. 이 초기 단계는 집에서 브라우징하든 `프로덕션 서버`가 API 와 통신하든 동일합니다.

### 루트 서버

인터넷의 DNS 계층 구조는 13 개의 논리적 루트 서버에서 시작되며, 이는 전 세계 수백 개의 실제 위치에 미러링됩니다. 이 서버들은 모든 `도메인`의 IP 주소를 알지는 못하지만, `.com`, `.org`, `.net`과 같은 최상위 도메인 (TLD) 을 관리하는 곳은 알고 있습니다. `catzontheinterwebz.com`에 대한 요청을 받으면 루트 서버는 "모르지만 `.com` TLD 서버에 문의해야 합니다"라고 응답하고 해당 IP 주소를 제공합니다.

### 최상위 도메인 서버

다음으로 재귀적 서버는 `.com` TLD 서버에 새 쿼리를 보내 다시 `catzontheinterwebz.com`의 위치를 요청합니다. TLD 서버의 역할은 해당 특정 `도메인`에 대한 올바른 권한 있는 네임 서버를 가리키는 것입니다. 최종 IP 주소는 없지만, 해당 `도메인`을 담당하는 `DNS 서버`가 누구인지는 알고 있으며, 이는 종종 `도메인 호스팅` 제공업체를 통해 구성됩니다. TLD 서버는 해당 권한 있는 네임 서버의 IP 주소로 응답합니다.

### 권한 있는 DNS 서버

마지막으로 재귀적 서버는 권한 있는 `DNS 서버`에 마지막 요청을 보냅니다. 이 서버는 `catzontheinterwebz.com` `도메인`에 대한 실제 DNS 레코드를 보유하고 있는 서버입니다. 이 서버는 레코드를 확인하고 호스트에 대한 'A' 레코드를 찾아 최종 IP 주소를 반환합니다. 이 서버는 `도메인` 이름과 `프로덕션 서버`의 IP 주소 간의 결정적인 연결을 제공하므로 웹사이트나 애플리케이션을 라이브로 `만드는` 모든 사람에게 중요한 단계입니다. IP 주소를 확보하면 컴퓨터가 연결하여 콘텐츠를 검색할 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! DNS 확인 및 관리에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux 에서 dig 및 nslookup 으로 DNS 레코드 쿼리하기](https://labex.io/ko/labs/comptia-query-dns-records-in-linux-with-dig-and-nslookup-592796)** - A, PTR, MX 와 같은 DNS 레코드를 쿼리하고 기본 DNS 서버를 식별하는 방법을 배우며, 이는 네트워크 문제 해결에 필수적입니다.
2. **[Linux 에 로컬 권한 있는 DNS 서버 설정하기](https://labex.io/ko/labs/comptia-set-up-a-local-authoritative-dns-server-on-linux-592803)** - 로컬 권한 있는 DNS 서버를 설치 및 구성하고, 영역을 정의하고, DNS 확인을 테스트하여 실습 경험을 쌓으십시오.
3. **[Linux 에서 로컬 호스트 이름 확인 관리하기](https://labex.io/ko/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - `/etc/hosts` 파일을 편집하여 로컬 호스트 이름 확인을 관리하는 연습을 하며, 이는 웹 개발 및 네트워크 테스트의 핵심 기술입니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 DNS 에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

.com, .net, .org 등의 주소가 발견되는 네임서버의 약어는 무엇입니까? 대문자 영어 알파벳만 사용하여 답하십시오.

## Quiz Answer

TLD
