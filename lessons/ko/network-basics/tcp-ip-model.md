---
lesson_id: "tcp-ip-model"
course_id: "network-basics"
lang: "ko"
order_index: 3
title: "TCP/IP 모델"
description: "TCP/IP 모델에서 응용, 전송, 인터넷 및 링크 계층이 협력하는 방법을 알아봅니다."
meta_title: "TCP/IP 모델 - 네트워크 기초"
meta_description: "현대 네트워킹의 토대인 TCP/IP 모델의 기본 계층을 살펴봅니다. 응용, 전송, 인터넷 및 링크 계층을 알아봅니다."
meta_keywords: "TCP/IP 모델, TCP IP 계층, TCP/IP 네트워킹, 네트워크 계층, TCP, IP, 리눅스 네트워킹"
---

TCP/IP 모델은 인터넷 호스트가 사용하는 프로토콜을 기능 계층으로 구성합니다. 일반적인 4계층 형식은 응용, 전송, 인터넷 및 링크 계층을 사용합니다. 일부 교육 모델은 물리 매체를 링크 계층에서 분리해 5개 계층으로 나타냅니다.

## 응용 계층

응용 프로토콜은 HTTP, DNS, SSH 및 SMTP 같은 서비스의 메시지와 동작을 정의합니다. 이 계층에는 OSI 모델이 별도로 다루는 표현 및 세션 책임도 많이 포함됩니다.

:::single-choice{#tcpip-http-layer} HTTP는 일반적으로 어느 TCP/IP 계층으로 분류됩니까?

::option[인터넷 계층입니다.]{#tcpip-http-internet explanation="인터넷 계층은 IP 주소 지정과 패킷 전달을 처리합니다."}
::option[링크 계층입니다.]{#tcpip-http-link explanation="링크 계층은 로컬 매체에서 트래픽을 운반합니다."}
::option[응용 계층입니다.]{#tcpip-http-application .correct explanation="HTTP는 애플리케이션 요청과 응답의 의미를 정의합니다."}
:::

## 전송 계층

전송 프로토콜은 애플리케이션 끝점 사이의 통신을 제공합니다. TCP는 혼잡 제어와 흐름 제어를 갖춘 신뢰할 수 있는 순서형 바이트 스트림을 제공합니다. UDP는 TCP의 연결, 순서 또는 재전송 보장 없이 독립적인 데이터그램을 제공합니다. 포트 번호는 전송 끝점을 식별하는 데 도움이 되지만 포트 번호만으로 어느 애플리케이션이 수신 중인지 입증할 수는 없습니다.

:::single-choice{#tcpip-udp-property} TCP가 아니라 UDP에 해당하는 특성은 무엇입니까?

::option[내장 재전송 보장이 없는 독립적인 데이터그램입니다.]{#tcpip-udp-datagrams .correct explanation="UDP를 사용하는 애플리케이션이 신뢰성을 추가할지와 그 방법을 결정합니다."}
::option[하나의 바이트 스트림을 순서대로 전달한다는 보장입니다.]{#tcpip-udp-ordered explanation="연결 성공을 전제로 하는 TCP 서비스의 특성입니다."}
::option[서로 다른 IP 네트워크 사이에서 패킷을 라우팅합니다.]{#tcpip-udp-routing explanation="네트워크 간 라우팅은 인터넷 계층 기능입니다."}
:::

## 인터넷 계층

인터넷 프로토콜은 출발지 및 목적지 IP 주소를 사용해 패킷을 운반합니다. 라우터는 라우팅 정보를 조사하고 홉 제한을 줄이면서 패킷을 목적지 방향으로 전달합니다. ICMP는 IP 작동을 위한 제어 및 오류 정보를 전달합니다. 전송은 최선형 서비스이며 필요한 복구는 상위 계층이나 애플리케이션이 처리합니다.

:::single-choice{#tcpip-router-layer} 라우터가 사용하는 IP 목적지를 제공하는 계층은 무엇입니까?

::option[인터넷 계층입니다.]{#tcpip-router-internet .correct explanation="IP 헤더에는 라우팅 전달에 사용하는 네트워크 계층 목적지가 들어 있습니다."}
::option[응용 계층입니다.]{#tcpip-router-application explanation="응용 메시지는 하위 계층 프로토콜 데이터 안에 운반됩니다."}
::option[링크 계층입니다.]{#tcpip-router-link explanation="링크 주소는 다음 로컬 홉의 프레임 목적지를 선택합니다."}
:::

## 링크 계층과 캡슐화

링크 계층은 Ethernet, Wi-Fi, 지점 간 프로토콜 또는 다른 기술을 사용해 하나의 로컬 링크에서 IP 패킷을 보냅니다. 응용 데이터가 아래로 이동할 때 각 계층은 자신의 범위에 필요한 정보를 추가합니다. 수신 측에서는 각 계층이 자체 캡슐화를 검증하고 제거한 뒤 데이터를 위로 전달합니다.

링크 헤더는 일반적으로 라우팅되는 각 홉에서 바뀝니다. 전송 및 응용 통신은 미들박스가 종료하거나 변환하지 않는 한 종단 간 유지됩니다.

:::single-choice{#tcpip-link-scope} 링크 계층 프레임의 일반적인 범위는 무엇입니까?

::option[하나의 로컬 링크 또는 홉입니다.]{#tcpip-one-link .correct explanation="라우터는 수신 프레이밍을 제거하고 다음 링크에 맞는 프레이밍을 만듭니다."}
::option[전역 인터넷의 모든 애플리케이션 세션입니다.]{#tcpip-global-frame explanation="프레임은 라우팅된 네트워크를 가로질러 변경 없이 유지되지 않습니다."}
::option[출발지 프로세스의 메모리만 해당합니다.]{#tcpip-process-memory explanation="프레임은 네트워크 링크를 통해 전송됩니다."}
:::

## 요약

이제 일반적인 인터넷 기능을 TCP/IP 모델에 배치할 수 있습니다.

1. 서비스 프로토콜을 응용 계층과 연결합니다.
2. TCP 스트림과 UDP 데이터그램을 구분합니다.
3. IP 주소 지정과 라우팅을 인터넷 계층에 배치합니다.
4. 링크 프레이밍을 로컬 홉 캡슐화로 다룹니다.
