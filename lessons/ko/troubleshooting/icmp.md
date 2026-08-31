---
lesson_id: "icmp"
course_id: "troubleshooting"
lang: "ko"
order_index: 1
title: "ICMP"
description: "ICMP가 IP 오류를 보고하고 진단을 지원하며 필수 IPv4 및 IPv6 동작을 가능하게 하는 방법을 알아봅니다."
meta_title: "ICMP - 문제 해결"
meta_description: "리눅스 네트워킹의 ICMP 프로토콜을 알아봅니다. 효과적인 네트워크 문제 해결을 위한 ICMP 메시지 유형과 코드를 설명합니다."
meta_keywords: "ICMP, ICMP 프로토콜, 네트워크 문제 해결, ICMP 유형, 리눅스 네트워킹"
---

ICMP(Internet Control Message Protocol)는 IP와 함께 제어, 오류 및 진단 정보를 운반합니다. IPv4용 ICMP와 ICMPv6는 관련 있지만 메시지 유형 번호와 책임이 다른 별개의 프로토콜입니다.

## 유형, 코드 및 체크섬

ICMP 메시지에는 유형, 해당하는 경우 더 구체적인 코드 및 체크섬이 있습니다. 오류 메시지는 일반적으로 오류를 일으킨 패킷의 일부를 포함해 송신자가 오류를 흐름과 연결할 수 있게 합니다.

:::single-choice{#icmp-code-purpose}
ICMP 코드는 무엇을 제공합니까?

::option[보고 라우터의 영구 DNS 이름입니다.]{#icmp-code-dns explanation="이름 확인은 이 필드의 목적으로 인코딩되지 않습니다."}
::option[ICMP 메시지 유형 안에서 더 구체적인 의미를 제공합니다.]{#icmp-code-specific .correct explanation="예를 들어 목적지 도달 불가 코드는 여러 장애 원인을 구분합니다."}
::option[이전 모든 패킷의 전체 페이로드입니다.]{#icmp-code-all-payload explanation="오류는 프로토콜 규칙에 따라 식별에 충분한 호출 패킷 부분만 인용합니다."}
:::

## 에코 및 오류 메시지

ICMPv4에서 Echo Request는 유형 8, Echo Reply는 유형 0입니다. Destination Unreachable은 유형 3이고 Time Exceeded는 유형 11입니다. ICMPv6는 다른 유형 번호를 사용하므로 캡처를 해석하기 전에 항상 주소 계열을 식별하십시오.

:::single-choice{#icmpv4-echo-request-type}
ICMPv4 Echo Request 유형은 무엇입니까?

::option[0]{#icmp-type-zero explanation="유형 0은 ICMPv4 Echo Reply입니다."}
::option[11]{#icmp-type-eleven explanation="유형 11은 ICMPv4 Time Exceeded입니다."}
::option[8]{#icmp-type-eight .correct explanation="ping은 일반적으로 에코 응답을 요청하기 위해 이 ICMPv4 메시지를 보냅니다."}
:::

## Path MTU와 필수 ICMP

ICMP는 선택적인 ping 트래픽만이 아닙니다. IPv4 단편화 필요 오류와 ICMPv6 Packet Too Big 메시지가 Path MTU Discovery를 지원합니다. ICMPv6는 Neighbor Discovery와 Router Advertisement도 운반합니다. 따라서 모든 ICMP를 차단하면 블랙홀이 생기고 IPv6 작동이 망가질 수 있습니다.

무조건 차단한다고 가정하지 말고 필요한 유형, 방향, 속도 및 범위를 기준으로 필터링합니다. 공격자가 일부 ICMP를 위조할 수 있으므로 인용된 패킷 맥락을 검증하고 로컬 경로 및 캡처와 대조하십시오.

:::single-choice{#icmp-block-all-risk}
모든 ICMP를 차단하면 정상 트래픽이 망가질 수 있는 이유는 무엇입니까?

::option[모든 HTTP 응답이 ICMP Echo Reply 안에서 전송되기 때문입니다.]{#icmp-http-echo explanation="HTTP는 일반적으로 ICMP 에코가 아니라 TCP 또는 QUIC을 사용합니다."}
::option[ICMP가 모든 애플리케이션 암호를 저장하기 때문입니다.]{#icmp-passwords explanation="자격 증명 데이터베이스가 아닙니다."}
::option[ICMP가 필수 경로 MTU 및 IPv6 제어 정보를 운반하기 때문입니다.]{#icmp-essential-control .correct explanation="이 메시지를 억제하면 올바른 패킷 크기나 이웃 및 라우터 탐색을 막을 수 있습니다."}
:::

## 응답 없음을 해석하기

ICMP 응답이 없는 것은 필터링, 속도 제한, 비대칭 라우팅, 반환 경로 부재, 중단된 호스트 또는 단순히 그 메시지에 응답하지 않는 장치를 뜻할 수 있습니다. 반대로 ICMP 오류는 최종 목적지가 아니라 중간 장치가 생성할 수 있습니다.

:::single-choice{#icmp-silence-meaning}
Echo Reply가 없다는 사실만으로 무엇이 입증됩니까?

::option[대상 애플리케이션이 확실히 중지됐습니다.]{#icmp-silence-app-down explanation="에코 트래픽을 필터링하거나 무시해도 서비스가 작동할 수 있습니다."}
::option[목적지 호스트 이름이 DNS에서 삭제됐습니다.]{#icmp-silence-dns-deleted explanation="숫자 주소 프로브는 DNS와 독립적으로 응답이 없을 수 있습니다."}
::option[이 에코 교환에서 관찰된 응답이 없었다는 사실만 입증합니다.]{#icmp-silence-limited .correct explanation="원인을 식별하려면 추가 경로, 전송, 애플리케이션 및 캡처 증거가 필요합니다."}
:::

## 요약

이제 ICMP를 이분법적인 연결 판정이 아니라 제어 증거로 해석할 수 있습니다.

1. 올바른 IP 주소 계열에서 유형과 코드를 읽습니다.
2. 에코, 도달 불가 및 시간 초과의 역할을 구분합니다.
3. 경로 MTU와 IPv6 작동에 필요한 ICMP를 허용합니다.
4. 오류와 응답 없음을 다른 경로 증거와 연관 지어 분석합니다.
