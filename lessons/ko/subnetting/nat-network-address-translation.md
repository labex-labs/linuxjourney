---
lang: "ko"
title: "NAT"
description: "Linux 에서 NAT(네트워크 주소 변환) 에 대해 알아보고, 작동 방식과 네트워크 보안에서의 역할을 이해합니다. 사설 IP 와 공용 IP 를 이해합니다. Linux 네트워킹 가이드."
keywords: "NAT, 네트워크 주소 변환, Linux 네트워킹, 사설 IP, 공용 IP, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

이전에 NAT(Network Address Translation) 에 대해 언급했지만 자세히 다루지는 않았습니다. 우리가 네트워크에서 작업할 때 인터넷이 우리의 IP 주소를 볼 수 있다는 의미일까요? 그렇지는 않습니다.

NAT 는 라우터와 같은 장치가 인터넷과 사설 네트워크 사이에서 중개자 역할을 하도록 만듭니다. 따라서 전체 컴퓨터 그룹을 나타내기 위해 단일하고 고유한 IP 주소만 필요합니다.

NAT 를 큰 사무실의 접수원이라고 생각해보세요. 누군가 당신에게 연락하고 싶다면, 그들은 사무실 전체의 번호만 알고 있습니다. 그러면 접수원은 당신의 내선 번호를 찾아 전화를 연결해 줄 것입니다.

### How does it work?

간단한 경우는 다음과 같습니다:

1. Patty 는 <www.google.com>에 연결하려고 하므로, 그녀의 컴퓨터는 이 요청을 라우터를 통해 보냅니다.
2. 라우터는 그 요청을 받아 google.com 에 자체 연결을 열고, 연결이 되면 Patty 의 요청을 보냅니다.
3. 라우터는 Patty 와 <www.google.com> 사이의 중개자입니다. Google 은 Patty 에 대해 알지 못하며, 대신 라우터만 볼 수 있습니다.

NAT 와 일반적인 패킷 라우팅은 상당히 복잡해질 수 있지만, 우리는 세부 사항까지 깊이 파고들지는 않을 것입니다.

## Exercise

No exercises for this lesson.

## Quiz Question

인터넷에 단일 사설 주소를 나타내는 데 사용되는 것은 무엇입니까?

## Quiz Answer

NAT
