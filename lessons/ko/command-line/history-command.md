---
index: 9
lang: "ko"
title: "history"
meta_title: "history - 명령줄"
meta_description: "Linux history 명령어, !! 단축키, Ctrl-R 을 사용하여 효율적인 명령어 재호출 방법을 배우세요. 이 필수 팁으로 터미널 생산성을 향상시키세요!"
meta_keywords: "Linux history, bash history, Ctrl-R, clear command, Linux tutorial, command line, beginner guide"
---

## Lesson Content

쉘에는 이전에 입력했던 명령어들의 기록이 있습니다. 이 명령어들을 실제로 찾아볼 수 있습니다. 이는 이전에 사용했던 명령어를 다시 입력하지 않고도 찾아 실행하고 싶을 때 매우 유용합니다.

```bash
history
```

이전에 사용했던 동일한 명령어를 다시 실행하고 싶으신가요? 위쪽 화살표 키를 누르세요.

이전 명령어를 다시 입력하지 않고 실행하고 싶으신가요? `!!`를 사용하세요. 만약 `cat file1`을 입력했고 이를 다시 실행하고 싶다면, `!!`를 입력하기만 하면 마지막으로 실행했던 명령어가 실행됩니다.

또 다른 히스토리 단축키는 `Ctrl-R`입니다. 이것은 역방향 검색 명령어입니다. `Ctrl-R`을 누르고 원하는 명령어의 일부를 입력하기 시작하면 일치하는 항목을 보여줍니다. `Ctrl-R` 키를 다시 누르면 항목들을 탐색할 수 있습니다. 다시 사용하고 싶은 명령어를 찾으면 Enter 키를 누르세요.

터미널이 조금 지저분해졌죠? 좀 정리해 봅시다. `clear` 명령어를 사용하여 화면을 지우세요.

```bash
clear
```

자, 이제 좀 나아 보이죠?

유용한 기능에 대해 이야기하는 김에, 모든 명령줄 환경에서 가장 유용한 기능 중 하나는 탭 완성 (tab completion) 입니다. 명령어, 파일, 디렉토리 등의 시작 부분을 입력하고 Tab 키를 누르면, 검색하는 디렉토리에서 찾은 내용을 기반으로 자동 완성됩니다. 단, 해당 문자로 시작하는 다른 파일이 없어야 합니다. 예를 들어, `chrome` 명령어를 실행하려고 할 때 `chr`을 입력하고 Tab 을 누르면 `chrome`으로 자동 완성됩니다.

## Exercise

이 주제에 대한 특정 랩은 없지만, 관련 Linux 기술 및 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 탐색하는 것을 권장합니다.

## Quiz Question

터미널을 지우는 명령어는 무엇입니까?

## Quiz Answer

clear
