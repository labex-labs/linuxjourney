---
index: 3
lang: "ko"
title: "간단한 HTTP 서버"
meta_title: "간단한 HTTP 서버 - 네트워크 공유"
meta_description: "Python 의 http.server 모듈을 사용하여 간단한 HTTP 서버를 만드는 방법을 배우십시오. 이 초보자 친화적인 Linux 튜토리얼을 통해 네트워크에서 파일을 빠르게 공유하십시오."
meta_keywords: "http.server, SimpleHTTPServer, Python 웹 서버, 파일 공유, Linux 튜토리얼, 초보자 가이드"
---

## Lesson Content

Python 에는 HTTP 를 통해 파일을 제공하는 데 매우 유용한 도구가 있습니다. 이는 네트워크의 다른 머신이 액세스할 수 있는 빠른 네트워크 공유를 생성하려는 경우에 유용합니다. 이를 위해 공유하려는 디렉토리로 이동하여 다음을 실행하십시오:

```bash
python -m http.server
```

또는 Python 2 를 사용하는 경우:

```bash
python -m SimpleHTTPServer
```

이렇게 하면 localhost 주소를 통해 액세스할 수 있는 기본 웹 서버가 설정됩니다. 따라서 이 서버를 실행한 머신의 IP 주소를 가져와서 다른 머신에서 브라우저에 `http://IP_ADDRESS:8000`을 입력하여 액세스하십시오. 자신의 머신에서는 웹 브라우저에 `http://localhost:8000`을 입력하여 사용 가능한 파일을 볼 수 있습니다.

## Exercise

연습하면 완벽해집니다! 다음은 네트워크를 통해 파일을 공유하는 데 필수적인 네트워크 연결 및 IP 주소 지정에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/linux-explore-ip-address-types-and-reachability-in-linux-592780)** - Python HTTP 서버에 액세스할 수 있는지 확인하는 데 중요한 다양한 IP 주소 유형을 식별하고 네트워크 도달 가능성을 테스트하는 연습을 하십시오.
2. **[Linux 에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/linux-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 머신의 IP 주소를 찾는 방법을 배우십시오. 이는 다른 장치에서 공유 파일에 액세스하기 전에 필요한 단계입니다.
3. **[Linux 에서 로컬 호스트 이름 확인 관리](https://labex.io/ko/labs/linux-manage-local-hostname-resolution-in-linux-592792)** - /etc/hosts 파일을 편집하여 Linux 에서 로컬 호스트 이름 확인을 관리하는 방법을 배우십시오. 이는 웹 개발 및 네트워크 테스트를 위한 핵심 기술입니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux 에서 기본 네트워크 작업에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

Python 으로 간단한 HTTP 서버를 생성하는 데 사용할 수 있는 도구는 무엇입니까?

## Quiz Answer

http.server
