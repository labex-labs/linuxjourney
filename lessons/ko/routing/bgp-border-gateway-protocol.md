---
index: 7
lang: "ko"
title: "Border Gateway Protocol"
meta_title: "Border Gateway Protocol - 라우팅"
meta_description: "BGP, Border Gateway Protocol, 그리고 이것이 자율 시스템 간의 인터넷 라우팅을 어떻게 가능하게 하는지 알아보세요. 초보자를 위한 BGP 기본 사항을 이해하세요."
meta_keywords: "BGP, Border Gateway Protocol, 인터넷 라우팅, 자율 시스템, Linux 네트워킹, BGP 튜토리얼, 네트워크 프로토콜, 초보자 가이드"
---

## Lesson Content

우리가 논의할 마지막 중요한 프로토콜은 BGP 입니다. BGP 는 기본적으로 인터넷이 작동하는 방식입니다. 자율 시스템 간에 라우팅 정보를 수집하고 교환하는 데 사용됩니다. 자율 시스템을 인터넷 서비스 제공업체, 회사, 대학, 모든 조직 등으로 생각해보세요. BGP 가 없으면 이러한 시스템은 서로 통신하는 방법을 알지 못하고 고립될 것입니다. BGP 는 이러한 자율 시스템 내부에서 라우팅하는 대신 시스템 간에 라우팅합니다.

당신이 집 네트워크에 있고 제가 스타벅스에서 일하고 있다고 가정해 봅시다. 저는 당신과 통신하고 싶어서 이메일을 보냅니다. 네트워크 패킷은 스타벅스 네트워크를 통해 이동하고, 그곳에서 이리저리 튀어 다니며, 스타벅스 네트워크의 라우팅 테이블을 거쳐 마침내 스타벅스 네트워크의 경계 지점에 도달하여 Border Gateway 라우터로 전달됩니다. 이 라우터에는 내 패킷이 스타벅스 네트워크를 떠나 다른 네트워크를 통과하는 데 필요한 정보가 포함되어 있습니다.

## Exercise

이 주제에 대한 특정 실습은 없지만, 관련 Linux 기술 및 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 탐색하는 것을 권장합니다.

## Quiz Question

인터넷을 기본적으로 작동하게 하는 프로토콜은 무엇입니까?

## Quiz Answer

BGP
