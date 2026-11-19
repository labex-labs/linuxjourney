---
lesson_id: "host-attack-surface"
course_id: "linux-hardening"
lang: "ko"
order_index: 1
title: "공격 표면"
description: "Linux 호스트에서 공개해야 할 항목과 검토가 필요한 접근 경로를 파악하는 방법을 알아봅니다."
meta_title: "공격 표면 - Linux 보안 강화"
meta_description: "Linux 호스트에서 공개해야 할 항목과 검토가 필요한 접근 경로를 파악하는 방법을 알아봅니다."
meta_keywords: "공격 표면, Linux 보안 강화, 사이버 보안, Linux Journey"
---

Linux 호스트에는 공개 웹 페이지, 유지보수용 접속 수단, 백그라운드 서비스가 있을 수 있습니다. 서비스마다 하는 일과 접근해야 하는 대상을 적으세요. 그러면 목적이 불분명한 접근을 찾아낼 수 있습니다.

## 필요한 접근 목록 만들기

간단한 목록을 만들어 각 리소스를 사용해야 하는 사람이나 프로그램을 연결합니다. 아래는 실습용 호스트의 예시입니다.

```text
Resource           Intended access
Public homepage    Visitors
Maintenance SSH    Operations team
Preview panel      Local staff on this host only
```

**접근 경로**는 사용자나 프로그램이 리소스에 도달하는 방법입니다. 외부에서 시스템에 영향을 줄 수 있는 접근 가능한 인터페이스는 **공격 표면**의 일부입니다.

:::single-choice{#host-attack-surface-intended-audience} 이 목록에서 공개 네트워크 경로가 필요한 리소스는 무엇인가요?

::option[유지보수용 SSH입니다.]{#host-attack-surface-intended-audience-b explanation="운영팀이 사용하는 접속 수단입니다."}
::option[공개 홈페이지입니다.]{#host-attack-surface-intended-audience-a .correct explanation="호스트 외부의 방문자도 이용하는 페이지입니다."}
::option[미리 보기 패널입니다.]{#host-attack-surface-intended-audience-c explanation="호스트에서 로컬로 사용하도록 되어 있습니다."}
:::

## 예상한 접근과 실제 접근 비교하기

목록에는 로컬 전용이라고 되어 있는데 네트워크를 통해 미리 보기 패널에 접근할 수 있다고 가정해 보세요. 설정을 바꾸기 전에 담당자에게 확인하고 실제 경로를 검증하세요. 서비스는 계속 실행해야 하더라도 원격 요청을 받을 필요는 없을 수 있습니다.

:::single-choice{#host-attack-surface-mismatch} 명시된 정책에 따라 어떤 관찰 결과를 검토해야 하나요?

::option[방문자가 미리 보기 패널에 접근할 수 있습니다.]{#host-attack-surface-mismatch-b .correct explanation="패널을 사용하도록 정해진 대상 이외에도 접근할 수 있는 경로가 열려 있습니다."}
::option[방문자가 홈페이지를 열 수 있습니다.]{#host-attack-surface-mismatch-a explanation="공개 홈페이지의 용도에 맞는 동작입니다."}
::option[담당자가 호스트에서 로컬로 미리 보기를 열 수 있습니다.]{#host-attack-surface-mismatch-c explanation="로컬 접근은 명시된 요구 사항에 맞습니다."}
:::

## 확인할 항목의 우선순위 정하기

불필요하면서도 영향이 큰 접근부터 살펴보세요. 실습 예시에서는 사이트를 수정할 수 있는 미리 보기 패널이 중요 데이터가 없는 미사용 서비스보다 우선입니다. 사용 대상, 관찰한 노출 범위, 정상적인 사용을 방해하지 않으면서 제한이 적용되었는지 확인할 검사 방법을 기록하세요.

:::single-choice{#host-attack-surface-priority-check} 미리 보기 접근 설정을 바꾼 뒤 어떤 두 가지 결과로 제한이 목표를 달성했는지 확인할 수 있나요?

::option[패널이 여전히 로컬 요청을 받습니다.]{#host-attack-surface-priority-check-a explanation="필수 접근은 확인했지만 의도하지 않은 원격 경로는 아직 검사하지 않았습니다."}
::option[장비를 재부팅했고 호스트 이름이 같습니다.]{#host-attack-surface-priority-check-b explanation="호스트 상태로는 정책대로 접근이 제한되었는지 알 수 없습니다."}
::option[담당자는 여전히 로컬로 접근할 수 있고 의도하지 않은 원격 경로는 닫혔습니다.]{#host-attack-surface-priority-check-c .correct explanation="두 검사로 필요한 접근과 제한을 모두 검증합니다."}
:::

## 요약

이제 어떤 접근 경로에 보안 강화 검토가 필요한지 판단할 수 있습니다.

1. 리소스와 사용 대상을 설명합니다.
2. 의도한 접근과 관찰한 접근을 비교합니다.
3. 변경 후 보호 조치가 적용되었는지와 정상적으로 사용할 수 있는지를 모두 확인합니다.
