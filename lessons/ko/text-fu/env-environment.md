---
lesson_id: "env-environment"
course_id: "text-fu"
lang: "ko"
order_index: 5
title: "env (환경)"
description: "Bash에서 환경 변수를 확장하고 내보내고 확인하며 일시적으로 재정의하는 방법을 배웁니다."
meta_title: "env (환경) - Text-Fu"
meta_description: "Linux 에서 env 명령어가 무엇을 하는지 알아보세요. 이 가이드는 env 리눅스 명령어를 사용하여 PATH, HOME, USER 와 같은 리눅스 환경 변수를 보고 사용하는 방법을 설명합니다."
meta_keywords: "env, 리눅스 env, env 리눅스, env 명령어 리눅스, 리눅스 env 명령어, 리눅스에서 env 는 무엇을 하는가, 환경 변수, PATH 변수, 셸 변수"
---

모든 프로세스에는 상위 프로세스에서 물려받은 이름-값 문자열 모음인 환경이 있습니다. 쉘은 환경 변수로 언어 설정이나 실행 파일 검색 경로 같은 구성을 시작하는 프로그램에 전달합니다.

## Bash에서 변수 값 확장하기

Bash는 명령어를 실행하기 전에 `$NAME` 또는 `${NAME}`을 변수 값으로 확장합니다. 값을 하나의 인자로 보존하려면 확장을 따옴표로 묶습니다.

```bash
$ printf '%s\n' "$HOME"
/home/pete
```

자주 쓰는 환경 변수는 다음과 같습니다.

- `HOME`: 현재 사용자의 홈 디렉터리 경로
- `USER`: 여러 시스템에서 로그인 환경이 제공하는 사용자 이름
- `PWD`: 쉘의 현재 작업 디렉터리
- `PATH`: 명령어 이름을 검색할 디렉터리

값은 현재 프로세스 환경에 따라 달라지며 보편적인 상수가 아닙니다. 더 엄격한 쉘 동작을 켜지 않았다면 설정되지 않은 변수는 빈 문자열로 확장됩니다.

:::single-choice{#env-print-home-value}
`HOME` 값을 하나의 인자로 보존하면서 출력하는 Bash 명령어는 무엇인가요?

::option[`printf '%s\n' '$HOME'`]{#env-literal-home explanation="작은따옴표는 매개변수 확장을 막으므로 문자 그대로 `$HOME`을 출력합니다."}
::option[`printf '%s\n' "$HOME"`]{#env-quoted-home .correct explanation="Bash는 큰따옴표 안에서 `$HOME`을 확장하고 `printf`는 전체 값을 한 인자로 받습니다."}
::option[`printf '%s\n' HOME`]{#env-name-home explanation="달러 기호나 매개변수 구문이 없는 `HOME`은 변수 확장이 아니라 일반 텍스트입니다."}
:::

## 현재 환경 확인하기

현재 세션에 설정된 모든 환경 변수를 보려면 `env` 명령을 사용할 수 있습니다. `linux env command`는 셸 구성을 검사하는 기본적인 도구입니다.

```bash
$ env
```

`env` 명령을 실행하면 키 - 값 쌍 목록이 출력됩니다. 표시될 수 있는 내용의 간단한 예는 다음과 같습니다.

```plaintext
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/bin
PWD=/home/user
USER=pete
```

환경 변수에는 자격 증명, 토큰, 내부 경로나 그 밖의 민감한 데이터가 들어 있을 수 있습니다. 전체 `env` 출력을 검토하고 가리지 않은 채 공개 이슈나 로그에 붙여 넣지 마세요.

:::single-choice{#env-list-exported-values}
새로 시작한 프로세스에 보이는 환경을 출력하는 명령어는 무엇인가요?

::option[`env`]{#env-print-all .correct explanation="명령어나 할당 없이 실행한 `env`는 자신이 받은 이름-값 환경을 출력합니다."}
::option[`alias`]{#env-alias-list explanation="`alias`는 내보낸 환경 레코드가 아니라 쉘 상태인 별칭 정의를 나열합니다."}
::option[`history`]{#env-history-list explanation="`history`는 쉘이 기억하는 명령줄을 표시하며 내보낸 변수를 나열하지 않습니다."}
:::

## PATH로 명령어 찾기

`env linux` 출력에서 가장 중요한 변수 중 하나는 `PATH`입니다. 다음을 사용하여 내용을 구체적으로 볼 수 있습니다.

```bash
$ printf '%s\n' "$PATH"
```

`PATH`는 명령어 이름에 슬래시가 없을 때 Bash가 검색하는 콜론 구분 디렉터리 목록입니다. 순서가 중요하며 Bash는 이름 해석 규칙에 따라 처음 찾은 적합한 명령어를 사용합니다. 현재 쉘의 해석을 보려면 `type -a NAME`을 사용합니다.

기존 검색 경로를 보존하면서 현재 쉘과 이후 자식 프로세스에 `/opt/coolapp/bin`을 앞에 추가합니다.

```bash
$ export PATH="/opt/coolapp/bin:$PATH"
```

실수로 `PATH`를 새 디렉터리 하나로 교체하거나 신뢰할 수 없는 쓰기 가능 디렉터리를 추가하지 마세요. 정상 명령어를 찾지 못하게 하거나 예상하지 않은 실행 파일이 실행될 수 있습니다.

:::single-choice{#env-prepend-path-directory}
현재 Bash와 이후 자식 프로세스의 기존 `PATH` 앞에 `/opt/coolapp/bin`을 추가하는 명령어는 무엇인가요?

::option[`export PATH="/opt/coolapp/bin"`]{#env-replace-path explanation="기존 검색 디렉터리를 모두 버려 일반 명령어를 찾기 어려워질 수 있습니다."}
::option[`export PATH="/opt/coolapp/bin:$PATH"`]{#env-export-path .correct explanation="새 디렉터리를 앞에 추가하고 기존 값을 유지하며 결과를 자식 프로세스에 내보냅니다."}
::option[`PATH='$PATH:/opt/coolapp/bin'`]{#env-literal-path explanation="작은따옴표가 문자 그대로 `$PATH`를 보존하고 이후 자식 프로세스에 내보내지도 않습니다."}
:::

## 자식 프로세스에 변수 내보내기

터미널에서 다음 명령을 실행하면 현재 세션에 대해서만 환경 변수 `TEST`가 설정됩니다.

```bash
$ export TEST=test
```

Bash 변수는 자동으로 자식 프로세스의 환경에 들어가지 않습니다. `export`로 이름을 내보내도록 표시합니다.

```bash
$ printenv TEST
test
```

현재 Bash에는 `TEST` 변수가 있고 시작하는 명령어는 `TEST=test`를 물려받습니다. 자식 프로세스가 이 방식으로 상위 환경을 바꿀 수는 없습니다. 할당은 보통 `unset`하거나 쉘이 종료될 때까지 유지되며 시스템 전체 환경을 수정하지 않습니다.

:::single-choice{#env-export-inheritance}
Bash에서 `export TEST=test`의 주된 효과는 무엇인가요?

::option[모든 사용자의 시스템 설정에 `TEST`를 씁니다.]{#env-system-wide explanation="현재 쉘과 자식의 상속에만 영향을 주며 모든 사용자나 운영체제 전체에는 적용되지 않습니다."}
::option[이후 자식 프로세스가 `TEST=test`를 물려받도록 표시합니다.]{#env-child-inheritance .correct explanation="`export`는 Bash가 시작하는 명령어에 전달할 환경에 쉘 변수를 추가합니다."}
::option[이미 실행 중인 프로세스의 환경을 바꿉니다.]{#env-existing-processes explanation="기존 프로세스는 각자의 환경을 유지하며 export는 이후 시작되는 프로세스에 영향을 줍니다."}
:::

## 한 명령어에만 값 설정하기

명령어 앞에 할당을 두면 해당 명령어의 환경에만 값을 제공합니다.

```bash
$ LANG=C sort names.txt
```

현재 쉘의 `LANG` 값은 영구적으로 바뀌지 않습니다. `env` 유틸리티는 또 다른 명시적인 형식을 제공합니다.

```bash
$ env LANG=C sort names.txt
```

`env -i COMMAND`는 처음에 빈 환경으로 명령어를 시작한 뒤 필요한 할당만 추가할 때 사용합니다. 여러 프로그램이 환경 값에 의존하므로 의도적으로 사용하세요.

:::single-choice{#env-one-command-value}
현재 쉘의 `LANG`을 영구 변경하지 않고 `LANG=C`로 `sort names.txt`를 실행하는 명령어는 무엇인가요?

::option[`env LANG=C sort names.txt`]{#env-lang-sort .correct explanation="`env`는 시작하는 명령어의 환경에 할당을 추가하고 상위 쉘은 이전 값을 유지합니다."}
::option[`export LANG=C; sort names.txt`]{#env-export-lang explanation="현재 쉘에서 `LANG=C`를 내보내므로 `sort`가 끝난 뒤에도 값이 바뀐 채로 남습니다."}
::option[`env -i sort names.txt`]{#env-empty-sort explanation="빈 환경으로 시작하지만 요청한 `LANG=C` 값을 설정하지 않습니다."}
:::

## 이후 세션에 개인 값 불러오기

이후 대화형 Bash 세션에 내보낸 변수를 다시 만들려면 해당 세션이 실제로 읽는 시작 파일에 적절한 `export` 줄을 둡니다. 대화형 비로그인 Bash에서는 흔히 `~/.bashrc`입니다.

```bash
export TEST=test
```

Zsh는 흔히 `~/.zshrc`를 사용하고 Fish는 다른 구문과 설정을 사용합니다. 로그인 및 비대화형 쉘은 다른 파일을 읽을 수 있으므로 한 파일이 모든 프로세스를 설정한다고 가정하지 말고 쉘과 세션 유형을 확인하세요.

환경 상속과 쉘 설정은 다음 실습에서 연습해 보세요.

1. **[Linux 에서 셸 환경 및 구성 관리](https://labex.io/ko/labs/comptia-manage-shell-environment-and-configuration-in-linux-590838)** - 로컬 및 환경 변수 생성 및 관리, 상속 이해, `.bashrc` 파일을 수정하여 구성을 영구화하는 방법을 연습합니다.
2. **[Linux 의 환경 변수](https://labex.io/ko/labs/linux-environment-variables-in-linux-385274)** - 환경 변수의 개념과 사용법, 환경 변수를 생성, 수정 및 관리하는 방법, 시스템 구성에서 환경 변수의 역할에 대해 알아봅니다.
## 요약

이제 Bash가 자식 프로세스에 전달하는 환경을 확인하고 제어할 수 있습니다.

1. 의도적인 따옴표로 변수 값을 확장할 수 있습니다.
2. 비밀을 노출하지 않고 내보낸 값을 검토할 수 있습니다.
3. `PATH`에서 명령어 디렉터리를 보존하고 순서를 정할 수 있습니다.
4. 이후 자식 프로세스에 쉘 변수를 내보낼 수 있습니다.
5. 상위 쉘을 바꾸지 않고 한 명령어의 값을 재정의할 수 있습니다.
