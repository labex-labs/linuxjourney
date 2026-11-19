---
lesson_id: "deployment-image-versions"
course_id: "deployment"
lang: "ko"
order_index: 2
title: "이미지 버전"
description: "이미지 태그와 다이제스트를 구분하고, 두 환경에서 사용하는 이미지를 정확히 비교하는 방법을 알아봅니다."
meta_title: "이미지 버전 - 배포"
meta_description: "이미지 태그와 다이제스트를 구분하고, 두 환경에서 사용하는 이미지를 정확히 비교하는 방법을 알아봅니다."
meta_keywords: "이미지 버전, 이미지 태그, 다이제스트, 배포, DevOps, Linux Journey"
---

`site:2` 같은 태그는 이미지 참조를 읽기 쉽게 해 줍니다. 게시자가 새 이미지를 푸시할 때 같은 태그가 다른 이미지를 가리키게 할 수 있습니다. 이미지의 정확한 내용을 식별하려면, 해당 내용에서 계산한 값인 **다이제스트**를 기록하세요.

## 태그 읽기

이미지 레지스트리에 서로 다른 날짜에 다음 기록이 나왔다고 가정해 봅시다. 줄여 쓴 다이제스트는 예시이며, 이 값으로 이미지를 가져올 수는 없습니다.

```text
Monday    site:2    sha256:a1b2…
Tuesday   site:2    sha256:c3d4…
```

같은 태그가 이제 다른 내용을 가리킵니다. 월요일에 이미지를 가져온 컴퓨터는 여전히 이전 이미지를 사용할 수 있습니다.

:::single-choice{#deployment-image-versions-moving-tag} 두 환경이 모두 site:2 태그를 표시합니다. 각각 실제로 어떤 이미지를 가져왔는지 무엇으로 확인하나요?

::option[두 환경이 쓰는 공통 태그만 봅니다.]{#deployment-image-versions-moving-tag-b explanation="예시에서는 서로 다른 이미지가 같은 태그를 사용합니다."}
::option[각 컴퓨터의 컨테이너 수를 확인합니다.]{#deployment-image-versions-moving-tag-c explanation="컨테이너 수로는 사용 중인 이미지를 알 수 없습니다."}
::option[기록된 다이제스트를 확인합니다.]{#deployment-image-versions-moving-tag-a .correct explanation="태그가 가리키는 대상은 바뀔 수 있습니다. 다이제스트는 가져올 때 선택한 내용을 식별합니다."}
:::

## 다이제스트로 지정한 참조 읽기

이미지 참조에 `@` 기호와 전체 다이제스트를 차례로 적을 수 있습니다. 이 형식으로 레지스트리에 정확한 객체를 요청합니다. 레지스트리나 빌드 기록에 있는 전체 다이제스트를 사용하세요. 짧게 표시한 값은 예시에 유용하지만 이미지를 가져오려면 전체 값이 필요합니다.

:::single-choice{#deployment-image-versions-fixed-reference} 어떤 형식으로 레지스트리의 특정 객체를 선택할 수 있나요?

::option[태그 없이 이미지 이름만 씁니다.]{#deployment-image-versions-fixed-reference-a explanation="Docker는 기본 태그를 적용합니다. 이 태그가 가리키는 대상도 바뀔 수 있습니다."}
::option[이미지 이름 뒤에 전체 다이제스트를 붙입니다.]{#deployment-image-versions-fixed-reference-c .correct explanation="다이제스트는 정확히 어떤 내용인지 식별합니다."}
::option[빌드한 날짜를 주석에 적습니다.]{#deployment-image-versions-fixed-reference-b explanation="레지스트리는 주석으로 객체를 가져올 수 없습니다."}
:::

## 같은 플랫폼의 이미지 비교하기

이미지 이름은 여러 종류의 컴퓨터를 위한 빌드 목록이나 특정 플랫폼용 이미지 하나를 가리킬 수 있습니다. 두 호스트가 실제로 무엇을 실행하는지 비교하려면, 호스트의 플랫폼을 기록하고 그에 해당하는 이미지 참조를 비교하세요. 원래의 전체 참조는 릴리스 기록에 남깁니다.

:::single-choice{#deployment-image-versions-compare-platform} 어떤 릴리스가 arm64와 amd64를 모두 지원합니다. 두 amd64 호스트를 확인할 때 어떤 비교가 유용한가요?

::option[두 호스트가 선택한 amd64 이미지 참조를 비교합니다.]{#deployment-image-versions-compare-platform-b .correct explanation="같은 플랫폼을 대상으로 만든 내용을 비교하는 방식입니다."}
::option[서로 다른 아키텍처용 이미지를 비교합니다.]{#deployment-image-versions-compare-platform-a explanation="이 객체들은 원래 서로 다른 플랫폼을 대상으로 합니다."}
::option[두 호스트의 이름을 비교합니다.]{#deployment-image-versions-compare-platform-c explanation="호스트 이름은 컴퓨터를 식별하지만 무엇을 배포했는지는 알려 주지 않습니다."}
:::

## 요약

이제 읽기 쉬운 태그에서 한 걸음 더 나아가 실제 사용한 이미지를 정확히 추적할 수 있습니다.

1. 같은 태그가 다른 내용을 가리킬 수 있는 이유를 설명합니다.
2. 전체 다이제스트를 포함한 참조를 알아봅니다.
3. 해당 플랫폼의 이미지를 비교합니다.
