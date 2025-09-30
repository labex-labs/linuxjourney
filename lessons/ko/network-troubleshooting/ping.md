---
index: 2
lang: "ko"
title: "ping"
meta_title: "ping - 문제 해결"
meta_description: "Linux ping 명령을 사용하여 네트워크 연결을 테스트하고 문제를 해결하는 방법을 배웁니다. 효과적인 네트워크 진단을 위해 ICMP, TTL 및 왕복 시간을 이해합니다."
meta_keywords: "Linux ping, 네트워크 연결, ICMP, TTL, Linux 네트워킹, 초보자 Linux, Linux 튜토리얼, ping 명령"
---

## Lesson Content

가장 간단한 네트워킹 도구 중 하나인 **ping**은 패킷이 호스트에 도달할 수 있는지 여부를 테스트하는 데 사용됩니다. 이 도구는 ICMP 에코 요청 (유형 8) 패킷을 대상 호스트로 보내고 ICMP 에코 응답 (유형 0) 을 기다리는 방식으로 작동합니다. 호스트가 요청 패킷을 보내고 대상으로부터 응답을 받으면 Ping 이 성공합니다. 다음 예시를 살펴보겠습니다.

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

이 예시에서는 `www.google.com`에 도달할 수 있는지 확인하기 위해 ping 을 사용하고 있습니다. `-c` 플래그 (count) 는 지정된 횟수에 도달한 후 에코 요청 패킷 전송을 중지하는 데 사용됩니다.

첫 번째 부분은 74.125.239.112(google.com) 로 64 바이트 패킷을 보내고 있음을 나타내며, 나머지는 전송에 대한 세부 정보를 보여줍니다. 기본적으로 초당 하나의 패킷을 보냅니다.

### icmp_seq

`icmp_seq` 필드는 전송된 패킷의 시퀀스 번호를 표시하는 데 사용됩니다. 이 경우 3 개의 패킷을 보냈고, 3 개의 패킷이 모두 돌아온 것을 확인할 수 있습니다. ping 을 수행했는데 일부 시퀀스 번호가 누락된 경우, 이는 연결 문제가 발생하고 있으며 모든 패킷이 통과하지 못하고 있음을 의미합니다. 시퀀스 번호가 순서가 맞지 않으면 패킷이 기본 1 초를 초과하고 있으므로 연결이 매우 느릴 가능성이 높습니다.

### ttl

Time To Live (TTL) 필드는 홉 카운터로 사용됩니다. 홉을 수행할 때마다 카운터가 1 씩 감소하며, 홉 카운터가 0 에 도달하면 패킷은 소멸됩니다. 이는 패킷에 수명을 부여하기 위한 것으로, 패킷이 영원히 돌아다니는 것을 원치 않습니다.

### time

에코 요청 패킷을 보낸 시점부터 에코 응답을 받은 시점까지 걸린 왕복 시간입니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 네트워크 연결 및 `ping` 명령에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 ping 및 arp 를 사용하여 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` 및 `arp`를 사용하여 네트워크 및 데이터 링크 계층 상호 작용을 탐색하고 기본 게이트웨이가 원격 트래픽을 처리하는 방식을 관찰합니다.
2. **[Linux 에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping` 및 `ip a`를 활용하여 로컬 TCP/IP 스택을 테스트하고, 공용 인터넷 연결을 확인하며, 네트워크 도달 가능성을 탐색합니다.
3. **[Linux 에서 네트워크 계층 연결 시뮬레이션](https://labex.io/ko/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - `ip addr`로 고정 IP 주소를 할당하고 동일한 서브넷 및 다른 서브넷에서 `ping`으로 연결을 테스트하는 방법을 배웁니다.

이러한 실습은 실제 시나리오에서 네트워크 도달 가능성 및 `ping` 명령의 개념을 적용하고 Linux 에서 네트워크 진단에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

왕복 시간 측정 단위는 무엇입니까?

## Quiz Answer

ms
