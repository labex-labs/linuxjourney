---
lesson_id: "incident-reports"
course_id: "incident-response"
lang: "ko"
order_index: 6
title: "사고 보고서"
description: "관찰한 증거와 남은 질문을 바탕으로 간결한 사고 보고를 작성하는 방법을 알아봅니다."
meta_title: "사고 보고서 - 사고 대응"
meta_description: "관찰한 증거와 남은 질문을 바탕으로 간결한 사고 보고를 작성하는 방법을 알아봅니다."
meta_keywords: "사고 보고서, 사고 대응, 사이버 보안, Linux Journey"
---

짧은 사고 보고서가 있으면 다른 담당자가 조사 전체를 다시 구성하지 않고도 업무를 이어받을 수 있습니다. 영향을 받은 서비스와 시각이 명시된 주요 관찰 결과, 다음 조치를 포함하세요.

## 관찰 결과 보고하기

아래는 서비스 사고에서 나온 모의 기록 세 건입니다.

```text
09:17 UTC  Deployment record: version 3 reached production
09:22 UTC  Visitor-path check: homepage returned 503
09:31 UTC  After rollback: version 2, homepage returned 200
```

이 기록에는 변경, 실패, 복구 후 성공한 검사가 나옵니다. 영향을 받은 경로와 시각을 포함하고, 무엇을 검사했는지도 구체적으로 적으세요.

:::single-choice{#incident-reports-report-claim} 기록에서 직접 확인할 수 있는 사실은 무엇인가요?

::option[홈페이지 검사가 09:22에 실패했고 롤백한 뒤 성공했습니다.]{#incident-reports-report-claim-b .correct explanation="관찰한 결과와 순서를 요약한 설명입니다."}
::option[버전 3이 확실히 데이터베이스를 망가뜨렸습니다.]{#incident-reports-report-claim-a explanation="기록에는 실패가 어떻게 발생했는지 나오지 않습니다."}
::option[해당 구간 내내 모든 사용자가 영향을 받았습니다.]{#incident-reports-report-claim-c explanation="제공된 결과로는 모든 요청을 확인할 수 없습니다."}
:::

![운영 환경의 변경, 503 응답, 성공한 복구 검사를 보여 주는 모의 사고 증거](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-reports/evidence-timeline.png)

## 확인되지 않은 부분 설명하기

롤백 후 요청이 성공했다면 배포를 조사할 근거가 됩니다. 증거가 확보될 때까지 원인은 미확정 상태로 남겨 두세요. 예를 들어 유지보수 담당자는 실패한 요청이 발생한 구간에서 두 버전의 서비스 로그를 비교할 수 있습니다.

:::single-choice{#incident-reports-uncertainty-statement} 아직 확인할 사항으로 기록해야 할 문장은 무엇인가요?

::option[조사할 만한 사항이 없습니다.]{#incident-reports-uncertainty-statement-b explanation="릴리스와 오류 기록으로 다음 검사 범위를 좁힐 수 있습니다."}
::option[서비스를 영영 이용할 수 없었습니다.]{#incident-reports-uncertainty-statement-c explanation="이후 테스트 요청이 성공했으므로 그 주장은 해당 요청에 대해서는 성립하지 않습니다."}
::option[503이 발생한 원인은 아직 밝혀지지 않았습니다.]{#incident-reports-uncertainty-statement-a .correct explanation="증거에는 실패와 복구 검사가 나오지만 원인을 판단하려면 근거가 더 필요합니다."}
:::

## 다음 담당자의 작업 정하기

누가 다음 조치를 맡을 수 있는지, 어떤 기록을 찾아야 하는지, 어떤 결과가 남은 질문에 답할 수 있는지 명시하세요. 널리 공유하는 보고에 비밀 정보와 개인정보를 넣지 마세요. 승인된 검토자가 볼 수 있도록 보고서에 보호된 증거의 링크를 넣을 수 있습니다.

:::single-choice{#incident-reports-useful-handoff} 이 사례에서 어떤 조치를 이어서 하면 좋을까요?

::option[시각이나 서비스를 명시하지 않고 아무 스크린샷이나 찍어 달라고 요청합니다.]{#incident-reports-useful-handoff-a explanation="어떤 증거가 실패를 설명하는지 지정하지 않았습니다."}
::option[홈페이지 요청에 실패한 구간의 버전 3 로그를 서비스 유지보수 담당자에게 확인해 달라고 요청합니다.]{#incident-reports-useful-handoff-c .correct explanation="남은 질문을 조사할 구체적인 출처와 시간 구간을 지정했습니다."}
::option[이미 성공한 버전 2 검사만 다시 해 달라고 유지보수 담당자에게 요청합니다.]{#incident-reports-useful-handoff-b explanation="복구를 다시 확인하는 데는 도움이 될 수 있습니다. 버전 3에서 앞서 실패한 이유는 별도로 조사해야 합니다."}
:::

## 복구 확인 범위 기록하기

보고서에는 복구 후의 관찰 결과와 아직 밝혀지지 않은 영향 범위를 함께 담아야 할 수 있습니다. 롤백 후 홈페이지 검사가 성공하면 검사한 경로가 복구되었다는 근거가 됩니다. 영향을 받은 방문자 수를 추정하려면 실패 구간의 요청 건수나 그에 준하는 관찰 자료가 더 필요합니다.

:::single-choice{#incident-reports-final-application} 두 종류의 증거를 모두 정확하게 설명한 인계 내용은 무엇인가요?

::option[요청 한 건에서 200을 반환했으므로 모든 방문자가 다시 이용할 수 있게 되었습니다.]{#incident-reports-final-application-b explanation="성공한 요청은 검사에 사용한 경로와 시각의 상태만 확인해 줍니다."}
::option[복구 검사를 통과했으므로 실패한 검사는 보고서에서 삭제해야 합니다.]{#incident-reports-final-application-c explanation="앞서 발생한 실패도 사고 증거입니다."}
::option[롤백 후 홈페이지 검사는 성공했으며 영향을 받은 총 요청 건수는 아직 모릅니다.]{#incident-reports-final-application-a .correct explanation="검사로 확인한 복구 결과와 현재 기록에서 알 수 없는 건수를 구분했습니다."}
:::

패킷과 호스트 증거를 살펴보는 연습을 마쳤다면 [SOC 기초 복습](https://labex.io/courses/project-soc-foundations-review)에서 좀 더 긴 실습을 해 보세요.

## 요약

이제 확인한 사실, 아직 모르는 부분, 다음 조치를 포함해 사고를 인계할 수 있습니다.

1. 영향을 받은 경로와 관찰 결과의 시간 순서를 적습니다.
2. 추정한 원인과 확인된 증거를 구분합니다.
3. 어떤 출처와 시간 구간을 조사할지 지정합니다.
