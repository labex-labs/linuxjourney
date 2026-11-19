---
lesson_id: "git-revert-command"
course_id: "git"
lang: "ko"
order_index: 8
title: "git revert"
description: "git revert로 원래 커밋을 이력에 남겨 둔 채 변경을 취소하는 방법을 알아봅니다."
meta_title: "git revert - Git"
meta_description: "git revert로 원래 커밋을 이력에 남겨 둔 채 변경을 취소하는 방법을 알아봅니다."
meta_keywords: "git revert, 커밋 되돌리기, git, devops, Linux Journey"
---

이미 공유한 변경도 취소할 수 있습니다. `git revert`는 원래 변경을 되돌리는 내용을 새 커밋으로 기록합니다. 이력에는 처음에 무엇을 바꿨는지와 그 변경을 취소한 기록이 모두 남습니다.

## 되돌릴 변경 찾기

실습 저장소의 `main`에는 홈페이지와 상태 페이지의 커밋이 들어 있습니다. 짧은 이력을 확인해 어느 항목이 최신인지 알아봅니다. 아래 식별자는 예시입니다.

```text
$ git log --oneline
3ab4501 Add a health page
a12c345 Set the homepage heading
```

`HEAD`는 현재 체크아웃한 커밋을 가리킵니다. 이 커밋이 되돌리려는 변경인지 확인하세요. 계속하기 전에 `git status`로 작업 트리에 변경이 남아 있지 않은지도 확인합니다.

:::single-choice{#git-revert-command-newest-commit} 이 예시에서 HEAD를 되돌리면 어느 변경이 취소되나요?

::option[앞서 홈페이지 제목을 바꾼 변경입니다.]{#git-revert-command-newest-commit-b explanation="제목을 바꾼 것은 한 단계 이전 커밋입니다."}
::option[두 변경이 한 번에 취소됩니다.]{#git-revert-command-newest-commit-c explanation="여기서 HEAD는 커밋 하나를 가리키며, 해당 커밋에만 되돌리기가 적용됩니다."}
::option[상태 페이지를 추가한 변경입니다.]{#git-revert-command-newest-commit-a .correct explanation="HEAD는 이 브랜치에 표시된 가장 최근 커밋을 가리킵니다."}
:::

## 되돌리기 기록하기

작업 트리에 남은 변경이 없는 실습 저장소에서 상태 페이지 커밋을 되돌립니다. 이 작업은 작업 트리의 파일을 바꾸고 커밋을 만듭니다. `--no-edit`을 사용하면 Git이 제안한 되돌리기 메시지를 그대로 쓸 수 있습니다.

```bash
$ git revert --no-edit HEAD
```

원래 커밋이 상태 페이지 파일을 추가했으므로, 이 예에서 되돌리면 그 파일이 삭제됩니다. 이후 작업에서 같은 줄을 바꿨다면 Git이 멈추고 충돌을 해결하라고 할 수 있습니다. 계속하기 전에 저장소 상태를 확인하세요.

:::single-choice{#git-revert-command-undo-effect} 예시에서 되돌리기가 성공하면 프로젝트 파일은 어떻게 바뀌나요?

::option[홈페이지 파일이 상태 페이지와 함께 삭제됩니다.]{#git-revert-command-undo-effect-a explanation="앞서 홈페이지를 바꾼 커밋은 그대로 적용됩니다."}
::option[상태 페이지 파일이 사라집니다.]{#git-revert-command-undo-effect-b .correct explanation="되돌리기는 선택한 커밋이 추가한 파일을 제거합니다."}
::option[상태 페이지가 한 번 더 추가됩니다.]{#git-revert-command-undo-effect-c explanation="되돌리기는 원래 변경을 반대로 적용합니다."}
:::

![새 되돌리기 커밋과 원래 상태 페이지 커밋을 보여 주는 Git 이력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-revert-command/recorded-undo.png)

## 되돌린 뒤 이력 확인하기

`git log --oneline`을 다시 실행합니다. 원래 상태 페이지 커밋 위에 새 되돌리기 커밋이 나타납니다. `git status --short`로 남은 로컬 변경을 확인합니다. 새 커밋도 다른 변경과 같은 절차로 검토하고 공유할 수 있습니다.

:::single-choice{#git-revert-command-history-after-revert} 새 되돌리기 항목 아래에 여전히 남아 있어야 하는 것은 무엇인가요?

::option[원래 상태 페이지를 추가한 커밋입니다.]{#git-revert-command-history-after-revert-c .correct explanation="두 커밋이 원래 변경과 그 변경을 취소한 작업을 함께 기록합니다."}
::option[홈페이지 제목을 처음 바꾼 커밋만 남습니다.]{#git-revert-command-history-after-revert-a explanation="원래 상태 페이지 커밋도 이력에 남아 있습니다."}
::option[어떤 커밋도 남지 않습니다.]{#git-revert-command-history-after-revert-b explanation="되돌리기는 기존 브랜치 이력에 커밋을 추가합니다."}
:::

## 관련 없는 변경은 유지하기

이력에 별개의 변경이 세 가지 있다고 가정해 봅시다. 상태 파일을 먼저 추가한 뒤 홈페이지 오타를 고쳤고, 두 변경은 이미 공유했습니다. 상태 파일을 추가한 커밋만 골라 되돌리면 오타 수정은 유지하면서 파일을 없앨 수 있습니다. 커밋을 선택하기 전에 이력과 영향을 받는 파일을 읽으세요.

:::single-choice{#git-revert-command-final-application} 남기려던 작업이 유지됐다는 것을 어떻게 확인하나요?

::option[상태 파일을 추가한 커밋이 이력에서 사라졌습니다.]{#git-revert-command-final-application-b explanation="되돌려도 원래 항목은 이력에 남습니다."}
::option[홈페이지의 오타 수정도 사라졌습니다.]{#git-revert-command-final-application-c explanation="오타 수정은 별개 변경이므로 남아 있어야 합니다."}
::option[상태 파일은 사라졌고 홈페이지의 수정은 그대로이며 이력에 되돌리기가 표시됩니다.]{#git-revert-command-final-application-a .correct explanation="선택한 변경을 되돌렸는지, 별개 변경이 남았는지, 이력이 추가됐는지 모두 확인했습니다."}
:::

## 요약

이제 원래 변경과 취소 기록을 모두 남기면서 커밋한 변경을 되돌릴 수 있습니다.

1. 되돌릴 커밋을 정확히 찾습니다.
2. 작업 트리에 남은 변경이 없는 상태에서 되돌립니다.
3. 이력에 원래 커밋과 되돌리기 커밋이 모두 있는지 확인합니다.
