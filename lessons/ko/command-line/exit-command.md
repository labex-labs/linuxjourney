---
lesson_id: "exit-command"
course_id: "command-line"
lang: "ko"
order_index: 19
title: "exit"
description: "현재 쉘을 종료하고 호출자에게 반환할 상태를 선택하는 방법을 배웁니다."
meta_title: "exit - 명령줄"
meta_description: "Linux exit 명령어 사용법, 셸 세션 종료 방법, logout과 exit의 차이점, 종료 상태 값 작동 방식을 배워보세요."
meta_keywords: "exit 명령어, 리눅스 exit, logout 명령어, 셸 세션, 터미널 종료, 종료 상태, bash exit"
---

쉘은 중첩될 수 있습니다. 그래픽 터미널은 쉘을 시작하고, SSH 연결은 원격 쉘을 시작하며, 한 쉘이 다른 쉘을 시작할 수도 있습니다. 쉘 하나를 종료하면 보통 현재 쉘을 시작한 대상에 제어권이 돌아갑니다.

## 현재 쉘 종료하기

셸 세션을 종료하는 가장 일반적인 방법은 `exit` 명령어를 사용하는 것입니다. `exit`를 입력하고 Enter 키를 누르면 현재 셸 프로세스가 종료됩니다. 이 명령어는 거의 모든 셸 환경에서 작동합니다.

```bash
$ exit
```

현재 쉘이 그래픽 터미널 탭의 주 프로세스라면 터미널 설정에 따라 탭이 닫힐 수 있습니다. SSH에서는 원격 쉘을 나가 로컬 쉘로 돌아가고, 중첩 쉘에서는 상위 쉘로 돌아갑니다.

:::single-choice{#leave-current-shell}
다른 쉘 안에서 Bash를 시작했고 이제 상위 쉘로 돌아가려 합니다. 중첩된 Bash에서 어떤 명령어를 실행해야 하나요?

::option[`clear`]{#clear-nested explanation="`clear`는 보이는 터미널 영역을 새로 고치지만 현재 쉘은 계속 실행합니다."}
::option[`exit`]{#exit-nested .correct explanation="`exit`는 현재 쉘을 종료해 상위 쉘이 다시 실행되게 합니다."}
::option[`history -c`]{#clear-nested-history explanation="Bash의 메모리 내 히스토리를 지울 뿐 현재 쉘을 종료하지 않습니다."}
:::

## 종료 상태 반환하기

`exit` 명령어는 상태 코드도 반환할 수 있습니다. 상태 코드가 `0`이면 보통 성공을 의미하고, 0이 아닌 값은 오류나 특별한 조건을 나타냅니다.

```bash
$ exit 0
```

관례상 `0`은 성공을, 0이 아닌 값은 실패나 프로그램이 정의한 다른 조건을 뜻합니다. Bash에 숫자를 주지 않으면 `exit` 직전에 실행한 마지막 명령어의 상태로 종료합니다.

:::single-choice{#return-success-status}
현재 쉘을 종료하면서 호출자에게 성공을 명시적으로 알리는 명령어는 무엇인가요?

::option[`exit 0`]{#exit-zero .correct explanation="상태 `0`은 관례상 호출자에게 성공적인 완료를 나타냅니다."}
::option[`exit 1`]{#exit-one explanation="0이 아닌 상태는 관례상 성공이 아니라 실패나 다른 예외 조건을 나타냅니다."}
::option[`logout 0`]{#logout-zero explanation="Bash `logout`은 로그인 쉘용이며 이 형식으로 요청한 상태를 지정하지 않습니다."}
:::

:::single-choice{#exit-without-number}
Bash에서 숫자를 지정하지 않은 `exit`는 어떤 상태를 반환하나요?

::option[항상 성공 상태 `0`을 반환합니다.]{#always-zero explanation="성공 관례가 숫자 없는 `exit`를 항상 0으로 만들지는 않으며 Bash는 이 경우 이전 상태를 유지합니다."}
::option[항상 실패 상태 `1`을 반환합니다.]{#always-one explanation="Bash는 숫자 없는 모든 `exit`에 실패 상태 1을 부여하지 않으며 이전 명령어가 값을 결정합니다."}
::option[이전 명령어의 종료 상태를 반환합니다.]{#last-command-status .correct explanation="명시적인 숫자가 없으면 Bash는 가장 최근 명령어의 상태로 종료합니다."}
:::

## 로그인 쉘에서 logout 사용하기

`logout`은 Bash 로그인 쉘을 종료하도록 설계된 내장 명령어입니다.

```bash
$ logout
```

로그인 쉘이 아닌 Bash에서는 로그인 쉘이 아니라는 오류를 표시하므로 대신 `exit`를 사용합니다.

:::single-choice{#leave-login-shell}
로그인 쉘을 종료하도록 특별히 마련된 Bash 내장 명령어는 무엇인가요?

::option[`logout`]{#logout-login .correct explanation="Bash는 로그인 쉘을 종료하기 위해 `logout`을 제공합니다."}
::option[`unalias`]{#unalias-login explanation="`unalias`는 현재 쉘에서 별칭 정의를 제거할 뿐 세션을 종료하지 않습니다."}
::option[`source`]{#source-login explanation="`source`는 파일의 명령어를 현재 쉘로 읽으며 쉘을 종료하지 않습니다."}
:::

## Ctrl+D 사용 또는 터미널 닫기

빈 대화형 프롬프트에서 `Ctrl+D`를 누르면 보통 터미널의 입력 끝 문자를 제공합니다. Bash는 이를 흔히 종료 요청으로 해석합니다. 이는 신호가 아니며 Bash의 `ignoreeof` 같은 설정에 따라 동작이 달라질 수 있습니다.

그래픽 터미널 창을 닫으면 터미널 애플리케이션이 프로세스들을 닫도록 요청해 실행 중인 작업에 영향을 줄 수 있습니다. 가능하면 정상적인 `exit`를 사용하고 세션을 닫기 전에 활성 작업을 확인하세요.

## 요약

이제 현재 쉘을 종료하고 완료 상태를 전달할 수 있습니다.

1. `exit`로 현재 쉘의 호출자에게 돌아갈 수 있습니다.
2. 성공에는 `0`, 그 밖에는 정의된 0이 아닌 상태를 전달할 수 있습니다.
3. 숫자 없는 `exit`가 사용하는 상태를 이해할 수 있습니다.
4. 로그인 쉘에서만 `logout`을 사용할 수 있습니다.
5. `Ctrl+D`가 신호가 아니라 입력 끝임을 알아볼 수 있습니다.
