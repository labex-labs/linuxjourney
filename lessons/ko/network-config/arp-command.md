---
lesson_id: "arp-command"
course_id: "network-config"
lang: "ko"
order_index: 5
title: "arp"
description: "리눅스 IPv4 ARP 및 IPv6 이웃 캐시 상태를 조사하고 해석하는 방법을 알아봅니다."
meta_title: "arp - 네트워크 설정"
meta_description: "리눅스 ARP와 ARP 캐시를 확인하는 방법을 알아봅니다. 네트워크 통신에서 ARP의 역할과 ip neighbor 명령을 설명합니다."
meta_keywords: "리눅스 ARP, ARP 캐시, ip neighbour show, 네트워크 명령, 리눅스 네트워킹"
---

리눅스는 최근 확인한 다음 홉 링크 주소를 이웃 테이블에 저장합니다. Ethernet상의 IPv4 항목은 ARP로 학습하고 IPv6는 Neighbor Discovery를 사용합니다. 기존 `arp` 명령은 이 상태의 일부만 보여 주지만 `ip neighbor`는 두 주소 계열을 모두 처리합니다.

## 이웃 항목 보기

모든 항목 또는 하나의 인터페이스를 조사합니다.

```bash
$ ip neighbor show
$ ip neighbor show dev enp1s0
```

항목에는 IP 주소, 링크 계층 주소, 장치 및 연결 상태가 들어 있습니다. 부팅 후 테이블이 비어 있다가 트래픽에 로컬 다음 홉이 필요할 때 채워질 수 있습니다.

:::single-choice{#arp-command-modern-view}
현대적인 리눅스 이웃 테이블 상태를 표시하는 명령은 무엇입니까?

::option[`pwd neighbor`]{#arp-command-pwd explanation="pwd는 셸의 작업 디렉터리를 보고합니다."}
::option[`ip neighbor show`]{#arp-command-ip-neighbor .correct explanation="IPv4 ARP 기반 항목과 IPv6 Neighbor Discovery 항목을 모두 보고합니다."}
::option[`route --passwords`]{#arp-command-route-passwords explanation="그런 경로 검사 명령으로 자격 증명을 노출하면 안 됩니다."}
:::

## IPv4 이웃 확인하기

링크상 IPv4 매핑이 없으면 호스트가 대상 주소의 소유자를 묻는 ARP 요청을 브로드캐스트합니다. 대상 또는 명시적으로 프록시 ARP를 수행하는 라우터가 응답합니다. 송신자는 매핑을 캐시하고 대기 중인 프레임을 전송합니다.

원격 IP 목적지의 경우 호스트는 원격 호스트의 MAC이 아니라 선택된 게이트웨이 주소를 확인합니다.

:::single-choice{#arp-command-remote-target}
호스트는 링크 밖 목적지에 대해 어느 IPv4 이웃을 확인합니까?

::option[모든 라우터 너머의 최종 원격 서버입니다.]{#arp-command-final-server explanation="그 MAC 주소는 출발지 링크에서 의미가 없습니다."}
::option[확인자 설정에 나열된 모든 DNS 서버입니다.]{#arp-command-all-dns explanation="이웃 확인은 확인자 목록이 아니라 선택된 경로를 따릅니다."}
::option[선택된 링크상 게이트웨이입니다.]{#arp-command-gateway .correct explanation="로컬 Ethernet 프레임은 IP 패킷을 전달할 라우터를 목적지로 합니다."}
:::

## 상태 해석하기

일반적인 상태에는 `REACHABLE`, `STALE`, `DELAY`, `PROBE`, `INCOMPLETE` 및 `FAILED`가 있습니다. `STALE`은 최근 연결 확인이 만료됐다는 뜻입니다. 스택이 필요에 따라 프로브하는 동안에도 캐시된 주소를 사용할 수 있습니다. `FAILED`는 주소 확인이나 연결 감지가 성공하지 못했음을 나타내지만 링크, VLAN, 주소, 경로, 필터링 또는 통신 상대 중단 등 여러 원인이 있을 수 있습니다.

:::single-choice{#arp-command-stale-state}
`STALE`은 이웃에 도달할 수 없다고 확인됐다는 뜻입니까?

::option[아니요. 최근 확인이 없으며 사용할 때 프로브할 수 있다는 뜻입니다.]{#arp-command-stale-probe .correct explanation="FAILED와 같은 상태가 아닙니다."}
::option[예. 항목을 다시는 사용할 수 없습니다.]{#arp-command-stale-dead explanation="오래된 항목도 후보로 남으며 연결 검사 후 상태가 바뀔 수 있습니다."}
::option[예. DNS 레코드가 만료됐기 때문입니다.]{#arp-command-stale-dns explanation="이웃 상태와 DNS 캐싱은 서로 별개입니다."}
:::

## 이웃 상태를 신중하게 변경하기

정적 항목과 캐시 플러시는 상태를 변경하며 활성 트래픽을 중단하거나 원래 증거를 숨길 수 있습니다. 먼저 현재 경로, 패킷 카운터 및 이웃 상태를 기록합니다. 전체 인터페이스를 비우기 전에 승인된 테스트 네트워크에서 대상 프로브와 패킷 캡처를 우선하십시오.

ARP에는 내장 인증이 없으므로 중복 주소나 위조 응답이 매핑을 오염시킬 수 있습니다. 스위치 보호, 분할, 모니터링 및 상위 계층 인증이 영향을 줄이는 데 도움이 됩니다.

:::single-choice{#arp-command-flush-first}
첫 진단 단계로 전체 이웃 테이블을 비우면 안 되는 이유는 무엇입니까?

::option[이웃 항목이 DNS 루트 서버에만 저장되기 때문입니다.]{#arp-command-neighbors-dns explanation="로컬 네트워크 스택이 유지합니다."}
::option[플러시가 인터페이스 하드웨어를 영구적으로 제거하기 때문입니다.]{#arp-command-flush-hardware explanation="물리 장치가 아니라 캐시 항목을 제거합니다."}
::option[증거를 바꾸고 정상적으로 작동하던 다음 홉을 중단할 수 있기 때문입니다.]{#arp-command-flush-disrupts .correct explanation="읽기 전용 조사와 대상 테스트는 원인 진단에 필요한 상태를 보존합니다."}
:::

## 요약

이제 모든 캐시 상태를 장애로 취급하지 않고 이웃 확인을 조사할 수 있습니다.

1. IPv4와 IPv6 상태에 `ip neighbor`를 사용합니다.
2. 목적지가 링크상에 있을 때만 그 주소를 직접 확인합니다.
3. 링크 밖 IP 트래픽에는 게이트웨이 주소를 확인합니다.
4. 대상 상태 변경 전에 캐시 증거를 보존합니다.
