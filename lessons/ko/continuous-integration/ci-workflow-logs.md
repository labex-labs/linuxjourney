---
lesson_id: "ci-workflow-logs"
course_id: "continuous-integration"
lang: "ko"
order_index: 5
title: "워크플로 로그"
description: "워크플로에서 실패한 단계를 찾고 조사에 도움이 되는 첫 메시지를 읽는 방법을 알아봅니다."
meta_title: "워크플로 로그 - 지속적 통합"
meta_description: "워크플로에서 실패한 단계를 찾고 조사에 도움이 되는 첫 메시지를 읽는 방법을 알아봅니다."
meta_keywords: "워크플로 로그, 오류 조사, 지속적 통합, DevOps, Linux Journey"
---

워크플로 결과에는 전체 상태가 표시됩니다. 실패 이유를 알아보려면 실패한 작업을 펼쳐 단계를 순서대로 읽으세요. 앞 단계가 성공적으로 끝나지 않아 뒤 단계가 건너뛰어질 수 있습니다.

## 첫 실패 찾기

이 모의 실행에는 페이지 검사 작업의 각 단계 상태가 표시됩니다.

```text
Prepare: passed
Build page: failed
Check heading: skipped
Package site: skipped
```

`Build page`부터 살펴봅니다. 건너뛴 검사는 페이지에 대한 결과를 내지 않습니다. 실패 원인을 고친 뒤에는 새 실행에서 뒤 단계의 결과를 확인하세요.

:::single-choice{#ci-workflow-logs-first-failure} 어느 단계의 출력을 먼저 읽어야 하나요?

::option[마지막에 나오는 Package site입니다.]{#ci-workflow-logs-first-failure-a explanation="이 실행에서는 패키지를 만드는 명령을 건너뛰었습니다."}
::option[페이지 검사 워크플로이므로 Check heading입니다.]{#ci-workflow-logs-first-failure-c explanation="상태를 보면 제목 검사가 실행되지 않았습니다."}
::option[다른 단계가 시작되기 전에 실패한 Build page입니다.]{#ci-workflow-logs-first-failure-b .correct explanation="이 단계의 로그를 보면 뒤 단계가 생략된 이유를 알 수 있습니다."}
:::

![빌드가 실패하고 이후 단계가 생략된 모의 CI 실행](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/continuous-integration/ci-workflow-logs/skipped-steps.png)

## 오류 메시지 따라가기

실패한 단계에는 다음 줄이 표시됩니다.

```text
Run cp index.html dist/index.html
cp: cannot create regular file 'dist/index.html': No such file or directory
Process completed with exit code 1.
```

메시지에 복사 대상 경로가 나옵니다. 상위 디렉터리 `dist`가 없으면 복사 명령은 그 안에 파일을 만들 수 없습니다. 복사하기 전에 앞선 명령으로 디렉터리를 만들었는지 확인하세요. 종료 코드 1은 명령이 실패했다는 뜻이고, 메시지는 어디를 살펴볼지 알려 줍니다.

:::single-choice{#ci-workflow-logs-actionable-log} dist가 없다면 어떤 변경으로 보고된 문제를 해결할 수 있나요?

::option[grep이 검사하는 제목을 바꿉니다.]{#ci-workflow-logs-actionable-log-b explanation="제목 검사를 실행하지 않았으므로 텍스트가 잘못됐다는 근거는 없습니다."}
::option[파일을 복사하기 전에 dist를 만듭니다.]{#ci-workflow-logs-actionable-log-a .correct explanation="대상 파일을 만들려면 상위 디렉터리가 필요합니다."}
::option[생략된 단계에서 아티팩트를 다운로드합니다.]{#ci-workflow-logs-actionable-log-c explanation="여기서는 패키지를 만드는 단계에서 아티팩트가 생성되지 않았습니다."}
:::

## 새 실행 확인하기

빌드를 수정한 다음 새 실행의 리비전과 각 단계 상태를 비교합니다. 복사에 성공하면 출력 파일이 생성됐다는 사실을 알 수 있습니다. 전체 과정이 성공했다고 판단하기 전에 테스트와 패키지 생성 결과까지 읽으세요. 문제를 보고할 때는 도움이 되는 첫 오류와 단계 이름을 함께 기록합니다.

:::single-choice{#ci-workflow-logs-rerun-evidence} 새 실행에서 Build page는 통과했지만 Check heading은 실패했습니다. 무엇이 바뀌었나요?

::option[빌드는 성공했고 이제 조사할 제목 검사 결과가 생겼습니다.]{#ci-workflow-logs-rerun-evidence-c .correct explanation="남은 첫 실패 지점이 테스트 단계로 옮겨 갔습니다."}
::option[이전 빌드가 실패했으므로 새 실행은 의미가 없습니다.]{#ci-workflow-logs-rerun-evidence-a explanation="각 실행은 해당 리비전의 결과를 보여 줍니다."}
::option[빌드가 통과했으므로 패키지 생성도 통과했을 것입니다.]{#ci-workflow-logs-rerun-evidence-b explanation="뒤 단계도 실패하거나 생략될 수 있습니다."}
:::

## 요약

이제 앞뒤 단계의 흐름을 보며 워크플로 실패를 해석할 수 있습니다.

1. 실행된 단계 중 처음으로 실패한 단계를 찾습니다.
2. 로그를 읽고 무엇을 조사할지 파악합니다.
3. 수정 후 새 리비전과 뒤 단계의 상태를 확인합니다.
