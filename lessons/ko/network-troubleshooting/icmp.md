---
index: 1
lang: "ko"
title: "ICMP"
meta_title: "ICMP - 문제 해결"
meta_description: "ICMP 프로토콜의 기본 사항, 메시지 유형 및 네트워크 문제 해결을 위한 코드를 학습합니다. ICMP 가 네트워크 문제를 디버깅하는 방법을 이해합니다."
meta_keywords: "ICMP, ICMP 프로토콜, 네트워크 문제 해결, ICMP 유형, Linux 네트워킹, 초급, 튜토리얼, 가이드"
---

## Lesson Content

ICMP(Internet Control Message Protocol) 는 TCP/IP 프로토콜 스위트의 일부입니다. 업데이트 및 오류 메시지를 보내는 데 사용되며, 패킷 전달 실패와 같은 네트워크 문제를 디버깅하는 데 매우 유용한 프로토콜입니다.

각 ICMP 메시지에는 type, code, checksum 필드가 포함됩니다. type 필드는 ICMP 메시지의 유형을 나타내고, code 는 메시지에 대한 추가 정보를 제공하는 하위 유형이며, checksum 은 메시지 무결성 문제를 감지하는 데 사용됩니다.

몇 가지 일반적인 ICMP 유형을 살펴보겠습니다:

- Type 0 - Echo Reply
- Type 3 - Destination Unreachable
- Type 8 - Echo Request
- Type 11 - Time Exceeded

패킷이 대상에 도달할 수 없을 때, Type 3 ICMP 메시지가 생성됩니다. Type 3 내에는 대상에 도달할 수 없는 이유를 더 자세히 설명하는 16 개의 code 값이 있습니다:

- Code 0 - Network Unreachable
- Code 1 - Host Unreachable
  etc...etc...

이러한 메시지는 일부 네트워크 문제 해결 도구를 사용하면서 더 이해하기 쉬울 것입니다.

## Exercise

No exercises for this lesson.

## Quiz Question

에코 요청에 대한 ICMP 유형은 무엇입니까?

## Quiz Answer

8
