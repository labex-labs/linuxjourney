---
index: 1
lang: "ko"
title: "IPv4"
meta_title: "IPv4 - 서브넷팅"
meta_description: "완벽한 리눅스 튜토리얼로 IPv4 주소 학습을 시작하세요. 초보 리눅스 사용자를 위한 이 가이드는 IP 구조 및 ip addr 와 같은 필수 명령줄 도구를 다루며 리눅스 네트워킹을 배우는 가장 좋은 방법입니다."
meta_keywords: "IPv4, IP 주소, 초보 리눅스, 리눅스 학습 최고의 방법, 완벽한 리눅스 튜토리얼, 무료 온라인 리눅스 강좌, 무료 리눅스 자격증 과정, 리눅스 네트워킹, ifconfig, ip addr"
---

## Lesson Content

네트워크의 모든 장치에는 IP(인터넷 프로토콜) 주소라는 고유 식별자가 있습니다. 이 강의는 `완벽한 리눅스 튜토리얼`의 핵심 부분으로, 가장 일반적으로 접하게 될 IPv4 주소에 중점을 둡니다. 모든 `초보 리눅스` 사용자에게 IPv4 를 이해하는 것은 네트워킹 세계로 들어가는 중요한 첫걸음입니다.

### IPv4 가 필수적인 이유

시스템 관리나 네트워크 관리에 진지한 사람이라면 IPv4 에 대해 배우는 것이 기본입니다. 이는 대부분의 네트워크 통신의 기반을 형성합니다. 이 가이드는 네트워킹을 처음부터 배울 수 있는 `최고의 방법`을 제공합니다. 이것이 `무료 리눅스 자격증 과정` 중 하나는 아니지만, 이러한 기본 사항을 숙달하는 것은 전문 자격증을 향한 중요한 단계입니다.

### IPv4 주소 구조

IPv4 주소는 32 비트 숫자이지만, 일반적으로 다음과 같이 사람이 읽을 수 있는 형식으로 표시됩니다.

```
204.23.124.23
```

이 주소에는 네트워크를 식별하는 **네트워크 부분**과 해당 네트워크의 특정 장치를 식별하는 **호스트 부분**이라는 두 가지 주요 부분이 있습니다. 주소는 점으로 구분된 네 부분으로 나뉘며, 각 부분을 **옥텟 (octet)**이라고 합니다. 옥텟은 8 비트의 그룹이므로 IPv4 주소는 4 바이트 (32 비트) 길이입니다. 이 구조를 이해하는 것은 네트워크 구성 및 문제 해결에 매우 중요합니다.

### IP 주소 찾기

모든 리눅스 사용자의 첫 번째 작업 중 하나는 시스템의 IP 주소를 찾는 것입니다. 간단한 명령줄 도구를 사용하여 이 작업을 수행할 수 있습니다. 이를 위한 전통적인 명령은 `ifconfig`입니다. 여전히 많은 시스템에서 발견되지만 레거시 도구로 간주됩니다.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

위 출력에서 IPv4 주소는 `192.168.1.129`입니다.

### ip addr 명령어 사용

현대적이고 권장되는 방법은 `ip` 명령어를 사용하는 것입니다. `ip addr` 명령어는 `ifconfig`를 대체했으며 대부분의 최신 리눅스 배포판에서 표준입니다. 더 자세한 정보를 제공하며 학습에 집중해야 할 도구입니다.

```bash
pete@icebox:~$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 1d:3a:32:24:4d:ce brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.129/24 brd 192.168.1.255 scope global dynamic eth0
       valid_lft 85646sec preferred_lft 85646sec
```

여기서 `eth0` 인터페이스에 대해 `inet` 옆에 동일한 IPv4 주소인 `192.168.1.129`를 찾을 수 있습니다.

## Exercise

IP 주소 지정 및 리눅스에서 네트워크 식별에 대한 이해를 강화하기 위해 다음 실습 랩을 통해 기술을 연습해 보세요:

1. **[리눅스에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령어를 사용하여 리눅스 시스템에서 IPv4 및 IPv6 주소를 포함한 네트워크 주소 지정 정보를 식별하는 연습을 합니다.
2. **[리눅스에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping` 및 `ip a`와 같은 명령어를 사용하여 다양한 IP 주소 유형을 탐색하고 네트워크 도달 가능성을 테스트합니다.
3. **[리눅스 터미널에서 IP 서브넷팅 및 이진 변환 수행](https://labex.io/ko/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - IP 주소와 네트워크가 비트 수준에서 구성되는 방식을 더 깊이 이해하는 데 필수적인 IP 서브넷팅 및 이진 변환을 마스터합니다.

이러한 랩은 실제 시나리오에서 IP 주소 지정 개념을 적용하고 리눅스에서 네트워크 구성 및 문제 해결에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

IPv4 주소는 몇 바이트로 구성되어 있습니까?

## Quiz Answer

4
