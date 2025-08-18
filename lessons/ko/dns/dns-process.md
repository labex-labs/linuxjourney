---
lang: "ko"
title: "DNS 프로세스"
meta_description: "루트 서버부터 권한 있는 DNS 까지 DNS 가 단계별로 작동하는 방식을 배웁니다. 초보자와 중급 사용자를 위한 DNS 조회 프로세스를 이해합니다."
meta_keywords: "DNS 프로세스, DNS 조회, DNS 작동 방식, DNS 튜토리얼, 초보자 DNS, Linux DNS, TLD, 루트 서버"
---

## Lesson Content

DNS 를 사용하여 호스트가 도메인 (catzontheinterwebz.com) 을 찾는 방법을 예시로 살펴보겠습니다. 기본적으로, 해당 도메인을 아는 DNS 서버에 도달할 때까지 깔때기처럼 아래로 내려갑니다.

### Local DNS Server

먼저, 우리 호스트는 "catzontheinterwebz.com 은 어디에 있나요?"라고 묻습니다. 우리 로컬 DNS 서버는 모르기 때문에, 깔때기의 맨 위부터 시작하여 Root Servers 에 묻습니다. 우리 호스트가 catzontheinterwebz.com 을 직접 찾기 위해 이러한 요청을 하는 것이 아니라는 점을 명심하십시오. 대부분의 사용자는 ISP 가 제공하는 재귀적 DNS 서버와 통신하며, 이 서버는 catzontheinterwebz.com 의 위치를 찾는 임무를 맡습니다.

### Root Servers

인터넷에는 13 개의 Root Servers 가 있습니다. 이들은 전 세계에 미러링되고 분산되어 인터넷의 DNS 요청을 처리하므로, 실제로는 수백 개의 서버가 작동하고 있습니다. 이들은 다른 조직에 의해 제어되며 Top-Level Domains 에 대한 정보를 포함합니다. Top-level domains 는 .org, .com, .net 등과 같은 주소로 알려져 있습니다. 따라서 Root Server 는 catzontheinterwebz.com 이 어디에 있는지 모르지만, 우리가 제공하는 IP 주소에 있는 .com Top-Level Domain DNS Server 에 물어보라고 알려줍니다.

### Top-Level Domain

이제 우리는 ".com" 주소를 아는 네임 서버에 또 다른 요청을 보내 catzontheinterwebz.com 이 어디에 있는지 아는지 묻습니다. TLD 는 zone files 에 catzontheinterwebz.com 을 가지고 있지 않지만, catzontheinterwebz.com 의 네임 서버에 대한 레코드를 발견합니다. 그래서 해당 네임 서버의 IP 주소를 알려주고 그곳에서 찾아보라고 합니다.

### Authoritative DNS Server

이제 우리는 실제로 원하는 레코드를 가지고 있는 DNS 서버에 최종 요청을 보냅니다. 네임 서버는 catzontheinterwebz.com 에 대한 zone file 을 가지고 있으며, 이 호스트에 대한 'www' 리소스 레코드가 있음을 확인합니다. 그런 다음 이 호스트의 IP 주소를 알려주고, 마침내 인터넷에서 고양이들을 볼 수 있습니다.

## Exercise

No exercises for this lesson.

## Quiz Question

.com, .net, .org 등과 같은 주소가 발견되는 네임 서버의 약어는 무엇입니까?

## Quiz Answer

TLD
