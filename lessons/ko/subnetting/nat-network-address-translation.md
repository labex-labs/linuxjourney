---
index: 6
lang: "ko"
title: "NAT"
meta_title: "NAT - 서브넷팅"
meta_description: "Linux 에서 NAT(네트워크 주소 변환) 의 작동 방식과 네트워크 보안에서의 역할에 대해 알아보세요. 사설 IP 와 공용 IP 를 이해합니다. Linux 네트워킹 가이드."
meta_keywords: "NAT, 네트워크 주소 변환, Linux 네트워킹, 사설 IP, 공용 IP, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

이전에 NAT(네트워크 주소 변환) 에 대해 언급했지만 자세히 다루지는 않았습니다. 우리가 네트워크에서 작업할 때 인터넷이 우리의 IP 주소를 볼 수 있다는 의미일까요? 그렇지는 않습니다.

NAT 는 우리의 라우터와 같은 장치가 인터넷과 사설 네트워크 사이의 중개자 역할을 하도록 만듭니다. 따라서 전체 컴퓨터 그룹을 나타내기 위해 단일하고 고유한 IP 주소만 필요합니다.

NAT 를 큰 사무실의 접수원이라고 생각해보세요. 누군가 당신에게 연락하고 싶다면, 그들은 사무실 전체의 번호만 알고 있습니다. 접수원은 당신의 내선 번호를 찾아 전화를 당신에게 연결해 줄 것입니다.

### 작동 방식

간단한 경우는 다음과 같습니다.

1. Patty 는 `www.google.com`에 연결하려고 하므로, 그녀의 기기는 이 요청을 라우터를 통해 보냅니다.
2. 라우터는 그 요청을 받아 google.com 에 자체 연결을 열고, 연결이 되면 Patty 의 요청을 보냅니다.
3. 라우터는 Patty 와 `www.google.com` 사이의 중개자입니다. Google 은 Patty 에 대해 알지 못하며, 대신 라우터만 볼 수 있습니다.

NAT 와 일반적인 패킷 라우팅은 상당히 복잡해질 수 있지만, 우리는 세부 사항에 깊이 파고들지 않을 것입니다.

## Exercise

연습하면 완벽해집니다! 다음은 NAT 와 같은 개념을 이해하는 데 기초가 되는 네트워크 주소 지정 및 연결에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 Linux 시스템에서 IPv4 및 IPv6 주소를 포함한 네트워크 주소 지정 정보를 식별하는 연습을 합니다.
2. **[Linux 에서 IP 주소 지정 관리](https://labex.io/ko/labs/comptia-manage-ip-addressing-in-linux-592736)** - 고정 및 동적 IP 를 구성하고 네트워크 구성을 확인하여 IP 주소 지정을 관리하는 방법을 배우며, 장치가 주소를 얻는 방법을 이해하는 데 도움이 됩니다.
3. **[Linux 에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 다양한 IP 주소 유형 (사설, 공용, 멀티캐스트) 을 탐색하고 네트워크 도달 가능성을 테스트하여 NAT 가 내부 및 외부 주소를 구별하는 방법에 대한 실제적인 맥락을 제공합니다.

이러한 실습은 실제 시나리오에 개념을 적용하고 Linux 에서 네트워크 구성 및 문제 해결에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

단일 사설 주소를 인터넷에 나타내기 위해 사용되는 것은 무엇입니까?

## Quiz Answer

NAT
