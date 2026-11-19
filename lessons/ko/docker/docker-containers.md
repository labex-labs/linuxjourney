---
lesson_id: "docker-containers"
course_id: "docker"
lang: "ko"
order_index: 1
title: "컨테이너"
description: "Docker 컨테이너 안에서 무엇이 실행되는지, 컨테이너와 Docker를 실행하는 컴퓨터가 어떤 관계인지 배웁니다."
meta_title: "컨테이너 - Docker"
meta_description: "작은 웹 서버로 컨테이너의 동작을 살펴보고 주 프로그램을 시작하거나 중지하면 무엇이 달라지는지 알아봅니다."
meta_keywords: "Docker 컨테이너, 컨테이너 기초, Docker 호스트, 컨테이너 프로세스, 웹 서버"
---

브라우저에서 Docker로 실행한 웹 서버의 페이지를 엽니다. 이 서버는 어디에서 실행될까요? 서버를 중지하면 페이지는 어떻게 될까요? 먼저 브라우저에 응답하는 프로그램부터 살펴봅시다.

## 컨테이너 안에서 실행되는 프로그램

**웹 서버**는 페이지를 요청받아 응답하는 프로그램입니다. 브라우저와 `web`이라는 작은 웹 서버가 같은 컴퓨터에서 실행된다고 가정해 봅시다. Docker는 서버를 **컨테이너** 안에서 실행합니다. 프로그램이 볼 수 있는 파일과 기타 리소스는 컨테이너마다 다를 수 있습니다. 이 과정에는 실행 예제가 준비되어 있어 Docker를 설치하지 않고도 따라갈 수 있습니다.

:::single-choice{#docker-containers-page-request} 브라우저가 페이지를 요청하면 무엇이 페이지 내용을 돌려주나요?

::option[컨테이너 안에서 실행 중인 웹 서버.]{#docker-containers-page-server .correct explanation="서버 프로그램이 요청을 받아 페이지를 돌려줍니다."}
::option[컨테이너 시작 방법을 적어 둔 파일.]{#docker-containers-page-files explanation="이 파일은 실행 환경을 설정하는 데 쓰입니다. 요청에 응답하는 것은 실행 중인 프로그램입니다."}
::option[컴퓨터에 있는 Docker 컨테이너의 목록.]{#docker-containers-page-list explanation="목록은 Docker에서 무엇을 실행하는지 보여 줍니다. 페이지를 제공하지는 않습니다."}
:::

## 컨테이너와 호스트

컨테이너를 실행하는 컴퓨터를 **호스트**라고 합니다. Linux의 Docker에서 Linux 컨테이너를 실행하면 그 안의 프로그램은 Linux 호스트에서 프로세스로 동작합니다. **프로세스**란 실행 중인 프로그램입니다. 여러 컨테이너가 같은 호스트를 공유하더라도 각 컨테이너에서 볼 수 있는 리소스의 범위는 제한됩니다. Docker Desktop에서는 Docker가 관리하는 Linux 가상 머신 안에서 Linux 컨테이너가 실행됩니다.

:::single-choice{#docker-containers-shared-host} Linux 컨테이너 두 개가 같은 Linux 호스트에서 실행됩니다. 이 사실에서 무엇을 알 수 있나요?

::option[두 컨테이너의 프로그램은 반드시 같은 파일을 봅니다.]{#docker-containers-host-shared-files explanation="같은 호스트에서도 컨테이너마다 보이는 파일이 다를 수 있습니다."}
::option[각 프로그램은 같은 호스트에서 별도의 프로세스로 실행될 수 있습니다.]{#docker-containers-host-separate-processes .correct explanation="하나의 호스트에서 서로 다른 컨테이너의 프로그램을 따로 실행할 수 있습니다."}
::option[컨테이너마다 별도의 Linux 컴퓨터를 시작해야 합니다.]{#docker-containers-host-separate-machines explanation="컨테이너마다 컴퓨터를 시작할 필요 없이 Linux 컨테이너를 한 호스트의 프로세스로 실행할 수 있습니다."}
:::

## 이미지로 컨테이너 만들기

Docker는 **이미지**를 바탕으로 컨테이너를 만듭니다. 이미지는 프로그램과 필요한 파일을 한데 묶은 것입니다. 같은 웹 서버 이미지로 `web`과 `demo`를 만들 수 있습니다. 시작하면 각 컨테이너가 같은 서버 프로그램을 별도의 프로세스로 실행합니다. 한쪽만 따로 중지할 수 있습니다.

:::single-choice{#docker-containers-two-from-image} web이 실행 중일 때 demo를 중지하면 web은 어떻게 되나요?

::option[demo가 다시 시작될 때까지 일시 중지됩니다.]{#docker-containers-two-paused explanation="각 컨테이너는 자신의 프로그램을 실행합니다. 이 예에서는 demo가 멈춰도 web은 멈추지 않습니다."}
::option[이미지에서 다시 만들어야 합니다.]{#docker-containers-two-recreate explanation="web은 따로 만든 컨테이너이므로 계속 실행할 수 있습니다."}
::option[자기 컨테이너에서 계속 실행됩니다.]{#docker-containers-two-independent .correct explanation="두 컨테이너는 같은 이미지를 바탕으로 만들었지만 서로 독립적으로 실행됩니다."}
:::

## 서비스 중지 전후 확인하기

브라우저가 이미 `web`에 요청을 보낼 수 있다고 가정해 봅시다. 컨테이너를 중지하기 전에는 브라우저가 페이지를 받습니다. 중지한 뒤 새로 요청하면 이 서버에서 더는 페이지가 오지 않습니다. 이미지는 그대로 있어서 다른 컨테이너를 만드는 데 쓸 수 있습니다. 페이지를 받으려면 서버 프로그램이 실행 중이어야 하고, 브라우저가 서버에 접속할 수 있어야 합니다. 브라우저에서 컨테이너에 연결하는 방법은 뒤에서 다룹니다.

:::single-choice{#docker-containers-stopped-server} 이미지는 남아 있지만 web은 중지된 상태입니다. web이 다시 응답하려면 무엇이 필요한가요?

::option[web의 서버 프로그램이 다시 실행되어야 합니다.]{#docker-containers-stopped-program .correct explanation="이미지는 파일을 제공합니다. 새 요청은 실행 중인 서버 프로그램이 처리합니다."}
::option[페이지를 제공할 수 있도록 이미지 이름을 바꿔야 합니다.]{#docker-containers-stopped-rename explanation="이미지 이름을 바꿔도 중지된 서버가 시작되지는 않습니다."}
::option[브라우저에 서버 이미지 사본을 하나 더 제공해야 합니다.]{#docker-containers-stopped-browser-image explanation="브라우저는 요청을 보내고 서버 프로그램은 컨테이너에서 실행됩니다."}
:::

![컨테이너 중지 전에는 HTTP 200 응답을, 중지 후에는 연결 실패를 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker/docker-containers/server-response.png)

이 LabEx 예제에서는 `page-demo`라는 컨테이너가 페이지를 제공합니다. 첫 `curl` 요청에는 HTTP 200 응답이 돌아옵니다. 컨테이너를 중지한 뒤에는 새 요청이 실패합니다. HTTP 응답을 받지 못했기 때문에 curl은 `000`을 출력합니다.

## 요약

이제 컨테이너가 호스트에서 프로그램을 실행하는 방식을 설명할 수 있습니다.

1. 브라우저 요청에 응답하는 프로그램을 알아봅니다.
2. 여러 컨테이너가 하나의 호스트를 공유하는 방식을 설명합니다.
3. 같은 이미지로 여러 컨테이너를 만들 수 있음을 설명합니다.
4. 새 요청을 보내 이전에 접속할 수 있었던 서버가 여전히 응답하는지 확인합니다.
