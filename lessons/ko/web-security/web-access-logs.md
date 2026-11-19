---
lesson_id: "web-access-logs"
course_id: "web-security"
lang: "ko"
order_index: 7
title: "웹 접근 로그"
description: "자격 증명을 노출하지 않고 HTTP 접근 로그에서 서비스의 응답을 확인하는 방법을 알아봅니다."
meta_title: "웹 접근 로그 - 웹 보안"
meta_description: "자격 증명을 노출하지 않고 HTTP 접근 로그에서 서비스의 응답을 확인하는 방법을 알아봅니다."
meta_keywords: "웹 접근 로그, 웹 보안, 사이버 보안, Linux Journey"
---

웹 서버는 요청마다 **접근 로그**를 하나씩 남길 수 있습니다. 로그에는 시각, 경로, 응답 코드, 요청 ID 등이 들어갈 수 있습니다. 조사하려는 내용에 필요한 필드만 사용하세요.

## 요청 결과 읽기

이 모의 로그에는 각 필드의 이름이 표시됩니다. 두 요청은 서로 다른 경로로 전송되었습니다.

```text
t=09:18:01Z request=r31 method=GET path=/health status=200
t=09:18:04Z request=r32 method=GET path=/staff status=403
```

`403`은 서비스가 요청을 거부했음을 나타냅니다. 응답을 다른 기록과 비교하기 전에 정확한 경로와 요청 ID를 확인하세요.

:::single-choice{#web-access-logs-log-result} 요청 거부를 조사하려면 어느 요청을 추적해야 하나요?

::option[/health의 r31입니다.]{#web-access-logs-log-result-a explanation="이 행은 상태 확인 요청이 성공했음을 보여 줍니다."}
::option[/staff의 r32입니다.]{#web-access-logs-log-result-b .correct explanation="이 행의 상태 코드는 403이며, 예시에서 요청이 거부된 기록입니다."}
::option[두 요청이 같다고 보고 둘 다 추적합니다.]{#web-access-logs-log-result-c explanation="요청 ID와 경로를 보면 서로 다른 요청임을 알 수 있습니다."}
:::

## 접근 권한 판단 기록 찾기

접근 로그에는 서버에서 반환한 결과가 기록됩니다. 특정 요청에 왜 그런 권한 판단을 내렸는지는 표시되지 않을 수 있습니다. 애플리케이션에 권한 판단 기록도 남는다면 요청 ID와 시각을 대조하세요. 이 예시에서는 어떤 규칙이 적용되었는지 확인할 수 있습니다.

:::single-choice{#web-access-logs-refusal-reason} 접근 로그에 403이 표시됩니다. 어떤 기록을 추가로 살펴보면 이유를 파악할 수 있나요?

::option[r32에 대해 애플리케이션이 내린 권한 판단입니다.]{#web-access-logs-refusal-reason-a .correct explanation="해당 기록에는 어느 규칙을 적용했는지 나올 수 있습니다."}
::option[다른 사이트에서 받은 성공 응답입니다.]{#web-access-logs-refusal-reason-b explanation="다른 사이트의 응답은 이 요청의 거부와 관련이 없습니다."}
::option[상태 확인 경로에 보낸 이전 요청입니다.]{#web-access-logs-refusal-reason-c explanation="별개의 작업과 결과에 관한 기록입니다."}
:::

## 로그에 자격 증명 남기지 않기

세션 쿠키 전체나 인증 토큰처럼 다른 사람의 세션을 이용할 수 있는 값은 로그에 남기지 마세요. 요청 ID와 응답 상태만으로도 문제를 해결하는 데 도움이 됩니다. 로그 일부를 공유할 때는 민감한 필드를 제거하고 조사에 필요한 정보만 남기세요.

:::single-choice{#web-access-logs-safe-fields} 자격 증명을 복사하지 않고 거부된 요청을 추적하는 데 도움이 되는 두 가지 정보는 무엇인가요?

::option[세션 쿠키 전체와 계정 비밀번호입니다.]{#web-access-logs-safe-fields-a explanation="두 값은 민감하므로 공유 로그에 넣으면 안 됩니다."}
::option[인증 토큰과 공개 경로입니다.]{#web-access-logs-safe-fields-b explanation="경로는 유용할 수 있지만 토큰은 비공개 자격 증명입니다."}
::option[요청 ID와 해당 응답 상태입니다.]{#web-access-logs-safe-fields-c .correct explanation="세션 값을 공개하지 않고 관련 기록과 대조할 수 있습니다."}
:::

## 필요한 로그 일부만 공유하기

검토자가 거부된 요청의 상황을 파악해야 한다고 가정해 보세요. 시각, ID, 메서드, 민감한 정보를 제거한 경로, 상태로 충분하다면 이 필드만 남기세요. 경로의 쿼리 문자열에 비공개 값이 들어 있기도 합니다. 공유하기 전에 발췌 내용을 확인하세요.

:::single-choice{#web-access-logs-final-application} 어떤 정보를 발췌하면 이 검토에 가장 적합한가요?

::option[기본적으로 요청 전체와 모든 헤더를 공유합니다.]{#web-access-logs-final-application-b explanation="요청에는 자격 증명이나 검토에 필요하지 않은 개인정보가 포함될 수 있습니다."}
::option[모든 식별자를 빼고 상태 코드만 공유합니다.]{#web-access-logs-final-application-c explanation="코드만으로는 관련 정책 기록과 대조하기 어려울 수 있습니다."}
::option[민감한 정보를 제거한 경로와 요청 시각, ID, 응답 상태를 공유합니다.]{#web-access-logs-final-application-a .correct explanation="세션 값을 공개하지 않으면서 기록을 연결하는 데 필요한 필드를 남깁니다."}
:::

## 요약

이제 기본 접근 로그를 해석하고 필요한 상황 정보를 안전하게 남길 수 있습니다.

1. 요청 ID, 경로, 응답을 대조합니다.
2. 이유를 알아야 할 때 관련 정책 기록을 찾습니다.
3. 로그를 수집하고 공유할 때 자격 증명을 제외합니다.
