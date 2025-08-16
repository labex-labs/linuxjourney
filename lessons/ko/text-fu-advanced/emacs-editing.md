---
lang: "ko"
title: "Emacs 편집"
description: "Emacs 편집의 기본 사항: 텍스트 탐색, 효율적인 잘라내기 및 붙여넣기를 배웁니다. 이 초보자 친화적인 가이드는 Linux 에서 필수 Emacs 명령을 마스터하는 데 도움이 됩니다."
keywords: "Emacs, Emacs 튜토리얼, Emacs 명령, 텍스트 편집기, Linux 편집기, Emacs 탐색, 초보자 Emacs, Emacs 가이드"
---

## Lesson Content

### Text Navigation

```
C-up arrow: move up one paragraph
C-down arrow: move down one paragraph
C-left arrow: move one word left
C-right arrow: move one word right
M->: move to the end of the buffer
```

텍스트 탐색 시, Home, End, Page Up, Page Down, 화살표 키 등 일반적인 텍스트 버튼이 정상적으로 작동합니다.

### Cutting and Pasting

Emacs 에서 자르기 (kill) 또는 붙여넣기 (yank) 를 하려면 먼저 텍스트를 선택할 수 있어야 합니다. 텍스트를 선택하려면 커서를 자르거나 붙여넣고 싶은 위치로 이동한 다음 `C-space key`를 누릅니다. 그런 다음 탐색 키를 사용하여 원하는 텍스트를 선택할 수 있습니다. 이제 다음과 같이 자르고 붙여넣을 수 있습니다:

```
C-w: cut
C-y: yank
```

## Exercise

텍스트 탐색을 연습해 보세요.

## Quiz Question

버퍼의 끝으로 이동하려면 어떻게 해야 합니까?

## Quiz Answer

M->
