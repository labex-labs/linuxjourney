---
lesson_id: "git-diff-command"
course_id: "git"
lang: "ko"
order_index: 3
title: "git diff"
description: "git diff로 작업 트리의 파일과 스테이징된 파일을 비교하는 방법을 알아봅니다."
meta_title: "git diff - Git"
meta_description: "git diff로 작업 트리의 파일과 스테이징된 파일을 비교하는 방법을 알아봅니다."
meta_keywords: "git diff, 차이 비교, git, devops, Linux Journey"
---

상태를 보면 어느 파일이 바뀌었는지 알 수 있습니다. 어느 줄이 바뀌었는지 보려면 `git diff`를 사용합니다. 이 예에서는 앞 레슨에서 Hello라는 제목이 들어 있는 `index.html`을 이미 스테이징했습니다.

## 작업 파일을 스테이징된 버전과 비교하기

실습 파일의 제목을 바꾼 다음, 작업 트리의 파일과 스테이징된 버전을 비교합니다.

```bash
$ printf '%s\n' '<h1>Welcome</h1>' > index.html
$ git diff -- index.html
```

`--`는 옵션과 확인할 파일의 경로를 구분합니다. 출력에서 `-`로 시작하는 줄은 이전 버전의 내용입니다. `+`로 시작하는 줄은 바꾼 뒤의 내용입니다. 아래 두 줄은 이 편집을 보여 주는 출력의 일부입니다.

```diff
-<h1>Hello</h1>
+<h1>Welcome</h1>
```

:::single-choice{#git-diff-command-changed-heading} 현재 작업 파일에는 어떤 제목이 들어 있나요?

::option[Welcome입니다.]{#git-diff-command-changed-heading-b .correct explanation="이 비교에서 더하기 기호로 표시된 줄은 작업 트리의 새 내용입니다."}
::option[Hello입니다.]{#git-diff-command-changed-heading-a explanation="빼기 기호로 표시된 줄은 앞서 스테이징한 내용입니다."}
::option[두 제목이 모두 들어 있습니다.]{#git-diff-command-changed-heading-c explanation="두 줄은 같은 한 줄을 바꾸기 전과 바꾼 후의 모습입니다."}
:::

## 스테이징 영역과 이력 비교하기

`git diff --staged -- index.html`을 실행하면 스테이징된 내용을 가장 최근 커밋과 비교할 수 있습니다. 첫 커밋을 하기 전에는 빈 상태를 기준으로 비교합니다. 여기서는 스테이징된 Hello 제목이 추가된 줄로 표시됩니다. 한편 옵션 없는 `git diff`는 그 뒤에 제목을 Welcome으로 바꾼 내용을 보여 줍니다.

```bash
$ git diff --staged -- index.html
```

:::single-choice{#git-diff-command-preview-commit} 지금 커밋하면 어떤 내용이 들어갈지 미리 보려면 어느 명령을 사용해야 하나요?

::option[git diff -- index.html]{#git-diff-command-preview-commit-b explanation="이 명령은 현재 작업 파일을 스테이징된 파일과 비교합니다."}
::option[git status --short]{#git-diff-command-preview-commit-c explanation="상태 출력은 어디에 변경이 있는지 알려 주지만 바뀐 줄은 보여 주지 않습니다."}
::option[git diff --staged -- index.html]{#git-diff-command-preview-commit-a .correct explanation="이 명령은 스테이징한 내용을 이전에 저장한 상태와 비교합니다."}
:::

![작업 트리의 Welcome 제목과 스테이징된 Hello 제목을 비교하는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-diff-command/working-and-staged.png)

## 차이가 표시되지 않을 때 확인하기

현재 파일을 다시 스테이징해 스테이징된 버전을 갱신합니다.

```bash
$ git add index.html
$ git diff -- index.html
```

작업 파일과 스테이징된 버전이 같아졌으므로 옵션 없는 `git diff`에 아무것도 나오지 않을 수 있습니다. 아직 커밋하지 않은 변경을 보려면 스테이징된 내용을 이전 커밋과 비교하세요. 이런 일반적인 비교에서는 추적하지 않는 파일도 표시되지 않습니다. 변경이 어느 상태에 있는지 확실하지 않으면 저장소 상태를 확인하세요.

:::single-choice{#git-diff-command-empty-diff} 수정한 파일을 스테이징하자마자 옵션 없는 git diff를 실행했더니 아무것도 나오지 않습니다. 이전 이력과의 차이를 어디서 볼 수 있나요?

::option[옵션 없는 git diff를 한 번 더 실행합니다.]{#git-diff-command-empty-diff-a explanation="같은 비교를 반복해도 두 버전이 같아서 차이가 나오지 않습니다."}
::option[git diff --staged에서 볼 수 있습니다.]{#git-diff-command-empty-diff-c .correct explanation="스테이징된 버전을 이력에 있는 기준 상태와 비교합니다."}
::option[커밋한 뒤에만 볼 수 있습니다.]{#git-diff-command-empty-diff-b explanation="커밋을 만들기 전에 들어갈 변경을 확인할 수 있습니다."}
:::

## 요약

이제 확인하려는 내용에 맞는 비교를 고를 수 있습니다.

1. 차이를 보여 주는 출력에서 삭제된 줄과 추가된 줄을 읽습니다.
2. 작업 중인 파일을 스테이징 영역과 비교합니다.
3. 커밋 전에 스테이징한 변경을 미리 봅니다.
