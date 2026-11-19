---
lesson_id: "ci-workflow-permissions"
course_id: "continuous-integration"
lang: "ko"
order_index: 7
title: "워크플로 권한"
description: "일상적인 CI 검사에 필요한 저장소 접근 권한만 부여하는 방법을 알아봅니다."
meta_title: "워크플로 권한 - 지속적 통합"
meta_description: "일상적인 CI 검사에 필요한 저장소 접근 권한만 부여하는 방법을 알아봅니다."
meta_keywords: "워크플로 권한, 읽기 권한, 지속적 통합, DevOps, Linux Journey"
---

CI 작업은 명령을 실행하고 자격 증명을 받을 수 있습니다. **권한**은 그 자격 증명으로 무엇을 읽거나 바꿀 수 있는지 정합니다. 페이지를 검사하기만 하는 작업에는 보통 소스 파일을 읽을 권한이면 충분합니다.

## 검사 작업에 읽기 권한 주기

이 GitHub Actions 설정은 워크플로의 기본 제공 토큰에 저장소 콘텐츠의 읽기 권한만 줍니다.

```yaml
permissions:
  contents: read
```

체크아웃과 로컬 테스트는 저장소를 읽을 수 있습니다. 패키지를 게시하는 작업에는 다른 리소스에서 다른 동작을 수행할 권한이 필요합니다. 게시 권한은 필요한 작업에만 부여하세요.

:::single-choice{#ci-workflow-permissions-choose-permission} 어떤 작업이 페이지를 읽고 grep을 실행합니다. 저장소 콘텐츠에 어떤 권한이 필요한가요?

::option[테스트 결과를 터미널에 쓰므로 쓰기 권한이 필요합니다.]{#ci-workflow-permissions-choose-permission-a explanation="터미널에 결과를 출력하는 데 저장소 콘텐츠를 바꾸는 권한은 필요하지 않습니다."}
::option[읽기 권한이 필요합니다.]{#ci-workflow-permissions-choose-permission-c .correct explanation="이 작업은 콘텐츠를 가져와야 하지만 저장소의 내용을 수정하지는 않습니다."}
::option[소스가 Git 저장소에 있으므로 쓰기 권한이 필요합니다.]{#ci-workflow-permissions-choose-permission-b explanation="설명한 검사에는 소스 파일 읽기만으로 충분합니다."}
:::

## 민감한 값 다루기

비공개 토큰 같은 민감한 값을 **시크릿**이라고 합니다. 승인된 작업에서 그런 값이 필요하다면 플랫폼의 시크릿 저장소를 사용하세요. 일반적인 페이지 설정과 시크릿은 따로 관리합니다. 로컬 예시를 검사하는 일상적인 작업은 게시용 자격 증명 없이 실행할 수 있어야 합니다.

:::single-choice{#ci-workflow-permissions-secret-needed} 접근을 제한한 시크릿 저장소에 넣어야 할 값은 무엇인가요?

::option[패키지 업로드에 쓰는 비공개 자격 증명입니다.]{#ci-workflow-permissions-secret-needed-a .correct explanation="자격 증명으로 다른 시스템에 접근할 수 있습니다."}
::option[테스트에서 사용하는 Welcome이라는 문자열입니다.]{#ci-workflow-permissions-secret-needed-b explanation="공개된 예시 텍스트입니다."}
::option[출력 디렉터리 이름인 dist입니다.]{#ci-workflow-permissions-secret-needed-c explanation="디렉터리 이름은 일반적인 설정입니다."}
:::

## 조사에 도움이 되는 로그 남기기

워크플로 로그는 다른 사람과 공유될 수 있습니다. 시크릿 값을 출력하지 않고 어떤 동작을 실행했고 결과가 어땠는지 기록하세요. 필요한 자격 증명을 얻지 못했거나 접근이 거부되었다고 알릴 수 있습니다. 관리자가 조사할 수 있도록 작업 이름과 리비전을 제공하고, 메시지에는 자격 증명 값을 넣지 않습니다.

:::single-choice{#ci-workflow-permissions-safe-diagnostic} 게시 작업이 인증에 실패했습니다. 자격 증명을 노출하지 않으면서 조사에 도움이 되는 메시지는 무엇인가요?

::option[복사할 수 있도록 자격 증명을 전부 출력합니다.]{#ci-workflow-permissions-safe-diagnostic-a explanation="로그에 접근할 수 있는 사람은 누구나 출력된 자격 증명을 볼 수 있습니다."}
::option[작업 상태를 보여 주려고 모든 환경 변수 값을 출력합니다.]{#ci-workflow-permissions-safe-diagnostic-c explanation="환경 변수를 모두 출력하면 민감한 값이 포함될 수 있습니다."}
::option[어느 게시 단계가 실패했고 접근 결과가 어땠는지 알립니다.]{#ci-workflow-permissions-safe-diagnostic-b .correct explanation="검토하는 사람은 실패 위치를 찾고 설정된 접근 권한을 따로 확인할 수 있습니다."}
:::

## 새 작업 검토하기

제안된 워크플로는 풀 리퀘스트에서 페이지를 검사하고 패키지를 게시하는 작업을 추가합니다. 두 작업에 필요한 권한은 다릅니다. 검사 작업에는 필요한 읽기 권한만 두고, 승인된 게시 권한은 실제로 게시하는 작업에만 부여하세요.

:::single-choice{#ci-workflow-permissions-final-application} 두 작업에 필요한 권한을 가장 잘 반영한 수정은 무엇인가요?

::option[두 작업 모두에 저장소 쓰기 권한을 줍니다.]{#ci-workflow-permissions-final-application-b explanation="검사는 소스만 읽습니다. 패키지 게시에는 저장소 쓰기 권한과 다른 권한이 필요할 수 있습니다."}
::option[재실행 결과를 일정하게 유지하려고 모든 단계에서 업로드 자격 증명을 공유합니다.]{#ci-workflow-permissions-final-application-c explanation="업로드용 자격 증명은 게시 작업에만 필요합니다."}
::option[검사는 읽기 전용으로 유지하고, 게시 작업에는 필요한 패키지 접근 권한만 줍니다.]{#ci-workflow-permissions-final-application-a .correct explanation="각 작업에 필요한 권한을 주면서 다른 곳의 권한을 줄일 수 있습니다."}
:::

## 요약

이제 간단한 CI 파이프라인에 필요한 접근 권한을 판단할 수 있습니다.

1. 작업에 필요한 만큼 저장소 권한을 부여합니다.
2. 비공개 자격 증명은 접근이 통제되는 곳에 보관합니다.
3. 자격 증명 값은 숨긴 채 조사에 도움이 되는 오류를 기록합니다.
