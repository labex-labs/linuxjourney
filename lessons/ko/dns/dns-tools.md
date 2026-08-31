---
lesson_id: "dns-tools"
course_id: "dns"
lang: "ko"
order_index: 6
title: "DNS 도구"
description: "getent, resolvectl 및 dig로 시스템 이름 확인과 직접 DNS 쿼리를 비교하는 방법을 알아봅니다."
meta_title: "DNS 도구 - DNS"
meta_description: "dig와 nslookup 같은 필수 리눅스 DNS 도구를 알아봅니다. DNS 쿼리와 문제 해결 기법을 설명합니다."
meta_keywords: "nslookup, dig 명령, DNS 도구, 리눅스 DNS, DNS 문제 해결, 네임 서버 조회"
---

DNS 문제 해결은 어느 계층을 테스트하는지 식별하는 것부터 시작합니다. 시스템 확인자 도구에는 로컬 파일과 정책이 포함되지만 `dig`와 `nslookup`은 DNS 쿼리를 보내고 특정 서버를 직접 대상으로 할 수 있습니다.

## 시스템 확인자 테스트하기

일반적인 호스트 이름 서비스 경로를 사용합니다.

```bash
$ getent ahosts www.example.com
```

systemd-resolved 호스트에서는 링크별 서버, 검색 도메인 및 프로토콜 상태를 조사합니다.

```bash
$ resolvectl status
$ resolvectl query www.example.com
```

애플리케이션이 별도의 확인자 라이브러리나 프록시를 사용할 수 있으므로 출력이 다르면 애플리케이션을 통해 재현하십시오.

:::single-choice{#dns-tools-system-resolver}
설정된 시스템 이름 서비스 경로를 사용하는 명령은 무엇입니까?

::option[`dig @SERVER NAME`만 사용합니다.]{#dns-tools-dig-direct explanation="dig는 DNS 쿼리를 보내며 일반적으로 hosts 파일 매핑을 읽지 않습니다."}
::option[`ip link set down`]{#dns-tools-link-down explanation="이름 확인을 테스트하는 대신 인터페이스를 중단합니다."}
::option[`getent ahosts NAME`]{#dns-tools-getent .correct explanation="/etc/hosts, DNS 및 기타 Name Service Switch 소스를 반영할 수 있습니다."}
:::

## dig로 조회하기

이름과 레코드 유형을 지정합니다.

```bash
$ dig www.example.com A
$ dig www.example.com AAAA
$ dig example.com MX
```

출력은 응답 서버, 상태, 플래그, 질문, 응답, 권위, 추가 데이터, 쿼리 시간 및 전송 메타데이터를 식별합니다. `+short`는 스크립트에 편리하지만 진단에 필요한 증거를 숨깁니다.

:::single-choice{#dns-tools-record-type}
IPv6 주소 레코드를 요청하는 쿼리는 무엇입니까?

::option[`dig NAME AAAA`]{#dns-tools-aaaa .correct explanation="AAAA 레코드에 IPv6 주소가 들어 있습니다."}
::option[`dig NAME MX`]{#dns-tools-mx explanation="MX는 메일 교환기 레코드를 요청합니다."}
::option[정방향 이름에 `dig NAME PTR`을 사용합니다.]{#dns-tools-ptr-forward explanation="PTR은 일반적으로 역방향 조회 이름으로 요청합니다."}
:::

## 서버 선택하기

확인자 또는 권위 서버를 명시적으로 대상으로 합니다.

```bash
$ dig @192.0.2.53 www.example.com A
```

캐시와 권위를 구분할 때 설정된 재귀 확인자, 승인된 둘째 확인자 및 각 권위 서버를 비교합니다. `NOERROR` 상태에도 요청한 응답이 없을 수 있습니다. `NXDOMAIN`은 조회한 이름이 존재하지 않는다는 뜻이고 `SERVFAIL`은 서버가 쿼리를 완료하지 못했다는 뜻입니다.

:::single-choice{#dns-tools-noerror-empty}
`NOERROR`에 빈 응답 섹션이 있을 수 있습니까?

::option[예. 이름은 존재하지만 요청한 레코드 데이터가 없을 수 있습니다.]{#dns-tools-noerror-nodata .correct explanation="상태와 응답 수를 함께 해석해야 합니다."}
::option[아니요. 주소 레코드가 하나 이상 있음을 보장합니다.]{#dns-tools-noerror-always-answer explanation="이름이 존재하면서 요청한 유형의 데이터가 없을 수 있습니다."}
::option[아니요. 빈 응답은 언제나 Ethernet 장애입니다.]{#dns-tools-empty-ethernet explanation="링크 프레이밍이 아니라 DNS 의미로 유효한 데이터 없음 응답을 설명합니다."}
:::

## 재귀와 권위 확인하기

쿼리의 `rd`는 재귀를 요청하고 응답의 `ra`는 서버가 재귀를 제공한다고 나타냅니다. `aa`는 응답이 권위 있음을 뜻합니다. 재귀 캐시와 제공 중인 영역 데이터를 혼동하지 않도록 권위 서버를 `+norecurse`로 조회합니다.

`dig +trace NAME`은 루트 힌트에서 시작해 자체 반복 조회를 수행합니다. 해당 확인자의 캐시, 전달, 정책, DNSSEC 검증 및 네트워크 위치를 우회하므로 프로덕션 확인자와 결과가 다를 수 있습니다.

:::single-choice{#dns-tools-aa-flag}
`aa` 응답 플래그는 무엇을 뜻합니까?

::option[쿼리가 동일한 IPv4 주소 두 개를 사용했습니다.]{#dns-tools-two-addresses explanation="응답 수나 주소 계열과 관계없는 플래그입니다."}
::option[응답이 애플리케이션 자격 증명으로 암호화됐습니다.]{#dns-tools-aa-encrypted explanation="DNS 플래그는 암호화된 전송을 확립하지 않습니다."}
::option[응답이 권위 있습니다.]{#dns-tools-authoritative-answer .correct explanation="응답 서버가 응답 데이터에 대한 권위를 주장합니다."}
:::

## 역방향 및 TCP 쿼리 테스트하기

`-x`로 역방향 PTR 쿼리를 구성합니다.

```bash
$ dig -x 192.0.2.25
```

잘림, 영역 전송 또는 방화벽 차이를 조사할 때 TCP 기반 DNS를 테스트합니다.

```bash
$ dig +tcp @192.0.2.53 example.com SOA
```

현대 DNS는 UDP 또는 TCP 포트 53을 사용할 수 있으며 필요한 곳에서는 둘 다 허용해야 합니다. 잘림 플래그가 있는 UDP 응답을 받으면 규격을 따르는 클라이언트는 적절한 전송으로 다시 시도합니다.

:::single-choice{#dns-tools-tcp-test}
`dig +tcp`는 무엇을 바꿉니까?

::option[기본 UDP 시도 대신 TCP로 DNS 쿼리를 보냅니다.]{#dns-tools-use-tcp .correct explanation="전송 필터링과 더 큰 신뢰성 있는 스트림이 필요한 응답을 구분하는 데 도움이 됩니다."}
::option[TCP 서비스 이름 레코드만 요청합니다.]{#dns-tools-tcp-records explanation="요청하는 DNS 유형은 별도로 지정합니다."}
::option[서버의 확인자 설정을 영구적으로 바꿉니다.]{#dns-tools-tcp-persistent explanation="쿼리는 서버 설정을 편집하지 않습니다."}
:::

## 요약

이제 조사하는 확인자 계층에 맞는 DNS 도구를 선택할 수 있습니다.

1. 설정된 시스템 확인자 경로에는 `getent`를 사용합니다.
2. `dig`에 레코드 유형과 서버를 명시합니다.
3. 상태, 플래그, 섹션 및 응답 서버를 함께 해석합니다.
4. 재귀 캐시와 권위 데이터를 구분합니다.
5. 역방향 쿼리와 필요한 두 DNS 전송을 모두 테스트합니다.
