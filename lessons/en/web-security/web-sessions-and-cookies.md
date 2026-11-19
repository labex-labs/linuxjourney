---
lesson_id: "web-sessions-and-cookies"
course_id: "web-security"
lang: "en"
order_index: 5
title: "Sessions and Cookies"
description: "Learn how a cookie connects browser requests to a web session."
meta_title: "Sessions and Cookies - Web Security"
meta_description: "Learn how a cookie connects browser requests to a web session."
meta_keywords: "sessions and cookies, web security, cybersecurity, Linux Journey"
---

A browser often sends another request after a successful login. A **session** lets the application associate those requests with the signed-in account. One common approach uses a short identifier stored in a browser cookie.

## Following a Cookie

These examples are abridged. The response sends a cookie named `session` using a fake token for illustration.

```http
Set-Cookie: session=sample-token; Secure; HttpOnly; SameSite=Lax
```

A browser can then include the cookie in a later request that matches its rules.

```http
Cookie: session=sample-token
```

The server uses the token to look up the session it previously created.

:::single-choice{#web-sessions-and-cookies-direction} Which header carries the cookie value back in a matching request?

::option[Set-Cookie.]{#web-sessions-and-cookies-direction-a explanation="The server sends this header in the response to set the cookie."}
::option[Content-Type.]{#web-sessions-and-cookies-direction-c explanation="That header describes the message body's format."}
::option[Cookie.]{#web-sessions-and-cookies-direction-b .correct explanation="The browser includes this request header when the rules match."}
:::

## Reading the Attributes

`Secure` restricts ordinary transmission of the cookie to HTTPS. `HttpOnly` tells browser page scripts that they cannot read it through the usual cookie API. `SameSite` controls when the browser includes it in requests initiated from another site. Each setting applies to a different part of browser behavior.

:::single-choice{#web-sessions-and-cookies-secure-attribute} Which attribute tells the browser to restrict transmission of this cookie to HTTPS?

::option[HttpOnly.]{#web-sessions-and-cookies-secure-attribute-b explanation="This restricts page script access to the cookie."}
::option[Secure.]{#web-sessions-and-cookies-secure-attribute-a .correct explanation="This attribute applies to the protected transport used for the cookie."}
::option[The name session.]{#web-sessions-and-cookies-secure-attribute-c explanation="A cookie's name is a label chosen by the application."}
:::

## Ending a Session

When a user signs out, the service can invalidate the session on the server and ask the browser to remove its stored cookie. Server-side invalidation matters because a browser may still briefly have an older value. Treat a real session token like a credential and leave it out of screenshots and shared logs.

:::single-choice{#web-sessions-and-cookies-after-sign-out} What should happen when an invalidated session token reaches the server again?

::option[The server should treat it as unauthenticated.]{#web-sessions-and-cookies-after-sign-out-c .correct explanation="The server-side session associated with the value is no longer valid."}
::option[The server should restore the old session automatically.]{#web-sessions-and-cookies-after-sign-out-a explanation="The old session ended."}
::option[The server should accept it because the cookie still has a name.]{#web-sessions-and-cookies-after-sign-out-b explanation="A cookie's name does not make its value valid."}
:::

## Summary

You can now follow a session cookie between a browser and a service.

1. Identify the header that sets a cookie and the header that sends it back.
2. Explain the purpose of common cookie attributes.
3. Describe how server-side invalidation ends a session.
