---
title: "ping"
description: "Linux ping 명령을 사용하여 네트워크 연결을 테스트하고 문제를 해결하는 방법을 배웁니다. 효과적인 네트워크 진단을 위해 ICMP, TTL 및 왕복 시간을 이해합니다."
keywords: "Linux ping, 네트워크 연결, ICMP, TTL, Linux 네트워킹, 초보자 Linux, Linux 튜토리얼, ping 명령"
---

## Lesson Content

가장 간단한 네트워킹 도구 중 하나인 **ping**은 패킷이 호스트에 도달할 수 있는지 테스트하는 데 사용됩니다. 이 도구는 ICMP 에코 요청 (Type 8) 패킷을 대상 호스트로 보내고 ICMP 에코 응답 (Type 0) 을 기다리는 방식으로 작동합니다. ping 은 호스트가 요청 패킷을 보내고 대상으로부터 응답을 받으면 성공합니다. 다음 예시를 살펴보겠습니다:

```plaintext
pete@icebox:~$ ping -c 3 www.google.com
PING www.google.com (74.125.239.112) 56(84) bytes of data.
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=1 ttl=128 time=29.0 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=2 ttl=128 time=23.7 ms
64 bytes from nuq05s01-in-f16.1e100.net (74.125.239.112): icmp_seq=3 ttl=128 time=15.1 ms
```

이 예시에서는 ping 을 사용하여 <www.google.com>에 도달할 수 있는지 확인합니다. `-c` 플래그 (count) 는 지정된 횟수에 도달하면 에코 요청 패킷 전송을 중지하는 데 사용됩니다.

첫 번째 부분은 64 바이트 패킷을 74.125.239.112(google.com) 로 보내고 있음을 나타내며, 나머지는 전송에 대한 세부 정보를 보여줍니다. 기본적으로 초당 하나의 패킷을 보냅니다.

### icmp_seq

`icmp_seq` 필드는 전송된 패킷의 시퀀스 번호를 보여주는 데 사용됩니다. 이 경우 3 개의 패킷을 보냈고, 3 개의 패킷이 모두 돌아온 것을 확인할 수 있습니다. ping 을 수행했을 때 일부 시퀀스 번호가 누락되었다면, 연결 문제가 발생하여 모든 패킷이 전송되지 못하고 있음을 의미합니다. 시퀀스 번호가 순서가 맞지 않는다면, 패킷이 기본 1 초를 초과하고 있으므로 연결이 매우 느릴 가능성이 있습니다.

### ttl

Time To Live (TTL) 필드는 홉 카운터로 사용됩니다. 홉을 할 때마다 카운터가 1 씩 감소하며, 홉 카운터가 0 에 도달하면 패킷은 소멸됩니다. 이는 패킷에 수명을 부여하기 위한 것으로, 패킷이 영원히 돌아다니는 것을 원치 않습니다.

### time

에코 요청 패킷을 보낸 시점부터 에코 응답을 받은 시점까지 걸린 왕복 시간입니다.

## Exercise

웹사이트에 ping 을 수행하고 수신되는 출력을 살펴보세요.

## Quiz Question

왕복 시간 측정 단위는 무엇입니까?

## Quiz Answer

ms
