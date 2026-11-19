---
lesson_id: "git-remotes"
course_id: "git"
lang: "ko"
order_index: 6
title: "원격 저장소"
description: "Git에서 다른 저장소에 연결하는 방법과 가져오기와 푸시의 차이를 알아봅니다."
meta_title: "원격 저장소 - Git"
meta_description: "Git에서 다른 저장소에 연결하는 방법과 가져오기와 푸시의 차이를 알아봅니다."
meta_keywords: "원격 저장소, 가져오기, 푸시, git, devops, Linux Journey"
---

Git에서 **원격**은 로컬 저장소가 다른 저장소에 접근할 때 사용하는 이름이 붙은 주소입니다. 연결할 저장소는 호스팅 서비스에 있을 수도 있고, 같은 컴퓨터의 디렉터리에 있을 수도 있습니다. 이 예에서는 별도의 로컬 디렉터리를 사용하므로 호스팅 계정이 없어도 됩니다.

## 주소 추가하기

실습 저장소에서 별도의 **베어 저장소**를 만듭니다. 베어 저장소에는 이력과 참조가 있지만 프로젝트 작업 트리는 없습니다. 작업 공간에서 보낸 커밋을 받을 수 있습니다. 실습을 처음부터 하려면 아직 사용하지 않은 `journey-remote.git` 디렉터리가 필요합니다.

```bash
$ git init --bare --initial-branch=main ../journey-remote.git
$ git remote add origin ../journey-remote.git
$ git remote -v
```

원격 이름으로는 흔히 `origin`을 사용합니다. 원격 목록을 확인하면 그 이름이 어떤 주소를 가리키는지 알 수 있습니다.

:::single-choice{#git-remotes-add-address} git remote add를 실행하니 목록에 origin이 보입니다. Git은 무엇을 했나요?

::option[다른 저장소를 가리키는 이름을 등록했습니다.]{#git-remotes-add-address-b .correct explanation="이후에는 명령에서 해당 주소를 origin으로 지정할 수 있습니다."}
::option[로컬 커밋을 모두 업로드했습니다.]{#git-remotes-add-address-a explanation="원격을 추가하면 주소가 등록됩니다. 커밋을 보내는 데는 푸시를 사용합니다."}
::option[프로젝트 안에 다른 작업 트리를 복제했습니다.]{#git-remotes-add-address-c explanation="기존 작업 트리는 원래 위치에 그대로 있습니다."}
:::

## 브랜치 보내기

`git push`로 로컬 커밋을 보내고 원격 저장소의 브랜치 갱신을 요청합니다. `-u` 옵션을 주면 원격 브랜치를 업스트림으로 기록합니다. 이후 명령에서 Git이 로컬 브랜치와 연결해 사용하는 브랜치입니다.

```bash
$ git push -u origin main
```

여기서는 별도로 만든 실습용 디렉터리에만 푸시합니다. 공유 원격 저장소는 권한을 요구하거나 갱신을 거부할 수 있으므로, 출력에서 푸시가 성공했는지 확인하세요.

:::single-choice{#git-remotes-push-direction} 로컬 main의 새 커밋을 이 원격 저장소로 보내는 명령은 무엇인가요?

::option[git fetch origin]{#git-remotes-push-direction-b explanation="가져오기는 원격 저장소의 정보를 로컬 저장소로 받습니다."}
::option[git remote -v]{#git-remotes-push-direction-c explanation="이 명령은 origin에 연결된 주소를 보여 줍니다."}
::option[git push origin main]{#git-remotes-push-direction-a .correct explanation="푸시는 원격에 필요한 커밋을 보내고 브랜치 갱신을 요청합니다."}
:::

## 업데이트 받아 오기

`git fetch origin`으로 원격 이력에 대한 로컬 정보를 갱신합니다. Git은 `origin/main` 같은 **원격 추적 브랜치**에 마지막으로 확인한 상태를 기록합니다. `git log --oneline origin/main`으로 그 이력을 볼 수 있습니다. 가져오기만 하면 작업 트리는 현재 체크아웃한 로컬 브랜치에 그대로 남습니다.

```bash
$ git fetch origin
$ git log --oneline origin/main
```

:::single-choice{#git-remotes-after-fetch} 가져온 뒤 origin/main은 이동했지만 로컬 main은 그대로입니다. 무슨 일이 있었나요?

::option[가져오기 때문에 편집하던 파일이 바뀌었습니다.]{#git-remotes-after-fetch-a explanation="가져오기는 원격 브랜치에 대해 로컬에 기록된 정보를 갱신합니다."}
::option[Git이 원격의 변경을 확인했습니다. 로컬 브랜치에 반영하려면 별도의 작업이 필요합니다.]{#git-remotes-after-fetch-c .correct explanation="origin/main이 이동해도 로컬 브랜치는 기존 위치에 남을 수 있습니다."}
::option[가져오는 도중 푸시가 원격을 갱신했습니다.]{#git-remotes-after-fetch-b explanation="가져오기는 원격에서 정보를 받는 작업입니다."}
:::

## 요약

이제 Git 명령이 어느 저장소에 영향을 주는지 구분할 수 있습니다.

1. 원격 주소를 등록하고 확인합니다.
2. 브랜치를 푸시하고 업스트림을 확인합니다.
3. 체크아웃한 파일을 그대로 두고 원격의 새 이력을 가져옵니다.
