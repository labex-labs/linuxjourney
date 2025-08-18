---
index: 5
lang: "ko"
title: "CIDR"
meta_title: "CIDR - 서브넷팅"
meta_description: "Linux 네트워킹을 위한 CIDR 표기법을 배우세요. 이 초보자 친화적인 가이드를 통해 서브넷 마스크, IP 주소 지정 및 호스트 계산을 이해하세요. 네트워크 기술을 향상시키세요!"
meta_keywords: "CIDR, 서브넷 마스크, IP 주소 지정, 네트워크 프리픽스, Linux 네트워킹, 초보자, 튜토리얼, 가이드"
---

## Lesson Content

CIDR (Classless Inter-Domain Routing) 은 서브넷 마스크를 더 간결하게 표현하는 데 사용됩니다. 10.42.3.0/255.255.255.0과 같은 서브넷이 10.42.3.0/24와 같이 CIDR 표기법으로 표시되는 것을 볼 수 있습니다. 이 표기법은 서브넷 프리픽스와 서브넷 마스크를 모두 포함합니다.

IP 주소는 4 바이트 또는 32 비트로 구성된다는 것을 기억하십시오. CIDR 은 네트워크 프리픽스로 사용되는 비트 수를 나타냅니다. 따라서 123.12.24.0/23은 처음 23 비트가 사용됨을 의미합니다. 이것이 무엇을 의미할까요? 호스트 수는 몇 개일까요?

간단한 요령은 IP 주소가 가질 수 있는 총 비트 수 (32) 에서 CIDR 주소 (23) 를 빼는 것입니다. 그러면 9 비트가 남습니다. 따라서 2^9 = 512 입니다. 그러나 2 개의 주소 (서브넷 주소와 브로드캐스트 주소) 를 제외해야 하므로 사용 가능한 호스트는 510 개입니다.

## Exercise

No exercises for this lesson.

## Quiz Question

No questions, move along!

## Quiz Answer
