---
lesson_id: "docker-ps-command"
course_id: "docker"
lang: "ko"
order_index: 4
title: "docker ps"
description: "Docker 컨테이너 목록을 보고 실행 중인 컨테이너와 종료된 컨테이너를 구분합니다."
meta_title: "docker ps - Docker"
meta_description: "docker ps 출력을 읽고 docker ps -a로 중지된 컨테이너를 찾으며 이름과 종료 코드를 확인합니다."
meta_keywords: "docker ps, Docker 컨테이너 목록, 중지된 컨테이너, docker ps -a, 컨테이너 상태, 종료 코드"
---

Docker에서 시작한 웹 서버가 아직 실행 중인가요? `docker ps`로 확인해 봅시다. Docker 이미지에는 프로그램과 필요한 파일이 들어 있습니다. 컨테이너는 그 이미지로 만든 인스턴스입니다. 이 명령어는 실행한 시점의 컨테이너 목록을 보여 줍니다.

## 실행 중인 컨테이너 확인하기

기본적으로 `docker ps`는 실행 중인 컨테이너를 나열합니다. 아래 예제는 준비된 Docker 환경의 출력에서 몇 개 열만 보여 주므로 Docker를 따로 설정하지 않아도 읽을 수 있습니다. 터미널에서 따라 할 때는 `$` 프롬프트 뒤의 명령어를 입력하세요.

```text
$ docker ps
IMAGE         STATUS         NAMES
nginx:alpine  Up 4 minutes   web
nginx:alpine  Up 30 seconds  demo
```

열 제목만 나온다면 실행 중인 컨테이너 목록이 비어 있다는 뜻입니다. 같은 환경에 중지된 컨테이너가 남아 있을 수는 있습니다.

:::single-choice{#docker-ps-running-list} `docker ps` 실행 후 열 제목만 나타났습니다. 무엇을 알 수 있나요?

::option[실행에 사용할 이미지가 없다.]{#docker-ps-running-list-images explanation="이 명령어는 컨테이너를 나열합니다. 실행 중인 컨테이너가 없어도 이미지는 있을 수 있습니다."}
::option[실행 중인 컨테이너 목록이 비어 있다.]{#docker-ps-running-list-empty .correct explanation="기본 목록에는 실행 중인 컨테이너만 나타납니다. 중지된 컨테이너는 여전히 있을 수 있습니다."}
::option[확인할 수 있는 중지된 컨테이너가 없다.]{#docker-ps-running-list-stopped explanation="중지된 컨테이너는 기본 조회 범위 밖에 있습니다. 빈 목록으로는 존재 여부를 알 수 없습니다."}
:::

## 이름과 상태 읽기

`NAMES` 열에서 원하는 컨테이너를 찾습니다. 두 행의 `IMAGE` 열에는 모두 `nginx:alpine`이 표시됩니다. 오른쪽 끝에서 `web`을 찾고 같은 행에서 `STATUS`를 읽으세요. `Up 4 minutes`는 해당 컨테이너가 약 4분 동안 실행됐다는 뜻입니다.

:::single-choice{#docker-ps-name-column} 약 30초 동안 실행된 컨테이너는 어느 행에 있나요?

::option[이름이 `demo`인 행.]{#docker-ps-name-demo .correct explanation="STATUS에서 Up 30 seconds를 찾고, 같은 행의 NAMES에서 demo를 확인합니다."}
::option[이름이 `web`인 행.]{#docker-ps-name-web explanation="web 행에는 Up 4 minutes라고 표시됩니다. 둘은 같은 이미지를 쓰지만 시작한 시각이 다릅니다."}
::option[이미지가 `nginx:alpine`인 두 행 모두.]{#docker-ps-name-image-reference explanation="행마다 상태가 다릅니다. 같은 이미지를 사용하더라도 시작 시각이 같은 것은 아닙니다."}
:::

## 종료된 컨테이너도 표시하기

찾던 컨테이너가 없다면 `docker ps -a`를 사용해 보세요. `-a`는 `--all`의 짧은 표기입니다. 중지되었지만 남아 있는 컨테이너도 포함합니다. 예제에는 미리 준비한 `preview`라는 작업도 있습니다.

```text
$ docker ps -a
IMAGE         STATUS                         NAMES
nginx:alpine  Up 4 minutes                   web
nginx:alpine  Up 30 seconds                  demo
busybox:1.36  Exited (0) 2 minutes ago       report
busybox:1.36  Exited (1) About a minute ago  preview
```

컨테이너는 웹 서버나 스크립트와 같은 주 프로그램을 실행합니다. `Exited`는 해당 프로그램이 멈췄다는 뜻입니다. 괄호 안의 숫자는 프로그램이 끝날 때 반환한 **종료 코드**입니다. 일반적으로 0은 성공을, 0이 아닌 코드는 오류를 나타냅니다. `report`의 `Exited (0)`은 짧은 작업이 성공적으로 끝났을 때의 정상적인 결과입니다.

![실행 중과 종료 상태의 컨테이너, report의 종료 코드 0과 preview의 종료 코드 1을 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-ps-command/running-and-exited.png)

LabEx 화면에는 예제 컨테이너 네 개의 이름과 상태만 표시됩니다. 경과 시간은 실행 시점에 따라 달라집니다.

:::single-choice{#docker-ps-exit-code-reading} 종료 코드로 판단할 때 어느 행의 오류를 조사해야 하나요?

::option[작업이 끝났으므로 `report`.]{#docker-ps-exit-code-report explanation="짧은 작업은 끝나면 종료될 수 있습니다. 종료 코드 0은 보통 성공을 나타냅니다."}
::option[실행 중인 컨테이너 중 가장 최근에 시작했으므로 `demo`.]{#docker-ps-exit-code-demo explanation="Up은 프로그램이 얼마나 오래 실행되었는지를 말합니다. 이 행에는 종료 코드가 없습니다."}
::option[코드 1로 종료됐으므로 `preview`.]{#docker-ps-exit-code-preview .correct explanation="preview에는 Exited (1)이 표시됩니다. 문제를 더 확인할 만한 단서지만 이 상태만으로 원인을 알 수는 없습니다."}
:::

## 다음 확인 항목 고르기

종료 코드는 어디를 조사할지 알려 주는 단서입니다. `preview`가 오류 메시지를 출력했는지 보려면 `docker logs` 뒤에 그 이름을 적으세요. Docker가 그 컨테이너에서 수집한 출력이 표시됩니다.

```bash
$ docker logs preview
```

실행 중인 웹 서버의 페이지를 실제 방문자가 열 수 있는지도 확인할 수 있습니다. 페이지를 이용해야 하는 컴퓨터에서 직접 열어 보세요. `Up`은 컨테이너 내부 프로그램의 상태입니다. 브라우저 요청이 성공하면 테스트한 컴퓨터에서 페이지에 도달할 수 있다는 뜻입니다.

:::single-choice{#docker-ps-check-visitor-access} Docker가 실행되는 컴퓨터에서는 페이지가 열립니다. 다른 컴퓨터를 쓰는 동료도 페이지를 열어야 합니다. 어떤 확인으로 알 수 있나요?

::option[동료의 컴퓨터에서 페이지를 연다.]{#docker-ps-next-check-visitor-browser .correct explanation="동료가 실제로 사용할 연결 경로가 확인됩니다."}
::option[Docker가 실행되는 컴퓨터에서 `docker ps`를 다시 실행한다.]{#docker-ps-next-check-status-again explanation="목록에서 web이 실행 중인지 확인할 수 있습니다. 동료의 컴퓨터에서 접속되는지는 그쪽에서 요청해야 알 수 있습니다."}
::option[Docker가 실행되는 컴퓨터에서 페이지를 다시 연다.]{#docker-ps-next-check-host-browser explanation="같은 위치에서 검사를 반복합니다. 동료의 연결은 다르게 동작할 수 있습니다."}
:::

## 요약

이제 컨테이너 목록에서 대상을 찾고 상태를 읽은 뒤 다음에 확인할 항목을 선택할 수 있습니다.

1. `docker ps`로 실행 중인 컨테이너를 표시합니다.
2. 이름으로 컨테이너를 찾고 상태를 읽습니다.
3. `docker ps -a`로 종료된 컨테이너도 포함합니다.
4. 상태만으로 확인하기 어렵다면 로그나 브라우저 요청을 사용합니다.
