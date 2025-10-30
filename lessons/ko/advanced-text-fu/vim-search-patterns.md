---
index: 4
lang: "ko"
title: "Vim 검색 패턴"
meta_title: "Vim 검색 패턴 - 고급 텍스트 기술"
meta_description: "Vim 검색 패턴을 배우세요: 정방향 (/) 및 역방향 (?) 검색. 'n'과 'N'으로 결과를 탐색하세요. 오늘 Vim 기술을 향상시키세요!"
meta_keywords: "Vim 검색, Vim 명령, Linux 텍스트 편집기, Vim 튜토리얼, Vim 가이드, 초보자 Vim"
---

## Lesson Content

Vim 세션에서 표현식을 검색하려면 `/` 키를 누른 다음 검색어를 입력하면 됩니다. Enter 키를 누르면 `n`을 눌러 검색 결과에서 앞으로 이동하거나 `N`을 눌러 뒤로 이동할 수 있습니다.

```plaintext
My pretty file is very pretty.

/pretty

will find the pretty words in the text file.
```

`?` 검색 명령은 텍스트 파일을 뒤로 검색합니다. 따라서 이전 예시에서는 마지막 "pretty"가 먼저 나타납니다.

```plaintext
My pretty file is very pretty.

?pretty

will find the pretty words in the text file.
```

## Exercise

연습하면 완벽해집니다! 다음은 Linux 에서 텍스트 편집 및 검색에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Vim 및 Nano 로 Linux 에서 텍스트 파일 편집](https://labex.io/ko/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - Vim 및 Nano 를 사용하여 텍스트 파일을 생성, 편집, 저장 및 탐색하는 연습을 합니다. 이 랩은 검색 기능을 포함하여 필수 텍스트 편집 도구에 능숙해지는 데 도움이 될 것입니다.

이 랩은 실제 시나리오에 개념을 적용하고 Linux 에서 텍스트 파일 조작에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

Vim 에서 검색하는 데 사용되는 키는 무엇입니까?

## Quiz Answer

/
