---
index: 1
lang: "ko"
title: "regex (정규 표현식)"
meta_title: "regex (정규 표현식) - 고급 Text-Fu"
meta_description: "Linux 패턴 매칭을 위한 정규 표현식 (regex) 을 학습합니다. 텍스트 조작을 위한 ^, $, ., []와 같은 regex 구문을 이해합니다. grep 기술을 향상시키세요!"
meta_keywords: "정규 표현식, regex, Linux regex, grep regex, 패턴 매칭, regex 튜토리얼, Linux 명령어, 초급"
---

## Lesson Content

정규 표현식 (Regular expressions) 은 패턴 기반 선택을 위한 강력한 도구입니다. 이는 우리가 이미 접했던 `*` 와일드카드와 유사한 특별한 표기법을 사용합니다.

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

### 4. [] 및 () 를 사용한 괄호 표기법

이것은 약간 까다로울 수 있습니다. 괄호는 괄호 안에 있는 문자를 지정할 수 있게 해줍니다.

```plaintext
d[iou]g
would match: dig, dog, dug
```

괄호 안에서 사용될 때 이전 앵커 태그 `^`는 괄호 안의 문자를 제외한 모든 것을 의미합니다.

```plaintext
d[^i]g
would match: dog and dug but not dig
```

괄호는 또한 범위를 사용하여 사용하려는 문자 수를 늘릴 수 있습니다.

```plaintext
d[a-c]g
will match patterns like dag, dbg, and dcg
```

하지만 괄호는 대소문자를 구분하므로 주의하십시오:

```plaintext
d[A-C]g
will match dAg, dBg and dCg but not dag, dbg and dcg
```

이것이 몇 가지 기본적인 정규 표현식입니다.

## Exercise

정규 표현식을 `grep`과 결합하여 일부 파일을 검색해 보십시오.

```bash
grep [regular expression here] [file]
```

## Quiz Question

단일 문자를 일치시키려면 어떤 정규 표현식을 사용하시겠습니까?

## Quiz Answer

.
