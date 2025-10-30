---
index: 3
lang: "ko"
title: "TCP/IP 모델"
meta_title: "TCP/IP 모델 - 네트워크 기본"
meta_description: "TCP/IP 모델의 계층 (애플리케이션, 전송, 네트워크, 링크) 에 대해 알아보세요. 데이터가 네트워크를 통해 어떻게 이동하는지 이해하세요. Linux 네트워킹 여정을 시작하세요!"
meta_keywords: "TCP/IP 모델, 네트워킹 기본, Linux 네트워킹, TCP, IP, 초보자 튜토리얼, 네트워크 계층, 가이드"
---

## Lesson Content

OSI 모델은 결국 TCP/IP 모델이 되었고, 이 모델은 실제로 인터넷의 기반이 됩니다. 이는 네트워킹의 실제 구현입니다. TCP/IP 모델은 일반적으로 TCP/IP라고 부르는 TCP/IP 프로토콜 스위트를 사용합니다. 이 프로토콜들은 함께 작동하여 데이터가 네트워크를 통해 어떻게 수집되고, 주소가 지정되고, 전송되고, 라우팅되어야 하는지를 명시합니다. TCP/IP 모델을 사용하면 이러한 프로토콜이 패킷이 네트워크를 통해 이동하는 과정을 어떻게 보여주는지 알 수 있습니다.

### 애플리케이션 계층

TCP/IP 모델의 최상위 계층입니다. 웹 브라우저와 같은 컴퓨터 프로그램이 전송 계층 서비스와 어떻게 인터페이스하여 전송되거나 수신되는 데이터를 볼지 결정합니다.

이 계층은 다음을 사용합니다:

- HTTP (Hypertext Transfer Protocol) - 인터넷 웹페이지에 사용됩니다.
- SMTP (Simple Mail Transfer Protocol) - 전자 메일 (이메일) 전송

### 전송 계층

데이터가 어떻게 전송될지, 올바른 포트 확인, 데이터 무결성 확인, 그리고 기본적으로 패킷을 전달하는 것을 포함합니다.

이 계층은 다음을 사용합니다:

- TCP (Transmission Control Protocol) - 신뢰할 수 있는 데이터 전송
- UDP (User Datagram Protocol) - 신뢰할 수 없는 데이터 전송

### 네트워크 계층

이 계층은 호스트 간 및 네트워크 간에 패킷을 이동하는 방법을 명시합니다.

이 계층은 다음을 사용합니다:

- IP (Internet Protocol) - 한 장치에서 다른 장치로 패킷을 라우팅하는 데 도움을 줍니다.
- ICMP (Internet Control Message Protocol) - 오류 메시지 및 디버깅 정보와 같이 현재 상황을 알려주는 데 도움을 줍니다.

### 링크 계층

이 계층은 이더넷, 광섬유 등을 통해 이동하는 데이터와 같이 물리적인 하드웨어 조각을 통해 데이터를 전송하는 방법을 명시합니다.

각 계층이 사용하는 프로토콜 목록은 광범위하지 않으며, 앞으로 많은 다른 프로토콜들을 접하게 될 것입니다.

다음 레슨에서는 각 계층을 자세히 살펴보고 TCP/IP 모델의 관점에서 패킷이 네트워크를 어떻게 통과하는지 논의할 것입니다 (패킷이 네트워크를 통해 이동하는 방식에 대한 많은 관점이 있습니다. 우리는 모든 것을 살펴보지는 않겠지만, 그러한 관점들이 존재한다는 것을 알아두십시오).

## Exercise

연습은 완벽을 만듭니다! 다음은 TCP/IP 모델 및 네트워크 기본 사항에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 MAC 및 IP 주소와 같은 주요 네트워크 주소 지정 정보를 식별하는 연습을 통해 TCP/IP 모델의 네트워크 및 데이터 링크 계층을 이해하는 데 필수적인 지식을 습득합니다.
2. **[Linux 에서 ping 및 arp 를 사용한 네트워크 계층 상호 작용 탐색](https://labex.io/ko/labs/comptia-explore-network-layer-interaction-with-ping-and-arp-in-linux-592746)** - `ping` 및 `arp` 명령이 네트워크 및 데이터 링크 계층 간의 상호 작용을 어떻게 보여주는지 학습하여 TCP/IP 스택 내에서 장치가 통신하는 방식에 대한 실질적인 통찰력을 얻습니다.
3. **[Linux 에서 네트워크 계층 연결 시뮬레이션](https://labex.io/ko/labs/comptia-simulate-network-layer-connectivity-in-linux-592752)** - Linux 노드 간의 네트워크 연결을 시뮬레이션하고, IP 주소를 할당하고, 통신을 테스트하는 실습 경험을 통해 TCP/IP 모델의 네트워크 계층과 관련된 개념을 직접 적용합니다.

이러한 랩은 실제 시나리오에서 TCP/IP 모델의 개념을 적용하고 네트워크 구성 및 문제 해결에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

TCP/IP 모델의 최상위 계층은 무엇입니까?

## Quiz Answer

Application
