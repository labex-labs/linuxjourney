---
index: 8
lang: "ko"
title: "less"
meta_title: "less 명령어 - 명령줄"
meta_description: "효율적인 텍스트 파일 보기를 위해 Linux less 명령어를 마스터하세요. 이 가이드는 less 명령어 사용법, 탐색 방법, unix less 검색 수행 방법 및 less 종료 방법을 다룹니다."
meta_keywords: "less 명령어, 명령어 less, less 종료, unix less 검색, linux less, 텍스트 파일 보기, 파일 탐색, 리눅스 명령줄"
---

## Lesson Content

화면에 한 번에 표시하기에는 너무 큰 텍스트 파일을 볼 때, `less command`는 매우 유용한 도구입니다. 오래된 유닉스 속담처럼, "less is more"입니다. (이는 유사한 기능을 가진 `more` 명령어가 있다는 사실을 이용한 말장난입니다). `less` 유틸리티는 텍스트를 페이지 형식으로 표시하여 전체 파일을 메모리에 로드하지 않고도 파일을 페이지별로 탐색할 수 있게 해줍니다.

### Less 명령어로 시작하기

파일 보기를 시작하려면, 파일 이름 뒤에 `command less`를 사용하기만 하면 됩니다. 그러면 `less` 인터페이스에서 파일이 열립니다.

```bash
less /home/pete/Documents/text1
```

`less` 뷰어 안에 들어가면 표준 셸 명령은 작동하지 않습니다. 대신, 텍스트를 탐색하고 상호 작용하기 위해 특정 키 세트를 사용합니다.

### 탐색 및 제어

문서를 이동하기 위해 여러 키를 사용할 수 있습니다:

- **화살표 키 및 페이지 키**: `Page Up`, `Page Down`, `Up`, `Down`을 사용하여 줄 단위 또는 페이지 단위로 이동합니다.
- **시작으로 이동**: `g`를 눌러 텍스트 파일의 시작 부분으로 바로 이동합니다.
- **끝으로 이동**: `G` (Shift + g) 를 눌러 텍스트 파일의 끝으로 이동합니다.
- **도움말 메뉴**: `less` 내에서 명령어를 잊어버렸다면, `h`를 누르기만 하면 유용한 요약이 표시됩니다.

### Unix Less 검색

`less`의 강력한 기능 중 하나는 텍스트를 검색할 수 있는 기능입니다. `unix less search`를 수행하려면, 찾으려는 텍스트 앞에 `/`를 입력한 다음 Enter 키를 누릅니다. 그러면 검색어의 모든 발생 항목이 강조 표시됩니다.

- `/search_term`: "search_term"을 앞으로 검색합니다.
- `?search_term`: "search_term"을 뒤로 검색합니다.
- `n`: 검색어의 다음 항목으로 이동합니다.
- `N`: 이전 항목으로 이동합니다.

### Less 종료 방법

파일 보기를 마쳤을 때, `exit less`하고 명령 프롬프트로 돌아오는 방법을 알아야 합니다.

- **종료**: 단순히 `q`를 눌러 `less` 뷰어를 종료하고 셸로 돌아갑니다.

`less command`를 마스터하는 것은 Linux 명령줄에서 작업하는 모든 사람에게 기본적인 기술이며, 파일 검사를 훨씬 더 효율적으로 만듭니다.

## Exercise

연습이 완벽을 만듭니다! Linux 에서 텍스트 파일을 보고 탐색하는 이해도를 높이기 위한 실습 랩이 있습니다:

1. **[Linux less 명령어: 파일 페이징](https://labex.io/ko/labs/linux-linux-less-command-file-paging-214301)** - 검색, 줄 번호, 패턴 일치를 포함하여 효율적인 텍스트 파일 보기 및 탐색을 위한 Linux 'less' 명령어를 배웁니다.
2. **[Linux more 명령어: 파일 스크롤](https://labex.io/ko/labs/linux-linux-more-command-file-scrolling-214299)** - 기본 사용법, 특정 줄에서 시작하기, 디스플레이 사용자 지정을 다루는 효율적인 텍스트 파일 보기를 위한 Linux 'more' 명령어를 배웁니다.
3. **[Linux 에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `cat`, `more`, `less`와 같은 명령어를 사용하여 시스템 로그 및 구성 파일을 포함하여 텍스트 파일을 효율적으로 보고 탐색하는 필수 Linux 명령줄 기술을 배웁니다.

이 랩들은 실제 시나리오에서 개념을 적용하고 텍스트 파일 조작 및 탐색에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`less` 명령에서 어떻게 종료합니까? 답변으로 단일 문자 키를 제공하십시오. 참고: 답변은 대소문자를 구분하는 영어 문자입니다.

## Quiz Answer

q
