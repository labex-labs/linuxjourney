---
index: 2
lang: "ko"
title: "route"
meta_title: "route - 네트워크 구성"
meta_description: "Linux route 및 ip 명령을 사용하여 네트워크 경로를 추가하고 삭제하는 방법을 배웁니다. 초보자 및 중급 사용자를 위한 라우팅 테이블 관리를 이해합니다."
meta_keywords: "route command, ip route, add route, delete route, Linux networking, routing table, Linux tutorial, beginner guide"
---

## Lesson Content

`route` 명령을 사용하여 라우팅 테이블을 보는 방법에 대해 이미 논의했습니다. 경로를 추가하거나 제거하려면 수동으로 수행할 수 있습니다.

### 새 경로 추가

```bash
sudo route add -net 192.168.2.1/23 gw 10.11.12.3
```

### 경로 삭제

```bash
sudo route del -net 192.168.2.1/23
```

**ip** 명령으로도 이러한 변경을 수행할 수 있습니다:

### 경로를 추가하려면

```bash
ip route add 192.168.2.1/23 via 10.11.12.3
```

### 경로를 삭제하려면

```bash
$ ip route delete 192.168.2.1/23 via 10.11.12.3
or
$ ip route delete 192.168.2.1/23
```

## Exercise

연습이 완벽을 만듭니다! 다음은 네트워크 라우팅 및 IP 주소 지정에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 IP 주소 관리](https://labex.io/ko/labs/linux-manage-ip-addressing-in-linux-592736)** - `ip` 명령을 사용하여 고정 IP 구성, 기본 게이트웨이 설정 및 네트워크 구성 확인을 연습합니다.
2. **[Linux 에서 ping 및 arp 를 사용한 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/linux-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - 기본 게이트웨이가 원격 트래픽을 처리하는 방법과 네트워크 계층 상호 작용을 관찰하는 방법을 배웁니다.

이 랩은 실제 시나리오에서 IP 주소 지정 및 라우팅 개념을 적용하고 Linux 네트워킹에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

경로를 삭제하는 명령 플래그는 무엇입니까?

## Quiz Answer

del
