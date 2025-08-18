---
index: 6
lang: "ko"
title: "Vim 텍스트 삽입 및 추가"
meta_title: "Vim 텍스트 삽입 및 추가 - 고급 Text-Fu"
meta_description: "Vim 의 삽입 및 추가 모드를 배웁니다. 효율적인 텍스트 편집을 위한 'i', 'a', 'I', 'A', 'o', 'O' 명령을 이해합니다. 지금 바로 Vim 기술을 향상시키세요!"
meta_keywords: "Vim 삽입 모드, Vim 추가, Vim 명령, Vim 튜토리얼, Linux 텍스트 편집기, 초보자 Vim, Vim 가이드, Vim 'i' 'a"
---

## Lesson Content

Vim 에는 자주 사용하게 될 두 가지 주요 모드가 있습니다: Normal 모드 (명령용) 와 Insert 모드 (텍스트 입력용).

- 언제든지 `Esc`를 눌러 Normal 모드로 돌아갈 수 있습니다.

텍스트를 입력하려는 위치에 따라 다양한 방법으로 Insert 모드에 진입할 수 있습니다:

- `i` – 커서 앞에 삽입
- `a` – 커서 뒤에 추가
- `I` – 현재 줄의 시작 부분에 삽입
- `A` – 현재 줄의 끝 부분에 추가
- `o` – 현재 줄 아래에 새 줄을 열고 삽입 시작
- `O` – 현재 줄 위에 새 줄을 열고 삽입 시작

팁: 이 명령들 앞에 숫자를 붙일 수 있습니다. 예를 들어, `3o`는 아래에 세 개의 새 줄을 엽니다.

텍스트 삽입을 마쳤으면 `Esc`를 눌러 Normal 모드로 돌아갑니다.

## Exercise

`vim [file]`로 아무 텍스트 파일을 열고 다음을 시도해 보세요: `i`, `a`, `I`, `A`, `o`, `O`를 사용한 다음, 각각의 작업 후에 `Esc`를 눌러 Normal 모드로 돌아갑니다.

## Quiz Question

커서 앞에 Insert 모드로 진입하는 키는 무엇입니까?

## Quiz Answer

i
