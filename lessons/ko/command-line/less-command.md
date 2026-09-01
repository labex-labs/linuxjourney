---
lesson_id: "less-command"
course_id: "command-line"
lang: "ko"
order_index: 8
title: "less"
description: "less로 긴 텍스트 파일을 대화형으로 탐색하고 검색하며 새 내용을 추적하는 방법을 배웁니다."
meta_title: "less - 명령어 라인"
meta_description: "큰 파일 보기, 스크롤, 검색, 특정 줄로 이동, 로그 추적, less 종료 방법 등 Linux less 명령어를 예제로 배워보세요."
meta_keywords: "less 명령어, 리눅스 less, 큰 파일 보기 리눅스, less에서 검색, less 종료, less -N, less +F, 텍스트 뷰어 리눅스"
---

텍스트 파일이 한 화면보다 길 때 `less`를 사용하면 전체 파일이 터미널을 빠르게 지나가게 하지 않고 읽을 수 있습니다. `more`도 또 다른 페이저이기 때문에 이름에서 오래된 유닉스 농담인 "less is more"가 나왔습니다.

## 파일 열기

파일을 보기 위해서는 `less` 다음에 파일 이름을 입력하세요.

```bash
$ less /home/pete/Documents/text1
```

`less`가 실행 중일 때 누르는 키는 일반 쉘 명령어를 시작하는 대신 페이저를 제어합니다. 페이저를 종료하면 쉘로 돌아옵니다.

:::single-choice{#open-long-file} `/var/log/syslog`를 대화형 페이저로 여는 명령어는 무엇인가요?

::option[`less /var/log/syslog`]{#page-log .correct explanation="`less`는 파일을 페이저로 열어 이동하고 검색한 뒤 쉘로 돌아갈 수 있게 합니다."}
::option[`cat /var/log/syslog`]{#print-log explanation="`cat`은 파일 전체를 표준 출력으로 한꺼번에 보내므로 대화형 페이징 제어를 제공하지 않습니다."}
::option[`file /var/log/syslog`]{#classify-log explanation="`file`은 예상 내용 유형을 알려 줄 뿐 로그를 대화형으로 읽도록 열지 않습니다."}
:::

## less에서 탐색하기

문서 내에서 이동할 때 다음 키들을 사용할 수 있습니다:

- **화살표 키와 페이지 키**: `Page Up`, `Page Down`, `Up`, `Down` 키로 한 줄씩 또는 한 페이지씩 이동합니다.
- **처음으로 이동**: `g` 키를 눌러 텍스트 파일의 시작 부분으로 바로 이동합니다.
- **끝으로 이동**: `G` (Shift + g) 키를 눌러 텍스트 파일의 끝으로 점프합니다.
- **반 페이지 이동**: `u` 키로 위로, `d` 키로 아래로 반 페이지씩 이동합니다.
- **도움말 메뉴**: `less` 안에서 명령어가 기억나지 않으면 `h` 키를 눌러 도움말 요약을 볼 수 있습니다.

:::single-choice{#jump-to-file-end} `less`에서 파일 끝으로 바로 이동하는 키는 무엇인가요?

::option[`g`]{#lowercase-g explanation="소문자 `g`는 파일의 시작으로 이동하며 대문자는 반대 방향으로 이동합니다."}
::option[`G`]{#uppercase-g .correct explanation="대문자 `G`는 입력의 끝으로 이동합니다. 이 명령은 대소문자를 구분합니다."}
::option[`h`]{#help-key explanation="`h`는 페이저의 도움말을 열며 파일 끝으로 이동하지 않습니다."}
:::

## less에서 검색하기

`less`의 강력한 기능 중 하나는 텍스트 검색입니다. `/` 다음에 찾고 싶은 텍스트를 입력하고 Enter를 누르세요.

- `/search_term`: "search_term"을 앞으로 검색합니다.
- `?search_term`: "search_term"을 뒤로 검색합니다.
- `n`: 같은 방향으로 검색을 반복합니다.
- `N`: 반대 방향으로 검색을 반복합니다.

:::single-choice{#repeat-search-direction} `error`를 앞으로 검색한 뒤 같은 방향으로 검색을 반복하는 키는 무엇인가요?

::option[`n`]{#same-search .correct explanation="소문자 `n`은 최근 검색을 원래 방향으로 반복합니다. 여기서는 앞으로 검색합니다."}
::option[`N`]{#opposite-search explanation="대문자 `N`은 최근 검색을 반대 방향으로 반복하므로 앞으로 검색한 뒤에는 이전 일치 항목으로 이동합니다."}
::option[`g`]{#search-to-start explanation="`g`는 입력의 시작으로 이동하며 검색을 반복하지 않습니다."}
:::

## less 종료하기

`q` 키를 눌러 `less`를 종료하고 쉘 프롬프트로 돌아갑니다.

:::single-choice{#quit-less} `less`를 종료하고 쉘로 돌아가는 키는 무엇인가요?

::option[`q`]{#less-quit .correct explanation="`q` 명령은 페이저를 종료하고 쉘 프롬프트로 돌아갑니다."}
::option[`h`]{#less-help explanation="`h`는 `less` 안에서 도움말을 열며 곧바로 쉘로 돌아가지 않습니다."}
::option[`G`]{#less-end explanation="대문자 `G`는 입력의 끝으로 이동하지만 페이저는 계속 열려 있습니다."}
:::

## 옵션을 사용해 less 시작하기

옵션을 붙여서 `less`를 시작할 수 있습니다:

```bash
$ less -N file.txt
$ less +G file.txt
$ less +F /var/log/syslog
```

- `-N`: 줄 번호를 표시합니다.
- `+G`: 파일 끝에서 시작합니다.
- `+F`: `tail -f`와 비슷하게 새로 추가되는 내용을 따라갑니다.

`+F` 옵션으로 파일을 따라가다가 `Ctrl-C`를 눌러 추적을 멈추고 일반 탐색 모드로 돌아간 후 `q`를 눌러 종료할 수 있습니다. 대문자가 없는 패턴은 대소문자를 무시하도록 `-i`를 사용하거나, 패턴과 관계없이 항상 대소문자를 무시하도록 `-I`를 사용합니다.

명령어 출력도 파이프로 `less`에 보낼 수 있습니다.

```bash
$ dmesg | less
```

:::single-choice{#follow-growing-log} `/var/log/syslog`를 열고 새 내용이 들어올 때마다 계속 표시하는 명령어는 무엇인가요?

::option[`less +F /var/log/syslog`]{#follow-log .correct explanation="`+F` 초기 명령은 추적 모드로 들어가 로그 뒤에 추가되는 새 내용을 표시합니다."}
::option[`less +G /var/log/syslog`]{#open-at-log-end explanation="`+G`는 파일 끝에서 시작하지만 나중에 들어오는 내용을 계속 추적하지는 않습니다."}
::option[`less -N /var/log/syslog`]{#number-log-lines explanation="`-N`은 줄 번호를 표시할 뿐 지속적인 추적을 활성화하지 않습니다."}
:::

페이징과 검색, 시스템 텍스트 읽기를 연습하려면 다음 실습을 활용해 보세요.

1. **[Linux less 명령어: 파일 페이징](https://labex.io/ko/labs/linux-linux-less-command-file-paging-214301)** - 효율적인 텍스트 파일 보기 및 탐색을 위한 Linux 'less' 명령어 학습, 검색, 줄 번호, 패턴 매칭 포함.
2. **[Linux에서 로그 및 설정 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `cat`, `more`, `less` 같은 명령어로 시스템 로그와 설정 파일을 효율적으로 탐색하는 방법을 연습하세요.

## 요약

이제 터미널을 가득 채우지 않고 `less`로 긴 파일을 살펴볼 수 있습니다.

1. 파일이나 파이프로 받은 명령어 출력을 페이저에서 열 수 있습니다.
2. 입력의 특정 위치로 이동할 수 있습니다.
3. 앞이나 뒤로 검색하고 검색을 반복할 수 있습니다.
4. 줄 번호를 표시하거나 늘어나는 내용을 추적할 수 있습니다.
5. 안전하게 종료해 쉘로 돌아갈 수 있습니다.
