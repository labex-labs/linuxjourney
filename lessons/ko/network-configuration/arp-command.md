---
index: 5
lang: "ko"
title: "arp"
meta_title: "arp - 네트워크 구성"
meta_description: "Linux ARP 명령과 ARP 캐시를 보는 방법을 알아보세요. 네트워크 통신에서 ARP 의 역할을 이해하세요. ARP 초보자 가이드입니다."
meta_keywords: "Linux ARP, ARP 캐시, ip neighbour show, 네트워크 명령, Linux 네트워킹, 초보자 Linux, Linux 튜토리얼"
---

## Lesson Content

ARP 로 MAC 주소를 찾을 때, 시스템에 로컬로 저장된 ARP 캐시를 먼저 확인한다는 것을 기억하십시오. 이 캐시를 실제로 볼 수 있습니다:

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

ARP 캐시는 머신이 부팅될 때 실제로 비어 있습니다. 패킷이 다른 호스트로 전송될 때 채워집니다. ARP 캐시에 없는 대상으로 패킷을 보내면 다음이 발생합니다:

1. 소스 호스트는 ARP 요청 패킷으로 이더넷 프레임을 생성합니다.
2. 소스 호스트는 이 프레임을 전체 네트워크에 브로드캐스트합니다.
3. 네트워크의 호스트 중 하나가 올바른 MAC 주소를 알고 있다면, MAC 주소를 포함하는 응답 패킷과 프레임을 보낼 것입니다.
4. 소스 호스트는 IP-MAC 주소 매핑을 ARP 캐시에 추가한 다음 패킷 전송을 진행합니다.

`ip` 명령을 통해 ARP 캐시를 볼 수도 있습니다:

```bash
ip neighbour show
```

## Exercise

연습이 완벽을 만듭니다! ARP 및 네트워크 계층 상호 작용에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 ping 및 arp 를 사용하여 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` 및 `arp` 명령을 사용하여 IP 주소가 MAC 주소로 어떻게 확인되는지, 그리고 기본 게이트웨이가 트래픽을 어떻게 처리하는지 관찰합니다.
2. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 MAC 및 IP 주소를 포함한 네트워크 주소 지정 정보를 식별하는 방법을 배웁니다. 이는 ARP 를 이해하는 데 기본적입니다.
3. **[Linux 에서 IP 주소 지정 관리](https://labex.io/ko/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip` 명령을 사용하여 IP 주소 지정을 관리하고 `arp` 및 `traceroute`로 네트워크 구성을 확인하는 연습을 합니다.

이 랩들은 실제 시나리오에서 ARP 및 네트워크 주소 지정 개념을 적용하고 Linux 네트워킹에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

ARP 캐시를 확인하는 데 사용할 수 있는 명령은 무엇입니까?

## Quiz Answer

arp
