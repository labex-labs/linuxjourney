---
lesson_id: "linux-least-privilege"
course_id: "linux-hardening"
lang: "ko"
order_index: 3
title: "최소 권한"
description: "특정 서비스 작업에 필요한 파일 권한과 관리 권한을 정하는 방법을 알아봅니다."
meta_title: "최소 권한 - Linux 보안 강화"
meta_description: "특정 서비스 작업에 필요한 파일 권한과 관리 권한을 정하는 방법을 알아봅니다."
meta_keywords: "최소 권한, Linux 보안 강화, 사이버 보안, Linux Journey"
---

**최소 권한**은 계정에 맡은 작업을 수행하는 데 필요한 접근 권한만 주는 원칙입니다. 먼저 계정이 수행할 동작을 적어 보세요. 한 파일을 읽고 다른 파일에 쓰기만 하면 되며 관리 작업은 필요하지 않을 수도 있습니다.

## 작업에 맞는 권한 부여하기

웹 워커는 `index.html`을 읽어야 합니다. 이 파일을 업데이트하는 것은 배포 계정의 역할입니다. 두 작업에 다른 권한을 부여할 수 있습니다. 워커에는 페이지를 읽을 권한을, 배포 계정에는 쓸 권한을 줍니다.

:::single-choice{#linux-least-privilege-read-only-page} 이 예시에서 워커에는 페이지에 대한 어떤 권한이 필요한가요?

::option[읽기 권한입니다.]{#linux-least-privilege-read-only-page-a .correct explanation="파일을 제공하려면 내용을 읽어야 합니다."}
::option[쓰기 권한입니다.]{#linux-least-privilege-read-only-page-b explanation="페이지를 변경하는 계정은 배포 계정입니다."}
::option[관련 없는 서비스를 관리할 권한입니다.]{#linux-least-privilege-read-only-page-c explanation="그 관리 작업은 웹 워커의 역할에 포함되지 않습니다."}
:::

## 전체 경로 확인하기

파일 자체의 권한 외에 파일까지 이어지는 디렉터리에 들어갈 권한도 필요합니다. 디렉터리의 실행 권한이 있으면 프로그램이 필요한 이름을 알고 있을 때 그 디렉터리를 통과할 수 있습니다. 파일에 읽기 권한이 있어도 워커가 중간 디렉터리를 통과할 수 없으면 해당 파일에 접근할 수 없습니다.

:::single-choice{#linux-least-privilege-path-boundary} 파일 모드에 따르면 워커가 index.html을 읽을 수 있지만 상위 디렉터리에 들어갈 수 없습니다. 무엇을 검토해야 하나요?

::option[페이지 파일이 더 큰지 확인합니다.]{#linux-least-privilege-path-boundary-a explanation="파일 크기는 디렉터리 접근 권한과 관계없습니다."}
::option[모든 사용자가 페이지에 쓸 수 있게 할지 검토합니다.]{#linux-least-privilege-path-boundary-c explanation="쓰기 권한을 주어도 경로를 통과할 수 없는 문제는 해결되지 않습니다."}
::option[워커가 디렉터리를 통과할 권한을 갖는지 확인합니다.]{#linux-least-privilege-path-boundary-b .correct explanation="파일에 대한 권한과 그 파일까지 경로를 통과할 권한이 모두 필요합니다."}
:::

## 관리 작업 제한하기

`sudo` 같은 관리 도구로 승인된 사용자가 특정 유지보수 작업을 수행할 수 있게 할 수 있습니다. 어떤 작업인지, 누가 승인되었는지, 새 권한을 어떻게 검증할지 정하세요. 같은 정책에서 승인된 유지보수 작업은 가능하고 관련 없는 관리 작업은 여전히 제한되는지 확인합니다.

:::single-choice{#linux-least-privilege-policy-test} 유지보수 역할을 맡은 사람이 서비스 상태를 확인해야 합니다. 의도한 권한을 검증하는 데 가장 적절한 계획은 무엇인가요?

::option[모든 관리 명령이 성공하는지 확인합니다.]{#linux-least-privilege-policy-test-a explanation="추가 권한은 문서에 명시한 작업 범위를 넘어섭니다."}
::option[서비스 상태를 확인할 수 있고 관련 없는 관리자 권한 변경 작업은 여전히 제한되는지 확인합니다.]{#linux-least-privilege-policy-test-c .correct explanation="필요한 접근과 의도한 권한 범위를 모두 검사합니다."}
::option[사용자 이름이 있는지만 확인합니다.]{#linux-least-privilege-policy-test-b explanation="계정이 있어도 어떤 권한이 있는지는 알 수 없습니다."}
:::

## 요약

이제 작업에 필요한 최소한의 접근 권한을 판단할 수 있습니다.

1. 읽기, 쓰기, 관리 작업을 구분합니다.
2. 경로에 포함된 디렉터리를 통과할 권한을 확인합니다.
3. 역할에 허용한 작업과 제한한 작업을 모두 검증합니다.
