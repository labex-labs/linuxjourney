---
lang: "ko"
title: "DNS 설정"
meta_title: "DNS 설정 - DNS"
meta_description: "BIND, DNSmasq, PowerDNS 와 같은 Linux 용 인기 DNS 서버에 대해 알아보세요. 이 초보자 친화적인 가이드를 통해 네트워크 설정에 가장 적합한 DNS 서버를 찾아보세요."
meta_keywords: "Linux DNS, BIND, DNSmasq, PowerDNS, DNS 서버 설정, Linux 네트워킹, DNS 튜토리얼, 초보자"
---

## Lesson Content

DNS 서버 설정은 매우 긴 튜토리얼이 될 것이므로 다루지 않겠습니다. 대신, Linux 에서 사용할 인기 있는 DNS 서버에 대한 간략한 비교 목록을 제공합니다.

### BIND

인터넷에서 가장 인기 있는 DNS 서버이며, Linux 배포판에서 사용되는 표준입니다. 원래 캘리포니아 대학교 버클리에서 개발되었으며, 그래서 BIND(Berkeley Internet Name Domain) 라는 이름이 붙었습니다. 모든 기능을 갖춘 강력함과 유연성이 필요하다면 BIND 가 최적의 선택입니다.

### DNSmasq

가볍고 BIND 보다 훨씬 쉽게 구성할 수 있습니다. 단순함을 원하고 BIND 의 모든 부가 기능이 필요하지 않다면 DNSmasq 를 사용하세요. DHCP 및 DNS 를 설정하는 데 필요한 모든 도구가 포함되어 있으며, 소규모 네트워크에 권장됩니다.

### PowerDNS

모든 기능을 갖추고 BIND 와 유사하며, 더 많은 유연성을 제공합니다. MySQL, PostgreSQL 등 여러 데이터베이스에서 정보를 읽어 관리가 더 쉽습니다. BIND 가 오랫동안 사용되어 왔다고 해서 계속 그래야 한다는 의미는 아닙니다.

이것이 전체 목록은 아니지만, 자신만의 DNS 서버를 설정할 때 어디를 찾아봐야 할지에 대한 아이디어를 제공할 것입니다.

## Exercise

No exercises for this lesson.

## Quiz Question

Linux 의 사실상 (de facto) DNS 서버는 무엇입니까?

## Quiz Answer

BIND
