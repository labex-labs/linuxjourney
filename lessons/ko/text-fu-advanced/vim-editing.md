---
lang: "ko"
title: "Vim 편집"
meta_title: "Vim 편집 - 고급 Text-Fu"
meta_description: "Vim 편집의 기본 사항을 배우세요: 텍스트를 효율적으로 삭제, 변경, 복사, 붙여넣기. 초보자를 위한 필수 Vim 명령을 익히고 Linux 텍스트 편집 기술을 향상시키세요."
meta_keywords: "Vim 편집, Vim 명령, Linux 텍스트 편집기, Vim 튜토리얼, Vim 가이드, 초보자 Vim, dd 명령, Vim 삭제"
---

## Lesson Content

Vim 에서의 편집은 Normal 모드에서 연산자 (operator) 와 이동 (motion) 을 사용하여 수행됩니다. 텍스트를 효율적으로 삭제 (delete), 변경 (change), 복사 (yank), 붙여넣기 (paste), 그리고 교체 (replace) 할 수 있습니다.

- 이 명령들을 사용하기 전에 `Esc`를 눌러 Normal 모드에 있는지 확인하십시오.

삭제 (operator `d`):

- `x` – 커서 아래의 문자 삭제
- `dw` – 커서부터 다음 단어 시작까지 삭제
- `d$` – 커서부터 줄 끝까지 삭제
- `dd` – 현재 줄 삭제
- 횟수 적용: `3dd`는 세 줄을 삭제하고; `2dw`는 두 단어를 삭제합니다.

변경 (operator `c`, 삭제 후 Insert 모드 진입):

- `cw` – 커서부터 단어 변경
- `c$` – 줄 끝까지 변경
- `cc` – 전체 줄 변경

복사 (Yank) 및 붙여넣기 (Put):

- `yw` – 단어 복사
- `yy` – 현재 줄 복사
- `p` – 커서 뒤 또는 줄 아래에 붙여넣기
- `P` – 커서 앞 또는 줄 위에 붙여넣기

교체 (Replace) 및 기타 유용한 편집:

- `r{char}` – 커서 아래의 문자를 `{char}`로 교체
- `R` – 텍스트를 덮어쓰기 위해 Replace 모드 진입
- `J` – 현재 줄을 다음 줄과 연결
- `.` – 마지막 변경 반복

연산자를 이동과 결합하여 강력하게 사용하십시오: `d}`는 다음 단락까지 삭제하고; `caw`는“a word” (주변 공백을 포함한 커서 아래 단어) 를 변경합니다.

## Exercise

`vim [file]`로 파일을 열고 다음을 시도하십시오: `dw`, `cw`, `yy` 다음 `p`, `dd`, `J`, 그리고 `.`를 사용하여 변경을 반복합니다.

## Quiz Question

Vim 에서 현재 줄을 삭제하는 명령은 무엇입니까?

## Quiz Answer

dd
