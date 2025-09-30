---
index: 4
lang: "ko"
title: "네트워크 관리자"
meta_title: "Network Manager - 네트워크 구성"
meta_description: "Linux 의 NetworkManager, 네트워크 구성 자동화 방법, nm-tool 및 nmcli 명령 사용법에 대해 알아보세요. 이 초보자 가이드로 시작하세요!"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux 네트워킹, 네트워크 구성, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

물론, 시스템의 네트워킹이 자동으로 작동하도록 하려면 이미 준비된 것이 있습니다. 대부분의 배포판은 NetworkManager 데몬을 활용하여 네트워크를 자동으로 구성합니다.

GUI 를 사용하는 경우 데스크톱 작업 표시줄 어딘가에 있는 애플릿 형태로 NetworkManager 를 볼 수 있습니다. 보시다시피, NetworkManager 는 네트워크의 하드웨어 및 연결 정보를 관리합니다. 예를 들어, 시작 시 NetworkManager 는 네트워크 하드웨어 정보를 수집하고 연결 (무선, 유선 등) 을 검색한 다음 활성화합니다.

NetworkManager 와 상호 작용하는 명령줄 도구도 있습니다:

### nm-tool

`nm-tool`은 NetworkManager 의 상태와 장치를 보고합니다.

```plaintext
pete@icebox:/$ nm-tool
NetworkManager Tool

State: connected (global)

- Device: eth0  [Wired connection 1] -------------------------------------------
  Type:              Wired
  Driver:            pcnet32
  State:             connected
  Default:           yes
  HW Address:        12:3D:45:56:7D:CC

  Capabilities:
    Carrier Detect:  yes

  Wired Properties
    Carrier:         on

  IPv4 Settings:
    Address:         192.168.22.1
    Prefix:          24 (255.255.255.0)
    Gateway:         192.168.22.2

    DNS:             192.168.22.2
```

### nmcli

`nmcli` 명령을 사용하면 NetworkManager 를 제어하고 수정할 수 있습니다. 자세한 내용은 man 페이지를 참조하십시오.

## Exercise

연습하면 완벽해집니다! NetworkManager 가 네트워크 구성의 많은 부분을 자동화하지만, NetworkManager 가 관리하는 기본 명령과 개념을 이해하는 것은 문제 해결 및 고급 관리에 중요합니다. 다음은 Linux 에서 네트워크 식별 및 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 Linux 시스템에서 MAC 및 IP 주소를 포함한 네트워크 주소 지정 정보를 식별하는 연습을 합니다.
2. **[Linux 에서 IP 주소 지정 관리](https://labex.io/ko/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip` 명령과 `dhclient`를 사용하여 고정 및 동적 IP 주소를 구성하고, 기본 게이트웨이를 설정하고, 네트워크 구성을 확인하는 방법을 배웁니다.
3. **[Linux 에서 ping 및 arp 를 사용한 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` 및 `arp`를 사용하여 네트워크 및 데이터 링크 계층이 어떻게 상호 작용하는지 이해하고, ARP 의 작동 방식과 기본 게이트웨이가 트래픽을 처리하는 방식을 관찰합니다.

이러한 랩은 실제 시나리오에서 네트워크 식별 및 구성 개념을 적용하고 Linux 네트워킹 기본 사항에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

NetworkManager 정보를 보는 명령은 무엇입요?

## Quiz Answer

nm-tool
