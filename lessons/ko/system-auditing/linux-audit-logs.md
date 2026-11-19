---
lesson_id: "linux-audit-logs"
course_id: "system-auditing"
lang: "ko"
order_index: 2
title: "Linux 감사 로그"
description: "기록된 작업 하나를 설명하는 Linux 감사 레코드를 묶어 읽는 방법을 알아봅니다."
meta_title: "Linux 감사 로그 - 시스템 감사"
meta_description: "기록된 작업 하나를 설명하는 Linux 감사 레코드를 묶어 읽는 방법을 알아봅니다."
meta_keywords: "Linux 감사 로그, 시스템 감사, 사이버 보안, Linux Journey"
---

Linux Audit은 이벤트 하나에 여러 레코드를 남길 수 있습니다. 한 행에는 작업이 나오고 다른 행에는 경로가 나올 수 있습니다. 어떤 작업이 있었는지 판단하기 전에 관련 행을 묶어서 확인하세요.

## 같은 이벤트에 속한 기록 읽기

다음은 같은 호스트에서 같은 날짜에 남긴 실습용 레코드의 일부입니다. 감사 이벤트 참조에서 콜론 뒤에 있는 번호는 타임스탬프와 이벤트 ID가 같은 레코드를 묶는 데 쓰입니다. 아래 행들은 같은 이벤트에 속합니다.

```text
type=SYSCALL msg=audit(1763456400.120:42) success=yes auid=1001 euid=0
type=PATH    msg=audit(1763456400.120:42) name="/etc/journey/site.conf"
```

첫 번째 행에는 작업 결과와 계정 관련 필드가 나옵니다. 경로가 있는 행에는 이벤트와 관련된 파일이 표시됩니다.

:::single-choice{#linux-audit-logs-group-rows} 이 예시에서 어떤 필드로 작업과 경로를 연결할 수 있나요?

::option[SYSCALL과 PATH라는 두 레코드 유형만 확인합니다.]{#linux-audit-logs-group-rows-a explanation="유형은 각 행의 역할을 나타냅니다. 여러 이벤트에서 같은 유형을 쓸 수 있습니다."}
::option[두 행이 모두 type으로 시작한다는 점을 확인합니다.]{#linux-audit-logs-group-rows-c explanation="모든 행에 유형이 있어도 서로 다른 이벤트일 수 있습니다."}
::option[같은 호스트에서 일치하는 감사 이벤트 참조를 확인합니다.]{#linux-audit-logs-group-rows-b .correct explanation="이 참조는 이벤트 42에 해당하는 행을 묶어 줍니다."}
:::

![같은 감사 이벤트 참조를 가진 모의 Linux Audit SYSCALL 및 PATH 행](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/linux-audit-logs/grouped-event.png)

## 두 사용자 ID 읽기

이 예시에서 `auid`는 감사 로그인 사용자 ID이고, `euid`는 작업에 사용된 유효 사용자 ID입니다. 프로그램은 로그인 계정과 다른 유효 사용자 ID로 실행될 수 있습니다. 숫자 ID는 호스트의 계정을 식별합니다. 실제로 누가 작업했는지 알려면 추가 기록이 필요할 수 있습니다.

:::single-choice{#linux-audit-logs-identify-login} 이 예시에서 감사 로그인 사용자 ID를 보여 주는 필드는 무엇인가요?

::option[euid 0입니다.]{#linux-audit-logs-identify-login-b explanation="이 이벤트에서 프로그램이 사용한 유효 사용자 ID입니다."}
::option[auid 1001입니다.]{#linux-audit-logs-identify-login-a .correct explanation="auid는 감사 로그인 사용자 ID이며 euid는 유효 사용자 ID입니다."}
::option[이벤트 번호 42입니다.]{#linux-audit-logs-identify-login-c explanation="이 번호는 레코드를 묶는 데 쓰이며 계정 ID와는 별개입니다."}
:::

## 기록이 뒷받침하는 사실만 판단하기

결과 필드는 기록된 작업이 성공했음을 보여 줍니다. 어떤 작업이었는지 알려면 이벤트 전체를 살펴보세요. 파일 내용이 달라졌는지 확인하려면 알려진 기준과 파일을 비교하세요.

:::single-choice{#linux-audit-logs-useful-follow-up} 파일 내용이 승인된 파일과 다른지 판단하는 데 무엇이 도움이 되나요?

::option[승인된 사본이나 무결성 기록과 비교합니다.]{#linux-audit-logs-useful-follow-up-c .correct explanation="이 증거를 통해 파일 수준에서 무엇이 달라졌는지 확인할 수 있습니다."}
::option[다른 작업이 성공한 두 번째 감사 항목을 봅니다.]{#linux-audit-logs-useful-follow-up-a explanation="다른 작업이 기록되었다는 사실을 확인할 수 있습니다. 현재 파일의 바이트와 승인된 사본은 별도로 비교해야 합니다."}
::option[같은 이벤트에서 로그인 계정 ID를 봅니다.]{#linux-audit-logs-useful-follow-up-b explanation="로그인 ID로 해당 작업의 계정 정보를 파악할 수 있습니다. 파일 바이트의 변경 여부는 알 수 없습니다."}
:::

## 요약

이제 관련 레코드를 묶어 하나의 감사 이벤트를 읽을 수 있습니다.

1. 호스트와 감사 이벤트 참조가 같은 레코드를 찾습니다.
2. 로그인 사용자 ID와 유효 사용자 ID를 구분해 읽습니다.
3. 기록된 결과만으로 알 수 없는 사항은 다음에 무엇을 확인할지 정합니다.
