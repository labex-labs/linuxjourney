---
index: 2
lang: "ko"
title: "라우팅 테이블"
meta_title: "라우팅 테이블 - 라우팅"
meta_description: "Linux 라우팅 테이블을 이해하고 route 명령을 사용하여 패킷이 어떻게 라우팅되는지 배웁니다. 네트워크 기본 사항을 위해 대상, 게이트웨이 및 인터페이스를 탐색합니다."
meta_keywords: "Linux 라우팅 테이블, route 명령, 네트워크 라우팅, Linux 네트워킹, Linux 초보자, Linux 튜토리얼, 네트워크 가이드"
---

## Lesson Content

머신의 라우팅 테이블을 살펴보세요:

```plaintext
pete@icebox:~$ sudo route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.224.2   0.0.0.0         UG    0      0        0 eth0
192.168.224.0   0.0.0.0         255.255.255.0   U     1      0        0 eth0
```

### Destination

첫 번째 필드에는 192.168.224.0 의 대상 IP 주소가 있습니다. 이는 이 네트워크로 가려고 하는 모든 패킷이 이더넷 케이블 (eth0) 을 통해 나간다는 것을 의미합니다. 만약 제가 192.168.224.5 이고 192.168.224.7 로 가고 싶다면, 단순히 네트워크 인터페이스 eth0 을 직접 사용할 것입니다.

**0.0.0.0** 주소가 있음을 주목하세요. 이는 주소가 지정되지 않았거나 알 수 없음을 의미합니다. 따라서 예를 들어, IP 주소 151.123.43.6 으로 패킷을 보내고 싶지만, 라우팅 테이블이 어디로 가는지 모른다면, 0.0.0.0 으로 표시하고 따라서 패킷을 Gateway 로 라우팅합니다.

### Gateway

동일한 네트워크에 있지 않은 패킷을 보내는 경우, 이 Gateway 주소로 전송됩니다. 이 이름은 다른 네트워크로 가는 Gateway 라는 의미에 적합합니다.

### Genmask

이것은 서브넷 마스크이며, 어떤 IP 주소가 어떤 대상과 일치하는지 파악하는 데 사용됩니다.

### Flags

- UG - 네트워크가 Up 상태이고 Gateway 입니다.
- U - 네트워크가 Up 상태입니다.

### Iface

이것은 패킷이 나갈 인터페이스입니다. eth0 은 일반적으로 시스템의 첫 번째 이더넷 장치를 의미합니다.

## Exercise

라우팅 테이블을 살펴보고 패킷이 어디로 갈 수 있는지 확인하세요.

## Quiz Question

라우팅 테이블이 알 수 없는 경우 패킷은 어디로 라우팅됩니까?

## Quiz Answer

Gateway
