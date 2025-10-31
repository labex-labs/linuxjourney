---
index: 4
lang: "ko"
title: "네트워크 관리자"
meta_title: "네트워크 관리자 - 네트워크 구성"
meta_description: "최신 Linux 네트워크 관리에서 NetworkManager 데몬의 역할을 알아보세요. 이 도구가 네트워크 구성을 자동화하는 방법과 nm-tool 및 강력한 nmcli 명령줄 유틸리티를 사용하여 상호 작용하는 방법을 학습합니다."
meta_keywords: "NetworkManager, nm-tool, nmcli, 리눅스 네트워크 관리자, networkmanager 리눅스, 리눅스 네트워크 관리, 네트워크 구성, 리눅스 네트워킹"
---

## Lesson Content

시스템의 네트워킹이 자동으로 구성되려면 일반적으로 서비스가 이미 설정되어 있어야 합니다. 대부분의 최신 Linux 배포판은 이 목적으로 NetworkManager 데몬을 사용하며, 이는 **리눅스 네트워크 관리**의 초석이 됩니다.

### 리눅스에서 네트워크 관리자란 무엇인가요?

그래픽 사용자 인터페이스 (GUI) 를 사용하는 경우, 데스크톱 작업 표시줄의 작은 응용 프로그램으로 **네트워크 관리자 리눅스** 서비스를 발견할 가능성이 높습니다. 이 도구는 네트워크 하드웨어와 연결 정보를 관리합니다. 예를 들어, 시작 시 NetworkManager 는 네트워크 하드웨어에 대한 정보를 수집하고, 사용 가능한 연결 (무선 또는 유선 네트워크 등) 을 검색한 다음, 온라인 상태가 되도록 활성화합니다.

### 명령줄 상호 작용

GUI 앱릿은 편리하지만, **네트워크 관리자 리눅스** 서비스와 상호 작용할 수 있는 강력한 명령줄 도구도 있습니다. 이는 서버 관리 및 스크립팅에 필수적입니다.

### nm-tool 사용하기

`nm-tool` 명령어는 NetworkManager 의 현재 상태와 관리되는 장치 목록을 보고합니다. `nm-tool`은 많은 최신 시스템에서 `nmcli`를 선호하여 사용되지 않는 것으로 간주된다는 점에 유의하십시오.

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

### 최신 nmcli 도구

`nmcli` 명령어는 **리눅스 네트워크 관리자**를 제어하고 수정하기 위한 주요 명령줄 유틸리티입니다. 이를 통해 터미널에서 직접 상태를 확인하고, 연결을 관리하며, 네트워크 장치를 구성할 수 있습니다. 기능 전체 목록은 해당 man 페이지 (`man nmcli`) 를 참조하십시오.

## Exercise

연습이 완벽을 만듭니다! NetworkManager 가 네트워크 구성의 많은 부분을 자동화하지만, 근본적인 명령과 개념을 이해하는 것은 문제 해결 및 고급 관리에 매우 중요합니다. 리눅스에서 네트워크 식별 및 관리에 대한 이해를 강화하기 위한 실습 랩은 다음과 같습니다.

1. **[리눅스에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 리눅스 시스템에서 MAC 및 IP 주소를 포함한 네트워크 주소 정보를 식별하는 연습을 합니다.
2. **[리눅스에서 IP 주소 관리](https://labex.io/ko/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip` 명령과 `dhclient`를 사용하여 고정 및 동적 IP 주소 구성, 기본 게이트웨이 설정 및 네트워크 구성 확인 방법을 배웁니다.
3. **[리눅스에서 ping 및 arp 를 사용한 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` 및 `arp`를 사용하여 네트워크 계층과 데이터 링크 계층이 상호 작용하는 방식을 이해하고, ARP 작동 방식과 기본 게이트웨이가 트래픽을 처리하는 방식을 관찰합니다.

이러한 랩은 네트워크 식별 및 구성 개념을 실제 시나리오에 적용하고 리눅스 네트워킹 기본 사항에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

수업에서 표시된 NetworkManager 의 상태 및 장치 요약을 보려면 어떤 명령을 사용해야 합니까? 답변은 영어 명령 이름만 소문자로 입력하십시오.

## Quiz Answer

nm-tool
