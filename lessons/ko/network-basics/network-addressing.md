---
lesson_id: "network-addressing"
course_id: "network-basics"
lang: "ko"
order_index: 4
title: "네트워크 주소 지정"
description: "링크 주소, IP 주소 및 호스트 이름이 네트워크 통신의 서로 다른 부분을 식별하는 방법을 알아봅니다."
meta_title: "네트워크 주소 지정 - 네트워크 기초"
meta_description: "네트워크 주소 지정의 기초를 알아봅니다. 리눅스 네트워킹에서 장치 통신을 이해하는 핵심 개념인 MAC 주소, IP 주소 및 호스트 이름을 설명합니다."
meta_keywords: "네트워크 주소 지정, MAC 주소, IP 주소, 호스트 이름, 네트워크 식별자, 리눅스 네트워킹"
---

네트워크 통신은 범위에 따라 서로 다른 식별자를 사용합니다. 링크 계층 주소는 로컬 링크에서 프레임을 전달하고, IP 주소는 라우팅되는 전송을 지원하며, 이름은 애플리케이션과 사람이 서비스를 선택하는 데 도움이 됩니다.

## 링크 계층 주소

Ethernet MAC 주소는 48비트이며 일반적으로 `00:c4:b5:45:b2:43`처럼 16진수 옥텟 여섯 개로 표기합니다. 출발지 주소는 현재 링크의 인터페이스를 식별하고 목적지는 유니캐스트, 멀티캐스트 또는 브로드캐스트일 수 있습니다.

MAC 주소는 영구적이거나 전역적으로 고유하다고 보장되지 않습니다. 소프트웨어가 로컬 관리 주소를 할당할 수 있고, 가상 인터페이스가 주소를 생성하며, Wi-Fi 개인 정보 보호 기능이 주소를 무작위화할 수 있습니다. 라우터는 일반적으로 각 홉에서 Ethernet 프레이밍을 교체하므로 원격 서버는 원래 로컬 Ethernet 출발지 주소를 받지 않습니다.

:::single-choice{#network-addressing-mac-scope}
패킷 전송에서 Ethernet MAC 주소의 일반적인 범위는 무엇입니까?

::option[현재 로컬 링크입니다.]{#network-addressing-local-link .correct explanation="라우터는 이후 홉에 맞는 새 링크 계층 프레이밍을 만듭니다."}
::option[최종 인터넷 서버까지 라우팅되는 모든 홉입니다.]{#network-addressing-all-hops explanation="원래 프레임은 라우터를 변경 없이 통과하지 않습니다."}
::option[애플리케이션의 텍스트 인코딩만 해당합니다.]{#network-addressing-text-encoding explanation="MAC 주소는 링크 계층 프레이밍에 속합니다."}
:::

## IP 주소와 접두사

IPv4 주소는 32비트, 즉 옥텟 네 개이며 IPv6 주소는 128비트입니다. IP 주소는 일반적으로 인터페이스에 할당되고 `192.0.2.10/24` 또는 `2001:db8::10/64` 같은 접두사 길이와 함께 해석됩니다. 접두사는 앞쪽 몇 비트가 네트워크를 나타내는지 식별합니다.

하나의 인터페이스에 여러 IP 주소가 있을 수 있고 주소는 DHCP, 개인 정보 보호 주소 지정, 장애 조치 또는 관리 작업으로 바뀔 수 있습니다. 사설 IPv4 주소는 서로 다른 네트워크에서 재사용할 수 있으며 외부 연결 가능성은 공용 라우팅 및 NAT 정책에 따라 달라집니다.

:::single-choice{#network-addressing-ipv4-size}
IPv4 주소의 크기는 얼마입니까?

::option[옥텟 네 개의 32비트입니다.]{#network-addressing-thirty-two .correct explanation="표시되는 각 10진수 구성 요소는 8비트를 나타냅니다."}
::option[16진수 한 자리의 4비트입니다.]{#network-addressing-four-bits explanation="4비트는 16진수 한 자리만 나타냅니다."}
::option[옥텟 열여섯 개의 128비트입니다.]{#network-addressing-128-octets explanation="IPv6는 128비트이지 128옥텟이 아닙니다."}
:::

## 호스트 이름과 이름 확인

호스트 이름은 주소가 아니라 이름입니다. 호스트의 이름 서비스 설정에 따라 `/etc/hosts`, DNS, 멀티캐스트 시스템 또는 다른 소스에서 이름을 확인할 수 있습니다. 하나의 이름이 여러 주소로 확인될 수 있고 여러 이름이 하나의 서비스를 가리킬 수도 있습니다.

애플리케이션이 볼 가능성이 높은 결과를 테스트하려면 시스템 확인 경로를 사용합니다.

```bash
$ getent ahosts example.com
```

DNS 응답은 바뀌거나 캐시될 수 있으며 이름 확인 성공이 서비스에 연결할 수 있음을 입증하지는 않습니다.

:::single-choice{#network-addressing-getent-purpose}
이름 확인 검사에서 `getent ahosts`를 사용하는 이유는 무엇입니까?

::option[반환된 주소를 모든 인터페이스에 영구적으로 할당합니다.]{#network-addressing-getent-assign explanation="이 명령은 데이터베이스를 조회하며 인터페이스를 설정하지 않습니다."}
::option[시스템에 설정된 이름 서비스 경로에 주소를 요청합니다.]{#network-addressing-system-resolver .correct explanation="호스트 정책에 따라 로컬 파일과 DNS 등이 포함될 수 있습니다."}
::option[반환된 모든 호스트의 애플리케이션 상태를 보장합니다.]{#network-addressing-getent-health explanation="이름 조회와 애플리케이션 상태는 서로 다른 테스트입니다."}
:::

## 리눅스 호스트 조사하기

링크와 IP 설정을 별도로 확인합니다.

```bash
$ ip -brief link
$ ip -brief address
```

연결 문제를 진단할 때는 이어서 경로와 이웃 상태를 조사합니다. 이름만 보고 올바른 출발지 인터페이스나 주소를 추론하지 마십시오. 라우팅 선택, 정책 규칙, 네임스페이스 및 터널이 경로를 바꿀 수 있습니다.

:::single-choice{#network-addressing-ip-link-versus-address}
할당된 IP 주소에 초점을 맞춘 명령 보기는 무엇입니까?

::option[`ip -brief address`]{#network-addressing-address-view .correct explanation="address 객체는 인터페이스의 IPv4 및 IPv6 할당을 표시합니다."}
::option[`ip -brief link`만 사용합니다.]{#network-addressing-link-only explanation="link 보기는 인터페이스와 링크 계층 상태에 초점을 맞춥니다."}
::option[`pwd`]{#network-addressing-pwd explanation="pwd는 셸의 현재 작업 디렉터리를 출력합니다."}
:::

## 요약

이제 이름과 주소를 네트워킹 범위에 따라 구분할 수 있습니다.

1. MAC 주소를 변경될 수 있는 로컬 링크 식별자로 다룹니다.
2. IPv4와 IPv6 주소를 접두사 길이와 함께 읽습니다.
3. 인터페이스가 여러 논리 주소를 가질 수 있음을 이해합니다.
4. 설정된 시스템 확인자를 통해 호스트 이름을 조회합니다.
