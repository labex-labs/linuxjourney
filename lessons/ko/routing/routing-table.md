---
index: 2
lang: "ko"
title: "라우팅 테이블"
meta_title: "라우팅 테이블 - 라우팅"
meta_description: "Linux 라우팅 테이블을 이해하고 route 명령을 사용하여 패킷이 라우팅되는 방법을 배웁니다. 네트워크 기본 사항을 위한 대상, 게이트웨이 및 인터페이스를 탐색합니다."
meta_keywords: "Linux 라우팅 테이블, route 명령, 네트워크 라우팅, Linux 네트워킹, 초보자 Linux, Linux 튜토리얼, 네트워크 가이드"
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

### 대상

첫 번째 필드에는 대상 IP 주소 192.168.224.0 이 있습니다. 이는 이 네트워크로 이동하려는 모든 패킷이 이더넷 케이블 (eth0) 을 통해 나간다는 것을 의미합니다. 만약 제가 192.168.224.5 이고 192.168.224.7 로 가고 싶다면, 단순히 네트워크 인터페이스 eth0 을 직접 사용할 것입니다.

**0.0.0.0** 주소가 있음을 주목하세요. 이는 주소가 지정되지 않았거나 알 수 없음을 의미합니다. 따라서 예를 들어, IP 주소 151.123.43.6 으로 패킷을 보내고 싶지만 라우팅 테이블이 어디로 가는지 모른다면, 0.0.0.0 으로 표시하고 패킷을 Gateway 로 라우팅합니다.

### 게이트웨이

동일한 네트워크에 있지 않은 패킷을 보내는 경우, 다른 네트워크로의 Gateway 라고 적절하게 명명된 이 Gateway 주소로 전송됩니다.

### Genmask

이것은 서브넷 마스크이며, 어떤 IP 주소가 어떤 대상과 일치하는지 파악하는 데 사용됩니다.

### 플래그

- UG - 네트워크가 활성화 (Up) 되어 있고 게이트웨이 (Gateway) 입니다.
- U - 네트워크가 활성화 (Up) 되어 있습니다.

### Iface

이것은 패킷이 나갈 인터페이스입니다. eth0 은 일반적으로 시스템의 첫 번째 이더넷 장치를 의미합니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 네트워크 라우팅 및 IP 주소 지정에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 IP 주소 및 네트워크 인터페이스를 포함한 네트워크 주소 지정 정보를 식별하는 연습을 합니다. 이는 라우팅 테이블의 핵심 구성 요소입니다.
2. **[Linux 에서 IP 주소 지정 관리](https://labex.io/ko/labs/linux-manage-ip-addressing-in-linux-592736)** - IP 주소 지정을 관리하고, 고정 IP 를 구성하고, 기본 게이트웨이를 설정하고, 네트워크 구성을 확인하는 방법을 배웁니다. 이는 라우팅 테이블에서 찾을 수 있는 항목과 직접 관련이 있습니다.
3. **[Linux 에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping` 및 `ip a`를 사용하여 IP 주소 지정 및 네트워크 도달 가능성을 탐색하여 다양한 IP 유형이 어떻게 상호 작용하고 네트워크 도달 가능성이 어떻게 결정되는지 이해하는 데 도움이 됩니다. 이는 라우팅 결정에 반영됩니다.

이러한 실습은 실제 시나리오에 개념을 적용하고 네트워크 구성 및 문제 해결에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

라우팅 테이블이 알 수 없는 경우 패킷은 어디로 라우팅됩니까?

## Quiz Answer

Gateway
