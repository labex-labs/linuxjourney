---
lesson_id: "sudo-events"
course_id: "security-logs"
lang: "ko"
order_index: 3
title: "sudo 이벤트"
description: "sudo 기록에서 명령어를 요청한 계정, 명령어를 실행할 계정, 허용 여부를 읽는 법을 배웁니다."
meta_title: "sudo 이벤트 - 보안 로그"
meta_description: "sudo 기록의 요청 계정, 대상 계정, 명령어와 권한 결정을 구분합니다."
meta_keywords: "sudo 이벤트, sudo 로그, sudo 권한, 대상 계정, Linux 권한"
---

일반 계정으로 로그인한 뒤 더 높은 권한이 필요한 작업을 해야 할 수 있습니다. `sudo`를 쓰는 시스템에서는 다른 계정으로 명령어를 실행할 수 있도록 요청할 수 있습니다. 요청 기록을 보면 어떤 권한을 요청했고 시스템이 어떤 결정을 내렸는지 알 수 있습니다.

## 두 계정 확인하기

다음 모의 기록에서 `account`는 요청한 계정, `target`은 명령어를 실행할 때 쓰려는 계정입니다. `root` 계정에는 시스템 관리 권한이 있습니다. `sudo` 요청에는 `backup`과 같이 다른 대상 계정도 지정할 수 있습니다.

```text
t=09:15:10Z source=sudo host=web-01 account=alex target=root
command=systemctl status nginx decision=allowed session=42
```

둘째 줄은 같은 기록의 이어지는 부분입니다. 여기서는 `alex`가 `root`로 명령어를 실행하도록 요청했습니다.

:::single-choice{#sudo-events-account-target} 기록에 `account=sam target=backup`이 있다면 어느 계정이 어떤 계정으로 명령어를 실행하려 했나요?

::option[backup이 sam으로 실행해 달라고 요청했다.]{#sudo-events-target-swapped explanation="account는 요청한 계정이고 target은 명령어를 실행할 때 쓸 계정입니다."}
::option[sam이 backup으로 실행해 달라고 요청했다.]{#sudo-events-target-backup .correct explanation="account는 요청자, target은 명령어가 사용할 계정입니다."}
::option[sam이 root로 실행해 달라고 요청했다.]{#sudo-events-target-root explanation="root는 지정할 수 있는 대상 계정 중 하나입니다. 이 기록에는 backup이 나옵니다."}
:::

## 요청한 명령어 읽기

`command` 필드는 요청에 해당하는 명령어를 가리킵니다. 예제의 `systemctl status nginx`는 Nginx 웹 서비스의 현재 상태를 보여 달라는 요청입니다. 다른 기록에 `systemctl restart nginx`가 나온다면 서비스를 중지한 뒤 다시 시작하라는 요청입니다. 둘 다 같은 서비스를 다루지만 요청하는 동작은 다릅니다.

:::single-choice{#sudo-events-command-scope} 웹 서비스의 실행 상태를 변경하도록 요청하는 명령어는 무엇인가요?

::option[`systemctl restart nginx`]{#sudo-events-command-restart .correct explanation="restart는 서비스를 중지한 뒤 다시 시작하므로 실행 상태를 바꿀 수 있습니다."}
::option[`systemctl status nginx`]{#sudo-events-command-status explanation="status는 서비스 정보를 보여 달라는 명령어입니다. 재시작을 요청하지 않습니다."}
::option[둘 다 nginx를 지정하므로 어느 쪽이든 해당한다.]{#sudo-events-command-both explanation="서비스 이름은 같습니다. 동작을 나타내는 단어를 보면 무엇을 요청했는지 알 수 있습니다."}
:::

## 허용 여부 읽기

**정책**은 `sudo`가 요청을 허용할지 판단하는 규칙입니다. 예제에서 `decision=allowed`는 정책이 요청을 허용했다는 뜻입니다. `decision=denied`는 `sudo`가 요청을 거부했다는 뜻입니다.

```text
t=09:16:00Z source=sudo host=web-01 account=alex target=root
command=systemctl restart nginx decision=denied session=42
```

허용 결정은 실행할 권한이 있었다는 뜻입니다. 명령어의 결과를 알아야 한다면 시스템에서 제공하는 결과 기록을 찾으세요.

![상태 조회는 허용되고 재시작은 거부된 모의 sudo 기록을 보여 주는 LabEx 터미널](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/security-logs/sudo-events/sudo-decisions.png)

두 모의 기록의 명령어와 권한 결정을 비교해 보세요.

:::single-choice{#sudo-events-denied-request} 두 번째 예제에서 재시작 요청은 어떻게 처리됐나요?

::option[sudo가 재시작 요청을 거부했다.]{#sudo-events-denied-refused .correct explanation="명령어는 요청된 동작을, denied는 권한 결정이 거부였음을 보여 줍니다."}
::option[서비스가 성공적으로 다시 시작됐다.]{#sudo-events-denied-success explanation="이 기록은 요청이 거부됐다고 보고합니다. 재시작이 성공했다는 증거는 없습니다."}
::option[앞선 상태 조회 요청도 거부됐다.]{#sudo-events-denied-earlier explanation="각 결정은 해당 요청에만 적용됩니다. 앞선 기록에는 allowed가 나옵니다."}
:::

## 로그인 계정도 함께 확인하기

두 예제는 `alex`를 요청자로 표시하고 `session=42`를 포함합니다. 이 번호는 로그인 후 활동 기간인 로그인 세션을 가리킵니다. 전후의 로그인 기록을 찾을 때 도움이 됩니다. 각각의 대상 계정은 그 명령어 요청에만 해당합니다. 요청을 설명할 때는 요청 계정과 대상 계정을 함께 확인하세요.

:::single-choice{#sudo-events-session-interpretation} 첫 번째 예제를 가장 잘 요약한 것은 무엇인가요?

::option[root가 직접 로그인해 세션 42를 열었다.]{#sudo-events-session-root-login explanation="이것은 sudo 기록입니다. 대상 계정 필드는 별도의 로그인을 설명하지 않습니다."}
::option[Alex가 세션의 모든 명령어에 root 권한을 요청했다.]{#sudo-events-session-all-commands explanation="이 기록은 명령어 하나를 명시합니다. 세션 안의 모든 명령어를 다루지 않습니다."}
::option[Alex가 세션 42에서 특정 명령어 하나를 root로 실행해 달라고 요청했다.]{#sudo-events-session-one-command .correct explanation="요청자, 대상, 명령어, 세션 필드가 이 설명을 뒷받침합니다."}
:::

## 요약

이제 sudo 기록을 읽고 권한 결정과 명령어의 실행 결과를 구분할 수 있습니다.

1. 요청 계정과 대상 계정을 찾습니다.
2. 명령어 필드로 구체적인 요청을 설명합니다.
3. 허용된 요청과 거부된 요청을 구분합니다.
4. 요청을 설명할 때 로그인 세션을 함께 확인합니다.
