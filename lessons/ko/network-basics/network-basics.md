---
lesson_id: "network-basics"
course_id: "network-basics"
lang: "ko"
order_index: 1
title: "네트워크 기초"
description: "호스트, 링크, 스위치, 라우터 및 패킷이 로컬 및 광역 네트워크를 구성하는 방법을 알아봅니다."
meta_title: "네트워크 기초 - 네트워크 기초"
meta_description: "네트워크 기초부터 리눅스를 배워 보세요. 초보자를 위해 WAN, LAN, 라우터 및 호스트 같은 네트워크 구성 요소를 설명합니다."
meta_keywords: "네트워크 기초, 리눅스 기초, WAN, LAN, WLAN, 네트워크 튜토리얼, 네트워킹 가이드"
---

네트워크는 서로 다른 호스트의 애플리케이션이 데이터를 교환할 수 있도록 인터페이스를 연결합니다. 경로의 각 부분을 어느 장치, 주소 및 링크가 처리하는지 이해하면 이후의 리눅스 명령을 더 쉽게 해석할 수 있습니다.

## 호스트와 인터페이스

호스트는 노트북, 서버, 휴대전화 또는 가상 머신 같은 끝점이나 네트워크 시스템입니다. 하나의 호스트에 Ethernet, Wi-Fi, 루프백, 터널, 브리지 또는 가상 어댑터 등 여러 인터페이스가 있을 수 있습니다. 각 인터페이스는 기술에 맞는 링크 계층 및 네트워크 계층 설정을 가질 수 있습니다.

리눅스 호스트의 인터페이스와 주소를 조사합니다.

```bash
$ ip address show
```

인터페이스가 존재하거나 관리상 활성 상태라는 사실만으로 종단 간 연결이 입증되지는 않습니다.

:::single-choice{#network-basics-host-interface}
네트워크 인터페이스란 무엇입니까?

::option[인터넷의 모든 패킷을 영구적으로 복사한 것입니다.]{#network-basics-interface-copy explanation="인터페이스는 트래픽을 송수신하며 전역 패킷 아카이브가 아닙니다."}
::option[호스트가 네트워크나 가상 링크에 연결되는 지점입니다.]{#network-basics-interface-attachment .correct explanation="호스트에는 별도 설정을 가진 여러 물리 또는 가상 인터페이스가 있을 수 있습니다."}
::option[ISP 청구서의 사람이 읽기 쉬운 별칭입니다.]{#network-basics-interface-invoice explanation="청구 레이블은 호스트의 네트워크 연결과 관계없습니다."}
:::

## 로컬 네트워크

LAN(Local Area Network)은 가정, 사무실 또는 데이터 센터 세그먼트 같은 제한된 환경을 포괄합니다. Ethernet 스위치는 로컬 링크의 포트 사이에서 프레임을 전달합니다. WLAN(Wireless LAN)은 무선 링크 기술을 사용합니다. 브리지나 접근 지점이 둘을 연결하면 유선 및 무선 인터페이스가 같은 IP 서브넷에 속할 수도 있습니다.

:::single-choice{#network-basics-wlan-relationship}
WLAN은 LAN과 어떤 관계입니까?

::option[WLAN은 언제나 별도의 전역 인터넷입니다.]{#network-basics-wlan-global explanation="무선 링크 기술을 사용하는 로컬 네트워크입니다."}
::option[WLAN은 라우터가 사용하는 디스크 파티션입니다.]{#network-basics-wlan-disk explanation="이 용어는 저장소 배치가 아니라 네트워킹을 설명합니다."}
::option[WLAN은 무선 형태의 로컬 영역 네트워크입니다.]{#network-basics-wlan-local .correct explanation="무선 및 유선 링크를 하나의 로컬 브로드캐스트 도메인으로 브리지할 수도 있습니다."}
:::

## 라우터와 광역 네트워크

라우터는 라우팅 테이블에 따라 IP 네트워크 사이에서 네트워크 계층 패킷을 전달합니다. 가정용 장치는 흔히 라우팅, 스위칭, Wi-Fi 접근, 방화벽, NAT 및 DHCP를 함께 제공하지만 이들은 서로 다른 기능입니다.

WAN(Wide Area Network)은 더 넓은 지리적 또는 관리적 경계에 걸쳐 있습니다. 인터넷 서비스 제공자는 고객 네트워크를 다른 네트워크와 연결할 수 있지만 “WAN”이 단순히 한 집 밖의 모든 장치를 뜻하지는 않습니다.

:::single-choice{#network-basics-router-role}
라우터를 정의하는 역할은 무엇입니까?

::option[네트워크 계층 네트워크 사이에서 패킷을 전달합니다.]{#network-basics-forward-networks .correct explanation="라우팅은 IP 네트워크 경계를 가로지르는 다음 홉을 선택합니다."}
::option[모든 사용자의 파일을 필수 백업으로 저장합니다.]{#network-basics-router-backup explanation="파일 보존은 라우팅을 정의하는 기능이 아닙니다."}
::option[DNS를 조회하지 않고 모든 호스트 이름을 변환합니다.]{#network-basics-router-hostnames explanation="이름 확인과 패킷 전달은 별도의 기능입니다."}
:::

## 패킷, 프레임 및 흐름

애플리케이션은 프로토콜 계층이 전송을 위해 분할하고 캡슐화하는 데이터를 생성합니다. IP는 네트워크를 가로질러 패킷을 운반하고, 로컬 링크는 각 패킷을 해당 기술에 맞는 프레임 안에 운반합니다. 라우터는 일반적으로 IP 패킷을 계속 전달하면서 각 홉에서 링크 계층 프레이밍을 교체합니다.

하나의 통신에는 양방향으로 많은 패킷이 포함될 수 있습니다. 손실, 순서 변경, 단편화, 재전송 및 경로 변경이 발생할 수 있으므로 캡처한 패킷 하나만으로 전체 애플리케이션 트랜잭션을 설명할 수 있는 경우는 드뭅니다.

:::single-choice{#network-basics-router-frame}
라우터 홉에서 링크 계층 프레이밍에는 일반적으로 어떤 일이 일어납니까?

::option[라우터가 수신 프레이밍을 제거하고 다음 링크에 맞는 프레이밍을 만듭니다.]{#network-basics-reframe .correct explanation="전달되는 IP 패킷은 출력 인터페이스에 맞는 새 링크 계층 프레임에 실립니다."}
::option[같은 Ethernet 프레임이 인터넷 전체를 변경 없이 통과합니다.]{#network-basics-same-frame explanation="프레임은 해당 링크 범위에 속하며 라우팅 홉에서 교체됩니다."}
::option[애플리케이션이 IP 주소를 영구적으로 삭제합니다.]{#network-basics-delete-ip explanation="라우팅은 네트워크 계층 주소에 의존합니다."}
:::

## 요약

이제 기본 네트워크 경로의 주요 구성 요소를 설명할 수 있습니다.

1. 호스트와 물리 및 가상 인터페이스를 구분합니다.
2. 유선 및 무선 형태의 로컬 네트워크를 알아봅니다.
3. 복합 가정용 장치의 라우팅과 다른 기능을 구분합니다.
4. 링크 프레임과 라우팅되는 IP 패킷을 구분합니다.
