---
lesson_id: "compose-service-discovery"
course_id: "docker-compose"
lang: "ko"
order_index: 3
title: "서비스 검색"
description: "Compose 서비스가 이름으로 서로 연결하고, 호스트에서는 공개된 포트로 연결하는 방법을 알아봅니다."
meta_title: "서비스 검색 - Docker Compose"
meta_description: "Compose 서비스가 이름으로 서로 연결하고, 호스트에서는 공개된 포트로 연결하는 방법을 알아봅니다."
meta_keywords: "서비스 검색, Compose 네트워크, 공개 포트, Docker Compose, DevOps, Linux Journey"
---

Docker 호스트의 브라우저는 공개 주소를 통해 웹 서비스에 접속합니다. 같은 프로젝트의 다른 컨테이너는 다른 경로를 사용합니다. Compose는 보통 같은 프로젝트의 서비스를 공용 네트워크에 연결합니다. 서비스는 이 네트워크에서 상대를 이름으로 찾을 수 있습니다.

## 도구 컨테이너에서 페이지 요청하기

`compose.yaml`이 있는 실습 폴더로 돌아갑니다. 이전 레슨 이후에 도구 컨테이너가 종료됐다면 `docker compose start toolbox`로 다시 시작합니다. 두 서비스가 모두 실행 중일 때 `docker compose exec`로 기존 도구 컨테이너 안에서 명령을 실행합니다. BusyBox의 `wget` 명령으로 페이지를 요청합니다. `-q` 옵션은 진행 메시지를 숨기고 `-O -`는 페이지 내용을 터미널에 출력합니다.

```bash
$ docker compose exec -T toolbox wget -q -O - http://web:80/
```

`-T` 옵션은 대화형 터미널을 할당하지 않도록 합니다. URL에는 웹 서비스 이름과 컨테이너 포트가 들어 있습니다. 요청이 성공하면 Nginx 페이지의 HTML을 받습니다.

:::single-choice{#compose-service-discovery-sibling-url} 같은 Compose 네트워크를 쓰는 다른 서비스는 어떤 주소로 웹 컨테이너에 연결해야 하나요?

::option[`http://web:80/`]{#compose-service-discovery-sibling-url-c .correct explanation="공용 네트워크에서 web은 대상 서비스를 가리키며, 프로그램은 80번 포트에서 요청을 받습니다."}
::option[`http://127.0.0.1:8080/`]{#compose-service-discovery-sibling-url-a explanation="이 루프백 주소는 요청을 보내는 서비스 자신의 네트워크 환경을 가리킵니다."}
::option[`http://web:8080/`]{#compose-service-discovery-sibling-url-b explanation="이 예시에서 웹 프로그램은 네트워크 안에서 80번 포트로 요청을 받습니다."}
:::

![서비스 이름으로 웹 페이지를 요청한 뒤 도구 컨테이너에 반환된 HTML](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-discovery/internal-request.png)

## 호스트에서 접속할 주소 고르기

원래 포트 매핑을 유지했다면 Docker 호스트에서 `http://127.0.0.1:8080/`을 엽니다. 이전 레슨에서 호스트 포트를 바꿨다면 브라우저 주소에도 그 포트를 사용합니다. 도구 컨테이너는 계속 `http://web:80/`을 사용합니다. 서비스 이름 `web`이 통하는 Compose 네트워크 안에서 연결하기 때문입니다.

:::single-choice{#compose-service-discovery-host-url} 매핑의 호스트 쪽 포트를 8081로 바꿨다고 가정해 봅시다. 예시의 어느 주소를 함께 바꿔야 하나요?

::option[도구 컨테이너가 web의 80번 포트에 접속하는 URL입니다.]{#compose-service-discovery-host-url-b explanation="이 연결은 계속 웹 컨테이너가 요청을 받는 포트로 바로 이어집니다."}
::option[예시의 두 주소 모두입니다.]{#compose-service-discovery-host-url-c explanation="호스트 쪽 포트만 바뀌었습니다."}
::option[호스트의 브라우저가 사용하는 주소입니다.]{#compose-service-discovery-host-url-a .correct explanation="브라우저는 호스트에 새로 공개된 포트를 통해 연결합니다."}
:::

## 서비스 이름 계속 사용하기

컨테이너를 교체하면 네트워크 주소가 바뀔 수 있습니다. Compose의 서비스 이름은 그대로 유지됩니다. 클라이언트는 다시 이름으로 주소를 찾아 연결할 수 있습니다. 교체한 컨테이너에 열려 있던 연결은 끊어질 수 있습니다.

:::single-choice{#compose-service-discovery-replacement} 웹 컨테이너를 다시 만들면서 주소가 바뀌었습니다. 도구 컨테이너는 다음 요청에 무엇을 사용할 수 있나요?

::option[기존 컨테이너에서 복사해 둔 예전 주소입니다.]{#compose-service-discovery-replacement-a explanation="새 컨테이너에는 다른 네트워크 주소가 할당될 수 있습니다."}
::option[같은 웹 서비스 이름과 컨테이너 포트입니다.]{#compose-service-discovery-replacement-b .correct explanation="프로젝트 네트워크에서 이름을 조회하면 현재 컨테이너를 찾을 수 있습니다."}
::option[도구 컨테이너 자신의 이름입니다.]{#compose-service-discovery-replacement-c explanation="이 이름은 요청을 보내는 쪽을 가리킵니다."}
:::

## 요약

이제 요청하는 위치에 맞는 주소를 고를 수 있습니다.

1. 프로젝트 네트워크에서는 서비스 이름과 컨테이너 포트를 사용합니다.
2. 호스트 브라우저에서는 공개된 주소를 사용합니다.
3. 컨테이너를 교체한 뒤 서비스 이름을 다시 조회합니다.
