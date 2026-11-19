---
lesson_id: "incident-evidence-preservation"
course_id: "incident-response"
lang: "ko"
order_index: 2
title: "증거 보존"
description: "실습 기록과 사본, 체크섬을 나중에 검토할 수 있도록 보존하는 방법을 알아봅니다."
meta_title: "증거 보존 - 사고 대응"
meta_description: "실습 기록과 사본, 체크섬을 나중에 검토할 수 있도록 보존하는 방법을 알아봅니다."
meta_keywords: "증거 보존, 사고 대응, 사이버 보안, Linux Journey"
---

사고에 대응하는 동안 로그 일부를 보면 무슨 일이 있었는지 파악하는 데 도움이 됩니다. 원본 자료나 승인된 내보내기 파일을 보존하고 다른 검토자가 내용을 이해하는 데 필요한 정보도 함께 남기세요.

## 수집 배경 기록하기

호스트, 출처, 시간대, 수집 구간을 적으세요. 누가 기록을 수집했고 어떤 필터를 사용했는지도 남깁니다. 이런 정보가 없으면 다른 장비에서 나온 로그와 내용이 같은 줄을 구분하기 어려울 수 있습니다.

:::single-choice{#incident-evidence-preservation-context-fields} 동료가 시각 09:22만 있고 다른 배경 정보가 없는 로그 한 줄을 받았습니다. 어떤 정보를 추가해야 하나요?

::option[사본을 로컬에 저장한 경로입니다.]{#incident-evidence-preservation-context-fields-b explanation="그 경로로 사본을 찾을 수는 있지만 원본의 출처와 시간 정보는 알 수 없습니다."}
::option[원인에 대한 추측입니다.]{#incident-evidence-preservation-context-fields-c explanation="어떻게 수집했는지와 기록을 어떻게 해석하는지는 구분해 적으세요."}
::option[출처 호스트, 시간대, 수집 구간입니다.]{#incident-evidence-preservation-context-fields-a .correct explanation="검토자가 해당 로그를 올바른 타임라인에 배치할 수 있습니다."}
:::

## 사본과 원본 비교하기

새 실습 폴더에 실습용 로그 한 줄을 저장하고 복사한 뒤 두 파일의 SHA-256 값을 계산하세요. 예시 파일만 사용합니다. 파일에 쓰는 과정에서 이 폴더에 이름이 같은 기존 파일을 덮어씁니다.

```bash
$ printf '%s\n' '09:22 UTC public homepage returned 503' > sample.log
$ cp sample.log review-copy.log
$ sha256sum sample.log review-copy.log
```

첫 번째 열에는 내용 해시가 나옵니다. 두 값은 같아야 합니다. 검사 시점에 사본의 바이트가 원본과 일치하는지 확인할 수 있습니다. 원래 이벤트가 정확히 기록되었는지는 별도로 확인해야 합니다.

:::single-choice{#incident-evidence-preservation-copy-meaning} 해시가 일치한다는 사실은 무엇을 뒷받침하나요?

::option[원본의 타임스탬프가 반드시 정확합니다.]{#incident-evidence-preservation-copy-meaning-a explanation="해시는 파일 내용을 측정합니다. 시계가 정확한지는 검증할 수 없습니다."}
::option[검토용 사본에서 측정한 바이트가 실습용 원본과 같습니다.]{#incident-evidence-preservation-copy-meaning-b .correct explanation="두 해시는 같은 알고리즘으로 계산했습니다."}
::option[이 사본은 공개 공유 승인을 받았습니다.]{#incident-evidence-preservation-copy-meaning-c explanation="공유 승인은 파일을 누가 볼 수 있는지에 관한 결정입니다."}
:::

![실습 파일과 검토용 사본의 해시가 일치함을 보여 주는 LabEx 체크섬 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/incident-response/incident-evidence-preservation/matching-copy-hashes.png)

## 공유할 검토용 사본 준비하기

원본 기록은 그대로 보존하고 접근을 제한하세요. 다른 팀에 몇 가지 필드만 필요하다면 별도로 발췌본을 만들고 그 사본에서 민감한 정보를 제거하세요. 내용을 줄였다는 사실을 기록하고 보호된 원본에 대한 참조를 남기세요.

:::single-choice{#incident-evidence-preservation-redact-copy} 공유하기 위해 어느 파일에서 민감한 정보를 가려야 하나요?

::option[별도의 검토용 발췌본입니다.]{#incident-evidence-preservation-redact-copy-c .correct explanation="원본을 보존하면서 공유 자료의 범위를 줄일 수 있습니다."}
::option[모든 사본이 바뀌도록 보호된 원본을 수정합니다.]{#incident-evidence-preservation-redact-copy-a explanation="이렇게 하면 보존해야 할 증거가 달라집니다."}
::option[파일을 수정해도 같은 값처럼 보이도록 체크섬을 수정합니다.]{#incident-evidence-preservation-redact-copy-b explanation="측정값과 해당 파일은 그대로 보관하세요."}
:::

## 요약

이제 다른 검토자가 해석할 수 있도록 증거를 준비할 수 있습니다.

1. 어디에서 언제 자료를 수집했는지 기록합니다.
2. 사본의 바이트가 원본과 일치하는지 확인합니다.
3. 공유할 때 별도의 발췌본에서 민감한 정보를 제거합니다.
