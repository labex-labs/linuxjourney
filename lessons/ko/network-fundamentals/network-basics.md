---
index: 1
lang: "ko"
title: "네트워크 기본 사항"
meta_title: "네트워크 기본 사항 - 네트워크 기본 사항"
meta_description: "Linux 네트워크 기본 사항을 배우세요: WAN, LAN, WLAN, 라우터 및 호스트를 이해하세요. 이 초보자 가이드로 네트워킹 여정을 시작하세요!"
meta_keywords: "Linux 네트워크 기본 사항, WAN, LAN, WLAN, 네트워크 튜토리얼, 초보자 Linux, 네트워킹 가이드, Linux 개념"
---

## Lesson Content

일반적인 가정 네트워크를 살펴보겠습니다. 몇 가지 다른 구성 요소가 있습니다.

- ISP - 인터넷 서비스 공급자, 집에서 인터넷을 사용하기 위해 비용을 지불하는 회사입니다.
- Router - 라우터는 네트워크의 각 컴퓨터가 인터넷에 연결할 수 있도록 합니다. 대부분의 최신 라우터에서는 무선 또는 이더넷 케이블을 통해 연결할 수 있습니다.
- WAN - 광역 네트워크 (Wide Area Network). 라우터와 인터넷과 같은 더 넓은 네트워크 사이의 모든 것을 포함하는 네트워크를 말합니다.
- WLAN - 무선 근거리 통신망 (Wireless Local Area Network). 라우터와 노트북과 같은 무선 장치 사이의 네트워크입니다.
- LAN - 근거리 통신망 (Local Area Network). 라우터와 데스크톱 PC 와 같은 유선 장치 사이의 네트워크입니다.
- Hosts - 네트워크의 각 컴퓨터는 호스트 (host) 라고 불립니다.

네트워크를 통해 전송되는 데이터와 정보는 패킷 (packets) 이라고 불리며, 네트워킹 노마드 섹션이 끝날 때쯤에는 패킷이 호스트로 이동하고 호스트에서 이동하는 방법을 자세히 이해하게 될 것입니다.

## Exercise

연습이 완벽을 만듭니다! 실습 경험은 네트워킹 기본 사항을 이해하는 데 중요합니다. 다음은 네트워크 구성 요소와 호스트가 통신하는 방식에 대한 이해를 강화하기 위한 몇 가지 실습입니다.

1. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 MAC 및 IP 주소를 포함한 호스트의 네트워크 주소 지정 정보를 식별하는 연습을 합니다.
2. **[Linux 에서 IP 주소 유형 및 연결 가능성 탐색](https://labex.io/ko/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - 네트워크 연결 가능성을 테스트하고 다양한 IP 주소 유형을 식별하는 방법을 배우며, 이는 호스트가 연결되는 방식을 이해하는 데 필수적입니다.
3. **[Linux 에서 ping 및 arp 를 사용하여 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - ARP(Address Resolution Protocol) 를 관찰하고 `ping`으로 연결을 테스트하여 호스트가 네트워크에서 상호 작용하는 방식을 이해합니다.

이러한 실습은 실제 시나리오에서 호스트, 주소 지정 및 기본 연결 개념을 적용하고 기본적인 네트워킹에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

근거리 통신망은 무엇으로 알려져 있습니까?

## Quiz Answer

LAN
