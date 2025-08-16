---
title: "간단한 HTTP 서버"
description: "Python 의 http.server 모듈을 사용하여 간단한 HTTP 서버를 만드는 방법을 배우세요. 이 초보자 친화적인 Linux 튜토리얼을 통해 네트워크에서 파일을 빠르게 공유하세요."
keywords: "http.server, SimpleHTTPServer, Python 웹 서버, 파일 공유, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

Python 에는 HTTP 를 통해 파일을 제공하는 매우 유용한 도구가 있습니다. 이는 네트워크의 다른 컴퓨터가 액세스할 수 있는 빠른 네트워크 공유를 생성하려는 경우에 유용합니다. 그렇게 하려면 공유하려는 디렉토리로 이동하여 다음을 실행하십시오:

```bash
python -m http.server
```

또는 Python 2 를 사용 중인 경우:

```bash
python -m SimpleHTTPServer
```

이렇게 하면 localhost 주소를 통해 액세스할 수 있는 기본 웹 서버가 설정됩니다. 따라서 이 서버를 실행한 컴퓨터의 IP 주소를 가져와서 다른 컴퓨터에서 브라우저에서 `http://IP_ADDRESS:8000`으로 액세스하십시오. 자신의 컴퓨터에서는 웹 브라우저에 `http://localhost:8000`을 입력하여 사용 가능한 파일을 볼 수 있습니다.

## Exercise

`http.server`를 설정해 보세요!

## Quiz Question

Python 으로 간단한 HTTP 서버를 생성하는 데 사용할 수 있는 도구는 무엇입니까?

## Quiz Answer

http.server
