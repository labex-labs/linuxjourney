---
index: 5
lang: "ko"
title: "패킷 분석"
meta_title: "패킷 분석 - 문제 해결"
meta_description: "tcpdump 를 사용하여 패킷 분석의 기본을 배웁니다. 이 초보자 친화적인 Linux 가이드를 통해 네트워크 트래픽을 이해하고, 데이터를 캡처하고, 출력을 해석하는 방법을 알아보세요."
meta_keywords: "tcpdump, 패킷 분석, 네트워크 분석, Linux 네트워킹, 초보자 튜토리얼, Wireshark, Linux 명령, 네트워크 트래픽"
---

## Lesson Content

패킷 분석은 그 자체로 전체 과정을 채울 수 있으며, 패킷 분석에 대해서만 쓰여진 책도 많습니다. 하지만 오늘은 기본적인 내용만 배우겠습니다. Wireshark 와 tcpdump 라는 두 가지 매우 인기 있는 패킷 분석기가 있습니다. 이 도구들은 네트워크 인터페이스를 스캔하고, 패킷 활동을 캡처하고, 패킷을 파싱하고, 정보를 출력하여 우리가 볼 수 있도록 합니다. 이를 통해 네트워크 분석의 세부 사항에 들어가고 낮은 수준의 내용을 탐구할 수 있습니다. 우리는 더 간단한 인터페이스를 가진 tcpdump 를 사용할 것이지만, 패킷 분석을 도구로 사용하려면 Wireshark 를 살펴보는 것을 추천합니다.

### tcpdump 설치

```bash
sudo apt install tcpdump
```

### 인터페이스에서 패킷 데이터 캡처

```plaintext
pete@icebox:~$ sudo tcpdump -i wlan0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on wlan0, link-type EN10MB (Ethernet), capture size 65535 bytes
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
11:28:24.960464 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 3, length 64
11:28:24.979299 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 3, length 64
11:28:25.961869 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 4, length 64
11:28:25.976176 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 4, length 64
11:28:26.963667 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 5, length 64
11:28:26.976137 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 5, length 64
11:28:30.674953 ARP, Request who-has 172.254.1.0 tell ThePickleParty.lan, length 28
11:28:31.190665 IP ThePickleParty.lan.51056 > 192.168.86.255.rfe: UDP, length 306
```

패킷 캡처를 실행하면 많은 일이 일어나는 것을 알 수 있습니다. 예상했던 대로 백그라운드에서 많은 네트워크 활동이 발생하고 있습니다. 위 예시에서는 캡처의 일부만 가져왔는데, 특히 `www.google.com`을 핑하기로 결정했을 때의 스니펫입니다.

### 출력 이해하기

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- 첫 번째 필드는 네트워크 활동의 타임스탬프입니다.
- IP: 프로토콜 정보가 포함되어 있습니다.
- 다음으로, 소스 및 대상 주소를 볼 수 있습니다: `icebox.lan > nuq04s29-in-f4.1e100.net`.
- `seq`: TCP 패킷의 시작 및 종료 시퀀스 번호입니다.
- `length`: 바이트 단위의 길이입니다.

tcpdump 출력에서 볼 수 있듯이, 우리는 `www.google.com`으로 ICMP 에코 요청 패킷을 보내고 ICMP 에코 응답 패킷을 다시 받고 있습니다! 또한, 다른 패킷은 다른 정보를 출력한다는 점에 유의하십시오. 자세한 내용은 man 페이지를 참조하십시오.

### tcpdump 출력을 파일에 쓰기

```bash
sudo tcpdump -w /some/file
```

마지막으로 몇 가지 생각: 우리는 패킷 분석 주제의 표면만 긁었습니다. 살펴볼 것이 너무 많고, Hex 및 ASCII 출력으로 더 깊이 들어가는 것은 아직 다루지도 않았습니다. 패킷 분석기에 대해 더 많이 배울 수 있는 온라인 자료가 많으니, 꼭 찾아보시길 바랍니다!

## Exercise

연습이 완벽을 만듭니다! 다음은 패킷 분석에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 tcpdump 로 이더넷 프레임 분석하기](https://labex.io/ko/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - `tcpdump`를 사용하여 이더넷 프레임을 캡처하고 검사하고, 트래픽을 생성하고, 프레임 헤더 및 MAC 주소를 분석하는 연습을 합니다.

이 랩은 실제 시나리오에서 패킷 분석 개념을 적용하고 네트워크 문제 해결에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

tcpdump 로 특정 인터페이스를 캡처하는 플래그는 무엇입니까?

## Quiz Answer

-i
