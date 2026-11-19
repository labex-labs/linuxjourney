---
lesson_id: "git-repositories"
course_id: "git"
lang: "ko"
order_index: 1
title: "저장소"
description: "Git 저장소에 무엇이 들어 있는지 알아보고, 작은 웹사이트를 위한 빈 저장소를 만듭니다."
meta_title: "저장소 - Git"
meta_description: "Git 저장소에 무엇이 들어 있는지 알아보고, 작은 웹사이트를 위한 빈 저장소를 만듭니다."
meta_keywords: "저장소, git, devops, Linux Journey"
---

웹사이트는 몇 개의 파일에서 시작합니다. Git을 사용하면 특정 시점에 그 파일들이 어떤 상태였는지 기록할 수 있습니다. 프로젝트 파일과 그 이력이 모여 로컬 Git 작업 환경을 이룹니다.

## 저장소 만들기

새 폴더를 만들 수 있는 실습용 디렉터리에서 시작하세요. 다음 명령을 한 번 실행합니다. 달러 기호는 셸 프롬프트를 나타냅니다.

```bash
$ mkdir journey-git
$ cd journey-git
$ git init --initial-branch=main
```

새 폴더는 프로젝트 파일을 편집하는 **작업 트리**입니다. Git은 이력과 설정을 저장하기 위해 그 안에 숨김 디렉터리인 `.git`을 만듭니다. 새 저장소에는 아직 저장된 변경 사항이 없습니다. 첫 작업 흐름에는 `main`이라는 이름을 붙입니다.

:::single-choice{#git-repositories-empty-history} index.html이 이미 있는 디렉터리에서 저장소를 초기화했습니다. 이 파일은 이력에 어떻게 기록되나요?

::option[Git이 파일을 즉시 첫 번째 커밋으로 기록합니다.]{#git-repositories-empty-history-b explanation="초기화만으로는 프로젝트 파일이 기록되지 않습니다."}
::option[나중에 커밋하면 파일을 기록할 수 있습니다.]{#git-repositories-empty-history-a .correct explanation="초기화는 저장소를 준비합니다. 그 시점의 상태를 저장하려면 별도로 커밋해야 합니다."}
::option[Git이 파일을 숨김 디렉터리로 옮깁니다.]{#git-repositories-empty-history-c explanation="프로젝트 파일은 편집할 수 있도록 작업 트리에 남습니다."}
:::

![빈 Git 저장소를 초기화하고 실습 폴더를 저장소의 루트로 표시한 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/git/git-repositories/init-and-root.png)

## 작업 트리 찾기

`git rev-parse --show-toplevel`을 사용하면 현재 저장소의 루트 경로가 표시됩니다. 실습 폴더에서 실행하면 `journey-git`으로 끝나는 경로가 나옵니다. 작업 트리 아래의 폴더는 그 안에 별도 저장소가 없는 한 같은 저장소에 속합니다.

```bash
$ git rev-parse --show-toplevel
```

:::single-choice{#git-repositories-find-root} journey-git 안에 있는 images 하위 디렉터리로 이동했습니다. Git은 어느 디렉터리를 최상위로 표시하나요?

::option[journey-git 디렉터리입니다.]{#git-repositories-find-root-b .correct explanation="Git은 현재 위치보다 위에 있는 저장소의 루트를 찾습니다."}
::option[images 하위 디렉터리입니다.]{#git-repositories-find-root-a explanation="셸의 현재 위치가 하위 디렉터리여도 표시되는 경로는 저장소의 최상위입니다."}
::option[숨김 디렉터리인 .git입니다.]{#git-repositories-find-root-c explanation="이 명령은 프로젝트 파일을 두는 작업 트리의 루트를 표시합니다."}
:::

## 기존 이력으로 시작하기

이미 있는 저장소를 복사하려면 `git clone`을 사용합니다. 일반적인 복제는 로컬에 새 작업 트리를 만들고 기존 저장소의 이력도 가져옵니다. 로컬에서 새 프로젝트의 이력을 시작할 때는 `git init`을 사용합니다. 다음 레슨에서도 `journey-git`을 계속 사용합니다.

:::single-choice{#git-repositories-choose-start} 팀원이 저장소 주소를 알려 주었고 그 저장소의 이력이 필요합니다. 먼저 무엇을 해야 하나요?

::option[빈 폴더를 만들고 초기화합니다.]{#git-repositories-choose-start-a explanation="새 저장소에는 팀원의 이력이 없습니다."}
::option[눈에 보이는 웹사이트 파일만 복사합니다.]{#git-repositories-choose-start-b explanation="파일만 복사하면 한 시점의 상태만 얻을 수 있고 저장소 이력은 빠집니다."}
::option[팀원의 저장소를 복제합니다.]{#git-repositories-choose-start-c .correct explanation="복제하면 공유 저장소의 이력을 가져오고 로컬 작업 트리도 만들 수 있습니다."}
:::

## 요약

이제 상황에 맞게 로컬 Git 저장소를 만드는 방법을 고를 수 있습니다.

1. 작업 트리와 Git의 숨김 디렉터리를 구분합니다.
2. 하위 디렉터리에서 저장소의 루트를 찾습니다.
3. 새 이력을 시작할 때는 초기화하고, 기존 이력을 가져올 때는 복제합니다.
