---
index: 5
lang: "ko"
title: "touch"
meta_title: "touch - 명령줄"
meta_description: "Linux touch 명령어를 사용하여 새 파일을 만들고 타임스탬프를 업데이트하는 방법을 배우세요. 이 초보자 친화적인 가이드는 파일 관리를 이해하는 데 도움이 됩니다."
meta_keywords: "touch 명령어, 파일 생성, Linux 튜토리얼, 파일 타임스탬프, 초보자를 위한 Linux, Linux 가이드, 기본 명령어"
---

## Lesson Content

파일을 만드는 방법을 배워봅시다. 아주 간단한 방법은 `touch` 명령어를 사용하는 것입니다. `touch`를 사용하면 새로운 빈 파일을 만들 수 있습니다.

```bash
touch mysuperduperfile
```

그리고 짠, 새 파일이 생겼습니다!

`touch`는 또한 기존 파일 및 디렉터리의 타임스탬프를 변경하는 데 사용됩니다. 한번 시도해 보세요: 파일에 `ls -l`을 실행하여 타임스탬프를 확인한 다음, 해당 파일을 `touch`하면 타임스탬프가 업데이트됩니다.

리디렉션 및 텍스트 편집기와 같은 다른 방법을 포함하여 파일을 만드는 다른 많은 방법이 있지만, 이는 텍스트 조작 과정에서 다룰 것입니다.

## Exercise

연습하면 완벽해집니다! 파일 시스템 객체 생성 및 관리에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux mkdir 명령어: 디렉토리 생성](https://labex.io/ko/labs/linux-linux-mkdir-command-directory-creating-209739)** - Linux에서 `mkdir` 명령어를 사용하여 디렉토리를 생성하고, 권한을 설정하고, 파일 시스템을 구성하는 방법을 배웁니다. 이는 파일 시스템에서 새 항목을 생성하는 더 넓은 개념을 이해하는 데 도움이 될 것입니다.
2. **[새 프로젝트 구조 설정](https://labex.io/ko/labs/linux-setting-up-a-new-project-structure-387859)** - `mkdir` 및 `cd`와 같은 필수 명령어를 사용하여 특정 프로젝트 구조를 생성하고 탐색함으로써 Linux 디렉토리 관리 기술을 연습합니다.

이러한 랩은 실제 시나리오에서 파일 시스템 생성 및 구성 개념을 적용하고 Linux 명령어에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`myfile`이라는 파일을 어떻게 생성합니까?

## Quiz Answer

touch myfile