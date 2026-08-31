---
lesson_id: "routing-table"
course_id: "routing"
lang: "ko"
order_index: 2
title: "라우팅 테이블"
description: "리눅스 경로를 읽고 목적지에 대해 선택된 경로를 조사하는 방법을 알아봅니다."
meta_title: "라우팅 테이블 - 라우팅"
meta_description: "리눅스 라우팅 테이블을 이해하는 방법을 알아봅니다. 목적지, 게이트웨이, 인터페이스 및 현대적인 ip route 출력을 설명합니다."
meta_keywords: "리눅스 라우팅 테이블, 리눅스 경로, route 명령, 네트워크 라우팅, IP 라우팅, 목적지, 게이트웨이"
---

리눅스 라우팅 상태는 IP 목적지에 사용할 수 있는 다음 홉, 인터페이스 및 출발지를 결정합니다. 기존 `route -n` 보기도 여전히 접하지만 `ip route`가 현대적인 커널 라우팅 개념을 더 직접적으로 보여 줍니다.

## IPv4 경로 읽기

예제 출력은 다음과 같습니다.

```text
$ ip -4 route show
default via 192.168.224.2 dev eth0 proto dhcp src 192.168.224.10 metric 100
192.168.224.0/24 dev eth0 proto kernel scope link src 192.168.224.10 metric 100
```

연결된 `/24` 경로는 일치하는 목적지를 `eth0`을 통해 직접 보냅니다. 기본 경로는 다음 홉 게이트웨이 `192.168.224.2`를 사용합니다. `proto`는 경로가 설치된 방식을, `src`는 일치하는 트래픽의 선호 출발지를 나타내며, 메트릭은 그 밖의 조건이 비슷한 경로의 순위를 정하는 데 도움이 됩니다.

:::single-choice{#routing-table-via-meaning}
`via 192.168.224.2`는 무엇을 나타냅니까?

::option[경로를 사용할 수 있는 유일한 애플리케이션입니다.]{#routing-table-application explanation="애플리케이션 권한 부여는 via 키워드에 인코딩되지 않습니다."}
::option[경로의 다음 홉 게이트웨이입니다.]{#routing-table-next-hop .correct explanation="패킷의 IP 목적지는 유지하면서 링크상 라우터를 목적지로 프레임을 만듭니다."}
::option[경로의 파일시스템 마운트 지점입니다.]{#routing-table-mount explanation="라우팅 항목은 파일시스템이 아니라 네트워크 전달과 관련됩니다."}
:::

## 연결 경로와 기본 경로

`scope link`이고 `via` 다음 홉이 없는 경로는 해당 접두사를 인터페이스에서 직접 연결 가능한 것으로 취급합니다. 기본 경로는 모든 주소와 일치하지만 더 구체적인 적격 경로가 있으면 선택되지 않습니다.

:::single-choice{#routing-table-connected-route}
연결된 `scope link` 목적지에는 일반적으로 어떻게 도달합니까?

::option[연결 경로가 일치해도 기본 게이트웨이를 통합니다.]{#routing-table-connected-default explanation="연결된 접두사가 더 구체적이며 게이트웨이 피연산자가 없습니다."}
::option[목적지를 DNS 서버로 변환합니다.]{#routing-table-connected-dns explanation="이름 서비스는 이미 선택된 IP 경로의 일부가 아닙니다."}
::option[이웃 확인 후 지정된 인터페이스를 통해 직접 도달합니다.]{#routing-table-direct .correct explanation="호스트가 목적지의 링크상 주소를 확인하고 로컬에서 프레임을 만듭니다."}
:::

## 접두사 길이와 메트릭

경로 선택은 정책 규칙을 고려하고 가장 긴 적격 접두사를 선택합니다. 메트릭은 적절하게 비교할 수 있는 경로 집합 안에서 순위를 정합니다. 숫자가 더 낮다는 이유만으로 낮은 메트릭의 기본 경로가 일치하는 `/24`보다 우선하지 않습니다.

:::single-choice{#routing-table-prefix-before-default}
`192.168.224.50`에 일반적으로 더 구체적으로 일치하는 경로는 무엇입니까?

::option[`192.168.224.0/24 dev eth0`]{#routing-table-twenty-four .correct explanation="24비트 일치 접두사가 나열된 경로 중 가장 깁니다."}
::option[`default via 192.168.224.2`]{#routing-table-default-less-specific explanation="기본 경로의 접두사 길이는 0입니다."}
::option[`192.168.0.0/16 via 192.168.224.3`]{#routing-table-sixteen explanation="주소를 포함하지만 /24보다 적은 비트를 고정합니다."}
:::

## 정책 규칙과 여러 테이블

리눅스는 출발지, 마크, 인터페이스 또는 다른 선택자를 기반으로 하는 `ip rule` 정책에 따라 여러 라우팅 테이블을 조회할 수 있습니다. 따라서 주 테이블만 보면 실제 경로를 놓칠 수 있습니다.

```bash
$ ip rule show
$ ip route show table all
```

네트워크 네임스페이스와 VRF도 별도의 상태를 가질 수 있습니다. 영향을 받는 프로세스와 같은 컨텍스트에서 조사하십시오.

:::single-choice{#routing-table-policy-limit}
`ip route show`만으로 애플리케이션 경로를 설명하지 못할 수 있는 이유는 무엇입니까?

::option[정책 규칙이나 다른 네트워크 네임스페이스가 다른 라우팅 상태를 선택할 수 있습니다.]{#routing-table-policy-context .correct explanation="실제 조회는 패킷 속성과 프로세스의 네트워크 컨텍스트에 따라 달라집니다."}
::option[리눅스 라우팅 테이블에 목적지 접두사가 없습니다.]{#routing-table-no-prefixes explanation="목적지 접두사는 기본 경로 키입니다."}
::option[애플리케이션은 IP 패킷을 절대 보내지 않습니다.]{#routing-table-apps-never explanation="애플리케이션 트래픽은 네트워크 및 전송 프로토콜로 운반됩니다."}
:::

## 실제 경로 조회하기

커널에 목적지와 선택적인 출발지를 평가하도록 요청합니다.

```bash
$ ip route get 203.0.113.10
$ ip route get 203.0.113.10 from 192.168.224.10
```

결과는 그 순간의 로컬 조회를 예측합니다. 프로브를 보내지 않으며 이웃, 하위 경로, 방화벽 또는 애플리케이션 연결 가능성을 입증하지 않습니다.

:::single-choice{#routing-table-route-get-limit}
`ip route get`이 하지 않는 일은 무엇입니까?

::option[선택한 로컬 인터페이스와 다음 홉을 표시합니다.]{#routing-table-get-does-interface explanation="조회 결과의 주요 필드입니다."}
::option[목적지에 대한 현재 로컬 경로 정책을 평가합니다.]{#routing-table-get-does-policy explanation="이 명령은 커널 경로 조회를 수행합니다."}
::option[모든 하위 홉을 통한 성공적인 전송을 입증합니다.]{#routing-table-get-not-probe .correct explanation="종단 간 네트워크 프로브가 아니라 로컬 결정 쿼리입니다."}
:::

## 요약

이제 리눅스 라우팅 항목을 읽고 실제 로컬 결정을 조회할 수 있습니다.

1. 연결 경로와 게이트웨이를 통한 경로를 구분합니다.
2. 접두사, 인터페이스, 프로토콜, 출발지 및 메트릭 필드를 읽습니다.
3. 관련 메트릭을 비교하기 전에 최장 접두사 일치를 적용합니다.
4. 정책 테이블, 네임스페이스 및 VRF를 고려합니다.
5. `ip route get`을 연결 테스트가 아니라 조회로 다룹니다.
