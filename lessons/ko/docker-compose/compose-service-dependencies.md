---
lesson_id: "compose-service-dependencies"
course_id: "docker-compose"
lang: "ko"
order_index: 6
title: "서비스 의존 관계"
description: "의존하는 서비스를 먼저 시작하는 것과 그 서비스가 요청에 응답할 준비가 되는 것의 차이를 알아봅니다."
meta_title: "서비스 의존 관계 - Docker Compose"
meta_description: "의존하는 서비스를 먼저 시작하는 것과 그 서비스가 요청에 응답할 준비가 되는 것의 차이를 알아봅니다."
meta_keywords: "서비스 의존 관계, 상태 검사, 시작 순서, Docker Compose, DevOps, Linux Journey"
---

웹 서버가 필요한 보조 프로그램은 두 서비스가 올바른 순서로 시작되어도 첫 요청을 너무 일찍 보낼 수 있습니다. **상태 검사**는 Docker가 실행하는 짧은 테스트입니다. 예를 들어 서비스가 HTTP 요청에 응답할 수 있는지 확인합니다.

## 준비 상태 검사 고르기

이 별도 예제에서는 웹 컨테이너 안에서 검사를 실행합니다. 컨테이너 내부에서 웹 페이지를 요청합니다. 요청이 성공하면 그 위치에서 서버가 응답한다는 사실을 Docker가 확인할 수 있습니다.

```yaml
services:
  web:
    image: nginx:alpine
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1/"]
      interval: 3s
      timeout: 2s
      retries: 5
  toolbox:
    image: busybox:1.36
    command: ["sleep", "3600"]
    depends_on:
      web:
        condition: service_healthy
```

이 예시를 같은 실습 폴더에 `compose.health.yaml`로 저장합니다. 상태 검사는 일정 간격으로 실행되고 시도마다 제한 시간이 있습니다. 웹 컨테이너 내부에서 응답을 확인하는 검사입니다.

:::single-choice{#compose-service-dependencies-check-location} 이 상태 검사에서 wget은 어디에서 실행되나요?

::option[웹 컨테이너 안에서 실행됩니다.]{#compose-service-dependencies-check-location-c .correct explanation="루프백 URL로 보내는 요청은 이 컨테이너 안에서 실행합니다."}
::option[호스트의 브라우저에서 실행됩니다.]{#compose-service-dependencies-check-location-a explanation="Docker가 웹 서비스 정의에 따라 명령을 실행합니다."}
::option[도구 컨테이너 안에서 실행됩니다.]{#compose-service-dependencies-check-location-b explanation="검사는 web 아래에 정의되어 있습니다."}
:::

## 의존 대상이 정상 상태가 될 때까지 기다리기

`service_healthy` 조건을 지정하면 Compose는 상태 검사가 성공한 뒤에 그 서비스에 의존하는 도구 컨테이너를 시작합니다. 시작 순서만 설정하면 의존 대상이 실행되자마자 다음 컨테이너가 시작될 수 있습니다. 아직 첫 요청에 응답할 수 없는 시점일 수도 있습니다.

```bash
$ docker compose -p journey-health -f compose.health.yaml up -d
$ docker compose -p journey-health -f compose.health.yaml ps
```

목록에서 web의 상태가 정상이고 도구 컨테이너가 실행 중인지 확인하세요.

:::single-choice{#compose-service-dependencies-ready-condition} 웹 프로세스가 시작됐지만 컨테이너 내부 요청은 아직 실패합니다. 도구 컨테이너를 기다리게 하려면 어떤 조건을 써야 하나요?

::option[시작 순서만 지정합니다.]{#compose-service-dependencies-ready-condition-b explanation="web이 먼저 시작해도 응답할 때까지 시간이 걸릴 수 있습니다."}
::option[백그라운드 모드를 선택합니다.]{#compose-service-dependencies-ready-condition-c explanation="백그라운드 모드는 터미널이 대기하는 방식에 영향을 줍니다. 서비스가 준비됐는지는 판단하지 않습니다."}
::option[service_healthy 조건을 지정합니다.]{#compose-service-dependencies-ready-condition-a .correct explanation="이 조건을 적용하면 상태 검사 결과를 기다립니다."}
:::

![의존 대상인 웹 서비스는 정상이고, 도구 컨테이너는 실행 중인 Compose 상태 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/docker-compose/compose-service-dependencies/healthy-dependency.png)

## 나중에 발생한 장애에 대응하기

Compose의 시작 조건은 서비스가 처음 시작될 때의 순서를 정합니다. 처음에 정상 상태였던 서비스도 나중에 응답을 멈출 수 있습니다. 클라이언트는 요청 실패를 처리하고, 의존 대상이 다시 준비되면 연결을 재시도할 수 있어야 합니다. 현재 서비스 상태를 살펴보고 직접 요청을 보내 동작을 확인하세요.

:::single-choice{#compose-service-dependencies-later-failure} 두 서비스가 시작된 지 한 시간 뒤에 요청이 실패했습니다. 지금 무엇을 확인하면 도움이 되나요?

::option[시작 당시의 순서만 확인합니다.]{#compose-service-dependencies-later-failure-a explanation="시작할 때 어떤 일이 일어났는지만 보여 줍니다."}
::option[현재 상태 검사 결과와 의존하는 서비스에서 보낸 요청 결과를 확인합니다.]{#compose-service-dependencies-later-failure-b .correct explanation="두 결과로 서비스가 현재 어떤 상태인지, 클라이언트가 사용하는 경로가 동작하는지 확인할 수 있습니다."}
::option[Docker 캐시에 있는 이미지 수를 확인합니다.]{#compose-service-dependencies-later-failure-c explanation="이미지 수로는 실행 중인 서비스의 응답을 알기 어렵습니다."}
:::

## 두 위치에서 확인하기

내부 상태 검사가 성공하면 웹 컨테이너에서 무엇에 접근할 수 있는지 알 수 있습니다. 도구 컨테이너가 접속하려면 프로젝트 네트워크와 접속 가능한 서비스 주소가 여전히 필요합니다. 상태 검사 결과와 도구 컨테이너에서 보낸 요청 결과는 따로 확인하세요.

:::single-choice{#compose-service-dependencies-final-application} 웹 서비스는 정상으로 표시되지만 도구 컨테이너의 요청은 실패합니다. 어떤 비교를 하면 문제가 발생한 위치를 좁힐 수 있나요?

::option[처음 시작한 시각만 확인합니다.]{#compose-service-dependencies-final-application-b explanation="시작 시각으로는 지금 어느 경로가 동작하는지 알 수 없습니다."}
::option[web이 정상으로 표시되므로 두 요청이 모두 성공했다고 판단합니다.]{#compose-service-dependencies-final-application-c explanation="상태 검사는 한 위치에서 관찰한 결과를 보여 줍니다."}
::option[web 내부에서 보낸 요청과 도구 컨테이너에서 web으로 보낸 같은 요청을 비교합니다.]{#compose-service-dependencies-final-application-a .correct explanation="서비스 자체에서 응답할 수 있는지와 의존하는 서비스가 실제 사용하는 경로로 연결되는지를 비교할 수 있습니다."}
:::

## 요약

이제 상태 검사로 의존 대상이 요청에 응답할 준비가 됐는지 판단할 수 있습니다.

1. 상태 검사가 실제로 무엇을 확인하는지 파악합니다.
2. 시작 순서로 부족하다면 의존 대상의 정상 상태를 기다리는 조건을 선택합니다.
3. 서비스에서 나중에 장애가 발생하면 현재 동작을 확인합니다.
