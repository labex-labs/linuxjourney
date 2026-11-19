---
lesson_id: "web-http-requests-responses"
course_id: "web-security"
lang: "en"
order_index: 1
title: "HTTP Requests and Responses"
description: "Learn to read the method, path, status, and content type in an HTTP exchange."
meta_title: "HTTP Requests and Responses - Web Security"
meta_description: "Learn to read the method, path, status, and content type in an HTTP exchange."
meta_keywords: "http requests and responses, web security, cybersecurity, Linux Journey"
---

A browser or another client asks a web server for something by sending an **HTTP request**. The server returns an **HTTP response**. Reading the two messages tells you what was requested and what the server returned.

## Reading the Request

Here is a short HTTP/1.1 request. `GET` is the method, which describes the action the client asks for. `/health` is the path. The `Host` header identifies which website the client addresses.

```http
GET /health HTTP/1.1
Host: site.example
```

A **header** is a named value that carries information about the message. The method and path appear on the request's first line.

:::single-choice{#web-http-requests-responses-request-path} What does this client ask the server to retrieve?

::option[A file named HTTP/1.1.]{#web-http-requests-responses-request-path-b explanation="That field is the protocol version."}
::option[The resource at /health.]{#web-http-requests-responses-request-path-a .correct explanation="The path appears after GET on the first line."}
::option[A resource at /site.example.]{#web-http-requests-responses-request-path-c explanation="The Host header identifies the website, not the path."}
:::

## Reading a Response

In an empty practice folder, create a page and start a Python HTTP server on loopback. The redirection writes the page. Leave this terminal running until the request finishes, then stop the server with Ctrl+C.

```bash
$ mkdir web-demo
$ printf '%s\n' ready > web-demo/health.txt
$ python3 -m http.server 8094 --bind 127.0.0.1 --directory web-demo
```

From a second terminal on the same machine, run `curl -i`. The option includes response headers before the response content.

```bash
$ curl -i http://127.0.0.1:8094/health.txt
```

A response begins with a **status code**. A `200` indicates success for this request. A blank line separates the headers from the body. `Content-Type` tells the client how to interpret the body, for example as plain text.

:::single-choice{#web-http-requests-responses-response-parts} Which part helps the client decide how to display the content?

::option[The response Content-Type header.]{#web-http-requests-responses-response-parts-b .correct explanation="It describes the type of the response body."}
::option[The hostname in the original request.]{#web-http-requests-responses-response-parts-a explanation="That names the site the client contacted."}
::option[The path alone.]{#web-http-requests-responses-response-parts-c explanation="The path identifies the resource and does not specify the returned format."}
:::

![Recorded LabEx HTTP response with status 200, a text content type, and the ready body](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/web-security/web-http-requests-responses/http-response.png)

## Comparing Two Results

A `404` response reports that the server did not find or disclose the requested resource. A page can return 200 on one path and 404 on another. Use the exact method and path when comparing outcomes.

:::single-choice{#web-http-requests-responses-health-scope} A request to /health gets 200. What can you conclude about /welcome?

::option[/welcome also returned 200.]{#web-http-requests-responses-health-scope-a explanation="The sample checked a different path."}
::option[The host could not be contacted.]{#web-http-requests-responses-health-scope-b explanation="A response arrived for the health check."}
::option[You need to request /welcome to learn its result.]{#web-http-requests-responses-health-scope-c .correct explanation="The two paths can have different behavior."}
:::

To practice checking response headers and connectivity, try [How to test server connectivity with curl in Linux](https://labex.io/tutorials/linux-how-to-test-server-connectivity-with-curl-in-linux-415082).

## Summary

You can now read the main parts of a simple HTTP exchange.

1. Find the method, path, and host in a request.
2. Read the status and content type in a response.
3. Describe the result for the exact request that was made.
