---
index: 3
lang: "ko"
title: "cd (디렉토리 변경)"
meta_title: "cd (디렉토리 변경) - 명령줄"
meta_description: "디렉토리를 변경하는 필수적인 cd 리눅스 명령어를 알아보세요. 이 가이드는 명령 프롬프트에서 cd 명령 사용법, 절대 및 상대 경로를 사용하여 모든 cd 폴더로 이동하는 방법, 유용한 단축키를 다룹니다."
meta_keywords: "cd 명령어, cd 리눅스 명령어, cd 폴더, cd 명령 프롬프트, cd 명령어 cmd, 디렉토리 변경, 리눅스 탐색, 절대 경로, 상대 경로"
---

## Lesson Content

리눅스 파일 시스템을 탐색하려면 목적지를 지정하기 위해 경로를 사용하게 됩니다. 이를 위한 주요 도구는 `cd`(디렉토리 변경) 명령어입니다. 이 `cd linux command` 사용법을 이해하는 것은 터미널이나 `cd command prompt`에서 작업하는 데 필수적인 기술입니다.

### 경로 이해하기

경로를 지정하는 방법에는 두 가지가 있습니다: 절대 경로와 상대 경로.

- **절대 경로**: 이는 루트 디렉토리 (`/`) 에서 시작하는 전체 경로입니다. 루트는 파일 시스템의 최상위 디렉토리입니다. `/`로 시작하는 모든 경로는 절대 경로입니다. 예시: `/home/pete/Desktop`.

- **상대 경로**: 이 경로는 파일 시스템 내 현재 위치를 기준으로 합니다. 만약 `/home/pete/Documents`에 있고 `taxes`라는 하위 디렉토리에 접근하고 싶다면, 전체 경로가 필요하지 않습니다. 단순히 상대 경로인 `taxes/`를 사용할 수 있습니다.

### cd 명령어 사용하기

경로를 이해했다면, `cd command`를 사용하여 현재 디렉토리를 변경할 수 있습니다. 리눅스 터미널에 있든 Windows `cd command cmd` 프롬프트에 있든, 디렉토리를 변경하는 개념은 보편적이지만 구문은 약간 다를 수 있습니다.

절대 경로를 사용하여 특정 디렉토리로 변경하려면 다음과 같이 입력합니다:

```bash
cd /home/pete/Pictures
```

이 명령어는 사용자를 `Pictures` 디렉토리로 직접 이동시킵니다.

### cd 폴더로 이동하기

이미 디렉토리 내에 있고 하위 디렉토리로 이동하고 싶다면 상대 경로를 사용할 수 있습니다. 예를 들어, 현재 위치가 `/home/pete/Pictures`이고 그 안에 `Hawaii`라는 `cd folder`가 있다면, 다음과 같이 이동할 수 있습니다:

```bash
cd Hawaii
```

이름만 사용했다는 점에 유의하세요. 이는 현재 부모 디렉토리인 `/home/pete/Pictures` 안에 있었기 때문입니다.

### 필수 탐색 단축키

전체 경로로 탐색하는 것은 지루할 수 있습니다. 다행히 셸은 이동을 훨씬 빠르게 만드는 몇 가지 단축키를 제공합니다.

- `.` (현재 디렉토리): 현재 위치한 디렉토리를 나타냅니다.
- `..` (부모 디렉토리): 현재 디렉토리를 포함하는 상위 디렉토리로 한 단계 이동합니다.
- `~` (홈 디렉토리): `/home/pete`와 같은 개인 홈 디렉토리에 대한 바로 가기입니다.
- `-` (이전 디렉토리): 마지막으로 있었던 디렉토리로 돌아갑니다.

You can use these shortcuts with the `cd command`:

```bash
cd .
cd ..
cd ~
cd -
```

이 단축키들을 실험하여 명령줄에서 더 효율적으로 작업해 보세요.

## Exercise

연습이 완벽을 만듭니다! 리눅스 디렉토리 탐색에 대한 이해를 강화하기 위한 몇 가지 실습 랩이 있습니다:

1. **[Linux cd Command: Directory Changing](https://labex.io/ko/labs/linux-linux-cd-command-directory-changing-209733)** - 다양한 디렉토리 변경 기술, 경로 이해, 파일 구조 탐색을 포함하여 파일 시스템을 효율적으로 탐색하기 위한 리눅스 `cd` 명령어 학습.
2. **[Linux Directory Navigation](https://labex.io/ko/labs/linux-directory-navigation-387844)** - 필수 명령어를 사용하여 디렉토리를 탐색하며 기본적인 리눅스 명령줄 기술을 테스트해 보세요.
3. **[Setting Up a New Project Structure](https://labex.io/ko/labs/linux-setting-up-a-new-project-structure-387859)** - `mkdir` 및 `cd`와 같은 필수 명령어를 사용하여 특정 프로젝트 구조를 생성하고 탐색하면서 리눅스 디렉토리 관리 기술을 연습하세요.

이 랩들은 실제 시나리오에 개념을 적용하고 리눅스 파일 시스템 탐색에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

만약 `/home/pete/Pictures`에 있고 부모 디렉토리 (`/home/pete`) 로 이동하려면, 사용해야 할 전체 명령어는 무엇입니까? 대소문자와 공백에 주의하여 영어로 답변해 주세요.

## Quiz Answer

cd ..
