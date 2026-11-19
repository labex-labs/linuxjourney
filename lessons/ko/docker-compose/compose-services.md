---
lesson_id: "compose-services"
course_id: "docker-compose"
lang: "ko"
order_index: 2
title: "Compose 서비스"
description: "Compose 서비스를 시작하고 컨테이너 상태를 확인하는 방법을 알아봅니다."
meta_title: "Compose 서비스 - Docker Compose"
meta_description: "Compose 서비스를 시작하고 컨테이너 상태를 확인하는 방법을 알아봅니다."
meta_keywords: "Compose 서비스, 컨테이너 상태, Docker Compose, DevOps, Linux Journey"
---

이전 레슨에서 `web`과 `toolbox`를 정의한 `compose.yaml`을 사용합니다. 두 서비스는 같은 Compose **프로젝트**에 속합니다. 프로젝트는 한 설정으로 함께 관리하는 리소스의 묶음입니다. 실습 폴더에서 명령을 실행하세요.

## 프로젝트 시작하기

8080번 포트를 이미 사용 중이라면 `compose.yaml`에서 빈 호스트 포트를 선택하세요. 예를 들어 Docker 과정의 `published-web` 컨테이너는 실행하는 동안 8080번 포트를 사용합니다. 이를 계속 실행한 채 8081번 포트가 비어 있다면 Compose의 매핑을 `127.0.0.1:8081:80`으로 설정할 수 있습니다. 컨테이너 쪽 포트는 80번으로 유지하고, 이후 브라우저 요청에서는 선택한 호스트 포트를 사용합니다.

`docker compose up -d`로 서비스를 백그라운드에서 시작합니다. Compose는 프로젝트에 필요한 리소스를 준비하고 서비스 설정에 따라 컨테이너를 만들거나 갱신합니다.

```bash
$ docker compose up -d
```

:::single-choice{#compose-services-project-start} 이 실습 폴더에서 up -d를 실행합니다. 무엇을 시작할지는 어떤 설정으로 결정하나요?

::option[Docker 호스트에서 쓸 수 있는 모든 이미지입니다.]{#compose-services-project-start-a explanation="호스트에는 이 프로젝트와 관계없는 이미지도 있을 수 있습니다."}
::option[현재 중지된 모든 컨테이너입니다.]{#compose-services-project-start-c explanation="Compose는 시작하도록 지정한 프로젝트를 다룹니다."}
::option[선택한 Compose 파일의 서비스입니다.]{#compose-services-project-start-b .correct explanation="이 예에서 Compose는 web과 toolbox의 정의를 사용합니다."}
:::

## 서비스 목록 읽기

`docker compose ps`로 프로젝트를 확인합니다. 서비스 열에는 YAML 파일에 적은 이름이 나옵니다. Docker는 각 컨테이너에도 이름을 부여하며, 컨테이너 이름에 프로젝트 이름이 들어갈 수 있습니다.

```bash
$ docker compose ps
```

`web`과 `toolbox`를 찾아 상태를 확인합니다. 컨테이너가 실행 중이면 확인한 시점에 프로그램이 동작 중이라는 뜻입니다. 웹 응답은 브라우저에서 요청을 보내 따로 확인하세요.

:::single-choice{#compose-services-compose-list} Compose에 web이 실행 중이라고 나옵니다. 예상한 페이지를 반환하는지 직접 확인하려면 어떻게 해야 하나요?

::option[config가 표시한 서비스 수를 셉니다.]{#compose-services-compose-list-b explanation="설정에 있는 서비스 수로는 웹 응답을 알 수 없습니다."}
::option[공개된 웹 주소로 요청을 보냅니다.]{#compose-services-compose-list-a .correct explanation="요청을 보내면 실제로 어떤 페이지를 받는지 확인할 수 있습니다."}
::option[다른 컨테이너의 이름을 확인합니다.]{#compose-services-compose-list-c explanation="이름은 컨테이너를 식별하지만 서비스가 응답하는지는 알려 주지 않습니다."}
:::

![web과 toolbox가 실행 중이고 호스트의 8080번 포트가 공개된 Compose 상태 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-services/project-status.png)

스크린샷은 원래 호스트 포트인 8080번을 사용합니다. 다른 포트를 선택했다면 매핑의 호스트 쪽에서 해당 번호를 찾으세요.

## 중지된 서비스 확인하기

도구 컨테이너는 실습 중 잠시 사용합니다. 대기가 끝나거나 직접 중지했다면 `-a`를 추가해 Compose 목록에 중지된 컨테이너도 표시할 수 있습니다. 아래 예시는 웹 서비스는 그대로 두고 이 실습 프로젝트의 도구 컨테이너만 중지합니다. 과정을 계속할 때는 도구 컨테이너를 다시 시작하세요.

```bash
$ docker compose stop toolbox
$ docker compose ps -a
$ docker compose start toolbox
```

:::single-choice{#compose-services-stopped-service} toolbox를 중지한 뒤 어디에서 확인할 수 있나요?

::option[이 프로젝트의 docker compose ps -a 출력에서 확인합니다.]{#compose-services-stopped-service-c .correct explanation="이 옵션은 프로젝트에서 중지된 컨테이너도 표시합니다."}
::option[이미지 목록에서만 확인합니다.]{#compose-services-stopped-service-a explanation="실행 중인 프로그램을 중지해도 컨테이너가 남아 상태를 확인할 수 있습니다."}
::option[다른 프로젝트의 컨테이너 목록에서 확인합니다.]{#compose-services-stopped-service-b explanation="toolbox는 이 프로젝트에 속합니다."}
:::

컨테이너와 Compose를 더 연습하려면 [Docker 명령 실습](https://labex.io/courses/docker-command-labs)을 참고하세요.

## 요약

이제 Compose 파일을 사용해 여러 서비스를 시작하고 확인할 수 있습니다.

1. 선택한 프로젝트의 서비스를 시작합니다.
2. 서비스 이름과 현재 상태를 확인합니다.
3. 프로젝트를 조사할 때는 중지된 서비스도 확인합니다.
