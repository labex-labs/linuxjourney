---
lesson_id: "security-events"
course_id: "security-logs"
lang: "ko"
order_index: 1
title: "보안 이벤트"
description: "보안 이벤트와 이를 설명하는 로그 기록, 검토를 요청하는 경보를 구분합니다."
meta_title: "보안 이벤트 - 보안 로그"
meta_description: "짧은 Linux 보안 기록을 읽고 경보와 비교하며, 기록만으로 답을 낼 수 없을 때 무엇을 더 확인할지 결정합니다."
meta_keywords: "보안 이벤트, 보안 로그, 로그 기록, 경보, Linux 로그"
---

서버가 로그인 실패를 보고했습니다. 어떤 일이 있었고, 이 기록으로 무엇을 알 수 있을까요? 컴퓨터가 남긴 사실과 그 사실에서 내린 결론을 먼저 구분해 봅시다.

## 이벤트와 로그 기록

**이벤트**는 로그인 시도가 거부되는 것처럼 실제로 일어난 일입니다. **로그 기록**은 그 이벤트를 설명해 저장한 내용입니다. **로그**는 이러한 기록을 모아 놓은 것입니다. 이 과정에서는 읽는 연습을 하기 쉽도록 필드 이름을 맞춘 모의 기록을 사용합니다. 실제 도구는 필드 이름이나 저장 방식을 다르게 사용할 수 있습니다.

```text
t=08:55:00Z source=ssh host=web-01 account=alex login=rejected
```

이 기록은 `alex` 계정의 원격 로그인 시도가 거부됐다고 보고합니다. 시도가 끝난 뒤에도 저장된 기록을 읽을 수 있습니다. 서로 다른 출처의 기록 시각을 비교하는 법은 뒤에서 다룹니다.

![web-01에서 alex의 SSH 로그인이 거부됐다는 모의 기록을 표시한 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/security-events/event-fields.png)

LabEx 터미널은 텍스트 파일에 저장한 동일한 모의 기록을 보여 줍니다.

:::single-choice{#security-events-event-versus-record} 이 예에서 이벤트 자체는 무엇인가요?

::option[거부 결과를 설명하는 저장된 줄.]{#security-events-event-line explanation="이 줄은 이벤트 이후에 읽을 수 있는 기록입니다."}
::option[저장된 줄을 나중에 검토한 일.]{#security-events-event-review explanation="검토는 나중에 한 작업입니다. 이 줄이 설명하는 이벤트는 로그인 시도가 거부된 일입니다."}
::option[로그인 시도가 거부된 일.]{#security-events-event-attempt .correct explanation="서버에서 실제로 로그인을 거부했습니다. 로그에는 그 일이 기록됩니다."}
:::

## 필드 읽기

**필드**는 기록을 이루는 개별 정보입니다. 이 예에서는 `t`가 기록된 시각, `host`가 이벤트가 일어난 컴퓨터, `source`가 이벤트를 보고한 도구를 나타냅니다. `account`는 관련 계정이고 `login`은 로그인 시도의 결과입니다.

:::single-choice{#security-events-field-host} 로그인 시도가 거부됐다고 기록한 컴퓨터를 확인하려면 어느 값을 봐야 하나요?

::option[account 필드의 `alex`.]{#security-events-field-host-account explanation="account는 시도와 관련된 계정을 나타냅니다."}
::option[host 필드의 `web-01`.]{#security-events-field-host-web .correct explanation="host는 이벤트가 일어난 컴퓨터를 가리킵니다."}
::option[source 필드의 `ssh`.]{#security-events-field-host-tool explanation="source는 이벤트를 보고한 도구를 나타냅니다."}
:::

## 경보와 규칙

**경보**는 검토가 필요할 수 있는 상황을 알립니다. 예를 들어 같은 호스트에서 같은 계정으로 5분 안에 로그인이 세 번 거부되면 경보를 내는 규칙을 만들 수 있습니다. 이 규칙은 기록을 계정, 호스트, 시간으로 묶습니다. 경보가 떴다는 것은 규칙과 일치했다는 뜻입니다. 누군가 비밀번호를 몇 번 잘못 입력했을 수도 있습니다.

:::single-choice{#security-events-alert-interpretation} web-01의 alex 계정에 실패가 세 번 기록되어 경보가 발생했습니다. 이 경보는 무엇을 보여 주나요?

::option[기록된 실패가 규칙의 조건을 충족했다.]{#security-events-alert-condition .correct explanation="경보는 검토할 만한 패턴을 알려 줍니다. 규칙으로는 누가 그 일을 일으켰는지 알 수 없습니다."}
::option[서로 다른 세 사람이 로그인을 시도했다.]{#security-events-alert-people explanation="한 사람이 세 번 시도했을 수도, 여러 사람이 시도했을 수도 있습니다. 이 규칙은 기록의 수를 셉니다."}
::option[세 번 시도한 뒤 누군가 로그인에 성공했다.]{#security-events-alert-success explanation="이 규칙은 거부된 로그인을 셉니다. 이후에 성공했는지는 알려 주지 않습니다."}
:::

## 다음 확인 항목 선택하기

`alex`가 나중에 로그인했는지 알고 싶다면 실패 시각 이후의 `web-01` 로그인 결과를 찾습니다. 결론을 내리기 전에 기록이 어느 시간까지 있는지 확인하세요. 로그 내보내기 파일은 선택한 기록의 사본이라 필요한 시각보다 일찍 끝날 수 있습니다.

:::single-choice{#security-events-next-record} 내보낸 기록은 09:00에 끝납니다. 09:05에 성공한 로그인이 있었는지 확인하려면 무엇을 찾나요?

::option[같은 내보내기 파일에서 가장 최근 기록부터 정렬한 것.]{#security-events-next-sort explanation="정렬은 순서만 바꿉니다. 09:00 이후의 기록은 추가되지 않습니다."}
::option[09:05가 포함된 web-01의 로그인 기록.]{#security-events-next-window .correct explanation="확인하려는 이벤트에 맞는 출처와 해당 시각을 포함하는 기록이 필요합니다."}
::option[09:00 이전 실패 횟수를 다시 센 것.]{#security-events-next-count explanation="이 수치는 더 이른 시간대의 다른 결과를 설명합니다."}
:::

## 요약

이제 보안 기록을 읽고 경보가 발생했을 때 무엇을 확인할지 결정할 수 있습니다.

1. 이벤트와 이를 기록한 줄을 구분합니다.
2. 예제 기록에서 계정, 호스트, 결과를 찾습니다.
3. 경보 규칙을 보고 무엇이 관측됐는지 파악합니다.
4. 기록의 출처와 시간 범위가 질문에 맞는지 확인합니다.
