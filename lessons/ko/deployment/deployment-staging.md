---
lesson_id: "deployment-staging"
course_id: "deployment"
lang: "ko"
order_index: 3
title: "스테이징"
description: "스테이징에서 무엇을 확인할 수 있는지 알아보고, 같은 아티팩트가 환경에 따라 다르게 동작하는 이유를 살펴봅니다."
meta_title: "스테이징 - 배포"
meta_description: "스테이징에서 무엇을 확인할 수 있는지 알아보고, 같은 아티팩트가 환경에 따라 다르게 동작하는 이유를 살펴봅니다."
meta_keywords: "스테이징, 테스트 환경, 배포, DevOps, Linux Journey"
---

릴리스가 거의 준비되었습니다. 아티팩트를 **스테이징**에서 실행해 보세요. 스테이징은 사용자가 이용할 운영 서비스와 비슷하게 구성한 테스트 환경입니다. 운영 트래픽을 받기 전에 실제와 비슷한 설정으로 릴리스를 확인할 수 있습니다.

## 같은 아티팩트를 다음 환경으로 넘기기

테스트하고 승인한 이미지를 사용합니다. 의존성이 바뀐 뒤 다시 빌드하면 다른 아티팩트가 만들어질 수 있습니다. 배포할 때마다 전체 이미지 참조를 기록하세요.

```text
Environment  Artifact      Page configuration
staging      site@digest-A Internal preview
production   site@digest-A Public website
```

예시에 나온 다이제스트는 설명을 위한 값입니다. 두 환경은 같은 아티팩트를 쓰고 설정은 서로 다릅니다.

:::single-choice{#deployment-staging-same-artifact} 스테이징에서 확인한 패키지를 운영 환경에도 그대로 배포할 수 있다는 것을 무엇으로 확인하나요?

::option[두 배포 기록의 아티팩트 참조가 같습니다.]{#deployment-staging-same-artifact-b .correct explanation="정확한 참조를 보면 두 환경이 같은 빌드를 쓰는지 알 수 있습니다."}
::option[두 환경의 포트 라벨 하나가 같습니다.]{#deployment-staging-same-artifact-a explanation="설정 하나가 같아도 아티팩트까지 같은지는 알 수 없습니다."}
::option[두 환경을 같은 날 배포했습니다.]{#deployment-staging-same-artifact-c explanation="배포 날짜만으로는 무엇을 배포했는지 알 수 없습니다."}
:::

## 실제 사용을 반영하는 검사 고르기

스테이징에서는 페이지를 열거나 테스트용 의존 서비스에서 데이터를 읽는 등 중요한 동작을 확인할 수 있어야 합니다. 허가받은 테스트 계정과 테스트 데이터를 사용하세요. 스테이징에서 검사가 성공하면 그 시나리오에 대한 신뢰가 높아집니다. 운영으로 옮긴 뒤에는 트래픽, 데이터, 설정의 차이가 여전히 영향을 줄 수 있습니다.

:::single-choice{#deployment-staging-staging-scope} 스테이징에서 테스트 데이터베이스를 사용해 페이지가 열렸습니다. 운영 환경에 배포한 뒤 무엇을 확인해야 하나요?

::option[아티팩트에 더 이상 버전 정보가 필요 없는지 확인합니다.]{#deployment-staging-staging-scope-b explanation="버전 기록은 확인과 복구에 계속 도움이 됩니다."}
::option[운영 환경의 모든 요청이 성공하는지 확인합니다.]{#deployment-staging-staging-scope-c explanation="적은 수의 테스트로 앞으로의 모든 결과를 알 수는 없습니다."}
::option[운영 환경의 접속 경로가 승인된 설정으로 동작하는지 확인합니다.]{#deployment-staging-staging-scope-a .correct explanation="스테이징 요청은 운영 환경을 거치지 않았습니다."}
:::

## 변경 전에 대상 확인하기

배포를 적용하기 전에 대상의 이름과 주소를 읽습니다. 배포한 뒤에는 같은 주소에서 새 버전과 중요한 동작을 확인합니다. 어떤 환경의 결과인지 바로 알 수 있도록 기록에서 스테이징과 운영 환경을 명확히 표시하세요.

:::single-choice{#deployment-staging-correct-target} 스테이징에 배포할 예정인데 명령에 운영 주소가 표시됩니다. 먼저 무엇을 해야 하나요?

::option[그대로 진행하고 나중에 결과를 스테이징으로 표시합니다.]{#deployment-staging-correct-target-a explanation="주소에 따라 어느 서비스에 변경이 적용될지 결정됩니다."}
::option[멈추고 배포하려던 대상 환경을 확인합니다.]{#deployment-staging-correct-target-c .correct explanation="이렇게 하면 잘못된 환경을 바꾸는 일을 피할 수 있습니다."}
::option[배포한 뒤 다른 브라우저로 테스트합니다.]{#deployment-staging-correct-target-b explanation="변경을 시작하기 전에 대상을 바로잡아야 합니다."}
:::

CI/CD 실습 예시는 [스테이징에 지속적으로 배포하기](https://labex.io/tutorials/cd-deployment-to-staging-636593)를 참고하세요.

## 요약

이제 승인된 아티팩트를 다음 환경으로 넘기기 전에 스테이징에서 검증할 수 있습니다.

1. 환경을 옮겨도 같은 아티팩트를 유지합니다.
2. 사용자에게 중요한 동작을 반영하는 검사를 선택합니다.
3. 변경을 적용하기 전에 대상 환경을 확인합니다.
