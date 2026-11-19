---
lesson_id: "dockerfile"
course_id: "docker"
lang: "ko"
order_index: 7
title: "Dockerfile"
description: "Dockerfile로 페이지와 베이스 이미지를 묶어 재사용할 수 있는 웹 서버 이미지를 만드는 법을 배웁니다."
meta_title: "Dockerfile - Docker"
meta_description: "작은 Dockerfile에 나오는 FROM, COPY, CMD를 읽고 이미지 빌드와 컨테이너 시작을 구분합니다."
meta_keywords: "Dockerfile, Docker 이미지 빌드, FROM, COPY, CMD, 빌드 컨텍스트"
---

앞에서는 기존 웹 서버 이미지로 컨테이너를 시작했습니다. 내 페이지를 제공하려면 그 페이지가 이미 들어 있는 이미지를 만들 수 있습니다. **Dockerfile**은 이미지를 빌드하는 방법을 적은 텍스트 파일입니다.

## 베이스 이미지로 시작하기

**베이스 이미지**에는 빌드의 바탕이 되는 파일과 프로그램이 들어 있습니다. 다음 Dockerfile은 Nginx 이미지에서 시작해 페이지를 추가하고 컨테이너가 기본으로 실행할 명령어를 기록합니다. Dockerfile과 `index.html`을 같은 연습 폴더에 두세요. 페이지 내용은 `<h1>Hello from Docker</h1>`처럼 한 줄이면 됩니다.

```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/index.html
CMD ["nginx", "-g", "daemon off;"]
```

`FROM nginx:alpine`은 Nginx 프로그램을 이미 포함한 이미지를 시작점으로 선택합니다. Docker는 새 이미지를 빌드할 때 이 이미지를 사용합니다.

:::single-choice{#dockerfile-base-image-purpose} 페이지를 추가하기 전에 Nginx를 제공하는 줄은 어느 줄인가요?

::option[`COPY index.html /usr/share/nginx/html/index.html`]{#dockerfile-base-image-copy explanation="COPY는 페이지를 추가합니다. 서버는 베이스 이미지에서 제공됩니다."}
::option[`FROM nginx:alpine`]{#dockerfile-base-image-from .correct explanation="FROM은 서버가 이미 들어 있는 베이스 이미지를 선택합니다."}
::option[`CMD`로 시작하는 줄.]{#dockerfile-base-image-cmd explanation="CMD는 기본 시작 명령어를 설정합니다. 서버 프로그램은 베이스 이미지에서 가져옵니다."}
:::

## 파일 추가하기

`COPY`는 빌드에 제공한 파일 중 `index.html`을 읽습니다. 오른쪽에 적힌 경로에 페이지를 씁니다. 이 버전의 Nginx 이미지는 그 위치에서 기본 페이지를 제공합니다. 나중에 로컬 페이지를 수정했다면 변경 내용을 담도록 이미지를 다시 빌드하세요.

:::single-choice{#dockerfile-copy-after-edit} 빌드한 다음 로컬 index.html의 제목을 바꿨습니다. 새 이미지에 변경 내용을 어떻게 넣나요?

::option[기존 이미지에서 다른 컨테이너를 시작한다.]{#dockerfile-copy-edit-run explanation="그 컨테이너는 기존 이미지에 이미 들어 있는 페이지를 사용합니다."}
::option[기존 컨테이너의 이름만 바꾼다.]{#dockerfile-copy-edit-rename explanation="컨테이너 이름은 이미지 안에 담긴 파일을 바꾸지 않습니다."}
::option[업데이트한 페이지로 이미지를 다시 빌드한다.]{#dockerfile-copy-edit-rebuild .correct explanation="빌드 중 COPY가 현재 로컬 파일을 읽어 새 이미지에 넣습니다."}
:::

## 시작 명령어 설정하기

`CMD`는 새 컨테이너에서 사용할 기본 명령어를 설정합니다. 이 예제에서는 Nginx가 컨테이너 안에서 포그라운드로 계속 실행됩니다. `docker run -d`를 사용하면 컨테이너는 현재 터미널과 분리해 백그라운드로 실행할 수 있습니다.

:::single-choice{#dockerfile-cmd-start-time} 예제의 기본 CMD는 언제 적용되나요?

::option[컨테이너가 기본 명령어로 시작될 때.]{#dockerfile-cmd-when-start .correct explanation="Docker는 컨테이너를 시작할 때 이미지의 기본 명령어를 사용합니다."}
::option[Docker가 페이지를 이미지에 복사하는 동안.]{#dockerfile-cmd-when-copy explanation="COPY는 빌드 중 페이지를 추가합니다. 서버를 실행하지는 않습니다."}
::option[Docker가 이미지 쓰기를 끝낼 때.]{#dockerfile-cmd-when-build explanation="빌드에서는 나중에 쓸 시작 명령어를 기록합니다."}
:::

## 이미지 빌드하고 컨테이너 실행하기

두 파일이 모두 들어 있는 폴더에서 빌드하세요. `-t` 옵션은 이미지에 `journey-web:1`이라는 참조를 지정합니다. 끝의 점은 현재 폴더를 빌드에 제공할 파일의 위치로 사용한다는 뜻입니다.

```bash
$ docker build -t journey-web:1 .
$ docker run -d --name custom-web -p 127.0.0.1:8082:80 journey-web:1
```

두 번째 명령어는 컨테이너를 시작합니다. 8082번 포트가 비어 있다면 Docker 호스트의 브라우저에서 `http://127.0.0.1:8082`를 열고 직접 만든 페이지를 볼 수 있습니다.

:::single-choice{#dockerfile-build-versus-run} 빌드가 성공했고 두 번째 명령어는 아직 실행하지 않았습니다. 무엇이 준비됐나요?

::option[이미지가 만들어져 컨테이너를 생성하는 데 쓸 수 있다.]{#dockerfile-build-ready-image .correct explanation="빌드에서 이미지가 생성됐습니다. 다음 명령어로 이 이미지에서 컨테이너를 시작합니다."}
::option[이름을 붙인 컨테이너가 이미 내가 만든 페이지를 제공하고 있다.]{#dockerfile-build-ready-container explanation="서버는 이미지에서 컨테이너를 실행할 때 시작됩니다."}
::option[Docker가 이미지에 브라우저용 포트를 이미 공개했다.]{#dockerfile-build-ready-port explanation="포트 매핑은 docker run의 옵션입니다. 빌드에서는 연결을 설정하지 않습니다."}
:::

![이미지 빌드, 컨테이너 시작, 직접 만든 페이지의 HTML 응답을 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/dockerfile/build-and-run.png)

마지막 요청의 응답은 빌드할 때 이미지에 넣은 페이지입니다. 빌드 진행 메시지와 이미지 ID는 환경에 따라 다를 수 있습니다.

## 요약

이제 작은 Dockerfile을 읽고 로컬 페이지를 실행 중인 서버가 제공하기까지의 과정을 설명할 수 있습니다.

1. `FROM`에서 베이스 이미지를 찾습니다.
2. `COPY`가 파일을 어디서 읽고 어디에 쓰는지 설명합니다.
3. `CMD`를 컨테이너의 기본 시작 명령어로 구분합니다.
4. 이미지를 빌드하고 그 이미지에서 컨테이너를 시작합니다.
