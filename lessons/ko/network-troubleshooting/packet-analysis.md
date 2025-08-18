---
index: 5
lang: "ko"
title: "패킷 분석"
meta_title: "패킷 분석 - 문제 해결"
meta_description: "tcpdump 를 사용하여 패킷 분석의 기본을 배웁니다. 이 초보자 친화적인 Linux 가이드를 통해 네트워크 트래픽을 이해하고, 데이터를 캡처하며, 출력을 해석합니다."
meta_keywords: "tcpdump, 패킷 분석, 네트워크 분석, Linux 네트워킹, 초보자 튜토리얼, Wireshark, Linux 명령어, 네트워크 트래픽"
---

## Lesson Content

패킷 분석이라는 주제는 그 자체로 하나의 전체 과정을 채울 수 있으며, 패킷 분석에 대해서만 쓰여진 책도 많습니다. 하지만 오늘은 기본적인 내용만 배우겠습니다. Wireshark 와 tcpdump 라는 두 가지 매우 인기 있는 패킷 분석기가 있습니다. 이 도구들은 네트워크 인터페이스를 스캔하고, 패킷 활동을 캡처하며, 패킷을 파싱하고, 정보를 출력하여 우리가 볼 수 있도록 합니다. 이를 통해 네트워크 분석의 핵심을 파고들어 낮은 수준의 내용을 탐구할 수 있습니다. 우리는 더 간단한 인터페이스를 가진 tcpdump 를 사용할 것이지만, 만약 패킷 분석을 도구로 사용하고 싶다면 Wireshark 를 살펴보는 것을 추천합니다.

### Install tcpdump

```bash
sudo apt install tcpdump
```

### Capture packet data on an interface

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

패킷 캡처를 실행하면 많은 일이 일어나는 것을 알 수 있습니다. 이는 예상된 일입니다. 백그라운드에서 많은 네트워크 활동이 발생하고 있습니다. 위 예시에서는 캡처의 일부만 가져왔는데, 특히 <www.google.com>을 ping 하기로 결정한 시점의 스니펫입니다.

### Understanding the output

```plaintext
11:28:23.958840 IP icebox.lan > nuq04s29-in-f4.1e100.net: ICMP echo request, id 1901, seq 2, length 64
11:28:23.970928 IP nuq04s29-in-f4.1e100.net > icebox.lan: ICMP echo reply, id 1901, seq 2, length 64
```

- 첫 번째 필드는 네트워크 활동의 타임스탬프입니다.
- IP: 프로토콜 정보를 포함합니다.
- 다음으로, 소스 및 대상 주소를 볼 수 있습니다: `icebox.lan > nuq04s29-in-f4.1e100.net`.
- `seq`: TCP 패킷의 시작 및 종료 시퀀스 번호입니다.
- `length`: 바이트 단위의 길이입니다.

tcpdump 출력에서 볼 수 있듯이, 우리는 <www.google.com>으로 ICMP echo request 패킷을 보내고 ICMP echo reply 패킷을 응답으로 받고 있습니다! 또한, 다른 패킷은 다른 정보를 출력한다는 점에 유의하십시오. 자세한 내용은 manpage 를 참조하십시오.

### Writing tcpdump output to a file

```bash
sudo tcpdump -w /some/file
```

마지막으로, 우리는 패킷 분석 주제의 표면만 훑었습니다. 살펴볼 것이 너무 많고, Hex 및 ASCII 출력으로 더 깊이 들어가는 것은 아직 다루지도 않았습니다. 패킷 분석기에 대해 더 많이 배울 수 있는 온라인 자료가 많으니 찾아보시길 권합니다!

## Exercise

Wireshark 도구를 다운로드하여 설치하고 인터페이스를 사용해보세요.

## Quiz Question

tcpdump 로 특정 인터페이스를 캡처하는 플래그는 무엇입니까?

## Quiz Answer

-i
