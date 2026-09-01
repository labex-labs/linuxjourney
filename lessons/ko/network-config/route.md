---
lesson_id: "route"
course_id: "network-config"
lang: "ko"
order_index: 2
title: "route"
description: "ip 명령으로 리눅스 경로를 조사하고 추가, 교체, 삭제하며 안전하게 검증하는 방법을 알아봅니다."
meta_title: "route - 네트워크 설정"
meta_description: "리눅스 라우팅 테이블을 관리하는 방법을 알아봅니다. 현대적인 ip route 명령으로 네트워크 경로를 추가하고 삭제하는 방법을 설명합니다."
meta_keywords: "리눅스 ip route 명령, 경로 추가, 경로 삭제, 라우팅 테이블, 네트워크 라우팅, 리눅스 네트워킹"
---

수동 경로는 커널이 출력 인터페이스와 다음 홉을 선택하는 방식을 바꿉니다. 실수하면 호스트 연결이 끊기거나 민감한 트래픽이 다른 곳으로 향할 수 있으므로 상태를 변경하기 전에 실제 경로, 설정 소유자 및 복구 경로를 조사하십시오.

## 현재 결정 조사하기

관련 경로를 기록하고 커널이 현재 목적지에 어떻게 도달하는지 조회합니다.

```bash
$ ip -4 route show
$ ip route get 192.168.2.25
```

정책 규칙과 대체 테이블이 있다면 함께 조사합니다. 경로 조회는 로컬 증거이며 트래픽을 보내지 않습니다.

:::single-choice{#route-get-before-change} 경로 변경 전에 `ip route get DESTINATION`을 실행하는 이유는 무엇입니까?

::option[비교와 되돌리기를 위해 현재 로컬 결정을 기록합니다.]{#route-get-baseline .correct explanation="선택된 인터페이스, 다음 홉 및 출발지는 의도한 변경을 정의하는 데 도움이 됩니다."}
::option[모든 라우터에서 목적지를 영구적으로 예약합니다.]{#route-get-reserves explanation="이 명령은 로컬 조회를 수행하며 원격 상태를 바꾸지 않습니다."}
::option[모든 정책 라우팅 규칙을 비활성화합니다.]{#route-get-disables-policy explanation="조회는 정책을 제거하지 않고 평가합니다."}
:::

## 경로 추가 또는 교체하기

연결 가능한 다음 홉을 통해 정규 접두사에 경로를 추가합니다.

```bash
$ sudo ip route add 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

게이트웨이는 관련 링크 또는 명시적으로 유효한 링크상 설계에 따라 연결 가능해야 합니다. `add`는 동등한 경로가 이미 있으면 실패합니다. `replace`는 경로를 만들거나 변경하므로 멱등 설정에 유용하지만 작동 중인 상태를 덮어쓸 수 있습니다. 정확한 대상을 먼저 확인하십시오.

:::single-choice{#route-add-existing} `ip route add`가 이미 존재하는 경로를 대상으로 하면 일반적으로 어떻게 됩니까?

::option[기존 목적지 접두사를 조용히 삭제합니다.]{#route-add-deletes explanation="add는 교체하지 않고 일반적으로 기존 객체 오류를 보고합니다."}
::option[기존 경로를 교체하지 않고 실패합니다.]{#route-add-fails .correct explanation="변경할 항목을 검토한 뒤에만 의도적으로 replace를 사용하십시오."}
::option[선택된 게이트웨이를 재부팅합니다.]{#route-add-reboots explanation="로컬 경로 설정으로 이런 방식의 원격 재부팅을 요청할 수 없습니다."}
:::

## 정확하게 삭제하기

후보나 테이블이 여러 개일 수 있다면 정확한 경로 속성을 지정해 삭제합니다.

```bash
$ sudo ip route del 192.168.2.0/23 via 10.11.12.3 dev enp1s0
```

목적지만 지정한 삭제는 의도보다 넓게 일치하거나 모호할 수 있습니다. 경로를 제거하기 전에 복원에 필요한 원래 명령을 기록하십시오.

:::single-choice{#route-delete-precision} 경로 삭제 시 다음 홉과 장치를 함께 지정하는 이유는 무엇입니까?

::option[의도한 항목을 더 정확하게 식별하기 위해서입니다.]{#route-delete-exact .correct explanation="명시적인 속성은 같은 접두사의 다른 경로를 제거할 가능성을 줄입니다."}
::option[물리 네트워크 어댑터도 함께 삭제하기 위해서입니다.]{#route-delete-adapter explanation="경로 삭제는 커널 링크 객체를 제거하지 않습니다."}
::option[목적지의 DNS 영역을 지우기 위해서입니다.]{#route-delete-dns explanation="라우팅과 권위 있는 DNS 데이터는 별도의 시스템입니다."}
:::

## 영구 적용과 원격 안전

`ip route` 명령은 현재 커널 상태만 바꿉니다. NetworkManager, systemd-networkd, netplan, ifupdown, DHCP, 라우팅 데몬 또는 오케스트레이션이 나중에 이를 교체할 수 있습니다. 런타임 동작을 테스트한 뒤에만 활성 소유자에 경로를 저장합니다.

원격 호스트에서는 독립적인 콘솔을 보존하고 변경하는 경로에 의존하지 않는 되돌리기를 사용합니다. 그런 다음 경로 조회, 이웃 상태, 양방향 트래픽 및 실제 서비스를 검증합니다.

:::single-choice{#route-runtime-persistence} 네트워크 관리자 다시 불러오기 후 수동으로 추가한 경로에는 어떤 일이 생길 수 있습니까?

::option[영원히 변경할 수 없는 커널 기능이 됩니다.]{#route-manual-immutable explanation="런타임 경로는 제거되거나 교체될 수 있습니다."}
::option[서브넷의 모든 호스트에 자동으로 나타납니다.]{#route-manual-all-hosts explanation="명령은 현재 네트워크 네임스페이스만 바꿉니다."}
::option[영구 정책에 없으면 사라질 수 있습니다.]{#route-manual-disappears .correct explanation="관리자가 설정된 프로필에 따라 커널 상태를 조정합니다."}
:::

## 요약

이제 복구 가능한 작업 흐름으로 범위가 제한된 리눅스 경로 변경을 수행할 수 있습니다.

1. 현재 경로, 규칙 및 실제 조회를 기록합니다.
2. 정규 접두사와 연결 가능한 다음 홉을 사용합니다.
3. 추가와 의도적인 교체를 구분합니다.
4. 정확한 경로를 삭제하고 복원 명령을 보존합니다.
5. 활성 관리자를 통해 영구 적용하고 양방향을 검증합니다.
