---
lesson_id: "ci-overview"
course_id: "continuous-integration"
lang: "ko"
order_index: 1
title: "지속적 통합"
description: "작은 변경이 공유 브랜치에 들어가기 전에 지속적 통합이 어떻게 변경을 검사하는지 알아봅니다."
meta_title: "지속적 통합 - 지속적 통합"
meta_description: "작은 변경이 공유 브랜치에 들어가기 전에 지속적 통합이 어떻게 변경을 검사하는지 알아봅니다."
meta_keywords: "지속적 통합, CI, DevOps, Linux Journey"
---

홈페이지를 바꾼 뒤 내 브라우저에서는 멀쩡해 보여도 다른 사람이 열었을 때 문제가 생길 수 있습니다. **지속적 통합**(CI)은 변경을 자주 합치고, 특정 리비전에 대해 같은 방식으로 반복할 수 있는 검사를 실행하는 방식입니다.

## 변경과 검사 결과 연결하기

리비전은 검사하는 파일의 버전을 식별합니다. 변경 제안에서 `index.html`을 수정하면 CI는 바로 그 버전을 검사하고 조건을 충족하는지 알려 줄 수 있습니다. 이 사이트에서는 필요한 제목이 있는지 검사할 수 있습니다. 팀은 변경을 병합할지 결정할 때 검사 결과를 참고합니다.

:::single-choice{#ci-overview-revision-result} 월요일에 검사를 통과했고, 화요일에는 새 커밋에서 페이지를 수정했습니다. 월요일 결과로 무엇을 알 수 있나요?

::option[두 리비전이 모두 검사를 통과했다는 사실입니다.]{#ci-overview-revision-result-b explanation="나중에 추가된 커밋은 그 커밋에 대한 결과가 필요합니다."}
::option[월요일 리비전이 해당 검사를 통과했다는 사실입니다.]{#ci-overview-revision-result-a .correct explanation="결과는 검사를 실행한 리비전에 해당합니다."}
::option[방문자에게 새 페이지가 보인다는 사실입니다.]{#ci-overview-revision-result-c explanation="소스 파일을 검사한 결과만으로는 실제 서비스에 배포됐는지 알 수 없습니다."}
:::

## 실패한 검사 읽기

검사에서 예상한 제목이 없다고 보고했다고 가정해 봅시다. 변경을 작성한 사람은 우선 확인할 곳을 알 수 있습니다. 페이지를 고치기 전에 예상한 조건과 실제 결과를 읽으세요. 파일을 잘못 고쳤을 수도 있고, 기대하는 동작이 바뀌어 검사도 수정해야 할 수도 있습니다.

:::single-choice{#ci-overview-failed-action} 제목 검사가 실패하면 가장 먼저 무엇을 확인해야 하나요?

::option[예상한 제목과 검사 대상 리비전의 파일입니다.]{#ci-overview-failed-action-b .correct explanation="두 내용을 비교하면 이번 불일치의 원인을 찾을 수 있습니다."}
::option[이전의 성공한 실행에서 만든 아티팩트입니다.]{#ci-overview-failed-action-a explanation="그 아티팩트는 과거 결과입니다. 이번에 실패한 검사와 현재 파일이 더 직접적인 단서입니다."}
::option[방문자의 네트워크 설정입니다.]{#ci-overview-failed-action-c explanation="이 검사는 브라우저 요청을 보내지 않고 파일을 읽습니다."}
:::

## 검사와 배포 과정 구분하기

파이프라인은 파일을 검사하고 결과물을 만든 뒤, 나중에 배포 단계로 넘길 수 있습니다. **빌드**에서는 웹 서버가 제공할 수 있도록 정리한 디렉터리처럼 이후 단계에서 쓸 결과물을 만듭니다. **배포**는 특정 버전을 대상 환경에 설치하거나 시작하는 작업입니다. 첫 CI 워크플로는 페이지를 다음 단계로 넘기기 전에 검사합니다.

:::single-choice{#ci-overview-output-vs-live} 테스트가 통과하고 사이트 압축 파일도 만들어졌습니다. 방문자가 이 버전을 쓸 수 있는지 어떻게 확인하나요?

::option[검사 로그의 사본을 하나 더 확인합니다.]{#ci-overview-output-vs-live-a explanation="로그에는 검사와 빌드에 대한 정보가 있습니다."}
::option[압축 파일이 있는지 확인합니다.]{#ci-overview-output-vs-live-b explanation="파일이 만들어져도 사이트에서 제공하지 않을 수 있습니다."}
::option[배포 기록을 확인하고, 대상 페이지로 보낸 요청이 성공했는지 봅니다.]{#ci-overview-output-vs-live-c .correct explanation="두 결과를 보면 빌드한 버전과 대상 환경의 응답을 연결할 수 있습니다."}
:::

## 요약

이제 변경이 반영되는 과정에서 CI가 어떤 역할을 하는지 설명할 수 있습니다.

1. 검사 결과를 특정 리비전과 연결합니다.
2. 검사가 실패하면 무엇을 먼저 조사할지 판단합니다.
3. 검사, 빌드, 배포를 구분합니다.
