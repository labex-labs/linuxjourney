---
lesson_id: "osi-model"
course_id: "network-basics"
lang: "ko"
order_index: 2
title: "OSI 모델"
description: "7계층 OSI 참조 모델이 네트워크 기능과 문제 해결 용어를 구성하는 방법을 알아봅니다."
meta_title: "OSI 모델 - 네트워크 기초"
meta_description: "네트워킹의 기초인 7계층 OSI 모델을 살펴봅니다. 이 이론적 개념이 TCP/IP 모델에 미친 영향과 리눅스 네트워킹에서의 중요성을 알아봅니다."
meta_keywords: "OSI 리눅스, OSI 모델, 네트워킹 개념, TCP/IP, 리눅스 네트워킹, 네트워크 계층, 7계층 모델"
---

OSI(Open Systems Interconnection) 모델은 7계층 참조 프레임워크입니다. 엔지니어가 책임, 인터페이스 및 장애의 위치를 설명할 때 공통으로 사용하는 어휘를 제공합니다. 모든 구현을 문자 그대로 묘사한 것은 아닙니다.

## 7개 계층

가장 낮은 계층부터 높은 계층까지 OSI 계층은 다음과 같습니다.

1. 물리: 신호, 매체, 커넥터 및 비트 전송
2. 데이터 링크: 로컬 프레임, 링크 주소 지정 및 매체 접근
3. 네트워크: 논리적 주소 지정 및 네트워크 간 전달
4. 전송: 끝점 또는 프로세스 간 통신
5. 세션: 통신 세션 관리
6. 표현: 데이터 표현, 변환 및 인코딩
7. 응용: 애플리케이션이 사용하는 네트워크 서비스

:::single-choice{#osi-network-layer-number}
논리적 주소 지정과 네트워크 간 전달을 처리하는 OSI 계층은 무엇입니까?

::option[3계층 네트워크입니다.]{#osi-layer-three .correct explanation="네트워크 계층은 논리적 주소 지정과 네트워크 간 전달을 설명합니다."}
::option[1계층 물리입니다.]{#osi-layer-one explanation="물리 계층은 신호와 매체를 다룹니다."}
::option[7계층 응용입니다.]{#osi-layer-seven explanation="응용 계층은 네트워크 애플리케이션에 제공되는 서비스를 설명합니다."}
:::

## 모델을 공통 어휘로 사용하기

“2계층 루프”나 “4계층 포트” 같은 표현은 모든 구현 세부 정보를 설명하지 않고도 기능 영역을 지목합니다. 실제 프로토콜은 경계를 가로지를 수 있으며 암호화, 터널, 프록시 또는 오버레이로 여러 계층이 중첩될 수 있습니다.

:::single-choice{#osi-model-purpose}
일상적인 문제 해결에서 OSI 모델은 무엇에 가장 유용합니까?

::option[모든 프로토콜에 정확히 일곱 개의 헤더가 있음을 보장합니다.]{#osi-seven-headers explanation="구현은 유선상의 일곱 헤더와 일대일로 대응하지 않습니다."}
::option[모든 패킷 캡처를 다이어그램으로 대체합니다.]{#osi-replace-captures explanation="모델은 조사를 안내하지만 증거를 대신하지 않습니다."}
::option[네트워크 기능을 분류하는 공통 방식을 제공합니다.]{#osi-shared-vocabulary .correct explanation="프레임워크는 팀이 논의하는 기능 영역을 좁히는 데 도움이 됩니다."}
:::

## OSI와 TCP/IP 비교하기

인터넷 프로토콜 모음과 OSI 참조 모델은 서로 다른 표준화 역사를 거쳐 발전했습니다. 실용적인 TCP/IP 모델은 흔히 OSI의 세션 및 표현 책임을 응용 계층에 묶고, 물리 및 데이터 링크 영역을 링크 또는 네트워크 접근 계층에 결합합니다. 매핑은 대략적인 비교일 뿐, 한 스택이 다른 스택에서 직접 구현됐다는 증거가 아닙니다.

:::single-choice{#osi-tcpip-mapping}
OSI와 TCP/IP 계층 간 매핑은 어떻게 해석해야 합니까?

::option[모든 프로토콜이 따라야 하는 정확한 규칙입니다.]{#osi-exact-rule explanation="프로토콜의 책임은 개념적 경계를 가로지르는 경우가 많습니다."}
::option[TCP/IP가 유선상에서 필수 7계층을 사용한다는 증거입니다.]{#osi-tcp-seven explanation="TCP/IP는 흔히 4개 또는 5개 계층으로 설명됩니다."}
::option[기능 모델 사이의 대략적인 비교입니다.]{#osi-approximate-map .correct explanation="두 모델은 일부 책임을 서로 다르게 묶습니다."}
:::

## 계층을 가로질러 문제 해결하기

계층을 숫자 순서대로 기계적으로 확인하지 말고 증상에서 시작해 가정을 테스트합니다. 웹 장애에는 로컬 링크 상태, IP 라우팅, 전송 연결, TLS, 이름 확인, 인증 또는 애플리케이션 동작이 관련될 수 있습니다. 한 계층의 증거는 다음 테스트를 안내할 수 있지만 상위 계층의 작동을 입증하지는 않습니다.

:::single-choice{#osi-link-success-limit}
정상적으로 작동하는 로컬 Ethernet 링크가 입증하는 것은 무엇입니까?

::option[모든 원격 HTTP 서비스가 정상이라는 사실입니다.]{#osi-link-proves-http explanation="로컬 링크 상태는 원격 애플리케이션 상태를 입증할 수 없습니다."}
::option[DNS에 잘못된 레코드가 없다는 사실입니다.]{#osi-link-proves-dns explanation="이름 데이터는 기본 링크 연결과 독립적입니다."}
::option[관련된 로컬 링크 조건이 작동한다는 사실만 입증합니다.]{#osi-link-limited-proof .correct explanation="라우팅, 전송, 이름 지정, 보안 및 애플리케이션 장애는 여전히 남아 있을 수 있습니다."}
:::

## 요약

이제 OSI 모델을 계층화된 진단 어휘로 사용할 수 있습니다.

1. 일곱 계층의 이름을 순서대로 말합니다.
2. 각 계층을 대략적인 책임과 연결합니다.
3. TCP/IP와의 매핑을 대략적인 것으로 다룹니다.
4. 계층별 증거로 종단 간 테스트를 대신하지 말고 다음 조사를 안내합니다.
