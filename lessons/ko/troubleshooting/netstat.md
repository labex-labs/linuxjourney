---
lesson_id: "netstat"
course_id: "troubleshooting"
lang: "ko"
order_index: 4
title: "netstat"
description: "ss로 리눅스 소켓, 리스너, 큐 및 TCP 상태를 조사하는 방법을 알아봅니다."
meta_title: "netstat - 문제 해결"
meta_description: "리눅스 네트워크 연결, 포트 및 소켓을 분석하는 방법을 알아봅니다. ss 명령과 SYN-SENT, CLOSE-WAIT 같은 상태를 설명합니다."
meta_keywords: "리눅스 netstat, netstat, ss 명령, SYN-SENT, CLOSE-WAIT, 네트워크 연결, 리눅스 네트워킹"
---

기존 `netstat` 도구는 소켓, 경로 및 인터페이스 통계를 표시합니다. 현대 리눅스에서는 커널 소켓 상태를 효율적으로 보여 주고 iproute2와 함께 유지 관리되는 `ss`가 선호되는 소켓 조사 도구입니다.

## 수신 소켓 나열하기

수신 중인 TCP와 UDP 소켓을 숫자로 표시하고, 권한이 있으면 소유 프로세스도 포함합니다.

```bash
$ sudo ss -lntup
```

`-l`은 리스너를 선택하고, `-n`은 이름 조회를 피하고, `-t`와 `-u`는 TCP와 UDP를 선택하며, `-p`는 프로세스 데이터를 요청합니다. UDP는 비연결형이므로 연결되지 않은 바인드 소켓에 TCP 방식의 `LISTEN` 핸드셰이크가 없습니다.

:::single-choice{#netstat-ss-numeric}
소켓 문제 해결 중 `-n`을 사용하는 이유는 무엇입니까?

::option[새 네트워크 네임스페이스를 만듭니다.]{#netstat-new-namespace explanation="이 옵션은 출력의 이름 확인을 제어합니다."}
::option[주소 및 포트 이름 조회를 방지합니다.]{#netstat-numeric-output .correct explanation="숫자 출력은 서비스 이름 매핑을 관찰된 프로토콜 신원으로 혼동하는 일을 막습니다."}
::option[수신 중이 아닌 모든 소켓을 닫습니다.]{#netstat-close-sockets explanation="검사 작업은 소켓을 종료하지 않습니다."}
:::

## 포트, 끝점 및 서비스

로컬 소켓 끝점은 주소, 전송 프로토콜 및 포트로 구성됩니다. TCP 연결은 프로토콜과 출발지 및 목적지 주소와 포트로 구분됩니다. `/etc/services`는 관례적인 이름을 숫자에 매핑하지만 현재 어느 프로세스가 포트를 소유하거나 어떤 응용 프로토콜을 사용하는지 입증하지 않습니다.

:::single-choice{#netstat-services-file-limit}
`https 443/tcp` 같은 `/etc/services` 항목은 무엇을 확립합니까?

::option[정상적인 HTTPS 서버가 현재 수신 중입니다.]{#netstat-healthy-listener explanation="정적 이름 데이터베이스는 런타임 상태를 입증하지 않습니다."}
::option[해당 포트의 관례적인 서비스 이름 매핑입니다.]{#netstat-conventional-name .correct explanation="소켓 소유권과 실제 프로토콜 동작에는 런타임 조사 및 테스트가 필요합니다."}
::option[모든 포트 443 트래픽이 올바르게 암호화됩니다.]{#netstat-all-encrypted explanation="포트 번호는 TLS 동작을 검증할 수 없습니다."}
:::

## TCP 상태 읽기

일반적인 상태는 다음과 같습니다.

- `SYN-SENT`: 로컬 끝점이 연결 요청을 보내고 진행을 기다립니다.
- `ESTAB`: TCP 연결이 수립됐습니다.
- `CLOSE-WAIT`: 통신 상대가 송신 측을 닫았지만 로컬 애플리케이션이 소켓을 닫지 않았습니다.
- `TIME-WAIT`: 능동적으로 닫은 끝점이 지연 세그먼트가 만료되고 최종 교환을 안전하게 처리할 수 있도록 기다립니다.

`CLOSE-WAIT` 수가 많거나 계속 증가하면 흔히 로컬 애플리케이션 정리 동작을 가리킵니다. `TIME-WAIT`는 정상적인 프로토콜 상태이며 수량과 리소스 영향에 따라 운영상 문제인지 판단합니다.

:::single-choice{#netstat-close-wait-owner}
`CLOSE-WAIT`에서 어느 쪽이 아직 소켓을 닫아야 합니까?

::option[인터넷의 모든 라우터입니다.]{#netstat-all-routers-close explanation="라우터는 끝점 소켓을 소유하지 않습니다."}
::option[DNS 권위 서버입니다.]{#netstat-dns-close explanation="이름 서비스는 로컬 TCP 닫기 처리와 관계없습니다."}
::option[로컬 애플리케이션입니다.]{#netstat-local-close .correct explanation="TCP가 통신 상대의 FIN을 받았으며 로컬 프로세스가 자기 쪽을 닫기를 기다립니다."}
:::

## 큐 해석하기

`Recv-Q`와 `Send-Q`의 의미는 상태와 프로토콜에 따라 다릅니다. 수립된 TCP 소켓에서는 애플리케이션 수신 또는 전송 확인 응답을 기다리는 데이터를 나타낼 수 있습니다. 수신 소켓에서 큐 필드는 같은 방식의 응용 페이로드 바이트가 아니라 연결 백로그 상태를 설명합니다.

스냅샷 하나만으로 누수나 병목을 확립할 수 없습니다. 시간에 따라 표본을 수집하고 프로세스 동작, 애플리케이션 지연 시간, 재전송 및 리소스 제한과 연관 지으십시오.

:::single-choice{#netstat-queue-snapshot}
큰 소켓 큐 스냅샷 하나만으로 진단하기에 부족한 이유는 무엇입니까?

::option[리눅스는 소켓 큐에 데이터를 저장하지 않기 때문입니다.]{#netstat-no-queues explanation="커널 네트워킹은 송수신 큐에 의존합니다."}
::option[모든 큐 값이 파일시스템 권한이기 때문입니다.]{#netstat-queue-permission explanation="필드는 네트워킹 상태를 설명합니다."}
::option[큐의 영향에는 상태, 추세 및 작업 부하 맥락이 필요하기 때문입니다.]{#netstat-queue-context .correct explanation="일시적인 버스트는 지속적인 애플리케이션 또는 네트워크 병목과 다릅니다."}
:::

## 조사 범위 제한하기

문제의 프로토콜, 상태, 끝점 또는 프로세스로 출력을 제한합니다.

```bash
$ ss -tn state established
$ ss -ltn 'sport = :443'
```

리스너는 로컬 전송 준비 상태를 입증하지만 원격 연결 가능성이나 애플리케이션 상태는 입증하지 않습니다. 증상에 맞는 경로, 방화벽, 패킷, TLS 및 응용 테스트를 이어서 수행하십시오.

:::single-choice{#netstat-listener-limit}
포트 443의 TCP 리스너가 입증하지 못하는 것은 무엇입니까?

::option[로컬 소켓이 bind와 listen 작업을 받아들였습니다.]{#netstat-listen-local explanation="표시된 로컬 상태가 정확히 그 사실을 나타냅니다."}
::option[원격 클라이언트가 유효한 HTTPS 요청을 완료할 수 있습니다.]{#netstat-not-remote-proof .correct explanation="경로 정책, TLS 및 응용 동작은 테스트되지 않았습니다."}
::option[TCP에 숫자 포트 필드가 있습니다.]{#netstat-port-field explanation="리스너 출력에 직접 포함됩니다."}
:::

## 요약

이제 포트를 애플리케이션과 혼동하지 않고 `ss`로 소켓 상태를 조사할 수 있습니다.

1. 프로세스 맥락과 함께 리스너를 숫자로 나열합니다.
2. 관례적인 서비스 이름과 런타임 소유권을 구분합니다.
3. 로컬 끝점 관점에서 TCP 닫기 상태를 해석합니다.
4. 작업 부하 맥락과 함께 시간에 따라 큐를 표본 추출합니다.
5. 로컬 리스너를 넘어 원격 응용 동작을 검증합니다.
