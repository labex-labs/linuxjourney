---
lang: "ko"
title: "pwd (현재 작업 디렉토리 출력)"
meta_title: "pwd (현재 작업 디렉토리 출력) - Command Line"
meta_description: "Linux 에서 'pwd' 명령어를 사용하여 현재 작업 디렉토리를 출력하는 방법을 배우세요. 초보자를 위한 Linux 파일 시스템 경로 및 탐색을 이해합니다."
meta_keywords: "pwd 명령어, Linux 디렉토리, 현재 디렉토리, Linux 경로, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

Linux 의 모든 것은 파일입니다. Linux 를 더 깊이 탐구하면서 이 점을 이해하게 되겠지만, 지금은 그냥 기억해 두세요. 모든 파일은 계층적 디렉토리 트리로 구성됩니다. 파일 시스템의 첫 번째 디렉토리는 루트 디렉토리라고 불립니다. 루트 디렉토리에는 더 많은 폴더와 파일을 저장할 수 있는 많은 폴더와 파일이 있습니다. 다음은 디렉토리 트리가 어떻게 생겼는지 보여주는 예시입니다:

```plaintext
/
|-- bin
| |-- file1
| |-- file2
|-- etc
| |-- file3
| `-- directory1
|  |-- file4
|  `-- file5
|-- home
|-- var
```

이러한 파일과 디렉토리의 위치를 경로라고 합니다. `home`이라는 폴더 안에 `pete`이라는 폴더가 있고, 그 폴더 안에 `Movies`라는 또 다른 폴더가 있다면, 그 경로는 `/home/pete/Movies`와 같이 보일 것입니다. 아주 간단하죠?

파일 시스템 탐색은 실제 생활과 마찬가지로, 자신이 어디에 있고 어디로 가고 있는지 알면 도움이 됩니다. 자신이 어디에 있는지 확인하려면 `pwd` 명령어를 사용할 수 있습니다. 이 명령어는 "print working directory"를 의미하며, 현재 어떤 디렉토리에 있는지 보여줍니다. 경로는 루트 디렉토리에서 시작된다는 점에 유의하세요.

```bash
pwd
```

당신은 어디에 있나요? 저는 어디에 있나요? 한번 시도해 보세요.

## Exercise

No exercises for this lesson.

## Quiz Question

현재 어떤 디렉토리에 있는지 어떻게 알 수 있나요?

## Quiz Answer

pwd
