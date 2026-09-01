---
lesson_id: "etc-shadow-file"
course_id: "user-management"
lang: "ko"
order_index: 4
title: "/etc/shadow"
description: "민감한 데이터를 노출하지 않고 로컬 shadow 레코드가 비밀번호 해시와 만료 정책을 나타내는 방식을 배웁니다."
meta_title: "/etc/shadow - User Management"
meta_description: "사용자 인증의 핵심 구성 요소인 Linux /etc/shadow 파일을 알아봅니다. 민감한 내용을 노출하지 않고 etc shadow 파일의 구조와 비밀번호 해시 및 정책 정보를 이해합니다."
meta_keywords: "etc shadow, linux etc/shadow 파일, etc shadow in linux, /etc/shadow, 사용자 인증, 비밀번호 보안, Linux 시스템 관리"
---

`/etc/shadow`는 보호된 로컬 비밀번호 해시와 비밀번호 만료 필드를 저장합니다. 일반적으로 읽을 수 있는 `/etc/passwd` 데이터베이스와 이 값을 분리하면 오프라인 비밀번호 추측 공격에 노출되는 정도가 줄어듭니다.

## Shadow 데이터 보호하기

비밀번호는 나중에 표시할 수 있도록 되돌릴 수 있는 방식으로 “암호화”되어 저장되지 않습니다. 로컬 비밀번호 항목에는 일반적으로 알고리즘 식별자, 솔트, 매개변수로 인코딩한 단방향 비밀번호 해시가 들어 있습니다. 공격자가 해시를 얻으면 후보 비밀번호를 오프라인에서 추측할 수 있으므로 데이터베이스 접근은 제한되어야 합니다.

정확한 소유권과 권한은 다양하지만 일반적으로 root와 좁게 승인된 시스템 구성 요소만 접근할 수 있습니다. 계정 상태를 살펴본다는 이유만으로 shadow 내용을 출력하거나 복사하거나 기록하거나 공유하지 마세요.

:::single-choice{#shadow-restricted-reason} 로컬 shadow 데이터의 일반 읽기 접근이 보통 제한되는 이유는 무엇인가요?

::option[모든 사용자의 암호화되지 않은 현재 비밀번호가 들어 있기 때문입니다.]{#shadow-plaintext-passwords explanation="올바른 shadow 항목은 되돌릴 수 있는 평문 비밀번호가 아니라 단방향 비밀번호 해시나 특수 표시를 저장합니다."}
::option[비밀번호 해시가 노출되면 오프라인 공격을 받을 수 있기 때문입니다.]{#shadow-offline-guessing .correct explanation="공격자는 로그인 서비스와 상호작용하지 않고 훔친 해시에 비밀번호 추측을 시험할 수 있습니다."}
::option[파일을 읽으면 모든 비밀번호 만료 날짜가 자동으로 바뀌기 때문입니다.]{#shadow-read-changes explanation="읽기 자체가 정책 필드를 갱신하지는 않습니다. 민감한 인증 자료 노출이 문제입니다."}
:::

## 아홉 필드 형식 읽기

로컬 shadow 레코드는 콜론으로 구분된 필드 아홉 개를 포함합니다. 해시를 의도적으로 생략한 개략적인 레코드는 다음과 같습니다.

```text
alice:<password-field>:20000:0:90:7:14:20500:
```

필드는 다음과 같습니다.

1. **로그인 이름**
2. **비밀번호 해시 또는 특수 비밀번호 표시**
3. **마지막 비밀번호 변경일**: 1970-01-01 이후 날짜 수. 일반 도구에서 `0`은 다음 비밀번호 인증 로그인 시 변경을 요청함
4. **최소 비밀번호 사용 기간**: 일수
5. **최대 비밀번호 사용 기간**: 일수
6. **비밀번호 만료 전 경고 기간**: 일수
7. **비밀번호 만료 후 비활성 기간**: 일수
8. **계정 만료 날짜**: 1970-01-01 이후 날짜 수
9. **예약 필드**

빈 필드와 특수 숫자 값은 필드와 도구에 따라 달라질 수 있는 정의된 의미를 갖습니다. 눈으로 보고 값을 직접 편집하지 말고 계정 관리 명령을 사용하세요.

:::single-choice{#shadow-account-expiration-field} 1970-01-01 이후 날짜 수로 계정 만료 날짜를 저장하는 shadow 필드는 무엇인가요?

::option[필드 3]{#shadow-field-three explanation="필드 3은 계정 만료가 아니라 마지막 비밀번호 변경 날짜를 기록합니다."}
::option[필드 8]{#shadow-field-eight .correct explanation="여덟 번째 필드는 절대적인 계정 만료 날짜 수입니다."}
::option[필드 5]{#shadow-field-five explanation="필드 5는 최대 비밀번호 사용 기간을 기록합니다."}
:::

## 비밀번호 필드 신중하게 해석하기

필드 2의 유효한 해시는 로컬 Unix 비밀번호 검증을 지원합니다. `!`로 시작하는 값은 일반적으로 해당 비밀번호 해시를 잠그고 `*`나 다른 유효하지 않은 해시 표시는 이 필드를 통한 성공적인 비밀번호 검증을 막습니다. 빈 값은 보안에 민감하며 PAM 정책에 따라 비밀번호 없는 동작을 허용할 수 있습니다.

이 표시는 가능한 모든 인증 방법이 아니라 로컬 비밀번호 경로를 설명합니다. SSH 공개 키, 인증서, 토큰, 애플리케이션별 자격 증명은 별도로 제한하지 않는 한 계속 사용할 수 있습니다. 필드 8의 계정 만료도 비밀번호 잠금과 다릅니다.

:::single-choice{#shadow-password-lock-scope} `!`로 시작하는 shadow 비밀번호 필드에서 안전하게 결론 내릴 수 있는 것은 무엇인가요?

::option[저장된 Unix 비밀번호 해시를 일반 비밀번호 검증에 사용할 수 없게 만들었습니다.]{#shadow-password-locked .correct explanation="해시 앞에 `!`를 붙이면 shadow 비밀번호 경로에서 제공된 비밀번호와 일치하지 않게 됩니다."}
::option[계정의 모든 가능한 로그인 방법이 비활성화되었습니다.]{#shadow-all-login-disabled explanation="다른 인증 방법은 독립적일 수 있으므로 비밀번호 표시만으로 완전한 계정 잠금을 증명하지 못합니다."}
::option[모든 신원 데이터베이스에서 계정이 삭제되었습니다.]{#shadow-account-deleted explanation="shadow 레코드는 여전히 존재하며 삭제는 별도의 계정 관리 작업입니다."}
:::

## 비밀번호 날짜와 계정 날짜 구분하기

필드 3부터 7은 비밀번호 만료를 다룹니다. 비밀번호를 마지막으로 바꾼 시점, 다시 변경할 수 있는 시점, 만료 시점, 경고 시작 시점, 만료 후 비밀번호 로그인이 가능한 기간을 나타냅니다. 필드 8은 비밀번호 사용 기간과 관계없이 절대 날짜에 계정을 만료시킵니다.

예를 들어 최대 비밀번호 사용 기간 90일은 계정 만료 날짜와 같지 않습니다. 전자는 마지막 비밀번호 변경을 기준으로 움직이고 후자는 관리자가 바꿀 때까지 고정된 날짜입니다.

:::single-choice{#shadow-max-age-versus-expire} shadow 필드 5와 8의 차이는 무엇인가요?

::option[필드 5는 사용자 이름, 필드 8은 로그인 쉘을 저장합니다.]{#shadow-username-shell explanation="사용자 이름은 필드 1이고 로그인 쉘은 shadow 레코드가 아니라 `/etc/passwd`에 기록됩니다."}
::option[필드 5는 비밀번호 해시, 필드 8은 솔트를 저장합니다.]{#shadow-hash-salt explanation="비밀번호 해시 인코딩은 필드 2에 있고 만료 필드는 솔트를 별도로 저장하지 않습니다."}
::option[필드 5는 최대 비밀번호 사용 기간이고 필드 8은 절대 계정 만료 날짜입니다.]{#shadow-password-vs-account-expiry .correct explanation="비밀번호 사용 기간은 마지막 변경을 기준으로 하고 계정 만료는 절대 날짜 수로 저장됩니다."}
:::

## 도구로 정책 확인하고 변경하기

관리자는 작업에 필요한 정보만 질의해야 합니다.

```bash
$ sudo passwd -S alice
$ sudo chage -l alice
```

`passwd -S`는 로컬 비밀번호 상태를 요약하고 `chage -l`은 만료 정보를 읽기 쉬운 형태로 나열합니다. 출력 형식과 권한 요구 사항은 배포판마다 다를 수 있습니다.

변경에는 `passwd`, `chage`, `usermod` 및 관련 계정 도구를 사용하세요. 로컬 shadow 데이터베이스를 수동으로 복구해야 한다면 `vipw -s`가 잠금을 제공하며 `pwck`로 계정 데이터베이스를 검증할 수 있습니다. 원격 인증을 바꾸기 전에 복구 세션을 유지하세요.

:::single-choice{#shadow-list-aging-policy} 로컬 계정 `alice`의 읽기 쉬운 비밀번호 만료 정보를 나열하도록 설계된 명령은 무엇인가요?

::option[`cat /etc/shadow`]{#shadow-cat-entire-file explanation="모든 로컬 shadow 레코드와 작업에 필요한 것보다 훨씬 민감한 정보를 노출합니다."}
::option[`passwd -d alice`]{#shadow-passwd-delete explanation="`-d` 작업은 비밀번호 해시를 제거하는 상태 변경 보안 작업이며 목록 명령이 아닙니다."}
::option[`chage -l alice`]{#shadow-chage-list .correct explanation="소문자 `-l` 옵션은 `chage`에 계정의 비밀번호 만료 필드를 읽기 쉬운 형태로 표시하도록 요청합니다."}
:::

PAM과 NSS는 로컬 shadow 파일 외의 인증 및 신원 출처를 통합할 수 있습니다. 따라서 시스템 계정에 로컬 shadow 레코드가 없거나 추가 서비스를 통해 인증할 수 있습니다.

통제된 환경에서 계정 상태와 만료 정책을 연습하려면 다음 실습을 진행해 보세요.

1. **[useradd, usermod, userdel로 Linux 사용자 계정 관리하기](https://labex.io/ko/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - `useradd`와 `passwd`를 사용한 새 계정 생성 및 보안 설정부터 수정과 삭제까지 연습합니다.
2. **[Linux 사용자 계정과 Sudo 권한 구성하기](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 비밀번호 정책 적용과 계정 보호를 포함한 사용자 계정 및 sudo 권한 관리 기법을 배웁니다.

## 요약

이제 전체 비밀번호 데이터베이스를 노출하지 않고 shadow 정책을 해석할 수 있습니다.

1. 비밀번호 해시를 제한된 인증 자료로 다룰 수 있습니다.
2. shadow 필드 아홉 개를 목적별로 읽을 수 있습니다.
3. 비밀번호 잠금과 모든 로그인 방법 비활성화를 구분할 수 있습니다.
4. 비밀번호 사용 기간과 절대 계정 만료를 분리할 수 있습니다.
5. 범위가 명확한 계정 도구로 정책을 확인하고 변경할 수 있습니다.
