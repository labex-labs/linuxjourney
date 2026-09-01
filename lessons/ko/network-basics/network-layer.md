---
lesson_id: "network-layer"
course_id: "network-basics"
lang: "ko"
order_index: 7
title: "네트워크 계층"
description: "IP 주소, 접두사, 라우팅 테이블 및 홉 제한이 네트워크 사이에서 패킷을 이동하는 방법을 알아봅니다."
meta_title: "네트워크 계층 - 네트워크 기초"
meta_description: "리눅스 네트워킹의 네트워크 계층을 살펴봅니다. IP 주소와 서브넷이 네트워크 간 데이터 전송을 위한 패킷 라우팅을 가능하게 하는 방법을 설명합니다."
meta_keywords: "네트워크 계층, IP 주소, 서브넷, 리눅스 네트워킹, 패킷 라우팅, 데이터 전송, IP 패킷"
---

네트워크 계층은 서로 연결된 네트워크를 가로질러 논리적 주소 지정과 최선형 패킷 전송을 제공합니다. 인터넷 프로토콜 모음에서는 IPv4와 IPv6가 패킷을 운반하고 라우터가 각 목적지 방향의 다음 홉을 선택합니다.

## IP 패킷

IP 헤더에는 출발지 및 목적지 주소와 전달 및 프로토콜 처리에 필요한 필드가 들어 있습니다. 페이로드에는 일반적으로 TCP 세그먼트, UDP 데이터그램 또는 ICMP 메시지가 들어 있습니다. IP는 도착, 순서 또는 중복 없음을 보장하지 않습니다.

:::single-choice{#network-layer-ip-service} IP 자체가 제공하는 전송 서비스는 무엇입니까?

::option[애플리케이션 트랜잭션의 반영을 보장합니다.]{#network-layer-guaranteed-commit explanation="IP 전송 결과로 애플리케이션의 영구 저장을 입증할 수 없습니다."}
::option[최선형 패킷 전송입니다.]{#network-layer-best-effort .correct explanation="필요한 복구나 순서 처리는 상위 계층 또는 애플리케이션이 추가합니다."}
::option[하나의 물리 케이블을 영구적으로 예약합니다.]{#network-layer-cable-reservation explanation="패킷 전달은 전용 물리 경로를 예약하지 않습니다."}
:::

## 접두사와 서브넷

주소와 접두사 길이는 앞쪽 몇 비트가 네트워크 접두사를 이루는지 정의합니다. 호스트는 이 정보와 경로를 사용해 목적지가 링크상에 있는지 다음 홉 라우터가 필요한지 결정합니다. 서브넷은 접두사와 정책 아래의 주소 범위이며 모든 다른 서브넷과 자동으로 연결되지는 않습니다.

:::single-choice{#network-layer-prefix-decision} 호스트가 IPv4 목적지가 링크상에 있는지 결정하는 데 도움이 되는 것은 무엇입니까?

::option[목적지 애플리케이션의 암호입니다.]{#network-layer-password explanation="인증 데이터는 네트워크 접두사를 정의하지 않습니다."}
::option[Ethernet 케이블의 색상입니다.]{#network-layer-cable-color explanation="케이블 외관에는 주소 지정 의미가 없습니다."}
::option[설정된 접두사와 라우팅 테이블입니다.]{#network-layer-prefix-routes .correct explanation="호스트는 연결된 접두사를 포함한 경로와 목적지를 비교합니다."}
:::

## 라우팅 결정

리눅스는 라우팅 정책과 테이블을 조회해 출력 인터페이스, 다음 홉 및 선호 출발지 정보를 선택합니다. 다른 조건이 같은 적격 경로 중에서는 일반적으로 가장 구체적으로 일치하는 접두사를 우선합니다. 목적지에 대한 실제 결정을 조사합니다.

```bash
$ ip route get 203.0.113.10
```

이는 로컬 경로 조회일 뿐이며 모든 하위 라우터에 작동하는 경로가 있거나 목적지가 트래픽을 받아들인다는 증거가 아닙니다.

:::single-choice{#network-layer-longest-prefix} 같은 목적지로 향하는 적격 경로 중 일반적으로 어느 경로가 선택됩니까?

::option[인터페이스 이름이 알파벳순으로 가장 앞선 경로입니다.]{#network-layer-alphabetical explanation="인터페이스 철자는 선택 규칙이 아닙니다."}
::option[접두사와 관계없이 가장 오래된 경로입니다.]{#network-layer-oldest explanation="경로의 나이만으로 접두사 일치를 무시하지 않습니다."}
::option[가장 구체적으로 일치하는 접두사의 경로입니다.]{#network-layer-most-specific .correct explanation="최장 접두사 일치는 일치하는 주소 범위가 가장 좁은 경로를 선택합니다."}
:::

## 홉 제한과 전달 변경

각 IPv4 패킷에는 TTL이 있고 각 IPv6 패킷에는 Hop Limit이 있습니다. 라우터는 이 값을 줄이며 0에 도달하면 패킷을 버리고 ICMP 오류를 보낼 수 있습니다. 이를 통해 전달 루프가 무한히 순환하지 못하게 합니다.

라우터는 일반적으로 종단 간 IP 주소를 보존하지만 NAT, 터널, 프록시 및 다른 미들박스가 패킷을 변환하거나 감쌀 수 있습니다. 링크 계층 헤더는 관계없이 라우팅되는 각 홉에서 바뀝니다.

:::single-choice{#network-layer-hop-limit} 라우터가 TTL 또는 Hop Limit을 줄이는 이유는 무엇입니까?

::option[애플리케이션의 파일 권한을 높이기 위해서입니다.]{#network-layer-hop-permissions explanation="홉 수는 파일시스템 권한 부여와 관계없습니다."}
::option[모든 패킷을 IPv4에서 IPv6로 변환하기 위해서입니다.]{#network-layer-hop-convert explanation="프로토콜 변환은 이 필드의 목적이 아닙니다."}
::option[패킷이 영원히 순환하지 못하게 하기 위해서입니다.]{#network-layer-prevent-loop .correct explanation="유한한 홉 수는 지속적인 라우팅 루프에서 결국 패킷을 버리게 합니다."}
:::

## 요약

이제 IP 호스트가 목적지 방향의 다음 단계를 선택하는 방법을 설명할 수 있습니다.

1. IP 전송을 최선형 서비스로 다룹니다.
2. 접두사와 경로로 링크상 목적지와 라우팅되는 목적지를 구분합니다.
3. 경로 선택에 최장 접두사 일치를 적용합니다.
4. 홉 제한이 전달 루프를 제한하는 방식을 이해합니다.
