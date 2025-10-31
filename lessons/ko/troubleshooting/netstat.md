---
index: 4
lang: "ko"
title: "netstat"
meta_title: "netstat - 문제 해결"
meta_description: "리눅스 netstat 명령어를 마스터하여 네트워크 연결, 포트 및 소켓을 분석합니다. 이 가이드는 SYN_SENT 및 netstat close_wait 와 같은 일반적인 상태를 다루어 효과적인 문제 해결을 돕습니다."
meta_keywords: "리눅스 netstat, netstat, netstat 명령어, syn_sent netstat, netstat close_wait, 네트워크 연결, 리눅스 네트워킹, 네트워크 분석, 리눅스 튜토리얼"
---

## Lesson Content

### 잘 알려진 포트 (Well-Known Ports)

데이터가 우리 컴퓨터의 포트를 통해 어떻게 전송되는지 살펴보았습니다. 이제 일반적이고 잘 알려진 포트들을 살펴보겠습니다. 이러한 포트 목록은 **/etc/services** 파일에서 찾을 수 있습니다.

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

첫 번째 열은 서비스 이름, 그 뒤에 할당된 포트 번호 및 사용되는 전송 계층 프로토콜을 보여줍니다.

### linux netstat 소개

상세한 네트워크 정보를 수집하는 데 매우 유용한 도구는 **netstat**입니다. `linux netstat` 명령어는 활성 네트워크 연결, 라우팅 테이블 및 인터페이스 통계를 포함하여 광범위한 네트워크 관련 데이터를 표시합니다. 종종 네트워킹 도구의 스위스 군용 칼이라고 불립니다.

이 레슨에서는 `netstat`을 사용하여 네트워크 연결 상태를 확인하는 데 중점을 둘 것입니다. 예제로 넘어가기 전에 소켓과 포트의 차이점을 명확히 해보겠습니다. **포트**는 데이터를 특정 애플리케이션으로 전달하는 데 사용되는 숫자 식별자입니다. **소켓**은 통신의 종단점으로, 프로그램이 데이터를 송수신할 수 있게 해줍니다. 소켓 주소는 IP 주소와 포트 번호의 고유한 조합입니다. 호스트와 대상 간의 모든 연결에는 고유한 소켓이 필요합니다. 예를 들어, HTTP 서비스는 포트 80 에서 실행되지만, 여러 HTTP 연결이 동시에 존재할 수 있으며, 각각에 대해 고유한 소켓이 생성됩니다.

`netstat -at`의 출력을 살펴보겠습니다.

```bash
pete@icebox:~$ netstat -at
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 icebox:domain           *:*                     LISTEN
tcp        0      0 localhost:ipp           *:*                     LISTEN
tcp        0      0 icebox.lan:44468        124.28.28.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34751        124.28.29.50:http       TIME_WAIT
tcp        0      0 icebox.lan:34604        economy.canonical.:http TIME_WAIT
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN
tcp6       1      0 ip6-localhost:35094     ip6-localhost:ipp       CLOSE_WAIT
tcp6       0      0 ip6-localhost:ipp       ip6-localhost:35094     FIN_WAIT2
```

`netstat -a` 명령어는 수신 대기 중인 소켓과 수신 대기 중이 아닌 소켓을 모두 표시하며, `-t` 플래그는 출력을 TCP 연결만 표시하도록 필터링합니다.

열은 다음과 같습니다.

- **Proto**: 사용된 프로토콜 (예: TCP 또는 UDP).
- **Recv-Q**: 수신 대기 중인 데이터 큐.
- **Send-Q**: 전송 대기 중인 데이터 큐.
- **Local Address**: 로컬 호스트의 주소.
- **Foreign Address**: 원격 호스트의 주소.
- **State**: 소켓의 현재 상태.

### 연결 상태 이해하기

**State** 열은 연결 상태에 대한 중요한 정보를 제공합니다. 일반적으로 접하게 되는 몇 가지 일반적인 상태는 다음과 같습니다.

- **LISTENING**: 소켓이 들어오는 연결을 기다리고 있습니다. TCP 연결이 이루어지려면 대상이 수신 대기 중이어야 합니다.
- **SYN_SENT**: `netstat`을 사용할 때 `SYN_SENT` 상태는 소켓이 적극적으로 연결을 설정하려고 시도하고 있음을 나타냅니다.
- **ESTABLISHED**: 소켓이 완전히 설정된 연결을 가지고 있습니다.
- **CLOSE_WAIT**: `netstat close_wait` 상태는 원격 호스트가 종료되었으며 로컬 시스템이 애플리케이션이 소켓을 닫기를 기다리고 있음을 의미합니다.
- **TIME_WAIT**: 소켓은 네트워크에 남아 있을 수 있는 패킷을 처리하기 위해 닫은 후 대기 중입니다.

You can see a full list of socket states in the `netstat` man page.

### 연결 상태 이해하기

**State** 열은 연결 상태에 대한 중요한 정보를 제공합니다. 일반적으로 접하게 되는 몇 가지 일반적인 상태는 다음과 같습니다.

- **LISTENING**: 소켓이 들어오는 연결을 기다리고 있습니다. TCP 연결이 이루어지려면 대상이 수신 대기 중이어야 합니다.
- **SYN_SENT**: `netstat`을 사용할 때 `SYN_SENT` 상태는 소켓이 적극적으로 연결을 설정하려고 시도하고 있음을 나타냅니다.
- **ESTABLISHED**: 소켓이 완전히 설정된 연결을 가지고 있습니다.
- **CLOSE_WAIT**: `netstat close_wait` 상태는 원격 호스트가 종료되었으며 로컬 시스템이 애플리케이션이 소켓을 닫기를 기다리고 있음을 의미합니다.
- **TIME_WAIT**: 소켓은 네트워크에 남아 있을 수 있는 패킷을 처리하기 위해 닫은 후 대기 중입니다.

`netstat` man 페이지에서 소켓 상태의 전체 목록을 볼 수 있습니다.

## Exercise

연습이 완벽함을 만듭니다! 다음은 네트워크 인터페이스 설정에 대한 이해를 강화하기 위한 실습 랩입니다.

1. **[Linux 에서 ethtool 을 사용하여 네트워크 인터페이스 설정 검토하기](https://labex.io/ko/labs/comptia-examine-network-interface-settings-with-ethtool-in-linux-592759)** - `ethtool` 명령어를 사용하여 인터페이스 속도 및 이중 모드 보기 및 설정, 링크 모드 분석 등을 통해 물리적 계층 네트워크 문제를 해결하는 방법을 알아봅니다.

이 랩은 실제 시나리오에서 개념을 적용하고 네트워크 인터페이스 관리 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

HTTPS 에 사용되는 포트는 무엇입니까?

## Quiz Answer

443
