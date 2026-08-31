---
lesson_id: "application-layer"
course_id: "network-basics"
lang: "ko"
order_index: 5
title: "응용 계층"
description: "응용 프로토콜이 서비스 메시지, 상태, 이름 지정 및 보안 동작을 정의하는 방법을 알아봅니다."
meta_title: "응용 계층 - 네트워크 기초"
meta_description: "TCP/IP 모델의 최상위 계층인 응용 계층을 살펴봅니다. 응용 계층 프로토콜, SMTP 예시 및 네트워크 통신을 위한 데이터 준비를 알아봅니다."
meta_keywords: "응용 계층, 응용 계층 프로토콜, TCP/IP 모델, SMTP, 네트워크 프로토콜"
---

TCP/IP 응용 계층에는 애플리케이션이 네트워크 서비스를 요청하고 제공하는 데 사용하는 프로토콜이 포함됩니다. OSI 용어에서 응용, 표현 및 세션 계층으로 분리하는 많은 기능을 포괄합니다.

## 프로토콜 메시지와 의미

응용 프로토콜은 통신 상대가 메시지와 상태를 해석하는 방식을 정의합니다. HTTP는 요청, 응답, 메서드, 상태 코드 및 필드를 정의합니다. DNS는 쿼리와 리소스 레코드를 정의합니다. SMTP는 메일 전송을 위한 명령과 응답을 정의합니다.

모든 응용 프로토콜이 하나의 고정된 “응용 헤더”를 추가하는 것은 아닙니다. 텍스트 필드, 바이너리 레코드, 여러 중첩 형식 등을 사용할 수 있으며 하나의 전송 연결에서 연속적인 메시지 흐름을 운반하기도 합니다.

:::single-choice{#application-layer-protocol-role}
응용 프로토콜이 주로 정의하는 것은 무엇입니까?

::option[서비스 메시지의 의미와 교환 규칙입니다.]{#application-layer-message-semantics .correct explanation="통신 상대가 상호 운용하려면 구문, 의미 및 상태 동작을 공유해야 합니다."}
::option[모든 Ethernet 케이블의 전압입니다.]{#application-layer-voltage explanation="물리적 신호는 하위 계층 기술에 속합니다."}
::option[인터넷 라우터마다 독립적으로 선택하는 경로입니다.]{#application-layer-router-choice explanation="라우팅 결정은 네트워크 계층 동작입니다."}
:::

## 클라이언트, 서버 및 피어

클라이언트는 서비스에 요청하거나 연결을 시작하고, 서버는 수신 대기하거나 연결을 받아들입니다. 이는 영구적인 장치 분류가 아니라 상호작용 속 역할입니다. 하나의 호스트가 DNS에는 클라이언트이고 동시에 SSH에는 서버일 수 있으며, 일부 프로토콜은 피어 투 피어 역할을 사용합니다.

:::single-choice{#application-layer-client-role}
일반적인 요청-응답 교환에서 프로그램이 클라이언트가 되는 기준은 무엇입니까?

::option[서비스에 요청을 시작합니다.]{#application-layer-client-initiates .correct explanation="클라이언트와 서버는 하나의 호스트가 여러 서비스에서 동시에 수행할 수 있는 상호작용 역할입니다."}
::option[서버가 아니라 노트북에서 실행되어야 합니다.]{#application-layer-client-laptop explanation="하드웨어 분류는 프로토콜 역할을 결정하지 않습니다."}
::option[목적지 IP 접두사를 소유합니다.]{#application-layer-client-prefix explanation="네트워크 소유권은 응용 요청을 시작하는 일과 관계없습니다."}
:::

## 이름, 포트 및 서비스 선택

애플리케이션은 서비스 이름을 하나 이상의 IP 주소로 확인하고 전송 끝점을 선택할 수 있습니다. 잘 알려진 포트는 기본 관례이지 프로토콜을 변하지 않게 입증하는 증거가 아닙니다. HTTP는 흔히 TCP 포트 80, HTTPS는 TCP 포트 443을 사용하지만 둘 다 다른 곳에서 실행될 수 있습니다. SMTP는 릴레이와 메시지 제출에 서로 다른 포트와 정책을 사용합니다.

:::single-choice{#application-layer-port-limit}
열린 TCP 포트 443 하나만으로 무엇이 입증됩니까?

::option[프로세스가 그곳에서 TCP 끝점을 받아들였지만 응용 동작은 여전히 테스트해야 합니다.]{#application-layer-port-endpoint .correct explanation="프로토콜 교환과 TLS 검증이 더 강한 응용 계층 증거를 제공합니다."}
::option[서비스가 올바르게 설정된 HTTPS 애플리케이션임이 확실합니다.]{#application-layer-port-proves-https explanation="포트 번호는 프로토콜 동작, 신원 또는 상태를 검증하지 않습니다."}
::option[DNS가 IPv6 주소를 반환할 수 없습니다.]{#application-layer-port-dns explanation="전송 포트는 DNS 레코드 주소 계열을 제한하지 않습니다."}
:::

## 보안 및 종단 간 테스트

인증서 검증과 끝점 이름 지정이 올바르면 TLS는 기밀성, 무결성 및 인증된 통신 상대 신원을 추가할 수 있습니다. 모든 응용 작업을 자동으로 승인하지는 않습니다. 실제 클라이언트가 사용하는 것과 같은 이름, 주소 계열, 포트, 프로토콜, 자격 증명 및 요청을 테스트하십시오.

예를 들어 HTTPS 진단에서는 이름 확인, TCP 연결, TLS 인증서와 이름, HTTP 응답 및 응용 콘텐츠를 별도로 검사할 수 있습니다. 한 단계의 성공은 문제 범위를 좁히지만 이후 모든 단계의 성공을 입증하지 않습니다.

:::single-choice{#application-layer-tls-limit}
성공적인 TLS 인증서 검증이 확립하는 것은 무엇입니까?

::option[모든 사용자가 모든 리소스에 접근할 권한이 있습니다.]{#application-layer-tls-all-users explanation="전송 인증은 응용 접근 정책을 대신하지 않습니다."}
::option[검증된 이름에 대한 통신 상대 신원과 인증된 보안 채널입니다.]{#application-layer-tls-identity .correct explanation="응용 권한 부여와 콘텐츠 정확성은 별도로 검사해야 합니다."}
::option[라우터가 이후 패킷을 절대 버리지 않습니다.]{#application-layer-tls-routing explanation="TLS는 향후 네트워크 전송을 보장할 수 없습니다."}
:::

## 요약

이제 포트 번호나 프로그램 이름을 넘어 응용 계층 동작을 설명할 수 있습니다.

1. 프로토콜 구문, 의미 및 상태를 응용 계층 관심사로 식별합니다.
2. 클라이언트와 서버를 교환 속 역할로 다룹니다.
3. 포트를 프로토콜의 증거가 아니라 끝점 관례로 사용합니다.
4. 이름 지정, 보안 및 응용 응답을 종단 간 테스트합니다.
