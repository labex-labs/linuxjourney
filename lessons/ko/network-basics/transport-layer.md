---
lesson_id: "transport-layer"
course_id: "network-basics"
lang: "ko"
order_index: 6
title: "전송 계층"
description: "TCP와 UDP가 포트 및 서로 다른 전달 의미를 사용해 응용 끝점을 연결하는 방법을 알아봅니다."
meta_title: "전송 계층 - 네트워크 기초"
meta_description: "리눅스 네트워킹의 전송 계층을 살펴봅니다. TCP, UDP, 네트워크 포트, 데이터 분할 및 신뢰할 수 있는 전송을 위한 TCP 핸드셰이크를 설명합니다."
meta_keywords: "리눅스 전송 계층, TCP, UDP, TCP 핸드셰이크, 네트워크 포트, 데이터 분할, 리눅스 네트워킹"
---

전송 계층은 IP 네트워크를 가로질러 응용 끝점을 연결합니다. TCP와 UDP는 모두 16비트 포트 번호를 사용하지만 애플리케이션에 서로 다른 통신 모델과 보장을 제공합니다.

## 포트와 소켓

목적지 포트는 운영체제가 수신 소켓에 트래픽을 전달하는 데 도움이 됩니다. 연결이나 흐름은 포트 하나만으로 식별되지 않습니다. 프로토콜, 출발지와 목적지 주소, 출발지와 목적지 포트가 모두 중요합니다. 따라서 같은 서버 포트가 여러 클라이언트를 동시에 지원할 수 있습니다.

:::single-choice{#transport-layer-many-clients}
하나의 TCP 서버 포트가 여러 클라이언트를 동시에 처리할 수 있는 이유는 무엇입니까?

::option[각 연결에 끝점 주소와 포트의 고유한 조합이 있기 때문입니다.]{#transport-layer-connection-tuple .correct explanation="전체 전송 튜플은 하나의 수신 포트를 공유하는 동시 연결을 구분합니다."}
::option[서버가 패킷마다 포트 이름을 영구적으로 바꾸기 때문입니다.]{#transport-layer-renames-port explanation="수신 포트는 그대로 유지되며 받아들인 연결은 서로 다른 통신 상대 튜플을 가질 수 있습니다."}
::option[IP가 전달 전에 모든 출발지 주소를 제거하기 때문입니다.]{#transport-layer-removes-source explanation="출발지 주소는 통신 상대와 경로를 식별하는 요소입니다."}
:::

## TCP 바이트 스트림

TCP는 연결이 유지되는 동안 순서 있고 신뢰할 수 있는 바이트 스트림을 제공합니다. 순서 번호, 확인 응답, 재전송, 흐름 제어 및 혼잡 제어를 사용합니다. TCP는 응용 메시지 경계를 보존하지 않습니다. 한 번의 쓰기가 여러 번의 읽기로 도착하거나 여러 번의 쓰기가 한 번의 읽기로 반환될 수 있습니다. 애플리케이션이 자체 프레이밍을 정의합니다.

신뢰성이 절대적인 전달을 뜻하지는 않습니다. 연결은 시간 초과되거나 재설정되거나 실패할 수 있으며, 확인 응답이 애플리케이션의 영구적인 데이터 반영을 입증하지는 않습니다.

:::single-choice{#transport-layer-tcp-boundaries}
TCP에서 응용 메시지 경계에는 어떤 일이 일어납니까?

::option[TCP는 쓰기 경계를 보존하지 않는 순서형 바이트 스트림을 제공합니다.]{#transport-layer-byte-stream .correct explanation="응용 프로토콜이 메시지 구분이나 크기 표현 방식을 정의해야 합니다."}
::option[모든 쓰기가 정확히 하나의 IP 패킷과 한 번의 읽기가 됩니다.]{#transport-layer-one-write-packet explanation="분할, 버퍼링 및 수신 API는 이런 대응을 보존하지 않습니다."}
::option[TCP가 각 메시지를 DNS 레코드로 변환합니다.]{#transport-layer-tcp-dns explanation="DNS는 별도의 응용 프로토콜입니다."}
:::

## TCP 핸드셰이크

일반적인 TCP 연결은 3방향 핸드셰이크로 시작합니다.

1. 시작 측이 초기 순서 정보와 함께 `SYN`을 보냅니다.
2. 수신 측이 자체 순서 정보 및 확인 응답을 담은 `SYN-ACK`로 응답합니다.
3. 시작 측이 `ACK`를 반환합니다.

이 교환은 양쪽 끝점에 전송 상태를 수립합니다. 응용 서버를 인증하거나 요청한 응용 작업의 성공을 입증하지는 않습니다.

:::single-choice{#transport-layer-handshake-order}
일반적인 TCP 3방향 핸드셰이크 순서는 무엇입니까?

::option[SYN, SYN-ACK, ACK입니다.]{#transport-layer-syn-order .correct explanation="이 교환은 양방향의 초기 연결 상태를 동기화하고 확인합니다."}
::option[ACK, ACK, SYN입니다.]{#transport-layer-ack-ack-syn explanation="시작 측이 먼저 동기화를 요청합니다."}
::option[SYN, FIN, RST입니다.]{#transport-layer-syn-fin-rst explanation="FIN과 RST는 정상 핸드셰이크를 구성하는 대신 상태를 닫거나 중단합니다."}
:::

## UDP 데이터그램

UDP는 데이터그램 경계를 보존하고 체크섬 기반 오류 감지를 제공하지만 TCP와 같은 연결 상태, 순서, 재전송, 흐름 제어 또는 혼잡 제어는 제공하지 않습니다. 애플리케이션이 필요한 신뢰성이나 혼잡 동작을 직접 추가할 수 있습니다. UDP가 자동으로 더 빠른 것은 아니며 성능은 프로토콜 설계, 작업 부하, 경로 및 구현에 따라 달라집니다.

:::single-choice{#transport-layer-udp-boundaries}
UDP가 애플리케이션에 제공하는 특성은 무엇입니까?

::option[자동 재전송되는 순서형 바이트 스트림입니다.]{#transport-layer-udp-stream explanation="기본 UDP가 아니라 TCP와 같은 서비스를 설명합니다."}
::option[제출한 데이터그램 사이의 경계를 보존합니다.]{#transport-layer-udp-datagrams .correct explanation="유실되지 않는다면 수신된 UDP 데이터그램은 보낸 데이터그램 하나에 대응합니다."}
::option[고정된 기한 이전의 전달을 보장합니다.]{#transport-layer-udp-deadline explanation="UDP는 전달 기한을 보장하지 않습니다."}
:::

## 전송 끝점 조사하기

`ss`로 수신 및 연결된 소켓을 변경하지 않고 조사합니다.

```bash
$ ss -lntup
$ ss -tn state established
```

프로세스 세부 정보에는 권한이 필요할 수 있습니다. 수신 소켓은 전송 경계의 로컬 준비 상태만 입증합니다. 방화벽, 라우팅, 주소 계열, TLS 및 애플리케이션 상태는 적절한 테스트로 별도 확인해야 합니다.

:::single-choice{#transport-layer-listener-proof}
수신 중인 TCP 소켓이 확립하는 사실은 무엇입니까?

::option[모든 원격 방화벽이 연결을 허용합니다.]{#transport-layer-all-firewalls explanation="로컬 소켓 상태는 전체 경로의 정책을 보여 주지 않습니다."}
::option[애플리케이션이 모든 상태 검사를 통과했습니다.]{#transport-layer-all-health explanation="수신 상태는 성공한 응용 트랜잭션보다 약한 증거입니다."}
::option[로컬 프로세스가 일치하는 TCP 연결을 받아들일 준비가 됐습니다.]{#transport-layer-local-listener .correct explanation="원격 연결 가능성과 올바른 응용 응답은 별도의 문제입니다."}
:::

## 요약

이제 TCP 스트림 동작과 UDP 데이터그램 동작을 구분할 수 있습니다.

1. 프로토콜, 주소 및 포트로 흐름을 식별합니다.
2. TCP를 메시지 경계가 없는 신뢰할 수 있는 순서형 바이트 스트림으로 다룹니다.
3. TCP 핸드셰이크가 입증하는 것과 입증하지 않는 것을 구분합니다.
4. UDP 신뢰성과 혼잡 동작을 응용 설계 선택으로 다룹니다.
5. 로컬 소켓 상태를 넘어 애플리케이션 상태를 검증합니다.
