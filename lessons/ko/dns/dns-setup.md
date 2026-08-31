---
lesson_id: "dns-setup"
course_id: "dns"
lang: "ko"
order_index: 5
title: "DNS 설정"
description: "권위 또는 재귀 DNS 서비스를 선택하고 보호하며 검증하고 운영하는 방법을 알아봅니다."
meta_title: "DNS 설정 - DNS"
meta_description: "BIND, dnsmasq 및 PowerDNS 같은 리눅스 DNS 서버를 알아봅니다. 네트워크 요구 사항에 맞는 DNS 서버 역할을 선택하는 방법을 설명합니다."
meta_keywords: "리눅스 DNS, BIND, dnsmasq, PowerDNS, DNS 서버 설정, 리눅스 네트워킹"
---

DNS 소프트웨어는 보편적인 “최고의 서버”가 아니라 역할과 운영 요구 사항에 따라 선택해야 합니다. 권위 서비스는 영역을 게시하고, 재귀 서비스는 이름을 확인하고 캐싱해 클라이언트에 응답하며, 전달 확인자는 쿼리를 다른 확인자에 보냅니다. 역할을 결합하면 공격 표면이 달라집니다.

## 역할과 구현 선택하기

- BIND는 폭넓은 표준 지원과 함께 권위 및 재귀 서비스를 제공할 수 있습니다.
- Unbound는 검증하는 재귀 확인자로 흔히 배포됩니다.
- dnsmasq는 규모가 작은 통제된 네트워크를 위한 경량 전달, 캐싱 및 DHCP 기능을 제공합니다.
- PowerDNS는 여러 데이터 백엔드와 함께 별도의 권위 및 재귀 제품을 제공합니다.

기능과 패키징은 바뀌므로 설치된 버전의 공식 문서를 확인하십시오. 필요한 역할만 배포하고 의도하지 않은 재귀 또는 영역 서비스를 비활성화합니다.

:::single-choice{#dns-setup-authoritative-role}
제공하는 영역의 확정 레코드를 게시하는 역할은 무엇입니까?

::option[권위 DNS 서버입니다.]{#dns-setup-authoritative .correct explanation="임의 이름을 재귀적으로 찾지 않고 설정된 영역 권위에서 응답합니다."}
::option[Ethernet 스위치입니다.]{#dns-setup-switch explanation="스위치는 링크 계층 프레임을 전달하며 DNS 영역을 게시하지 않습니다."}
::option[임의 클라이언트 쿼리에 응답하는 재귀 확인자입니다.]{#dns-setup-stub explanation="스텁은 재귀 서비스에 쿼리를 보내며 권위 영역을 호스팅하지 않습니다."}
:::

## 설치 전 설계하기

영역, 클라이언트, 쿼리 양, 갱신 메커니즘, DNSSEC 요구 사항, 로깅, 모니터링, 백업 및 복구를 정의합니다. 권위 영역에는 이중화된 서버와 올바르게 등록된 위임이 필요합니다. 재귀 서비스에는 명시적인 클라이언트 접근 제어, 캐시 정책, 상위 또는 반복 조회 연결 및 악용 방지가 필요합니다.

제한 없는 재귀 기능을 인터넷에 공개하지 마십시오. 개방형 확인자는 반사 공격에 악용되고 로컬 리소스를 소모할 수 있습니다.

:::single-choice{#dns-setup-open-recursion}
재귀 쿼리를 승인된 클라이언트로 제한해야 하는 이유는 무엇입니까?

::option[재귀 DNS는 어떤 레코드도 캐시할 수 없기 때문입니다.]{#dns-setup-no-cache explanation="캐싱은 재귀 확인자의 핵심 기능입니다."}
::option[권위 위임이 모든 사용자에게 root 권한을 요구하기 때문입니다.]{#dns-setup-all-root explanation="DNS 위임은 운영체제 권한을 부여하지 않습니다."}
::option[개방형 재귀가 증폭 및 리소스 소모에 악용될 수 있기 때문입니다.]{#dns-setup-recursion-abuse .correct explanation="접근 제어는 확인자가 공용 공격 인프라로 사용되는 일을 줄입니다."}
:::

## 설정과 영역 데이터 검증하기

다시 불러오기 전에 구현체의 구문 및 영역 검사 도구를 사용합니다. BIND의 일반적인 예시는 다음과 같습니다.

```bash
$ named-checkconf
$ named-checkzone example.com /etc/bind/zones/db.example.com
```

호스트에 맞는 권한과 경로로 실행합니다. 파서 성공은 위임, 시리얼 전파, DNSSEC 체인, 방화벽 연결 또는 올바른 응답을 입증하지 않으므로 통제된 쿼리로 이어서 확인하십시오.

:::single-choice{#dns-setup-zone-validation-limit}
성공한 영역 구문 검사가 입증하지 못하는 것은 무엇입니까?

::option[위임과 종단 간 권위 응답이 작동합니다.]{#dns-setup-not-end-to-end .correct explanation="상위 데이터, 서비스 활성화, 네트워크 정책 및 런타임 로딩은 별개입니다."}
::option[검사기가 영역 텍스트를 파싱할 수 있습니다.]{#dns-setup-parser-proves explanation="검사기가 직접 제공하는 증거입니다."}
::option[파일에 레코드 소유자 필드가 있습니다.]{#dns-setup-record-owner explanation="유효한 레코드 파싱으로 구조적 측면을 이미 검사합니다."}
:::

## 안전하게 적용 및 테스트하기

현재 설정과 복구 접근을 보존하고 검증한 뒤 지원된다면 재시작 대신 다시 불러옵니다. 재귀를 비활성화한 상태로 각 권위 서버를 직접 조회하고 SOA 시리얼, NS 집합, 긍정 레코드, 존재하지 않는 이름 및 UDP와 TCP 동작을 비교합니다.

```bash
$ dig @192.0.2.53 example.com SOA +norecurse
$ dig @192.0.2.53 missing.example.com A +norecurse
$ dig @192.0.2.53 example.com SOA +norecurse +tcp
```

재귀 서비스에서는 허용 및 거부된 클라이언트 네트워크, DNSSEC 검증, 캐시 동작 및 상위 의존성 장애를 테스트합니다.

:::single-choice{#dns-setup-norecurse-test}
권위 서버를 `+norecurse`로 조회하는 이유는 무엇입니까?

::option[재귀를 요청하지 않고 권위 응답을 테스트합니다.]{#dns-setup-authority-only .correct explanation="영역 서비스와 재귀 동작을 구분합니다."}
::option[영역의 모든 레코드를 제거합니다.]{#dns-setup-remove-records explanation="쿼리는 권위 데이터를 편집하지 않습니다."}
::option[모든 응답을 HTTP로 강제합니다.]{#dns-setup-force-http explanation="이 옵션은 DNS recursion-desired 플래그를 제어합니다."}
:::

## 서비스 운영하기

쿼리 실패, 지연 시간, 캐시 동작, 리소스 사용량, 영역 전송, 시리얼 일관성, DNSSEC 만료 및 위임 상태를 모니터링합니다. 소스 설정과 서명 자료를 안전하게 백업하되 새 인스턴스가 영역을 불러와 올바른 응답을 제공할 수 있는지도 검증합니다. 지원되는 버전을 패치하고 제어 인터페이스, 동적 갱신 및 전송 접근을 제한합니다.

:::single-choice{#dns-setup-redundancy-verification}
권위 DNS 이중화 테스트에는 무엇이 포함되어야 합니까?

::option[각 서버를 조회하고 다른 서버를 사용할 수 없을 때의 작동을 테스트합니다.]{#dns-setup-test-each-server .correct explanation="여러 NS 레코드를 나열하는 것만으로 각 독립 서비스의 연결 가능성과 최신 상태가 입증되지는 않습니다."}
::option[모든 서버의 호스트 이름이 비슷한지만 확인합니다.]{#dns-setup-hostname-similarity explanation="이름은 데이터 동기화나 가용성을 입증하지 않습니다."}
::option[광고된 모든 서버에 하나의 공유 프로세스와 디스크를 사용합니다.]{#dns-setup-shared-failure explanation="공유 장애 도메인은 이중화를 약화합니다."}
:::

## 요약

이제 명시적인 권위 또는 재귀 역할을 중심으로 DNS 배포를 설계할 수 있습니다.

1. 필요한 역할을 정의한 뒤 소프트웨어를 선택합니다.
2. 재귀와 관리 인터페이스를 제한합니다.
3. 다시 불러오기 전에 설정과 영역을 검증합니다.
4. 권위, 부재, 전송 및 클라이언트 정책을 직접 테스트합니다.
5. 이중화, DNSSEC, 데이터 일관성 및 복구를 모니터링합니다.
