---
lesson_id: "git-status-command"
course_id: "git"
lang: "ko"
order_index: 2
title: "git status"
description: "git status로 추적하지 않는 파일, 스테이징한 파일, 수정한 파일을 구분하는 방법을 알아봅니다."
meta_title: "git status - Git"
meta_description: "git status로 추적하지 않는 파일, 스테이징한 파일, 수정한 파일을 구분하는 방법을 알아봅니다."
meta_keywords: "git status, git, devops, Linux Journey, 스테이징"
---

저장소에서 작업할 때 `git status`를 실행하면 Git이 작업 트리에서 어떤 변경을 발견했는지, 그중 무엇을 다음에 저장하도록 골랐는지 알 수 있습니다. 앞 레슨에서 만든 빈 `journey-git` 저장소를 사용하세요.

## 새 파일 찾기

작은 페이지를 만들고, 결과가 한눈에 들어오도록 짧은 형식으로 표시합니다.

```bash
$ printf '%s\n' '<h1>Hello</h1>' > index.html
$ git status --short
```

여기서 `>`는 지정한 파일에 내용을 씁니다. 파일이 이미 있으면 기존 내용을 덮어씁니다. 새 파일은 짧은 형식에서 `?? index.html`로 표시됩니다. Git에서는 이런 파일을 **추적하지 않는 파일**이라고 합니다. 파일은 있지만 저장할 내용에 아직 포함되지 않았습니다.

:::single-choice{#git-status-command-untracked-file} Git이 새 파일 옆에 물음표 두 개를 표시했습니다. 이 파일은 어떤 상태인가요?

::option[마지막으로 저장한 상태에 포함되어 있습니다.]{#git-status-command-untracked-file-a explanation="추적하지 않는 파일은 그때 저장한 상태에 들어 있지 않습니다."}
::option[작업 트리에서 삭제되었습니다.]{#git-status-command-untracked-file-c explanation="Git은 작업 트리에서 이 파일을 발견했습니다."}
::option[파일은 있지만 다음에 저장할 상태에는 아직 포함되지 않았습니다.]{#git-status-command-untracked-file-b .correct explanation="필요하면 이 파일을 스테이징 영역에 추가할 수 있습니다."}
:::

![index.html이 추적하지 않는 파일에서 스테이징된 파일로 바뀌는 모습을 보여 주는 Git의 짧은 상태 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-status-command/staged-file.png)

## 스테이징한 변경 확인하기

`git add`를 실행해 파일의 현재 내용을 다음에 저장할 상태에 포함합니다. 이렇게 저장한 상태를 **커밋**이라고 합니다. 저장할 내용을 골라 두는 곳이 **스테이징 영역**입니다. 짧은 상태 출력의 첫 번째 열에 추가를 뜻하는 `A`가 표시됩니다. 이 추가는 아직 커밋되지 않았습니다.

```bash
$ git add index.html
$ git status --short
```

:::single-choice{#git-status-command-staged-new} git add를 실행한 뒤, 선택한 index.html 버전은 어디에 있나요?

::option[이미 새 커밋에 들어 있습니다.]{#git-status-command-staged-new-a explanation="git add는 다음 커밋을 준비하는 명령입니다. 커밋 자체를 만들지는 않습니다."}
::option[스테이징 영역에 있습니다.]{#git-status-command-staged-new-c .correct explanation="Git은 git add를 실행할 당시의 파일 내용을 골라 두었습니다."}
::option[다른 사람의 저장소에 있습니다.]{#git-status-command-staged-new-b explanation="이 명령은 내 로컬 스테이징 영역에만 영향을 줍니다."}
:::

## 두 종류의 변경 구분하기

짧은 상태 출력에서는 파일 이름 앞에 두 열이 있습니다. 첫 번째 열은 스테이징한 변경, 두 번째 열은 스테이징한 뒤에 생긴 변경을 나타냅니다. 예를 들어 `AM index.html`은 새 파일을 스테이징한 다음 작업 트리에서 다시 수정했다는 뜻입니다. 항목별로 자세히 보려면 옵션 없이 `git status`를 실행하세요.

:::single-choice{#git-status-command-two-columns} index.html 옆에 AM이 표시됩니다. 다음 커밋 전에 무엇을 확인해야 하나요?

::option[저장하려는 수정 내용이 스테이징한 버전에 들어 있는지 확인합니다.]{#git-status-command-two-columns-a .correct explanation="두 번째 열의 M은 작업 트리에 나중에 수정한 내용이 있음을 뜻합니다."}
::option[저장소에 AM이라는 다른 파일이 있는지 확인합니다.]{#git-status-command-two-columns-b explanation="AM은 index.html의 상태를 나타내는 두 기호입니다."}
::option[파일이 디스크에서 삭제되었는지 확인합니다.]{#git-status-command-two-columns-c explanation="M은 작업 트리에서 파일이 수정되었음을 뜻합니다."}
:::

## 요약

이제 Git이 다음에 어떤 변경을 저장할지 확인할 수 있습니다.

1. 새로 생긴 추적하지 않는 파일을 알아봅니다.
2. git add로 파일을 스테이징합니다.
3. 스테이징한 변경과 작업 트리의 변경을 따로 읽습니다.
