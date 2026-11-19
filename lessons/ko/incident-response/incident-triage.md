---
lesson_id: "incident-triage"
course_id: "incident-response"
lang: "ko"
order_index: 1
title: "사고 초기 분류"
description: "최초 사고 보고를 바탕으로 초기 조사의 범위를 정하는 방법을 알아봅니다."
meta_title: "사고 초기 분류 - 사고 대응"
meta_description: "최초 사고 보고를 바탕으로 초기 조사의 범위를 정하는 방법을 알아봅니다."
meta_keywords: "사고 초기 분류, 사고 대응, 사이버 보안, Linux Journey"
---

최초 보고에는 페이지에서 오류가 발생했거나 알림이 왔다는 내용이 담길 수 있습니다. **초기 분류**는 무엇을 먼저 처리해야 할지 판단하는 과정입니다. 조치를 정하기 전에 영향을 받은 서비스, 시각, 관찰한 동작을 적으세요.

## 최초 보고서 읽기

팀원이 아래와 같은 모의 보고서를 작성했습니다.

```text
09:22 UTC: Visitors received 503 from the public homepage.
The staff preview still loaded during the same check.
First failure observed at approximately 09:19 UTC.
```

보고서에는 두 경로와 서로 다른 두 관찰 결과가 나옵니다. 공개 홈페이지를 확인하고 검사 시각과 주소를 기록하세요.

:::single-choice{#incident-triage-affected-service} 어떤 증상을 먼저 확인해야 하나요?

::option[직원용 미리 보기가 503을 반환하는 증상입니다.]{#incident-triage-affected-service-b explanation="보고서에 따르면 미리 보기는 계속 열렸습니다."}
::option[공개 홈페이지가 503을 반환하는 증상입니다.]{#incident-triage-affected-service-a .correct explanation="보고서에 영향을 받았다고 명시된 경로입니다."}
::option[관련 없는 호스트에서 페이지가 사라진 증상입니다.]{#incident-triage-affected-service-c explanation="이 보고서에 해당하는 경로가 아닙니다."}
:::

## 영향 범위 추정하기

영향을 받은 사용자 수나 요청 건수를 확인하고 서비스를 계속 이용할 수 있는지 살펴보세요. 상황이 진행 중인지도 확인합니다. 더 정확한 증거를 확보할 때까지 불확실한 추정치는 추정치라고 명시하세요. 누구에게 알려야 할지는 대응 계획을 따릅니다.

:::single-choice{#incident-triage-triage-scope} 여전히 긴급한 문제인지 판단하는 데 어떤 관찰이 도움이 되나요?

::option[실패한 경로의 현재 상태와 최근 요청 결과입니다.]{#incident-triage-triage-scope-b .correct explanation="증상이 계속되는지, 얼마나 넓게 나타나는지 확인할 수 있습니다."}
::option[저장소의 첫 커밋으로부터 지난 시간입니다.]{#incident-triage-triage-scope-a explanation="현재 어떤 영향이 있는지 보여 주지 않습니다."}
::option[최초 보고에 표시된 심각도만 확인합니다.]{#incident-triage-triage-scope-c explanation="최초 심각도는 참고 정보입니다. 여전히 긴급한지는 현재 영향을 확인해 판단합니다."}
:::

## 첫 조치 선택하기

지금 보낸 요청도 실패한다면 결과를 남기고 최근 서비스 변경 사항과 문제가 발생한 구간의 로그를 살펴보세요. 정상적으로 동작하는 다른 경로를 함께 보면 문제 범위를 좁힐 수 있습니다. 처음 떠오른 그럴듯한 설명을 확인된 원인으로 취급하지 마세요.

:::single-choice{#incident-triage-first-next-step} 공개 경로는 여전히 실패하고 직원용 미리 보기는 계속 동작합니다. 다음으로 무엇을 살펴봐야 하나요?

::option[회사 내 관련 없는 프로젝트를 모두 살펴봅니다.]{#incident-triage-first-next-step-a explanation="보고서에는 더 좁은 서비스 범위와 시간 구간이 제시되어 있습니다."}
::option[다른 날짜에 발생한 오래된 오류를 임의로 하나 봅니다.]{#incident-triage-first-next-step-b explanation="관찰된 실패와 가까운 시각의 증거부터 살펴보세요."}
::option[보고된 시간 구간의 공개 경로 기록을 살펴봅니다.]{#incident-triage-first-next-step-c .correct explanation="라우팅 문제인지 서비스 장애인지 구분하는 데 도움이 됩니다."}
:::

## 요약

이제 사고 보고를 받고 범위를 좁혀 초기 대응을 시작할 수 있습니다.

1. 영향을 받은 경로, 시각, 증상을 명시합니다.
2. 현재 사용자에게 어떤 영향이 있는지 확인합니다.
3. 영향을 받은 경로에 관해 다음에 확인할 증거 출처를 선택합니다.
