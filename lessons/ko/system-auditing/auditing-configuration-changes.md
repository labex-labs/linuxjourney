---
lesson_id: "auditing-configuration-changes"
course_id: "system-auditing"
lang: "ko"
order_index: 5
title: "설정 변경"
description: "승인된 변경, 파일 비교 결과, 감사 이벤트를 함께 살펴보는 방법을 알아봅니다."
meta_title: "설정 변경 - 시스템 감사"
meta_description: "승인된 변경, 파일 비교 결과, 감사 이벤트를 함께 살펴보는 방법을 알아봅니다."
meta_keywords: "설정 변경, 시스템 감사, 사이버 보안, Linux Journey"
---

변경 티켓에는 예정된 작업이 기록됩니다. 파일 비교 결과에는 현재 달라진 부분이 나오고, 감사 이벤트에는 수집 범위에서 관찰된 작업이 나옵니다. 이 세 가지를 함께 보고 설정 변경에 관해 무엇을 확인할 수 있는지 판단하세요.

## 예정된 변경과 대조하기

다음 모의 유지보수 기록을 살펴보세요.

```text
Approved: change banner.txt mode to 640
Window: 09:00–09:30 UTC
Host: web-01
```

어느 파일의 어떤 속성에 대한 변경이 승인되었는지 나옵니다. 같은 시간대에 생겼더라도 다른 변경에는 별도의 설명이 필요합니다.

:::single-choice{#auditing-configuration-changes-approve-scope} 설명된 승인 작업과 일치하는 변경은 무엇인가요?

::option[web-01에서 site.conf의 내용이 바뀌었습니다.]{#auditing-configuration-changes-approve-scope-b explanation="이 설정 파일은 승인 범위에 포함되지 않습니다."}
::option[다른 호스트에서 banner.txt가 사라졌습니다.]{#auditing-configuration-changes-approve-scope-c explanation="작업과 호스트가 모두 기록과 다릅니다."}
::option[web-01에서 banner.txt의 모드가 640으로 바뀌었습니다.]{#auditing-configuration-changes-approve-scope-a .correct explanation="기록에 명시된 파일, 속성, 호스트, 승인된 결과와 모두 일치합니다."}
:::

## 관찰 결과 비교하기

파일 비교 결과에는 배너 파일의 모드가 바뀌었고 `site.conf`의 바이트가 달라졌다고 나옵니다. 별도의 감사 이벤트에는 09:15에 `web-01`의 `site.conf`에 쓰기 작업을 수행했다고 기록되어 있습니다. 감사 이벤트를 보면 어느 시각을 조사할지 알 수 있습니다. 작업이 승인되었는지는 따로 확인해야 합니다.

:::single-choice{#auditing-configuration-changes-source-comparison} site.conf에 관한 두 관찰을 종합하면 어떤 결론을 내릴 수 있나요?

::option[쓰기 시각이 해당 구간에 있으므로 승인된 작업이었습니다.]{#auditing-configuration-changes-source-comparison-a explanation="티켓에는 다른 작업이 적혀 있습니다."}
::option[쓰기 기록이 있고 내용도 달라졌으므로 이 파일을 검토해야 합니다.]{#auditing-configuration-changes-source-comparison-b .correct explanation="파일 비교로 차이를 확인했고 감사 이벤트로 조사할 시각을 좁혔습니다."}
::option[배너 변경 때문에 쓰기 작업이 발생했습니다.]{#auditing-configuration-changes-source-comparison-c explanation="관찰 결과만으로는 두 작업의 인과관계를 확인할 수 없습니다."}
:::

## 검토 내용 남기기

어떤 차이가 계획과 일치하고 어떤 차이가 아직 설명되지 않았는지 적으세요. 파일, 호스트, 시각, 근거 자료도 함께 적습니다. 다음으로 현재 설정을 승인된 사본과 비교하고, 이 변경에 적용되는 별도의 승인이 있는지 확인할 수 있습니다.

:::single-choice{#auditing-configuration-changes-useful-review} 인계할 때 site.conf에 대해 무엇을 적어야 하나요?

::option[변경된 부분과 관찰된 쓰기 작업을 적고, 승인 근거를 요청합니다.]{#auditing-configuration-changes-useful-review-c .correct explanation="확인한 증거와 남은 질문을 함께 전달할 수 있습니다."}
::option[승인됨으로 표시하고 파일 경로를 생략합니다.]{#auditing-configuration-changes-useful-review-a explanation="변경 대상을 알 수 없게 되며 기록에 없는 승인을 가정하게 됩니다."}
::option[배너를 변경한 담당자가 한 작업으로 기록합니다.]{#auditing-configuration-changes-useful-review-b explanation="현재 기록으로는 누가 작업했는지 판단할 수 없습니다."}
:::

## 두 유지보수 기록 비교하기

또 다른 티켓에는 나중에 site.conf를 수정하는 작업이 승인되어 있습니다. 검토를 마치기 전에 관찰 시각, 대상 호스트, 파일을 티켓과 대조하세요. 같은 파일의 변경이 승인되었더라도 그보다 먼저 발생한 이벤트까지 설명하지는 못할 수 있습니다.

:::single-choice{#auditing-configuration-changes-final-application} 티켓은 web-01의 site.conf에 대해 09:40부터 10:00까지를 승인합니다. 09:15에 기록된 쓰기 작업에 관해 무엇을 더 확인해야 하나요?

::option[티켓 시스템 밖에 site.conf가 있는지 확인합니다.]{#auditing-configuration-changes-final-application-b explanation="파일 비교에서 이미 해당 설정 파일을 확인했습니다."}
::option[나중에 발급된 티켓으로 과거의 모든 쓰기 작업을 자동으로 설명할 수 있는지 확인합니다.]{#auditing-configuration-changes-final-application-c explanation="승인은 명시된 작업과 시간에 적용됩니다."}
::option[앞서 발생한 쓰기 작업에 별도의 승인이 있는지 확인합니다.]{#auditing-configuration-changes-final-application-a .correct explanation="호스트와 경로는 일치하지만 기록 시각이 승인된 시간대를 벗어납니다."}
:::

## 요약

이제 설정 변경에 관해 확인된 사실을 정리할 수 있습니다.

1. 승인된 변경에서 의도한 작업 범위를 확인합니다.
2. 파일 비교 결과와 감사 이벤트를 바탕으로 관찰한 내용을 설명합니다.
3. 어떤 증거가 부족한지 설명하고 다음으로 확인할 사항을 정합니다.
