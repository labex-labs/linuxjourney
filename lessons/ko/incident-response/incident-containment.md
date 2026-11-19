---
lesson_id: "incident-containment"
course_id: "incident-response"
lang: "ko"
order_index: 4
title: "확산 방지"
description: "승인된 확산 방지 조치를 목적, 영향, 보존할 증거에 따라 비교하는 방법을 알아봅니다."
meta_title: "확산 방지 - 사고 대응"
meta_description: "승인된 확산 방지 조치를 목적, 영향, 보존할 증거에 따라 비교하는 방법을 알아봅니다."
meta_keywords: "확산 방지, 사고 대응, 사이버 보안, Linux Journey"
---

**확산 방지**는 팀이 사고를 조사하는 동안 추가 피해를 줄이기 위한 단기 조치입니다. 적절한 조치는 영향을 받은 대상과 계속 허용해야 하는 접근에 따라 달라집니다.

## 제한 범위 정하기

공개 경로로 내부 미리 보기 패널에 접근할 수 있고, 홈페이지는 계속 열어 두어야 한다고 가정해 보세요. 미리 보기 경로만 제한할 수도 있고, 사이트 전체를 오프라인으로 전환할 수도 있습니다. 각각 어떤 동작에 영향을 주는지 비교하세요.

:::single-choice{#incident-containment-narrow-action} 홈페이지는 계속 열어 두면서 공개 미리 보기 접근을 차단하려면 어떤 방법이 가장 적절한가요?

::option[용도에 관계없이 모든 공개 경로를 비활성화합니다.]{#incident-containment-narrow-action-b explanation="이렇게 하면 홈페이지도 닫힙니다."}
::option[문제가 있는 미리 보기 경로를 제한하고 두 경로를 모두 확인합니다.]{#incident-containment-narrow-action-a .correct explanation="보고된 노출 문제에 대응하면서 필요한 서비스가 계속 제공되는지 확인합니다."}
::option[미리 보기 서비스의 이름을 바꿉니다.]{#incident-containment-narrow-action-c explanation="이름을 바꿔도 요청이 서비스에 도달하는 것은 막을 수 없습니다."}
:::

## 증거 보존과 접근 계획하기

대응 계획을 확인하고 변경 권한이 있는 사람과 상의하세요. 승인자와 조치를 유지할 기간을 기록하고, 상황이 허락하면 먼저 보존해야 할 증거도 적으세요. 조치로 인해 서비스 로그 수집이나 대응 담당자의 접근이 중단될 수 있는지 고려하세요.

:::single-choice{#incident-containment-action-impact} 격리 조치를 적용하면 조사 담당자가 기록을 가져오는 데도 문제가 생길 수 있습니다. 팀에서 무엇을 검토해야 하나요?

::option[어떤 증거를 보존하고 승인된 대응 담당자의 접근을 어떻게 유지할지 검토합니다.]{#incident-containment-action-impact-b .correct explanation="확산 방지와 조사에 필요한 사항을 모두 고려할 수 있습니다."}
::option[설정 파일 이름이 짧은지만 검토합니다.]{#incident-containment-action-impact-a explanation="파일 이름을 확인해도 기록을 보존하거나 접근을 유지할 수 없습니다."}
::option[누구나 다시 접속할 수 있도록 자격 증명을 공개할지 검토합니다.]{#incident-containment-action-impact-c explanation="자격 증명은 보호하고 접근은 계속 통제해야 합니다."}
:::

## 확산 방지 조치 검증하기

의도하지 않은 경로가 닫혔는지 확인하세요. 정상적으로 열려 있어야 할 경로를 별도로 검사해 부작용이 있는지 파악합니다. 조치를 적용한 시각과 팀이 다시 검토할 시각을 기록하세요. 추가 피해를 막았더라도 근본 원인은 여전히 조사 중일 수 있습니다.

:::single-choice{#incident-containment-containment-success} 공개 미리 보기 경로는 닫혔고 홈페이지는 계속 동작합니다. 무엇을 확인했다고 말할 수 있나요?

::option[근본 원인을 확실히 해결했습니다.]{#incident-containment-containment-success-a explanation="이 검사에서는 접근 범위만 확인했습니다. 근본 원인을 해결했는지는 별도로 확인해야 합니다."}
::option[미리 보기에 접근할 수 있는 모든 경로를 검사했습니다.]{#incident-containment-containment-success-b explanation="검사에서 사용한 특정 경로에 해당하는 결과입니다."}
::option[검사한 공개 미리 보기 경로는 차단되었고 필요한 홈페이지는 계속 이용할 수 있습니다.]{#incident-containment-containment-success-c .correct explanation="검증한 범위 안에서 결과를 설명했습니다."}
:::

## 요약

이제 단기 확산 방지 조치를 평가할 수 있습니다.

1. 제한해야 할 경로나 접근 방식을 명시합니다.
2. 승인 여부, 보존할 증거, 예상 영향을 확인합니다.
3. 의도한 제한과 필수 서비스의 동작을 각각 검증합니다.
