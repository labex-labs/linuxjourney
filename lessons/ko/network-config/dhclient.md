---
lesson_id: "dhclient"
course_id: "network-config"
lang: "ko"
order_index: 3
title: "dhclient"
description: "시스템 네트워크 관리자와 충돌하지 않도록 dhclient를 사용하는 시점과 방법을 알아봅니다."
meta_title: "dhclient - 네트워크 설정"
meta_description: "dhclient가 DHCP로 IP 주소를 얻고 네트워크 임대를 관리하는 방법을 알아봅니다. dhclient.conf와 dhclient.leases도 설명합니다."
meta_keywords: "dhclient, DHCP, 리눅스 네트워킹, IP 주소, 네트워크 설정"
---

`dhclient`는 일부 리눅스 시스템에 있는 ISC DHCP 클라이언트입니다. 현재 설치에서는 흔히 NetworkManager, systemd-networkd 또는 다른 서비스가 자체 DHCP 클라이언트를 실행합니다. 관리 중인 인터페이스에서 두 번째 클라이언트를 시작하면 주소, 경로, DNS 설정 및 임대 상태가 서로 경쟁할 수 있습니다.

## 활성 클라이언트 식별하기

`dhclient`를 호출하기 전에 설정 소유자와 프로세스를 조사합니다.

```bash
$ nmcli device status
$ networkctl status
$ ps -ef | grep '[d]hclient'
```

호스트에 존재하는 도구를 사용하십시오. 관리자가 인터페이스를 소유한다면 별도의 클라이언트를 시작하지 말고 그 관리자를 통해 DHCP를 요청합니다.

:::single-choice{#dhclient-second-client-risk} 이미 관리 중인 인터페이스에서 `dhclient`를 시작하면 안 되는 이유는 무엇입니까?

::option[DHCP는 루프백 주소만 할당할 수 있기 때문입니다.]{#dhclient-loopback-only explanation="DHCP는 일반적으로 루프백이 아닌 네트워크 설정을 할당합니다."}
::option[두 클라이언트가 주소, 경로, DNS 및 임대를 두고 경쟁할 수 있기 때문입니다.]{#dhclient-competing-state .correct explanation="일반적으로 식별된 설정 소유자만 인터페이스를 조정해야 합니다."}
::option[모든 DHCP 요청이 로컬 디스크를 포맷하기 때문입니다.]{#dhclient-reformats explanation="프로토콜은 디스크 형식이 아니라 네트워크 상태를 바꿉니다."}
:::

## 명시적으로 임대 요청하기

`dhclient`가 의도한 소유자인 관리되지 않는 테스트 인터페이스에서는 인터페이스를 지정하고 상세 출력을 사용합니다.

```bash
$ sudo dhclient -v enp1s0
```

인터페이스 없이 실행하면 여러 적격 인터페이스에 영향을 줄 수 있습니다. 설정 및 임대 경로는 패키지와 호출 방식에 따라 다릅니다. 흔한 이름으로 `dhclient.conf`와 `dhclient.leases`가 있지만 하나의 고정 위치를 가정하지 마십시오.

:::single-choice{#dhclient-interface-operand} 수동 요청에서 `enp1s0`을 지정하는 이유는 무엇입니까?

::option[의도한 네트워크 인터페이스만 대상으로 하기 위해서입니다.]{#dhclient-scope-interface .correct explanation="대상을 지정하지 않은 클라이언트 호출은 의도보다 많은 인터페이스를 고려할 수 있습니다."}
::option[DHCP에 TCP 포트 1을 선택하기 위해서입니다.]{#dhclient-tcp-port explanation="DHCP는 UDP를 사용하며 인터페이스 이름은 포트가 아닙니다."}
::option[임대를 영구적으로 만들기 위해서입니다.]{#dhclient-permanent explanation="DHCP 설정은 시간 제한이 있는 임대 상태입니다."}
:::

## 임대 해제하기

`dhclient -r INTERFACE`는 임대 해제를 요청하며 사용 가능한 설정을 제거할 수 있습니다. 이는 운영에 영향을 주며 서버가 해제 요청을 받는다고 보장하지 않습니다. 특히 원격 관리 경로에서는 임대를 조사하기 위해 해제하지 마십시오.

:::single-choice{#dhclient-release-effect} `dhclient -r enp1s0`의 운영상 위험은 무엇입니까?

::option[변경 없이 현재 임대만 출력합니다.]{#dhclient-release-readonly explanation="해제는 상태를 변경하는 작업입니다."}
::option[모든 임대를 무제한으로 갱신합니다.]{#dhclient-release-renews explanation="해제와 갱신은 반대 작업입니다."}
::option[현재 DHCP 연결을 제거할 수 있습니다.]{#dhclient-release-connectivity .correct explanation="임대 해제 과정은 임대 상태를 포기하며 원격 접근을 종료할 수 있습니다."}
:::

## 적용된 임대 검증하기

통제된 요청 후 주소 이상의 정보를 검증합니다.

```bash
$ ip address show dev enp1s0
$ ip route show
$ resolvectl status
```

관리자 또는 클라이언트 로그와 임대 수명을 조사한 뒤 의도한 이름 확인과 애플리케이션을 테스트합니다. DHCPACK에 잘못된 옵션이 들어 있을 수 있고 주소 할당 성공이 게이트웨이나 DNS 연결을 입증하지는 않습니다.

:::single-choice{#dhclient-verify-state} 임대를 얻은 뒤 무엇을 검증해야 합니까?

::option[주소, 경로, DNS, 임대 및 애플리케이션 동작입니다.]{#dhclient-complete-verify .correct explanation="임대는 함께 작동해야 하는 여러 관련 구성 요소를 설정합니다."}
::option[주소 문자열이 나타나는지만 확인합니다.]{#dhclient-address-only explanation="경로, DNS, 수명 및 종단 간 기능은 여전히 잘못될 수 있습니다."}
::option[바탕 화면 배경만 확인합니다.]{#dhclient-wallpaper explanation="바탕 화면 모양은 DHCP 상태와 관계없습니다."}
:::

## 요약

이제 `dhclient`가 인터페이스의 의도한 소유자일 때만 사용할 수 있습니다.

1. 활성 네트워크 관리자와 DHCP 클라이언트를 찾습니다.
2. 하나의 인터페이스에서 클라이언트가 경쟁하지 않게 합니다.
3. 수동 요청 범위를 이름이 지정된 테스트 인터페이스로 제한합니다.
4. 해제를 운영에 영향을 주는 작업으로 다루고 전체 임대 결과를 검증합니다.
