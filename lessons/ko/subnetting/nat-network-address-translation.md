---
lesson_id: "nat-network-address-translation"
course_id: "subnetting"
lang: "ko"
order_index: 6
title: "NAT"
description: "출발지, 목적지 및 포트 변환이 IPv4 흐름과 연결 상태를 변경하는 방법을 알아봅니다."
meta_title: "NAT - 서브넷팅"
meta_description: "리눅스의 NAT가 작동하는 방식과 사설 및 공인 IP의 차이를 알아봅니다. 네트워크 보안과 NAT의 관계도 설명합니다."
meta_keywords: "NAT, 네트워크 주소 변환, 리눅스 네트워킹, 사설 IP, 공인 IP"
---

NAT(Network Address Translation)는 패킷이 변환 장치를 통과할 때 주소 필드와 흔히 전송 포트까지 다시 씁니다. 사설 주소를 사용하는 IPv4 네트워크를 더 적은 수의 외부 라우팅 가능 주소로 연결하는 데 널리 사용됩니다.

## 출발지 변환

출발지 NAT는 패킷이 네트워크를 떠날 때 출발지 주소를 바꿉니다. 다대일 배포에서는 여러 내부 흐름이 하나의 외부 주소를 공유할 수 있도록 출발지 포트도 변환합니다. 포트를 인식하는 이 형식은 흔히 NAPT, PAT 또는 외부 주소가 바뀔 수 있을 때 masquerading이라고 부릅니다.

변환기는 응답 패킷을 원래 내부 끝점으로 다시 쓸 수 있도록 매핑을 추적합니다. 일반적으로 같은 전송 흐름을 전달하며 응용 프록시처럼 별도의 프록시 연결을 열 필요는 없습니다.

:::single-choice{#nat-source-translation}
출발지 NAT는 외부로 나가는 패킷에서 무엇을 바꿉니까?

::option[목적지 애플리케이션의 파일 권한만 바꿉니다.]{#nat-file-permissions explanation="NAT는 원격 파일시스템이 아니라 네트워크 및 전송 헤더에서 작동합니다."}
::option[출발지 주소와 다대일 사용에서는 흔히 출발지 포트를 바꿉니다.]{#nat-source-fields .correct explanation="이 매핑으로 반환 트래픽을 원래 내부 흐름과 연결할 수 있습니다."}
::option[클라이언트가 영구 저장한 DNS 이름을 바꿉니다.]{#nat-dns-name explanation="변환은 클라이언트의 이름 서비스 데이터베이스를 다시 쓰지 않습니다."}
:::

## 목적지 변환

목적지 NAT는 목적지 주소나 포트를 다시 쓰며, 일반적으로 외부 끝점을 통해 내부 서비스를 공개하는 데 사용합니다. 포트 전달 규칙은 외부 TCP 포트를 다른 내부 주소 및 포트에 매핑할 수 있습니다. 반환 트래픽에는 일관된 역변환이 필요합니다.

:::single-choice{#nat-port-forward}
수신 포트 전달을 일반적으로 구현하는 NAT 형식은 무엇입니까?

::option[경로 조회 전 출발지 NAT만 사용합니다.]{#nat-snat-port-forward explanation="내부 목적지를 공개하려면 목적지 필드 변환이 필요합니다."}
::option[주소나 포트 변환을 전혀 사용하지 않습니다.]{#nat-no-translation explanation="포트 전달 규칙은 정의상 변환 정책입니다."}
::option[목적지 NAT입니다.]{#nat-dnat .correct explanation="DNAT는 외부 목적지를 선택한 내부 서비스 끝점에 매핑합니다."}
:::

## NAT와 방화벽 정책

NAT는 방화벽이 아닙니다. 상태 저장 변환기에 요청하지 않은 수신 트래픽을 위한 매핑이 없을 수 있지만 명시적인 전달, 목적지 변환, 필터링 및 애플리케이션 공개가 연결 가능성을 결정합니다. 주소 재작성에서 보안 정책을 추론하지 말고 방화벽 규칙, 최소 권한 서비스 및 종단 간 제어로 정책을 표현하고 감사합니다.

:::single-choice{#nat-not-firewall}
NAT 자체를 보안 정책으로 취급하면 안 되는 이유는 무엇입니까?

::option[NAT가 모든 페이로드를 자동으로 암호화하기 때문입니다.]{#nat-encrypts explanation="주소 변환은 페이로드 기밀성을 제공하지 않습니다."}
::option[변환 규칙과 트래픽 필터링 규칙의 목적이 다르기 때문입니다.]{#nat-filter-separate .correct explanation="변환이 있어도 연결 가능성과 권한 부여에는 명시적인 필터링 및 서비스 정책이 필요합니다."}
::option[NAT가 관리자의 방화벽 규칙 정의를 막기 때문입니다.]{#nat-prevents-firewall explanation="변환과 방화벽 정책은 흔히 함께 사용됩니다."}
:::

## 운영상 결과

NAT는 주소 및 포트 매핑을 소진하고, 피어 투 피어 프로토콜을 복잡하게 만들고, 애플리케이션에서 원래 출발지를 가리며, 주소를 포함하는 프로토콜에 특별한 처리를 요구할 수 있습니다. 흐름을 추적해야 한다면 로그에 변환 타임스탬프와 매핑 세부 정보를 보존해야 합니다.

리눅스에서 현대적인 정책은 흔히 nftables와 연결 추적으로 설정합니다. 변경 전에 실제 규칙 세트를 조사하십시오.

```bash
$ sudo nft list ruleset
$ sudo conntrack -L
```

둘째 명령에는 conntrack 도구와 권한이 필요합니다. 규칙 세트 변경으로 원격 접근이 끊길 수 있으므로 콘솔 복구, 원자적 설정, 검증 및 되돌리기를 사용합니다.

:::single-choice{#nat-trace-flow}
공유 주소 흐름을 내부 클라이언트까지 추적하려면 어떤 증거가 필요합니까?

::option[시간이나 포트 없이 외부 주소만 필요합니다.]{#nat-address-only explanation="여러 클라이언트와 흐름이 그 주소를 공유할 수 있습니다."}
::option[클라이언트에 표시된 호스트 이름만 필요합니다.]{#nat-hostname-only explanation="변환기는 반드시 호스트 이름이 아니라 패킷 튜플을 매핑합니다."}
::option[프로토콜과 포트를 포함해 시간 상관관계가 있는 변환 매핑입니다.]{#nat-correlated-mapping .correct explanation="완전한 튜플과 타임스탬프로 동시에 변환된 흐름을 구분합니다."}
:::

## 요약

이제 주소 변환을 라우팅, 프록시 및 방화벽 정책과 구분할 수 있습니다.

1. 외부로 나가는 흐름의 출발지 변환을 식별합니다.
2. 공개된 서비스의 목적지 변환을 식별합니다.
3. 포트 매핑이 주소 공유를 가능하게 하는 방식을 이해합니다.
4. NAT를 보안으로 취급하지 말고 명시적인 필터링을 적용합니다.
5. 변경 중 매핑 증거와 복구 접근을 보존합니다.
