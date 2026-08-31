---
lesson_id: "path-of-a-packet"
course_id: "routing"
lang: "ko"
order_index: 3
title: "패킷의 경로"
description: "경로, 이웃 탐색, 프레임 및 라우터가 IP 패킷을 경로 전체에 운반하는 방법을 알아봅니다."
meta_title: "패킷의 경로 - 라우팅"
meta_description: "로컬 네트워크와 인터넷을 이동하는 데이터의 전체 패킷 경로를 살펴봅니다. IP 주소, MAC 주소, ARP 및 라우팅 테이블의 협력 방식을 설명합니다."
meta_keywords: "패킷 경로, 네트워크 통신, ARP, IP 주소, MAC 주소, 라우팅 테이블, 기본 게이트웨이"
---

패킷 경로는 로컬 결정의 연속입니다. 출발지 호스트, 각 라우터 및 목적지는 자체 라우팅, 이웃, 필터링 및 프로토콜 상태를 적용합니다. 일반적으로 어떤 끝점도 모든 내부 결정을 미리 알지 못합니다.

## 링크상 목적지로 보내기

연결 경로가 포함하는 목적지에 대해 출발지는 인터페이스와 출발지 IP를 선택합니다. 그런 다음 목적지 링크 주소를 확인하고, Ethernet상의 IPv4에는 ARP를, IPv6에는 Neighbor Discovery를 사용해 IP 패킷을 담은 프레임을 보냅니다. 스위치는 IP 홉이 되지 않고 프레임을 전달할 수 있습니다.

:::single-choice{#packet-path-switch-hop}
일반적인 Ethernet 스위치는 IP 라우팅 홉으로 계산됩니까?

::option[아니요. IP 홉 필드를 줄이지 않고 로컬 프레임을 전달합니다.]{#packet-path-switch-not-hop .correct explanation="라우터가 IP 패킷을 처리하고 전달할 때 라우팅 홉이 발생합니다."}
::option[예. 모든 스위치가 IP 목적지를 바꿉니다.]{#packet-path-switch-replaces-ip explanation="2계층 전달은 일반적으로 IP 목적지를 다시 쓰지 않습니다."}
::option[예. 모든 케이블 커넥터도 IP 홉입니다.]{#packet-path-cable-hop explanation="물리 구성 요소는 IP 라우팅을 수행하지 않습니다."}
:::

## 게이트웨이를 통해 보내기

링크 밖의 목적지에는 선택된 경로가 다음 홉 라우터를 식별합니다. IP 목적지는 원격 끝점으로 유지되고 로컬 프레임 목적지는 게이트웨이의 링크 주소가 됩니다. 호스트는 로컬 링크에서 원격 서버가 아니라 게이트웨이의 주소를 확인합니다.

:::single-choice{#packet-path-gateway-mac}
링크 밖 서버로 향하는 첫 Ethernet 프레임에는 누구의 MAC 주소를 사용합니까?

::option[중간 네트워크 전체에서 원격 서버의 주소를 사용합니다.]{#packet-path-remote-mac explanation="원격 링크 주소는 출발지 LAN에서 의미가 없습니다."}
::option[서버 DNS 이름에서 계산한 값을 사용합니다.]{#packet-path-dns-mac explanation="DNS 이름은 로컬 다음 홉 MAC을 인코딩하지 않습니다."}
::option[선택된 로컬 게이트웨이의 주소를 사용합니다.]{#packet-path-local-gateway .correct explanation="프레임은 다음 홉으로 전달되고 IP 헤더는 최종 끝점을 대상으로 합니다."}
:::

## 각 라우터에서 처리하기

라우터는 수신 링크 프레이밍을 제거하고, IP 헤더를 검증하고 처리하고, TTL 또는 Hop Limit을 줄이고, 목적지를 조회하고, 정책을 적용하고, 출력 링크에 맞는 새 프레이밍을 만듭니다. IPv4에서는 변경된 TTL에 맞춰 헤더 체크섬도 처리합니다. 홉 필드가 0에 도달하면 라우터가 패킷을 버리고 ICMP 시간 초과 메시지를 반환할 수 있습니다.

:::single-choice{#packet-path-router-change}
모든 일반적인 라우팅 홉에서 바뀌는 IP 필드는 무엇입니까?

::option[애플리케이션 사용자 이름입니다.]{#packet-path-username explanation="기본 전달에 응용 계정 데이터가 필요하지 않습니다."}
::option[IPv4 TTL 또는 IPv6 Hop Limit입니다.]{#packet-path-hop-field .correct explanation="각 라우터가 필드를 줄여 라우팅 루프를 제한합니다."}
::option[모든 경우의 전송 목적지 포트입니다.]{#packet-path-port explanation="일반 라우팅은 전송 끝점을 보존하며 NAT는 별도의 변환입니다."}
:::

## 미들박스와 MTU 고려하기

일반 라우팅은 출발지 및 목적지 IP 주소를 보존하지만 NAT가 이를 다시 쓸 수 있고 터널이 원래 패킷을 감쌀 수 있습니다. 방화벽은 트래픽을 조용히 버리거나 거부할 수 있습니다. 링크 MTU도 다릅니다. IPv4 라우터는 일부 패킷을 단편화할 수 있지만 IPv6 라우터는 전달 패킷을 단편화하지 않고 Path MTU Discovery에 의존합니다.

:::single-choice{#packet-path-address-change-exception}
경로를 따라 종단 간 IP 주소가 바뀔 수 있는 때는 언제입니까?

::option[Ethernet 스위치가 출발지 MAC을 학습할 때마다 바뀝니다.]{#packet-path-switch-learning-ip explanation="스위치 학습은 IP 끝점 주소가 아니라 링크 전달 테이블에 영향을 줍니다."}
::option[NAT 정책이 패킷 헤더를 변환할 때 바뀔 수 있습니다.]{#packet-path-nat-change .correct explanation="변환은 일반 경로 전달을 넘어선 미들박스 기능입니다."}
::option[DNS 캐시 항목이 만료될 때마다 바뀝니다.]{#packet-path-dns-expiry explanation="이미 만들어진 패킷에는 숫자 주소가 들어 있습니다."}
:::

## 반환 경로 따라가기

목적지는 응답을 위해 자체 경로 조회를 수행합니다. 라우팅 정책, 부하 분산 또는 장애 때문에 반환 경로가 다른 라우터를 사용할 수 있습니다. 상태 저장 방화벽과 NAT는 관찰한 흐름을 고려해야 하므로 IP가 비대칭을 허용해도 운영상 중요할 수 있습니다.

:::single-choice{#packet-path-return-symmetry}
응답은 같은 라우터를 역순으로 통과해야 합니까?

::option[예. IP가 모든 패킷에 전체 송신 경로를 기록하기 때문입니다.]{#packet-path-records-route explanation="일반적인 IP 패킷에는 필수 전체 역경로가 들어 있지 않습니다."}
::option[예. 출발지와 목적지가 호스트 이름을 공유하지 않는 한 그렇습니다.]{#packet-path-hostname-symmetry explanation="이름은 경로 대칭성을 강제하지 않습니다."}
::option[아니요. 각 방향은 독립적으로 라우팅됩니다.]{#packet-path-independent-return .correct explanation="정책과 토폴로지가 비대칭이지만 유효한 경로를 만들 수 있습니다."}
:::

## 요약

이제 라우팅되는 IP 패킷 주변에서 바뀌는 링크 상태를 추적할 수 있습니다.

1. 최종 호스트가 링크상에 있을 때만 그 주소를 직접 확인합니다.
2. 링크 밖 트래픽은 선택된 로컬 게이트웨이로 프레임을 만듭니다.
3. 각 라우터의 경로 조회와 홉 제한 처리를 따릅니다.
4. NAT, 필터링, 터널 및 MTU 제약을 고려합니다.
5. 반환 방향을 독립적인 경로로 다룹니다.
