---
lesson_id: "deployment-records"
course_id: "deployment"
lang: "ko"
order_index: 6
title: "배포 기록"
description: "짧은 릴리스 타임라인을 읽고 배포와 롤백 과정을 재구성하는 방법을 알아봅니다."
meta_title: "배포 기록 - 배포"
meta_description: "짧은 릴리스 타임라인을 읽고 배포와 롤백 과정을 재구성하는 방법을 알아봅니다."
meta_keywords: "배포 기록, 배포, DevOps, Linux Journey"
---

배포 기록을 남기면 다른 사람이 사용자에게 나타난 결과와 변경 사항을 연결해 볼 수 있습니다. 시간, 환경, 소스 리비전, 아티팩트부터 적으세요. 검사 결과와 이후에 취한 조치도 추가합니다.

## 변경 사항 명시하기

이 실습 기록은 한 차례의 배포 과정을 보여 줍니다. 쉽게 읽을 수 있도록 식별자를 줄여 표기했습니다.

```text
UTC    Target   Commit   Artifact  Observation
09:00  staging  8a61e1   digest-C  version 3, home returned 200
09:12  prod     8a61e1   digest-C  version 3, home returned 503
09:18  prod     72b110   digest-B  version 2, home returned 200
```

HTTP 200은 요청이 성공했음을 나타냅니다. HTTP 503은 해당 요청을 처리할 때 서비스를 이용할 수 없었음을 나타냅니다. 실제로 기록할 때는 검사 방법과 주소도 결과와 함께 남기세요.

:::single-choice{#deployment-records-first-prod-change} 운영 환경에서 digest-C의 동작을 처음 확인한 행은 무엇인가요?

::option[09:12 prod 행입니다.]{#deployment-records-first-prod-change-b .correct explanation="이 행에는 운영 환경에 배포하려던 버전과 검사 실패가 나옵니다."}
::option[09:00 staging 행입니다.]{#deployment-records-first-prod-change-a explanation="이 검사는 다른 환경에서 실행했습니다."}
::option[09:18 prod 행입니다.]{#deployment-records-first-prod-change-c explanation="이 행은 롤백 후의 다른 아티팩트를 기록한 것입니다."}
:::

![스테이징 성공, 운영 환경의 503 응답, 버전 2로의 롤백을 보여 주는 모의 릴리스 타임라인](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/deployment/deployment-records/release-timeline.png)

## 롤백 설명하기

마지막 행은 digest-B로 돌아갔음을 보여 줍니다. 버전 검사와 홈페이지 응답은 롤백 후의 결과를 나타냅니다. 앞서 실패한 구체적인 원인까지 알 수는 없습니다. 뒷받침할 증거를 찾을 때까지 가설은 관찰 결과와 구분해 두세요.

:::single-choice{#deployment-records-rollback-evidence} 09:18의 결과로 무엇을 알 수 있나요?

::option[09:12의 실패는 데이터베이스가 없어서 발생했습니다.]{#deployment-records-rollback-evidence-b explanation="이 기록에는 의존 서비스에 관한 증거가 없습니다."}
::option[그 이후 모든 요청이 성공했습니다.]{#deployment-records-rollback-evidence-c explanation="검사 한 번의 성공은 해당 요청에 관한 증거입니다."}
::option[운영 환경이 버전 2로 돌아갔고 해당 홈페이지 요청이 성공했습니다.]{#deployment-records-rollback-evidence-a .correct explanation="이 행에는 복구한 버전과 실제로 받은 HTTP 응답이 나옵니다."}
:::

## 기록 인계하기

이후에 검토하는 사람도 같은 범위에서 검사할 수 있어야 합니다. 측정 방법, 시간대를 포함한 타임스탬프와, 가능하다면 아티팩트를 생성한 빌드의 링크를 남기세요. 원인을 아직 모른다면 다음으로 확인할 사항을 적습니다.

:::single-choice{#deployment-records-handoff-detail} 다음 담당자가 같은 홈페이지 검사를 수행하려면 어떤 정보가 필요할까요?

::option[이전 릴리스의 식별자만 알면 됩니다.]{#deployment-records-handoff-detail-a explanation="이전 버전은 비교에 도움이 되지만 검사를 어디에서 언제 실행했는지는 알려 주지 않습니다."}
::option[검사에 사용한 정확한 대상 주소와 검사 시각입니다.]{#deployment-records-handoff-detail-c .correct explanation="같은 경로를 확인하고 해당 시간대의 다른 신호와 비교할 수 있습니다."}
::option[소스 커밋을 생성한 시각입니다.]{#deployment-records-handoff-detail-b explanation="커밋 시각은 앞선 이벤트에 해당합니다. 검토자에게는 검사 시각과 대상 주소가 필요합니다."}
:::

## 실제로 실행한 아티팩트 기록하기

배포 기록에 적은 태그가 릴리스 이후 다른 이미지를 가리킬 수 있습니다. 서비스가 이미 버전 2를 보고한다면 알아보기 쉬운 태그와 함께 실제 실행 중인 아티팩트의 식별자도 기록하세요. 두 값을 남겨 두면 레지스트리의 태그가 바뀌더라도 나중에 릴리스와 비교할 수 있습니다.

:::single-choice{#deployment-records-final-application} 릴리스 노트에 site:2가 적혀 있습니다. 나중에 더 정확히 비교하려면 무엇을 추가해야 하나요?

::option[site:2를 가장 최근에 내려받은 사람이 확인한 다이제스트입니다.]{#deployment-records-final-application-c explanation="나중에 이미지를 내려받으면 실행 중인 서비스와 다른 내용을 받을 수 있습니다."}
::option[실제로 실행한 이미지의 전체 다이제스트입니다.]{#deployment-records-final-application-a .correct explanation="나중에 태그가 다른 이미지를 가리키더라도 배포에 사용한 이미지의 내용을 식별할 수 있습니다."}
::option[알아보기 쉬운 태그를 다른 필드에 한 번 더 적습니다.]{#deployment-records-final-application-b explanation="같은 태그를 반복해도 어느 이미지를 실행했는지 알 수 없습니다."}
:::

## 요약

이제 릴리스 타임라인을 읽고 다른 담당자에게 인계할 수 있습니다.

1. 배포 기록에서 환경, 리비전, 아티팩트를 파악합니다.
2. 관찰한 결과를 바탕으로 롤백을 설명합니다.
3. 다음 검사에 필요한 세부 정보를 남깁니다.
