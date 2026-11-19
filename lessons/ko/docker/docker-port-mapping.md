---
lesson_id: "docker-port-mapping"
course_id: "docker"
lang: "ko"
order_index: 5
title: "포트 매핑"
description: "컨테이너 포트를 공개하고 로컬 브라우저가 사용할 주소를 찾는 방법을 배웁니다."
meta_title: "포트 매핑 - Docker"
meta_description: "Docker 포트 매핑에서 호스트 포트와 컨테이너 포트를 구분하고, 잘못된 포트로 요청했는지 확인합니다."
meta_keywords: "Docker 포트 매핑, 포트 공개, docker run -p, 호스트 포트, 컨테이너 포트"
---

웹 서버가 컨테이너 안에서 실행 중이어도 브라우저가 그 서버에 닿을 방법이 필요합니다. **포트**는 컴퓨터가 들어오는 네트워크 요청을 맞는 서비스로 보내도록 돕는 번호입니다. Docker는 호스트 포트를 공개하고 그곳에 온 요청을 컨테이너 내부의 포트로 전달할 수 있습니다.

## 포트 매핑 읽기

이 예제에서 Nginx는 컨테이너 내부의 80번 포트로 웹 요청을 받습니다. 앞서 만든 `web` 컨테이너에는 공개한 포트가 없었습니다. 이번에는 다른 이름을 붙인 컨테이너를 만들면서 `-p`로 매핑을 정합니다.

```bash
$ docker run -d --name published-web -p 127.0.0.1:8080:80 nginx:alpine
```

`8080:80`은 **호스트 포트** 8080에서 **컨테이너 포트** 80으로 전달한다는 뜻입니다. 브라우저는 호스트 포트에 연결하고 서버는 컨테이너 포트에서 요청을 받습니다. `127.0.0.1`은 매핑을 호스트의 루프백 주소, 즉 컴퓨터가 자기 자신에 접속할 때 쓰는 주소에 연결합니다.

외부와 분리된 연습 환경을 사용하세요. Docker Engine 28.0.0 이전 버전에서는 같은 로컬 네트워크 구간의 다른 컴퓨터에서도 localhost에 공개한 포트에 접속할 수 있는 경우가 있습니다. [Docker의 포트 공개](https://docs.docker.com/engine/network/port-publishing/)

:::single-choice{#docker-port-mapping-request-target} `127.0.0.1:9090:80`에서 Docker 호스트의 브라우저는 어느 포트에 연결해야 하나요?

::option[호스트의 9090번 포트.]{#docker-port-mapping-target-outer .correct explanation="가운데 숫자는 브라우저가 연결할 호스트 포트를 지정합니다."}
::option[호스트의 80번 포트.]{#docker-port-mapping-target-inner explanation="80번 포트는 컨테이너 내부의 목적지입니다."}
::option[컨테이너 내부의 9090번 포트.]{#docker-port-mapping-target-wrong-side explanation="이 예제에서 서버는 컨테이너 내부의 80번 포트로 요청을 받습니다."}
:::

## 호스트에서 테스트하기

Docker가 포트를 공개한 컴퓨터의 브라우저에서 `http://127.0.0.1:8080`을 엽니다. Docker가 원격 컴퓨터에서 실행 중이라면 노트북에 `127.0.0.1`을 입력해도 노트북 자신을 가리킵니다. 브라우저 기반 실습에서는 실습 환경에서 안내하는 방법으로 접속하세요.

:::single-choice{#docker-port-mapping-local-browser} Docker가 별도의 실습 컴퓨터에서 8080번 포트를 공개했습니다. 내 노트북의 브라우저에 `127.0.0.1`을 입력하면 어디를 가리키나요?

::option[별도의 실습 컴퓨터.]{#docker-port-mapping-local-lab explanation="그 주소를 실습 컴퓨터에서 사용했을 때만 실습 컴퓨터 자신을 가리킵니다."}
::option[Docker의 웹 컨테이너.]{#docker-port-mapping-local-container explanation="브라우저는 자신이 실행되는 컴퓨터의 주소를 사용합니다. 포트 매핑을 통해 요청을 컨테이너로 전달할 수 있습니다."}
::option[내 노트북.]{#docker-port-mapping-local-laptop .correct explanation="루프백 주소는 브라우저가 실행 중인 컴퓨터를 가리킵니다."}
:::

## Docker에서 공개한 포트 확인하기

`docker ps`의 `PORTS` 열에서 매핑을 확인할 수 있습니다. 화살표는 호스트 주소와 포트에서 컨테이너 포트를 향합니다. `/tcp`는 이 매핑에 사용되는 네트워크 프로토콜입니다.

```text
$ docker ps
STATUS         PORTS                   NAMES
Up 2 minutes   127.0.0.1:8080->80/tcp   published-web
```

행에 `80/tcp`만 표시될 수도 있습니다. 호스트 주소와 화살표가 없다면 이 행에는 공개된 호스트 포트가 나타나지 않은 것입니다.

![호스트 8080번 포트에서 컨테이너 80번 포트로 전달되고 HTTP 200 응답이 온 모습을 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-port-mapping/loopback-mapping.png)

이 화면은 `published-web`만 보이도록 필터링했습니다. Docker 호스트에서 실행한 `curl` 요청은 공개 주소가 정상적으로 응답하는지 확인합니다.

:::single-choice{#docker-port-mapping-read-listing} 어떤 행에 화살표 없이 `80/tcp`만 표시됩니다. 이 항목에서 무엇을 알 수 있나요?

::option[Docker가 호스트의 80번 포트를 공개했다.]{#docker-port-mapping-listing-host explanation="공개된 매핑은 호스트 포트를 표시하고 컨테이너 포트를 가리킵니다."}
::option[컨테이너 포트가 표시되지만 공개된 호스트 포트는 보이지 않는다.]{#docker-port-mapping-listing-container .correct explanation="이 항목은 컨테이너 내부의 80번 포트를 나타냅니다. 호스트 주소나 전달 방향을 뜻하는 화살표는 없습니다."}
::option[Docker가 호스트의 8080번 포트를 공개했다.]{#docker-port-mapping-listing-default explanation="이 항목에는 호스트 포트가 없습니다. Docker가 8080번을 추정하는 것도 아닙니다."}
:::

## 테스트할 주소 고르기

페이지가 열리지 않으면 입력한 주소와 매핑의 왼쪽을 비교하세요. `Up` 상태와 화살표로 Docker가 무엇을 실행하고 어디로 전달하는지 알 수 있습니다. 서버가 실제로 페이지를 반환하는지는 브라우저에서 요청을 보내 확인합니다.

:::single-choice{#docker-port-mapping-correct-misdirected} Docker 호스트에서 8080번 포트로 접속했지만 페이지가 열리지 않습니다. 행에는 `127.0.0.1:8081->80/tcp`라고 표시됩니다. 다음에는 무엇을 해 봐야 하나요?

::option[`http://127.0.0.1:80`을 연다.]{#docker-port-mapping-misdirected-80 explanation="80번 포트는 매핑에서 컨테이너 쪽에 있습니다."}
::option[`http://127.0.0.1:8081`을 연다.]{#docker-port-mapping-misdirected-8081 .correct explanation="화살표 왼쪽에 있는 공개 호스트 포트를 사용합니다."}
::option[`http://127.0.0.1:8080`을 다시 시도한다.]{#docker-port-mapping-misdirected-8080 explanation="목록에 표시되는 호스트 포트는 8081입니다. 8080으로는 이 매핑을 확인할 수 없습니다."}
:::

## 요약

이제 포트 매핑을 읽고 브라우저에 올바른 주소를 입력할 수 있습니다.

1. 호스트 포트와 컨테이너 포트를 구분합니다.
2. `127.0.0.1`이 가리키는 위치를 설명합니다.
3. 컨테이너 목록에서 공개된 포트 매핑을 찾습니다.
4. 공개된 호스트 포트로 서비스를 테스트합니다.
