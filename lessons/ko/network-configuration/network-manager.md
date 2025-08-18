---
lang: "ko"
title: "네트워크 관리자"
meta_description: "Linux 에서 NetworkManager 에 대해 배우고, 네트워크 구성 자동화 방법, nm-tool 및 nmcli 명령 사용법을 익히세요. 이 초보자 가이드로 시작해보세요!"
meta_keywords: "NetworkManager, nm-tool, nmcli, Linux 네트워킹, 네트워크 구성, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

물론, 시스템의 네트워킹이 자동으로 작동하도록 하려면 이미 준비된 것이 있습니다. 대부분의 배포판은 NetworkManager 데몬을 사용하여 네트워크를 자동으로 구성합니다.

GUI 를 사용하는 경우 데스크톱 작업 표시줄 어딘가에 NetworkManager 가 애플릿 형태로 표시되는 것을 볼 수 있습니다. 보시다시피, NetworkManager 는 네트워크의 하드웨어 및 연결 정보를 관리합니다. 예를 들어, 시작 시 NetworkManager 는 네트워크 하드웨어 정보를 수집하고, 연결 (무선, 유선 등) 을 검색한 다음 활성화합니다.

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

이 수업에는 연습 문제가 없습니다.

## Quiz Question

NetworkManager 정보를 확인하는 명령은 무엇입니까?

## Quiz Answer

nm-tool
