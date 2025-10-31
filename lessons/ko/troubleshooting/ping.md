---
index: 2
lang: "ko"
title: "핑"
meta_title: "ping - 문제 해결"
meta_description: "Linux ping 명령어를 사용하여 네트워크 연결 상태를 테스트하는 방법을 알아보세요. 이 가이드는 icmp_seq, TTL 및 왕복 시간 (roundtrip time) 을 포함한 ping 출력 해석 방법을 설명합니다. 네트워크 문제를 진단하기 위해 ping 시퀀스를 이해하는 방법을 알아보세요."
meta_keywords: "Linux ping, 네트워크 연결, ICMP, TTL, ping 명령어, icmp_seq, ping 시퀀스, icmp seq, icmp_seq 의미, ping icmp_seq, Linux 네트워킹"
---

## Lesson Content

**ping** 명령어는 원격 호스트가 IP 네트워크를 통해 도달 가능한지 테스트하는 데 사용되는 가장 기본적인 네트워킹 유틸리티 중 하나입니다. 이 명령어는 대상 호스트에 ICMP(Internet Control Message Protocol) "에코 요청" 패킷을 보내고 ICMP "에코 응답"을 기다리는 방식으로 작동합니다. 요청 패킷이 전송되고 응답이 수신되면 성공적인 ping 으로 간주됩니다.

실행 중인 일반적인 `ping` 명령어를 살펴보겠습니다.

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

이 예시에서 우리는 `ping`을 사용하여 `www.google.com`에 대한 연결 상태를 확인합니다. `-c 3` 옵션은 `ping`에게 정확히 세 개의 에코 요청 패킷을 보내고 중지하도록 지시합니다. 기본적으로 `ping`은 초당 하나의 패킷을 보냅니다.

### Ping 출력 이해하기

`ping icmp_seq` 명령어의 출력은 유용한 진단 정보를 제공합니다. 주요 구성 요소를 분석해 보겠습니다.

### ICMP 시퀀스 (icmp_seq)

`icmp_seq` 필드는 각 ICMP 패킷의 시퀀스 번호를 표시합니다. 예시에서 우리는 세 개의 패킷을 보냈고, 출력은 세 개 모두 (`icmp_seq=1`, `icmp_seq=2`, `icmp_seq=3`) 성공적으로 반환되었음을 보여줍니다. `ping seq`는 패킷 손실을 진단하는 데 중요합니다. 시퀀스 번호가 누락된 경우, 일부 패킷이 목적지에 도달하지 못했거나 돌아오지 못하는 연결 문제를 나타냅니다. `icmp seq` 번호가 순서가 맞지 않게 나타나면, 패킷이 왕복하는 데 기본 1 초 간격보다 더 오래 걸리고 있음을 의미하므로 네트워크 혼잡이나 지연을 시사할 수 있습니다. `icmp_seq meaning`을 이해하는 것이 문제 해결의 핵심입니다.

### Time To Live (TTL)

Time To Live (TTL) 필드는 패킷의 홉 카운터 역할을 합니다. 패킷이 라우터 (한 "홉") 를 통과할 때마다 TTL 값이 1 씩 감소합니다. 패킷이 목적지에 도착하기 전에 카운터가 0 에 도달하면 패킷은 폐기됩니다. 이 메커니즘은 패킷이 네트워크에서 끝없이 순환하는 것을 방지합니다.

### 시간 (Time)

`time` 필드는 왕복 시간, 즉 패킷이 내 컴퓨터에서 대상 호스트까지 이동하고 에코 응답이 돌아오는 데 걸린 시간을 측정합니다. 이 값은 일반적으로 밀리초 (ms) 단위로 측정되며 네트워크 지연의 주요 지표입니다.

## Exercise

네트워크 진단을 마스터하려면 연습이 필수적입니다. 다음 실습 랩은 `ping` 명령어에 대한 이해를 강화하는 데 도움이 될 것입니다.

1. **[Linux 에서 ping 및 arp 를 사용하여 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping`과 `arp`를 사용하여 네트워크 및 데이터 링크 계층 상호 작용을 탐색하고 기본 게이트웨이가 원격 트래픽을 처리하는 방식을 관찰합니다.
2. **[Linux 에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping`과 `ip a`를 활용하여 로컬 TCP/IP 스택을 테스트하고, 공용 인터넷 연결을 확인하며, 네트워크 도달 가능성을 탐색합니다.
3. **[Linux 에서 네트워크 계층 연결 시뮬레이션](https://labex.io/ko/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - `ip addr`를 사용하여 정적 IP 주소를 할당하고 동일 및 다른 서브넷에서 `ping`으로 연결을 테스트하는 방법을 배웁니다.

이 랩들은 네트워크 도달 가능성 및 `ping` 명령어 개념을 실제 시나리오에 적용하여 Linux 에서 네트워크 진단에 대한 자신감을 높이는 데 도움이 될 것입니다.

## Quiz Question

왕복 시간의 측정 단위는 무엇입니까? 대소문자를 구분하여 영어로 답변하십시오.

## Quiz Answer

ms
