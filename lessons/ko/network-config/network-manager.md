---
lesson_id: "network-manager"
course_id: "network-config"
lang: "ko"
order_index: 4
title: "NetworkManager"
description: "NetworkManager가 장치, 영구 연결 프로필 및 활성 런타임 상태를 구분하는 방법을 알아봅니다."
meta_title: "NetworkManager - 네트워크 설정"
meta_description: "현대 리눅스 네트워크 관리에서 NetworkManager 데몬의 역할을 알아봅니다. nmcli로 네트워크 설정을 자동화하고 관리하는 방법을 설명합니다."
meta_keywords: "NetworkManager, nmcli, 리눅스 네트워크 관리자, 리눅스 네트워크 관리, 네트워크 설정"
---

NetworkManager는 많은 리눅스 데스크톱과 서버에서 네트워크 장치를 관리하고 연결 프로필을 활성화합니다. 보편적으로 사용되는 것은 아니므로 `nmcli`로 설정을 변경하기 전에 대상 인터페이스를 소유하는지 확인하십시오.

## 장치와 연결

장치는 `enp1s0` 또는 `wlan0` 같은 커널 인터페이스입니다. 연결은 IPv4, IPv6, DNS, Wi-Fi, 라우팅 및 기타 설정을 담은 저장 프로필입니다. 하나의 장치에 여러 프로필이 있을 수 있지만 일반적으로 한 번에 적용 가능한 프로필 하나만 활성 상태입니다.

```bash
$ nmcli device status
$ nmcli connection show
$ nmcli connection show --active
```

:::single-choice{#networkmanager-device-profile}
NetworkManager 연결 프로필이란 무엇입니까?

::option[네트워크 카드에 납땜된 물리 커넥터입니다.]{#networkmanager-physical-connector explanation="NetworkManager 프로필이 아니라 하드웨어입니다."}
::option[장치에서 활성화할 수 있는 저장된 설정 집합입니다.]{#networkmanager-stored-settings .correct explanation="프로필은 커널 인터페이스 객체와 별도로 설정을 영구 보존합니다."}
::option[모든 활성 흐름에서 캡처한 패킷입니다.]{#networkmanager-packet-capture explanation="프로필은 설정을 설명하며 모든 트래픽을 담지 않습니다."}
:::

## 실제 상태 조사하기

활성 프로필과 장치 세부 정보를 표시합니다.

```bash
$ nmcli -f GENERAL,IP4,IP6 device show enp1s0
$ nmcli connection show 'Wired connection 1'
```

프로필 설정, 런타임 DHCP 결과 및 커널 상태가 서로 다를 수 있습니다. `ip address`, `ip route` 및 확인자와 비교하십시오. 더 이상 권장되지 않는 `nm-tool`을 현재 작업 흐름의 기반으로 삼으면 안 됩니다.

:::single-choice{#networkmanager-active-command}
활성 NetworkManager 프로필을 나열하는 명령은 무엇입니까?

::option[`nmcli device delete --all`]{#networkmanager-delete-all explanation="검사 명령이 아니며 파괴적인 의도를 나타냅니다."}
::option[`nmcli connection show --active`]{#networkmanager-show-active .correct explanation="저장된 연결을 현재 활성화된 연결로 필터링합니다."}
::option[`ip route flush table all`]{#networkmanager-flush-routes explanation="프로필을 나열하는 대신 라우팅 상태를 제거합니다."}
:::

## 프로필 수정 및 활성화하기

이름이 지정된 프로필을 명시적으로 수정한 뒤 유지 관리 시간에 활성화합니다.

```bash
$ sudo nmcli connection modify 'Wired connection 1' ipv4.method auto
$ sudo nmcli connection up 'Wired connection 1'
```

수정은 영구 프로필 데이터를 바꾸고 활성화는 실시간 주소, 경로 및 DNS를 교체할 수 있습니다. 원격 변경에는 콘솔 접근, 저장된 원래 설정 및 독립적인 시간 제한 되돌리기가 필요합니다. 변경하는 연결 자체에 복구 명령 전달을 의존하지 마십시오.

:::single-choice{#networkmanager-modify-versus-up}
`connection modify`와 `connection up`의 차이는 무엇입니까?

::option[modify는 호스트를 재부팅하고 up은 DNS 소스 코드를 편집합니다.]{#networkmanager-reboot-source explanation="어느 설명도 명령과 맞지 않습니다."}
::option[modify는 프로필 설정을 바꾸고 up은 프로필을 활성화합니다.]{#networkmanager-change-activate .correct explanation="영구 설정과 런타임 활성화는 관련 있지만 별도의 작업입니다."}
::option[둘 다 연결에 영향을 줄 수 없는 읽기 전용 별칭입니다.]{#networkmanager-readonly explanation="이 작업 흐름에서 둘 다 상태를 바꿀 수 있습니다."}
:::

## 검증 및 비밀 정보 보호

활성화 후 프로필 상태, 커널 주소와 경로, DNS, 양쪽 주소 계열 및 의도한 애플리케이션을 검증합니다. Wi-Fi, VPN, 802.1X 및 모바일 프로필에는 비밀 정보가 들어 있을 수 있습니다. 프로필 권한을 제한하고 공유 로그나 셸 기록에 비밀 필드를 출력하지 마십시오.

:::single-choice{#networkmanager-verification}
NetworkManager가 “연결됨”을 보고하는 것보다 강한 증거는 무엇입니까?

::option[프로필 이름에 Wired라는 단어가 들어 있습니다.]{#networkmanager-name-proof explanation="레이블은 경로나 서비스 상태를 입증하지 않습니다."}
::option[터미널 창이 계속 열려 있습니다.]{#networkmanager-terminal-open explanation="부분적인 네트워크 장애에서도 터미널이 살아 있을 수 있습니다."}
::option[의도한 DNS 및 애플리케이션 테스트가 성공합니다.]{#networkmanager-end-to-end .correct explanation="관리자 상태를 커널 및 서비스 동작과 연관 지어야 합니다."}
:::

## 요약

이제 NetworkManager 프로필을 인터페이스 객체와 혼동하지 않고 관리할 수 있습니다.

1. NetworkManager가 대상 장치를 소유하는지 확인합니다.
2. 저장 프로필과 활성 런타임 상태를 구분합니다.
3. 장치, 모든 프로필 및 활성 프로필을 별도로 조사합니다.
4. 수정, 활성화, 복구 및 검증을 서로 다른 단계로 수행합니다.
