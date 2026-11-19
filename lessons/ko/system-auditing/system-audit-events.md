---
lesson_id: "system-audit-events"
course_id: "system-auditing"
lang: "ko"
order_index: 1
title: "감사 이벤트"
description: "보호된 파일의 변경을 검토할 때 어떤 이벤트를 감사해야 하는지 알아봅니다."
meta_title: "감사 이벤트 - 시스템 감사"
meta_description: "보호된 파일의 변경을 검토할 때 어떤 이벤트를 감사해야 하는지 알아봅니다."
meta_keywords: "감사 이벤트, 시스템 감사, 사이버 보안, Linux Journey"
---

서비스 로그에는 페이지를 열었다는 내용이 기록될 수 있습니다. **감사 레코드**에는 서비스 설정에 쓰는 작업처럼 시스템에서 관찰하도록 구성한 작업이 기록될 수 있습니다. 먼저 어떤 작업이 중요한지, 이를 검토하는 데 어떤 정보가 필요한지 정하세요.

## 감사에서 확인할 사항 정하기

웹 서비스 설정에서 미리 보기를 열 수 있는 사람을 지정한다고 생각해 보세요. 그 설정 파일의 변경을 검토하려면 대상, 작업, 시각, 관련 계정, 결과를 기록하는 것이 좋습니다. 각 필드는 작업의 한 부분을 재구성하는 데 도움이 됩니다.

:::single-choice{#system-audit-events-choose-object} 이 검토를 위해 감사 레코드에서 어떤 항목을 식별할 수 있어야 하나요?

::option[해당 날짜의 웹 요청 수만 알면 됩니다.]{#system-audit-events-choose-object-b explanation="요청량은 별개의 활동에 관한 정보입니다."}
::option[변경의 대상이 된 설정 파일을 식별해야 합니다.]{#system-audit-events-choose-object-a .correct explanation="대상을 알면 이 변경을 다른 곳에 쓰는 작업과 구분할 수 있습니다."}
::option[쓰기와 같은 작업 유형만 알면 됩니다.]{#system-audit-events-choose-object-c explanation="작업 유형은 무엇을 시도했는지 알려 줍니다. 해당 검토와 관련된 작업인지 알려면 대상 파일을 확인해야 합니다."}
:::

## 작업 결과 읽기

레코드에는 성공한 쓰기 또는 실패한 시도가 기록될 수 있습니다. 요청된 작업과 결과를 함께 확인하세요. 거부된 쓰기는 시도가 있었음을 보여 주는 증거가 될 수 있습니다. 쓰기가 성공했을 때와는 해석이 달라집니다.

:::single-choice{#system-audit-events-operation-result} 레코드에 설정 파일 쓰기와 거부 결과가 기록되었습니다. 무엇을 알 수 있나요?

::option[기록된 쓰기 시도가 거부되었습니다.]{#system-audit-events-operation-result-b .correct explanation="작업과 결과를 함께 보면 어떤 일이 관찰되었는지 알 수 있습니다."}
::option[파일이 확실히 교체되었습니다.]{#system-audit-events-operation-result-a explanation="거부 결과는 변경에 성공했다는 근거가 될 수 없습니다."}
::option[예상한 페이지가 HTTP 200을 반환했습니다.]{#system-audit-events-operation-result-c explanation="이 레코드에는 페이지 요청이 나와 있지 않습니다."}
:::

## 감사 범위 확인하기

감사 시스템에는 수집 방식과 정책에서 관찰할 수 있는 이벤트만 기록됩니다. 검색 결과가 비어 있다는 점을 근거로 삼기 전에 정책이 필요한 경로, 작업, 시간대를 포함했는지 확인하세요. 검토한 출처도 기록합니다.

:::single-choice{#system-audit-events-empty-audit} 선택한 로그에 쓰기 기록이 없습니다. 쓰기가 없었다고 결론 내리기 전에 무엇을 확인하면 좋을까요?

::option[설치된 편집기 수를 셉니다.]{#system-audit-events-empty-audit-a explanation="설치된 소프트웨어만으로는 감사 범위를 알 수 없습니다."}
::option[같은 시간대에서 다른 계정 이름 하나만 추가로 검색합니다.]{#system-audit-events-empty-audit-b explanation="수집이 정상적으로 동작한다는 사실을 확인한 뒤에는 추가 검색이 유용할 수 있습니다. 먼저 관련 이벤트가 기록될 수 있었는지 확인하세요."}
::option[감사 정책과 확인 가능한 시간 범위를 검증합니다.]{#system-audit-events-empty-audit-c .correct explanation="감사 범위에 포함되지 않았다면 작업이 발생해도 기록을 찾을 수 없습니다."}
:::

## 요약

이제 보호된 리소스를 검토하는 데 필요한 감사 증거를 고를 수 있습니다.

1. 검토할 작업과 대상을 식별합니다.
2. 요청된 작업과 기록된 결과를 함께 읽습니다.
3. 빈 검색 결과를 증거로 사용하기 전에 감사 범위를 확인합니다.
