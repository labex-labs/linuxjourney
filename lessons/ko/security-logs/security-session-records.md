---
lesson_id: "security-session-records"
course_id: "security-logs"
lang: "ko"
order_index: 4
title: "세션 기록"
description: "세션 시작과 종료 기록을 짝지어 보고 로그 발췌본으로 어디까지 설명할 수 있는지 확인합니다."
meta_title: "세션 기록 - 보안 로그"
meta_description: "Linux 세션의 시작과 종료 이벤트를 연결하고, 종료 기록이 없을 때 무엇을 확인할지 결정합니다."
meta_keywords: "Linux 세션 기록, 세션 시작, 세션 종료, 로그인 세션 ID, 로그 보존"
---

로그인 검사를 통과하면 어떤 계정으로 인증됐는지 알 수 있습니다. **세션**은 로그인 후부터 로그아웃하거나 연결이 끊길 때까지의 활동 기간입니다. 두 이벤트가 모두 기록됐다면 언제 시작하고 끝났는지 로그에 나타납니다.

## 세션 시작 기록 읽기

시스템은 컴퓨터에서 세션을 식별할 수 있도록 **세션 ID**를 지정할 수 있습니다. 다음 모의 기록에는 `web-01`에서 같은 계정으로 세션이 두 번 열린 것이 나타납니다. 이 레슨의 모든 시각은 같은 시간대를 사용합니다.

```text
t=09:14:05Z source=session host=web-01 account=alex session=42 state=opened
t=09:17:00Z source=session host=web-01 account=alex session=43 state=opened
```

첫 줄은 세션 42가 시작됐다고 보고합니다. 둘째 줄은 같은 호스트에서 별도의 세션 43이 시작됐다고 보고합니다.

:::single-choice{#security-session-records-two-openings} 두 시작 기록으로 무엇을 알 수 있나요?

::option[두 번째 세션을 시작할 때 첫 번째 세션이 끝났다.]{#security-session-records-open-ended explanation="두 번째 기록은 별도의 세션이 시작됐음을 보여 줍니다. 첫 번째 세션의 종료 시각은 알 수 없습니다."}
::option[서로 다른 계정 두 개가 해당 호스트에 로그인했다.]{#security-session-records-open-accounts explanation="두 줄 모두 같은 계정입니다. 세션 필드로 서로 다른 활동 기간을 구분할 수 있습니다."}
::option[같은 계정에서 별도의 세션 두 개가 열렸다.]{#security-session-records-open-two .correct explanation="두 줄에 모두 alex가 표시되고 web-01에서 각각 다른 세션 ID를 사용합니다."}
:::

## 시작과 종료 기록 연결하기

두 기록을 짝짓기 전에 호스트와 세션 ID를 함께 읽으세요. 아래 종료 줄을 앞의 시작 기록과 비교합니다.

```text
t=09:20:05Z source=session host=web-01 account=alex session=42 state=closed
```

`web-01`의 세션 42 시작과 종료는 6분 차이입니다. 짝지은 기록으로 기록된 시작과 끝을 알 수 있습니다. 그 사이의 동작 목록은 나오지 않습니다.

![세션 42와 43의 모의 시작 기록과 세션 42의 종료 기록을 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-session-records/session-records.png)

이 화면은 모의 시작 및 종료 기록을 함께 보여 줍니다.

:::single-choice{#security-session-records-pair-ids} 호스트와 시각은 그대로인데 종료 줄에 `session=43`이 표시됐다면, 그 세션은 언제 시작됐나요?

::option[09:14:05.]{#security-session-records-pair-forty-two explanation="같은 계정의 기록이지만 세션 42의 시작입니다."}
::option[09:17:00.]{#security-session-records-pair-forty-three .correct explanation="web-01과 세션 43은 두 번째 시작 기록과 일치합니다. 시작 시각은 09:17:00입니다."}
::option[09:20:05.]{#security-session-records-pair-end-time explanation="기록된 종료 시각입니다. 시작 시각은 해당 시작 기록에서 확인합니다."}
:::

## 종료 기록이 없을 때 확인하기

세션 42의 원래 종료 기록으로 돌아가 봅시다. 발췌본은 09:21에 끝나고 세션 43과 맞는 종료는 없습니다. 발췌본이 끝났을 때 세션이 여전히 활성 상태였을 수 있습니다. 종료 기록이 시간 범위 밖에 있거나 이 출처에 누락됐을 수도 있습니다. 로그의 **보존 기간**은 기록을 저장해 검토할 수 있는 기간입니다.

:::single-choice{#security-session-records-missing-close} 발췌본만으로 세션 43에 대해 무엇을 말할 수 있나요?

::option[발췌본이 끝날 때까지 활성 상태였다.]{#security-session-records-missing-active explanation="가능성은 있지만 종료 기록이 없다는 사실만으로 상태를 단정할 수 없습니다."}
::option[이 발췌본에 세션의 종료 시각이 없다.]{#security-session-records-missing-unknown .correct explanation="확보한 기록에 대해 말할 수 있는 내용입니다. 이후나 다른 출처의 기록에서 종료 시각을 찾을 수 있습니다."}
::option[세션 42와 함께 종료됐다.]{#security-session-records-missing-together explanation="기록된 종료는 세션 42에 속합니다. 여기에는 43과 맞는 기록이 없습니다."}
:::

## 질문에 맞는 출처 고르기

과거 종료 시각을 알고 싶다면 같은 호스트의 이후 기록에서 맞는 종료 항목을 찾으세요. 지금도 활성 상태인지 알고 싶다면 해당 호스트의 현재 세션 목록을 확인하세요. 저장된 로그와 현재 목록은 서로 다른 시점의 질문에 답합니다.

:::single-choice{#security-session-records-current-status} 세션 43이 지금 활성 상태인지 알아야 합니다. 가장 도움이 되는 출처는 무엇인가요?

::option[web-01의 현재 세션 목록.]{#security-session-records-current-list .correct explanation="현재 목록에는 호스트가 지금 활성 상태로 보고하는 세션이 나옵니다."}
::option[시작 기록의 오래된 사본.]{#security-session-records-current-opening explanation="시작했다는 사실은 보여 주지만 아직 활성 상태인지는 알 수 없습니다."}
::option[web-01의 세션 42 종료 기록.]{#security-session-records-current-other explanation="다른 세션이 종료됐다는 기록으로는 세션 43을 판단할 수 없습니다."}
:::

## 요약

이제 세션 기록을 사용해 기록된 시작과 종료를 설명할 수 있습니다.

1. 시작 기록에서 호스트와 세션 ID를 확인합니다.
2. 종료 기록을 알맞은 시작 기록과 연결합니다.
3. 종료 기록이 없을 때 밝혀지지 않은 내용을 설명합니다.
4. 질문에 따라 과거 기록과 현재 세션 목록 중 알맞은 출처를 고릅니다.
