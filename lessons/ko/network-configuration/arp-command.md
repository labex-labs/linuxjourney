---
lang: "ko"
title: "arp"
meta_title: "arp - 네트워크 구성"
meta_description: "Linux ARP 명령과 ARP 캐시를 확인하는 방법을 알아보세요. 네트워크 통신에서 ARP 의 역할을 이해합니다. ARP 초보자 가이드."
meta_keywords: "Linux ARP, ARP 캐시, ip neighbour show, 네트워크 명령, Linux 네트워킹, 초보자 Linux, Linux 튜토리얼"
---

## Lesson Content

ARP 로 MAC 주소를 찾을 때, 먼저 시스템에 로컬로 저장된 ARP 캐시를 확인한다는 것을 기억하세요. 이 캐시를 실제로 볼 수 있습니다:

```
pete@icebox:~$ arp
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.22.1            ether   00:12:24:fc:12:cc   C                     eth0
192.168.22.254          ether   00:12:45:f2:84:64   C                     eth0
```

ARP 캐시는 머신이 부팅될 때 실제로 비어 있습니다. 패킷이 다른 호스트로 전송되면서 채워집니다. ARP 캐시에 없는 대상으로 패킷을 보내면 다음이 발생합니다:

1. 소스 호스트는 ARP 요청 패킷으로 이더넷 프레임을 생성합니다.
2. 소스 호스트는 이 프레임을 전체 네트워크에 브로드캐스트합니다.
3. 네트워크의 호스트 중 하나가 올바른 MAC 주소를 알고 있다면, MAC 주소를 포함하는 응답 패킷과 프레임을 보냅니다.
4. 소스 호스트는 IP-MAC 주소 매핑을 ARP 캐시에 추가한 다음 패킷 전송을 진행합니다.

`ip` 명령을 통해 ARP 캐시를 볼 수도 있습니다:

```bash
ip neighbour show
```

## Exercise

머신을 재부팅한 다음 네트워크에서 작업을 수행할 때 ARP 캐시에 어떤 변화가 생기는지 관찰하십시오.

## Quiz Question

ARP 캐시를 확인하는 데 사용할 수 있는 명령은 무엇입니까?

## Quiz Answer

arp
