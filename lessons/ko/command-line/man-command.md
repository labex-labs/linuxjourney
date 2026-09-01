---
lesson_id: "man-command"
course_id: "command-line"
lang: "ko"
order_index: 16
title: "man"
description: "설치된 매뉴얼 페이지를 열고 탐색하고 검색하며 섹션을 선택하는 방법을 배웁니다."
meta_title: "man - 명령어 매뉴얼"
meta_description: "Linux man 명령어를 사용하여 매뉴얼 페이지 읽기, 매뉴얼 내 검색, 섹션 이해 및 명령어 옵션 찾기를 예제로 배워보세요."
meta_keywords: "man 명령어, 리눅스 매뉴얼 페이지, 명령어 매뉴얼, man ls, man 섹션, 매뉴얼 페이지 검색, 명령어 도움말"
---

많은 리눅스 명령어, 인터페이스, 설정 파일과 관리 도구에는 매뉴얼 페이지 또는 man 페이지라는 참조 문서가 설치되어 있습니다. `man` 명령어는 이 페이지를 찾아 표시합니다.

## 매뉴얼 페이지 열기

어떤 명령어의 매뉴얼을 보려면 `man` 다음에 명령어 이름을 입력하세요. 예를 들어 `ls` 매뉴얼을 읽으려면 다음과 같이 입력합니다:

```bash
$ man ls
```

매뉴얼 페이지는 보통 개요, 설명, 옵션, 관련 파일과 상호 참조를 포함하지만 정확한 구성은 페이지마다 다릅니다.

:::single-choice{#open-ls-manual} 설치된 `ls` 매뉴얼 페이지를 여는 명령어는 무엇인가요?

::option[`help ls`]{#help-ls explanation="Bash `help`는 쉘 내장 명령어를 설명하며 보통 외부 `ls` 매뉴얼 페이지를 열지 않습니다."}
::option[`man ls`]{#manual-ls-page .correct explanation="`man`은 매뉴얼 데이터베이스에서 `ls` 주제를 찾아 일치하는 페이지를 표시합니다."}
::option[`ls --help`]{#ls-usage explanation="`ls` 자체의 사용법 요약을 요청할 뿐 설치된 매뉴얼 페이지를 열지 않습니다."}
:::

## 페이지 탐색 및 검색하기

man 페이지는 명령어 옵션을 이해하는 데 특히 유용합니다. 예를 들어 `ls -l`을 본 적이 있고 `-l`이 무엇을 의미하는지 알고 싶다면 `man ls`를 열고 `-l`을 검색하세요.

많은 시스템에서 `man`은 `less` 같은 페이저로 페이지를 표시합니다. 페이지 안에서는 다음 키를 사용할 수 있습니다.

- `/`를 누르고 검색어를 입력하여 앞으로 검색합니다.
- `n`을 눌러 다음 검색 결과로 이동합니다.
- `N`을 눌러 이전 검색 결과로 이동합니다.
- `q`를 눌러 종료합니다.

페이저는 시스템이나 환경에 따라 다를 수 있으므로 모든 곳에서 같은 키를 보장하지는 않습니다. 위 키는 일반적인 `less` 설정에 해당합니다.

:::single-choice{#search-man-page} `less`에서 man 페이지가 열린 상태로 `--recursive`를 앞으로 검색하려면 무엇을 입력하나요?

::option[`?--recursive`를 입력하고 Enter를 누릅니다.]{#backward-man-search explanation="물음표는 뒤로 검색을 시작하므로 요청한 방향과 반대입니다."}
::option[`/--recursive`를 입력하고 Enter를 누릅니다.]{#forward-man-search .correct explanation="슬래시는 `less`에서 앞으로 검색을 시작하고 Enter는 패턴을 제출합니다."}
::option[`n--recursive`를 입력하고 Enter를 누릅니다.]{#repeat-man-search explanation="`n`은 기존 검색을 반복하며 이 방식으로 새 검색 패턴을 시작하지 않습니다."}
:::

:::single-choice{#leave-man-page} 일반적인 페이저에서 man 페이지가 열린 상태로 쉘로 돌아가는 키는 무엇인가요?

::option[`G`]{#man-page-end explanation="대문자 `G`는 `less`에서 페이지 끝으로 이동할 뿐 페이저를 닫지 않습니다."}
::option[`n`]{#next-man-match explanation="`n`은 최근 검색을 반복하며 매뉴얼 페이지를 계속 열어 둡니다."}
::option[`q`]{#quit-man .correct explanation="`q`는 일반적인 페이저를 종료하고 쉘에 제어권을 돌려줍니다."}
:::

## 매뉴얼 섹션 선택하기

매뉴얼 페이지는 번호가 매겨진 섹션으로 구성되어 있습니다. 일반적인 섹션은 다음과 같습니다:

- `1`: 사용자 명령어.
- `2`: 시스템 호출.
- `3`: 라이브러리 함수.
- `5`: 파일 형식.
- `8`: 시스템 관리 명령어.

때때로 같은 이름이 여러 섹션에 존재할 수 있습니다. 이 경우 섹션 번호를 지정할 수 있습니다:

```bash
$ man 5 passwd
$ man 1 passwd
```

첫 명령어는 섹션 5의 `passwd` 파일 형식 페이지를, 두 번째는 섹션 1의 사용자 명령어 페이지를 엽니다. `passwd(5)` 같은 참조도 같은 `주제(섹션)` 표기입니다.

:::single-choice{#open-passwd-file-format} `passwd` 파일 형식을 설명하는 섹션 5 페이지를 여는 명령어는 무엇인가요?

::option[`man passwd 5`]{#section-after-topic explanation="이 명령 형식에서는 섹션 선택자가 주제 앞에 와야 하므로 이 순서는 `passwd(5)`를 요청하지 않습니다."}
::option[`man 5 passwd`]{#passwd-format-page .correct explanation="섹션 `5`를 `passwd` 앞에 두면 파일 형식 페이지를 명확히 선택합니다."}
::option[`man 1 passwd`]{#passwd-command-page explanation="섹션 1은 사용자 명령어이므로 파일 형식 페이지가 아닌 `passwd` 명령어 페이지를 선택합니다."}
:::

## 페이지가 없을 때

모든 명령어 이름에 별도의 매뉴얼 페이지가 설치되는 것은 아닙니다. 항목이 없다고 나오면 다음 방법을 사용합니다.

- `type NAME`으로 Bash가 이름을 해석하는 방식을 확인합니다.
- Bash 내장 명령어라면 `help NAME`을 사용합니다.
- 외부 프로그램이 관례를 지원하면 `NAME --help`를 시도합니다.
- 배포판에 별도의 문서 패키지가 있는지 확인합니다.

:::single-choice{#missing-builtin-manual} `type cd`가 `cd`를 Bash 내장 명령어라고 표시하고 별도 man 페이지도 없습니다. 다음으로 어떤 명령어를 시도해야 하나요?

::option[`whatis cd`]{#whatis-missing-cd explanation="`whatis`는 매뉴얼 데이터베이스의 항목을 요약하므로 없는 내장 명령어 전용 페이지를 제공할 수 없습니다."}
::option[`file cd`]{#file-cd-name explanation="`file`은 파일 시스템 객체를 분류하지만 여기서 `cd`는 경로가 아니라 쉘 내장 명령어로 해석됩니다."}
::option[`help cd`]{#builtin-cd-help .correct explanation="Bash의 `help` 내장 명령어가 `cd`에 대한 쉘 자체 문서를 제공합니다."}
:::

## 요약

이제 설치된 매뉴얼 문서를 찾아 탐색할 수 있습니다.

1. 주제 이름으로 페이지를 열 수 있습니다.
2. 일반적인 페이저에서 페이지를 검색하고 이동할 수 있습니다.
3. 페이저를 종료해 쉘로 돌아갈 수 있습니다.
4. 번호가 매겨진 매뉴얼 섹션을 선택할 수 있습니다.
5. 페이지가 없을 때 다른 도움말 출처를 선택할 수 있습니다.
