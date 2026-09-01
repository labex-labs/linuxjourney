---
lesson_id: "routing-protocols"
course_id: "routing"
lang: "ko"
order_index: 4
title: "라우팅 프로토콜"
description: "동적 라우팅 프로토콜이 연결 가능성을 교환하고 사용 가능한 전달 경로로 수렴하는 방법을 알아봅니다."
meta_title: "라우팅 프로토콜 - 라우팅"
meta_description: "리눅스 네트워킹의 라우팅 프로토콜 기초를 살펴봅니다. 거리 벡터, 링크 상태, 네트워크 수렴 및 라우팅 테이블 유지를 설명합니다."
meta_keywords: "라우팅 프로토콜, 네트워크 수렴, 거리 벡터, 링크 상태, 리눅스 네트워킹, 라우팅 테이블"
---

정적 경로는 직접 설정하지만 동적 라우팅 프로토콜은 연결 가능성과 토폴로지 정보를 교환해 라우터가 변화에 적응하도록 합니다. 동적 학습은 수작업을 줄이지만 모니터링해야 할 프로토콜 상태, 신뢰 경계, 타이머 및 장애 모드를 추가합니다.

## 제어 평면과 전달 평면

라우팅 프로토콜은 자체 데이터베이스에서 후보를 학습합니다. 라우터는 경로를 라우팅 정보 베이스에 선택하고 사용할 수 있는 다음 홉을 전달 테이블에 설치합니다. 그런 다음 하드웨어나 커널이 그 테이블에서 패킷을 전달합니다.

프로토콜 인접 관계가 수립됐다는 사실만으로 원하는 접두사가 학습, 선택, 설치됐거나 전달 정책에서 허용됐음을 입증할 수 없습니다.

:::single-choice{#routing-protocols-adjacency-limit} 수립된 라우팅 인접 관계만으로 입증할 수 없는 것은 무엇입니까?

::option[원하는 모든 경로가 설치되어 성공적으로 전달 중이라는 사실입니다.]{#routing-protocols-not-full-proof .correct explanation="경로 광고, 선택, 설치, 필터링 및 데이터 평면 작동은 별도의 단계입니다."}
::option[두 프로토콜 화자가 제어 메시지를 교환했다는 사실입니다.]{#routing-protocols-no-messages explanation="인접 관계 수립에는 일반적으로 프로토콜 통신이 필요합니다."}
::option[제어 평면이 존재한다는 사실입니다.]{#routing-protocols-no-control explanation="인접 관계 자체가 제어 평면 상태입니다."}
:::

## 내부 및 외부 라우팅

IGP(Interior Gateway Protocol)는 하나의 관리 라우팅 도메인 안에서 작동합니다. 예로 RIP, OSPF 및 IS-IS가 있습니다. BGP는 자율 시스템 내부 및 사이에서 정책으로 제어되는 연결 가능성을 교환하며 인터넷의 외부 라우팅 프로토콜입니다.

메트릭의 의미는 프로토콜마다 다릅니다. OSPF 비용, RIP 홉 수 및 BGP 속성 집합을 하나의 보편적인 숫자 척도처럼 비교할 수 없습니다. 구현체는 프로토콜별 선택 전이나 그와 함께 경로 선호도 또는 관리 거리를 사용해 소스 사이에서 선택합니다.

:::single-choice{#routing-protocols-metric-comparison} RIP 홉 수와 OSPF 비용을 직접 비교할 수 있습니까?

::option[예. 모든 라우팅 메트릭이 같은 단위를 사용합니다.]{#routing-protocols-universal-metric explanation="각 프로토콜은 자체 메트릭과 선택 과정을 정의합니다."}
::option[예. 단, 두 값이 모두 0일 때만 가능합니다.]{#routing-protocols-zero-metric explanation="표시된 숫자와 관계없이 의미가 서로 다릅니다."}
::option[아니요. 프로토콜별 의미가 다릅니다.]{#routing-protocols-specific-metric .correct explanation="서로 다른 메트릭을 하나의 척도로 취급하지 않고 구현 정책으로 소스 사이에서 선택합니다."}
:::

## 거리 벡터와 링크 상태

거리 벡터 프로토콜은 이웃을 통해 연결 가능성과 거리를 광고하고 이웃 보고에서 경로를 도출합니다. 링크 상태 프로토콜은 인접 관계를 만들고, 범위에 링크 상태 정보를 플러딩하고, 토폴로지 데이터베이스를 구축하고, 최단 경로 트리를 계산합니다. 현대 프로토콜에는 단순한 범주 요약으로 모두 설명하기 어려운 개선 사항이 있습니다.

:::single-choice{#routing-protocols-link-state-input} 링크 상태 라우터가 경로 계산에 사용하는 것은 무엇입니까?

::option[기본 게이트웨이의 호스트 이름만 사용합니다.]{#routing-protocols-hostname-only explanation="토폴로지 계산에는 링크와 접두사 정보가 필요합니다."}
::option[라우팅 범위의 링크를 설명하는 동기화된 데이터베이스입니다.]{#routing-protocols-link-database .correct explanation="라우터는 학습한 토폴로지에서 최단 경로 알고리즘을 실행합니다."}
::option[모든 호스트의 응용 계층 암호입니다.]{#routing-protocols-passwords explanation="라우팅 토폴로지 교환에는 최종 사용자 자격 증명이 필요하지 않습니다."}
:::

## 수렴

토폴로지나 정책이 바뀌면 라우터는 변화를 감지하고, 제어 정보를 전파하고, 경로를 계산하고, 전달 상태를 갱신합니다. 수렴은 영향을 받는 목적지에 대해 네트워크가 안정적이고 서로 사용할 수 있는 라우팅에 도달하는 과정과 결과입니다. 모든 라우터가 완전히 같은 테이블을 가질 필요는 없습니다. 역할과 정책이 의도적으로 다를 수 있습니다.

수렴 중에는 일시적인 손실, 루프 또는 블랙홀이 발생할 수 있습니다. 감지, 전파, 계산 및 설치를 별도로 측정하고 데이터 평면 프로브로 검증하십시오.

:::single-choice{#routing-protocols-convergence} 라우팅 수렴이란 무엇입니까?

::option[변경 후 안정적이고 사용 가능한 라우팅에 도달하는 과정입니다.]{#routing-protocols-stable-routing .correct explanation="제어 전파와 그 결과인 전달 갱신을 포함합니다."}
::option[모든 라우터가 동일한 전역 테이블을 저장해야 한다는 요구 사항입니다.]{#routing-protocols-identical-table explanation="정책, 영역 및 역할로 의도적인 차이가 생길 수 있습니다."}
::option[가능한 모든 라우팅 장애를 영구적으로 방지하는 것입니다.]{#routing-protocols-no-failure explanation="수렴된 네트워크에도 정책이나 용량 문제가 있을 수 있습니다."}
:::

## 요약

이제 동적 라우팅 정보를 프로토콜 교환부터 전달까지의 경로에 배치할 수 있습니다.

1. 학습한 후보, 선택한 경로 및 전달 항목을 구분합니다.
2. 내부 라우팅과 BGP 정책 교환을 구분합니다.
3. 메트릭은 해당 프로토콜의 의미 안에서만 비교합니다.
4. 제어 평면과 데이터 평면 모두에서 수렴을 검증합니다.
