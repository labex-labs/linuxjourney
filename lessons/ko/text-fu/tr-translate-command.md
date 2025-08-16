---
lang: "ko"
title: "tr (변환)"
description: "Linux 'tr' 명령어를 사용하여 문자를 변환하고 삭제하는 방법을 배웁니다. 예제와 연습을 통해 문자 변환을 이해합니다. Linux 여정을 시작하세요!"
keywords: "tr command, Linux tr, 문자 변환, 문자 삭제, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`tr` (translate) 명령어는 한 문자 집합을 다른 문자 집합으로 변환할 수 있게 해줍니다. 모든 소문자를 대문자로 변환하는 예시를 살펴보겠습니다.

```bash
$ tr a-z A-Z
hello
HELLO
```

보시다시피, `a-z` 범위를 `A-Z`로 만들었고, 입력하는 모든 소문자 텍스트가 대문자로 변환됩니다.

## Exercise

다음 명령어를 시도해 보세요. 어떤 일이 발생하나요?

```bash
$ tr -d ello
hello
```

## Quiz Question

문자를 변환하는 데 사용되는 명령어는 무엇입니까?

## Quiz Answer

tr
