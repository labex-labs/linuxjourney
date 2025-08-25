---
index: 1
lang: "ko"
title: "IPv4"
meta_title: "IPv4 - 서브넷팅"
meta_description: "IPv4 주소, 구조 및 ifconfig 를 사용하여 IP 를 찾는 방법을 알아보세요. Linux 초보자를 위한 네트워크 기본 사항을 이해합니다."
meta_keywords: "IPv4, IP 주소, ifconfig, 네트워크 기본 사항, Linux 네트워킹, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

네트워크 호스트는 고유한 주소를 가지고 있으며, 이 주소를 통해 호스트를 찾을 수 있습니다. 이러한 주소를 IP 주소라고 합니다. IPv4 주소는 다음과 같이 생겼습니다:

```
204.23.124.23
```

이 주소는 실제로 두 부분으로 구성됩니다: 어떤 네트워크에 있는지 알려주는 네트워크 부분과 해당 네트워크에서 어떤 호스트인지 알려주는 호스트 부분입니다. 이 과정에서는 주로 IPv4 주소에 대해 다룰 것입니다. 이는 일반적으로 IP 주소를 언급할 때 보게 될 주소입니다.

IP 주소는 마침표로 옥텟으로 구분됩니다. 따라서 IPv4 주소에는 4 개의 옥텟이 있습니다. 컴퓨터 과학을 조금 아신다면, 옥텟은 8 비트이고, 8 비트는 실제로 1 바이트와 같으므로, IPv4 주소는 4 바이트를 가진다고도 말합니다. 서브넷과 IP 주소를 다룰 때 비트를 자주 사용합니다.

`ifconfig -a` 명령으로 IP 주소를 확인할 수 있습니다:

```bash
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

보시다시피, 제 IPv4 주소는 192.168.1.129 입니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 에서 IP 주소 지정 및 네트워크 식별에 대한 이해를 강화하기 위한 실습입니다:

1. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 Linux 시스템에서 IPv4 및 IPv6 주소를 포함한 네트워크 주소 지정 정보를 식별하는 연습을 합니다.
2. **[Linux 에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping` 및 `ip a`와 같은 명령을 사용하여 다양한 IP 주소 유형을 탐색하고 네트워크 도달 가능성을 테스트합니다.
3. **[Linux 터미널에서 IP 서브넷팅 및 이진 변환 수행](https://labex.io/ko/labs/linux-perform-ip-subnetting-and-binary-conversion-in-the-linux-terminal-592782)** - IP 주소와 네트워크가 비트 수준에서 어떻게 구성되는지에 대한 더 깊은 이해를 위해 필수적인 IP 서브넷팅 및 이진 변환을 마스터합니다.

이 실습들은 실제 시나리오에서 IP 주소 지정 개념을 적용하고 Linux 에서 네트워크 구성 및 문제 해결에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

IPv4 주소는 몇 바이트입니까?

## Quiz Answer

4
