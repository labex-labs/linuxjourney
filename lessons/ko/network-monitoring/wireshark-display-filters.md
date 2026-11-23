---
lesson_id: "wireshark-display-filters"
course_id: "network-monitoring"
lang: "ko"
order_index: 4
title: "Wireshark 표시 필터"
description: "Wireshark의 표시 필터를 사용해 준비된 캡처에서 원하는 패킷만 보는 방법을 알아봅니다."
meta_title: "Wireshark 표시 필터 - 네트워크 모니터링"
meta_description: "Wireshark의 표시 필터를 사용해 준비된 캡처에서 원하는 패킷만 보는 방법을 알아봅니다."
meta_keywords: "Wireshark 표시 필터, 네트워크 모니터링, 사이버 보안, Linux Journey"
---

패킷 캡처에는 여러 프로토콜의 패킷이 들어갈 수 있습니다. **표시 필터**는 저장된 패킷 중 어떤 패킷을 Wireshark에 표시할지 지정합니다. 화면에 보이는 결과만 바뀌고 캡처 파일은 그대로 유지됩니다.

## 프로토콜 선택하기

GitHub에서 [예시 캡처](https://github.com/labex-labs/linuxjourney/blob/master/examples/network-monitoring/sample.pcap) 페이지를 열고 파일을 `sample.pcap`으로 저장하세요. Wireshark에서 파일을 열고 표시 필터 입력란에 `dns`를 입력합니다. TShark가 설치된 Linux 터미널에서는 아래 명령으로 저장된 파일에 같은 필터를 적용할 수 있습니다. 이 파일에는 실습용 이름 조회와 별도의 예시 트래픽이 들어 있습니다.

```bash
$ tshark -r sample.pcap -Y dns
```

`-r` 옵션은 파일을 읽고 `-Y`는 표시 필터를 적용합니다. 질의와 그에 해당하는 응답을 찾아보세요.

:::single-choice{#wireshark-display-filters-display-effect} 필터를 적용하니 원래 화면보다 두 행이 줄었습니다. 나머지 패킷은 어떻게 되었나요?

::option[캡처 파일에서 삭제되었습니다.]{#wireshark-display-filters-display-effect-a explanation="표시 필터는 화면에 보이는 결과를 바꿉니다."}
::option[파일에 그대로 있고 이 필터의 조건과 일치하지 않았습니다.]{#wireshark-display-filters-display-effect-b .correct explanation="필터를 지우면 다시 전체 화면을 볼 수 있습니다."}
::option[네트워크로 다시 전송되었습니다.]{#wireshark-display-filters-display-effect-c explanation="저장된 캡처를 읽을 때는 패킷이 전송되지 않습니다."}
:::

## 주소와 일치하는 패킷 찾기

필터에서 패킷의 필드를 지정할 수도 있습니다. `ip.addr`는 출발지나 목적지의 IPv4 주소와 일치하는지 확인합니다. 등호 두 개로 필드 값을 예시 값과 비교합니다.

```bash
$ tshark -r sample.pcap -Y 'ip.addr == 192.0.2.10'
```

셸에서 따옴표로 묶으면 식 전체가 인수 하나로 전달됩니다. 출력된 각 행에서 통신의 양쪽 엔드포인트를 확인할 수 있습니다.

:::single-choice{#wireshark-display-filters-address-scope} 패킷이 다른 주소에서 192.0.2.10으로 향합니다. 필터와 일치하나요?

::option[예. 양쪽 엔드포인트 중 어느 쪽이든 조건과 일치하면 됩니다.]{#wireshark-display-filters-address-scope-a .correct explanation="ip.addr는 출발지 또는 목적지 주소를 확인할 수 있습니다."}
::option[아니요. 조건은 출발지만 확인합니다.]{#wireshark-display-filters-address-scope-b explanation="이 필드는 양방향에서 일치하는 주소를 찾을 수 있습니다."}
::option[패킷에 DNS가 포함된 경우에만 일치합니다.]{#wireshark-display-filters-address-scope-c explanation="이 식에서는 IPv4 주소만 확인합니다."}
:::

![실습 캡처에서 DNS만 표시한 결과와 두 프로토콜을 모두 표시한 결과를 비교하는 TShark 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/network-monitoring/wireshark-display-filters/saved-dns-exchange.png)

## 빈 결과 설명하기

결과가 비어 있으면 확인한 파일에 필터 조건과 일치하는 패킷이 없었다는 뜻입니다. 더 넓은 범위의 결론을 내리기 전에 필터 식, 시간, 캡처 지점을 확인하세요. 먼저 필터를 지우고 캡처에 트래픽이 들어 있는지 확인합니다.

:::single-choice{#wireshark-display-filters-empty-capture-view} 저장된 캡처에 dns를 적용했는데 행이 하나도 나오지 않습니다. 무엇을 보고할 수 있나요?

::option[네트워크의 어느 곳에서도 DNS를 사용하지 않았습니다.]{#wireshark-display-filters-empty-capture-view-a explanation="캡처 파일은 제한된 지점과 시간대를 담습니다."}
::option[Wireshark에서 DNS 증거를 삭제했습니다.]{#wireshark-display-filters-empty-capture-view-b explanation="표시 필터는 저장된 패킷을 삭제하지 않습니다."}
::option[이 필터를 적용했을 때 이 캡처에서 DNS 패킷이 표시되지 않았습니다.]{#wireshark-display-filters-empty-capture-view-c .correct explanation="검토한 증거의 범위 안에서 결과를 설명했습니다."}
:::

브라우저 실습에서 다른 캡처를 살펴보려면 [초보자를 위한 Wireshark](https://labex.io/courses/quick-start-with-wireshark)의 표시 필터 연습을 해 보세요.

## 요약

이제 저장된 패킷 캡처를 필터링하고 결과의 범위를 설명할 수 있습니다.

1. 표시 필터로 프로토콜을 선택합니다.
2. ip.addr로 패킷의 주소가 일치하는지 확인합니다.
3. 파일에서 관찰할 수 있는 범위를 고려해 필터 결과를 해석합니다.
