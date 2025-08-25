---
index: 3
lang: "ko"
title: "DNS 프로세스"
meta_title: "DNS 프로세스 - DNS"
meta_description: "DNS 가 루트 서버에서 권한 있는 DNS 까지 단계별로 작동하는 방식을 알아보세요. 초보자 및 중급 사용자를 위한 DNS 조회 프로세스를 이해합니다."
meta_keywords: "DNS 프로세스, DNS 조회, DNS 작동 방식, DNS 튜토리얼, 초보자 DNS, Linux DNS, TLD, 루트 서버"
---

## Lesson Content

DNS 를 사용하여 호스트가 도메인 (catzontheinterwebz.com) 을 찾는 방법을 예시로 살펴보겠습니다. 기본적으로, 해당 도메인을 아는 DNS 서버에 도달할 때까지 아래로 내려갑니다.

### 로컬 DNS 서버

먼저, 우리 호스트는 "catzontheinterwebz.com 은 어디에 있나요?"라고 묻습니다. 우리 로컬 DNS 서버는 모르기 때문에, 루트 서버에 물어보기 위해 깔때기 상단부터 시작합니다. 우리 호스트가 catzontheinterwebz.com 을 직접 찾기 위해 이러한 요청을 하는 것이 아니라는 점을 명심하십시오. 대부분의 사용자는 ISP 가 제공하는 재귀적 DNS 서버와 통신하며, 이 서버는 catzontheinterwebz.com 의 위치를 찾는 임무를 맡습니다.

### 루트 서버

인터넷에는 13 개의 루트 서버가 있습니다. 이들은 인터넷의 DNS 요청을 처리하기 위해 전 세계에 미러링되고 분산되어 있으므로, 실제로는 수백 대의 서버가 작동하고 있습니다. 이들은 다른 조직에 의해 제어되며 최상위 도메인 (Top-Level Domains) 에 대한 정보를 포함합니다. 최상위 도메인은 .org, .com, .net 등과 같은 주소로 알려져 있습니다. 따라서 루트 서버는 catzontheinterwebz.com 이 어디에 있는지 모르지만, 우리가 제공하는 IP 주소에 있는 .com 최상위 도메인 DNS 서버에 물어보라고 알려줍니다.

### 최상위 도메인

이제 ".com" 주소를 아는 네임 서버에 또 다른 요청을 보내 catzontheinterwebz.com 이 어디에 있는지 아는지 묻습니다. TLD 는 catzontheinterwebz.com 을 자신의 존 파일에 가지고 있지 않지만, catzontheinterwebz.com 의 네임 서버에 대한 레코드를 가지고 있습니다. 그래서 해당 네임 서버의 IP 주소를 알려주고 그곳에서 찾아보라고 합니다.

### 권한 있는 DNS 서버

이제 우리가 원하는 레코드를 실제로 가지고 있는 DNS 서버에 최종 요청을 보냅니다. 네임 서버는 catzontheinterwebz.com 에 대한 존 파일을 가지고 있으며, 이 호스트에 대한 'www' 리소스 레코드가 있음을 확인합니다. 그런 다음 이 호스트의 IP 주소를 알려주고, 마침내 인터넷에서 고양이를 볼 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 DNS 확인 및 관리에 대한 이해를 강화하기 위한 실습입니다:

1. **[dig 및 nslookup 을 사용하여 Linux 에서 DNS 레코드 쿼리](https://labex.io/ko/labs/linux-query-dns-records-in-linux-with-dig-and-nslookup)** - A, PTR, MX 와 같은 DNS 레코드를 쿼리하고 기본 DNS 서버를 식별하는 방법을 배우세요. 이는 네트워크 문제 해결에 필수적입니다.
2. **[Linux 에 로컬 권한 있는 DNS 서버 설정](https://labex.io/ko/labs/linux-set-up-a-local-authoritative-dns-server-on-linux)** - 로컬 권한 있는 DNS 서버를 설치 및 구성하고, 존을 정의하고, DNS 확인을 테스트하여 실습 경험을 쌓으세요.
3. **[Linux 에서 로컬 호스트 이름 확인 관리](https://labex.io/ko/labs/linux-manage-local-hostname-resolution-in-linux)** - `/etc/hosts` 파일을 편집하여 로컬 호스트 이름 확인을 관리하는 연습을 하세요. 이는 웹 개발 및 네트워크 테스트에 중요한 기술입니다.

이러한 실습은 실제 시나리오에 개념을 적용하고 DNS 에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

.com, .net, .org 등과 같은 주소가 발견되는 네임 서버의 약어는 무엇입니까?

## Quiz Answer

TLD
