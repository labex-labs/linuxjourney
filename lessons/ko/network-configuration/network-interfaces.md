---
index: 1
lang: "ko"
title: "네트워크 인터페이스"
meta_title: "네트워크 인터페이스 - 네트워크 구성"
meta_description: "Linux 네트워크 인터페이스, ifconfig 및 ip 명령어에 대해 알아보세요. 네트워크 설정을 구성하고 관리하는 방법을 이해하세요. Linux 네트워킹 여정을 시작하세요!"
meta_keywords: "Linux 네트워크 인터페이스, ifconfig, ip 명령어, 네트워크 구성, Linux 네트워킹, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

네트워크 인터페이스는 커널이 네트워킹의 소프트웨어 측면을 하드웨어 측면에 연결하는 방법입니다. 우리는 이미 이것의 예를 보았습니다:

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### ifconfig 명령어

**ifconfig** 도구를 사용하면 네트워크 인터페이스를 구성할 수 있습니다. 네트워크 인터페이스가 설정되어 있지 않으면 커널의 장치 드라이버와 네트워크가 서로 통신하는 방법을 알 수 없습니다. ifconfig 는 부팅 시 실행되어 구성 파일을 통해 인터페이스를 구성하지만, 수동으로 수정할 수도 있습니다. ifconfig 의 출력은 왼쪽에 인터페이스 이름을 표시하고 오른쪽에 자세한 정보를 표시합니다. 일반적으로 eth0 (머신의 첫 번째 이더넷 카드), wlan0 (무선 인터페이스), lo (루프백 인터페이스) 와 같은 인터페이스 이름을 볼 수 있습니다. 루프백 인터페이스는 컴퓨터를 나타내는 데 사용됩니다. 자신에게 다시 루프백됩니다. 이는 디버깅 또는 로컬에서 실행되는 서버에 연결하는 데 유용합니다.

인터페이스의 상태는 up 또는 down 일 수 있습니다. 짐작할 수 있듯이 인터페이스를 "끄고" 싶다면 down 으로 설정할 수 있습니다. ifconfig 출력에서 가장 많이 보게 될 필드는 HWaddr (인터페이스의 MAC 주소), inet address (IPv4 주소), inet6 (IPv6 주소) 입니다. 물론 서브넷 마스크와 브로드캐스트 주소도 있습니다. /etc/network/interfaces에서 인터페이스 정보를 볼 수도 있습니다.

### 인터페이스를 생성하고 활성화하는 방법

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

이것은 eth0 인터페이스에 IP 주소와 넷마스크를 할당하고 활성화합니다.

### 인터페이스를 활성화하거나 비활성화하는 방법

```bash
ifup eth0
ifdown eth0
```

### ip 명령어

**ip** 명령어를 사용하면 시스템의 네트워킹 스택을 조작할 수도 있습니다. 사용 중인 배포판에 따라 네트워크 설정을 조작하는 데 선호되는 방법일 수 있습니다.

다음은 사용 예시입니다:

### 모든 인터페이스의 정보 표시

```bash
ip link show
```

### 인터페이스 통계 표시

```bash
ip -s link show eth0
```

### 인터페이스에 할당된 IP 주소 표시

```bash
ip address show
```

### 인터페이스 활성화 및 비활성화

```bash
ip link set eth0 up
ip link set eth0 down
```

### 인터페이스에 IP 주소 추가

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

연습하면 완벽해집니다! 다음은 네트워크 인터페이스 및 IP 주소 지정에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 Linux 시스템에서 MAC, IPv4 및 IPv6 주소를 포함한 네트워크 주소 지정 정보를 식별하는 연습을 합니다.
2. **[Linux 에서 IP 주소 지정 관리](https://labex.io/ko/labs/linux-manage-ip-addressing-in-linux-592736)** - `ip` 명령을 사용하여 고정 및 동적 IP 주소를 구성하고, 기본 게이트웨이를 설정하고, 네트워크 구성을 확인하는 방법을 배웁니다.
3. **[Linux 에서 IP 주소 유형 및 연결 가능성 탐색](https://labex.io/ko/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - `ping` 및 `ip a`를 사용하여 다양한 IP 주소 유형 (사설, 공용, 멀티캐스트) 을 탐색하고 네트워크 연결 가능성을 테스트합니다.

이러한 랩은 실제 시나리오에서 네트워크 인터페이스 식별 및 IP 주소 지정 개념을 적용하고 Linux 네트워킹에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

네트워크 인터페이스를 구성하는 명령어는 무엇입니까?

## Quiz Answer

ifconfig
