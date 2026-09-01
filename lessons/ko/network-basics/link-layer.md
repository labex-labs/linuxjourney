---
lesson_id: "link-layer"
course_id: "network-basics"
lang: "ko"
order_index: 8
title: "링크 계층"
description: "Ethernet 프레임, 이웃 탐색, 스위치 및 라우터가 로컬 링크에서 패킷을 전달하는 방법을 알아봅니다."
meta_title: "링크 계층 - 네트워크 기초"
meta_description: "TCP/IP 링크 계층의 기초를 살펴봅니다. 링크 계층 헤더, ARP의 IP-MAC 주소 확인 및 로컬 네트워크의 패킷 이동을 알아봅니다."
meta_keywords: "링크 계층, 링크 계층 헤더, ARP, TCP/IP, MAC 주소, 네트워크 기초, 리눅스 네트워킹"
---

링크 계층은 하나의 로컬 매체나 가상 링크를 가로질러 네트워크 계층 패킷을 운반합니다. Ethernet과 Wi-Fi는 프레이밍 세부 사항이 다르지만 모두 IP 아래에서 로컬 전송을 제공합니다.

## Ethernet 프레임

Ethernet 프레임에는 목적지 및 출발지 MAC 주소, EtherType 또는 길이 필드, 페이로드와 프레임 검사 시퀀스 트레일러가 들어 있습니다. 물리 전송에는 프리앰블과 시작 구분자도 사용됩니다. 프레임 검사 시퀀스는 링크의 손상을 감지하지만 손상된 프레임을 복구하거나 암호학적으로 보호하지는 않습니다.

:::single-choice{#link-layer-fcs-purpose} Ethernet 프레임 검사 시퀀스는 무엇에 사용됩니까?

::option[링크에서 프레임 손상을 감지합니다.]{#link-layer-detect-corruption .correct explanation="수신자는 무결성 검사를 통과하지 못한 프레임을 버릴 수 있습니다."}
::option[라우팅되는 모든 홉에서 페이로드를 암호화합니다.]{#link-layer-fcs-encryption explanation="FCS는 오류 감지 코드이며 암호화나 인증이 아닙니다."}
::option[TCP 포트로 애플리케이션을 선택합니다.]{#link-layer-fcs-port explanation="전송 포트는 IP 페이로드 안에 운반됩니다."}
:::

## 스위치와 로컬 전송

Ethernet 스위치는 어느 포트에서 어떤 출발지 MAC 주소가 나타나는지 학습하고 알려진 유니캐스트 프레임을 학습한 목적지 포트로 전달합니다. 브로드캐스트와 일부 알 수 없는 목적지 트래픽은 브로드캐스트 도메인 안에서 플러딩됩니다. VLAN은 하나의 스위칭 시스템을 별도의 논리 링크 도메인으로 나눌 수 있습니다.

:::single-choice{#link-layer-switch-learning} Ethernet 스위치는 일반적으로 프레임에서 어떤 정보를 학습합니까?

::option[애플리케이션 암호와 HTTP 쿠키입니다.]{#link-layer-switch-passwords explanation="기본 전달 테이블은 응용 자격 증명이 아니라 링크 주소를 사용합니다."}
::option[모든 라우터의 완전한 인터넷 라우팅 테이블입니다.]{#link-layer-switch-routing-table explanation="2계층 스위칭과 전역 경로 교환은 서로 다른 기능입니다."}
::option[스위치 포트와 연결된 출발지 MAC 주소입니다.]{#link-layer-switch-source .correct explanation="이 학습으로 이후의 알려진 유니캐스트 트래픽에 사용할 전달 테이블을 만듭니다."}
:::

## 다음 홉 주소 확인하기

Ethernet상의 IPv4에서 ARP(Address Resolution Protocol)는 링크상 IPv4 다음 홉 주소를 MAC 주소로 매핑합니다. 호스트는 먼저 이웃 캐시를 확인합니다. 필요하면 ARP 요청을 브로드캐스트하고 주소 소유자나 승인된 프록시가 응답합니다.

링크 밖의 IP 목적지에 대해서는 원격 목적지의 MAC 주소가 아니라 기본 또는 선택된 게이트웨이의 MAC 주소를 확인합니다. IPv6는 ARP 대신 ICMPv6 기반 Neighbor Discovery를 사용합니다.

:::single-choice{#link-layer-remote-destination-mac} 호스트는 링크 밖의 IPv4 목적지에 어떤 MAC 주소를 사용합니까?

::option[선택한 다음 홉 라우터의 MAC 주소입니다.]{#link-layer-gateway-mac .correct explanation="IP 패킷은 원격 호스트를 목적지로 유지하지만 로컬 프레임은 라우터로 향합니다."}
::option[모든 라우터를 가로질러 원격 서버의 MAC 주소를 사용합니다.]{#link-layer-remote-mac explanation="MAC 주소는 로컬 링크 식별자이며 종단 간 운반되지 않습니다."}
::option[TCP 목적지 포트에서 파생한 MAC 주소입니다.]{#link-layer-port-mac explanation="전송 포트는 링크 주소를 결정하지 않습니다."}
:::

## 이웃 상태 조사하기

IPv4 ARP 및 IPv6 Neighbor Discovery 항목을 확인합니다.

```bash
$ ip neighbor show
```

`REACHABLE`, `STALE`, `DELAY`, `PROBE` 및 `FAILED` 같은 상태는 이웃 연결 불가 감지 과정을 설명합니다. `STALE`이 고장을 뜻하지는 않습니다. 캐시된 연결 확인이 최근 상태가 아니며 사용할 때 테스트할 수 있다는 뜻입니다.

:::single-choice{#link-layer-stale-neighbor} `STALE` 이웃 항목은 무엇을 나타냅니까?

::option[방화벽이 이웃을 영구적으로 차단했습니다.]{#link-layer-stale-blocked explanation="이 상태는 방화벽 정책을 설명하지 않습니다."}
::option[MAC 주소가 백업으로 디스크에 기록됐습니다.]{#link-layer-stale-backup explanation="이웃 상태는 운영 캐시 정보입니다."}
::option[캐시된 매핑에 최근 연결 확인이 없습니다.]{#link-layer-stale-confirmation .correct explanation="스택은 여전히 매핑을 사용하고 필요하면 연결 감지를 수행할 수 있습니다."}
:::

## 라우터를 가로지르는 캡슐화

송신자는 IP 패킷을 다음 홉을 목적지로 하는 프레임 안에 넣습니다. 라우터는 수신 프레임을 검증하고 제거하고, IP 헤더를 처리하고, 출력 경로를 선택한 뒤 해당 링크에 맞는 새 프레임을 만듭니다. 수신자는 캡슐화를 역순으로 제거하고 전송 페이로드를 적절한 소켓에 전달합니다.

:::single-choice{#link-layer-router-reframing} 라우터에서 Ethernet 프레이밍이 바뀌는 일반적인 전달 중 무엇이 그대로 유지됩니까?

::option[NAT 같은 미들박스가 바꾸지 않는 한 IP 목적지가 유지됩니다.]{#link-layer-ip-destination .correct explanation="일반적인 라우터는 홉별 로컬 프레임을 교체하면서 최종 IP 목적지 방향으로 전달합니다."}
::option[수신 프레임 검사 시퀀스가 유지됩니다.]{#link-layer-same-fcs explanation="새 출력 프레임에는 자체 링크 무결성 값이 생깁니다."}
::option[모든 링크에서 목적지 MAC 주소가 유지됩니다.]{#link-layer-same-mac explanation="각 링크는 적절한 다음 홉 링크 주소를 사용합니다."}
:::

## 요약

이제 하나의 로컬 링크 전송 단계를 거치는 IP 패킷을 추적할 수 있습니다.

1. 주요 Ethernet 프레임 필드와 무결성 트레일러를 식별합니다.
2. 스위치가 로컬 전달 위치를 학습하는 방법을 설명합니다.
3. ARP로 IPv4 다음 홉을, NDP로 IPv6 이웃을 확인합니다.
4. 실패를 과장하지 않고 이웃 캐시 상태를 해석합니다.
5. 라우터가 각 출력 링크에 맞게 프레임을 다시 만드는 것을 이해합니다.
