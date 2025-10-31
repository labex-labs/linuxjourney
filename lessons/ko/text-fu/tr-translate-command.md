---
index: 13
lang: "ko"
title: "tr (변환)"
meta_title: "tr (변환) - Text-Fu"
meta_description: "문자 변환 및 삭제를 위한 Linux tr 명령어를 마스터하세요. 이 가이드는 tr 로 문자를 변환하는 방법, linux tr -d 와 같은 옵션을 사용하여 문자를 제거하는 방법, 그리고 텍스트 조작을 위한 실용적인 예제를 다룹니다."
meta_keywords: "tr, tr 명령어, tr 변환, linux tr -d, tr -d linux, 문자 변환, 문자 삭제, 텍스트 처리, Linux 명령어"
---

## Lesson Content

tr 명령어는 translate(변환) 의 약자로, 표준 입력에서 문자를 변환하거나 삭제하는 Linux 명령줄 유틸리티입니다. 간단한 텍스트 조작에 유용한 도구이며, 다른 명령의 출력을 처리하기 위해 파이프와 함께 자주 사용됩니다. trtranslate 기능은 텍스트 처리의 핵심 부분입니다.

### 기본 문자 변환

tr 의 가장 일반적인 용도는 한 문자 집합을 다른 문자 집합으로 대체하는 것입니다. 예를 들어, 모든 소문자를 대문자로 쉽게 변환할 수 있습니다.

```bash
$ echo "hello world" | tr a-z A-Z
HELLO WORLD
```

이 예제에서는 `echo`의 출력을 `tr` 명령어로 파이프했습니다. 그런 다음 `tr` 명령어는 문자 범위 `a-z`를 범위 `A-Z`에 해당하는 문자로 변환했습니다.

### -d 를 사용한 문자 삭제

강력한 또 다른 기능은 `-d`(delete) 옵션을 사용하여 특정 문자를 삭제하는 기능입니다. 이는 텍스트 정리 시 특히 유용합니다. 예를 들어, 문자열에서 모든 숫자를 제거하려면 `linux tr -d`를 사용할 수 있습니다.

```bash
$ echo "My address is 123 Main Street" | tr -d '0-9'
My address is  Main Street
```

여기서 `tr -d` 명령어는 입력 스트림에서 지정된 집합 ('0'부터 '9'까지) 의 모든 문자를 삭제했습니다. 이는 `tr -d linux` 사용자의 일반적인 패턴입니다.

### 반복되는 문자 압축 (Squeezing)

tr 명령어는 `-s`(squeeze) 옵션을 사용하여 반복되는 문자를 단일 인스턴스로 "압축"할 수도 있습니다. 이는 추가 공백이 있는 텍스트를 정규화하는 데 매우 유용합니다.

```bash
$ echo "Hello      World,   how   are   you?" | tr -s ' '
Hello World, how are you?
```

이 경우 `tr -s ' '`는 여러 개의 공백 시퀀스를 단일 공백으로 대체하여 출력을 훨씬 깔끔하게 만들었습니다.

## Exercise

지식을 실제로 적용해 보기 위해 다음 실습 랩을 시도해 보세요. 이는 문자 변환 및 텍스트 처리에 대한 이해를 강화하는 데 도움이 될 것입니다.

1.  **[Linux tr 명령어: 문자 변환](https://labex.io/ko/labs/linux-linux-tr-command-character-translating-219198)** - 텍스트 스트림에서 문자 수준 변환을 위한 Linux `tr` 명령어를 학습합니다. 문자를 변환하고, 특정 문자를 삭제하고, 문자 클래스를 사용하고, 반복되는 문자를 압축하는 연습을 하게 됩니다.

이 랩은 실제 시나리오에서 텍스트 조작 개념을 적용하고 `tr` 명령어에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

문자를 변환하는 데 사용되는 명령어는 무엇입니까? (소문자 영어 알파벳만으로 답하십시오)

## Quiz Answer

tr
