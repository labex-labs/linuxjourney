---
lesson_id: "git-pull-requests"
course_id: "git"
lang: "ko"
order_index: 7
title: "풀 리퀘스트"
description: "풀 리퀘스트를 읽고 코드 검토와 자동 검사가 어떤 변경을 대상으로 하는지 파악하는 방법을 알아봅니다."
meta_title: "풀 리퀘스트 - Git"
meta_description: "풀 리퀘스트를 읽고 코드 검토와 자동 검사가 어떤 변경을 대상으로 하는지 파악하는 방법을 알아봅니다."
meta_keywords: "풀 리퀘스트, 코드 검토, git, devops, Linux Journey"
---

**풀 리퀘스트**는 줄여서 PR이라고도 합니다. 한 브랜치의 변경을 다른 브랜치에 반영하자는 제안입니다. Git은 커밋과 브랜치를 관리합니다. 호스팅 서비스는 변경을 검토하고 논의하며 검사 결과를 볼 수 있는 화면을 제공합니다.

## 원본과 대상 브랜치 확인하기

팀원이 사이트에 상태 페이지를 추가하자고 제안했습니다. 검토 화면에는 `health-page → main`이라고 나옵니다. **head**라고도 하는 원본 브랜치에는 제안한 변경이 들어 있습니다. **base**라고도 하는 대상 브랜치는 그 변경을 받아들일 브랜치입니다.

```text
Source: health-page at 3ab4501
Target: main
Changed file: health.txt
```

이 단계의 검토 화면에는 제안된 내용이 표시됩니다. PR을 병합하면 대상 브랜치에 변경이 반영됩니다.

:::single-choice{#git-pull-requests-pr-direction} 이 PR을 병합하면 상태 페이지가 어느 브랜치에 들어가나요?

::option[커밋 ID와 같은 이름의 브랜치입니다.]{#git-pull-requests-pr-direction-a explanation="커밋 ID는 저장된 한 상태를 식별합니다. 대상 브랜치에는 별도의 이름이 있습니다."}
::option[main입니다.]{#git-pull-requests-pr-direction-b .correct explanation="대상이 main이므로 검토한 변경이 이 브랜치에 반영됩니다."}
::option[health-page입니다.]{#git-pull-requests-pr-direction-c explanation="health-page는 변경을 제공하는 원본 브랜치입니다."}
:::

## 변경 내용 확인하기

변경된 파일 목록을 열고 PR의 대상 브랜치를 기준으로 차이를 읽습니다. `health.txt`에 한 줄이 추가됐다면 간단한 상태 페이지를 만들겠다는 제안에 맞습니다. `index.html`도 변경됐다면 그 수정이 같은 제안에 들어갈 내용인지 살펴보세요. PR에 실제로 표시된 파일을 직접 확인합니다.

:::single-choice{#git-pull-requests-unexpected-file} ‘상태 페이지 추가’라는 PR이 홈페이지도 수정합니다. 정확히 무엇을 고쳤는지 어디에서 확인하나요?

::option[변경된 파일의 차이에서 확인합니다.]{#git-pull-requests-unexpected-file-a .correct explanation="차이를 보면 이 제안이 어떤 줄을 바꾸는지 알 수 있습니다."}
::option[PR 제목만 봅니다.]{#git-pull-requests-unexpected-file-b explanation="제목은 목적을 요약하므로 세부 변경 사항이 빠질 수 있습니다."}
::option[브랜치 이름에서 확인합니다.]{#git-pull-requests-unexpected-file-c explanation="브랜치 이름은 작업을 구분할 뿐, 모든 변경을 설명하지는 않습니다."}
:::

## 자동 검사 결과 읽기

호스팅 서비스는 PR이 바뀔 때 테스트를 실행할 수 있습니다. 검사 결과가 어느 커밋이나 리비전을 대상으로 하는지 확인합니다. 테스트를 통과한 뒤 새 커밋을 푸시했다면, 바뀐 리비전에서 필요한 검사를 실행했는지도 확인합니다. 통과 결과는 실제로 실행한 검사에 해당합니다.

:::single-choice{#git-pull-requests-changed-revision} 3ab4501에서 테스트가 통과했습니다. 지금 PR은 78ac900을 가리킵니다. 검사 결과를 근거로 삼기 전에 무엇을 확인해야 하나요?

::option[이전 커밋의 메시지가 잘 작성되었는지 확인합니다.]{#git-pull-requests-changed-revision-a explanation="메시지로는 새 커밋까지 테스트했는지 알 수 없습니다."}
::option[PR 제목이 여전히 같은지 확인합니다.]{#git-pull-requests-changed-revision-b explanation="코드가 바뀌어도 제목은 그대로일 수 있습니다."}
::option[바뀐 리비전에서도 검사를 실행했는지 확인합니다.]{#git-pull-requests-changed-revision-c .correct explanation="이전 결과는 다른 리비전을 대상으로 했습니다."}
:::

## 요약

이제 풀 리퀘스트의 제안 내용을 읽고 병합을 판단할 근거를 확인할 수 있습니다.

1. 원본 브랜치와 대상 브랜치를 찾습니다.
2. 변경된 파일 목록에서 제안한 수정을 확인합니다.
3. 자동 검사 결과가 어느 리비전에 해당하는지 확인합니다.
