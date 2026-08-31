---
lesson_id: "packet-analysis"
course_id: "troubleshooting"
lang: "ko"
order_index: 5
title: "패킷 분석"
description: "범위가 제한되고 필터링된 패킷 추적을 캡처하고 tcpdump로 안전하게 분석하는 방법을 알아봅니다."
meta_title: "패킷 분석 - 문제 해결"
meta_description: "리눅스 네트워크 패킷 분석의 기초를 알아봅니다. tcpdump로 네트워크 트래픽을 캡처하고 해석하는 방법을 설명합니다."
meta_keywords: "tcpdump, 패킷 분석, 네트워크 패킷 분석, 네트워크 분석, 리눅스 네트워킹, Wireshark, 네트워크 트래픽"
---

패킷 캡처는 선택한 관찰 지점에서 보이는 트래픽을 기록합니다. 프로토콜 교환과 시간을 보여 줄 수 있지만 자격 증명, 개인 데이터 및 관련 없는 사용자의 트래픽도 수집할 수 있습니다. 승인을 받고, 범위를 최소화하고, 파일을 보호하며 보존 정책을 따르십시오.

## 관찰 지점 선택하기

영향받는 흐름이 실제로 통과하는 인터페이스와 네트워크 네임스페이스에서 캡처합니다. 브리지, 컨테이너, VPN, 본드, VLAN 및 오프로딩으로 하나의 인터페이스에 보이는 내용이 달라질 수 있습니다. 캡처 전에 `ip route get`과 `ip link`로 후보를 찾으십시오.

:::single-choice{#packet-analysis-interface-choice}
캡처 인터페이스 선택이 중요한 이유는 무엇입니까?

::option[모든 인터페이스가 인터넷 전체를 자동으로 미러링하기 때문입니다.]{#packet-analysis-mirrors-internet explanation="호스트는 일반적으로 인터페이스를 통해 전달되거나 미러링된 트래픽만 봅니다."}
::option[해당 관찰 지점에 보이는 트래픽만 기록할 수 있기 때문입니다.]{#packet-analysis-visible-point .correct explanation="네임스페이스, 터널, 브리지 및 라우팅으로 관련 흐름이 다른 곳에 있을 수 있습니다."}
::option[인터페이스 이름이 TLS 페이로드를 복호화하기 때문입니다.]{#packet-analysis-name-decrypts explanation="이름에는 복호화 기능이 없습니다."}
:::

## 범위가 제한된 흐름 캡처하기

이름 확인 없이 호스트와 TCP 포트로 제한해 패킷을 최대 100개 캡처합니다.

```bash
$ sudo tcpdump -i enp1s0 -n -c 100 -w incident.pcap \
    'host 192.0.2.25 and tcp port 443'
```

`-i`는 인터페이스를 선택하고, `-n`은 숫자 이름을 유지하고, `-c`는 패킷 수를 제한하고, `-w`는 pcap 데이터를 기록하며, 마지막 표현식은 캡처 필터입니다. 트래픽이 없을 수 있다면 외부에서 시간 제한도 설정하십시오.

:::single-choice{#packet-analysis-count-bound}
`-c 100`은 무엇을 합니까?

::option[TCP 포트 100만 캡처합니다.]{#packet-analysis-port-hundred explanation="포트 선택은 필터 표현식에 속합니다."}
::option[파일을 100바이트로 압축합니다.]{#packet-analysis-compress-hundred explanation="파일 크기 제한이 아니라 패킷 수입니다."}
::option[패킷 100개를 캡처한 뒤 중지합니다.]{#packet-analysis-hundred .correct explanation="횟수 제한은 방치된 캡처가 패킷 수 기준으로 무한히 커지는 것을 막습니다."}
:::

## 캡처한 패킷 읽기

저장된 파일을 변경하지 않고 분석합니다.

```bash
$ tcpdump -n -tttt -r incident.pcap
```

프로토콜에 따라 타임스탬프, 프로토콜, 출발지, 목적지, 플래그, 순서 또는 확인 응답 데이터 및 길이를 읽습니다. 캡처 타임스탬프는 이 호스트에서 관찰한 시점을 나타내며 반드시 다른 곳의 정확한 전송 시점은 아닙니다. 여러 시스템의 캡처를 연관 지을 때 시계 동기화가 중요합니다.

:::single-choice{#packet-analysis-read-file}
저장된 pcap 파일에서 패킷을 읽는 옵션은 무엇입니까?

::option[`-r`]{#packet-analysis-option-read .correct explanation="읽기 옵션은 기존 캡처 파일을 처리합니다."}
::option[`-i`]{#packet-analysis-option-interface explanation="실시간 캡처 인터페이스를 선택합니다."}
::option[`-w`]{#packet-analysis-option-write explanation="원시 패킷을 파일에 씁니다."}
:::

## 부재와 암호화 해석하기

캡처된 패킷이 없다는 것은 잘못된 인터페이스나 네임스페이스, 캡처 손실, 지나치게 좁은 필터, 오프로딩 효과, 다른 곳으로의 라우팅 또는 실제 트래픽 부재를 뜻할 수 있습니다. tcpdump의 수신 및 드롭 카운터를 확인하고 알려진 이벤트를 재현합니다.

TLS와 다른 암호화는 일반적으로 응용 페이로드를 숨기지만 끝점, 시간, 크기, TCP 동작 및 핸드셰이크 일부 같은 유용한 메타데이터는 남깁니다. 승인 없이 복호화를 시도하거나 개인 키를 무심코 수집하지 마십시오.

:::single-choice{#packet-analysis-no-packets}
필터링된 빈 캡처가 입증하는 것은 무엇입니까?

::option[원격 애플리케이션이 영구적으로 삭제됐습니다.]{#packet-analysis-empty-deleted explanation="관찰 지점 및 필터 오류도 같은 결과를 만들 수 있습니다."}
::option[전체 네트워크에 트래픽이 전혀 없습니다.]{#packet-analysis-empty-network explanation="좁은 필터가 관련 없는 트래픽을 제외할 수 있습니다."}
::option[해당 캡처 지점에서 일치하는 패킷이 기록되지 않았다는 사실만 입증합니다.]{#packet-analysis-empty-limited .correct explanation="결론 전에 인터페이스, 네임스페이스, 필터, 캡처 드롭 및 테스트 생성을 검증합니다."}
:::

## 증거 보호 및 공유하기

pcap을 제한적인 권한으로 저장하고 명령, 호스트, 인터페이스, 시간대, 필터 및 사고 시간대를 기록하며 무결성이 중요하면 증거 해시를 계산합니다. 공유 전에 필요한 필드를 보존하는 도구와 절차로 데이터를 최소화하거나 비식별화합니다. 패킷 페이로드와 메타데이터도 사용자와 시스템을 식별할 수 있습니다.

:::single-choice{#packet-analysis-pcap-safety}
사고 pcap은 어떻게 다뤄야 합니까?

::option[접근을 제한하고 출처를 문서화한 민감한 증거로 다룹니다.]{#packet-analysis-sensitive-evidence .correct explanation="캡처에는 기밀 내용이 포함될 수 있으며 기밀성과 무결성 제어가 모두 필요합니다."}
::option[검토 없이 공개 업로드해도 되는 무해한 텍스트로 다룹니다.]{#packet-analysis-public explanation="바이너리 캡처가 페이로드, 신원 및 인프라를 노출할 수 있습니다."}
::option[원본을 보존하지 않고 바이트를 직접 편집합니다.]{#packet-analysis-edit-original explanation="출처를 훼손해 이후 분석을 무효화할 수 있습니다."}
:::

## 요약

이제 불필요하게 광범위하거나 위험하지 않은 유용한 패킷 캡처를 만들 수 있습니다.

1. 올바른 인터페이스와 네트워크 네임스페이스를 선택합니다.
2. 필터, 패킷 수 및 시간으로 캡처 범위를 제한합니다.
3. 원시 패킷을 저장하고 파일을 읽기 전용으로 분석합니다.
4. 패킷 부재와 암호화된 페이로드의 한계를 올바르게 다룹니다.
5. 캡처의 기밀성, 무결성 및 출처를 보호합니다.
