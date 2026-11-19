---
lesson_id: "web-https"
course_id: "web-security"
lang: "en"
order_index: 2
title: "HTTPS"
description: "Learn to identify the part of a web request protected by HTTPS."
meta_title: "HTTPS - Web Security"
meta_description: "Learn to identify the part of a web request protected by HTTPS."
meta_keywords: "https, web security, cybersecurity, Linux Journey"
---

HTTP defines the messages a browser and server exchange. HTTPS sends those same messages through **TLS**, a protocol that protects the connection and helps the browser verify the server.

## Identifying the Protected Connection

Imagine a browser connecting to `https://site.example`. After setting up TLS, the browser and server can exchange encrypted HTTP messages. Someone observing that part of the network cannot simply read the HTTP body or change it undetected.

```text
Browser  ===== HTTPS connection =====  Website server
```

The web browser must still validate the identity the server presents.

:::single-choice{#web-https-protected-hop} What does HTTPS protect in this simple setup?

::option[The page after the browser has already displayed it.]{#web-https-protected-hop-b explanation="The browser reads the page after decrypting the response."}
::option[Every backup stored by the website.]{#web-https-protected-hop-c explanation="Backup protection is a separate concern."}
::option[The HTTP messages sent along the protected connection.]{#web-https-protected-hop-a .correct explanation="TLS protects messages in transit between its endpoints."}
:::

## Reading a Multi-Hop Path

A proxy can receive a browser's request and forward it to a separate server. If the proxy ends TLS, it can read the request before passing it along. The next connection needs its own protection. Evaluating each connection matters.

```text
Browser  === HTTPS ===  Proxy  --- HTTP ---  Internal server
```

In this diagram the outer connection uses TLS. The inner connection is plain HTTP.

:::single-choice{#web-https-inner-hop} Which hop needs a separate change to gain TLS protection?

::option[The browser to the proxy.]{#web-https-inner-hop-a explanation="That hop already shows HTTPS."}
::option[The proxy to the internal server.]{#web-https-inner-hop-b .correct explanation="The illustrated inner hop uses plain HTTP."}
::option[A browser tab that never requests the site.]{#web-https-inner-hop-c explanation="That tab has no connection in the diagram."}
:::

## Keeping Access Decisions Separate

A valid secure connection helps you trust the server identity and protects messages in transit. The application still decides which account can read a page or change a setting. A private page can have strong TLS and still require an application access policy.

:::single-choice{#web-https-access-vs-transport} What should the service check before returning a private account page?

::option[Whether the authenticated account is allowed to read that page.]{#web-https-access-vs-transport-c .correct explanation="Application authorization controls what the account can access."}
::option[Only whether TLS is in use.]{#web-https-access-vs-transport-a explanation="HTTPS protects the exchange, while the service still needs an access decision."}
::option[Only whether the certificate covers the requested hostname.]{#web-https-access-vs-transport-b explanation="The certificate helps verify the server identity. The application still controls access to private pages."}
:::

## Summary

You can now describe what HTTPS protects along a web request's path.

1. Identify where TLS starts and ends.
2. Check each hop when a proxy forwards the request.
3. Recognize why the application still needs access controls.
