---
index: 5
lang: "ko"
title: "env (환경)"
meta_title: "env (환경) - Text-Fu"
meta_description: "Linux 에서 env 명령어가 무엇을 하는지 알아보세요. 이 가이드는 env 리눅스 명령어를 사용하여 PATH, HOME, USER 와 같은 리눅스 환경 변수를 보고 사용하는 방법을 설명합니다."
meta_keywords: "env, 리눅스 env, env 리눅스, env 명령어 리눅스, 리눅스 env 명령어, 리눅스에서 env 는 무엇을 하는가, 환경 변수, PATH 변수, 셸 변수"
---

## Lesson Content

Linux 시스템은 셸과 다른 프로세스가 접근할 수 있는 정보를 저장하기 위해 환경 변수를 사용합니다. 이 변수들에는 사용자 세션 및 시스템 구성에 대한 유용한 데이터가 포함되어 있습니다.

### 기본 환경 변수 탐색

`$` 기호를 변수 이름 앞에 붙여 특정 변수의 값을 볼 수 있습니다. 예를 들어, 다음 명령을 실행해 보세요.

```bash
echo $HOME
```

이 명령은 홈 디렉터리의 경로를 표시하며, `/home/pete`와 유사하게 보일 수 있습니다.

이제 다른 변수를 시도해 보세요.

```bash
echo $USER
```

이것은 현재 사용자 이름을 출력합니다. 하지만 이 정보는 어디서 오는 것일까요? 셸 환경에 저장되어 있습니다.

### Linux 에서 env 는 무엇을 하는가

현재 세션에 설정된 모든 환경 변수를 보려면 `env` 명령을 사용할 수 있습니다. `linux env command`는 셸 구성을 검사하는 기본적인 도구입니다.

```bash
env
```

`env` 명령을 실행하면 키 - 값 쌍 목록이 출력됩니다. 표시될 수 있는 내용의 짧은 예는 다음과 같습니다.

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

`linux env`를 이해하는 것은 시스템을 효과적으로 관리하는 데 매우 중요합니다.

### PATH 변수의 중요성

`env linux` 출력에서 가장 중요한 변수 중 하나는 `PATH`입니다. 다음을 사용하여 내용을 구체적으로 볼 수 있습니다.

```bash
echo $PATH
```

이 명령은 콜론으로 구분된 디렉터리 목록을 반환합니다. 명령을 입력하면 시스템은 해당 실행 파일을 찾기 위해 이 디렉터리들을 검색합니다.

수동으로 `/opt/coolapp/bin`과 같은 비표준 디렉터리에 프로그램을 설치했다고 가정해 봅시다. `coolcommand`를 입력하여 실행하려고 하면 "command not found" 오류가 발생할 수 있습니다. 이는 프로그램을 포함하는 디렉터리가 `PATH` 변수에 나열되어 있지 않아 셸이 어디서 찾아야 할지 모르기 때문에 발생합니다.

이 문제를 해결하려면 `PATH` 변수를 수정하여 새 디렉터리를 포함시켜야 합니다. 사용자 지정 디렉터리를 `PATH`에 추가하면 셸이 터미널 어디에서든 프로그램을 찾고 실행할 수 있게 됩니다.

### 현재 세션에 대한 환경 변수 설정

터미널에서 다음 명령을 실행하면 현재 세션에 대해서만 환경 변수 `TEST`가 설정됩니다.

```bash
export TEST=test
```

이후 다음을 실행하면:

```bash
echo $TEST
```

출력은 다음과 같습니다.

```
test
```

이 변수는 터미널 세션이 열려 있는 동안 사용할 수 있습니다. 터미널을 닫고 다시 열면 변수는 더 이상 존재하지 않습니다.

### 세션 간 환경 변수 영구화

환경 변수를 터미널 세션을 닫고 다시 열어도 모든 터미널 세션에서 사용할 수 있도록 하려면 셸 시작 파일에 추가해야 합니다. Bash(많은 Linux 배포판 및 macOS 의 기본 셸) 의 경우 이 파일은 일반적으로 홈 디렉터리의 `.bashrc`입니다.

다음은 그 방법입니다.

1.  선호하는 텍스트 편집기로 `.bashrc`를 엽니다. 예를 들면 다음과 같습니다.

        ```bash

    nano ~/.bashrc
    ```

2.  파일 끝에 `export` 줄을 추가합니다.

        ```bash

    export TEST=test
    ```

3.  편집기를 저장하고 종료합니다 (Nano 의 경우 `Ctrl+X`, 확인을 위해 `Y`, 그리고 `Enter`).

4.  변경 사항을 터미널을 다시 열지 않고 즉시 적용하려면 다음을 실행합니다.

        ```bash

    source ~/.bashrc
    ```

이후 `TEST` 변수는 모든 향후 터미널 세션에서 사용할 수 있으며, 터미널을 닫고 다시 열어도 `echo $TEST`를 실행하면 `test`가 출력됩니다.

### 셸 구성 파일에 대한 참고 사항

- **Bash** (많은 시스템의 기본값) 의 경우 관련 파일은 비로그인 대화형 셸에 대해 `~/.bashrc`입니다.
- **Zsh**의 경우 동등한 파일은 일반적으로 `~/.zshrc`입니다.
- **Fish**의 경우 일반적으로 `~/.config/fish/config.fish`를 사용합니다.

## Exercise

연습이 완벽을 만듭니다! Linux 환경 변수에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux 에서 셸 환경 및 구성 관리](https://labex.io/ko/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - 로컬 및 환경 변수 생성 및 관리, 상속 이해, `.bashrc` 파일을 수정하여 구성을 영구화하는 방법을 연습합니다.
2. **[Linux 환경 변수](https://labex.io/ko/labs/linux-environment-variables-in-linux-385274)** - 환경 변수의 개념과 사용법, 생성, 수정 및 관리 방법, 시스템 구성에서의 역할에 대해 알아봅니다.
3. **[Linux 환경 변수 구성](https://labex.io/ko/labs/linux-configure-linux-environment-variables-437861)** - Linux 시스템에서 환경 변수를 생성, 설정 및 관리하는 실습 경험을 얻습니다.

이 랩들은 실제 시나리오에서 개념을 적용하고 Linux 셸 환경을 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

현재 모든 환경 변수를 표시하는 명령은 무엇입니까? (영어와 소문자 명령 이름만 사용하여 답변하십시오).

## Quiz Answer

env
