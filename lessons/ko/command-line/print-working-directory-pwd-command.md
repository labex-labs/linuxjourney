---
index: 2
lang: "ko"
title: "pwd (현재 작업 디렉토리 출력)"
meta_title: "pwd (현재 작업 디렉토리 출력) - 명령줄"
meta_description: "Linux 에서 'pwd' 명령을 사용하여 현재 작업 디렉토리를 출력하는 방법을 배우세요. 초보자를 위한 Linux 파일 시스템 경로 및 탐색을 이해합니다."
meta_keywords: "pwd command, Linux directory, current directory, Linux path, Linux tutorial, beginner Linux, Linux guide"
---

## Lesson Content

Linux 의 모든 것은 파일입니다. Linux 를 더 깊이 탐구하면서 이 점을 이해하게 되겠지만, 지금은 이 점을 염두에 두십시오. 모든 파일은 계층적 디렉토리 트리로 구성됩니다. 파일 시스템의 첫 번째 디렉토리는 적절하게 루트 디렉토리라고 명명됩니다. 루트 디렉토리에는 더 많은 폴더와 파일을 저장할 수 있는 많은 폴더와 파일 등이 있습니다. 다음은 디렉토리 트리가 어떻게 생겼는지에 대한 예시입니다:

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

이러한 파일과 디렉토리의 위치를 경로라고 합니다. `home`이라는 폴더 안에 `pete`라는 폴더가 있고 그 폴더 안에 `Movies`라는 또 다른 폴더가 있다면, 그 경로는 `/home/pete/Movies`와 같이 보일 것입니다. 꽤 간단하죠?

파일 시스템 탐색은 실제 생활과 마찬가지로, 자신이 어디에 있고 어디로 가고 있는지 알면 도움이 됩니다. 현재 위치를 확인하려면 `pwd` 명령을 사용할 수 있습니다. 이 명령은 "print working directory"를 의미하며, 현재 어떤 디렉토리에 있는지 보여줍니다. 경로는 루트 디렉토리에서 시작된다는 점에 유의하십시오.

```bash
pwd
```

당신은 어디에 있습니까? 저는 어디에 있습니까? 한번 시도해 보세요.

## Exercise

`pwd` 명령을 직접 실습하려면 다음 대화형 랩을 시도해 보세요:

- [Linux pwd Command: Directory Displaying](https://labex.io/ko/labs/linux-linux-pwd-command-directory-displaying-209734)

## Quiz Question

현재 어떤 디렉토리에 있는지 어떻게 알 수 있습니까?

## Quiz Answer

pwd
