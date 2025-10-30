---
index: 7
lang: "ko"
title: "네트워크 계층"
meta_title: "네트워크 계층 - 네트워크 기본"
meta_description: "Linux 의 네트워크 계층, IP 주소가 서브넷 간에 패킷을 라우팅하는 방법, 데이터 전송에서의 역할에 대해 알아보세요. Linux 네트워킹 여정을 시작하세요!"
meta_keywords: "네트워크 계층, IP 주소, 서브넷, Linux 네트워킹, 패킷 라우팅, 초급, 튜토리얼, 가이드"
---

## Lesson Content

네트워크 계층은 패킷이 소스 호스트에서 대상 호스트로 라우팅되는 방식을 결정합니다. 다행히도 이 예시에서는 패킷이 동일한 네트워크 내에서만 이동하지만, 인터넷은 많은 네트워크로 구성되어 있습니다. 인터넷을 구성하는 이러한 작은 네트워크를 서브넷이라고 합니다. 모든 서브넷은 어떤 식으로든 서로 연결되어 있으므로 `https://www.google.com`이 자체 네트워크에 있더라도 접속할 수 있습니다. 서브넷에 전념하는 전체 과정이 있으므로 자세히 설명하지는 않겠지만, 지금은 네트워크 계층과 관련하여 IP 주소가 다른 서브넷으로 이동하는 규칙을 정의한다는 것을 알아두십시오.

네트워크 계층에서는 전송 계층에서 오는 세그먼트를 수신하고 이 세그먼트를 IP 패킷으로 캡슐화한 다음, 소스 호스트의 IP 주소와 대상 호스트의 IP 주소를 패킷 헤더에 첨부합니다. 따라서 이 시점에서 패킷에는 어디로 가고 어디에서 왔는지에 대한 정보가 있습니다. 이제 패킷을 물리적 하드웨어 계층으로 보냅니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 네트워크 계층, IP 주소 지정 및 서브넷에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 네트워크 계층 연결 시뮬레이션](https://labex.io/ko/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Docker 컨테이너를 사용하여 정적 IP 주소를 할당하고 동일한 서브넷 및 다른 서브넷 내에서 연결을 테스트하는 연습을 합니다.
2. **[Linux 터미널에서 IP 서브넷팅 및 이진 변환 수행](https://labex.io/ko/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - Linux 터미널에서 직접 사용 가능한 호스트 및 서브넷 계산을 포함하여 IP 서브넷팅 및 이진 변환을 마스터합니다.
3. **[Linux 에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 다양한 IP 주소 유형 (사설, 공용, 멀티캐스트) 을 탐색하고 `ping` 및 `ip a`를 사용하여 네트워크 도달 가능성을 테스트합니다.

이 실습은 실제 시나리오에서 IP 주소 지정 및 서브넷팅 개념을 적용하고 네트워크 계층의 기본 사항에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

인터넷을 구성하는 작은 네트워크를 무엇이라고 부릅니까?

## Quiz Answer

subnets
