---
lesson_id: "deployment-rollbacks"
course_id: "deployment"
lang: "ko"
order_index: 5
title: "롤백"
description: "정상 동작이 확인된 버전을 선택하고 애플리케이션 롤백만으로 충분한지 판단하는 방법을 알아봅니다."
meta_title: "롤백 - 배포"
meta_description: "정상 동작이 확인된 버전을 선택하고 애플리케이션 롤백만으로 충분한지 판단하는 방법을 알아봅니다."
meta_keywords: "롤백, 배포, DevOps, Linux Journey"
---

**롤백**은 정상 동작이 확인된 이전 릴리스로 서비스를 되돌리는 작업입니다. 배포 이력을 보고 되돌릴 버전을 선택하세요. 변경을 되돌리기 전에 릴리스에서 공유 데이터나 설정도 바뀌었는지 확인합니다.

## 이전 릴리스 선택하기

이 예시에서는 새 릴리스를 배포한 뒤 요청이 실패했습니다. 마지막으로 검증한 버전은 2입니다. 아래 참조 이름은 실제 기록에서 전체 이미지 다이제스트가 들어갈 자리입니다.

```text
08:50  version 2  digest-B  homepage and version check passed
09:10  version 3  digest-C  homepage check failed
```

버전 2가 현재 환경에서도 동작한다면 롤백 후보로 적합합니다. 기록해 둔 아티팩트 식별자를 사용해 이미지를 찾으세요.

:::single-choice{#deployment-rollbacks-previous-version} 롤백 대상으로 어떤 이미지를 먼저 확인해야 하나요?

::option[호스트에 가장 최근에 캐시된 이미지입니다.]{#deployment-rollbacks-previous-version-a explanation="캐시 순서만으로 정상 동작하는 릴리스를 찾을 수 없습니다."}
::option[가장 최근에 배포한 Digest-C입니다.]{#deployment-rollbacks-previous-version-c explanation="기록에 따르면 이 아티팩트를 배포했을 때 검사에 실패했습니다."}
::option[이전에 관련 검사를 통과한 Digest-B입니다.]{#deployment-rollbacks-previous-version-b .correct explanation="기록에 따르면 마지막으로 검증한 버전의 아티팩트입니다."}
:::

## 데이터 호환성 확인하기

애플리케이션을 릴리스할 때 데이터베이스나 다른 공유 리소스가 바뀔 수 있습니다. 이전 이미지를 실행해도 애플리케이션 외부의 상태는 그대로입니다. 이전 버전이 현재 데이터를 읽을 수 있는지 확인하세요. 데이터 복원이 필요하면 팀의 복구 계획에 따르고, 백업 이후에 생긴 변경 사항도 고려하세요.

:::single-choice{#deployment-rollbacks-external-state} 버전 3에서 데이터베이스 형식이 바뀌었습니다. 이 데이터베이스에 버전 2를 연결하기 전에 무엇을 확인해야 하나요?

::option[버전 2가 이전 홈페이지 검사를 통과했는지 확인합니다.]{#deployment-rollbacks-external-state-b explanation="이전 검사 결과를 근거로 버전 2를 후보에 올릴 수 있습니다. 현재 데이터베이스 형식과의 호환성은 별도로 확인해야 합니다."}
::option[버전 2가 현재 형식을 지원하는지 확인합니다.]{#deployment-rollbacks-external-state-a .correct explanation="애플리케이션 이미지를 바꿔도 공유 데이터는 이전 상태로 돌아가지 않습니다."}
::option[릴리스 노트에 데이터베이스 이름이 있는지 확인합니다.]{#deployment-rollbacks-external-state-c explanation="이전 버전의 코드로 현재 데이터를 사용할 수 있는지가 중요합니다."}
:::

## 롤백 결과 확인하기

롤백을 마치면 실행 중인 버전을 확인하고, 앞서 실패했던 사용자 관점의 검사를 반복하세요. 주요 의존 서비스의 상태도 다시 확인합니다. 최초 장애와 복구를 구분할 수 있도록 시각, 복구한 버전, 검사 결과를 기록하세요.

:::single-choice{#deployment-rollbacks-rollback-proof} 롤백 명령이 끝났습니다. 어떤 두 가지 결과로 서비스가 복구되었음을 확인할 수 있나요?

::option[엔드포인트에서 버전 2를 반환했고, 앞서 실패했던 검사를 통과했습니다.]{#deployment-rollbacks-rollback-proof-c .correct explanation="이 결과를 함께 보면 목표 버전이 실행 중이고 문제가 발생한 동작이 복구되었음을 확인할 수 있습니다."}
::option[이미지 다운로드에 두 번 성공했습니다.]{#deployment-rollbacks-rollback-proof-a explanation="다운로드는 파일을 준비하는 과정입니다. 실행 중인 서비스를 검사하는 과정은 별도로 거쳐야 합니다."}
::option[버전 2의 예전 스크린샷이 있습니다.]{#deployment-rollbacks-rollback-proof-b explanation="스크린샷은 과거의 상태를 보여 줍니다."}
:::

## 요약

이제 확인한 증거에 근거해 롤백을 계획할 수 있습니다.

1. 정상 동작을 검증한 이력이 있는 릴리스를 선택합니다.
2. 공유 데이터와 설정의 호환성을 확인합니다.
3. 복구한 버전과 사용자에게 문제가 되었던 동작을 확인합니다.
