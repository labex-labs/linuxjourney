---
title: "Vim 검색 패턴"
description: "Vim 검색 패턴: 정방향 (/) 및 역방향 (?) 검색을 배웁니다. 'n'과 'N'으로 결과를 탐색합니다. 오늘 Vim 기술을 향상시키세요!"
keywords: "Vim 검색, Vim 명령, Linux 텍스트 편집기, Vim 튜토리얼, Vim 가이드, 초보자 Vim"
---

## Lesson Content

Vim 세션에서 표현식을 검색하려면 `/` 키를 누른 다음 검색어를 입력하면 됩니다. Enter 키를 누르면 `n`을 눌러 검색 결과를 앞으로 이동하거나 `N`을 눌러 뒤로 이동할 수 있습니다.

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

검색 키를 가지고 연습해보세요. `vim [textfile]` 명령으로 Vim 에서 텍스트 파일을 열고 검색을 시작해보세요!

## Quiz Question

Vim 에서 검색하는 데 사용되는 키는 무엇입니까?

## Quiz Answer

/
