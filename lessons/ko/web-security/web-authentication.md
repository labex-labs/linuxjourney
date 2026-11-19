---
lesson_id: "web-authentication"
course_id: "web-security"
lang: "ko"
order_index: 4
title: "인증"
description: "웹 서비스가 사용자의 신원을 확인하는 방법과 두 가지 인증 요소가 서로 다른 증거를 제공하는 이유를 알아봅니다."
meta_title: "인증 - 웹 보안"
meta_description: "웹 서비스가 사용자의 신원을 확인하는 방법과 두 가지 인증 요소가 서로 다른 증거를 제공하는 이유를 알아봅니다."
meta_keywords: "인증, 웹 보안, 사이버 보안, Linux Journey"
---

**인증**은 사용자가 자신이라고 주장하는 신원을 확인하는 절차입니다. 로그인 화면에서는 계정 이름과 비밀번호를 요구할 수 있습니다. 계정 이름으로 사용하려는 신원을 밝히고, 비밀번호로 서비스가 검증할 수 있는 증거를 제공합니다.

## 사용자가 제시한 신원 파악하기

사용자가 계정 이름으로 `alex`를 입력했다고 생각해 보세요. 이름을 아는 사람은 누구나 이 값을 입력할 수 있습니다. 서비스는 해당 계정의 정보와 정책에 따라 제출된 증거를 검증합니다.

:::single-choice{#web-authentication-username-claim} 어떤 입력값을 보면 사용자가 접속하려는 계정을 알 수 있나요?

::option[비밀번호 검사 결과입니다.]{#web-authentication-username-claim-a explanation="검사 결과는 사용자가 제시한 신원을 받아들일지 판단하는 근거입니다."}
::option[계정 이름입니다.]{#web-authentication-username-claim-b .correct explanation="서비스가 어느 신원을 검증해야 하는지 알려 줍니다."}
::option[홈페이지의 응답 형식입니다.]{#web-authentication-username-claim-c explanation="콘텐츠 유형은 로그인할 계정과 관계없습니다."}
:::

## 인증 요소 비교하기

**인증 요소**는 신원을 입증하는 증거의 유형입니다. 비밀번호는 사용자가 알고 있는 정보입니다. 등록한 보안 키는 사용자가 가지고 있는 물건을 바탕으로 증거를 제공합니다. 비밀번호와 별도로 등록한 보안 키를 함께 사용하면 두 유형의 증거를 확인할 수 있습니다.

:::single-choice{#web-authentication-independent-factors} 알고 있는 정보와 소유한 물건을 함께 사용하는 예는 무엇인가요?

::option[비밀번호와 등록한 보안 키입니다.]{#web-authentication-independent-factors-a .correct explanation="하나는 정보를 알고 있는지, 다른 하나는 키를 사용할 수 있는지 확인합니다."}
::option[비밀번호와 별도로 외운 두 번째 비밀번호입니다.]{#web-authentication-independent-factors-b explanation="둘 다 사용자가 알고 있는 정보입니다."}
::option[사용자 이름과 페이지 제목입니다.]{#web-authentication-independent-factors-c explanation="이 두 이름은 신원을 입증할 증거로 쓰기 어렵습니다."}
:::

## 인증 성공의 의미 이해하기

증거를 검증한 뒤 서비스는 사용자가 세션을 시작하도록 허용할 수 있습니다. 신원 확인에 성공하면 서비스에서 어떤 계정이 로그인한 것으로 처리할지 정해집니다. 계정이 어떤 작업을 할 수 있는지는 별도의 문제입니다. 서비스는 특정 리소스에 대한 요청을 받을 때 접근 규칙을 적용합니다.

:::single-choice{#web-authentication-auth-limit} 로그인에 성공한 계정이 관리자 페이지를 요청합니다. 다음으로 무엇을 해야 하나요?

::option[로그인한 모든 계정에 페이지를 자동으로 제공합니다.]{#web-authentication-auth-limit-a explanation="해당 페이지에서 요구하는 권한이 계정에 있어야 합니다."}
::option[원래 페이지의 제목에 따라 접근을 결정합니다.]{#web-authentication-auth-limit-b explanation="페이지 제목으로는 사용자의 권한을 알 수 없습니다."}
::option[애플리케이션이 해당 리소스에 대한 계정의 접근 권한을 확인합니다.]{#web-authentication-auth-limit-c .correct explanation="신원 확인과 리소스 접근 여부는 서로 다른 판단입니다."}
:::

## 요약

이제 인증으로 무엇을 확인하는지 설명할 수 있습니다.

1. 사용자가 밝힌 신원과 이를 입증하는 증거를 구분합니다.
2. 서로 다른 두 유형의 인증 요소를 알아봅니다.
3. 개별 리소스에 대한 접근은 서비스의 권한 정책에 따라 결정합니다.
