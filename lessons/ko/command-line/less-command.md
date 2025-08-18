---
index: 8
lang: "ko"
title: "less"
meta_title: "less - Command Line"
meta_description: "Linux 의 'less' 명령을 사용하여 텍스트 파일을 효율적으로 보고 탐색하는 방법을 배우세요. 이 초보자 친화적인 가이드를 통해 페이징, 검색 및 종료를 마스터하세요."
meta_keywords: "less command, Linux less, 텍스트 파일 보기, 파일 탐색, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

간단한 출력보다 큰 텍스트 파일을 볼 때, `less`는 더 유용합니다. (실제로 비슷한 기능을 하는 `more`라는 명령어가 있어서 아이러니합니다.) 텍스트는 페이지 단위로 표시되므로 텍스트 파일을 페이지별로 탐색할 수 있습니다.

`less`를 사용하여 파일 내용을 살펴보세요. `less` 명령 안에 있으면 다른 키보드 명령을 사용하여 파일 내에서 탐색할 수 있습니다.

```bash
less /home/pete/Documents/text1
```

`less`를 통해 탐색하려면 다음 명령을 사용하세요:

- `q` - `less`를 종료하고 셸로 돌아가는 데 사용됩니다.
- `Page up`, `Page down`, `Up` and `Down` - 화살표 키와 페이지 키를 사용하여 탐색합니다.
- `g` - 텍스트 파일의 시작 부분으로 이동합니다.
- `G` - 텍스트 파일의 끝으로 이동합니다.
- `/search` - 텍스트 문서 내에서 특정 텍스트를 검색할 수 있습니다. 검색하려는 단어 앞에 `/`를 붙입니다.
- `h` - `less` 안에 있는 동안 `less` 사용 방법에 대한 약간의 도움이 필요하면 도움말을 사용하세요.

## Exercise

파일에서 `less`를 실행한 다음, 파일 내에서 페이지를 위아래로 이동해 보세요. 특정 단어를 검색해 보세요. 파일의 시작이나 끝으로 빠르게 이동해 보세요.

## Quiz Question

`less` 명령을 어떻게 종료합니까?

## Quiz Answer

q
