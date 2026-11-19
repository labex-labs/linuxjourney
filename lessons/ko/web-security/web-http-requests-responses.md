---
lesson_id: "web-http-requests-responses"
course_id: "web-security"
lang: "ko"
order_index: 1
title: "HTTP 요청과 응답"
description: "HTTP 통신에서 메서드, 경로, 상태, 콘텐츠 유형을 읽는 방법을 알아봅니다."
meta_title: "HTTP 요청과 응답 - 웹 보안"
meta_description: "HTTP 통신에서 메서드, 경로, 상태, 콘텐츠 유형을 읽는 방법을 알아봅니다."
meta_keywords: "HTTP 요청과 응답, 웹 보안, 사이버 보안, Linux Journey"
---

브라우저나 다른 클라이언트는 **HTTP 요청**을 보내 웹 서버에 필요한 것을 요청합니다. 서버는 **HTTP 응답**을 반환합니다. 두 메시지를 읽으면 무엇을 요청했고 서버가 무엇을 반환했는지 알 수 있습니다.

## 요청 읽기

아래는 짧은 HTTP/1.1 요청입니다. `GET`은 메서드로, 클라이언트가 요청하는 작업을 나타냅니다. `/health`는 경로입니다. `Host` 헤더는 클라이언트가 요청을 보내는 웹사이트를 나타냅니다.

```http
GET /health HTTP/1.1
Host: site.example
```

**헤더**는 메시지에 관한 정보를 담는 이름 있는 값입니다. 메서드와 경로는 요청의 첫 줄에 나옵니다.

:::single-choice{#web-http-requests-responses-request-path} 이 클라이언트는 서버에 무엇을 가져오라고 요청하나요?

::option[이름이 HTTP/1.1인 파일입니다.]{#web-http-requests-responses-request-path-b explanation="이 필드는 프로토콜 버전입니다."}
::option[/health에 있는 리소스입니다.]{#web-http-requests-responses-request-path-a .correct explanation="경로는 첫 줄의 GET 뒤에 나옵니다."}
::option[/site.example에 있는 리소스입니다.]{#web-http-requests-responses-request-path-c explanation="Host 헤더는 사이트를 식별합니다. 요청 경로는 첫 줄에 따로 나옵니다."}
:::

## 응답 읽기

빈 실습 폴더에서 페이지를 만들고 루프백 주소에 Python HTTP 서버를 시작하세요. 리디렉션으로 페이지 파일을 작성합니다. 요청을 마칠 때까지 이 터미널에서 서버를 실행해 두세요. 그런 다음 Ctrl+C로 서버를 종료합니다.

```bash
$ mkdir web-demo
$ printf '%s\n' ready > web-demo/health.txt
$ python3 -m http.server 8094 --bind 127.0.0.1 --directory web-demo
```

같은 장비의 두 번째 터미널에서 `curl -i`를 실행하세요. 이 옵션을 사용하면 응답 내용 앞에 응답 헤더도 표시됩니다.

```bash
$ curl -i http://127.0.0.1:8094/health.txt
```

응답의 첫 줄에는 **상태 코드**가 나옵니다. `200`은 이 요청이 성공했다는 뜻입니다. 빈 줄이 헤더와 본문을 구분합니다. `Content-Type`은 클라이언트에 본문을 일반 텍스트 등 어떤 형식으로 해석해야 하는지 알려 줍니다.

:::single-choice{#web-http-requests-responses-response-parts} 클라이언트가 콘텐츠를 어떻게 표시할지 판단하는 데 어느 부분이 도움이 되나요?

::option[응답의 Content-Type 헤더입니다.]{#web-http-requests-responses-response-parts-b .correct explanation="이 헤더는 응답 본문의 유형을 나타냅니다."}
::option[원래 요청에 들어 있는 호스트 이름입니다.]{#web-http-requests-responses-response-parts-a explanation="이 값은 클라이언트가 접속한 사이트를 나타냅니다."}
::option[경로만 확인하면 됩니다.]{#web-http-requests-responses-response-parts-c explanation="경로는 리소스를 식별하지만 반환되는 콘텐츠의 형식을 지정하지 않습니다."}
:::

![상태 200, 텍스트 콘텐츠 유형, ready 본문을 보여 주는 LabEx HTTP 응답](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-http-requests-responses/http-response.png)

## 두 결과 비교하기

`404` 응답은 서버가 요청한 리소스를 찾지 못했거나 공개하지 않았음을 나타냅니다. 한 경로에서는 200을 반환하고 다른 경로에서는 404를 반환할 수 있습니다. 결과를 비교할 때는 정확한 메서드와 경로를 확인하세요.

:::single-choice{#web-http-requests-responses-health-scope} /health 요청에서 200을 받았습니다. /welcome에 관해 무엇을 알 수 있나요?

::option[/welcome도 200을 반환했습니다.]{#web-http-requests-responses-health-scope-a explanation="예시에서는 다른 경로를 검사했습니다."}
::option[호스트에 접속할 수 없었습니다.]{#web-http-requests-responses-health-scope-b explanation="상태 확인 요청에 대한 응답이 도착했습니다."}
::option[결과를 알려면 /welcome에 요청을 보내야 합니다.]{#web-http-requests-responses-health-scope-c .correct explanation="두 경로에서 서로 다르게 동작할 수 있습니다."}
:::

응답 헤더와 연결 상태를 확인하는 연습은 [Linux에서 curl로 서버 연결 확인하기](https://labex.io/tutorials/linux-how-to-test-server-connectivity-with-curl-in-linux-415082)를 참고하세요.

## 요약

이제 간단한 HTTP 통신의 주요 부분을 읽을 수 있습니다.

1. 요청에서 메서드, 경로, 호스트를 찾습니다.
2. 응답의 상태와 콘텐츠 유형을 읽습니다.
3. 실제로 보낸 요청의 결과를 설명합니다.
