---
index: 3
lang: "ko"
title: "traceroute"
meta_title: "traceroute - 문제 해결"
meta_description: "Linux traceroute 명령어를 사용하여 네트워크 경로를 추적하고 연결 문제를 해결하는 방법을 배웁니다. 초보자를 위한 TTL 및 패킷 라우팅을 이해합니다."
meta_keywords: "traceroute, Linux 네트워킹, 네트워크 문제 해결, TTL, Linux 명령어, 초보자, 튜토리얼"
---

## Lesson Content

`traceroute` 명령어는 패킷이 어떻게 라우팅되는지 확인하는 데 사용됩니다. 이 명령어는 TTL(Time To Live) 값을 1 부터 시작하여 점진적으로 증가시키면서 패킷을 전송하는 방식으로 작동합니다. 따라서 첫 번째 라우터는 패킷을 수신하고 TTL 값을 1 만큼 감소시켜 패킷을 드롭합니다. 라우터는 우리에게 ICMP Time Exceeded 메시지를 다시 보냅니다. 그런 다음, 다음 패킷은 TTL 이 2 가 되므로 첫 번째 라우터를 통과하지만, 두 번째 라우터에 도달하면 TTL 이 0 이 되어 또 다른 ICMP Time Exceeded 메시지를 반환합니다. Traceroute 는 패킷을 전송하고 드롭하면서 대상에 최종적으로 도달하여 ICMP Echo Reply 메시지를 수신할 때까지 패킷이 통과하는 라우터 목록을 구축하는 방식으로 작동합니다.

다음은 traceroute 의 작은 예시입니다:

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

각 줄은 사용자와 대상 사이에 있는 라우터 또는 머신을 나타냅니다. 대상의 이름과 IP 주소를 보여주며, 마지막 세 열은 해당 라우터에 도달하는 패킷의 왕복 시간을 나타냅니다. 기본적으로 경로를 따라 세 개의 패킷이 전송됩니다.

## Exercise

연습이 완벽을 만듭니다! 네트워크 경로 검색 및 문제 해결에 대한 이해를 강화하기 위한 실습 랩이 있습니다:

1. **[Linux 에서 IP 주소 관리](https://labex.io/ko/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip` 명령어를 사용하여 네트워크 설정을 구성하고 `traceroute`로 연결을 확인하는 연습을 합니다.
2. **[Linux 에서 ping 및 arp 를 사용하여 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` 및 `arp`가 어떻게 작동하여 네트워크 계층 상호 작용을 이해하는지 배우고, 이는 `traceroute`가 작동하는 방식의 기초가 됩니다.

이러한 랩은 실제 시나리오에서 네트워크 진단 개념을 적용하고 Linux 네트워킹 도구에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

네트워크를 가로질러 홉을 만들 때 무엇이 1 씩 감소합니까?

## Quiz Answer

TTL
