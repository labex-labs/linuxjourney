---
lesson_id: "docker-images"
course_id: "docker"
lang: "ko"
order_index: 2
title: "이미지"
description: "이미지 참조를 읽고 해당 이미지가 로컬에 있는지 확인하는 방법을 배웁니다."
meta_title: "이미지 - Docker"
meta_description: "Docker 이미지의 이름과 태그를 읽고 레지스트리와 다운로드를 살펴보며 이미지 목록과 컨테이너 목록을 구분합니다."
meta_keywords: "Docker 이미지, 이미지 태그, 이미지 레지스트리, docker pull, docker image ls"
---

Docker 이미지에는 프로그램과 파일, 기본 설정이 들어 있습니다. Docker는 이 묶음을 바탕으로 컨테이너를 만듭니다. 여기서는 이미지 이름을 읽고 Docker에 이미 어떤 이미지가 있는지 확인합니다.

## 이미지 이름과 태그 읽기

`nginx:alpine`에서 `nginx`는 이미지 이름이고, `alpine`은 특정 릴리스나 변형을 고르는 **태그**입니다. 이 예에서는 Alpine Linux를 기반으로 만든 변형을 선택합니다. 콜론은 이름과 태그를 구분합니다. `nginx:alpine`과 `nginx:latest`는 이미지 이름이 같지만 참조가 다릅니다.

:::single-choice{#docker-images-read-reference} `busybox:1.36`에서 어느 부분이 태그인가요?

::option[`busybox`]{#docker-images-reference-name explanation="콜론 앞의 busybox는 이름입니다."}
::option[`busybox:1.36`]{#docker-images-reference-whole explanation="전체 참조에는 이미지 이름과 태그가 모두 들어 있습니다."}
::option[`1.36`]{#docker-images-reference-tag .correct explanation="콜론 뒤의 글자가 이미지를 선택하는 태그입니다."}
:::

## 태그 선택하기

`nginx`처럼 태그를 생략하면 Docker는 `latest`를 사용합니다. 관례로 정해진 태그 이름입니다. 게시자가 어떤 이미지를 가리킬지 정하고 나중에 그 대상을 바꿀 수도 있습니다. `nginx:alpine`을 지정하면 원하는 변형을 명시할 수 있습니다. 다만 이 태그가 가리키는 이미지도 업데이트될 수 있습니다.

:::single-choice{#docker-images-default-tag} 동료가 태그 없이 `nginx`를 지정하고 가장 최근 릴리스가 선택됐다고 생각합니다. 실제로 선택된 것은 무엇인가요?

::option[latest 태그가 가리키는 이미지.]{#docker-images-default-latest .correct explanation="태그를 생략하면 latest를 사용합니다. 해당 태그가 가리키는 이미지는 게시자가 정합니다."}
::option[가장 최근에 게시된 Nginx 이미지.]{#docker-images-default-newest explanation="Docker는 latest라는 태그를 사용합니다. 게시 날짜에 따라 이미지를 정렬하지 않습니다."}
::option[사용할 수 있는 가장 작은 Nginx 이미지.]{#docker-images-default-smallest explanation="이미지 크기로 기본 태그를 고르는 것은 아닙니다. 원하는 변형은 이름으로 지정하세요."}
:::

## 이미지 다운로드하기

**레지스트리**는 이미지를 저장하고 다운로드할 수 있게 제공하는 곳입니다. `nginx:alpine`과 같은 참조에는 Docker Hub가 기본 레지스트리로 사용됩니다. 현재 연결된 Docker 환경에 이미지를 받으려면 `docker pull`을 사용합니다. 이렇게 다운로드하는 작업을 **이미지 가져오기** 또는 풀이라고도 합니다.

```bash
$ docker pull nginx:alpine
```

명령어가 성공하면 해당 환경에서 이미지를 사용할 수 있습니다. 컨테이너 시작은 별도 단계입니다. 터미널 예제에서 `$`는 프롬프트입니다.

:::single-choice{#docker-images-pull-result} 이미지 가져오기가 성공했습니다. Docker가 한 일은 무엇인가요?

::option[웹 요청에 응답하는 컨테이너를 시작했다.]{#docker-images-pull-started explanation="컨테이너는 실행 명령을 내렸을 때 시작합니다. 가져오기는 이미지를 쓸 수 있게 준비하는 작업입니다."}
::option[해당 환경에서 이미지를 사용할 수 있도록 했다.]{#docker-images-pull-available .correct explanation="다운로드한 이미지를 바탕으로 컨테이너를 만들 수 있습니다."}
::option[이미지의 사본을 레지스트리에 업로드했다.]{#docker-images-pull-uploaded explanation="가져오기는 레지스트리의 이미지를 Docker 로컬 저장소로 옮기는 작업입니다."}
:::

## 로컬 이미지 확인하기

`docker image ls`로 이미 사용 가능한 이미지를 확인합니다. 이 예제는 이름과 태그 열만 보여 줍니다. Docker는 이미지 이름 열을 `REPOSITORY`라고 표시합니다.

```text
$ docker image ls
REPOSITORY   TAG
nginx        alpine
busybox      1.36
```

첫 번째 행에는 `nginx:alpine`이 표시됩니다. 이 표는 어떤 이미지가 있는지 알려 줍니다. 이미지로 만든 컨테이너의 상태는 별도의 목록에서 확인합니다.

![docker pull과 docker image ls의 REPOSITORY 및 TAG 열을 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-images/pull-and-list.png)

이 화면에서는 레슨에 나온 두 참조만 보이도록 목록을 필터링했습니다.

:::single-choice{#docker-images-local-list} 이 출력에서 사용할 수 있는 이미지 참조는 무엇인가요?

::option[`busybox:latest`]{#docker-images-local-busybox-latest explanation="busybox 행의 태그는 1.36입니다. 예제에 latest 태그가 달린 busybox 행은 없습니다."}
::option[`busybox:1.36`]{#docker-images-local-busybox .correct explanation="REPOSITORY 열의 busybox와 TAG 열의 1.36을 함께 읽습니다."}
::option[`nginx:1.36`]{#docker-images-local-nginx-mixed explanation="이름과 태그는 같은 행에서 확인해야 합니다. 여기서 1.36은 busybox 행에 있습니다."}
:::

## 요약

이제 이미지 참조를 읽고 로컬 이미지 목록에 있는지 확인할 수 있습니다.

1. 이미지 참조에서 이름과 태그를 찾습니다.
2. 태그를 생략하면 어떻게 되는지 설명합니다.
3. `docker pull`로 레지스트리에서 이미지를 다운로드합니다.
4. `docker image ls`에서 이름과 태그 열을 읽습니다.
