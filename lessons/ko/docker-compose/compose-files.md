---
lesson_id: "compose-files"
course_id: "docker-compose"
lang: "ko"
order_index: 1
title: "Compose 파일"
description: "Compose 파일에서 서비스, 이미지, 명령, 포트를 찾아 읽는 방법을 알아봅니다."
meta_title: "Compose 파일 - Docker Compose"
meta_description: "Compose 파일에서 서비스, 이미지, 명령, 포트를 찾아 읽는 방법을 알아봅니다."
meta_keywords: "Compose 파일, 서비스, Docker Compose, DevOps, Linux Journey"
---

웹 서버와 보조 도구를 한 번만 실행한다면 명령을 따로 입력해도 됩니다. **Compose 파일**에 설정을 모아 두면 같은 서비스를 나중에 다시 시작할 수 있습니다. 이 과정에서는 `docker compose` 명령을 제공하는 Compose 플러그인이 설치된 Docker 환경을 사용합니다.

## 서비스 두 개 정의하기

`journey-compose`라는 실습 폴더를 새로 만들고 아래 내용을 `compose.yaml`로 저장합니다. **서비스**는 Compose가 컨테이너를 어떤 설정으로 실행할지 정의합니다. 이 파일에는 웹 서버와, 이후 확인에 쓸 수 있도록 계속 실행되는 간단한 도구 컨테이너가 있습니다.

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "127.0.0.1:8080:80"
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
```

들여쓰기에는 공백을 사용합니다. `web` 아래에 들여쓴 키는 그 서비스에 속합니다. `ports` 아래의 하이픈은 목록 항목의 시작을 나타냅니다. `command`의 대괄호도 목록을 나타내며, 여기에는 프로그램 이름과 인수가 들어 있습니다.

:::single-choice{#compose-files-service-images} 어느 서비스가 BusyBox 이미지를 사용하나요?

::option[web 서비스입니다.]{#compose-files-service-images-a explanation="web의 이미지 항목에는 nginx가 적혀 있습니다."}
::option[toolbox 서비스입니다.]{#compose-files-service-images-c .correct explanation="toolbox의 image 필드에는 busybox:1.36이 적혀 있습니다."}
::option[두 서비스 모두 사용합니다.]{#compose-files-service-images-b explanation="서비스마다 이미지 설정이 따로 있습니다."}
:::

## 웹 서비스 설정 읽기

웹 서비스는 컨테이너의 80번 포트를 호스트의 8080번 포트로 공개합니다. 서비스가 시작되면 Docker가 실행되는 컴퓨터에서 `http://127.0.0.1:8080`에 요청을 보내 Nginx에 접속할 수 있습니다. 도구 컨테이너는 포트를 공개하지 않습니다. `sleep` 명령으로 실습 중 3,600초 동안 실행 상태를 유지합니다.

:::single-choice{#compose-files-mapping-owner} Docker 호스트의 브라우저에서 Nginx에 접속하는 방법은 파일의 어디에서 결정하나요?

::option[web 아래의 ports 설정입니다.]{#compose-files-mapping-owner-a .correct explanation="이 항목은 호스트의 주소와 포트를 웹 컨테이너에 연결합니다."}
::option[toolbox 아래의 이미지 태그입니다.]{#compose-files-mapping-owner-b explanation="이 태그는 도구 컨테이너에서 사용할 이미지를 선택합니다."}
::option[toolbox 아래의 sleep 인수입니다.]{#compose-files-mapping-owner-c explanation="이 인수는 해당 프로그램이 실행될 시간을 정합니다."}
:::

## Compose가 읽은 설정 확인하기

파일이 있는 폴더에서 명령을 실행합니다. 프롬프트를 나타내는 `$` 뒤에 나오는 내용만 입력하세요. Compose는 `compose.yaml`을 읽고 해석한 설정을 출력합니다. `web`과 `toolbox` 항목을 찾으세요. 짧게 쓴 설정이 출력에서는 더 자세하게 표시될 수 있습니다.

```bash
$ docker compose config
```

:::single-choice{#compose-files-config-scope} 명령이 오류 없이 두 서비스를 출력했습니다. 무엇을 확인한 건가요?

::option[두 컨테이너가 시작되었습니다.]{#compose-files-config-scope-a explanation="이 명령은 설정을 읽어 화면에 표시합니다."}
::option[브라우저가 성공 응답을 받았습니다.]{#compose-files-config-scope-c explanation="서버를 시작한 뒤에 요청을 보내 확인할 수 있습니다."}
::option[Compose가 두 서비스 정의를 읽을 수 있습니다.]{#compose-files-config-scope-b .correct explanation="서비스를 시작하기 전에 Compose가 읽은 설정을 확인할 수 있습니다."}
:::

## 요약

이제 간단한 Compose 파일에서 각 부분의 역할을 알 수 있습니다.

1. services에서 서비스 이름과 이미지 지정을 읽습니다.
2. 서비스 설정이 컨테이너의 어느 부분에 해당하는지 확인합니다.
3. docker compose config로 Compose가 읽은 설정을 살펴봅니다.
