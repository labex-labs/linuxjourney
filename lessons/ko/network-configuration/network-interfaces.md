---
lang: "ko"
title: "네트워크 인터페이스"
description: "Linux 네트워크 인터페이스, ifconfig, ip 명령에 대해 알아보세요. 네트워크 설정을 구성하고 관리하는 방법을 이해하세요. Linux 네트워킹 여정을 시작하세요!"
keywords: "Linux 네트워크 인터페이스, ifconfig, ip command, 네트워크 구성, Linux 네트워킹, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

네트워크 인터페이스는 커널이 네트워킹의 소프트웨어 측면과 하드웨어 측면을 연결하는 방식입니다. 우리는 이미 이것의 예를 보았습니다:

```plaintext
pete@icebox:~$ ifconfig -a
eth0      Link encap:Ethernet  HWaddr 1d:3a:32:24:4d:ce
          inet addr:192.168.1.129  Bcast:192.168.1.255  Mask:255.255.255.0
          inet6 addr: fd60::21c:29ff:fe63:5cdc/64 Scope:Link
```

### The ifconfig command

**ifconfig** 도구는 네트워크 인터페이스를 구성할 수 있게 해줍니다. 설정된 네트워크 인터페이스가 없으면 커널의 장치 드라이버와 네트워크는 서로 통신하는 방법을 알지 못합니다. ifconfig 는 부팅 시 실행되어 구성 파일을 통해 인터페이스를 구성하지만, 수동으로 수정할 수도 있습니다. ifconfig 의 출력은 왼쪽에 인터페이스 이름을 보여주고, 오른쪽에는 자세한 정보를 보여줍니다. 가장 일반적으로 eth0 (머신의 첫 번째 이더넷 카드), wlan0 (무선 인터페이스), lo (루프백 인터페이스) 와 같은 이름의 인터페이스를 보게 될 것입니다. 루프백 인터페이스는 컴퓨터를 나타내는 데 사용됩니다. 단순히 자신에게 다시 루프백됩니다. 이는 디버깅이나 로컬에서 실행되는 서버에 연결하는 데 유용합니다.

인터페이스의 상태는 up 또는 down 일 수 있습니다. 짐작할 수 있듯이, 인터페이스를 "끄고" 싶다면 down 으로 설정할 수 있습니다. ifconfig 출력에서 가장 많이 보게 될 필드는 HWaddr (인터페이스의 MAC 주소), inet address (IPv4 주소), inet6 (IPv6 주소) 입니다. 물론 서브넷 마스크와 브로드캐스트 주소도 거기에 있음을 알 수 있습니다. /etc/network/interfaces에서도 인터페이스 정보를 볼 수 있습니다.

### To create an interface and bring it up

```bash
ifconfig eth0 192.168.2.1 netmask 255.255.255.0 up
```

이것은 eth0 인터페이스에 IP 주소와 넷마스크를 할당하고, 또한 인터페이스를 활성화합니다.

### To bring up or down an interface

```bash
ifup eth0
ifdown eth0
```

### The ip command

**ip** 명령은 또한 시스템의 네트워킹 스택을 조작할 수 있게 해줍니다. 사용 중인 배포판에 따라 네트워크 설정을 조작하는 데 선호되는 방법일 수 있습니다.

다음은 사용 예시입니다:

### To show interface information for all interfaces

```bash
ip link show
```

### To show the statistics of an interface

```bash
ip -s link show eth0
```

### To show IP addresses allocated to interfaces

```bash
ip address show
```

### To bring interfaces up and down

```bash
ip link set eth0 up
ip link set eth0 down
```

### To add an IP address to an interface

```bash
ip address add 192.168.1.1/24 dev eth0
```

## Exercise

네트워크 인터페이스의 상태를 up 또는 down 으로 변경하고 어떤 일이 발생하는지 관찰해 보세요.

ifconfig 와 ip 명령을 모두 사용하여 네트워크 인터페이스를 변경할 수 있습니까?

## Quiz Question

네트워크 인터페이스를 구성하는 명령은 무엇입니까?

## Quiz Answer

ifconfig
