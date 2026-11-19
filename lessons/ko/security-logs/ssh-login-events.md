---
lesson_id: "ssh-login-events"
course_id: "security-logs"
lang: "ko"
order_index: 2
title: "SSH 로그인 이벤트"
description: "SSH 기록에서 거부된 로그인과 허용된 로그인을 읽고 한 연결에서 일어난 시도를 묶는 법을 배웁니다."
meta_title: "SSH 로그인 이벤트 - 보안 로그"
meta_description: "SSH 로그에서 대상 계정, 원격 주소, 인증 방법과 결과를 읽고 연결 식별자로 각 시도를 비교합니다."
meta_keywords: "SSH 로그인 이벤트, SSH 로그, 로그인 성공, 로그인 거부, 인증 방법"
---

**SSH**는 Secure Shell의 약자로, 네트워크를 통해 다른 컴퓨터에 로그인할 때 사용합니다. 연결을 받는 컴퓨터는 각 로그인 시도를 기록할 수 있습니다. 기록에는 어떤 계정으로 로그인하려 했는지, 서버가 제시된 인증 증거를 받아들였는지가 나타납니다.

## 결과 읽기

다음은 모의 SSH 기록 두 건입니다. `login` 필드가 결과를 나타냅니다. 거부됐다는 것은 로그인 검사를 통과하지 못했다는 뜻입니다. 허용된 시도는 검사를 통과한 것입니다.

```text
t=09:13:48Z source=ssh host=web-01 account=alex login=rejected
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
```

첫 번째는 `alex`의 로그인 시도가 거부됐다는 기록입니다. 두 번째는 같은 계정의 다른 시도가 허용됐음을 보여 줍니다. 각 결과는 해당 시도에만 적용됩니다.

:::single-choice{#ssh-login-events-outcome-order} 두 기록으로부터 무엇을 알 수 있나요?

::option[나중에 한 시도가 로그인 검사를 통과했다.]{#ssh-login-events-outcome-later .correct explanation="두 번째 기록은 09:14:02의 login=accepted를 보여 줍니다."}
::option[두 시도 모두 로그인 검사를 통과했다.]{#ssh-login-events-outcome-both explanation="앞선 줄에는 로그인 거부가 기록되어 있습니다."}
::option[나중에 한 시도가 로그인 검사를 통과하지 못했다.]{#ssh-login-events-outcome-failed explanation="거부된 것은 첫 번째 시도입니다. 두 번째 시도는 허용됐습니다."}
:::

## 주소와 인증 방법 읽기

원격 주소는 연결을 받은 컴퓨터에서 본 연결 출발지입니다. 이 예에서는 `peer` 필드에 표시됩니다. 네트워크 주소는 여러 사람이 공유할 수 있어 이 필드만으로 누가 사용했는지는 알 수 없습니다.

```text
t=09:14:02Z source=ssh host=web-01 account=alex login=accepted
peer=192.0.2.10 method=publickey connection=17
```

둘째 줄은 같은 기록의 이어지는 부분입니다. `method`는 SSH가 확인한 인증 방법을 설명합니다. `password`는 SSH가 비밀번호를 확인했다는 뜻입니다. `publickey`는 접속한 기기가 그 계정에 대해 서버가 인정하는 키를 사용할 수 있음을 증명했다는 뜻입니다.

:::single-choice{#ssh-login-events-method-evidence} 허용된 시도에 대해 어떤 결론을 내릴 수 있나요?

::option[서버가 비밀번호를 사용한 로그인을 허용했다.]{#ssh-login-events-method-password explanation="비밀번호 방식이었다면 따로 표시됩니다. 이 기록은 공개 키 방식을 보여 줍니다."}
::option[서버가 해당 주소를 사용한 사람을 식별했다.]{#ssh-login-events-method-person explanation="주소는 호스트에서 본 연결을 나타냅니다. 누가 실제로 컴퓨터를 조작했는지는 확인할 수 없습니다."}
::option[서버가 키를 사용한 로그인을 허용했다.]{#ssh-login-events-method-key .correct explanation="기록에 login=accepted와 method=publickey가 모두 나옵니다."}
:::

## 연결별로 시도 묶기

**연결**은 SSH가 메시지를 주고받는 네트워크 경로입니다. 이 예에서 호스트는 각 연결에 식별자를 배정합니다. 하나의 연결에서 여러 번 로그인을 시도할 수 있고 같은 주소에서 새 연결을 시작할 수도 있습니다.

```text
t=09:13:48Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=rejected
t=09:13:55Z host=web-01 account=alex peer=192.0.2.10 connection=18 login=rejected
t=09:14:02Z host=web-01 account=alex peer=192.0.2.10 connection=17 login=accepted
```

`web-01`의 첫 기록과 마지막 기록은 둘 다 연결 17에 해당합니다. 이 식별자는 호스트와 함께 읽으세요.

![한 주소에서 연결 ID 17과 18로 들어온 모의 SSH 시도를 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/ssh-login-events/ssh-connections.png)

세 가지 모의 시도를 터미널에 함께 표시해 연결 번호를 비교할 수 있습니다.

:::single-choice{#ssh-login-events-group-connection} 어떤 기록이 web-01의 연결 18을 가리키나요?

::option[09:13:48과 09:14:02의 시도.]{#ssh-login-events-group-seventeen explanation="두 줄의 연결 번호는 모두 17입니다."}
::option[09:13:55의 시도만 해당한다.]{#ssh-login-events-group-eighteen .correct explanation="이 줄만 web-01의 연결 18을 보여 줍니다."}
::option[192.0.2.10에서 온 세 번의 시도 모두.]{#ssh-login-events-group-address explanation="같은 주소에 연결 번호가 두 가지 있습니다."}
:::

## 성공한 로그인 이후 살펴보기

로그인 성공은 SSH가 해당 계정의 인증 증거를 받아들였다는 뜻입니다. 그다음에 무슨 일이 있었는지 알려면 **세션**이 열렸다는 기록을 찾으세요. 로그인 세션은 로그인 후의 활동 기간입니다. 성공 기록만으로 확인되는 것은 로그인 검사 결과입니다.

:::single-choice{#ssh-login-events-after-accepted} 허용된 로그인 후 세션이 열렸는지 확인하려면 어떤 기록이 도움이 될까요?

::option[같은 로그인이 허용됐다는 다른 기록.]{#ssh-login-events-after-accepted-again explanation="로그인 검사 결과를 반복하는 데 그칩니다."}
::option[다른 호스트에서 같은 계정이 이전에 로그인에 실패했다는 기록.]{#ssh-login-events-after-other-host explanation="다른 컴퓨터에서 일어난 별도의 시도입니다."}
::option[해당 로그인으로 세션이 열렸다는 기록.]{#ssh-login-events-after-session .correct explanation="세션 시작 기록은 다음 단계가 일어났음을 보여 주며, 허용된 로그인과 연결할 수 있습니다."}
:::

## 요약

이제 SSH 시도의 결과를 읽고 어떤 기록이 같은 연결에 속하는지 판단할 수 있습니다.

1. 허용된 시도와 거부된 시도를 구분합니다.
2. 원격 주소와 인증 방법으로 시도를 설명합니다.
3. 식별자가 있으면 호스트와 연결을 함께 사용해 기록을 묶습니다.
4. 세션 기록을 찾아 로그인 성공 후 어떤 일이 있었는지 확인합니다.
