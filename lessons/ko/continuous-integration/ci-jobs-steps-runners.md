---
lesson_id: "ci-jobs-steps-runners"
course_id: "continuous-integration"
lang: "ko"
order_index: 3
title: "작업, 단계, 러너"
description: "짧은 GitHub Actions 파일에서 작업, 단계, 러너를 찾는 방법을 알아봅니다."
meta_title: "작업, 단계, 러너 - 지속적 통합"
meta_description: "짧은 GitHub Actions 파일에서 작업, 단계, 러너를 찾는 방법을 알아봅니다."
meta_keywords: "작업, 단계, 러너, GitHub Actions, 지속적 통합, DevOps, Linux Journey"
---

워크플로는 자동으로 진행되는 전체 과정입니다. **작업**은 **러너**에 맡기는 일의 묶음이며, 러너는 그 일을 실행하는 컴퓨터나 환경입니다. **단계**는 작업 안의 개별 동작입니다.

## 짧은 워크플로 읽기

이 예시는 GitHub가 호스팅하는 Ubuntu 러너에서 작업 하나를 실행합니다. 이런 워크플로를 GitHub 저장소의 `.github/workflows/`에 저장합니다.

```yaml
name: Page check
on: push
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - name: Get the repository
        uses: actions/checkout@v6
      - name: Find the heading
        run: grep -q '<h1>Welcome</h1>' index.html
```

작업 ID는 `check`입니다. `runs-on` 필드는 실행 환경을 고릅니다. `uses`는 재사용 가능한 액션을 호출하며, 여기서는 저장소 파일을 사용할 수 있게 합니다. `run`은 러너에서 명령을 실행합니다.

:::single-choice{#ci-jobs-steps-runners-job-fields} check 작업이 어디에서 실행될지 고르는 필드는 무엇인가요?

::option[runs-on입니다.]{#ci-jobs-steps-runners-job-fields-a .correct explanation="작업에서 쓸 러너 유형을 지정합니다."}
::option[uses입니다.]{#ci-jobs-steps-runners-job-fields-b explanation="이 단계는 체크아웃 액션을 호출합니다."}
::option[name입니다.]{#ci-jobs-steps-runners-job-fields-c explanation="워크플로의 이름을 정하는 필드입니다."}
:::

## 단계를 순서대로 살펴보기

한 작업의 단계는 기본적으로 기재된 순서대로 실행됩니다. 검사에서 저장소 파일을 읽으므로 먼저 체크아웃합니다. 같은 작업 안에서는 앞 단계에서 만든 파일을 뒤 단계에서 사용할 수 있습니다.

:::single-choice{#ci-jobs-steps-runners-step-order} 새 러너에서 체크아웃을 grep 뒤로 옮기면 grep 단계에 무엇이 없나요?

::option[작업의 이름입니다.]{#ci-jobs-steps-runners-step-order-a explanation="워크플로가 이미 작업을 선택했습니다."}
::option[Ubuntu 러너 자체입니다.]{#ci-jobs-steps-runners-step-order-c explanation="단계가 실행되기 전에 러너를 선택합니다."}
::option[읽어야 할 프로젝트 파일입니다.]{#ci-jobs-steps-runners-step-order-b .correct explanation="체크아웃을 앞에서 실행해야 검사에 필요한 저장소 파일을 얻을 수 있습니다."}
:::

## 작업별 실행 환경 구분하기

서로 다른 작업은 동시에 실행될 수 있습니다. GitHub가 호스팅하는 환경에서는 작업마다 별도 러너가 배정됩니다. 따라서 한 작업에서 만든 파일을 다른 작업에서 쓰려면 워크플로에서 전송해야 합니다. 한 작업이 다른 작업의 성공을 기다려야 한다면 `needs`로 의존 관계를 선언하고, 파일을 넘겨야 할 때는 아티팩트를 사용하세요.

:::single-choice{#ci-jobs-steps-runners-separate-jobs} 빌드 작업이 site.tar.gz를 만듭니다. 다음 작업은 다른 호스팅 러너에서 실행됩니다. 파일을 어떻게 넘겨야 하나요?

::option[같은 작업 디렉터리에 파일이 남아 있다고 가정합니다.]{#ci-jobs-steps-runners-separate-jobs-a explanation="별도 호스팅 러너는 자체 파일 시스템으로 시작합니다."}
::option[파일을 아티팩트로 전송합니다.]{#ci-jobs-steps-runners-separate-jobs-c .correct explanation="한 작업에서 업로드하고 다른 작업에서 다운로드하도록 워크플로를 구성할 수 있습니다."}
::option[두 번째 작업이 빌드를 기다리도록 needs를 설정합니다.]{#ci-jobs-steps-runners-separate-jobs-b explanation="needs는 순서를 정합니다. 빌드한 파일은 러너 사이에 따로 전송해야 합니다."}
:::

GitHub 저장소에 워크플로를 작성하고 실행하려면 [초보자를 위한 GitHub Actions](https://labex.io/courses/github-actions-for-beginners)를 실습해 보세요. 실습 과정에는 GitHub 계정이 필요합니다.

## 요약

이제 CI 워크플로의 주요 부분을 읽을 수 있습니다.

1. 작업과 해당 작업을 실행하는 러너를 찾습니다.
2. 재사용 가능한 액션과 셸 명령을 실행하는 단계를 구분합니다.
3. 작업 사이에 의존 관계나 파일 전송이 필요한 경우를 파악합니다.
