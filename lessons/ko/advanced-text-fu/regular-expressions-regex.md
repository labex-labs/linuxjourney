---
lesson_id: "regular-expressions-regex"
course_id: "advanced-text-fu"
lang: "ko"
order_index: 1
title: "regex (정규 표현식)"
description: "앵커, 문자 집합, 반복, 정규 표현식 종류가 텍스트 패턴 일치를 제어하는 방식을 배웁니다."
meta_title: "regex (정규 표현식) - Advanced Text-Fu"
meta_description: "정규 표현식(regex) 가이드로 Linux 기초를 익혀 보세요. grep에서 ^, $, [] 같은 구문을 사용해 패턴을 일치시키는 방법을 배웁니다."
meta_keywords: "Linux 정규 표현식, regex, Linux 기초, 패턴 일치, grep, 텍스트 처리, Linux 배우기, Linux 튜토리얼, Linux 고급 학습"
---

흔히 **regex**로 줄여 부르는 정규 표현식은 텍스트 패턴을 설명합니다. `grep`, `sed`, `awk` 같은 도구가 정규 표현식을 사용하지만 지원하는 구문은 다를 수 있으므로 항상 도구와 정규 표현식 종류를 확인해야 합니다.

GNU `grep`은 기본적으로 기본 정규 표현식(BRE)을 사용하고 `-E`를 지정하면 확장 정규 표현식(ERE)을 사용합니다. 이 레슨에서는 둘이 공유하는 구성 요소를 소개한 뒤 흔한 ERE 추가 요소를 설명합니다.

예제에는 다음 입력을 사용합니다.

```text
sally sells seashells
by the seashore
```

## 문자 그대로의 텍스트 일치시키기

대부분의 일반 문자는 자기 자신과 일치합니다. 패턴 `seashells`는 그 정확한 문자열이 어디든 들어 있는 줄을 선택합니다.

```bash
$ grep 'seashells' sample.txt
sally sells seashells
```

일치 도구가 받기 전에 쉘이 패턴을 확장하거나 분리하지 않도록 정규 표현식 패턴을 따옴표로 묶으세요. 정규 표현식은 쉘 경로명 확장과도 다릅니다. 정규 표현식에서 `*`는 앞의 원자를 반복하지만 쉘 글로브에서 `*`는 경로명 문자 문자열에 대응하는 와일드카드 자체입니다.

:::single-choice{#regex-versus-shell-star} `ab*` 같은 정규 표현식에서 `*`는 무엇을 하나요?

::option[현재 디렉터리의 모든 파일 이름과 일치합니다.]{#regex-shell-glob explanation="이는 명령 문맥에서 쉘 경로명 확장을 설명하며 정규 표현식 안의 `*` 의미가 아닙니다."}
::option[앞의 `b`를 0번 이상 반복합니다.]{#regex-repeat-b .correct explanation="정규 표현식 수량자는 바로 앞 원자에 적용되므로 `ab*`는 `a`, `ab`, `abb` 등에 일치합니다."}
::option[전체 문자열 `ab`를 정확히 두 번 반복합니다.]{#regex-repeat-ab-twice explanation="별표는 앞 원자에만 적용되고 0번 이상의 반복을 허용하며 전체 문자열을 정확히 두 번 반복하지 않습니다."}
:::

## 일치 위치 고정하기

대괄호 표현식 밖에서 패턴 시작의 `^`는 줄 시작에 일치 위치를 고정합니다.

```plaintext
^by
```

`$` 앵커는 줄 끝에 일치합니다.

```plaintext
seashore$
```

전체 줄이 패턴에 맞아야 하면 두 앵커를 함께 사용합니다.

```text
^by the seashore$
```

:::single-choice{#regex-complete-line} 전체 텍스트가 `by the seashore`인 줄에만 일치하는 패턴은 무엇인가요?

::option[`^by the seashore$`]{#regex-anchored-line .correct explanation="캐럿은 일치가 줄 시작에서 시작하도록 하고 달러 기호는 줄 끝에서 끝나도록 합니다."}
::option[`by the seashore`]{#regex-unanchored-line explanation="앵커가 없으면 앞뒤에 다른 텍스트가 있는 더 긴 줄 안에서도 이 문자열에 일치할 수 있습니다."}
::option[`$by the seashore^`]{#regex-reversed-anchors explanation="의도한 패턴에서 끝 앵커는 일치할 텍스트보다 앞에, 시작 앵커는 뒤에 올 수 없습니다."}
:::

## 문자 하나 일치시키기

일반적인 줄 단위 정규 표현식 모드에서 점은 문자 하나와 일치합니다.

```plaintext
b.
```

`by`와 일치하지만 `ba`나 `b7`에도 일치할 수 있습니다. 뒤에 문자 하나가 필요하므로 `b` 하나만 있는 경우에는 일치하지 않습니다. 문자 그대로의 마침표에는 `\.`로 이스케이프하거나 알맞은 대괄호 표현식 안에 넣습니다.

:::single-choice{#regex-dot-character} 전체 줄 패턴 `^b.$`와 일치하지 않는 문자열은 무엇인가요?

::option[`by`]{#regex-dot-by explanation="점이 `y`와 일치하므로 두 문자 줄이 패턴을 만족합니다."}
::option[`b`]{#regex-dot-b .correct explanation="점은 `b` 뒤에 문자 하나를 요구하지만 이 문자열은 바로 끝납니다."}
::option[`b7`]{#regex-dot-b7 explanation="점이 숫자 `7`과 일치하므로 두 문자 줄이 패턴을 만족합니다."}
:::

## 대괄호 표현식 사용하기

대괄호 표현식은 지정한 집합의 문자 하나와 일치합니다.

```plaintext
s[ae]lls
```

이 위치에서 `sells` 또는 `salls`와 일치합니다.

`^`가 `[` 바로 뒤의 첫 문자이면 집합을 부정합니다.

```plaintext
s[^e]lls
```

첫 번째 `s` 다음 문자가 `e`일 수 없으므로 `salls`와 일치하지만 `sells`와는 일치하지 않습니다.

:::single-choice{#regex-negated-bracket} `[^e]`는 무엇과 일치하나요?

::option[`e`가 아닌 문자 정확히 하나입니다.]{#regex-not-e .correct explanation="대괄호 안의 선행 캐럿은 나열된 집합의 여집합을 만들며 대괄호 표현식은 여전히 문자 하나를 소비합니다."}
::option[줄 시작 뒤에 오는 `e`입니다.]{#regex-caret-e-anchor explanation="대괄호 표현식 안의 선행 캐럿은 줄을 고정하지 않고 집합을 부정합니다."}
::option[문자 `e`가 0번 이상 나타나는 경우입니다.]{#regex-repeat-e explanation="반복에는 `*` 같은 수량자가 필요하며 이 대괄호 표현식은 `e`가 아닌 문자 하나와 일치합니다."}
:::

범위는 두 끝점 사이의 문자를 설명할 수 있습니다.

```plaintext
d[a-c]g
```

`dag`, `dbg`, `dcg`와 일치할 수 있습니다. 범위 동작은 로캘 배열에 따라 달라질 수 있습니다. `[[:lower:]]`, `[[:upper:]]`, `[[:digit:]]` 같은 문자 클래스가 의도를 더 명확하게 표현하는 경우가 많습니다.

## 패턴 반복하고 결합하기

BRE와 ERE 모두에서 `*`는 앞 원자의 0번 이상 반복을 뜻합니다.

```text
seashells*
```

`seashell` 뒤에 `s`가 0개 이상 이어지는 문자열과 일치합니다. `grep -E`를 사용하는 ERE 모드의 흔한 연산자는 다음과 같습니다.

- `+`: 1번 이상 반복
- `?`: 0번 또는 1번 반복
- `|`: 왼쪽 표현식 또는 오른쪽 표현식
- `(...)`: 표현식 그룹화

예를 들면 다음과 같습니다.

```bash
$ grep -E '^(cat|dog)s?$' animals.txt
```

전체 줄이 `cat`, `cats`, `dog`, `dogs` 중 하나인 경우를 선택합니다. BRE 모드에서는 이 연산자의 이스케이프 규칙이 다르므로 확인 없이 패턴을 종류 사이에 복사하지 마세요.

:::single-choice{#regex-extended-alternation} 패턴 `^(cat|dog)s?$`에 확장 정규 표현식 구문을 활성화하는 명령어는 무엇인가요?

::option[`grep -F '^(cat|dog)s?$' animals.txt`]{#regex-fixed-animals explanation="`-F`는 모든 정규 표현식 연산자를 문자 그대로 처리하므로 그룹화, 선택, 선택적 반복이 비활성화됩니다."}
::option[`grep -E '^(cat|dog)s?$' animals.txt`]{#regex-extended-animals .correct explanation="`-E`는 확장 정규 표현식을 선택하여 표시된 그룹화, 선택, 선택적 `s`를 활성화합니다."}
::option[`grep '^(cat|dog)s?$' animals.txt`]{#regex-basic-animals explanation="기본 grep은 BRE를 사용하며 이스케이프되지 않은 그룹 및 선택 문자는 의도한 ERE 의미를 갖지 않습니다."}
:::

Linux 텍스트 도구로 정규 표현식 선택을 연습하려면 다음 실습을 진행해 보세요.

1. **[Linux에서 grep으로 텍스트 검색](https://labex.io/ko/labs/comptia-search-text-with-grep-in-linux-590841)** - 기본 검색, 줄 번호, `^`와 `$` 앵커, 기본 및 확장 정규 표현식을 연습합니다.
2. **[텍스트 처리와 정규 표현식](https://labex.io/ko/labs/linux-text-processing-and-regular-expressions-18003)** - `grep`, `sed`, `awk`와 정규 표현식으로 텍스트를 효율적으로 조작하고 패턴을 일치시킵니다.
3. **[메일과 숫자 추출하기](https://labex.io/ko/labs/linux-extracting-mails-and-numbers-17991)** - `grep`과 정규 표현식으로 파일에서 이메일 주소와 숫자를 추출합니다.

## 요약

이제 줄 단위 정규 표현식의 기초를 읽고 만들 수 있습니다.

1. 정규 표현식 연산자와 쉘 경로명 와일드카드를 구분할 수 있습니다.
2. 줄 시작이나 끝에 일치 위치를 고정할 수 있습니다.
3. 점이나 대괄호 표현식으로 문자 하나를 일치시킬 수 있습니다.
4. 집합을 부정하고 로캘을 고려하는 문자 클래스를 사용할 수 있습니다.
5. BRE 또는 ERE 구문을 의도적으로 선택할 수 있습니다.
