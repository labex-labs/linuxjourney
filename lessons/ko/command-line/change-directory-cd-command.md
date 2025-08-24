---
index: 3
lang: "ko"
title: "cd (디렉토리 변경)"
meta_title: "cd (디렉토리 변경) - 명령줄"
meta_description: "Linux 에서 'cd' 명령어를 사용하여 디렉토리를 탐색하는 방법을 배우세요. 절대 경로, 상대 경로 및 유용한 단축키를 이해하세요. Linux 여정을 시작하세요!"
meta_keywords: "cd 명령어, 디렉토리 변경, Linux 경로, 절대 경로, 상대 경로, Linux 튜토리얼, 초보자 Linux, Linux 탐색"
---

## Lesson Content

이제 현재 위치를 알았으니 파일 시스템을 좀 둘러봅시다. 경로를 사용하여 이동해야 한다는 것을 기억하세요. 경로를 지정하는 방법에는 절대 경로와 상대 경로의 두 가지가 있습니다.

- 절대 경로: 루트 디렉토리에서 시작하는 경로입니다. 루트는 최고 책임자입니다. 루트 디렉토리는 일반적으로 슬래시 (`/`) 로 표시됩니다. 경로가 `/`로 시작할 때마다 루트 디렉토리에서 시작한다는 의미입니다. 예를 들어, `/home/pete/Desktop`입니다.

- 상대 경로: 현재 파일 시스템에 있는 위치에서 시작하는 경로입니다. 만약 제가 `/home/pete/Documents`에 있고 `Documents` 안에 있는 `taxes`라는 디렉토리로 이동하고 싶다면, `/home/pete/Documents/taxes`와 같이 루트에서 전체 경로를 지정할 필요 없이 `taxes/`로 이동할 수 있습니다.

이제 경로가 어떻게 작동하는지 알았으니, 원하는 디렉토리로 변경하는 데 도움이 되는 것이 필요합니다. 다행히 `cd` 또는 "change directory" 명령어가 있습니다.

```bash
cd /home/pete/Pictures
```

이제 디렉토리 위치를 `/home/pete/Pictures`로 변경했습니다.

이 디렉토리 안에 `Hawaii`라는 폴더가 있습니다. 다음 명령어로 해당 폴더로 이동할 수 있습니다:

```bash
cd Hawaii
```

폴더 이름만 사용한 것을 눈치채셨나요? 이미 `/home/pete/Pictures`에 있었기 때문입니다.

항상 절대 경로와 상대 경로로 이동하는 것은 꽤 피곤할 수 있습니다. 다행히도 도움이 되는 몇 가지 단축키가 있습니다.

- `.` (현재 디렉토리): 현재 있는 디렉토리입니다.
- `..` (이전 디렉토리): 현재 디렉토리의 상위 디렉토리로 이동합니다.
- `~` (홈 디렉토리): 이 디렉토리는 `/home/pete`와 같은 "홈 디렉토리"로 기본 설정됩니다.
- `-` (이전 디렉토리): 방금 있었던 이전 디렉토리로 이동합니다.

```bash
cd .
cd ..
cd ~
cd -
```

한번 시도해보세요!

## Exercise

1. 플래그 없이 `cd` 명령어를 실행해 보세요. 어디로 이동하나요?

`cd` 명령어를 직접 연습하려면 다음 대화형 실습을 시도해 보세요:

- [Linux cd Command: Directory Changing](https://labex.io/ko/labs/linux-linux-cd-command-directory-changing-209733)

## Quiz Question

`/home/pete/Pictures`에 있고 `/home/pete`로 이동하고 싶다면, 어떤 좋은 단축키를 사용할 수 있을까요?

## Quiz Answer

cd ..
