---
lesson_id: "web-https"
course_id: "web-security"
lang: "ko"
order_index: 2
title: "HTTPS"
description: "웹 요청에서 HTTPS로 보호되는 부분을 식별하는 방법을 알아봅니다."
meta_title: "HTTPS - 웹 보안"
meta_description: "웹 요청에서 HTTPS로 보호되는 부분을 식별하는 방법을 알아봅니다."
meta_keywords: "HTTPS, 웹 보안, 사이버 보안, Linux Journey"
---

HTTP는 브라우저와 서버가 주고받는 메시지의 형식을 정합니다. HTTPS는 **TLS**를 통해 같은 메시지를 전송합니다. TLS는 연결을 보호하고 브라우저가 서버의 신원을 확인할 수 있게 해 주는 프로토콜입니다.

## 보호되는 연결 확인하기

브라우저가 `https://site.example`에 접속한다고 생각해 보세요. TLS 연결을 맺은 뒤에는 브라우저와 서버가 암호화된 HTTP 메시지를 주고받을 수 있습니다. 이 네트워크 구간을 관찰하는 사람이 HTTP 본문을 그대로 읽거나 탐지되지 않은 채 변경하기는 어렵습니다.

```text
Browser  ===== HTTPS connection =====  Website server
```

브라우저는 서버가 제시한 신원도 검증해야 합니다.

:::single-choice{#web-https-protected-hop} 이 간단한 구성에서 HTTPS는 무엇을 보호하나요?

::option[브라우저가 이미 표시한 페이지입니다.]{#web-https-protected-hop-b explanation="브라우저는 응답을 복호화한 뒤 페이지를 읽습니다."}
::option[웹사이트에 저장한 모든 백업입니다.]{#web-https-protected-hop-c explanation="백업 보호는 별도로 다뤄야 합니다."}
::option[보호되는 연결을 통해 주고받는 HTTP 메시지입니다.]{#web-https-protected-hop-a .correct explanation="TLS는 연결의 양쪽 끝 사이에서 전송 중인 메시지를 보호합니다."}
:::

## 연결이 여러 구간을 거칠 때 확인하기

프록시는 브라우저의 요청을 받아 다른 서버에 전달할 수 있습니다. 프록시가 TLS 연결을 종료하는 지점이면 요청을 전달하기 전에 내용을 읽을 수 있습니다. 다음 연결 구간에도 별도의 보호가 필요하므로 연결을 하나씩 확인하세요.

```text
Browser  === HTTPS ===  Proxy  --- HTTP ---  Internal server
```

이 그림에서 외부 연결은 TLS를 사용합니다. 내부 연결은 암호화되지 않은 HTTP를 사용합니다.

:::single-choice{#web-https-inner-hop} 어느 구간을 별도로 변경해야 TLS로 보호할 수 있나요?

::option[브라우저에서 프록시까지입니다.]{#web-https-inner-hop-a explanation="이 구간에는 이미 HTTPS가 표시되어 있습니다."}
::option[프록시에서 내부 서버까지입니다.]{#web-https-inner-hop-b .correct explanation="그림의 내부 구간은 암호화되지 않은 HTTP를 사용합니다."}
::option[사이트를 요청한 적 없는 브라우저 탭입니다.]{#web-https-inner-hop-c explanation="그림에서 이 탭에 해당하는 연결은 없습니다."}
:::

## 애플리케이션의 접근 권한 확인하기

유효한 보안 연결은 서버의 신원을 확인하는 데 도움이 되고 전송 중인 메시지를 보호합니다. 어느 계정이 페이지를 읽거나 설정을 바꿀 수 있는지는 애플리케이션이 결정합니다. 비공개 페이지에 강력한 TLS를 적용하더라도 애플리케이션 접근 정책은 여전히 필요합니다.

:::single-choice{#web-https-access-vs-transport} 비공개 계정 페이지를 반환하기 전에 서비스는 무엇을 확인해야 하나요?

::option[인증된 계정에 해당 페이지를 읽을 권한이 있는지 확인합니다.]{#web-https-access-vs-transport-c .correct explanation="애플리케이션의 인가 정책은 계정이 어디까지 접근할 수 있는지 정합니다."}
::option[TLS를 사용 중인지만 확인합니다.]{#web-https-access-vs-transport-a explanation="HTTPS는 메시지 교환을 보호합니다. 서비스는 접근 권한도 판단해야 합니다."}
::option[인증서가 요청한 호스트 이름을 포함하는지만 확인합니다.]{#web-https-access-vs-transport-b explanation="인증서는 서버의 신원을 확인하는 데 쓰입니다. 비공개 페이지의 접근 권한은 애플리케이션이 정합니다."}
:::

## 요약

이제 웹 요청이 거치는 경로에서 HTTPS가 무엇을 보호하는지 설명할 수 있습니다.

1. TLS가 시작되고 끝나는 지점을 확인합니다.
2. 프록시가 요청을 전달하면 각 구간의 연결을 확인합니다.
3. 애플리케이션에 접근 제어가 필요한 이유를 이해합니다.
