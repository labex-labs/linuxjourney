---
index: 3
lang: "ko"
title: "간단한 HTTP 서버"
meta_title: "간단한 HTTP 서버 - 네트워크 공유"
meta_description: "Python 의 http.server 모듈을 사용하여 Linux 에서 간단한 HTTP 서버를 빠르게 설정하는 방법을 알아보세요. 이 가이드는 네트워크 전반에서 쉬운 파일 공유를 위한 간단한 Linux 웹 서버를 만드는 방법을 설명합니다."
meta_keywords: "리눅스 간단한 http 서버, 간단한 http 서버 리눅스, 간단한 리눅스 웹 서버, 파이썬 http.server, 파이썬 simplehttpserver 란, 파일 공유, 네트워크 서버"
---

## Lesson Content

Python 에는 네트워크를 통해 파일을 공유하는 데 매우 유용한, 즉시 웹 서버를 생성할 수 있는 내장 모듈이 있습니다. **리눅스 간단한 http 서버**를 설정하는 것은 단 하나의 명령만 필요하며 간단한 과정입니다.

### 리눅스에서 간단한 HTTP 서버 시작하기

시작하려면, 터미널을 사용하여 공유하려는 디렉터리로 이동합니다. 원하는 디렉터리로 이동한 후, Python 3 를 사용하는 경우 다음 명령어로 **간단한 http 서버 리눅스** 환경을 시작할 수 있습니다:

```bash
python -m http.server
```

이 명령은 기본 웹 서버를 실행하여 현재 디렉터리의 내용을 HTTP 를 통해 접근 가능하게 만듭니다.

### Python 2 용 레거시 방법

여전히 Python 2 를 사용하는 구형 시스템의 경우 명령어가 약간 다릅니다. 이 모듈은 이전에 `SimpleHTTPServer`라고 불렸습니다. **what is python simplehttpserver**가 무엇인지 궁금했다면, 이는 단순히 Python 2 버전의 `http.server` 모듈입니다. 다음을 사용하여 실행할 수 있습니다:

```bash
python -m SimpleHTTPServer
```

### 간단한 리눅스 웹 서버 액세스하기

명령을 실행한 후, **간단한 리눅스 웹 서버**가 활성화됩니다. 동일 네트워크의 다른 컴퓨터에서 웹 브라우저를 열고 서버를 실행하는 컴퓨터의 로컬 IP 로 `IP_ADDRESS`를 대체하여 `http://IP_ADDRESS:8000`으로 이동하여 공유된 파일에 액세스할 수 있습니다.

동일한 컴퓨터에서 파일을 보려면 로컬 호스트 주소인 `http://localhost:8000`을 사용할 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 네트워크를 통해 파일을 공유하는 데 필수적인 네트워크 연결 및 IP 주소 지정에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[리눅스에서 IP 주소 유형 및 도달 가능성 탐색](https://labex.io/ko/labs/comptia-explore-ip-address-types-and-reachability-in-linux-592780)** - 다양한 IP 주소 유형을 식별하고 네트워크 도달 가능성을 테스트하는 연습을 통해 Python HTTP 서버가 액세스 가능한지 확인합니다.
2. **[리눅스에서 MAC 및 IP 주소 식별](https://labex.io/ko/labs/comptia-identify-mac-and-ip-addresses-in-linux-592731)** - `ip a` 명령을 사용하여 컴퓨터의 IP 주소를 찾는 방법을 배우고, 이는 다른 장치에서 공유 파일에 액세스하기 위한 필수 단계입니다.
3. **[리눅스에서 로컬 호스트 이름 확인 관리](https://labex.io/ko/labs/comptia-manage-local-hostname-resolution-in-linux-592792)** - /etc/hosts 파일을 편집하여 리눅스에서 로컬 호스트 이름 확인을 관리하는 방법을 배우며, 이는 웹 개발 및 네트워크 테스트에 핵심적인 기술입니다.

이 랩들은 실제 시나리오에서 개념을 적용하고 리눅스 기본 네트워크 작업에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

Python 3 의 경우, 간단한 HTTP 서버를 만드는 데 사용되는 모듈의 이름은 무엇입니까? (대소문자를 구분하여 영어로 답변해 주십시오).

## Quiz Answer

http.server
