---
lesson_id: "ping"
course_id: "troubleshooting"
lang: "ko"
order_index: 2
title: "ping"
description: "범위가 제한된 ping 테스트를 실행하고 응답, 손실, RTT, TTL 및 한계를 해석하는 방법을 알아봅니다."
meta_title: "ping - 문제 해결"
meta_description: "리눅스 ping 명령으로 네트워크 연결을 테스트하는 방법을 알아봅니다. icmp_seq, TTL 및 왕복 시간을 포함한 출력을 설명합니다."
meta_keywords: "리눅스 ping, 네트워크 연결, ICMP, TTL, ping 명령, icmp_seq, 리눅스 네트워킹"
---

`ping`은 ICMP Echo Request를 보내고 관찰된 응답을 보고합니다. 하나의 주소로 향하는 제어 메시지 경로를 테스트하며 TCP, UDP, DNS, 인증 또는 애플리케이션이 작동함을 입증하지는 않습니다.

## 범위가 제한된 테스트 실행하기

일반적인 iputils 구현에서 패킷별 제한 시간을 2초로 두고 IPv4 요청 세 개를 보냅니다.

```bash
$ ping -4 -c 3 -W 2 example.com
```

IPv6를 선택하려면 `-6`을 사용합니다. 호스트 이름이 여러 주소를 반환하고 반복 실행에서 다른 주소를 선택할 수 있으므로 확인된 주소를 기록하십시오.

:::single-choice{#ping-count-option}
`-c 3`은 무엇을 요청합니까?

::option[정확히 3메가바이트인 패킷 페이로드입니다.]{#ping-three-megabytes explanation="패킷 크기에는 다른 옵션을 사용합니다."}
::option[목적지로 향하는 영구 경로 세 개입니다.]{#ping-three-routes explanation="ping은 트래픽을 프로브하며 경로를 설치하지 않습니다."}
::option[명령이 정상적으로 끝나기 전 Echo Request 세 개입니다.]{#ping-three-requests .correct explanation="유한한 횟수로 진단을 제한하고 반복 가능하게 만듭니다."}
:::

## 순서와 손실

`icmp_seq`는 실행 안에서 요청을 식별합니다. 응답 누락은 관찰된 손실에 포함되고 순서가 바뀐 응답은 변동하는 지연을 나타낼 수 있습니다. 작은 표본에는 잡음이 많으므로 범위가 제한된 여러 구간과 애플리케이션 자체 오류율을 비교합니다.

손실은 어느 방향에서나 발생할 수 있고 ICMP 속도 제한으로 ping 손실과 애플리케이션 손실이 다를 수 있습니다.

:::single-choice{#ping-sequence-gap}
`icmp_seq` 응답 누락은 무엇을 나타낼 수 있습니까?

::option[목적지가 MAC 주소를 영구적으로 바꿨습니다.]{#ping-sequence-mac explanation="순서 공백만으로 그런 링크 계층 결론을 내릴 수 없습니다."}
::option[요청 또는 응답이 유실, 필터링, 대기 시간 초과 또는 속도 제한됐을 수 있습니다.]{#ping-sequence-possibilities .correct explanation="순서 공백은 관찰된 응답이 없음을 식별하지만 정확한 방향이나 원인은 알 수 없습니다."}
::option[출발지 디스크에 여유 inode가 없습니다.]{#ping-sequence-inodes explanation="파일시스템 inode 상태는 ICMP 순서 응답과 관계없습니다."}
:::

## 왕복 시간

`time` 필드는 요청 전송부터 응답 수신까지의 왕복 시간을 밀리초로 나타냅니다. 송신 지연, 원격 처리 및 반환 지연을 합친 값입니다. 동기화된 끝점 측정 없이는 단방향 지연 시간을 알 수 없습니다.

:::single-choice{#ping-rtt-meaning}
`time=23.7 ms`는 무엇을 측정합니까?

::option[송신 방향의 단방향 경로 지연 시간만 측정합니다.]{#ping-outbound-only explanation="ping은 전체 요청 및 응답 구간을 측정합니다."}
::option[대상 시스템의 가동 시간입니다.]{#ping-target-uptime explanation="부팅 시간이 아니라 프로브 시간입니다."}
::option[해당 에코의 왕복 시간입니다.]{#ping-round-trip .correct explanation="양방향과 끝점 처리를 포함합니다."}
:::

## TTL 또는 Hop Limit

표시되는 IPv4 TTL 또는 IPv6 Hop Limit은 수신된 응답에 남아 있는 값입니다. 송신자의 초기 값과 반환 경로를 모르면 이를 빼서 정확한 홉 수를 구할 수 없습니다. 값 변경은 다른 응답자, 초기 값 또는 반환 경로를 나타낼 수 있습니다.

:::single-choice{#ping-received-ttl}
IPv4 Echo Reply에 표시되는 TTL은 무엇입니까?

::option[응답이 로컬 호스트에 도달했을 때 남은 값입니다.]{#ping-remaining-ttl .correct explanation="반환 경로의 각 라우터가 송신자의 초기 값을 줄였습니다."}
::option[양방향의 정확한 라우터 수입니다.]{#ping-exact-hop-count explanation="이 필드만으로 초기 TTL과 방향별 경로를 알 수 없습니다."}
::option[DNS 레코드의 캐시 수명입니다.]{#ping-dns-ttl explanation="DNS TTL과 IP 패킷 TTL은 서로 다른 필드입니다."}
:::

## 올바른 계층 테스트하기

ping은 성공하지만 서비스가 실패하면 실제 포트, TLS, 프로토콜 및 요청을 테스트합니다. ping이 실패하면 호스트가 중단됐다고 단정하기 전에 이름 확인, `ip route get`, 이웃 상태, 방화벽 정책 및 캡처를 조사합니다.

:::single-choice{#ping-success-limit}
성공한 ping이 입증하지 못하는 것은 무엇입니까?

::option[일부 ICMP 요청 및 응답 경로가 작동했습니다.]{#ping-icmp-worked explanation="응답이 직접 제공하는 증거입니다."}
::option[응답에 순서 번호가 있었습니다.]{#ping-sequence-present explanation="정상 출력에 응답 순서가 직접 보고됩니다."}
::option[의도한 애플리케이션이 요청을 받아 완료합니다.]{#ping-app-not-proven .correct explanation="응용 및 전송 동작에는 애플리케이션에 맞는 테스트가 필요합니다."}
:::

## 요약

이제 ping을 명시적인 한계가 있는 범위 제한 ICMP 측정으로 사용할 수 있습니다.

1. 주소 계열을 선택하고 확인된 주소를 기록합니다.
2. 반복 가능한 테스트를 위해 횟수와 대기 시간을 제한합니다.
3. 방향이나 원인을 단정하지 않고 손실을 해석합니다.
4. RTT를 양방향으로, TTL을 남은 값으로 취급합니다.
5. 실제 애플리케이션을 별도로 테스트합니다.
