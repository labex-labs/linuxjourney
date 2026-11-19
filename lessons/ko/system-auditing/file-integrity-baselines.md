---
lesson_id: "file-integrity-baselines"
course_id: "system-auditing"
lang: "ko"
order_index: 4
title: "무결성 기준선"
description: "무결성 보고서를 해석하고 언제 새 기준선을 승인할지 판단하는 방법을 알아봅니다."
meta_title: "무결성 기준선 - 시스템 감사"
meta_description: "무결성 보고서를 해석하고 언제 새 기준선을 승인할지 판단하는 방법을 알아봅니다."
meta_keywords: "무결성 기준선, 시스템 감사, 사이버 보안, Linux Journey"
---

**기준선**은 특정 시점에 파일이 어떤 속성을 가져야 하는지 담은 신뢰할 수 있는 기록입니다. 나중에 무결성을 검사할 때 현재 파일을 기준선과 비교해 차이를 보고할 수 있습니다.

## 비교 보고서 읽기

다음은 호스트를 마지막으로 승인된 상태와 비교한 모의 보고서의 일부입니다.

```text
File                      Property  Previous  Current
/etc/journey/site.conf    content   hash-A    hash-B
/etc/journey/banner.txt   mode      644       640
/etc/journey/site.prev    present   yes       no
```

첫 번째 행에는 파일의 바이트가 바뀌었다고 나옵니다. 두 번째 행에는 접근 권한이 바뀌었고, 세 번째 행에는 이전에 추적하던 파일이 검사 당시 없었다고 나옵니다.

:::single-choice{#file-integrity-baselines-report-mode} 어느 행에서 접근 권한이 바뀌었나요?

::option[site.conf 행입니다.]{#file-integrity-baselines-report-mode-a explanation="이 행에는 내용 해시가 바뀌었다고 나옵니다."}
::option[banner.txt 행입니다.]{#file-integrity-baselines-report-mode-b .correct explanation="모드가 644에서 640으로 바뀌었습니다."}
::option[site.prev 행입니다.]{#file-integrity-baselines-report-mode-c explanation="이 행은 해당 경로의 존재 여부를 기록합니다."}
:::

![파일 내용, 접근 모드, 존재 여부를 비교하는 모의 무결성 보고서](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/file-integrity-baselines/reference-comparison.png)

## 비교 기준 확인하기

이전 기준을 신뢰할 수 있어야 보고서를 활용할 수 있습니다. 기준의 식별자와 생성 날짜를 남기세요. 이미 문제가 발생한 상태에서 파일을 기록했다면 나중에 비교 결과를 잘못 해석할 수 있습니다. 해당 기준선이 어느 시점의 승인된 상태를 나타내는지 확인하세요.

:::single-choice{#file-integrity-baselines-reference-source} 오늘의 설정을 검토하는 데 어떤 기준선이 가장 유용한가요?

::option[변경 전에 기록하고 승인한 사본입니다.]{#file-integrity-baselines-reference-source-a .correct explanation="검토자가 검증할 수 있는 기준을 제공합니다."}
::option[아직 변경 이유를 모르는 오늘의 파일로 만든 기준선입니다.]{#file-integrity-baselines-reference-source-b explanation="검토하기도 전에 차이가 새 기준에 반영됩니다."}
::option[비교할 상황 설명 없이 관련 없는 호스트에서 가져온 설정입니다.]{#file-integrity-baselines-reference-source-c explanation="호스트의 역할에 따라 필요한 파일과 권한이 다를 수 있습니다."}
:::

## 기준선을 갱신하기 전에 검토하기

각 차이를 승인된 변경과 비교하고 서비스가 의도대로 동작하는지 검증하세요. 배너 파일의 모드 변경은 예정되어 있었지만 설정 변경은 예정되어 있지 않았다면 각각 검토합니다. 승인된 차이의 내용을 파악하고 검토를 마친 뒤 기준을 갱신하세요. 이전 기준의 기록도 보관합니다.

:::single-choice{#file-integrity-baselines-update-timing} 배너 파일의 모드 변경은 승인되었고 site.conf가 바뀐 이유는 아직 모릅니다. 새 기준선을 받아들이기 전에 무엇을 해야 하나요?

::option[한 행이 예상대로 바뀌었으므로 모든 차이를 승인합니다.]{#file-integrity-baselines-update-timing-a explanation="파일별 차이는 서로 별개의 변경입니다."}
::option[비교 보고서를 버립니다.]{#file-integrity-baselines-update-timing-b explanation="보고서에는 아직 검토해야 할 차이가 기록되어 있습니다."}
::option[설명되지 않은 site.conf 변경을 조사합니다.]{#file-integrity-baselines-update-timing-c .correct explanation="현재 상태를 검토한 뒤 새 기준선을 승인해야 합니다."}
:::

실습 환경에서 무결성 기준을 만들고 비교하려면 [파일 무결성 모니터링](https://labex.io/tutorials/linux-file-integrity-monitoring-fim-656122)을 해 보세요.

## 요약

이제 특정 비교의 근거로 기준선을 활용할 수 있습니다.

1. 보고서에서 내용, 모드, 존재 여부를 구분합니다.
2. 비교 기준이 신뢰할 수 있는 상태를 나타내는지 확인합니다.
3. 새 기준을 받아들이기 전에 예상치 못한 차이를 검토합니다.
