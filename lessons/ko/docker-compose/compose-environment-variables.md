---
lesson_id: "compose-environment-variables"
course_id: "docker-compose"
lang: "ko"
order_index: 5
title: "환경 변수"
description: "Compose 파일에 값을 채워 넣는 일과 컨테이너에 값을 전달하는 일을 구분하는 방법을 알아봅니다."
meta_title: "환경 변수 - Docker Compose"
meta_description: "Compose 파일에 값을 채워 넣는 일과 컨테이너에 값을 전달하는 일을 구분하는 방법을 알아봅니다."
meta_keywords: "환경 변수, 변수 치환, Docker Compose, DevOps, Linux Journey"
---

환경 변수는 프로그램에서 읽을 수 있는 이름이 붙은 값입니다. Compose는 파일을 읽을 때 설정에 값을 채워 넣을 수도 있고, 컨테이너 안의 프로그램에 값을 전달할 수도 있습니다.

## 파일에 값을 채워 넣기

실습 폴더에 예시를 `compose.env.yaml`로 저장합니다. 이 파일에서 `${PAGE_MODE:-demo}`는 `PAGE_MODE`가 설정되어 있고 비어 있지 않으면 그 값을 사용하고, 그렇지 않으면 `demo`를 사용한다는 뜻입니다.

```yaml
services:
  toolbox:
    image: busybox:1.36
    environment:
      PAGE_MODE: "${PAGE_MODE:-demo}"
```

Compose는 컨테이너를 만들기 전에 식을 값으로 바꿉니다. 이를 **변수 치환**이라고 합니다. 다른 파일에서는 같은 방식으로 호스트 포트나 이미지 태그를 고를 수도 있습니다.

:::single-choice{#compose-environment-variables-interpolate-default} PAGE_MODE가 설정되지 않았다면 출력된 설정에 어떤 값이 표시되나요?

::option[파일에 적힌 식이 그대로 표시됩니다.]{#compose-environment-variables-interpolate-default-a explanation="Compose는 파일을 읽을 때 식을 값으로 바꿉니다."}
::option[자동으로 생성한 컨테이너 이름입니다.]{#compose-environment-variables-interpolate-default-c explanation="컨테이너 이름과 환경 변수의 값은 별도로 설정합니다."}
::option[기본값 연산자 뒤의 demo입니다.]{#compose-environment-variables-interpolate-default-b .correct explanation="이 식은 값이 없을 때 사용할 값으로 demo를 지정합니다."}
:::

## 치환된 값 확인하기

명령 앞에 변수 대입을 쓰면 그 명령을 한 번 실행하는 동안만 변수에 값이 설정됩니다. 다른 값으로 설정이 어떻게 달라지는지 확인하세요. `config`는 치환된 설정을 출력하며 컨테이너는 만들지 않습니다.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml config
```

서비스의 환경 설정에서 `PAGE_MODE: review`를 찾으세요. `review`는 실습용 값입니다. 예시 설정이나 화면에 표시하는 출력에 비밀 정보를 넣지 마세요.

:::single-choice{#compose-environment-variables-config-scope} 출력된 설정에 review가 나옵니다. 지금까지 어떤 일이 있었나요?

::option[그 값으로 서비스가 이미 시작되었습니다.]{#compose-environment-variables-config-scope-b explanation="설정을 출력하는 일과 컨테이너를 시작하는 일은 별도 작업입니다."}
::option[Compose가 설정을 읽으면서 값을 치환했습니다.]{#compose-environment-variables-config-scope-a .correct explanation="config는 서비스를 시작하기 전에 치환된 설정을 보여 줍니다."}
::option[기존 컨테이너가 모두 그 값을 사용하게 되었습니다.]{#compose-environment-variables-config-scope-c explanation="이 명령은 실행 중인 컨테이너를 바꾸지 않습니다."}
:::

## 컨테이너에 값 전달하기

`environment` 섹션은 치환된 값을 새 컨테이너에 전달합니다. `printenv`를 사용해 이번 실행을 위해 만든 컨테이너 안에서 값을 출력합니다.

```bash
$ PAGE_MODE=review docker compose -p journey-env -f compose.env.yaml run --rm toolbox printenv PAGE_MODE
```

`review`가 표시됩니다. 변수 치환으로 값이 정해졌고, 환경 설정이 그 값을 컨테이너에 전달했습니다. 호스트 포트를 고르는 데만 쓰인 변수는 프로그램의 환경에 자동으로 들어가지 않습니다.

:::single-choice{#compose-environment-variables-actual-value} 도구 컨테이너의 프로그램이 받은 값은 어떻게 확인하나요?

::option[컨테이너 안에서 PAGE_MODE를 출력합니다.]{#compose-environment-variables-actual-value-c .correct explanation="프로그램의 환경을 직접 보면 실제로 어떤 값을 받았는지 알 수 있습니다."}
::option[원래 파일에서 기본값만 확인합니다.]{#compose-environment-variables-actual-value-a explanation="다른 값이 파일에 적힌 기본값을 대신할 수 있습니다."}
::option[도구 컨테이너의 IP 주소를 찾습니다.]{#compose-environment-variables-actual-value-b explanation="주소로는 프로그램 설정을 알 수 없습니다."}
:::

## 요약

이제 환경 변수의 두 가지 쓰임을 구분할 수 있습니다.

1. Compose 파일에서 기본값을 지정하는 식을 읽습니다.
2. 컨테이너를 시작하기 전에 치환된 설정을 확인합니다.
3. 실행한 프로그램의 환경에서 값을 확인합니다.
