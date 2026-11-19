---
lesson_id: "web-authorization"
course_id: "web-security"
lang: "ko"
order_index: 6
title: "인가"
description: "인증된 사용자의 요청을 애플리케이션 접근 정책과 비교하는 방법을 알아봅니다."
meta_title: "인가 - 웹 보안"
meta_description: "인증된 사용자의 요청을 애플리케이션 접근 정책과 비교하는 방법을 알아봅니다."
meta_keywords: "인가, 접근 권한, 웹 보안, 사이버 보안, Linux Journey"
---

로그인에 성공한 사용자라도 특정 작업을 수행할 권한이 없을 수 있습니다. **인가**는 특정 계정에 어떤 리소스에 대한 작업을 허용할지 판단하는 과정입니다.

## 정책 읽기

**역할**은 이름을 붙인 권한 묶음입니다. 이 실습에서는 아래 정책을 미리 보기 서비스에 적용합니다.

```text
Role       View published page   Edit draft
Reader    Yes                   No
Editor    Yes                   Yes
```

사용자의 역할에 해당하는 행과 요청한 작업에 해당하는 열을 읽으세요. 편집자는 공개된 페이지를 보고 초안을 편집할 수 있습니다. 읽기 전용 사용자는 공개된 페이지를 볼 수 있습니다.

:::single-choice{#web-authorization-read-policy} 로그인한 읽기 전용 사용자가 초안 편집을 요청합니다. 표에 따르면 어떻게 처리하나요?

::option[Reader 역할에는 이 작업이 허용되지 않습니다.]{#web-authorization-read-policy-b .correct explanation="Reader 행의 Edit draft 열에 No로 표시되어 있습니다."}
::option[로그인한 계정이면 누구나 이 작업을 할 수 있습니다.]{#web-authorization-read-policy-a explanation="요청한 작업의 권한은 역할에 따라 다릅니다."}
::option[편집 권한을 얻으려면 HTTPS로 전환해야 합니다.]{#web-authorization-read-policy-c explanation="전송 구간을 보호해도 애플리케이션 권한이 부여되지는 않습니다."}
:::

## 해당 리소스의 권한 확인하기

많은 시스템에서 리소스마다 다른 권한을 부여합니다. 편집자가 자기 프로젝트에서는 초안을 수정할 수 있지만 다른 프로젝트에서는 페이지를 보기만 할 수 있습니다. 권한을 확인할 때는 작업과 대상 리소스를 모두 확인하세요.

:::single-choice{#web-authorization-target-resource} Maya는 Project A를 편집할 수 있습니다. Project B도 편집할 수 있는지는 무엇으로 판단하나요?

::option[Project A의 제목입니다.]{#web-authorization-target-resource-b explanation="이 제목은 다른 프로젝트의 접근 권한을 설명하지 않습니다."}
::option[Maya가 로그인에 성공했다는 사실입니다.]{#web-authorization-target-resource-c explanation="인증을 통해 Maya의 계정을 확인했습니다. 해당 리소스의 권한은 별도로 확인해야 합니다."}
::option[Maya가 Project B에 접근할 때 적용되는 권한 정책입니다.]{#web-authorization-target-resource-a .correct explanation="앞서 부여된 권한은 특정 리소스에 적용됩니다."}
:::

## 서비스에서 권한 확인하기

사용자 인터페이스에서 읽기 전용 사용자에게 편집 버튼을 숨길 수 있습니다. 서버도 요청을 받을 때마다 정책을 적용해야 합니다. 실습 서비스에서는 승인된 일반 작업을 통해 허용되어야 할 경우와 거부되어야 할 경우를 모두 확인하세요.

:::single-choice{#web-authorization-decision-location} 애플리케이션에서 읽기 전용 사용자에게 Edit 버튼을 숨깁니다. 어느 곳에서 접근 정책을 추가로 적용해야 하나요?

::option[브라우저가 표시할 버튼을 결정할 때만 적용합니다.]{#web-authorization-decision-location-a explanation="브라우저는 권한에 맞는 화면을 보여 줄 수 있습니다. 실제 요청의 접근 여부는 요청을 받은 서비스가 판단합니다."}
::option[요청된 작업을 받는 서비스에서 적용합니다.]{#web-authorization-decision-location-c .correct explanation="서비스는 요청마다 계정, 작업, 대상 리소스를 확인할 수 있습니다."}
::option[역할을 나열한 페이지에서만 적용합니다.]{#web-authorization-decision-location-b explanation="역할 이름을 표시해도 제한된 작업을 막을 수는 없습니다."}
:::

## 요약

이제 애플리케이션이 접근 여부를 판단하는 방식을 이해할 수 있습니다.

1. 요청한 작업을 계정의 역할과 비교합니다.
2. 권한을 확인할 때 구체적인 대상 리소스를 포함합니다.
3. 서비스가 요청에 정책을 적용하는지 확인합니다.
