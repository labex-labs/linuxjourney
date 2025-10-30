---
index: 1
lang: "ko"
title: "IPv4"
meta_title: "IPv4 - 서브넷팅"
meta_description: "IPv4 주소를 이해하여 Linux 네트워킹을 배우는 가장 좋은 방법을 알아보세요. 이 초보자 가이드는 IP 구조와 명령줄을 사용하여 IP 를 찾는 방법을 다룹니다."
meta_keywords: "IPv4, IP 주소, 리눅스 초보자, 리눅스 학습 최고의 방법, 리눅스 명령줄 초보자, ifconfig, ip addr, 네트워크 기초"
---

## Lesson Content

네트워크에 연결된 모든 장치에는 IP(인터넷 프로토콜) 주소라고 하는 고유한 주소가 있습니다. 이 과정에서는 가장 일반적으로 접하게 될 IPv4 주소에 중점을 둘 것입니다. IPv4 주소를 이해하는 것은 Linux 에서 네트워킹을 배우는 핵심적인 부분입니다.

IPv4 주소는 일반적으로 다음과 같이 사람이 읽을 수 있는 형식으로 표시되는 32 비트 숫자입니다.

```
204.23.124.23
```

이 주소에는 두 가지 뚜렷한 부분이 포함됩니다. 장치가 속한 특정 네트워크를 식별하는 **네트워크 부분**과 해당 네트워크에서 특정 장치를 식별하는 **호스트 부분**입니다.

### IP 주소의 구조

IPv4 주소는 마침표로 구분된 네 부분으로 나뉩니다. 각 부분을 **옥텟 (octet)**이라고 합니다. 컴퓨터 과학에서 옥텟은 8 비트의 그룹이며, 8 비트가 1 바이트와 같으므로 IPv4 주소는 길이가 4 바이트입니다. 이 구조는 기본이며, 이를 숙달하는 것은 네트워킹에서 `초보자를 위한 리눅스 명령어 학습을 위한 최고의 자료` 중 하나입니다.

### Linux 에서 IP 주소 찾기

모든 `초보자 리눅스` 사용자에게 첫 번째 작업 중 하나는 시스템의 IP 주소를 찾는 것입니다. 명령줄 도구를 사용하여 이 작업을 수행할 수 있습니다.

이를 위한 전통적인 명령어는 `ifconfig`입니다. 여전히 많은 시스템에서 발견되지만 레거시 도구로 간주됩니다.

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

위 출력에서 IPv4 주소는 `192.168.1.129`입니다.

### ip addr 을 사용한 최신 접근 방식

오늘날 리눅스 네트워킹을 배우는 `가장 좋은 방법`은 최신 `ip` 명령어를 사용하는 것입니다. `ip addr` 명령어는 `ifconfig`를 대체했으며 대부분의 최신 Linux 배포판에서 표준입니다.

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

IP 주소 지정 및 Linux 에서의 네트워크 식별에 대한 이해를 강화하기 위해 다음 실습 랩을 통해 기술을 연습하십시오.

1. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령어를 사용하여 Linux 시스템에서 IPv4 및 IPv6 주소를 포함한 네트워크 주소 지정 정보를 식별하는 연습을 합니다.
2. **[Linux 에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 다양한 IP 주소 유형을 탐색하고 `ping` 및 `ip a`와 같은 명령어를 사용하여 네트워크 도달 가능성을 테스트합니다.
3. **[Linux 터미널에서 IP 서브넷팅 및 이진 변환 수행](https://labex.io/ko/labs/comptia-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - IP 주소와 네트워크가 비트 수준에서 구성되는 방식을 더 깊이 이해하는 데 필수적인 IP 서브넷팅 및 이진 변환을 마스터합니다.

이 랩들은 실제 시나리오에서 IP 주소 지정 개념을 적용하고 Linux 에서 네트워크 구성 및 문제 해결에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

IPv4 주소는 몇 바이트로 구성되어 있습니까?

## Quiz Answer

4
