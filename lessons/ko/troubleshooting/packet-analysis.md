---
index: 5
lang: "ko"
title: "패킷 분석"
meta_title: "패킷 분석 - 문제 해결"
meta_description: "Linux 에서 네트워크 패킷 분석의 기본 사항을 알아보세요. 이 가이드는 강력한 패킷 분석기인 tcpdump 를 사용하여 네트워크 트래픽을 캡처하고 해석하는 방법을 소개합니다."
meta_keywords: "tcpdump, 패킷 분석, 네트워크 패킷 분석, 네트워크 패킷 분석기, 네트워크 분석, 네트워크 패킷 분석 도구, Linux 네트워킹, Wireshark, Linux 명령어, 네트워크 트래픽"
---

## Lesson Content

네트워크 패킷 분석 분야는 방대하며 전체 강좌와 책의 주제가 될 수 있습니다. 본 강의에서는 기본 사항을 소개합니다. 패킷 분석은 네트워크를 통해 전송되는 데이터를 캡처하고 검사하는 것을 포함합니다. 이는 네트워크 문제 해결, 성능 튜닝 및 보안 분석을 위한 필수 기술입니다. 개별 패킷을 검사함으로써 네트워크에서 낮은 수준에서 무슨 일이 일어나고 있는지에 대한 깊은 통찰력을 얻을 수 있습니다.

### 인기 있는 네트워크 패킷 분석 도구

네트워크 패킷 분석 도구 중 매우 인기 있는 두 가지는 Wireshark 와 tcpdump 입니다. 둘 다 강력한 패킷 분석 애플리케이션으로, 네트워크 인터페이스를 스캔하고, 패킷 활동을 캡처하며, 검사를 위해 데이터를 구문 분석합니다. 이를 통해 네트워크 분석의 세부 사항까지 파고들 수 있습니다. 명령줄의 단순성 때문에 tcpdump 를 사용할 것이지만, 네트워크 패킷 분석을 더 깊이 탐구할 계획이라면 Wireshark 의 그래픽 인터페이스를 살펴보는 것이 강력히 권장됩니다.

### tcpdump 설치

Ubuntu 와 같은 Debian 기반 시스템에서는 다음 명령으로 tcpdump 를 설치할 수 있습니다.

```bash
sudo apt install tcpdump
```

### 실시간 패킷 데이터 캡처

특정 인터페이스에서 데이터 캡처를 시작하려면 `-i` 플래그 뒤에 인터페이스 이름을 사용합니다.

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

패킷 캡처를 실행하면 예상대로 많은 활동이 표시되는데, 이는 지속적인 백그라운드 네트워크 트래픽 때문입니다. 위의 예시는 `www.google.com`에 ping 을 보내는 동안 캡처한 내용의 일부를 보여줍니다.

### tcpdump 출력 해석

캡처된 한 줄을 분석해 보겠습니다.

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
```

- **타임스탬프**: 첫 번째 필드 (`11:28:23.958840`) 는 패킷이 캡처된 시간을 나타냅니다.
- **프로토콜**: `IP`는 네트워크 계층 프로토콜을 나타냅니다.
- **소스 및 대상**: `icebox.lan > nuq04s29-in-f4.1e100.net`은 패킷의 출발지와 목적지를 보여줍니다.
- **프로토콜별 정보**: 나머지 줄에는 프로토콜별 세부 정보가 포함되어 있습니다. 이 ICMP 패킷의 경우:
  - `seq`: 패킷의 시퀀스 번호입니다.
  - `length`: 패킷의 길이를 바이트 단위로 나타냅니다.

보시다시피, 우리 장치는 ICMP 에코 요청을 보냈고 ICMP 에코 응답을 받았습니다. 다른 프로토콜은 다른 정보를 표시하므로 자세한 내용은 매뉴얼 페이지를 참조하십시오.

### 나중에 분석을 위해 캡처 저장

실시간 트래픽을 보는 대신, `-w` 플래그를 사용하여 캡처를 파일로 저장할 수 있습니다. 이는 보다 심층적인 오프라인 패킷 분석에 유용합니다.

```bash
sudo tcpdump -w /some/file.pcap
```

우리는 패킷 분석의 표면만 훑어보았습니다. 고급 필터링 및 Hex 및 ASCII 로 패킷 내용을 검사하는 것을 포함하여 탐구할 것이 훨씬 더 많습니다. 수많은 온라인 리소스가 네트워크 패킷 분석 도구를 마스터하는 데 도움이 될 것이며, 학습 여정을 계속하시기를 권장합니다.

## Exercise

패킷 분석에 대한 이해를 공고히 하기 위해 이 실습 랩을 시도해 보세요. 연습이 완벽을 만듭니다!

1. **[Linux 에서 tcpdump 로 이더넷 프레임 분석하기](https://labex.io/ko/labs/comptia-analyze-ethernet-frames-with-tcpdump-in-linux-592765)** - `tcpdump`를 사용하여 이더넷 프레임 캡처 및 검사, 트래픽 생성, 프레임 헤더 및 MAC 주소 분석을 연습합니다.

이 랩은 실제 시나리오에서 패킷 분석 개념을 적용하고 네트워크 문제 해결에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

tcpdump 로 특정 인터페이스를 캡처하는 플래그는 무엇입니까? 답변 시 필요한 플래그만 영어로 입력하십시오. 대소문자를 구분합니다.

## Quiz Answer

-i
