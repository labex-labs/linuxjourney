---
index: 1
lang: "ko"
title: "DNS 란 무엇인가요?"
meta_title: "DNS 란 무엇인가요? - DNS"
meta_description: "DNS 가 무엇이며 도메인 이름을 IP 주소로 변환하는 방법을 알아보세요. 초보자 친화적인 Linux 가이드를 통해 이 핵심 인터넷 개념을 이해하세요."
meta_keywords: "DNS, 도메인 이름 시스템, IP 주소, 호스트 이름, Linux 네트워킹, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

Google 에서 검색을 할 때마다 `www.google.com` 대신 `http://192.78.12.4`를 입력해야 한다고 상상해 보세요. DNS("Domain Name System") 가 없다면 정확히 그렇게 될 것입니다. 하위 수준 네트워킹은 호스트를 식별하기 위해 원시 IP 주소만 이해합니다. DNS 는 우리 인간이 IP 주소 대신 이름으로 웹사이트와 호스트를 추적할 수 있도록 합니다. 인터넷의 연락처 목록과 같습니다. 누군가의 이름을 알지만 전화번호를 모른다면 연락처 목록에서 간단히 찾아볼 수 있습니다.

DNS 는 근본적으로 호스트 이름과 IP 주소의 분산 데이터베이스입니다. 우리는 사람들이 우리 사이트/도메인에 접근하는 방법을 알 수 있도록 데이터베이스를 관리하고, 다른 곳에서는 다른 사람이 자신의 데이터베이스를 관리하여 다른 사람들이 자신의 도메인에 접근할 수 있도록 합니다. 이 도메인들은 서로 통신하여 인터넷의 거대한 연락처 목록을 구축할 수 있습니다.

이 과정에서는 DNS 의 몇 가지 기본 사항을 다룰 것이지만, DNS 는 방대한 주제이므로 정말 깊이 파고들고 싶다면 추가 조사를 해야 한다는 점을 명심하십시오.

## Exercise

연습이 완벽을 만듭니다! 다음은 DNS 및 호스트 이름 확인에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[dig 및 nslookup 으로 Linux 에서 DNS 레코드 쿼리](https://labex.io/ko/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup)** - `dig` 및 `nslookup`과 같은 필수 Linux 도구를 사용하여 다양한 DNS 레코드 유형을 쿼리하는 방법을 배우고, 호스트 이름이 IP 주소로 확인되는 방식을 이해하는 데 도움이 됩니다.
2. **[Linux 에서 로컬 호스트 이름 확인 관리](https://labex.io/ko/labs/linux-manage-local-hostname-resolution-in-linux)** - `/etc/hosts` 파일을 편집하여 로컬 호스트 이름 확인을 관리하는 연습을 합니다. 이는 외부 DNS 서버에 의존하지 않고 Linux 시스템이 이름을 확인하는 방법을 제어하는 ​​기본적인 기술입니다.
3. **[Linux 에 로컬 권한 있는 DNS 서버 설정](https://labex.io/ko/labs/linux-set-up-a-local-authoritative-dns-server-on-linux)** - `bind9`를 사용하여 자신만의 로컬 권한 있는 DNS 서버를 설정하고 구성하여 DNS 영역 및 레코드가 관리되는 방식에 대해 더 깊이 탐구할 수 있는 실습 경험을 얻습니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux 환경에서 DNS 및 호스트 이름 확인에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

참 또는 거짓: DNS 는 호스트 이름의 MAC 주소를 찾는 데 도움이 됩니까?

## Quiz Answer

False
