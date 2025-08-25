---
index: 11
lang: "ko"
title: "Emacs 버퍼 탐색"
meta_title: "Emacs 버퍼 탐색 - 고급 텍스트 기술"
meta_description: "Emacs 버퍼 탐색 명령을 배우십시오. 이 초보자 친화적인 Emacs 튜토리얼을 통해 버퍼를 효율적으로 전환, 닫기 및 분할하십시오. 워크플로우를 개선하십시오!"
meta_keywords: "Emacs 버퍼 탐색, Emacs 명령, C-x b, C-x k, Linux 튜토리얼, Emacs 가이드, 초보자 Emacs"
---

## Lesson Content

버퍼 (또는 방문 중인 파일) 사이를 이동하려면 다음 명령을 사용하십시오:

### 버퍼 전환

```
C-x b - switch buffer
C-x right arrow - right-cycle through buffer
C-x left arrow - left-cycle through buffer
```

### 버퍼 닫기

```
C-x k
```

### 현재 버퍼 분할

```
C-x 2
```

이렇게 하면 한 화면에서 여러 버퍼를 볼 수 있습니다. 이 버퍼들 사이를 이동하려면 다음을 사용하십시오: C-x o

### 단일 버퍼를 현재 화면으로 설정

```
C-x 1
```

`screen` 또는 `tmux`와 같은 터미널 멀티플렉서를 사용해 본 적이 있다면, 버퍼 명령이 매우 익숙하게 느껴질 것입니다.

## Exercise

연습이 완벽을 만듭니다! 텍스트 파일과 버퍼를 탐색하고 조작하는 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux 에서 Vim 및 Nano 로 텍스트 파일 편집](https://labex.io/ko/labs/comptia-edit-text-files-in-linux-with-vim-and-nano-591076)** - 버퍼 작업에 필수적인 Vim 및 Nano 편집기 내에서 텍스트를 생성, 편집, 저장 및 탐색하는 연습을 하십시오.
2. **[Linux cat 명령어: 파일 연결](https://labex.io/ko/labs/linux-linux-cat-command-file-concatenating-210986)** - 텍스트 파일을 보고, 연결하고, 조작하는 방법을 배우십시오. 이는 버퍼 콘텐츠와 상호 작용하는 방식에 직접 적용됩니다.
3. **[Linux 에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `cat`, `more`, `less`와 같은 명령어를 사용하여 텍스트 파일을 효율적으로 보고 탐색하는 연습을 하십시오. 이는 버퍼와 유사한 콘텐츠를 검토하는 실제 시나리오를 시뮬레이션합니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux 에서 텍스트 파일 및 버퍼 조작에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

버퍼를 어떻게 종료합니까?

## Quiz Answer

C-x k
