---
lesson_id: "build-release-deploy"
course_id: "deployment"
lang: "ko"
order_index: 1
title: "빌드, 릴리스, 배포"
description: "빌드, 릴리스, 배포 기록을 따라가며 소스 리비전의 이력을 확인하는 방법을 알아봅니다."
meta_title: "빌드, 릴리스, 배포 - 배포"
meta_description: "빌드, 릴리스, 배포 기록을 따라가며 소스 리비전의 이력을 확인하는 방법을 알아봅니다."
meta_keywords: "빌드, 릴리스, 배포, DevOps, Linux Journey"
---

팀원이 버전 2가 준비됐다고 말합니다. 파일 빌드가 끝났다는 뜻일 수도 있고, 버전이 승인됐거나 방문자가 이미 접속할 수 있다는 뜻일 수도 있습니다. 기록을 살펴보고 어느 단계까지 진행됐는지 확인하세요.

## 빌드 확인하기

빌드는 특정 소스 리비전에서 결과물을 만듭니다. 이 예에서는 작은 웹사이트를 컨테이너 이미지로 패키징해 이미지 레지스트리에 저장합니다. 만들어진 이미지 참조와 함께 소스 커밋을 기록합니다.

```text
Build 81
Source commit: 3ab4501
Image: registry.example/journey/site:2
Result: succeeded
```

이 기록은 무엇을 만들었는지 보여 줍니다. 사이트는 여전히 이전 버전을 제공하고 있을 수 있습니다.

:::single-choice{#build-release-deploy-build-record} 패키징한 이미지와 소스 리비전을 연결해 주는 기록은 무엇인가요?

::option[브라우저의 북마크입니다.]{#build-release-deploy-build-record-b explanation="북마크에는 주소가 있지만 파일을 어떻게 빌드했는지는 나오지 않습니다."}
::option[빌드 81입니다.]{#build-release-deploy-build-record-a .correct explanation="소스 커밋과 만들어진 이미지가 모두 적혀 있습니다."}
::option[가장 최근 로컬 브랜치의 이름입니다.]{#build-release-deploy-build-record-c explanation="브랜치가 가리키는 커밋은 바뀔 수 있으므로 이름만으로 이 빌드를 식별할 수 없습니다."}
:::

## 릴리스 기록 읽기

**릴리스**는 배포가 승인된 버전을 식별합니다. 예를 들어 릴리스 기록에는 빌드 81에서 만든 바로 그 이미지를 스테이징에 사용하도록 승인했다고 남길 수 있습니다. 이렇게 하면 승인 후 다시 빌드할 필요 없이 같은 아티팩트를 참조할 수 있습니다.

:::single-choice{#build-release-deploy-release-record} 릴리스 2가 스테이징용으로 승인되었습니다. 무엇을 알 수 있나요?

::option[기록된 아티팩트를 그 용도로 사용해도 된다는 뜻입니다.]{#build-release-deploy-release-record-b .correct explanation="릴리스 기록은 어느 아티팩트를 스테이징에 사용하도록 승인했는지 보여 줍니다."}
::option[모든 환경에서 이미 버전 2를 제공한다는 뜻입니다.]{#build-release-deploy-release-record-a explanation="승인은 다음 단계로 진행해도 된다는 뜻입니다. 실행 중인 버전은 따로 확인해야 합니다."}
::option[버전 2의 요청량이 더 많다는 뜻입니다.]{#build-release-deploy-release-record-c explanation="릴리스 기록은 트래픽을 측정하지 않습니다."}
:::

## 배포한 버전 찾기

**배포**는 특정 버전을 환경에 배치하고, 그 환경에서 애플리케이션을 시작하거나 갱신하는 작업입니다. 스테이징이나 운영 환경에는 각각 고유한 설정과 리소스가 있습니다. 버전을 알려 주는 엔드포인트에 요청을 보내면 그 환경에서 어느 버전이 응답하는지 확인할 수 있습니다.

```text
Staging version response: 2
Production version response: 1
```

이 예에서는 스테이징에서 새 버전이 응답하지만 운영 환경에서는 여전히 버전 1이 응답합니다.

:::single-choice{#build-release-deploy-running-version} 검토자가 운영 환경에서 버전 2가 응답하는지 확인하려고 합니다. 어떤 결과가 직접적인 근거가 되나요?

::option[버전 2를 반환하는 스테이징 환경의 두 번째 응답입니다.]{#build-release-deploy-running-version-a explanation="이 요청으로 확인하는 곳은 여전히 스테이징입니다."}
::option[릴리스 승인 메시지입니다.]{#build-release-deploy-running-version-b explanation="승인은 실행 중인 서비스를 검사한 결과가 아닙니다."}
::option[운영 환경 주소에서 받은 버전 응답입니다.]{#build-release-deploy-running-version-c .correct explanation="검토자가 확인하려는 환경에 직접 요청한 결과입니다."}
:::

## 요약

이제 릴리스 과정의 각 단계에서 어떤 기록이 생기는지 구분할 수 있습니다.

1. 빌드 결과물을 해당 소스와 연결합니다.
2. 릴리스에서 승인한 아티팩트를 찾습니다.
3. 원하는 환경에서 어느 버전이 응답하는지 확인합니다.
