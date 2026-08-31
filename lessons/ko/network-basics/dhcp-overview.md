---
lesson_id: "dhcp-overview"
course_id: "network-basics"
lang: "ko"
order_index: 9
title: "DHCP 개요"
description: "DHCPv4가 탐색, 선택 및 갱신을 통해 주소와 네트워크 옵션을 임대하는 방법을 알아봅니다."
meta_title: "DHCP 개요 - 네트워크 기초"
meta_description: "DHCP의 기초를 알아봅니다. DHCP가 IP 주소를 할당하는 방법, 4단계 DORA 과정 및 네트워크에서의 역할을 설명합니다."
meta_keywords: "DHCP, 동적 호스트 설정 프로토콜, IP 주소, 리눅스 네트워킹, DHCP 과정, DORA, 네트워크 설정"
---

DHCP(Dynamic Host Configuration Protocol)는 클라이언트에 임대 방식의 네트워크 설정을 제공합니다. DHCPv4에서는 로컬 정책이 선택한 IPv4 주소, 서브넷 마스크, 기본 라우터, DNS 서버, 임대 시간 및 기타 옵션이 포함될 수 있습니다.

## 클라이언트, 서버 및 릴레이

DHCP 서버는 범위 또는 주소 풀과 임대 상태를 관리합니다. 서버가 모든 물리 세그먼트에 있을 필요는 없습니다. DHCP 릴레이가 서브넷과 중앙 서버 사이에서 클라이언트 교환을 전달할 수 있습니다. 정적 설정만 사용하는 네트워크는 DHCP를 전혀 제공하지 않을 수도 있습니다.

DHCP는 UDP 위에서 운반되는 응용 계층 프로토콜입니다. DHCPv4 서버는 일반적으로 UDP 포트 67, 클라이언트는 포트 68을 사용합니다.

:::single-choice{#dhcp-relay-purpose}
DHCP 릴레이는 무엇을 가능하게 합니까?

::option[모든 클라이언트가 정책 없이 주소를 선택합니다.]{#dhcp-client-any-address explanation="서버가 여전히 범위와 임대 정책을 적용합니다."}
::option[다른 서브넷의 클라이언트가 중앙 DHCP 서버에 도달합니다.]{#dhcp-central-server .correct explanation="릴레이는 라우팅 경계를 가로질러 DHCP 교환을 전달하고 클라이언트 네트워크를 식별합니다."}
::option[Ethernet 스위치가 모든 IP 라우터를 대체합니다.]{#dhcp-switch-router explanation="DHCP 릴레이는 라우팅되는 네트워크 경계를 제거하지 않습니다."}
:::

## 초기 DHCPv4 교환

일반적인 초기 과정은 DORA로 기억할 수 있습니다.

1. `DHCPDISCOVER`: 클라이언트가 사용 가능한 서버를 찾습니다.
2. `DHCPOFFER`: 서버가 주소와 옵션을 제안합니다.
3. `DHCPREQUEST`: 클라이언트가 제공된 임대를 선택해 요청합니다.
4. `DHCPACK`: 선택된 서버가 임대와 옵션을 확인합니다.

브로드캐스트와 유니캐스트 세부 사항은 클라이언트 상태, 릴레이 사용 및 서버 기능에 따라 달라집니다. 제안만으로는 아직 최종 사용 가능한 임대가 아니며 확인 응답이 일반적인 선택 교환을 완료합니다.

:::single-choice{#dhcp-dora-order}
일반적인 초기 DHCPv4 순서는 무엇입니까?

::option[OFFER, DISCOVER, ACK, REQUEST입니다.]{#dhcp-wrong-order-one explanation="클라이언트가 탐색한 뒤 서버가 제안하고, 요청한 뒤 확인 응답을 받습니다."}
::option[DISCOVER, OFFER, REQUEST, ACK입니다.]{#dhcp-correct-order .correct explanation="이 순서는 탐색하고, 제안하고, 선택하고, 확인합니다."}
::option[REQUEST, ACK, DISCOVER, OFFER입니다.]{#dhcp-wrong-order-two explanation="새 클라이언트는 일반적으로 임대를 선택하기 전에 탐색과 제안이 필요합니다."}
:::

## 임대 갱신

임대는 갱신하지 않으면 만료됩니다. 클라이언트는 일반적으로 만료 전에 갱신을 시작하며, 흔히 처음에는 원래 서버에 직접 연락합니다. 갱신이 성공하지 않으면 나중에 재바인딩 시도의 범위를 넓힙니다. 정확한 타이머는 프로토콜에 따라 제공되거나 계산됩니다.

주소가 동적으로 할당됐다고 표시된다는 사실이 임대의 영구 유지를 입증하지는 않습니다. 변경을 조사할 때 활성 임대, 수명, 서버 및 옵션을 기록하십시오.

:::single-choice{#dhcp-lease-expiration}
DHCP 주소 임대를 성공적으로 갱신하지 못하면 어떻게 됩니까?

::option[영구적인 하드웨어 MAC 주소가 됩니다.]{#dhcp-lease-mac explanation="IP 임대는 링크 계층 신원을 바꾸지 않습니다."}
::option[결국 만료되며 클라이언트는 더 이상 유효한 주소로 취급하면 안 됩니다.]{#dhcp-lease-expires .correct explanation="임대 방식으로 서버 정책에 따라 주소와 옵션을 회수하거나 변경할 수 있습니다."}
::option[클라이언트가 권위 있는 DNS 루트로 전환됩니다.]{#dhcp-lease-dns-root explanation="DHCP 임대는 DNS 권한을 부여하지 않습니다."}
:::

## 결과 조사하기

클라이언트가 DHCP를 설정한 뒤 주소만 보지 말고 필요한 모든 상태를 검증합니다.

```bash
$ ip address show
$ ip route show
$ resolvectl status
```

확인자 명령은 시스템마다 다릅니다. 활성 네트워크 관리자의 임대 데이터와 로그도 조사하십시오. 비인가 서버, 풀 안의 정적 할당, 오래된 상태 또는 수동 설정 때문에 중복 주소가 여전히 발생할 수 있습니다. DHCP는 실수를 줄이지만 모든 충돌을 자체적으로 방지하지는 못합니다.

:::single-choice{#dhcp-result-verification}
DHCP 임대를 수락한 뒤 무엇을 확인해야 합니까?

::option[인터페이스에 표시되는 이름만 확인합니다.]{#dhcp-interface-name-only explanation="인터페이스 이름으로 주소 지정, 라우팅 또는 이름 확인을 확립할 수 없습니다."}
::option[키보드가 반응하는지만 확인합니다.]{#dhcp-keyboard explanation="키보드 입력은 네트워크 임대 설정과 관계없습니다."}
::option[주소, 경로, DNS 및 임대 세부 정보를 확인합니다.]{#dhcp-check-complete-state .correct explanation="사용 가능한 설정은 여러 옵션과 시스템에 적용된 상태에 따라 달라집니다."}
:::

## DHCPv6와 IPv6 설정

IPv6 호스트는 SLAAC(Stateless Address Autoconfiguration), DHCPv6, 정적 설정 또는 그 조합을 사용할 수 있습니다. DHCPv6는 IPv4 DORA 교환을 사용하지 않으며 기본 라우터 정보는 일반적으로 DHCPv6가 아니라 IPv6 Router Advertisement에서 얻습니다.

:::single-choice{#dhcp-ipv6-default-router}
IPv6 호스트는 일반적으로 어디에서 기본 라우터 정보를 얻습니까?

::option[IPv6 Router Advertisement에서 얻습니다.]{#dhcp-router-advertisement .correct explanation="DHCPv6가 다른 설정을 제공할 수 있지만 라우터는 Neighbor Discovery를 통해 자신을 알립니다."}
::option[Ethernet FCS 트레일러에서 얻습니다.]{#dhcp-ipv6-fcs explanation="FCS는 링크 손상을 감지하며 라우터 설정을 담지 않습니다."}
::option[IPv4 DHCPACK에서만 얻습니다.]{#dhcp-ipv4-ack explanation="IPv4 DHCP 메시지는 IPv6 라우팅을 설정하지 않습니다."}
:::

## 요약

이제 DHCPv4가 호스트 네트워크 설정을 임대하고 갱신하는 방법을 설명할 수 있습니다.

1. DHCP 서버, 릴레이 및 클라이언트 서브넷을 구분합니다.
2. DISCOVER, OFFER, REQUEST 및 ACK 교환을 따릅니다.
3. 주소와 옵션을 시간 제한이 있는 임대 상태로 다룹니다.
4. 주소, 경로, DNS 및 임대 메타데이터를 함께 검증합니다.
5. DHCPv4 동작과 IPv6 자동 설정을 구분합니다.
