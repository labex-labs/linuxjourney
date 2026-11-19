---
lesson_id: "ci-workflow-triggers"
course_id: "continuous-integration"
lang: "ko"
order_index: 2
title: "워크플로 트리거"
description: "이벤트와 브랜치 필터를 읽고 GitHub Actions 워크플로가 언제 실행되는지 판단하는 방법을 알아봅니다."
meta_title: "워크플로 트리거 - 지속적 통합"
meta_description: "이벤트와 브랜치 필터를 읽고 GitHub Actions 워크플로가 언제 실행되는지 판단하는 방법을 알아봅니다."
meta_keywords: "워크플로 트리거, 브랜치 필터, 지속적 통합, DevOps, Linux Journey"
---

워크플로는 특정 일이 발생하면 실행됩니다. GitHub Actions에서는 `on` 섹션에 실행을 시작할 **이벤트**를 적습니다. 브랜치로 푸시하거나 풀 리퀘스트를 변경하는 등 GitHub가 지원하는 작업이 이벤트가 될 수 있습니다.

## 푸시 조건 읽기

워크플로의 이 부분을 살펴봅시다. YAML에서는 들여쓰기를 보면 `branches`가 `push`에 속하는 설정인지 알 수 있습니다.

```yaml
on:
  push:
    branches:
      - main
```

워크플로가 활성화되어 있고 다른 필수 조건도 충족하면 `main` 브랜치에 커밋을 푸시할 때 실행됩니다. 로컬 터미널에서 커밋을 만드는 것만으로는 변경이 GitHub에 전달되지 않습니다. 이 설정은 푸시가 발생할 때 반응합니다.

:::single-choice{#ci-workflow-triggers-push-filter} 이 푸시 트리거에 맞는 작업은 무엇인가요?

::option[main에서 로컬 커밋을 만듭니다.]{#ci-workflow-triggers-push-filter-a explanation="이 트리거는 GitHub에 있는 저장소의 이벤트를 기다립니다."}
::option[draft라는 브랜치에 커밋을 푸시합니다.]{#ci-workflow-triggers-push-filter-b explanation="브랜치 필터가 선택하는 브랜치는 main입니다."}
::option[main에 커밋을 푸시합니다.]{#ci-workflow-triggers-push-filter-c .correct explanation="이 작업은 push 이벤트와 브랜치 필터를 모두 충족합니다."}
:::

## 풀 리퀘스트 조건 읽기

별도의 이벤트로 병합 전에 제안된 변경을 검사할 수 있습니다. 여기서 브랜치 필터는 풀 리퀘스트의 대상 브랜치에 적용됩니다.

```yaml
on:
  pull_request:
    branches:
      - main
```

`health-page`에서 `main`으로 변경을 반영하는 제안은 이 필터에 맞습니다. 기본 활동 유형에서는 풀 리퀘스트를 열거나 원본 브랜치에 새 커밋을 푸시할 때 워크플로가 시작될 수 있습니다.

:::single-choice{#ci-workflow-triggers-pr-target} 풀 리퀘스트가 notes의 변경을 main에 반영하려고 합니다. 이 브랜치 필터에 적용되는 이름은 무엇인가요?

::option[원본 브랜치인 notes입니다.]{#ci-workflow-triggers-pr-target-b explanation="notes에는 제안하는 변경이 들어 있습니다."}
::option[대상 브랜치인 main입니다.]{#ci-workflow-triggers-pr-target-a .correct explanation="풀 리퀘스트의 브랜치 필터는 변경을 받을 대상, 즉 base 브랜치에 적용됩니다."}
::option[제안에서 수정한 파일 이름입니다.]{#ci-workflow-triggers-pr-target-c explanation="이 설정은 브랜치 이름으로 필터링합니다."}
:::

## 여러 트리거 읽기

한 파일에서 동일한 `on` 키 아래 두 이벤트를 모두 적을 수 있습니다. 풀 리퀘스트로 시작된 실행은 제안된 병합을 검사할 수 있습니다. 병합으로 `main`이 갱신되면 푸시로 시작된 실행이 그 브랜치의 새 상태를 검사할 수 있습니다. 각 결과는 해당 실행에 표시된 이벤트와 리비전에 대응합니다.

:::single-choice{#ci-workflow-triggers-after-merge} 워크플로에 위의 두 트리거가 있습니다. 병합으로 main이 갱신되었습니다. 이 업데이트에 맞는 이벤트는 무엇인가요?

::option[main으로의 푸시입니다.]{#ci-workflow-triggers-after-merge-b .correct explanation="변경을 받은 브랜치가 갱신되었으며 푸시 필터에 맞습니다."}
::option[새 브랜치에서 풀 리퀘스트를 여는 작업입니다.]{#ci-workflow-triggers-after-merge-a explanation="이 예시에서 일어난 일은 병합 후 main 업데이트입니다."}
::option[원격 저장소를 갱신하지 않는 로컬 커밋입니다.]{#ci-workflow-triggers-after-merge-c explanation="이 예시에서는 GitHub의 main이 이미 바뀌었습니다."}
:::

## 요약

이제 저장소 이벤트가 어느 워크플로 트리거에 해당하는지 판단할 수 있습니다.

1. 푸시 이벤트와 그 브랜치 필터를 읽습니다.
2. 풀 리퀘스트의 필터가 적용되는 대상 브랜치를 찾습니다.
3. 워크플로 결과를 실행을 일으킨 이벤트와 연결합니다.
