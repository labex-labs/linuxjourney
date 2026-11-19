---
lesson_id: "linux-listening-services"
course_id: "linux-hardening"
lang: "ko"
order_index: 4
title: "연결을 기다리는 서비스"
description: "Linux에서 서비스가 연결을 기다리는 주소를 읽고 어느 위치에서 접근을 검사할지 정하는 방법을 알아봅니다."
meta_title: "연결을 기다리는 서비스 - Linux 보안 강화"
meta_description: "Linux에서 서비스가 연결을 기다리는 주소를 읽고 어느 위치에서 접근을 검사할지 정하는 방법을 알아봅니다."
meta_keywords: "수신 소켓, Linux 보안 강화, 사이버 보안, Linux Journey"
---

서비스는 특정 주소와 포트에서 연결을 기다릴 수 있습니다. **수신 소켓**은 들어오는 연결을 받을 준비가 된 소켓입니다. 주소를 보면 누가 이 소켓에 접근할 수 있는지 짐작할 수 있습니다.

## TCP 수신 소켓 나열하기

Linux 실습 호스트에서 다음 읽기 전용 명령을 실행하세요. 옵션은 `ss`에 TCP 수신 소켓을 표시하고 주소와 포트를 숫자로 출력하도록 지정합니다.

```bash
$ ss -lnt
```

로컬 주소 열을 읽어 보세요. 아래 예시의 웹 미리 보기는 `127.0.0.1:8091`을 사용합니다. 포트 번호는 8091입니다. 주소는 호스트 자기 자신을 가리키는 **루프백** 주소입니다.

:::single-choice{#linux-listening-services-local-listener} 이 예시에서 같은 호스트의 브라우저로 미리 보기를 열려면 어느 주소를 사용해야 하나요?

::option[0.0.0.0:8091입니다.]{#linux-listening-services-local-listener-a explanation="이 표기는 어느 주소에서 연결을 받을지 지정하는 데 쓰입니다. 여기에 표시된 로컬 접속 대상은 별도입니다."}
::option[127.0.0.1:8091입니다.]{#linux-listening-services-local-listener-b .correct explanation="서비스가 이 루프백 주소와 포트에서 연결을 기다립니다."}
::option[관련 없는 서버의 80번 포트입니다.]{#linux-listening-services-local-listener-c explanation="예시의 수신 소켓은 자기 호스트의 8091번 포트를 사용합니다."}
:::

![실습용 루프백 8091번 포트의 수신 소켓을 보여 주는 LabEx ss 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-listening-services/loopback-listener.png)

## 모든 인터페이스의 의미 파악하기

IPv4 로컬 주소 `0.0.0.0:8091`은 서비스가 호스트의 모든 IPv4 인터페이스에서 연결을 기다린다는 뜻입니다. 다른 컴퓨터에서 도달할 수 있는 인터페이스도 포함될 수 있습니다. 수신 소켓 목록에서는 프로세스가 로컬에서 어떤 연결을 받는지 알 수 있습니다. 다른 컴퓨터에서 접근 가능한 범위는 방화벽 규칙과 네트워크 경로에 따라 제한될 수 있습니다.

:::single-choice{#linux-listening-services-all-interfaces} 서비스의 수신 주소가 127.0.0.1에서 0.0.0.0으로 바뀌고 포트는 그대로입니다. 무엇이 달라졌나요?

::option[더 많은 IPv4 인터페이스에서 연결을 기다릴 수 있습니다.]{#linux-listening-services-all-interfaces-a .correct explanation="들어오는 연결을 받을 수 있는 로컬 주소의 범위가 넓어졌습니다."}
::option[이제 다른 포트에서 연결을 기다립니다.]{#linux-listening-services-all-interfaces-b explanation="포트 번호는 그대로입니다."}
::option[모든 네트워크에서 즉시 접속할 수 있습니다.]{#linux-listening-services-all-interfaces-c explanation="접근할 수 있는 경로는 여전히 네트워크 규칙과 라우팅에 따라 달라집니다."}
:::

## 의도한 경로 확인하기

직원용 내부 서비스는 특정 네트워크에서만 사용하도록 구성할 수 있습니다. 그 네트워크에서 접근을 검증하세요. 제한이 적용되었다는 증거가 필요하면 네트워크 밖의 승인된 위치에서도 검사하세요. 수신 소켓과 경로를 모두 확인합니다. 로컬 소켓 목록만으로는 원격 클라이언트의 연결 결과를 알 수 없습니다.

:::single-choice{#linux-listening-services-verify-from-client} 수신 소켓이 모든 로컬 인터페이스에서 연결을 기다립니다. 직원의 워크스테이션에서 접속할 수 있는지 어떻게 확인하나요?

::option[호스트 이름을 다시 읽습니다.]{#linux-listening-services-verify-from-client-a explanation="호스트 이름을 읽어도 네트워크 경로를 검사할 수 없습니다."}
::option[수신 소켓이 몇 개인지 셉니다.]{#linux-listening-services-verify-from-client-b explanation="소켓 수만으로는 워크스테이션에서 접속할 수 있는지 알 수 없습니다."}
::option[직원 네트워크에서 승인된 요청을 보냅니다.]{#linux-listening-services-verify-from-client-c .correct explanation="실제로 사용하려는 경로를 검사할 수 있습니다."}
:::

Linux 호스트에서 연결을 기다리는 서비스를 확인하는 실습은 [DevSecOps를 위한 Linux 보안](https://labex.io/courses/linux-security-for-devsecops)의 수신 서비스 감사부터 시작하세요.

## 요약

이제 연결을 기다리는 주소를 읽고 어느 위치에서 접근을 검사할지 정할 수 있습니다.

1. 로컬 TCP 수신 소켓을 안전하게 나열합니다.
2. 루프백과 모든 IPv4 인터페이스를 구분합니다.
3. 해당 클라이언트의 위치에서 연결을 검증합니다.
