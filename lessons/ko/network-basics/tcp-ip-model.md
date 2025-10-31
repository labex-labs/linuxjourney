---
index: 3
lang: "ko"
title: "TCP/IP 모델"
meta_title: "TCP/IP 모델 - 네트워크 기초"
meta_description: "현대 네트워킹의 초석인 TCP/IP 모델의 기본 계층을 살펴보세요. 효과적인 TCP/IP 네트워킹을 위해 애플리케이션, 전송, 네트워크 및 링크 계층에 대해 알아보세요."
meta_keywords: "TCP/IP 모델, tcp ip 모델의 계층, tcp ip 네트워킹, tcp 프로토콜 계층, 네트워크 계층, TCP, IP, 리눅스 네트워킹, 실제 프로토콜 프로젝트"
---

## Lesson Content

이론적인 OSI 모델에서 탄생한 TCP/IP 모델은 인터넷이 구축된 실제적인 기반입니다. 이는 네트워킹의 실제 구현을 나타냅니다. TCP/IP 모델은 우리가 흔히 TCP/IP라고 부르는 TCP/IP 프로토콜 스위트를 사용합니다. 효과적인 **TCP/IP 네트워킹**은 데이터가 수집, 주소 지정, 전송 및 라우팅되는 방식을 지정하기 위해 함께 작동하는 이러한 프로토콜에 달려 있습니다. **TCP/IP 모델의 계층**을 검토함으로써 데이터 패킷이 네트워크를 통해 이동하는 방식을 이해할 수 있습니다.

### TCP/IP 모델의 네 가지 계층

이 모델은 각각 특정 기능을 가진 네 가지 뚜렷한 계층으로 나뉩니다. 이러한 계층을 이해하는 것은 모든 **실제 프로토콜 프로젝트** 또는 네트워크 문제 해결 작업에 중요합니다.

### 애플리케이션 계층

이 계층은 사용자 대면 애플리케이션과 네트워크 서비스가 상주하는 TCP/IP 모델의 최상위 계층입니다. 웹 브라우저나 이메일 클라이언트와 같은 프로그램이 전송 계층 서비스를 사용하여 데이터를 송수신하는 방법을 결정합니다.

이 계층은 다음과 같은 프로토콜을 사용합니다.

- HTTP (Hypertext Transfer Protocol): 월드 와이드 웹의 데이터 통신 기반.
- SMTP (Simple Mail Transfer Protocol): 전자 메일 (이메일) 전송에 사용됩니다.

### 전송 계층

전송 계층은 종단 간 통신 및 데이터 무결성을 담당합니다. 데이터가 전송되는 방식, 포트 번호 관리, 패킷이 안정적으로 전달되는지 확인하는 방법을 설정합니다. **TCP 프로토콜의 계층** 스위트가 이 부분에서 가장 두드러집니다.

이 계층은 주로 다음을 사용합니다.

- TCP (Transmission Control Protocol): 데이터 스트림의 안정적이고 순서가 지정되며 오류 검사가 수행되는 전송을 제공합니다. 연결 지향적입니다.
- UDP (User Datagram Protocol): 전송이나 순서를 보장하지 않으므로 신뢰할 수 없다고 간주되는 더 빠르고 비연결적인 데이터 전송 방법을 제공합니다.

### 네트워크 계층

인터넷 계층이라고도 하는 이 계층은 호스트 간 및 여러 네트워크를 통해 패킷을 이동하는 방법을 지정합니다. 주요 작업은 주소 지정 및 라우팅입니다. 이 계층에서 할당된 IP 주소는 네트워크에서 장치의 식별에 근본적이며, 이는 특정 네트워크의 일부라는 **ip 제휴 의미** 개념과 관련이 있습니다.

이 계층은 다음과 같은 프로토콜을 사용합니다.

- IP (Internet Protocol): 소스 머신에서 대상 머신으로 패킷을 라우팅합니다.
- ICMP (Internet Control Message Protocol): `ping` 명령과 같이 오류 메시지 및 운영 정보를 전송하는 데 사용됩니다.

### 링크 계층

네트워크 인터페이스 계층이라고도 하는 이 계층은 물리적 하드웨어를 통해 데이터를 전송하는 방법을 지정합니다. 이더넷, Wi-Fi 또는 광섬유 케이블을 통해 로컬 네트워크 세그먼트에서 데이터 패킷 전송을 처리합니다.

위에 나열된 프로토콜이 전부는 아니며, 다른 많은 프로토콜을 접하게 될 것입니다. 다음 강의에서는 TCP/IP 모델 관점에서 패킷이 네트워크를 통과하는 방식을 확인하기 위해 이러한 각 계층을 더 깊이 탐구할 것입니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 TCP/IP 모델 및 네트워크 기본 사항에 대한 이해를 강화하기 위한 실습 랩입니다.

1. **[Linux 에서 MAC 및 IP 주소 식별하기](https://labex.io/ko/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 MAC 및 IP 주소와 같은 주요 네트워크 주소 정보를 식별하는 연습을 합니다. 이는 TCP/IP 모델의 네트워크 및 데이터 링크 계층을 이해하는 데 기본이 됩니다.
2. **[Linux 에서 ping 및 arp 를 사용한 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` 및 `arp` 명령이 네트워크 계층과 데이터 링크 계층 간의 상호 작용을 시연하는 방법을 학습하여 장치가 TCP/IP 스택 내에서 통신하는 방식에 대한 실제적인 통찰력을 얻습니다.
3. **[Linux 에서 네트워크 계층 연결 시뮬레이션](https://labex.io/ko/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Linux 노드 간의 네트워크 연결을 시뮬레이션하고, IP 주소를 할당하고, 통신을 테스트하는 실습 경험을 얻습니다. 이는 TCP/IP 모델의 네트워크 계층과 관련된 개념을 직접 적용하는 것입니다.

이러한 랩은 실제 시나리오에서 TCP/IP 모델의 개념을 적용하고 네트워크 구성 및 문제 해결에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

What is the top layer of the TCP/IP model? (Please answer in English. Note that the answer is case-sensitive.)

## Quiz Answer

Application
