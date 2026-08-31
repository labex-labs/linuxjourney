---
lesson_id: "whatis-command"
course_id: "command-line"
lang: "ko"
order_index: 17
title: "whatis"
description: "간결한 매뉴얼 페이지 설명을 조회하고 표시된 섹션 번호를 해석하는 방법을 배웁니다."
meta_title: "whatis - 커맨드 라인"
meta_description: "man 페이지에서 한 줄 명령어 설명을 얻고 여러 매뉴얼 섹션을 이해하는 Linux whatis 명령어를 예제와 함께 배워보세요."
meta_keywords: "whatis 명령어, 리눅스 whatis, 명령어 설명 리눅스, man 페이지 요약, 커맨드 라인 도움말, apropos"
---

명령어 이름은 알지만 용도를 잊었을 때 `whatis`는 매뉴얼 페이지 데이터베이스에서 짧은 설명을 보여 줍니다.

## 정확한 이름 조회하기

`whatis` 사용법은 간단합니다. `whatis` 뒤에 알고 싶은 명령어를 입력하세요.

```bash
$ whatis cat
cat (1)              - concatenate files and print on the standard output
```

결과는 설명이며 명령어 옵션이나 예제 목록이 아닙니다. 자세한 정보가 필요하면 `man cat` 또는 `cat --help`를 사용합니다.

:::single-choice{#describe-known-command}
`cat`이라는 이름을 알고 있고 한 줄짜리 매뉴얼 페이지 설명이 필요합니다. 어떤 명령어를 실행해야 하나요?

::option[`man cat`]{#manual-cat explanation="`man cat`은 전체 매뉴얼 페이지를 열므로 요청한 한 줄 알림보다 많은 정보를 제공합니다."}
::option[`apropos cat`]{#apropos-cat explanation="`apropos`는 설명에서 키워드를 검색해 여러 관련 주제를 반환할 수 있으므로 정확한 이름 조회보다 범위가 넓습니다."}
::option[`whatis cat`]{#whatis-cat .correct explanation="`whatis`는 정확한 주제 이름을 조회해 매뉴얼 데이터베이스의 간결한 설명을 출력합니다."}
:::

## 섹션 번호 읽기

`whatis`가 제공하는 설명은 명령어 매뉴얼 페이지의 `NAME` 섹션에서 가져옵니다. 만약 이름이 여러 매뉴얼 섹션에 걸쳐 있다면, `whatis`는 여러 줄을 표시할 수 있습니다.

```bash
$ whatis passwd
passwd (1)           - change user password
passwd (5)           - the password file
```

괄호 안의 숫자는 매뉴얼 페이지 섹션 번호입니다. 여기서 `passwd(1)`은 사용자 명령어를, `passwd(5)`는 파일 형식을 설명합니다. `man 1 passwd` 또는 `man 5 passwd`로 원하는 페이지를 명시적으로 열 수 있습니다.

:::single-choice{#interpret-whatis-section}
`passwd (5) - the password file` 출력에서 `(5)`는 무엇을 나타내나요?

::option[`passwd` 명령어가 받는 다섯 번째 옵션입니다.]{#fifth-option explanation="숫자는 옵션 위치가 아니며 옵션은 선택한 매뉴얼 페이지 안에서 설명합니다."}
::option[파일 형식 페이지가 들어 있는 매뉴얼 섹션입니다.]{#section-five .correct explanation="섹션 5는 파일 형식과 규칙에 사용되므로 `passwd(5)`는 해당 매뉴얼 섹션을 뜻합니다."}
::option[`passwd`라는 이름을 공유하는 매뉴얼 페이지가 다섯 개라는 뜻입니다.]{#five-pages explanation="결과가 여러 개일 수 있지만 괄호의 값은 페이지 수가 아니라 하나의 섹션을 나타냅니다."}
:::

## whatis, man, apropos 선택하기

- `whatis ls`: 정확한 명령어 이름에 대한 한 줄 설명을 보여줍니다.
- `man ls`: 전체 매뉴얼 페이지를 엽니다.
- `apropos keyword`: 매뉴얼 페이지 설명에서 키워드를 검색합니다.

예를 들어:

```bash
$ apropos password
```

작업은 알지만 명령어 이름을 모르면 `apropos`를, 이름을 이미 알고 있으면 `whatis`를 사용합니다.

:::single-choice{#search-by-purpose}
명령어 이름은 모르지만 매뉴얼 설명에서 `password`라는 키워드를 찾고 싶습니다. 어떤 명령어가 알맞나요?

::option[`apropos password`]{#apropos-password .correct explanation="`apropos`는 매뉴얼 페이지 이름과 설명에서 키워드를 검색해 관련 주제를 찾도록 돕습니다."}
::option[`whatis password`]{#exact-password explanation="`whatis`는 정확히 `password`라는 매뉴얼 주제를 찾으며 일반 키워드 검색 인터페이스가 아닙니다."}
::option[`man password`]{#manual-password explanation="`man`은 해당 주제 이름의 페이지를 열려고 할 뿐 요청한 설명 검색을 수행하지 않습니다."}
:::

## 설명이 나오지 않을 때

`whatis`가 적절한 항목이 없다고 하면 주제의 매뉴얼 페이지가 설치되지 않았거나 데이터베이스가 오래되었을 수 있습니다. 그렇다고 같은 이름의 실행 파일, 별칭, 함수 또는 내장 명령어가 없다는 뜻은 아닙니다. `type NAME`으로 Bash가 이름을 해석하는 방식을 확인한 뒤 알맞은 도움말을 선택하세요.

:::single-choice{#whatis-versus-type}
`whatis deploy`가 매뉴얼 설명을 찾지 못했습니다. Bash가 `deploy`를 별칭, 함수, 내장 명령어 또는 실행 파일로 해석하는지 확인하는 명령어는 무엇인가요?

::option[`whatis -r deploy`]{#whatis-regex-deploy explanation="매뉴얼 데이터베이스 쿼리를 바꿔도 Bash의 모든 별칭, 함수, 내장 명령어와 경로 해석은 보여 주지 않습니다."}
::option[`man 5 deploy`]{#manual-five-deploy explanation="섹션 5 페이지를 열려고 할 뿐 Bash가 명령어 이름을 어떻게 해석하는지 확인하지 않습니다."}
::option[`type deploy`]{#resolve-deploy .correct explanation="Bash `type`은 매뉴얼 설명 설치 여부와 관계없이 현재 쉘이 명령어 이름을 해석하는 방식을 알려 줍니다."}
:::

## 요약

이제 매뉴얼 데이터베이스에서 간결한 설명을 가져와 해석할 수 있습니다.

1. `whatis`로 정확한 주제를 조회할 수 있습니다.
2. 괄호 안에 표시된 매뉴얼 섹션을 읽을 수 있습니다.
3. 전체 페이지가 필요할 때 `man`을 사용할 수 있습니다.
4. 이름 대신 키워드를 알 때 `apropos`를 사용할 수 있습니다.
