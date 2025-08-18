---
lang: "ko"
title: "TCP/IP 모델"
meta_title: "TCP/IP 모델 - 네트워크 기본"
meta_description: "TCP/IP 모델의 계층 (애플리케이션, 전송, 네트워크, 링크) 에 대해 알아보세요. 데이터가 네트워크를 통해 어떻게 이동하는지 이해하세요. Linux 네트워킹 여정을 시작하세요!"
meta_keywords: "TCP/IP 모델, 네트워킹 기초, Linux 네트워킹, TCP, IP, 초보자 튜토리얼, 네트워크 계층, 가이드"
---

## Lesson Content

OSI 모델은 결국 TCP/IP 모델의 기반이 되었으며, 이 모델은 실제로 인터넷이 기반으로 하는 것입니다. 이는 네트워킹의 실제 구현입니다. TCP/IP 모델은 우리가 일반적으로 TCP/IP라고 부르는 TCP/IP 프로토콜 스위트를 사용합니다. 이 프로토콜들은 데이터가 네트워크를 통해 어떻게 수집되고, 주소가 지정되고, 전송되고, 라우팅되어야 하는지를 지정하기 위해 함께 작동합니다. TCP/IP 모델을 사용하면 이러한 프로토콜들이 패킷이 네트워크를 통해 어떻게 이동하는지 보여주는 데 어떻게 사용되는지 알 수 있습니다.

### Application Layer

TCP/IP 모델의 최상위 계층입니다. 컴퓨터 프로그램 (예: 웹 브라우저) 이 전송 계층 서비스와 어떻게 인터페이스하여 전송되거나 수신되는 데이터를 볼지 결정합니다.

이 계층은 다음을 사용합니다:

- HTTP (Hypertext Transfer Protocol) - 인터넷의 웹 페이지에 사용됩니다.
- SMTP (Simple Mail Transfer Protocol) - 전자 메일 (이메일) 전송

### Transport Layer

데이터가 어떻게 전송될지, 올바른 포트 확인, 데이터 무결성, 그리고 기본적으로 패킷을 전달하는 것을 포함합니다.

이 계층은 다음을 사용합니다:

- TCP (Transmission Control Protocol) - 신뢰할 수 있는 데이터 전송
- UDP (User Datagram Protocol) - 신뢰할 수 없는 데이터 전송

### Network Layer

이 계층은 호스트 간 및 네트워크 간에 패킷을 이동하는 방법을 지정합니다.

이 계층은 다음을 사용합니다:

- IP (Internet Protocol) - 한 컴퓨터에서 다른 컴퓨터로 패킷을 라우팅하는 데 도움이 됩니다.
- ICMP (Internet Control Message Protocol) - 오류 메시지 및 디버깅 정보와 같이 무엇이 진행되고 있는지 알려주는 데 도움이 됩니다.

### Link Layer

이 계층은 이더넷, 광섬유 등을 통해 이동하는 데이터와 같이 물리적인 하드웨어 조각을 통해 데이터를 보내는 방법을 지정합니다.

각 계층이 사용하는 프로토콜 목록은 광범위하지 않으며, 여러분은 많은 다른 프로토콜들을 만나게 될 것입니다.

다음 강의에서는 이러한 각 계층을 자세히 살펴보고 TCP/IP 모델의 관점에서 패킷이 네트워크를 어떻게 통과하는지 논의할 것입니다 (패킷이 네트워크를 통해 이동하는 방식에 대한 많은 관점이 있습니다; 우리는 모든 것을 살펴보지는 않겠지만, 그것들이 존재한다는 것을 알아두십시오).

## Exercise

No exercises for this lesson.

## Quiz Question

TCP/IP 모델의 최상위 계층은 무엇입니까?

## Quiz Answer

Application
