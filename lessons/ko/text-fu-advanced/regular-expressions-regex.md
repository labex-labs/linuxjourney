---
index: 1
lang: "ko"
title: "정규 표현식 (Regular Expressions)"
meta_title: "정규 표현식 (regex) - 고급 텍스트 기술"
meta_description: "Linux 패턴 일치를 위한 정규 표현식 (regex) 을 배우세요. 텍스트 조작을 위한 ^, $, ., []와 같은 regex 구문을 이해하세요. grep 기술을 향상시키세요!"
meta_keywords: "정규 표현식, regex, Linux regex, grep regex, 패턴 일치, regex 튜토리얼, Linux 명령, 초보자"
---

## Lesson Content

정규 표현식은 패턴 기반 선택을 위한 강력한 도구입니다. 이는 `*` 와일드카드와 같이 이미 접했던 특수 표기법을 사용합니다.

가장 일반적인 정규 표현식 몇 가지를 살펴보겠습니다. 이들은 거의 모든 프로그래밍 언어에서 보편적으로 사용됩니다.

다음 구문을 테스트 문자열로 사용하겠습니다:

```plaintext
sally sells seashells
by the seashore
```

### 1. ^를 사용한 줄의 시작

```plaintext
^by
would match the line "by the seashore"
```

### 2. $를 사용한 줄의 끝

```plaintext
seashore$
would match the line "by the seashore"
```

### 3. .를 사용한 모든 단일 문자 일치

```plaintext
b.
would match by
```

### 4. [] 및 () 를 사용한 대괄호 표기법

이것은 약간 까다로울 수 있습니다. 대괄호를 사용하면 대괄호 안에 있는 문자를 지정할 수 있습니다.

```plaintext
d[iou]g
would match: dig, dog, dug
```

이전 앵커 태그 `^`는 대괄호 안에서 사용될 때 대괄호 안의 문자를 제외한 모든 것을 의미합니다.

```plaintext
d[^i]g
would match: dog and dug but not dig
```

대괄호는 또한 범위를 사용하여 사용하려는 문자 수를 늘릴 수 있습니다.

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

하지만 대괄호는 대소문자를 구분하므로 주의하십시오:

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

이것이 몇 가지 기본적인 정규 표현식입니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 정규 표현식과 패턴 일치에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 grep 으로 텍스트 검색](https://labex.io/ko/labs/comptia-search-text-with-grep-in-linux-590841)** - 이 랩에서는 `grep` 명령을 사용하여 Linux 시스템의 파일에서 텍스트를 검색하는 방법을 배웁니다. 기본 검색을 수행하고, 줄 번호를 표시하고, `^` 및 `$`와 같은 앵커를 사용하여 줄 위치를 일치시키고, 복잡한 패턴 일치를 위해 기본 및 확장 정규 표현식을 모두 활용합니다.
2. **[텍스트 처리 및 정규 표현식](https://labex.io/ko/labs/linux-text-processing-and-regular-expressions-18003)** - 강력한 텍스트 처리 도구인 grep, sed, awk 를 배웁니다. Linux 에서 효율적인 텍스트 조작 및 패턴 일치를 위해 정규 표현식을 사용하는 방법을 배웁니다.
3. **[메일 및 숫자 추출](https://labex.io/ko/labs/linux-extracting-mails-and-numbers-17991)** - 이 챌린지에서는 grep 과 정규 표현식을 사용하여 파일에서 이메일 주소와 숫자를 추출하는 방법을 배우고, 필수적인 Linux 텍스트 처리 기술을 시연합니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 정규 표현식 및 텍스트 처리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

단일 문자를 일치시키려면 어떤 정규 표현식을 사용하시겠습니까?

## Quiz Answer

.
