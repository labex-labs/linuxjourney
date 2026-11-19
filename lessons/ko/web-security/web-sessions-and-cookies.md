---
lesson_id: "web-sessions-and-cookies"
course_id: "web-security"
lang: "ko"
order_index: 5
title: "세션과 쿠키"
description: "쿠키가 브라우저 요청을 웹 세션과 연결하는 방식을 알아봅니다."
meta_title: "세션과 쿠키 - 웹 보안"
meta_description: "쿠키가 브라우저 요청을 웹 세션과 연결하는 방식을 알아봅니다."
meta_keywords: "세션과 쿠키, 웹 보안, 사이버 보안, Linux Journey"
---

브라우저는 로그인에 성공한 뒤에도 요청을 보냅니다. 애플리케이션은 **세션**을 사용해 이러한 요청을 로그인한 계정에 연결합니다. 흔히 브라우저의 쿠키에 짧은 식별자를 저장하는 방식을 사용합니다.

## 쿠키가 오가는 과정 살펴보기

아래 예시는 일부만 보여 줍니다. 응답에는 `session`이라는 쿠키가 들어 있으며, 설명을 위해 가짜 토큰을 사용합니다.

```http
Set-Cookie: session=sample-token; Secure; HttpOnly; SameSite=Lax
```

이후 브라우저는 쿠키의 조건에 맞는 요청에 이 쿠키를 포함할 수 있습니다.

```http
Cookie: session=sample-token
```

서버는 토큰을 사용해 앞서 만들었던 세션을 찾습니다.

:::single-choice{#web-sessions-and-cookies-direction} 조건에 맞는 요청에서 쿠키 값을 서버로 돌려보내는 헤더는 무엇인가요?

::option[Set-Cookie입니다.]{#web-sessions-and-cookies-direction-a explanation="서버는 쿠키를 설정하기 위해 응답에 이 헤더를 넣습니다."}
::option[Content-Type입니다.]{#web-sessions-and-cookies-direction-c explanation="이 헤더는 메시지 본문의 형식을 나타냅니다."}
::option[Cookie입니다.]{#web-sessions-and-cookies-direction-b .correct explanation="조건에 맞으면 브라우저가 이 요청 헤더를 포함합니다."}
:::

## 쿠키 속성 읽기

`Secure`는 쿠키의 일반적인 전송을 HTTPS로 제한합니다. `HttpOnly`는 웹 페이지의 스크립트가 일반적인 쿠키 API를 통해 쿠키를 읽지 못하게 합니다. `SameSite`는 다른 사이트에서 시작한 요청에 브라우저가 언제 쿠키를 포함할지 제어합니다. 각 속성은 브라우저 동작의 서로 다른 부분에 적용됩니다.

:::single-choice{#web-sessions-and-cookies-secure-attribute} 쿠키를 HTTPS로만 전송하도록 브라우저에 지시하는 속성은 무엇인가요?

::option[HttpOnly입니다.]{#web-sessions-and-cookies-secure-attribute-b explanation="이 속성은 페이지 스크립트의 쿠키 접근을 제한합니다."}
::option[Secure입니다.]{#web-sessions-and-cookies-secure-attribute-a .correct explanation="이 속성은 쿠키를 전송할 때 사용하는 연결의 보호 여부에 적용됩니다."}
::option[쿠키 이름 session입니다.]{#web-sessions-and-cookies-secure-attribute-c explanation="쿠키 이름은 애플리케이션이 정한 식별자입니다."}
:::

## 세션 끝내기

사용자가 로그아웃하면 서비스는 서버에서 세션을 무효화하고 브라우저에 저장된 쿠키를 삭제하도록 요청할 수 있습니다. 브라우저에 이전 값이 잠시 남아 있을 수 있으므로 서버에서 세션을 무효화하는 것이 중요합니다. 실제 세션 토큰은 자격 증명으로 취급하고 스크린샷이나 공유 로그에 넣지 마세요.

:::single-choice{#web-sessions-and-cookies-after-sign-out} 서버가 무효화된 세션 토큰을 다시 받으면 어떻게 처리해야 하나요?

::option[인증되지 않은 요청으로 처리합니다.]{#web-sessions-and-cookies-after-sign-out-c .correct explanation="이 값에 연결된 서버 측 세션은 더 이상 유효하지 않습니다."}
::option[이전 세션을 자동으로 복원합니다.]{#web-sessions-and-cookies-after-sign-out-a explanation="이전 세션은 이미 끝났습니다."}
::option[쿠키에 이름이 있으므로 서버가 이 요청을 인증합니다.]{#web-sessions-and-cookies-after-sign-out-b explanation="쿠키에 이름이 있어도 값이 유효하다는 뜻은 아닙니다."}
:::

## 요약

이제 브라우저와 서비스 사이에서 세션 쿠키가 오가는 흐름을 추적할 수 있습니다.

1. 쿠키를 설정하는 헤더와 쿠키를 돌려보내는 헤더를 구분합니다.
2. 자주 쓰는 쿠키 속성의 용도를 설명합니다.
3. 서버 측 무효화로 세션이 끝나는 과정을 설명합니다.
