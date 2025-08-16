---
lang: "ko"
title: "netstat"
description: "Linux 네트워크 분석을 위한 netstat 명령을 배우세요. 이 초보자 친화적인 가이드를 통해 네트워크 연결, 포트 및 소켓을 이해하세요."
keywords: "netstat, netstat command, Linux networking, network connections, Linux tutorial, beginner, guide"
---

## Lesson Content

### Well-Known Ports

우리는 우리 장비의 포트를 통한 데이터 전송에 대해 논의했습니다. 이제 잘 알려진 포트들을 살펴보겠습니다.

잘 알려진 포트 목록은 **/etc/services** 파일을 보면 알 수 있습니다:

```plaintext
ftp             21/tcp
ssh             22/tcp
smtp            25/tcp
domain          53/tcp  # DNS
http            80/tcp
https           443/tcp
..etc..
```

첫 번째 열은 서비스의 이름이고, 그 다음은 포트 번호, 그리고 사용되는 전송 계층 프로토콜입니다.

### netstat

네트워크에 대한 자세한 정보를 얻는 데 매우 유용한 도구는 **netstat**입니다. Netstat 은 네트워크 연결, 라우팅 테이블, 네트워크 인터페이스 정보 등 다양한 네트워크 관련 정보를 표시합니다. 이는 네트워킹 도구의 스위스 군용 칼과 같습니다. 우리는 netstat 이 가진 한 가지 기능, 즉 네트워크 연결 상태에 주로 초점을 맞출 것입니다. 예제를 살펴보기 전에 먼저 소켓과 포트에 대해 이야기해 봅시다. 소켓은 프로그램이 데이터를 송수신할 수 있도록 하는 인터페이스이며, 포트는 어떤 애플리케이션이 데이터를 송수신해야 하는지 식별하는 데 사용됩니다. 소켓 주소는 IP 주소와 포트의 조합입니다. 호스트와 대상 간의 모든 연결에는 고유한 소켓이 필요합니다. 예를 들어, HTTP 는 포트 80 에서 실행되는 서비스입니다. 그러나 우리는 많은 HTTP 연결을 가질 수 있으며, 각 연결을 유지하기 위해 연결당 소켓이 생성됩니다.

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

`netstat -a` 명령은 네트워크 연결에 대한 수신 및 비수신 소켓을 보여주며, `-t` 플래그는 TCP 연결만 보여줍니다.

열은 왼쪽에서 오른쪽으로 다음과 같습니다:

- **Proto**: 사용된 프로토콜, TCP 또는 UDP.
- **Recv-Q**: 수신 대기 중인 데이터.
- **Send-Q**: 전송 대기 중인 데이터.
- **Local Address**: 로컬로 연결된 호스트.
- **Foreign Address**: 원격으로 연결된 호스트.
- **State**: 소켓의 상태.

소켓 상태 목록은 manpage 를 참조하십시오. 다음은 몇 가지 예입니다:

- **LISTENING**: 소켓이 들어오는 연결을 수신 대기 중입니다. TCP 연결을 만들 때, 우리가 연결하기 전에 대상이 우리를 수신 대기해야 한다는 것을 기억하십시오.
- **SYN_SENT**: 소켓이 연결을 적극적으로 설정하려고 시도 중입니다.
- **ESTABLISHED**: 소켓이 연결을 설정했습니다.
- **CLOSE_WAIT**: 원격 호스트가 종료되었으며, 소켓이 닫히기를 기다리고 있습니다.
- **TIME_WAIT**: 소켓이 닫힌 후 네트워크에 남아있는 패킷을 처리하기 위해 기다리고 있습니다.

## Exercise

`netstat`의 manpage 를 살펴보고 제공하는 모든 기능을 알아보십시오.

## Quiz Question

HTTPS 에 사용되는 포트는 무엇입니까?

## Quiz Answer

443
