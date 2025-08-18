---
index: 3
lang: "ko"
title: "cd (디렉토리 변경)"
meta_title: "cd (디렉토리 변경) - Command Line"
meta_description: "Linux 에서 'cd' 명령을 사용하여 디렉토리를 탐색하는 방법을 배웁니다. 절대 경로, 상대 경로 및 유용한 단축키를 이해합니다. Linux 여정을 시작하세요!"
meta_keywords: "cd command, change directory, Linux paths, absolute path, relative path, Linux tutorial, beginner Linux, Linux navigation"
---

## Lesson Content

이제 여러분이 어디에 있는지 알았으니, 파일 시스템을 좀 돌아다녀 봅시다. 경로를 사용하여 이동해야 한다는 것을 기억하세요. 경로를 지정하는 두 가지 방법이 있습니다: 절대 경로와 상대 경로.

- Absolute path: 이것은 루트 디렉토리로부터의 경로입니다. 루트는 최고 책임자입니다. 루트 디렉토리는 일반적으로 슬래시 (`/`) 로 표시됩니다. 경로가 `/`로 시작할 때마다 루트 디렉토리에서 시작한다는 의미입니다. 예를 들어, `/home/pete/Desktop`입니다.

- Relative path: 이것은 파일 시스템에서 현재 위치로부터의 경로입니다. 만약 제가 `/home/pete/Documents`에 있고 `Documents` 안에 있는 `taxes`라는 디렉토리로 가고 싶다면, `/home/pete/Documents/taxes`와 같이 루트로부터 전체 경로를 지정할 필요 없이, 단순히 `taxes/`로 이동할 수 있습니다.

이제 경로가 어떻게 작동하는지 알았으니, 우리가 원하는 디렉토리로 변경하는 데 도움이 되는 것이 필요합니다. 다행히도, `cd` 또는 "change directory"가 그 역할을 합니다.

```bash
cd /home/pete/Pictures
```

이제 제 디렉토리 위치를 `/home/pete/Pictures`로 변경했습니다.

이제 이 디렉토리 안에 `Hawaii`라는 폴더가 있습니다. 다음 명령으로 해당 폴더로 이동할 수 있습니다:

```bash
cd Hawaii
```

폴더 이름만 사용한 것을 눈치채셨나요? 이미 `/home/pete/Pictures`에 있었기 때문입니다.

항상 절대 경로와 상대 경로로 이동하는 것은 꽤 피곤할 수 있습니다. 다행히도, 여러분을 돕기 위한 몇 가지 단축키가 있습니다.

- `.` (current directory): 현재 있는 디렉토리입니다.
- `..` (previous directory): 현재 디렉토리의 상위 디렉토리로 이동합니다.
- `~` (home directory): 이 디렉토리는 `/home/pete`와 같은 "홈 디렉토리"로 기본 설정됩니다.
- `-` (previous directory): 방금 전에 있었던 이전 디렉토리로 이동합니다.

```bash
cd .
cd ..
cd ~
cd -
```

한번 시도해보세요!

## Exercise

1. 아무 플래그 없이 `cd` 명령을 실행해 보세요. 어디로 이동하나요?

## Quiz Question

만약 `/home/pete/Pictures`에 있고 `/home/pete`로 가고 싶다면, 어떤 좋은 단축키를 사용할 수 있을까요?

## Quiz Answer

cd ..
