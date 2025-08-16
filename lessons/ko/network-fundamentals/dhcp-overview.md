---
lang: "ko"
title: "DHCP 개요"
description: "Linux 에서 DHCP(Dynamic Host Configuration Protocol) 에 대해 알아보세요. DHCP 가 IP 주소를 할당하는 방법과 4 단계 프로세스를 이해하세요. Linux 네트워킹 여정을 시작하세요!"
keywords: "DHCP, Dynamic Host Configuration Protocol, Linux 네트워킹, IP 주소, DHCP 튜토리얼, 초보자, 가이드"
---

## Lesson Content

아직 다루지 않은 중요한 네트워킹 개념은 DHCP (Dynamic Host Configuration Protocol) 입니다.

DHCP 는 우리 장치에 IP 주소, 서브넷 마스크 및 게이트웨이를 할당합니다. 예를 들어, 휴대폰이 있고 사람들과 대화하기 위해 휴대폰 번호를 받고 싶다고 가정해 봅시다. 통신사에 전화해야 하고, 통신사가 번호를 줄 것입니다. 요금을 지불하는 한 계속 휴대폰을 사용할 수 있습니다. 이 경우 DHCP 는 통신사 역할을 합니다. 다른 IP 주소와 통신할 수 있도록 IP 주소를 제공합니다. 또한 IP 주소를 임대받습니다. 이 임대는 특정 기간 동안 지속되며, 임대 설정에 따라 갱신됩니다.

DHCP 는 여러 가지 이유로 훌륭합니다. 네트워크 관리자가 IP 주소 할당에 대해 걱정할 필요가 없게 해주며, 중복된 IP 주소를 설정하는 것을 방지합니다. 모든 물리적 네트워크는 호스트가 IP 주소를 요청할 수 있도록 자체 DHCP 서버를 가지고 있어야 합니다. 일반적인 가정 환경에서는 라우터가 일반적으로 DHCP 서버 역할을 합니다.

DHCP 가 모든 동적 호스트 정보를 얻는 방법은 다음과 같습니다:

1. DHCP DISCOVER - 이 메시지는 DHCP 서버를 찾기 위해 브로드캐스트됩니다.
2. DHCP OFFER - 네트워크의 DHCP 서버가 제안 메시지로 응답합니다. 이 제안에는 DHCP 임대 시간, 서브넷 마스크, IP 주소 등이 포함된 패킷이 들어 있습니다.
3. DHCP REQUEST - 클라이언트는 어떤 제안을 수락했는지 모든 DHCP 서버에 알리기 위해 또 다른 브로드캐스트를 보냅니다.
4. DHCP ACK - 서버에서 승인이 전송됩니다.

DHCP 는 이보다 더 복잡하지만, 이것이 핵심입니다.

## Exercise

이 레슨에는 연습 문제가 없습니다.

## Quiz Question

DHCP 요청의 단계는 무엇입니까?

## Quiz Answer

DISCOVER, OFFER, REQUEST, ACK
