---
lesson_id: "change-directory-cd-command"
course_id: "command-line"
lang: "ko"
order_index: 3
title: "cd (디렉토리 변경)"
description: "경로와 바로가기를 사용해 리눅스 파일 시스템을 이동하는 cd 명령어를 배웁니다."
meta_title: "cd (디렉토리 변경) - 명령줄"
meta_description: "절대 경로, 상대 경로, 홈 디렉토리 바로가기, 상위 디렉토리, 이전 디렉토리 이동 예제와 함께 Linux cd 명령어를 배워보세요."
meta_keywords: "cd 명령어, linux cd 명령어, 디렉토리 변경, cd 상위 디렉토리, cd 홈, cd 이전 디렉토리, 절대 경로, 상대 경로"
---

Linux 파일 시스템을 이동하려면 경로를 사용하여 목적지를 지정합니다. 이때 주로 사용하는 도구가 `cd` 명령어이며, change directory(디렉토리 변경)의 약자입니다. 이 명령어는 셸의 현재 작업 디렉토리를 변경합니다.

목적지는 일반 파일이 아니라 디렉터리여야 합니다. 디렉터리가 없거나 이름을 잘못 입력했거나 들어갈 권한이 없으면 `cd`는 위치를 바꾸지 않고 오류를 표시합니다.

기본 구문은 다음과 같습니다:

```bash
cd [DIRECTORY]
```

## 경로 이해하기

경로를 지정하는 방법에는 절대 경로와 상대 경로 두 가지가 있습니다.

- **절대 경로**: 루트 디렉토리(`/`)부터 시작하는 전체 경로입니다. 예를 들어: `/home/pete/Desktop`.

- **상대 경로**: 현재 위치를 기준으로 한 경로입니다. 예를 들어 현재 위치가 `/home/pete/Documents`이고 `taxes`라는 하위 디렉토리에 접근하려면 `taxes/`를 사용할 수 있습니다.

:::single-choice{#recognize-absolute-cd-path}
절대 경로를 올바르게 설명한 것은 무엇인가요?

::option[쉘이 현재 사용 중인 디렉터리에서 시작합니다.]{#begins-at-current-directory explanation="쉘의 현재 위치에 따라 달라지는 경로는 상대 경로입니다. 상대 경로가 반드시 루트에서 시작하는 것은 아닙니다."}
::option[상위 디렉터리 없이 마지막 디렉터리 이름만 포함합니다.]{#contains-final-name-only explanation="목적지 이름 하나만 쓰면 보통 현재 디렉터리를 기준으로 해석합니다. 절대 경로에는 `/`부터 이어지는 경로가 포함됩니다."}
::option[`/`로 표시되는 루트 디렉터리에서 시작합니다.]{#begins-at-root .correct explanation="절대 경로는 파일 시스템 루트에서 시작합니다. 맨 앞의 `/` 덕분에 현재 디렉터리와 무관하게 시작점이 정해집니다."}
:::

## cd 명령어 사용법

절대 경로를 사용해 특정 디렉토리로 이동하려면 다음과 같이 입력합니다:

```bash
$ cd /home/pete/Pictures
```

이 명령어는 `Pictures` 디렉토리로 바로 이동합니다.

현재 위치를 확인하려면 `pwd`를 사용하세요:

```bash
$ pwd
/home/pete/Pictures
```

:::single-choice{#verify-changed-directory}
`cd`를 실행한 뒤 쉘의 현재 위치를 확인하는 명령어는 무엇인가요?

::option[`cd`]{#cd-command explanation="`cd`는 현재 디렉터리를 바꾸지만 보통 바뀐 전체 경로를 출력하지 않습니다. 확인하려면 `pwd`를 사용합니다."}
::option[`ls`]{#ls-command explanation="`ls`는 디렉터리 내용을 보여 줍니다. 위치를 살펴보는 데 도움은 되지만 위치 자체는 `pwd`가 알려 줍니다."}
::option[`pwd`]{#pwd-command .correct explanation="`pwd`는 현재 작업 디렉터리를 출력하므로 `cd`가 쉘을 어디로 이동했는지 확인할 수 있습니다."}
:::

## 하위 디렉토리로 이동하기

이미 디렉토리 안에 있을 때 하위 디렉토리로 이동하려면 상대 경로를 사용합니다. 예를 들어 현재 위치가 `/home/pete/Pictures`이고 그 안에 `Hawaii`라는 폴더가 있다면 다음과 같이 이동할 수 있습니다:

```bash
$ cd Hawaii
```

폴더 이름만 사용한 것을 주목하세요. 이는 이미 상위 디렉토리인 `/home/pete/Pictures`에 있기 때문입니다.

## 필수 네비게이션 바로가기

전체 경로를 사용해 이동하는 것은 번거로울 수 있습니다. 다행히 셸은 이동을 훨씬 빠르게 해주는 여러 바로가기를 제공합니다.

- `.` (현재 디렉토리): 현재 위치한 디렉토리를 나타냅니다.
- `..` (상위 디렉토리): 현재 디렉토리를 포함하는 한 단계 위 디렉토리로 이동합니다.
- `~` (홈 디렉토리): 개인 홈 디렉토리의 바로가기입니다. 예: `/home/pete`.
- `-` (이전 디렉토리): 마지막으로 있던 디렉토리로 돌아갑니다.

이 바로가기들은 `cd`와 함께 사용할 수 있습니다:

```bash
$ cd .
$ cd ..
$ cd ~
$ cd -
```

:::single-choice{#move-to-parent-directory}
`/home/pete/Pictures`에서 `/home/pete`로 이동하는 명령어는 무엇인가요?

::option[`cd .`]{#cd-current explanation="`.`은 현재 디렉터리를 나타내므로 쉘은 `/home/pete/Pictures`에 그대로 머뭅니다."}
::option[`cd -`]{#cd-previous explanation="`-`는 이전 작업 디렉터리로 돌아가며, 그곳이 반드시 상위 디렉터리인 것은 아닙니다. 한 단계 위로 갈 때는 `..`을 사용합니다."}
::option[`cd ..`]{#cd-parent .correct explanation="`..`은 현재 디렉터리의 상위를 나타냅니다. `Pictures`의 상위 디렉터리는 `/home/pete`입니다."}
:::

:::single-choice{#return-to-previous-directory}
현재 디렉터리 바로 전에 사용했던 디렉터리로 돌아가는 명령어는 무엇인가요?

::option[`cd -`]{#previous-directory .correct explanation="`cd -`는 이전 작업 디렉터리로 전환합니다. 그 디렉터리는 파일 시스템 어디에나 있을 수 있습니다."}
::option[`cd ..`]{#parent-directory explanation="`cd ..`은 상위 디렉터리로 이동합니다. 상위 디렉터리와 이전에 방문한 디렉터리는 항상 같지는 않습니다."}
::option[`cd ~`]{#home-directory explanation="`cd ~`는 홈 디렉터리로 이동하며 바로 전에 방문한 디렉터리를 추적하지 않습니다."}
:::

이 바로가기들을 실험해 보며 명령줄에서 더 효율적으로 이동하는 방법을 익히세요.

## 실용적인 cd 예제

홈 디렉토리로 이동하기:

```bash
$ cd
```

디렉터리 인자 없이 `cd`를 실행해도 홈 디렉터리로 이동합니다.

두 단계 위로 이동하기:

```bash
$ cd ../..
```

공백이 포함된 디렉토리 이름으로 이동할 때는 따옴표로 묶기:

```bash
$ cd "Vacation Photos"
```

:::single-choice{#enter-directory-with-spaces}
`Vacation Photos`를 하나의 디렉터리 이름으로 처리하는 명령어는 무엇인가요?

::option[`cd Vacation Photos`]{#unquoted-directory-name explanation="따옴표가 없으면 쉘은 `Vacation`과 `Photos`를 하나의 디렉터리 이름이 아닌 별도 인자로 전달합니다."}
::option[`"cd Vacation Photos"`]{#quote-entire-command explanation="전체 줄을 따옴표로 묶으면 쉘은 이를 하나의 명령어 이름으로 처리합니다. 명령어 자체는 경로의 따옴표 밖에 있어야 합니다."}
::option[`cd "Vacation Photos"`]{#quote-directory-name .correct explanation="따옴표가 두 단어를 `cd`에 전달할 하나의 경로 인자로 묶습니다."}
:::

이전 디렉토리로 돌아가기:

```bash
$ cd -
/home/pete/Documents
```

Linux 디렉터리 탐색을 더 익히려면 다음 실습을 활용해 보세요.

1. **[Linux cd 명령어: 디렉토리 변경](https://labex.io/ko/labs/linux-linux-cd-command-directory-changing-209733)** - 다양한 디렉토리 변경 기법, 경로 이해, 파일 구조 탐색을 포함하여 Linux `cd` 명령어를 효율적으로 배우세요.
2. **[Linux 디렉토리 탐색](https://labex.io/ko/labs/linux-directory-navigation-387844)** - 필수 명령어를 사용해 디렉토리를 탐색하며 기본 Linux 명령줄 실력을 테스트해 보세요.
3. **[새 프로젝트 구조 설정하기](https://labex.io/ko/labs/linux-setting-up-a-new-project-structure-387859)** - `mkdir`과 `cd` 같은 필수 명령어를 사용해 특정 프로젝트 구조를 만들고 탐색하는 Linux 디렉토리 관리 기술을 연습하세요.

## 요약

이제 전체 경로와 쉘 바로가기를 사용해 `cd`로 디렉터리 사이를 이동할 수 있습니다.

1. 절대 경로와 상대 경로를 구분할 수 있습니다.
2. 디렉터리를 바꾸고 `pwd`로 결과를 확인할 수 있습니다.
3. 상위, 홈, 이전 디렉터리로 이동할 수 있습니다.
4. 공백이 포함된 디렉터리 이름으로 들어갈 수 있습니다.
5. 일반적인 경로 및 권한 오류를 알아볼 수 있습니다.
