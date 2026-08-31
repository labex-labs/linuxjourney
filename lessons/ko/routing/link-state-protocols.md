---
lesson_id: "link-state-protocols"
course_id: "routing"
lang: "ko"
order_index: 6
title: "링크 상태 프로토콜"
description: "링크 상태 프로토콜이 인접 관계를 만들고 토폴로지 정보를 플러딩하며 경로를 계산하는 방법을 알아봅니다."
meta_title: "링크 상태 프로토콜 - 라우팅"
meta_description: "대규모 네트워크를 위한 OSPF 같은 링크 상태 프로토콜을 알아봅니다. 빠른 수렴과 라우팅 테이블 갱신 방식을 설명합니다."
meta_keywords: "링크 상태 프로토콜, OSPF, 리눅스 네트워킹, 라우팅 프로토콜, 네트워크 토폴로지"
---

링크 상태 프로토콜은 로컬 링크와 접두사를 설명하고, 그 설명을 라우팅 범위 전체에 배포하며, 각 라우터가 토폴로지 데이터베이스에서 경로를 계산하도록 합니다. OSPF와 IS-IS가 일반적인 예입니다.

## 인접 관계 형성하기

라우터는 호환되는 이웃을 찾고 인터페이스 유형, 영역, 타이머, 인증 및 기타 매개변수에 따라 프로토콜 인접 관계를 형성합니다. hello 패킷이 보인다고 완전한 인접 관계가 보장되지는 않습니다. 설정 불일치가 상태 머신을 더 이른 단계에서 멈출 수 있습니다.

:::single-choice{#link-state-hello-limit}
OSPF hello를 수신했다는 사실만으로 입증할 수 없는 것은 무엇입니까?

::option[라우터가 완전히 동기화된 인접 관계를 형성했습니다.]{#link-state-not-full .correct explanation="영역, 타이머, 인증, MTU 및 기타 상태 때문에 완전한 데이터베이스 교환이 실패할 수 있습니다."}
::option[이웃이 프로토콜 메시지를 하나 이상 보냈습니다.]{#link-state-hello-sent explanation="hello 수신이 그 제한적인 사실을 직접 입증합니다."}
::option[인터페이스가 프레임을 수신할 수 있습니다.]{#link-state-frame-received explanation="수신된 패킷은 로컬 수신 경로 일부가 작동했음을 입증합니다."}
:::

## 링크 상태 정보 플러딩하기

각 라우터는 관련 상태에 대한 광고를 생성합니다. 이웃은 최신 정보를 원래 이웃 쌍 사이에만 두지 않고 정의된 영역이나 도메인 전체에 신뢰성 있게 플러딩합니다. 순서와 에이징 메커니즘으로 현재 정보를 구분하고 오래된 상태를 제거합니다.

:::single-choice{#link-state-flooding-scope}
링크 상태 정보를 하나의 이웃 너머로 플러딩하는 이유는 무엇입니까?

::option[모든 애플리케이션에 모든 라우터 암호 사본이 필요하기 때문입니다.]{#link-state-password-copy explanation="응용 자격 증명은 토폴로지 광고가 아닙니다."}
::option[Ethernet이 유니캐스트 프레임을 보낼 수 없기 때문입니다.]{#link-state-no-unicast explanation="Ethernet은 유니캐스트를 지원하며 여기서 플러딩은 라우팅 프로토콜 배포 메커니즘입니다."}
::option[라우팅 범위의 라우터에 일관된 토폴로지 데이터베이스가 필요하기 때문입니다.]{#link-state-consistent-database .correct explanation="각 라우터는 현재 링크 상태 광고의 공유 집합에서 경로를 계산합니다."}
:::

## 최단 경로 계산하기

링크 상태 데이터베이스를 만든 뒤 라우터는 자신을 루트로 최단 경로 우선 알고리즘, 일반적으로 Dijkstra 알고리즘을 실행합니다. OSPF는 인터페이스 비용을 합산하며 정책과 동일 비용 규칙이 설치할 결과에 영향을 줍니다.

“최단”은 라우터 수가 가장 적거나 측정된 응용 지연 시간이 가장 낮다는 뜻이 아니라 프로토콜 비용이 가장 낮다는 뜻입니다. 비용 설계는 운영 의도를 반영해야 합니다.

:::single-choice{#link-state-shortest-meaning}
링크 상태 경로 계산에서 “최단”은 무엇을 뜻합니까?

::option[접두사를 쓴 문자가 가장 적은 경로입니다.]{#link-state-shortest-text explanation="텍스트 길이는 토폴로지 비용과 관계없습니다."}
::option[프로토콜 비용 합계가 가장 작은 경로입니다.]{#link-state-lowest-cost .correct explanation="비용 모델은 홉 수나 현재 지연 시간과 직접 대응하지 않을 수 있습니다."}
::option[패킷 손실이 항상 0인 경로입니다.]{#link-state-zero-loss explanation="계산된 경로는 애플리케이션 성능을 보장하지 않습니다."}
:::

## 영역과 수렴

OSPF 영역은 토폴로지 플러딩 및 계산 범위를 제한하며 정상적인 영역 간 설계에서는 Area 0이 백본 역할을 합니다. 요약과 영역 유형으로 라우터마다 의도적으로 서로 다른 데이터베이스 세부 수준을 제공할 수 있습니다.

링크 변경 후 감지, 광고 플러딩, SPF 계산, 경로 설치 및 전달 복구에 각각 시간이 걸립니다. 단순한 거리 벡터 설계보다 빠르게 수렴할 수 있지만 모든 장애나 설정에서 자동으로 보장되지는 않습니다.

:::single-choice{#link-state-convergence-stages}
OSPF 수렴 조사 중 무엇을 측정해야 합니까?

::option[관리자가 터미널을 연 시각만 측정합니다.]{#link-state-terminal-time explanation="프로토콜 또는 전달 단계를 격리하지 못합니다."}
::option[라우터 이름의 알파벳 순서만 측정합니다.]{#link-state-router-names explanation="이름은 수렴 시간을 결정하지 않습니다."}
::option[감지, 플러딩, 계산, 설치 및 전달 복구를 측정합니다.]{#link-state-all-stages .correct explanation="단계를 분리하면 수렴 지연이나 장애가 발생한 위치를 알 수 있습니다."}
:::

## 요약

이제 이웃 탐색부터 설치된 경로까지 링크 상태 라우팅을 추적할 수 있습니다.

1. hello 수신과 완전한 인접 관계를 구분합니다.
2. 라우팅 범위 전체의 신뢰성 있는 플러딩을 설명합니다.
3. 최단 경로를 설정된 프로토콜 비용이 가장 낮은 경로로 해석합니다.
4. 제어 및 데이터 평면의 모든 수렴 단계를 측정합니다.
