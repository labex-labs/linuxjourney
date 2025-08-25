---
index: 12
lang: "ko"
title: "Emacs 편집"
meta_title: "Emacs 편집 - 고급 텍스트 기술"
meta_description: "Emacs 편집의 기본 사항을 배웁니다: 텍스트 탐색, 효율적인 잘라내기 및 붙여넣기. 이 초보자 친화적인 가이드는 Linux 에서 필수 Emacs 명령을 마스터하는 데 도움이 됩니다."
meta_keywords: "Emacs, Emacs 튜토리얼, Emacs 명령, 텍스트 편집기, Linux 편집기, Emacs 탐색, 초보자 Emacs, Emacs 가이드"
---

## Lesson Content

### 텍스트 탐색

```
C-up arrow: move up one paragraph
C-down arrow: move down one paragraph
C-left arrow: move one word left
C-right arrow: move one word right
M->: move to the end of the buffer
```

텍스트 탐색 시, 일반적인 텍스트 버튼 (Home, End, Page Up, Page Down, 화살표 키 등) 은 정상적으로 작동합니다.

### 잘라내기 및 붙여넣기

Emacs 에서 잘라내기 (kill) 또는 붙여넣기 (yank) 를 하려면 먼저 텍스트를 선택할 수 있어야 합니다. 텍스트를 선택하려면 커서를 잘라내거나 붙여넣을 위치로 이동한 다음 `C-space key`를 누릅니다. 그런 다음 탐색 키를 사용하여 원하는 텍스트를 선택할 수 있습니다. 이제 다음과 같이 잘라내고 붙여넣을 수 있습니다:

```
C-w: cut
C-y: yank
```

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 사용자 및 그룹 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[useradd, usermod, userdel 을 사용하여 Linux 사용자 계정 관리](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성 및 보안 설정부터 수정 및 삭제에 이르기까지 사용자 관리의 전체 수명 주기를 연습합니다.
2. **[groupadd, usermod, groupdel 을 사용하여 Linux 그룹 관리](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - 새 그룹 생성, 사용자 멤버십 수정, 그룹 제거를 포함하여 그룹 관리를 위한 핵심 명령줄 유틸리티를 직접 경험해 봅니다.
3. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 암호 정책 적용 및 관리 권한 부여를 포함하여 Linux 시스템의 보안을 강화하기 위한 사용자 계정 및 sudo 권한 관리의 필수 기술을 배웁니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux 에서 사용자 및 그룹 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

버퍼의 끝으로 이동하려면 어떻게 해야 합니까?

## Quiz Answer

M->
