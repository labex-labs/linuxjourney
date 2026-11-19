---
lesson_id: "security-event-correlation"
course_id: "security-logs"
lang: "ko"
order_index: 5
title: "이벤트 상관관계"
description: "시각, 호스트, 계정과 세션 정보를 이용해 보안 기록을 서로 연결하는 방법을 배웁니다."
meta_title: "이벤트 상관관계 - 보안 로그"
meta_description: "SSH와 sudo 기록의 시각을 맞추고 어떤 증거가 이벤트 사이의 관계를 뒷받침하는지 판단합니다."
meta_keywords: "이벤트 상관관계, 보안 로그, SSH 로그인 기록, sudo 이벤트, 타임스탬프, 세션 ID"
---

어떤 기록은 누군가 컴퓨터에 로그인했다고 알려 줍니다. 다른 기록에는 명령어 실행이 허용됐다고 나옵니다. 두 기록은 서로 관련이 있을까요? **이벤트 상관 분석**은 여러 기록을 비교해 관련 활동인지 알아보는 작업입니다.

## 두 기록 읽기

SSH를 사용하면 다른 컴퓨터에 로그인할 수 있습니다. 로그인한 뒤 `sudo`로 다른 계정에서 명령어를 실행할 권한을 요청할 수 있습니다. 다음 두 모의 기록은 같은 날에 작성됐으며 연습하기 쉽게 필드 이름을 맞췄습니다. 실제 로그는 필드 이름이 다르거나 일부를 생략할 수 있습니다.

```text
t=09:14:02Z      source=ssh   host=web-01 account=alex session=42 login=accepted
t=11:15:10+02:00 source=sudo  host=web-01 account=alex session=42 decision=allowed
```

`source`는 이벤트를 보고한 도구이고 `host`는 이벤트가 일어난 컴퓨터입니다. 두 기록 모두 `alex` 계정의 활동을 보고합니다. 실제로 그 계정을 사용한 사람이 누구인지는 다른 증거가 필요합니다.

:::single-choice{#security-event-correlation-account-evidence} 동료가 Alex 본인이 sudo를 요청했다고 말합니다. 지금 기록으로 무엇을 확인할 수 있나요?

::option[Alex 본인이 sudo를 요청했다.]{#security-event-correlation-account-person explanation="계정 이름만으로는 실제 사용자를 식별할 수 없습니다."}
::option[두 기록은 서로 다른 계정의 활동을 보여 준다.]{#security-event-correlation-account-different explanation="account는 둘 다 alex입니다. source가 다른 것은 활동을 보고한 도구가 다르기 때문입니다."}
::option[이벤트 두 건에서 같은 계정이 나온다.]{#security-event-correlation-account-shared .correct explanation="둘 다 alex를 가리킵니다. 누가 계정을 사용했는지 알려면 추가 증거가 필요합니다."}
:::

## 이벤트 시각 비교하기

`t`에는 기록 시각이 들어 있습니다. 첫 번째 기록의 `Z`는 시각을 비교할 때 기준으로 삼는 UTC를 뜻합니다. 두 번째의 `+02:00`은 표시 시각이 UTC보다 두 시간 빠르다는 뜻입니다. `11:15:10`에서 두 시간을 빼면 UTC로 `09:15:10`입니다.

`09:14:02`와 `09:15:10`을 비교합니다. 로그인 기록이 먼저입니다. 시간이 가깝다고 해서 같은 로그인에서 나온 이벤트라고 볼 수는 없습니다.

:::single-choice{#security-event-correlation-time-order} 다른 날의 로그에 로그인은 `09:14Z`, 요청은 `11:13+02:00`으로 기록됐습니다. 순서는 어떻게 되나요?

::option[요청이 1분 먼저다.]{#security-event-correlation-time-request-first .correct explanation="두 시간을 빼면 요청은 09:13 UTC입니다. 로그인은 09:14 UTC입니다."}
::option[로그인이 1분 먼저다.]{#security-event-correlation-time-login-first explanation="요청을 UTC로 바꾸면 09:13이므로 09:14 UTC의 로그인보다 1분 빠릅니다."}
::option[로그인이 거의 두 시간 먼저다.]{#security-event-correlation-time-unadjusted explanation="표시된 시각을 그대로 비교한 결과입니다. 순서를 정하기 전에 둘 다 UTC로 바꿉니다."}
:::

## 호스트와 세션 확인하기

**세션**은 로그인부터 로그아웃하거나 연결이 끊기기까지의 활동 기간입니다. 연습용 SSH 기록에는 허용된 로그인에 연결된 세션 ID가 들어 있습니다. 두 출처는 같은 호스트에서 같은 로그인에 대해 동일한 세션 ID를 사용합니다. 처음 두 기록에는 `host=web-01`과 `session=42`가 있어 로그인과 요청을 한 세션으로 연결할 수 있습니다.

이 예에서 세션 번호는 해당 호스트 안에서만 의미가 있습니다. 다음 기록은 계정과 세션 번호가 같고 시각은 몇 초 뒤입니다.

```text
t=09:15:18Z source=sudo host=web-02 account=alex session=42 decision=allowed
```

![web-01과 web-02의 모의 기록 및 09:15:10 UTC로 변환한 결과를 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-event-correlation/utc-correlation.png)

터미널에는 모의 기록 세 건이 나옵니다. Ubuntu의 `date` 명령어로 UTC 변환 결과를 확인합니다.

:::single-choice{#security-event-correlation-host-scope} 세 번째 기록은 원래 SSH 세션과 어떤 관계인가요?

::option[계정이 같고 시각이 가까우므로 같은 세션에 속한다.]{#security-event-correlation-host-scope-account explanation="두 호스트에서 같은 계정 이름으로 일어난 활동이 몇 초 간격으로 기록될 수 있습니다."}
::option[호스트가 다르므로 별도의 세션에 속한다.]{#security-event-correlation-host-scope-machine .correct explanation="web-02의 세션 42는 해당 호스트의 세션입니다. 원래 로그인은 web-01에서 일어났습니다."}
::option[세션 번호가 같으므로 같은 세션에 속한다.]{#security-event-correlation-host-scope-session explanation="이 예에서 세션 번호는 각 호스트 안에서만 의미가 있습니다. 여기서는 호스트 이름이 다릅니다."}
:::

## 기록이 뒷받침하는 사실 설명하기

`web-01`에서 로그인이 허용됐으며 해당 세션에서 `sudo`가 명령어를 실행하도록 허용했습니다. 현재 확보한 증거가 보여 주는 것은 여기까지입니다. 명령어 실행이 어떻게 끝났는지 알고 싶다면 결과를 남긴 기록을 찾으세요. 한 세션에는 여러 명령어가 있을 수 있으므로 결과를 특정 요청과 맞춰 봅니다. 맞는 기록이 없으면 결과를 알 수 없다고 적습니다.

:::single-choice{#security-event-correlation-completion-evidence} 그 명령어가 성공적으로 끝났는지 확인하려면 어떤 기록이 필요한가요?

::option[같은 세션에서 실행된 다른 명령어의 결과.]{#security-event-correlation-completion-other-command explanation="한 세션에서는 여러 명령어를 실행할 수 있습니다. 결과가 조사 중인 요청과 일치해야 합니다."}
::option[요청이 허용됐음을 보여 주는 두 번째 기록.]{#security-event-correlation-completion-permission explanation="이것은 실행 권한을 확인합니다. 결과를 알려면 결과 기록이 따로 필요합니다."}
::option[그 요청에서 실행한 명령어의 결과 기록.]{#security-event-correlation-completion-result .correct explanation="일치하는 결과가 있으면 명령어가 어떻게 끝났는지 알 수 있습니다."}
:::

다른 인증 및 sudo 기록을 필터링하고 비교하려면 [시스템 로그 분석](https://labex.io/tutorials/linux-system-log-analysis-656124)을 실습해 보세요.

## 요약

이제 여러 보안 기록을 바탕으로 결론을 내리고 더 확인할 내용을 설명할 수 있습니다.

1. 이벤트에 나오는 계정을 식별합니다.
2. 비교하기 전에 시각을 같은 시간대로 바꿉니다.
3. 호스트와 세션을 함께 사용해 활동을 연결합니다.
4. 기록이 입증하는 사실을 설명하고 남은 질문에 답할 추가 증거를 찾습니다.
