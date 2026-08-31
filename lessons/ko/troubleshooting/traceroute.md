---
lesson_id: "traceroute"
course_id: "troubleshooting"
lang: "ko"
order_index: 3
title: "traceroute"
description: "traceroute가 응답하는 홉을 찾는 방법과 공백, 시간 및 경로 변화를 해석하는 방법을 알아봅니다."
meta_title: "traceroute - 문제 해결"
meta_description: "리눅스 traceroute 명령으로 네트워크 경로를 추적하고 연결 문제를 해결하는 방법을 알아봅니다. TTL로 패킷 경로를 찾는 방식을 설명합니다."
meta_keywords: "traceroute, 리눅스 traceroute, 리눅스 네트워킹, 네트워크 문제 해결, TTL, 패킷 라우팅"
---

`traceroute`는 점차 증가하는 IPv4 TTL 또는 IPv6 Hop Limit 값으로 프로브를 보냅니다. 값이 만료되는 라우터가 Time Exceeded 메시지를 반환하면 송신 경로에서 응답하는 일부 지점을 확인할 수 있습니다.

## 홉 탐색 작동 방식

프로브는 홉 제한 1에서 시작해 증가합니다. 첫 라우터가 1을 0으로 줄이고 ICMP 오류를 반환할 수 있습니다. 제한 2는 둘째 라우터에 도달한 뒤 만료되며 목적지가 응답하거나 최댓값에 도달할 때까지 과정이 계속됩니다.

:::single-choice{#traceroute-expiring-field}
연속된 프로브가 뒤쪽 라우터에서 만료되게 하는 필드는 무엇입니까?

::option[목적지 이름의 DNS 캐시 TTL입니다.]{#traceroute-dns-ttl explanation="DNS 레코드 수명은 패킷 전달 홉을 제어하지 않습니다."}
::option[Ethernet 출발지 MAC 주소입니다.]{#traceroute-source-mac explanation="링크 주소에는 종단 간 홉 카운터가 없습니다."}
::option[IPv4 TTL 또는 IPv6 Hop Limit입니다.]{#traceroute-hop-field .correct explanation="이 제한된 전달 횟수를 늘리면 응답하는 라우팅 홉을 확인할 수 있습니다."}
:::

## 프로브 방식

전통적인 리눅스 traceroute는 일반적으로 높은 목적지 포트에 UDP 프로브를 보냅니다. 목적지는 ICMP Port Unreachable로 완료를 알릴 수 있습니다. 옵션으로 ICMP Echo 또는 TCP SYN 프로브를 사용할 수 있으며 필터링 통과 방식이 다를 수 있습니다.

```bash
$ traceroute -n example.com
$ traceroute -I -n example.com
$ traceroute -T -p 443 -n example.com
```

필요한 권한과 지원 옵션은 다릅니다. 대상에 승인된 방식을 사용하고 결과를 비교할 때 사용한 방식을 기록하십시오.

:::single-choice{#traceroute-default-destination-response}
전통적인 리눅스 UDP traceroute를 일반적으로 끝내는 응답은 무엇입니까?

::option[목적지의 ICMP Port Unreachable 응답입니다.]{#traceroute-port-unreachable .correct explanation="높은 UDP 포트는 보통 사용되지 않으므로 목적지가 오류를 통해 자신을 식별할 수 있습니다."}
::option[모든 라우터의 필수 HTTP 200 응답입니다.]{#traceroute-http-every-router explanation="라우터는 HTTP 응답이 아니라 네트워크 제어 오류를 반환합니다."}
::option[인터넷 전체를 통과하는 목적지의 Ethernet 브로드캐스트입니다.]{#traceroute-ethernet-broadcast explanation="링크 브로드캐스트는 라우팅 경로를 통과하지 않습니다."}
:::

## 별표 해석하기

별표는 제한 시간 전에 해당 프로브의 응답이 관찰되지 않았다는 뜻입니다. 라우터는 전송 트래픽을 전달하면서 진단 응답을 필터링하거나 속도 제한할 수 있습니다. 이후 홉이 응답한다면 응답이 없던 홉도 적어도 일부 프로브를 전달한 것이 분명합니다.

:::single-choice{#traceroute-asterisk-meaning}
한 홉의 `*`는 무엇을 입증합니까?

::option[라우터가 모든 전송 패킷을 영구적으로 버렸습니다.]{#traceroute-star-all-drop explanation="이후 응답으로 계속 전달됐음을 확인할 수 있습니다."}
::option[프로브 제한 시간 전에 일치하는 응답이 도착하지 않았다는 사실만 입증합니다.]{#traceroute-star-no-response .correct explanation="필터링, 속도 제한, 손실 및 반환 경로 문제 모두 응답 없음을 만들 수 있습니다."}
::option[목적지에 IP 주소가 없습니다.]{#traceroute-star-no-address explanation="프로브가 이미 주소를 대상으로 하며 응답 없는 홉 하나가 주소를 지우지는 않습니다."}
:::

## 시간과 경로 변화

홉별 시간은 인접하게 출력된 줄 사이의 링크가 추가한 지연이 아니라 제어 응답까지의 왕복 시간을 측정합니다. 라우터가 제어 평면 응답의 우선순위를 낮출 수 있습니다. 부하 분산으로 프로브가 다른 경로를 통과할 수 있고 이름 확인이 표시 지연을 추가할 수 있으므로 `-n`으로 역방향 조회를 피합니다.

각 ICMP 응답의 반환 경로가 송신 경로와 다를 수 있습니다. 병목을 지목하기 전에 테스트를 반복하고 끝점 애플리케이션 시간과 연관 지으십시오.

:::single-choice{#traceroute-hop-rtt-limit}
인접 홉 RTT 값을 빼 정확한 링크 지연으로 보면 안 되는 이유는 무엇입니까?

::option[traceroute가 모든 시간을 밀리초가 아니라 바이트로 보고하기 때문입니다.]{#traceroute-times-bytes explanation="표시되는 프로브 시간은 일반적으로 밀리초입니다."}
::option[응답이 서로 다른 반환 경로와 제어 평면 처리를 사용할 수 있기 때문입니다.]{#traceroute-rtt-asymmetry .correct explanation="측정값은 동기화된 단방향 링크 표본이 아니라 각각의 종단-홉 왕복 시간입니다."}
::option[모든 라우터의 시계가 출발지와 같기 때문입니다.]{#traceroute-router-clock explanation="측정은 원격 시계 동기화에 의존하지 않습니다."}
:::

## 애플리케이션과 비교하기

traceroute가 목적지에 도달해도 서비스가 차단될 수 있고 중간 라우터가 응답을 숨겨도 서비스는 작동할 수 있습니다. 애플리케이션과 같은 주소 계열, 목적지, 전송 프로토콜 및 포트를 테스트한 뒤 traceroute를 보조 경로 증거로 사용하십시오.

:::single-choice{#traceroute-service-proof}
완료된 traceroute가 HTTPS 서비스의 정상 상태를 입증합니까?

::option[예. 모든 홉이 서버 인증서를 검증하기 때문입니다.]{#traceroute-validates-cert explanation="라우터는 클라이언트의 TLS 검증을 수행하지 않습니다."}
::option[아니요. 전송, TLS 및 HTTP 동작은 별도로 테스트해야 합니다.]{#traceroute-not-app-proof .correct explanation="경로 탐색과 애플리케이션 상태는 서로 다른 진단 계층입니다."}
::option[예. 단, 역방향 DNS 이름이 출력될 때만 그렇습니다.]{#traceroute-rdns-proof explanation="이름은 애플리케이션 기능을 확립하지 않습니다."}
:::

## 요약

이제 traceroute를 완전한 경로 판정기가 아니라 제한된 홉 프로브의 연속으로 해석할 수 있습니다.

1. TTL 또는 Hop Limit 만료를 통한 홉 탐색을 설명합니다.
2. UDP, ICMP 또는 TCP 중 어느 프로브를 사용했는지 기록합니다.
3. 별표를 입증된 장애가 아니라 응답 누락으로 다룹니다.
4. 인접 홉 RTT에서 정확한 링크 지연을 도출하지 않습니다.
5. 경로 증거를 실제 애플리케이션과 연관 지어 분석합니다.
