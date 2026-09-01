---
lesson_id: "help-command"
course_id: "command-line"
lang: "ko"
order_index: 15
title: "help"
description: "명령어에 따라 내장 도움말, 프로그램 사용법 출력 또는 매뉴얼 페이지를 선택하는 방법을 배웁니다."
meta_title: "help - 커맨드 라인 도움말"
meta_description: "Bash help, --help 출력, man 페이지, 그리고 셸 내장 명령과 외부 명령에 대한 type 명령어를 통해 Linux 커맨드 라인 도움말을 얻는 방법을 배워보세요."
meta_keywords: "리눅스 도움말 명령어, bash 도움말, 커맨드 라인 도움말, --help, 셸 내장 명령어, man 명령어, type 명령어"
---

모든 명령어 옵션을 외울 필요는 없습니다. Bash와 설치된 여러 프로그램은 터미널에서 구문을 직접 설명하지만, 알맞은 도움말은 사용하는 명령어의 종류에 따라 달라집니다.

## Bash 내장 명령어 도움말 보기

`help`는 Bash 자체가 구현한 명령어를 설명하는 내장 명령어입니다. 예로 `cd`, `history`, `type`이 있습니다.

`help`를 사용하려면 내장 명령어 이름 뒤에 입력하세요.

```bash
$ help echo
```

출력은 내장 명령어의 구문과 동작을 설명합니다. 인자 없이 `help`를 실행하면 Bash가 도움말을 제공하는 내장 명령어 목록이 나옵니다.

:::single-choice{#help-for-bash-cd} Bash의 `cd` 내장 명령어 도움말을 표시하는 명령어는 무엇인가요?

::option[`cd --help`]{#cd-help-option explanation="일부 내장 명령어가 옵션을 인식할 수는 있지만 Bash의 전용 문서 인터페이스는 내장 명령어 이름 뒤에 쓰는 `help`입니다."}
::option[`help cd`]{#help-cd .correct explanation="Bash의 `help`는 지정한 내장 명령어의 문서를 찾으며 여기서는 `cd`를 조회합니다."}
::option[`type cd`]{#type-cd explanation="`type`은 Bash가 `cd`라는 이름을 어떻게 해석하는지 알려 줄 뿐 전체 도움말 항목을 표시하지 않습니다."}
:::

## 프로그램 사용법 요약 요청하기

셸에 내장되지 않은 대부분의 실행 가능한 프로그램에는 `help` 명령어가 작동하지 않습니다. 대신, 일반적인 관례로 `--help` 플래그를 제공합니다. 이 옵션은 프로그램에 사용법 요약을 출력하고 종료하도록 지시합니다.

```bash
$ ls --help
```

이 관례가 흔하지만 모든 프로그램이 지원하는 것은 아닙니다. 모든 프로그램이 같은 옵션을 받는다고 가정하지 말고 출력과 종료 상태를 확인하세요.

:::single-choice{#quick-ls-usage} 외부 `ls` 프로그램이 제공하는 빠른 사용법 요약을 보통 출력하는 명령어는 무엇인가요?

::option[`help ls`]{#bash-help-ls explanation="Bash `help`는 쉘 내장 명령어를 설명하므로 일반적인 시스템에서 외부 `ls`의 사용법 페이지를 제공하지 않습니다."}
::option[`ls --help`]{#ls-help .correct explanation="GNU `ls`는 일반적인 `--help` 관례에 따라 사용법과 옵션을 출력합니다."}
::option[`type --help ls`]{#type-help-ls explanation="이는 `ls`가 사용법을 설명하게 하는 대신 `type` 내장 명령어 자체의 옵션 처리를 요청합니다."}
:::

## Bash가 이름을 해석하는 방식 찾기

명령어가 Bash 내장인지 외부 프로그램인지 확실하지 않을 때는 `type`을 사용하세요.

```bash
$ type cd
cd is a shell builtin
$ type ls
ls is /usr/bin/ls
```

결과는 별칭, 함수, 설치된 프로그램과 `PATH`에 따라 달라질 수 있습니다. Bash가 먼저 사용할 하나뿐 아니라 알려진 모든 해석을 보려면 `type -a NAME`을 사용합니다.

:::single-choice{#identify-command-resolution} `deploy`가 별칭, 함수, 내장 명령어 또는 실행 파일인지 모릅니다. 이름이 어떻게 해석되는지 확인하는 Bash 명령어는 무엇인가요?

::option[`type deploy`]{#type-deploy .correct explanation="`type` 내장 명령어는 현재 쉘 환경에서 Bash가 명령어 이름을 어떻게 해석하는지 알려 줍니다."}
::option[`help deploy`]{#help-deploy explanation="`help`는 Bash 내장 명령어 문서를 찾으며 일반적으로 별칭, 함수, 외부 파일을 식별하지 않습니다."}
::option[`deploy --help`]{#deploy-help explanation="명령어 실행을 시도하며 자체 옵션 지원에 의존하므로 Bash가 이름을 어떻게 해석했는지 먼저 설명하지 않습니다."}
:::

## 상세 수준 선택하기

- `cd`, `echo`, `history` 같은 Bash 내장 명령어에는 `help COMMAND`를 사용하세요.
- 많은 외부 명령어에는 빠른 요약을 위해 `COMMAND --help`를 사용하세요.
- 자세한 매뉴얼 페이지가 필요하면 `man COMMAND`를 사용하세요.
- 한 줄 설명이 필요하면 `whatis COMMAND`를 사용하세요.

다음 강의에서는 매뉴얼 페이지와 한 줄 설명을 더 자세히 살펴봅니다.

:::single-choice{#choose-detailed-manual} 외부 명령어 `ls`의 짧은 사용법 요약이 아니라 자세한 문서가 필요합니다. 어떤 명령어를 시도해야 하나요?

::option[`man ls`]{#man-ls .correct explanation="`man ls`는 보통 구문, 옵션, 동작을 더 충실히 설명하는 설치된 매뉴얼 페이지를 엽니다."}
::option[`whatis ls`]{#whatis-ls explanation="`whatis`는 간결한 매뉴얼 페이지 설명을 표시하므로 요청한 상세 문서가 아닙니다."}
::option[`type ls`]{#type-ls explanation="`type`은 Bash가 `ls`를 해석하는 방식을 알려 줄 뿐 프로그램의 자세한 매뉴얼을 표시하지 않습니다."}
:::

## 요약

이제 Bash가 명령어를 해석하는 방식에 따라 도움말 출처를 선택할 수 있습니다.

1. Bash 내장 명령어에는 `help`를 사용할 수 있습니다.
2. 프로그램의 빠른 사용법에는 `--help`를 시도할 수 있습니다.
3. `type`으로 이름 해석 방식을 확인할 수 있습니다.
4. `man`으로 자세한 문서를 열 수 있습니다.
