---
index: 3
lang: "ko"
title: "traceroute"
meta_title: "traceroute - 네트워크 문제 해결"
meta_description: "traceroute 리눅스 명령어를 마스터하여 네트워크 경로를 추적하고 연결 문제를 해결하세요. 이 튜토리얼은 traceroute 가 TTL 을 사용하여 패킷이 목적지까지 이동하는 경로를 매핑하는 방법을 설명합니다."
meta_keywords: "traceroute, traceroute 리눅스, 리눅스 네트워킹, 네트워크 문제 해결, TTL, 패킷 라우팅, 리눅스 명령어, 초보자, 튜토리얼"
---

## Lesson Content

traceroute`명령어는 패킷이 사용자의 컴퓨터에서 대상 호스트까지 이동하는 경로를 추적하는 데 사용되는 기본적인 네트워크 진단 도구입니다. 경로상의 각 "홉" 또는 라우터를 보여줌으로써 네트워크 병목 현상을 식별하고 연결 문제를 해결하는 데 도움이 됩니다.`traceroute linux` 유틸리티는 모든 시스템 관리자나 네트워크 엔지니어에게 필수적입니다.

### traceroute 작동 방식

traceroute 의 메커니즘은 IP 패킷 헤더의 TTL(Time To Live) 필드를 영리하게 조작하는 데 있습니다. 프로세스는 다음과 같이 작동합니다:

1. `traceroute`는 TTL 값이 1 인 프로브 패킷을 보냅니다.
2. 경로상의 첫 번째 라우터가 패킷을 수신하고 TTL 을 0 으로 감소시킨 후 폐기합니다. 그런 다음 라우터는 사용자 컴퓨터로 ICMP "Time Exceeded" 메시지를 다시 보냅니다.
3. `traceroute`는 해당 라우터의 IP 주소와 왕복 시간 (round-trip time) 을 기록합니다.
4. 그런 다음 TTL 을 2 로 설정하여 또 다른 패킷을 보냅니다. 이 패킷은 첫 번째 라우터는 성공적으로 통과하지만 두 번째 라우터에서 폐기되며, 두 번째 라우터 역시 "Time Exceeded" 메시지를 다시 보냅니다.
5. 이 프로세스는 이후 패킷 세트마다 TTL 을 1 씩 증가시키면서 반복됩니다. "Time Exceeded" 메시지를 반환하는 라우터 목록을 구축함으로써, `traceroute`는 전체 경로를 매핑합니다.
6. 패킷이 최종적으로 대상에 도달하면 (대상은 ICMP "Echo Reply" 메시지로 응답함) 프로세스가 완료됩니다.

### traceroute 출력 이해하기

Linux 터미널에서 `traceroute`를 실행했을 때의 샘플 출력을 살펴보겠습니다.

```bash
$ traceroute google.com
traceroute to google.com (216.58.216.174), 30 hops max, 60 byte packets
 1  192.168.4.254 (192.168.4.254)  0.028 ms  0.009 ms  0.008 ms
 2  100.64.1.113 (100.64.1.113)  1.227 ms  1.226 ms 0.920 ms
 3  100.64.0.20 (100.64.0.20)  1.501 ms 1.556 ms  0.855 ms
```

각 번호가 매겨진 줄은 네트워크 경로를 따라 있는 홉을 나타냅니다. 정보 해석 방법은 다음과 같습니다.

- **홉 번호:** 첫 번째 열 (예: `1`, `2`, `3`) 은 경로상의 라우터 순서를 나타냅니다.
- **라우터 이름 및 IP 주소:** 다음 부분은 해당 홉에 있는 라우터의 호스트 이름 (해결 가능한 경우) 과 IP 주소를 보여줍니다.
- **왕복 시간 (RTT):** 마지막 세 열은 해당 특정 홉으로 전송된 세 개의 프로브 패킷 각각에 대한 왕복 시간을 보여줍니다. 밀리초 (ms) 단위로 측정된 이 시간은 여정의 각 단계에서 지연 시간을 측정하는 데 도움이 됩니다.

`traceroute linux` 명령어를 효과적으로 사용하면 네트워크 성능과 구조에 대한 매우 귀중한 통찰력을 얻을 수 있습니다.

## Exercise

네트워크 진단을 마스터하는 데는 연습이 핵심입니다. 다음 실습 랩은 `traceroute`와 같은 도구를 사용하여 네트워크 경로 검색 및 문제 해결에 대한 이해를 강화하는 데 도움이 될 것입니다.

1. **[Linux 에서 IP 주소 지정 관리](https://labex.io/ko/labs/comptia-manage-ip-addressing-in-linux-592736)** - `ip` 명령어를 사용하여 네트워크 설정을 구성한 다음 `traceroute`로 연결 및 라우팅 경로를 확인하는 연습을 합니다.
2. **[Linux 에서 ping 및 arp 를 사용한 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping`과 `arp`가 함께 작동하여 네트워크 계층 상호 작용을 이해하는 방법을 학습합니다. 이는 `traceroute` 작동 방식의 기본 개념입니다.

이러한 랩은 실제 시나리오에서 네트워크 진단 개념을 적용하고 필수적인 Linux 네트워킹 도구에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

네트워크를 가로지르는 홉을 이동할 때 1 씩 감소하는 것은 무엇입니까? (대소문자를 구분하여 영어로 답하십시오.)

## Quiz Answer

TTL
