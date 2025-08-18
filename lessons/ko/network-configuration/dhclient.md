---
index: 3
lang: "ko"
title: "dhclient"
meta_title: "dhclient - 네트워크 구성"
meta_description: "dhclient, DHCP 를 사용하여 IP 주소를 얻는 방법, 네트워크 임대를 관리하는 방법에 대해 알아보세요. dhclient.conf 및 dhclient.leases 파일을 이해합니다. Linux 초보자 가이드."
meta_keywords: "dhclient, DHCP, Linux 네트워킹, IP 주소, 네트워크 구성, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

이전에 DHCP 에 대해 논의했으며, 대부분의 경우 IP 주소, 서브넷 마스크 등을 정적으로 설정할 필요가 없습니다. 대신 DHCP 를 사용하게 될 것입니다! `dhclient`는 부팅 시 시작되어 `dhclient.conf` 파일에서 네트워크 인터페이스 목록을 가져옵니다. 나열된 각 인터페이스에 대해 DHCP 프로토콜을 사용하여 인터페이스를 구성하려고 시도합니다.

`dhclient`는 `dhclient.leases` 파일에 시스템 재부팅 전반에 걸쳐 임대 목록을 추적합니다. `dhclient.conf`를 읽은 후 `dhclient.leases` 파일을 읽어 이미 할당된 임대가 무엇인지 알 수 있습니다.

### 새 IP 를 얻으려면

```bash
sudo dhclient
```

## Exercise

No exercises for this lesson.

## Quiz Question

DHCP 프로토콜로 IP 주소를 할당하려고 시도하는 것은 무엇입니까?

## Quiz Answer

dhclient
