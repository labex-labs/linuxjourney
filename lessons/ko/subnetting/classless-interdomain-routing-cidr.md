---
index: 5
lang: "ko"
title: "CIDR"
meta_title: "CIDR - 서브넷팅"
meta_description: "이 초보자 친화적인 가이드를 통해 Linux 네트워킹을 위한 CIDR 표기법을 배우세요. 서브넷 마스크, IP 주소 지정 및 호스트 계산을 이해하세요. 네트워크 기술을 향상시키세요!"
meta_keywords: "CIDR, 서브넷 마스크, IP 주소 지정, 네트워크 접두사, Linux 네트워킹, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

CIDR(Classless Inter-Domain Routing) 은 서브넷 마스크를 더 간결하게 표현하는 데 사용됩니다. 10.42.3.0/255.255.255.0과 같은 서브넷이 10.42.3.0/24와 같이 표기된 CIDR 표기법을 볼 수 있습니다. 이 표기법은 서브넷 접두사와 서브넷 마스크를 모두 포함합니다.

IP 주소는 4 바이트 또는 32 비트로 구성된다는 것을 기억하십시오. CIDR 은 네트워크 접두사로 사용되는 비트 수를 나타냅니다. 따라서 123.12.24.0/23은 처음 23 비트가 사용된다는 것을 의미합니다. 이것은 무엇을 의미할까요? 호스트는 몇 개일까요?

간단한 요령은 IP 주소가 가질 수 있는 총 비트 수 (32) 에서 CIDR 주소 (23) 를 빼는 것입니다. 그러면 9 비트가 남습니다. 따라서 2^9 = 512 입니다. 그러나 2 개의 주소 (서브넷 주소 및 브로드캐스트 주소) 를 제거해야 하므로 510 개의 사용 가능한 호스트가 있습니다.

## Exercise

연습하면 완벽해집니다! CIDR, IP 주소 지정 및 서브넷팅에 대한 이해를 강화하기 위한 실습 랩은 다음과 같습니다.

1. **[Linux 터미널에서 IP 서브넷팅 및 이진 변환 수행](https://labex.io/ko/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - CIDR 마스크 변환 및 사용 가능한 호스트 계산을 포함하여 IP 서브넷팅 및 이진 변환을 마스터합니다.
2. **[Linux 에서 네트워크 계층 연결 시뮬레이션](https://labex.io/ko/labs/linux-simulate-network-layer-connectivity-in-linux-592752)** - 시뮬레이션된 환경에서 고정 IP 주소를 할당하고 IP 서브넷이 직접 네트워크 통신을 어떻게 제어하는지 관찰하는 방법을 배웁니다.
3. **[Linux 에서 IP 주소 유형 및 연결 가능성 탐색](https://labex.io/ko/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping` 및 `ip a`와 같은 명령을 사용하여 다양한 IP 유형 및 연결을 테스트하여 IP 주소 지정 및 네트워크 연결 가능성을 탐색합니다.

이러한 랩은 실제 시나리오에서 CIDR 및 IP 주소 지정 개념을 적용하고 네트워크 구성에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

질문이 없습니다. 계속 진행하세요!

## Quiz Answer
