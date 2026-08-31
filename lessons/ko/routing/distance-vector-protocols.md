---
lesson_id: "distance-vector-protocols"
course_id: "routing"
lang: "ko"
order_index: 5
title: "거리 벡터 프로토콜"
description: "거리 벡터 프로토콜이 이웃 광고에서 경로를 도출하고 루프를 제한하는 방법을 알아봅니다."
meta_title: "거리 벡터 프로토콜 - 라우팅"
meta_description: "네트워크 라우팅의 거리 벡터 프로토콜을 알아봅니다. RIP가 홉 수로 경로를 결정하는 방식과 한계를 설명합니다."
meta_keywords: "거리 벡터 프로토콜, 네트워크 라우팅, RIP, 라우팅 정보 프로토콜, 홉 수, 리눅스 네트워킹"
---

거리 벡터 라우팅은 어떤 목적지에 도달할 수 있는지와 거리를 설명하는 메트릭을 이웃에게 알립니다. 라우터는 이웃의 광고와 그 이웃까지의 비용을 결합해 자체 후보 경로를 도출합니다.

## 이웃을 통해 학습하기

라우터 A가 접두사까지 거리 3을 광고하고 라우터 B가 비용 1로 A에 도달한다면 B는 A를 통한 거리 4를 도출할 수 있습니다. 이 정보는 완전한 토폴로지 지도가 아니라 방향과 메트릭을 설명하므로 이 방식을 소문에 의한 라우팅이라고 부르기도 합니다.

:::single-choice{#distance-vector-derived-distance}
이웃이 메트릭 3을 광고하고 링크 비용이 1이면 그 이웃을 통해 도출되는 메트릭은 얼마입니까?

::option[2]{#distance-vector-two explanation="링크 비용은 빼는 대신 더합니다."}
::option[31]{#distance-vector-thirty-one explanation="값은 이어 붙일 10진수 자릿수가 아니라 메트릭입니다."}
::option[4]{#distance-vector-four .correct explanation="이웃 거리와 로컬 링크 비용을 결합해 후보 경로를 만듭니다."}
:::

## 루프와 무한대까지 세기

장애 후 이웃이 서로에게 경로를 잘못 되돌려 광고하며 메트릭을 점차 높일 수 있습니다. 프로토콜은 유한한 무한대 값, 분할 지평선, 경로 포이즈닝, 포이즌 리버스, 트리거 갱신 및 타이머로 이를 완화합니다. 이러한 메커니즘은 문제를 줄이지만 모든 토폴로지 변경을 즉시 수렴하게 만들지는 않습니다.

:::single-choice{#distance-vector-split-horizon}
분할 지평선은 무엇을 줄이기 위한 것입니까?

::option[모든 IPv4 주소의 비트 수입니다.]{#distance-vector-ip-bits explanation="IPv4 주소 크기는 라우팅 갱신과 독립적으로 고정됩니다."}
::option[응용 페이로드의 암호화 오버헤드입니다.]{#distance-vector-encryption explanation="이 기법은 경로 광고 방향과 관련됩니다."}
::option[학습한 경로를 그 경로를 알려 준 이웃 방향으로 다시 광고하는 일입니다.]{#distance-vector-no-return .correct explanation="그 방향의 광고를 억제하면 단순한 피드백 루프를 막는 데 도움이 됩니다."}
:::

## RIP 메트릭과 제한

RIP는 홉 수를 사용합니다. 메트릭 16인 경로는 도달 불가이므로 사용할 수 있는 최대 메트릭은 15입니다. 이는 루프 증가를 제한하지만 네트워크 지름도 제한합니다. 홉이 적다고 반드시 지연 시간이 낮거나 대역폭이 넓은 것은 아닙니다.

RIPv2는 주기적 갱신과 트리거 갱신을 사용하며 CIDR 정보를 지원합니다. 모든 상황에서 전체 테이블을 브로드캐스트하는 대신 일반적으로 갱신을 멀티캐스트합니다. 인증과 필터링은 여전히 명시적으로 설정해야 합니다.

:::single-choice{#distance-vector-rip-infinity}
RIP 메트릭 16은 무엇을 나타냅니까?

::option[병렬 링크 16개가 있는 가장 빠른 경로입니다.]{#distance-vector-fastest-16 explanation="RIP는 이 값을 도달 불가로 취급합니다."}
::option[목적지에 도달할 수 없다는 무한대입니다.]{#distance-vector-unreachable .correct explanation="RIP는 사용할 수 있는 경로를 15홉으로 제한합니다."}
::option[BGP에서 학습한 경로입니다.]{#distance-vector-bgp-route explanation="이 숫자에는 RIP 고유의 의미가 있습니다."}
:::

## 학습한 경로 평가하기

이웃 상태, 수신 및 광고한 접두사, 메트릭, 다음 홉, 경로 설치 및 데이터 평면 연결 가능성을 확인합니다. 경로가 RIP 안에서 유효해도 로컬 선호 정책에 따라 다른 경로 소스에 밀릴 수 있습니다.

:::single-choice{#distance-vector-fewest-hop-limit}
RIP에서 홉 수가 가장 적은 경로의 성능이 나쁠 수 있는 이유는 무엇입니까?

::option[홉 수가 링크 대역폭, 지연 시간, 손실 또는 혼잡을 나타내지 않기 때문입니다.]{#distance-vector-hop-limited .correct explanation="홉이 더 많은 경로가 더 좋은 링크와 애플리케이션 성능을 제공할 수 있습니다."}
::option[RIP가 항상 홉이 가장 많은 경로를 선택하기 때문입니다.]{#distance-vector-most-hops explanation="RIP 메트릭은 사용할 수 있는 홉 수가 더 작은 경로를 선호합니다."}
::option[홉 수를 디스크 공간 바이트로 측정하기 때문입니다.]{#distance-vector-disk-bytes explanation="저장 공간이 아니라 라우팅 전환 수를 셉니다."}
:::

## 요약

이제 거리 벡터 라우팅의 단순성과 한계를 모두 설명할 수 있습니다.

1. 이웃의 광고에서 후보 거리를 도출합니다.
2. 루프와 무한대까지 세기 동작을 알아봅니다.
3. RIP의 사용 가능 15홉 제한과 메트릭 16을 설명합니다.
4. 경로 설치와 데이터 평면 결과를 별도로 검증합니다.
