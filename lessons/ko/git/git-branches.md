---
lesson_id: "git-branches"
course_id: "git"
lang: "ko"
order_index: 5
title: "브랜치"
description: "Git 브랜치로 작업을 나누고, 병합으로 변경을 main에 가져오는 방법을 알아봅니다."
meta_title: "브랜치 - Git"
meta_description: "Git 브랜치로 작업을 나누고, 병합으로 변경을 main에 가져오는 방법을 알아봅니다."
meta_keywords: "브랜치, 병합, git, devops, Linux Journey"
---

**브랜치**는 커밋을 가리키는 이름입니다. 현재 브랜치에서 새 커밋을 만들면 브랜치 이름이 새 커밋을 가리키게 됩니다. 다른 브랜치는 갱신하기 전까지 기존 커밋을 가리킵니다.

## 별도 브랜치에서 작업 시작하기

실습 저장소의 `main`에서 `health-page`라는 브랜치를 만들고 그 브랜치로 전환합니다. `git switch`의 `-c` 옵션은 브랜치를 새로 만들라는 뜻입니다.

```bash
$ git switch -c health-page
```

처음에는 두 이름이 같은 커밋을 가리킵니다. 다음 커밋에서 어느 브랜치가 앞으로 이동할지 확인하려면 `git branch --show-current`를 사용합니다.

:::single-choice{#git-branches-start-pointer} git switch -c health-page를 실행한 직후, 새 브랜치는 어떤 커밋을 가리키나요?

::option[이 명령이 만든 빈 커밋입니다.]{#git-branches-start-pointer-a explanation="이 명령은 기존 커밋을 가리키는 이름을 만듭니다."}
::option[다른 사람의 저장소에 있는 커밋입니다.]{#git-branches-start-pointer-c explanation="이 명령은 현재 저장소에 로컬 브랜치를 만듭니다."}
::option[새 브랜치를 만들 때 출발점이 된 커밋입니다.]{#git-branches-start-pointer-b .correct explanation="처음에는 두 이름이 같은 시점의 커밋을 가리킵니다."}
:::

## 브랜치에 변경 저장하기

`health-page`로 전환한 상태에서 한 줄짜리 상태 파일을 추가하고 커밋합니다.

```bash
$ printf '%s\n' ready > health.txt
$ git add health.txt
$ git commit -m "Add a health page"
```

홈페이지 커밋을 A, 상태 페이지 커밋을 B라고 하겠습니다.

```text
A (main) --- B (health-page)
```

`health-page`만 B로 이동했습니다. 작업 트리에 남은 변경이 없는 상태에서 `main`으로 돌아가면 파일도 A의 상태로 돌아갑니다.

:::single-choice{#git-branches-branch-snapshot} 병합하기 전에 상태 페이지 커밋을 포함하는 브랜치는 무엇인가요?

::option[같은 저장소에 있으므로 두 브랜치 모두 포함합니다.]{#git-branches-branch-snapshot-a explanation="한 저장소에서도 브랜치마다 다른 커밋을 가리킬 수 있습니다."}
::option[health-page만 포함합니다.]{#git-branches-branch-snapshot-c .correct explanation="커밋 B를 만들 때 사용하던 브랜치입니다."}
::option[처음 작업한 브랜치인 main만 포함합니다.]{#git-branches-branch-snapshot-b explanation="health-page에서 커밋해도 main의 위치는 바뀌지 않습니다."}
:::

## main으로 병합하기

변경을 받을 브랜치로 전환한 뒤 병합할 원본 브랜치를 지정합니다.

```bash
$ git switch main
$ git merge health-page
```

이 예에서 `main`은 A 이후 별도로 변경된 내용이 없습니다. Git이 main을 곧바로 B로 옮길 수 있는데, 이를 **패스트 포워드**라고 합니다. 두 브랜치에 각각 새 커밋이 있으면 변경을 합쳐야 할 수도 있습니다. 결과를 읽고 병합이 완료됐는지 확인하세요.

:::single-choice{#git-branches-merge-direction} health-page의 변경을 main에 반영하려면 어디에서 병합하나요?

::option[main에서 health-page를 원본으로 지정합니다.]{#git-branches-merge-direction-a .correct explanation="병합 결과는 현재 브랜치에 반영됩니다."}
::option[health-page에서 main을 원본으로 지정합니다.]{#git-branches-merge-direction-b explanation="그러면 health-page가 갱신됩니다."}
::option[두 브랜치와 무관한 새 브랜치에서 실행합니다.]{#git-branches-merge-direction-c explanation="main은 변경을 받기 전까지 기존 위치에 머뭅니다."}
:::

## 요약

이제 로컬 브랜치에서 작업한 변경이 main으로 들어가는 과정을 따라갈 수 있습니다.

1. 현재 커밋을 출발점으로 브랜치를 만듭니다.
2. 원하는 브랜치에 변경을 저장합니다.
3. 변경을 받아야 할 브랜치로 병합합니다.
