---
lesson_id: "root-user"
course_id: "user-management"
lang: "ko"
order_index: 2
title: "root"
description: "su, sudo, sudoers 정책이 권한 있는 신원에 대한 통제된 접근을 제공하는 방법을 배웁니다."
meta_title: "root - User Management"
meta_description: "Linux root 사용자의 역할을 알아봅니다. 슈퍼사용자 권한을 얻는 su와 sudo의 차이 및 /etc/sudoers 파일이 접근을 관리하는 방식을 설명합니다."
meta_keywords: "linux root 사용자, root user in linux, su, sudo, sudoers, visudo, 슈퍼사용자, 사용자 관리, linux 권한"
---

전통적으로 `root`라는 이름의 계정은 UID 0과 해당 보안 문맥에서 광범위한 권한을 갖습니다. 일상적인 작업에는 권한이 없는 계정을 사용하고 이해하는 특정 관리 목적에만 권한을 높이세요.

## su로 다른 사용자의 쉘 시작하기

substitute user를 뜻하는 `su`는 다른 계정의 신원으로 쉘이나 명령을 시작합니다. 사용자 이름이 없으면 기본 대상은 root입니다.

```bash
$ su
```

인증은 PAM과 로컬 정책으로 제어됩니다. 시스템은 대상 계정의 비밀번호를 묻거나 `su` 사용자를 제한하거나 root 비밀번호를 잠긴 상태로 둘 수 있습니다. 비밀번호를 아는 것이 유일한 조건이라고 가정하지 마세요.

일반 `su`는 신원을 바꾸면서 현재 환경을 더 많이 유지합니다. `su --login USER`로도 쓰는 `su - USER`는 로그인 형식의 쉘을 시작하고 대상 계정의 새 로그인에 가까운 환경을 초기화합니다.

```bash
$ su - operator
```

대상 계정 작업이 끝나면 하위 쉘을 종료하세요.

:::single-choice{#root-su-login-shell} `operator` 사용자로 로그인 형식 쉘을 요청하는 명령은 무엇인가요?

::option[`su - operator`]{#root-su-login-operator .correct explanation="하이픈은 `operator`에 대한 로그인 쉘 동작과 대상 중심 환경을 요청합니다."}
::option[`su operator`]{#root-su-preserve-environment explanation="대상 신원으로 바꾸지만 여기서 소개한 완전한 로그인 형식 초기화를 요청하지 않습니다."}
::option[`sudo -l operator`]{#root-sudo-list-operator explanation="`sudo -l`은 정책에 따라 허용된 명령을 나열하며 요청한 로그인 쉘을 시작하지 않습니다."}
:::

## sudo로 특정 명령 실행하기

`sudo COMMAND`는 대상 사용자로 명령 하나를 실행할 정책 권한을 요청하며 기본 대상은 보통 root입니다. 다른 대상을 요청하려면 `-u USER`를 사용합니다.

```bash
$ sudo -u postgres id
```

요청이 허용된다는 뜻은 아닙니다. Sudo 정책은 호출 사용자, 호스트, 대상 신원, 명령 및 기타 조건을 제어합니다. 구성에 따라 호출 사용자의 비밀번호나 다른 메커니즘으로 인증하거나 요청을 표시하지 않을 수 있습니다.

가능하면 오래 유지되는 권한 쉘보다 범위가 좁고 명확한 관리 명령 하나를 선호하세요. 범위가 작으면 실수한 명령이 높은 권한으로 실행될 가능성이 줄어듭니다.

:::single-choice{#root-sudo-target-user} `sudo -u postgres id`는 무엇을 요청하나요?

::option[현재 계정의 이름을 영구적으로 `postgres`로 바꿉니다.]{#root-sudo-rename explanation="`sudo`는 대상 자격 증명으로 명령을 실행하며 계정 레코드의 이름을 바꾸지 않습니다."}
::option[정책에 따라 `postgres`를 대상 사용자로 하여 `id`를 실행합니다.]{#root-sudo-postgres-id .correct explanation="`-u` 옵션이 대상 신원을 선택하고 sudoers 정책이 요청 허용 여부를 결정합니다."}
::option[현재 사용자보다 UID가 큰 모든 사용자를 나열합니다.]{#root-sudo-list-uids explanation="`id` 명령은 해당 프로세스의 신원 정보를 보고하며 이 구문은 계정 UID를 열거하지 않습니다."}
:::

## 지속되는 권한 쉘 피하기

정책이 허용하면 `su -`, `sudo -s`, `sudo -i` 같은 명령으로 권한 쉘을 만들 수 있습니다. 종료할 때까지 이후의 모든 명령이 높은 영향을 가질 수 있습니다. 경로 실수, 검토하지 않은 스크립트, 쉘 확장이 더 위험해집니다.

감사 동작은 구성에 따라 달라집니다. `sudo`는 일반적으로 호출을 기록하지만 쉘 시작 하나를 기록했다고 그 안에서 입력한 모든 명령의 완전한 기록이 자동으로 생기지는 않습니다. 쉘 기록, 시스템 감사, sudo 입출력 로깅은 각자의 정책을 가진 별도 메커니즘입니다.

:::single-choice{#root-persistent-shell-risk} 오래 유지되는 root 쉘이 이해한 명령 하나씩 권한을 높이는 것보다 위험한 이유는 무엇인가요?

::option[Root 쉘은 모든 감사 시스템에서 모든 명령을 자동으로 삭제합니다.]{#root-shell-no-audit explanation="로깅은 구성에 따라 달라지므로 모든 감사 기록이 자동으로 지워진다는 주장은 정확하지 않습니다."}
::option[쉘이 구성 요소 하나보다 긴 파일 시스템 경로를 비활성화합니다.]{#root-shell-path-limit explanation="권한은 이런 경로 제한을 만들지 않습니다. 일반 작업에 적용되는 권한의 크기가 문제입니다."}
::option[쉘이 종료될 때까지 이후 명령이 높은 영향을 계속 가질 수 있습니다.]{#root-shell-elevated-scope .correct explanation="지속되는 권한 신원은 오타나 신뢰할 수 없는 명령이 보호 자원을 바꿀 수 있는 시간을 늘립니다."}
:::

## sudo 권한 검토하기

`sudo -l`로 활성 정책에서 현재 계정이 요청할 수 있는 작업을 나열합니다.

```bash
$ sudo -l
```

명령 경로, 허용된 대상 사용자, 인자 제한을 검토하세요. 범위가 넓어 보이는 규칙을 관련 없는 작업의 허가로 여기지 마세요.

:::single-choice{#root-list-sudo-rules} 현재 호출 사용자가 사용할 수 있는 sudo 권한을 나열하는 명령은 무엇인가요?

::option[`sudo -i`]{#root-sudo-login explanation="대상의 로그인 형식 쉘을 요청하여 권한 범위를 늘릴 수 있으며 읽기 전용 정책 목록이 아닙니다."}
::option[`sudo -l`]{#root-sudo-list .correct explanation="소문자 `-l` 옵션은 sudo에 현재 정책이 허용하는 명령을 나열하도록 요청합니다."}
::option[`su -l`]{#root-su-login-default explanation="sudo 권한을 나열하지 않고 `su`의 로그인 쉘 동작을 호출합니다."}
:::

## sudoers 정책 안전하게 편집하기

기본 sudo 정책은 일반적으로 `/etc/sudoers`를 읽고 `/etc/sudoers.d/` 아래의 파일을 포함할 수 있습니다. 다른 정책 출처도 가능합니다. 구문은 단순한 사용자 및 그룹 목록보다 훨씬 많은 것을 제어합니다.

`visudo`는 파일을 잠그고 설치 전에 구문을 검증하므로 정책 변경에 사용하세요.

```bash
$ sudo visudo
```

드롭인 파일에는 정확한 경로를 지정합니다.

```bash
$ sudo visudo -f /etc/sudoers.d/application-admins
```

일반 리디렉션이나 검증되지 않은 편집기 작업 흐름으로 sudoers를 편집하지 마세요. 구문이나 권한 실수로 관리 접근을 잃을 수 있습니다. 원격 권한을 바꿀 때는 확인된 다른 복구 경로를 유지하세요.

:::single-choice{#root-edit-sudoers-safely} 주 sudoers 정책을 편집하고 구문을 검사할 때 사용해야 하는 도구는 무엇인가요?

::option[`cat`]{#root-cat-sudoers explanation="`cat`은 읽을 수 있는 텍스트를 표시하지만 sudoers 구문을 안전하게 편집하고 잠그거나 검증하지 않습니다."}
::option[`visudo`]{#root-visudo .correct explanation="`visudo`는 sudoers 정책 변경을 위해 설계된 잠금과 구문 검증을 제공합니다."}
::option[`echo`와 `>`]{#root-echo-sudoers explanation="쉘 리디렉션은 정책을 즉시 비울 수 있고 sudoers 구문 검증을 제공하지 않습니다."}
:::

통제된 환경에서 위임된 관리를 연습하려면 다음 실습을 진행해 보세요.

1. **[Linux 사용자 계정과 Sudo 권한 구성하기](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 비밀번호 정책 적용, 계정 잠금과 해제, root 계정 보호, 관리 권한 부여를 연습합니다.

## 요약

이제 신원 전환과 정책으로 제어되는 명령 위임을 구분할 수 있습니다.

1. 대상 로그인 쉘이 필요할 때만 `su - USER`를 사용할 수 있습니다.
2. `-u USER`로 특정 sudo 대상을 요청할 수 있습니다.
3. 권한 쉘에서 보내는 시간을 최소화할 수 있습니다.
4. `sudo -l`로 유효 sudo 규칙을 검토할 수 있습니다.
5. `visudo`를 통해서만 sudoers 정책을 편집할 수 있습니다.
