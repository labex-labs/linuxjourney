---
lesson_id: "etc-group-file"
course_id: "user-management"
lang: "ko"
order_index: 5
title: "/etc/group"
description: "로컬 그룹 레코드가 이름을 GID에 매핑하고 보조 구성원을 나열하는 방법을 배웁니다."
meta_title: "/etc/group - User Management"
meta_description: "Linux /etc/group 파일을 통해 그룹 관리를 이해합니다. 로컬 그룹 데이터와 GID 및 사용자 목록을 포함하는 구조를 알아봅니다."
meta_keywords: "/etc/group, /etc/group linux, linux /etc/group 파일, etc group linux, 그룹 관리, GID, Linux 권한, Linux 그룹"
---

`/etc/group`은 로컬 그룹 레코드를 저장합니다. 그룹 이름을 숫자 GID에 매핑하고 명시적인 구성원을 나열하여 여러 계정이 공유하는 접근 제어를 지원합니다.

## 로컬 그룹과 해석된 그룹 구분하기

이 파일은 가능한 그룹 출처 중 하나일 뿐입니다. NSS는 로컬 파일, 디렉터리 서비스 또는 구성된 다른 데이터베이스에서 그룹을 해석할 수 있습니다. 로컬 레코드는 다음 명령으로 표시합니다.

```bash
$ cat /etc/group
```

`getent`로 해석된 그룹 데이터베이스를 질의합니다.

```bash
$ getent group
$ getent group developers
```

그룹 목록은 내부 계정과 역할 이름을 노출할 수 있으므로 공유하기 전에 출력을 검토하세요.

:::single-choice{#group-query-resolved-database}
NSS로 해석된 그룹 데이터베이스를 질의하는 명령은 무엇인가요?

::option[`getent group`]{#group-getent-all .correct explanation="`getent`는 그룹 레코드에 대해 구성된 NSS 출처를 확인합니다."}
::option[`cat /etc/group`]{#group-cat-local explanation="로컬 그룹 파일만 읽으며 다른 출처가 제공하는 그룹을 누락할 수 있습니다."}
::option[`groups /etc/group`]{#group-groups-file explanation="`groups`는 사용자 이름을 받고 멤버십을 보고하며 로컬 데이터베이스 경로를 NSS 질의로 처리하지 않습니다."}
:::

## 네 필드 읽기

로컬 레코드에는 콜론으로 구분된 필드 네 개가 있습니다.

```text
developers:x:1500:alice,bob
```

1. **그룹 이름**: `developers`
2. **비밀번호 필드**: 일반적으로 `x`, `*` 또는 다른 자리 표시자. 보호된 그룹 비밀번호 데이터는 `/etc/gshadow`에 저장될 수 있음
3. **GID**: 숫자 그룹 신원. 여기서는 `1500`
4. **구성원 목록**: 쉼표로 구분된 명시적 구성원 이름. 여기서는 `alice`와 `bob`

그룹 비밀번호는 일부 구성에서 `newgrp` 같은 도구가 사용하는 레거시 기능입니다. sudo 권한을 부여하는 일반적인 방법이 아니며 필드를 수동으로 편집하여 도입해서는 안 됩니다.

:::single-choice{#group-gid-field}
`developers:x:1500:alice,bob`에서 GID가 들어 있는 필드는 무엇인가요?

::option[두 번째 필드 `x`]{#group-second-password explanation="필드 2는 숫자 신원이 아니라 그룹 비밀번호 자리 표시자입니다."}
::option[네 번째 필드 `alice,bob`]{#group-fourth-members explanation="필드 4는 GID가 아니라 명시적인 구성원 이름을 나열합니다."}
::option[세 번째 필드 `1500`]{#group-third-gid .correct explanation="콜론으로 구분된 세 번째 필드가 숫자 그룹 ID입니다."}
:::

:::single-choice{#group-explicit-member-field}
로컬 그룹 레코드에서 명시적인 구성원 이름은 어떻게 표현되나요?

::option[필드 4의 쉼표로 구분된 목록입니다.]{#group-members-field-four .correct explanation="마지막 필드에는 명시적인 보조 구성원 이름이 쉼표로 구분되어 있습니다."}
::option[필드 2의 공백으로 구분된 목록입니다.]{#group-members-field-two explanation="필드 2는 구성원 목록이 아니라 비밀번호 관련 데이터나 자리 표시자에 예약되어 있습니다."}
::option[그룹 이름 안에 포함된 숫자 UID입니다.]{#group-members-in-name explanation="그룹 이름과 구성원 이름은 별도 필드이며 일반 구성원 항목은 포함된 UID 숫자가 아니라 로그인 이름입니다."}
:::

## 기본 그룹 멤버십 고려하기

`/etc/group`의 구성원 목록에는 일반적으로 passwd 레코드에서 해당 GID를 기본 그룹으로 지정한 사용자를 다시 적지 않습니다. 따라서 필드 4에 이름이 없어도 사용자가 구성원일 수 있습니다.

예를 들어 Alice의 passwd 레코드가 기본 GID 1500을 사용하면 로컬 그룹 레코드의 구성원 필드가 비어 있어도 `developers`에 속합니다.

```text
developers:x:1500:
```

따라서 필드 4만 분석하면 불완전한 멤버십 결과가 나옵니다.

:::single-choice{#group-primary-membership-visibility}
Alice의 passwd 레코드는 GID 1500을 기본 GID로 사용하지만 그룹 1500의 필드 4에는 이름이 없습니다. Alice는 그 그룹의 구성원인가요?

::option[아니요. 모든 멤버십은 `/etc/group` 필드 4에 나타나야 합니다.]{#group-field-four-only explanation="기본 GID 멤버십을 무시하여 그룹 구성원 수를 적게 계산합니다."}
::option[예. 기본 멤버십은 passwd 레코드의 GID 필드에서 옵니다.]{#group-primary-from-passwd .correct explanation="그룹 파일의 명시적 목록은 주로 보조 멤버십에 쓰이고 기본 멤버십은 계정에 기록됩니다."}
::option[그룹 비밀번호 필드에 사용자 이름이 있을 때만 구성원입니다.]{#group-password-member explanation="비밀번호 필드는 기본 멤버십 선언과 관련이 없습니다."}
:::

## 사용자의 그룹 확인하기

해석된 계정 보기에는 `id USER`나 `groups USER`를 사용합니다.

```bash
$ id alice
$ groups alice
```

현재 프로세스에 대해서는 일반 `id`가 실제 자격 증명에 있는 그룹을 보고합니다. 새로 구성된 보조 멤버십은 보통 이미 실행 중인 로그인 세션에 나타나지 않습니다. 새 인증 세션을 시작하거나 적절한 경우 의도적으로 구성한 `newgrp` 같은 메커니즘을 사용하세요.

:::single-choice{#group-current-process-credentials}
현재 프로세스의 UID, 기본 GID, 보조 그룹을 보고하는 명령은 무엇인가요?

::option[`id`]{#group-current-id .correct explanation="사용자 피연산자가 없으면 `id`는 현재 프로세스의 신원 자격 증명을 보고합니다."}
::option[`cat /etc/group`]{#group-current-cat explanation="로컬 파일은 레코드를 나열하지만 현재 프로세스에서 활성화된 해석 그룹은 보여 주지 않습니다."}
::option[`getent passwd`]{#group-current-passwd explanation="계정 레코드를 질의하며 현재 프로세스의 보조 그룹 목록을 구체적으로 보고하지 않습니다."}
:::

## 로컬 그룹 안전하게 변경하기

일반 편집기로 레코드를 바꾸지 말고 `groupadd`, `groupmod`, `groupdel`, `gpasswd`, `usermod` 같은 도구를 사용하세요. 특히 다음 차이에 주의합니다.

- `usermod -aG GROUP USER`: 보조 그룹 멤버십 추가
- `usermod -G ...`: `-a`를 생략하면 보조 그룹 목록 교체

로컬 데이터베이스를 수동으로 복구해야 한다면 잠금을 위해 `vigr`, 검증을 위해 `grpck`를 사용합니다. 원격 신원 변경 전에는 복구 경로를 유지하세요.

통제된 환경에서 로컬 그룹 관리를 연습하려면 다음 실습을 진행해 보세요.

1. **[useradd, usermod, userdel로 Linux 사용자 계정 관리하기](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 새 계정 생성과 보안 설정부터 수정 및 삭제까지 사용자 관리 수명 주기를 연습합니다.
2. **[groupadd, usermod, groupdel로 Linux 그룹 관리하기](https://labex.io/ko/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - `groupadd`, `usermod`, `groupdel`을 포함한 핵심 그룹 관리 명령줄 도구를 연습합니다.
3. **[새 사용자와 그룹 추가하기](https://labex.io/ko/labs/linux-add-new-user-and-group-17987)** - 새 사용자 계정을 만들고 사용자 지정 그룹을 설정하며 멤버십을 관리합니다.

## 요약

이제 로컬 그룹 레코드를 해석하고 완전한 멤버십을 더 정확히 확인할 수 있습니다.

1. `getent group`으로 구성된 그룹 출처를 질의할 수 있습니다.
2. 콜론으로 구분된 그룹 필드 네 개를 읽을 수 있습니다.
3. 숫자 GID와 명시적인 구성원 목록을 찾을 수 있습니다.
4. passwd 레코드의 기본 멤버십을 포함할 수 있습니다.
5. 변경된 멤버십에 의존하기 전에 활성 자격 증명을 확인할 수 있습니다.
