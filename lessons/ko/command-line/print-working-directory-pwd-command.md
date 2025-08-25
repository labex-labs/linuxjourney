---
index: 2
lang: "ko"
title: "pwd (현재 작업 디렉토리 출력)"
meta_title: "pwd (현재 작업 디렉토리 출력) - 명령줄"
meta_description: "Linux 에서 'pwd' 명령을 사용하여 현재 작업 디렉토리를 출력하는 방법을 배웁니다. 초보자를 위한 Linux 파일 시스템 경로 및 탐색을 이해합니다."
meta_keywords: "pwd 명령, Linux 디렉토리, 현재 디렉토리, Linux 경로, Linux 튜토리얼, 초보자 Linux, Linux 가이드"
---

## Lesson Content

Linux 의 모든 것은 파일입니다. Linux 를 더 깊이 탐구하면서 이 점을 이해하게 될 것이지만, 지금은 그냥 기억해 두세요. 모든 파일은 계층적 디렉토리 트리로 구성됩니다. 파일 시스템의 첫 번째 디렉토리는 적절하게도 루트 디렉토리라고 불립니다. 루트 디렉토리에는 더 많은 폴더와 파일을 저장할 수 있는 많은 폴더와 파일 등이 있습니다. 다음은 디렉토리 트리가 어떻게 생겼는지에 대한 예시입니다:

```plaintext
/
|-- bin
|   |-- file1
|   |-- file2
|-- etc
|   |-- file3
|   `-- directory1
|       |-- file4
|       `-- file5
|-- home
|-- var
```

이러한 파일과 디렉토리의 위치를 경로라고 합니다. `home`이라는 폴더 안에 `pete`이라는 폴더가 있고 그 폴더 안에 `Movies`라는 또 다른 폴더가 있다면, 그 경로는 `/home/pete/Movies`와 같이 보일 것입니다. 꽤 간단하죠?

파일 시스템 탐색은 실제 생활과 마찬가지로, 자신이 어디에 있고 어디로 가고 있는지 알면 도움이 됩니다. 자신이 어디에 있는지 확인하려면 `pwd` 명령을 사용할 수 있습니다. 이 명령은 "print working directory"를 의미하며, 현재 어떤 디렉토리에 있는지 보여줍니다. 경로는 루트 디렉토리에서 시작된다는 점에 유의하세요.

```bash
pwd
```

당신은 어디에 있나요? 저는 어디에 있나요? 한번 시도해 보세요.

## Exercise

연습은 완벽을 만듭니다! 다음은 Linux 파일 시스템 탐색 및 현재 위치 식별에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux pwd Command: Directory Displaying](https://labex.io/ko/labs/linux-linux-pwd-command-directory-displaying-209734)** - 이 랩은 `pwd` 명령에 대한 집중적인 개요와 실제 사용법을 제공하며, 현재 디렉토리를 찾는 방법에 대한 수업의 소개와 직접적으로 일치합니다.
2. **[Linux Directory Navigation](https://labex.io/ko/labs/linux-directory-navigation-387844)** - 다양한 디렉토리를 탐색하여 기본적인 Linux 명령줄 기술을 테스트하고, 경로와 파일 시스템 구조에 대한 이해를 확고히 합니다.
3. **[Linux cd Command: Directory Changing](https://labex.io/ko/labs/linux-linux-cd-command-directory-changing-209733)** - `cd` 명령을 사용하여 파일 시스템을 효율적으로 탐색하고, 디렉토리를 변경하고 파일 구조를 탐색하는 다양한 기술을 이해합니다.

이 랩들은 파일 시스템 계층 구조 및 탐색 개념을 실제 시나리오에 적용하고 필수 Linux 명령에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

현재 어떤 디렉토리에 있는지 어떻게 알 수 있나요?

## Quiz Answer

pwd
