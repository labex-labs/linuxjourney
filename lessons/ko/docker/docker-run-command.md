---
lesson_id: "docker-run-command"
course_id: "docker"
lang: "ko"
order_index: 3
title: "docker run"
description: "docker run으로 이미지에서 컨테이너를 만들고 시작하는 방법을 배웁니다."
meta_title: "docker run - Docker"
meta_description: "docker run 명령어를 읽고 컨테이너에 이름을 붙이며 포그라운드의 짧은 작업과 백그라운드 서버를 구분합니다."
meta_keywords: "docker run, Docker 컨테이너 실행, 컨테이너 이름, 포그라운드, 백그라운드"
---

웹 서버 이미지가 준비되어 있습니다. 서버를 실행하려면 `docker run`을 사용해 이 이미지로 컨테이너를 만들고 시작합니다. 먼저 금방 끝나는 명령어를 실행해 터미널을 언제 다시 사용할 수 있는지 살펴봅시다.

## 짧은 작업 실행하기

BusyBox는 기본 Linux 명령어가 들어 있는 작은 이미지입니다. 아래 예제에서 `echo`는 메시지를 출력합니다. 이미지 참조 뒤에 컨테이너에서 실행할 명령어를 적습니다. 로컬에 이미지가 없다면 Docker가 보통 다운로드합니다. `$`는 터미널 프롬프트입니다. 이미지를 먼저 받아야 할 때는 예제의 출력 줄보다 앞에 다운로드 메시지가 표시될 수 있습니다.

```text
$ docker run busybox:1.36 echo Hello
Hello
```

터미널에 출력이 나타납니다. `echo`가 끝나면 컨테이너가 중지되고 프롬프트가 다시 표시됩니다.

:::single-choice{#docker-run-command-short-task} 이 예제에서 컨테이너 안에서 실행되는 것은 무엇인가요?

::option[셸 명령어로 실행되는 `busybox:1.36`.]{#docker-run-command-short-image explanation="BusyBox는 도구가 들어 있는 이미지입니다. 명령어는 이미지 참조 뒤에 나옵니다."}
::option[이미지의 도구로 실행하는 `echo Hello`.]{#docker-run-command-short-echo .correct explanation="이미지 참조 뒤에 echo가 나오고 뒤이어 출력할 문자열이 지정됩니다."}
::option[다른 Docker 명령어로 실행되는 `docker run`.]{#docker-run-command-short-docker explanation="docker run은 터미널에서 실행하는 명령어로, 컨테이너 안의 작업을 시작합니다."}
:::

## 컨테이너에 이름 붙이기

나중에 알아볼 수 있도록 이미지 참조 앞에 `--name`을 넣어 이름을 지정합니다. 이 명령어는 짧은 작업을 수행하는 컨테이너에 `report`라는 이름을 붙입니다.

```bash
$ docker run --name report busybox:1.36 echo Ready
```

이미 존재하는 컨테이너는 중지된 후에도 이름을 유지합니다. 같은 Docker 환경에서 다른 컨테이너를 만들 때는 사용 중이지 않은 이름을 고르세요.

:::single-choice{#docker-run-command-name-choice} report 작업이 끝났지만 컨테이너는 남아 있습니다. 같은 이미지로 두 번째 컨테이너를 만들고 싶다면 무엇을 바꾸면 될까요?

::option[이미지 참조는 그대로 두고 다른 컨테이너 이름을 사용한다.]{#docker-run-command-name-new .correct explanation="아직 사용하지 않는 이름이 있으면 Docker는 같은 이미지로 별도의 컨테이너를 만들 수 있습니다."}
::option[컨테이너 이름은 그대로 두고 이미지 태그를 바꾼다.]{#docker-run-command-name-change-tag explanation="다른 이미지를 골라도 기존 컨테이너가 이름을 계속 사용합니다."}
::option[컨테이너 이름은 그대로 두고 출력을 바꾼다.]{#docker-run-command-name-change-message explanation="메시지는 echo에 전달하는 입력입니다. 이를 바꿔도 report라는 이름은 계속 사용 중입니다."}
:::

## 백그라운드에서 서버 시작하기

이미지는 기본 명령어를 지정할 수 있습니다. `nginx:alpine` 이미지 뒤에 따로 명령어를 쓰지 않으면 웹 서버가 시작됩니다. `-d`를 붙이면 **백그라운드**에서 실행되어 서버가 동작하는 동안 프롬프트가 돌아옵니다.

```bash
$ docker run -d --name web nginx:alpine
```

Docker는 시작한 컨테이너를 식별하는 긴 컨테이너 ID를 출력합니다. 서버가 계속 실행되는지는 다음 레슨에서 확인합니다.

![짧은 Docker 작업의 Hello 및 Ready 출력과 백그라운드에서 시작한 서버의 컨테이너 ID를 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-run-command/foreground-and-detached.png)

짧은 작업은 터미널에 메시지를 출력합니다. 서버를 백그라운드에 띄우면 컨테이너 ID가 반환됩니다.

:::single-choice{#docker-run-command-detach-meaning} Docker가 ID를 출력한 뒤 프롬프트가 돌아왔습니다. 이 모드에서는 어떤 작업이 가능한가요?

::option[서버가 끝난 다음에만 터미널을 사용한다.]{#docker-run-command-detach-wait explanation="백그라운드 모드에서는 서버가 계속 실행되어도 프롬프트가 돌아옵니다."}
::option[서버를 시작하지 않고 이미지만 준비한다.]{#docker-run-command-detach-skip explanation="백그라운드 모드에서도 Docker는 컨테이너를 시작합니다."}
::option[서버가 실행되는 도중에도 터미널을 사용한다.]{#docker-run-command-detach-continue .correct explanation="이 모드에서는 컨테이너를 시작한 뒤 터미널을 다시 사용할 수 있습니다."}
:::

## 새 컨테이너 구분하기

`docker run`이 성공할 때마다 새 컨테이너가 만들어집니다. 같은 서버 이미지에 다른 이름을 지정하면 Docker가 두 번째 컨테이너를 만듭니다. 첫 번째 컨테이너는 이름과 상태를 유지합니다.

:::single-choice{#docker-run-command-second-instance} web이 실행 중입니다. demo라는 이름이 비어 있으면 `docker run -d --name demo nginx:alpine`은 무엇을 하나요?

::option[실행 중인 web 컨테이너의 이름을 demo로 바꾼다.]{#docker-run-command-second-rename explanation="docker run은 새 컨테이너를 만드는 명령어입니다. 기존 web의 이름은 그대로입니다."}
::option[이미지에 demo라는 새 태그를 붙인다.]{#docker-run-command-second-tag explanation="이 옵션은 컨테이너의 이름을 정합니다. 이미지 참조는 여전히 nginx:alpine입니다."}
::option[demo라는 별도의 컨테이너를 시작한다.]{#docker-run-command-second-new .correct explanation="Docker는 이 이미지로 새 컨테이너를 만들고 demo라는 이름을 지정합니다."}
:::

컨테이너를 직접 시작하고 출력을 확인하려면 [첫 Docker 실습](https://labex.io/labs/docker-your-first-docker-lab-92719)을 이용해 보세요.

## 요약

이제 docker run 명령어를 읽고 Docker가 무엇을 만들지 판단할 수 있습니다.

1. 이미지와 컨테이너 안에서 실행할 명령어를 구분합니다.
2. `--name`으로 나중에 찾기 쉬운 이름을 붙입니다.
3. 짧은 작업이 끝나면 어떤 일이 생기는지 설명합니다.
4. `-d`로 서버가 실행되는 동안 프롬프트를 사용합니다.
