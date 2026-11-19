---
lesson_id: "incident-recovery"
course_id: "incident-response"
lang: "ko"
order_index: 5
title: "복구"
description: "복구 완료를 선언하기 전에 서비스가 승인된 상태인지 검증하는 방법을 알아봅니다."
meta_title: "복구 - 사고 대응"
meta_description: "복구 완료를 선언하기 전에 서비스가 승인된 상태인지 검증하는 방법을 알아봅니다."
meta_keywords: "복구, 사고 대응, 사이버 보안, Linux Journey"
---

**복구**는 서비스를 기대한 상태로 되돌리고 계속 이용할 수 있는지 확인하는 과정입니다. 프로세스가 새로 시작되었다는 것은 초기 신호입니다. 설정, 의존 서비스, 사용자가 경험하는 동작도 의도한 상태와 일치하는지 확인해야 합니다.

## 복구된 상태 확인하기

승인된 복구 후보 버전과 설정을 기록하세요. 서비스를 격리했다면 어떤 접근을 계속 제한해야 하는지 확인하세요. 경로를 다시 열면 확산 방지 범위가 달라질 수 있습니다.

:::single-choice{#incident-recovery-restore-target} 의도한 버전으로 복구했는지 알려 주는 결과는 무엇인가요?

::option[관련 없는 VM에 새로 기록된 타임스탬프입니다.]{#incident-recovery-restore-target-b explanation="그 타임스탬프로는 복구한 서비스를 식별할 수 없습니다."}
::option[설치 가능한 패키지 목록만 확인합니다.]{#incident-recovery-restore-target-c explanation="설치 가능한 목록을 봐도 현재 어떤 버전이 요청을 처리하고 있는지 알 수 없습니다."}
::option[대상에서 승인된 버전을 확인할 수 있는 응답이나 배포 기록입니다.]{#incident-recovery-restore-target-a .correct explanation="실행 중인 서비스와 팀이 선택한 버전을 연결해 줍니다."}
:::

## 보고된 문제 다시 검사하기

모의 사고에서 방문자는 공개 홈페이지에서 `503`을 받았습니다. 복구 후에는 적절한 테스트 위치에서 같은 경로에 요청을 보내세요. 예상한 성공 응답이 오는지 확인하고 최근 요청 오류도 살펴보세요. 내부 미리 보기가 성공해도 공개 경로는 별도로 검사해야 합니다.

:::single-choice{#incident-recovery-verify-original-path} 처음 사용자에게 나타난 증상이 사라졌다는 것을 가장 잘 보여 주는 검사는 무엇인가요?

::option[서비스 실행 파일이 있는지만 확인합니다.]{#incident-recovery-verify-original-path-a explanation="파일이 있어도 공개 요청을 처리하고 있는지는 알 수 없습니다."}
::option[사용자가 이용하는 경로에서 공개 홈페이지를 확인합니다.]{#incident-recovery-verify-original-path-b .correct explanation="처음 실패했던 검사를 다시 수행하는 것입니다."}
::option[내부 미리 보기만 검사합니다.]{#incident-recovery-verify-original-path-c explanation="해당 경로는 영향을 받은 경로와 다릅니다."}
:::

## 관찰 계속하기

짧은 관찰 기간과 성공 기준을 합의하세요. 오류, 지연 시간, 접근 거부 등 관련 신호를 검토하세요. 확인 범위의 한계, 남은 조치, 다음 검토 시각을 기록합니다. 복구 증거는 사고 기록과 함께 보관하세요.

:::single-choice{#incident-recovery-observation-period} 초기 검사를 통과했지만 문제가 간헐적으로 발생했습니다. 복구 검사를 마치기 전에 무엇을 해야 하나요?

::option[정한 관찰 기간 동안 합의한 신호를 계속 확인합니다.]{#incident-recovery-observation-period-c .correct explanation="복구한 동작이 유지된다는 근거를 확보할 수 있습니다."}
::option[응답 한 건이 도착했으므로 즉시 완료로 처리합니다.]{#incident-recovery-observation-period-a explanation="한 번만 확인하면 간헐적인 문제를 놓칠 수 있습니다."}
::option[비교 자료를 모두 버립니다.]{#incident-recovery-observation-period-b explanation="이전 결과와 비교하면 무엇이 개선되었는지 알 수 있습니다."}
:::

## 요약

이제 복구 후 서비스 상태와 사용자에게 보이는 동작을 확인할 수 있습니다.

1. 승인된 버전과 설정을 확인합니다.
2. 사용자에게 나타난 증상을 다시 검사합니다.
3. 복구 검사를 마치기 전에 합의한 신호를 관찰합니다.
