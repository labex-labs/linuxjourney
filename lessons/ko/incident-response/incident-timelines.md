---
lesson_id: "incident-timelines"
course_id: "incident-response"
lang: "ko"
order_index: 3
title: "사고 타임라인"
description: "증거를 하나의 타임라인에 배치하고 시각이 확실하지 않은 이벤트를 표시하는 방법을 알아봅니다."
meta_title: "사고 타임라인 - 사고 대응"
meta_description: "증거를 하나의 타임라인에 배치하고 시각이 확실하지 않은 이벤트를 표시하는 방법을 알아봅니다."
meta_keywords: "사고 타임라인, 사고 대응, 사이버 보안, Linux Journey"
---

사고 타임라인은 여러 출처의 관찰 결과를 시간순으로 정리한 것입니다. 공통 시간대를 사용하고 원래의 타임스탬프도 기록에 남기세요. 사건의 순서를 정리하면 어떤 일이 서로 관련되어 있을지 살펴볼 수 있습니다.

## 타임스탬프 하나 변환하기

이 예시에서 웹 보고서는 UTC를 사용하고, 배포 기록은 UTC보다 두 시간 빠른 오프셋을 사용합니다.

```text
Deployment record:  2026-11-19 11:17:00 +02:00
Web report:         2026-11-19 09:22:00 UTC
```

GNU date가 있는 Linux에서 `-d`는 지정한 타임스탬프를 읽고 `-u`는 UTC로 출력하도록 지정합니다. `+`로 시작하는 인수는 표시 형식을 정합니다.

```bash
$ date -u -d '2026-11-19 11:17:00+02:00' '+%Y-%m-%d %H:%M:%S UTC'
```

결과는 `2026-11-19 09:17:00 UTC`입니다. 이 예시에서는 웹 보고보다 5분 앞섭니다.

:::single-choice{#incident-timelines-earlier-event} 같은 시간대로 변환한 타임라인에서 어느 항목이 먼저 발생했나요?

::option[배포 기록입니다.]{#incident-timelines-earlier-event-a .correct explanation="오프셋을 변환하면 09:17 UTC가 되므로 09:22에 작성된 보고보다 앞섭니다."}
::option[웹 보고서입니다.]{#incident-timelines-earlier-event-b explanation="변환 전에는 시간대가 달라 시를 나타내는 숫자가 더 작아 보입니다."}
::option[정확히 같은 시각에 발생했습니다.]{#incident-timelines-earlier-event-c explanation="같은 시간대로 바꾼 두 시각은 5분 차이가 납니다."}
:::

![오프셋 +02:00의 11:17을 09:17 UTC로 변환한 GNU date 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-timelines/normalize-utc.png)

## 관찰값과 추정값 구분하기

보고서에 첫 실패가 09:19쯤 발생했다고 적힐 수 있습니다. 이 시각은 추정값으로 남겨 두세요. 사용자가 보고한 시각과 실제 첫 요청이 실패한 시각은 서로 다른 정보입니다. 각 행에 출처와 시각의 정밀도를 표시하세요.

:::single-choice{#incident-timelines-estimated-time} 팀원이 09:19쯤이라고 말합니다. 이 시각을 어떻게 기록해야 하나요?

::option[로그로 확인된 정확한 시각인 09:19:00으로 기록합니다.]{#incident-timelines-estimated-time-a explanation="출처가 제공한 것은 추정 시각입니다."}
::option[출처 없는 이벤트로 기록합니다.]{#incident-timelines-estimated-time-c explanation="시각을 얼마나 신뢰할 수 있는지 판단하려면 출처가 필요합니다."}
::option[해당 보고에서 나온 대략적인 시각으로 기록합니다.]{#incident-timelines-estimated-time-b .correct explanation="출처에서 말한 내용과 시각의 정밀도를 모두 보존합니다."}
:::

## 시간순으로 정리하고 원인은 별도로 확인하기

배포가 서비스 문제보다 앞서 발생했다고 해서 배포가 원인이라고 볼 수는 없습니다. 영향을 받은 경로에 변경이 있었는지, 관련성을 뒷받침하는 다른 신호가 있는지 확인하세요. 아직 확인할 내용은 타임라인과 함께 기록합니다.

:::single-choice{#incident-timelines-timeline-cause} 시간순으로 나열한 기록만으로 무엇을 알 수 있나요?

::option[배포가 공개 경로의 장애를 일으켰습니다.]{#incident-timelines-timeline-cause-a explanation="순서로 가능성을 짐작할 수 있지만 원인을 확정할 수는 없습니다."}
::option[기록에 따르면 배포가 웹 보고보다 앞섰습니다.]{#incident-timelines-timeline-cause-c .correct explanation="기록으로 확인할 수 있는 시간 관계입니다."}
::option[그 밖의 이벤트는 아무 관련이 없습니다.]{#incident-timelines-timeline-cause-b explanation="타임라인에는 선택한 관찰 결과만 들어 있습니다."}
:::

## 요약

이제 증거와 불확실한 부분을 함께 표시한 타임라인을 만들 수 있습니다.

1. 기록된 시각을 일관된 시간대로 변환합니다.
2. 각 시각의 출처를 적고 추정 시각을 표시합니다.
3. 시간 순서를 바탕으로 다음에 확인할 사항을 선택합니다.
