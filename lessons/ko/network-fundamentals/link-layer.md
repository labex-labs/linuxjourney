---
lang: "ko"
title: "링크 계층"
meta_description: "TCP/IP의 링크 계층, ARP 가 MAC 주소를 해결하는 방법, 패킷 이동에 대해 알아보세요. 이 Linux 네트워킹 튜토리얼을 통해 네트워크 기본 사항을 이해하세요."
meta_keywords: "링크 계층, ARP, TCP/IP, MAC 주소, 네트워크 기본 사항, Linux 네트워킹, 초급, 튜토리얼"
---

## Lesson Content

TCP/IP 모델의 가장 아래에는 Link Layer 가 있습니다. 이 계층은 하드웨어에 특화되어 있습니다.

링크 계층에서 우리의 패킷은 프레임이라는 것으로 한 번 더 캡슐화됩니다. 프레임 헤더는 송신 및 수신 호스트의 MAC 주소, 체크섬, 그리고 수신자가 패킷이 언제 끝나는지 알 수 있도록 패킷 구분자를 첨부합니다.

다행히 우리는 같은 네트워크에 있으므로 패킷이 너무 멀리 이동할 필요는 없습니다. 먼저, 링크 계층은 내 송신 MAC 주소를 프레임 헤더에 첨부하지만, Patty 의 MAC 주소도 알아야 합니다. 그것을 어떻게 알 수 있으며, 인터넷에 없는데 어떻게 찾을 수 있을까요? 우리는 ARP 를 사용합니다!

### ARP (Address Resolution Protocol)

ARP 는 IP 주소와 연결된 MAC 주소를 찾습니다. ARP 는 동일한 네트워크 내에서 사용됩니다. 만약 Patty 가 같은 네트워크에 있지 않았다면, 우리는 패킷을 받을 다음 라우터를 결정하기 위해 라우팅 시스템을 사용했을 것이고, 일단 같은 네트워크에 있게 되면 ARP 를 사용할 수 있습니다.

일단 같은 네트워크에 있게 되면, 시스템은 먼저 어떤 IP 주소가 어떤 MAC 주소와 연결되어 있는지에 대한 정보를 저장하는 ARP 조회 테이블을 사용합니다. 만약 해당 값이 없으면 ARP 가 사용됩니다. 그러면 시스템은 ARP 프로토콜을 사용하여 네트워크에 브로드캐스트 메시지를 보내 IP 10.10.1.4 를 가진 호스트가 누구인지 찾습니다. 브로드캐스트 메시지는 네트워크의 모든 호스트에게 전송되는 특별한 메시지입니다 (브로드캐스트를 보내는 데 적합하게 이름이 붙여졌습니다). 요청된 IP 주소를 가진 모든 머신은 IP 주소와 MAC 주소를 포함하는 ARP 패킷으로 응답할 것입니다.

이제 필요한 모든 데이터 (IP 주소 및 MAC 주소) 를 확보했으므로, 우리의 링크 계층은 이 프레임을 네트워크 인터페이스 카드를 통해 다음 장치로 전달하고 Patty 의 네트워크를 찾습니다. 이 단계는 제가 방금 설명한 것보다 조금 더 복잡하지만, 라우팅 과정에서 더 자세히 논의할 것입니다.

그리고 이것이 바로 TCP/IP 계층을 통한 간단한 (또는 그렇게 간단하지 않은) 패킷 이동입니다. 패킷이 이런 식으로 일방적으로 이동하지 않는다는 점을 명심하십시오. 우리는 아직 Patty 의 네트워크에 도달하지도 않았습니다! 네트워크를 통해 이동할 때는 데이터가 전송되거나 수신되기 전에 TCP/IP 모델을 최소 두 번 거쳐야 합니다. 실제로는 이 패킷의 모습은 다음과 같을 것입니다:

### Packet Traversal

1. Pete sends Patty an email: this data gets sent to the transport layer.
2. The transport layer encapsulates the data into a TCP or UDP header to form a segment. The segment attaches the destination and source TCP or UDP port, then the segment is sent to the network layer.
3. The network layer encapsulates the TCP segment inside an IP packet; it attaches the source and destination IP address. Then it routes the packet to the link layer.
4. The packet then reaches Pete's physical hardware and gets encapsulated in a frame. The source and destination MAC addresses get added to the frame.
5. Patty receives this data frame through her physical layer and checks each frame for data integrity, then de-encapsulates the frame contents and sends the IP packet to the network layer.
6. The network layer reads the packet to find the source and destination IP that was previously attached. It checks if its IP is the same as the destination IP, which it is! It de-encapsulates the packet and sends the segment to the transport layer.
7. The transport layer de-encapsulates the segments, checks the TCP or UDP port numbers, and makes a connection to the application layer based on those port numbers.
8. The application layer receives the data from the transport layer on the port that was specified and presents it to Patty in the form of the final email message.

## Exercise

No exercises for this lesson.

## Quiz Question

동일한 네트워크에서 MAC 주소를 찾는 데 사용되는 것은 무엇입니까?

## Quiz Answer

ARP
