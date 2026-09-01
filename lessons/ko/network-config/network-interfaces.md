---
lesson_id: "network-interfaces"
course_id: "network-config"
lang: "ko"
order_index: 1
title: "네트워크 인터페이스"
description: "리눅스 인터페이스 상태, 주소, 통계 및 영구 설정 소유권을 조사하는 방법을 알아봅니다."
meta_title: "네트워크 인터페이스 - 네트워크 설정"
meta_description: "리눅스 네트워크 인터페이스 가이드입니다. 현대적인 ip 명령과 ifconfig, /etc/network/interfaces 같은 설정 파일을 알아봅니다."
meta_keywords: "리눅스 인터페이스, 리눅스 네트워크 인터페이스, etc network interfaces, ifconfig, ip 명령, 네트워크 설정"
---

리눅스 네트워크 인터페이스는 네트워크 네임스페이스를 물리 장치, 루프백 경로, 브리지, 터널, 가상 장치 또는 다른 링크와 연결합니다. 인터페이스 상태, 주소, 경로, DNS 및 영구 설정은 관련 있지만 서로 구분됩니다.

## 인터페이스 찾기

현대적인 iproute2 도구를 사용합니다.

```bash
$ ip -brief link show
$ ip -brief address show
```

인터페이스 이름은 `enp1s0` 같은 예측 가능한 하드웨어 기반 이름, `eth0` 같은 전통적 이름 또는 관리자가 정의한 이름일 수 있습니다. `eth0`가 존재하거나 특정 어댑터를 식별한다고 가정하지 마십시오.

:::single-choice{#interfaces-name-assumption} 스크립트가 `eth0`을 가정하지 말고 찾아야 하는 이유는 무엇입니까?

::option[모든 인터페이스의 이름이 lo여야 하기 때문입니다.]{#interfaces-all-loopback explanation="루프백은 하나의 특수 인터페이스이며 모든 링크의 이름이 아닙니다."}
::option[리눅스 시스템이 여러 인터페이스 명명 방식을 사용할 수 있기 때문입니다.]{#interfaces-naming-varies .correct explanation="하드웨어 기반, 가상 및 사용자 지정 이름 때문에 고정된 eth0 가정은 신뢰할 수 없습니다."}
::option[인터페이스 이름이 항상 원격 암호이기 때문입니다.]{#interfaces-name-password explanation="이름은 커널 장치를 식별하며 자격 증명이 아닙니다."}
:::

## 관리 상태와 운영 상태

`UP`은 인터페이스가 관리상 활성화됐음을 뜻합니다. `LOWER_UP`은 일반적으로 Ethernet 캐리어처럼 하위 계층이 운영 준비 상태를 보고한다는 뜻입니다. 어느 플래그만으로도 IP 주소, 경로, DNS, 방화벽 또는 애플리케이션 경로가 작동함을 입증할 수 없습니다.

```bash
$ ip -details link show dev enp1s0
$ ip -s link show dev enp1s0
```

통계 보기에서 오류, 드롭 및 카운터를 확인할 수 있지만 카운터는 시간 간격과 기준선이 있어야 의미가 있습니다.

:::single-choice{#interfaces-up-limit} 관리 상태 `UP`이 입증하지 못하는 것은 무엇입니까?

::option[종단 간 연결이 작동한다는 사실입니다.]{#interfaces-up-not-connectivity .correct explanation="하위 계층, 주소 지정, 라우팅, 필터링, 이름 지정 및 서비스 장애가 남아 있을 수 있습니다."}
::option[관리자가 인터페이스를 활성화했다는 사실입니다.]{#interfaces-up-does-prove explanation="상태가 직접 뜻하는 바입니다."}
::option[인터페이스에 커널 객체가 있다는 사실입니다.]{#interfaces-up-kernel-object explanation="표시된 상태는 존재하는 커널 인터페이스에 속합니다."}
:::

## 런타임 상태 변경하기

런타임 명령에는 다음이 있습니다.

```bash
$ sudo ip link set dev enp1s0 up
$ sudo ip address add 192.0.2.10/24 dev enp1s0
```

이 변경은 현재 커널 상태에 영향을 주며 나중에 프로필을 다시 적용하는 네트워크 관리자와 충돌할 수 있습니다. 원격 관리 인터페이스를 내리면 즉시 접근이 끝날 수 있습니다. 변경 전에 정확한 장치를 검증하고, 콘솔 접근을 보존하고, 현재 상태를 기록하고, 시간 제한 또는 테스트된 되돌리기를 준비하십시오.

:::single-choice{#interfaces-ip-address-add-persistence} `ip address add`만으로 재부팅 후 영구 적용이 보장됩니까?

::option[아니요. 활성 설정 시스템에도 설정을 저장해야 합니다.]{#interfaces-manager-persistence .correct explanation="NetworkManager, systemd-networkd, ifupdown 또는 다른 소유자가 영구 정책을 적용합니다."}
::option[예. 모든 커널 변경이 모든 관리자 프로필을 편집하기 때문입니다.]{#interfaces-runtime-always-persistent explanation="커널 런타임 변경은 보편적으로 영구 설정을 갱신하지 않습니다."}
::option[사설 IPv4 주소일 때만 보장됩니다.]{#interfaces-private-persistent explanation="주소 범위가 런타임 명령을 영구적으로 만들지는 않습니다."}
:::

## 설정 소유권 식별하기

영구 설정 경로는 배포판과 설치에 따라 다릅니다. NetworkManager 프로필, systemd-networkd 유닛, netplan 입력, `/etc/network/interfaces`, cloud-init 또는 오케스트레이션을 사용할 수 있습니다. 파일을 편집하기 전에 어느 서비스가 장치를 관리하는지 확인합니다.

```bash
$ systemctl --type=service --state=running | grep -E 'NetworkManager|networkd|networking'
$ networkctl status
$ nmcli device status
```

식별한 관리자에 존재하는 명령만 사용하십시오. 두 관리자가 같은 링크를 제어하면 서로 경쟁하며 상태를 덮어쓸 수 있습니다.

:::single-choice{#interfaces-config-owner} 영구 인터페이스 변경 전에 무엇을 해야 합니까?

::option[가능한 모든 네트워크 설정 파일을 편집합니다.]{#interfaces-edit-all explanation="경쟁하는 정의로 충돌과 예측할 수 없는 재적용이 발생합니다."}
::option[어느 네트워크 관리자가 인터페이스를 소유하는지 확인합니다.]{#interfaces-identify-owner .correct explanation="올바른 설정 소스와 적용 방법은 소유권에 따라 달라집니다."}
::option[검사 전에 현재 경로를 모두 삭제합니다.]{#interfaces-delete-routes explanation="복구 접근을 없앨 수 있는 파괴적 작업입니다."}
:::

## 변경 검증하기

링크 상태, 할당된 주소와 수명, 선택된 경로, 확인자 상태, 이웃 연결 및 실제 애플리케이션을 검증합니다. 영구 변경에는 복구 경로가 있을 때만 통제된 서비스 재시작이나 재부팅을 테스트합니다.

:::single-choice{#interfaces-change-verification} `ip address`에 새 주소가 보이는 것보다 더 나은 증거는 무엇입니까?

::option[인터페이스 이름에 숫자가 들어 있습니다.]{#interfaces-digit explanation="이름은 종단 간 검증을 제공하지 않습니다."}
::option[셸 프롬프트 색상이 그대로입니다.]{#interfaces-prompt-color explanation="터미널 모양은 네트워크 작동과 관계없습니다."}
::option[경로, 확인자 상태 및 의도한 애플리케이션도 작동합니다.]{#interfaces-end-to-end .correct explanation="사용 가능한 설정은 전체 경로와 서비스 동작에 따라 달라집니다."}
:::

## 요약

이제 런타임 상태와 영구 정책을 혼동하지 않고 인터페이스를 조사하고 변경할 수 있습니다.

1. 실제 인터페이스 이름과 주소를 찾습니다.
2. 관리 상태와 운영 연결을 구분합니다.
3. 직접 실행한 `ip` 변경을 현재 커널 상태로 다룹니다.
4. 영구 변경 전에 활성 설정 소유자를 식별합니다.
5. 이후 라우팅, 이름 확인 및 애플리케이션 동작을 검증합니다.
