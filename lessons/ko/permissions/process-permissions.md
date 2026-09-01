---
lesson_id: "process-permissions"
course_id: "permissions"
lang: "ko"
order_index: 7
title: "프로세스 권한"
description: "실제, 유효, 저장 사용자 ID가 Linux 프로세스에서 호출자를 추적하고 권한을 관리하는 방식을 배웁니다."
meta_title: "프로세스 권한 - Permissions"
meta_description: "실제, 유효, 저장 사용자 ID를 포함한 Linux 프로세스 권한을 배웁니다. UID가 보안과 명령 실행에 미치는 영향을 이해하세요."
meta_keywords: "Linux 프로세스 권한, 실제 UID, 유효 UID, 저장 UID, Linux 보안, passwd 명령, Linux 튜토리얼, 초보자 Linux"
---

Linux 권한 검사는 입력된 사용자 이름이 아니라 프로세스 자격 증명에 작동합니다. 프로세스에는 서로 관련되지만 역할이 다른 사용자 및 그룹 ID가 여러 개 있습니다. 대부분의 일반 프로그램은 일치하는 신원으로 시작하고 권한 프로그램은 서로 다른 값을 의도적으로 사용할 수 있습니다.

## 실제 사용자 ID

실제 사용자 ID는 프로세스를 시작한 계정이나 그 조상 로그인 세션을 식별합니다. 프로그램은 이를 확인하여 호출자를 높은 유효 신원과 구분할 수 있습니다.

사용자 Bob이 시작한 일반 명령의 실제 사용자 ID는 보통 Bob의 UID와 같습니다. 다른 프로세스를 만든다고 그 자체로 새 계정이 생기거나 이 신원이 바뀌지는 않습니다.

:::single-choice{#process-permissions-real-uid} 프로세스의 실제 사용자 ID는 일반적으로 무엇을 식별하나요?

::option[가장 최근에 연 파일의 소유자]{#process-permissions-real-opened-file explanation="파일을 열어도 프로세스의 실제 UID가 해당 파일 소유자로 바뀌지 않습니다."}
::option[프로세스의 원래 호출자와 연결된 계정]{#process-permissions-real-caller .correct explanation="실제 UID는 프로세스를 시작할 때 상속된 호출 사용자 신원을 기록합니다."}
::option[모든 접근 검사에 선택되는 그룹]{#process-permissions-real-group explanation="UID는 사용자 신원이며 그룹 검사는 별도의 그룹 자격 증명을 사용합니다."}
:::

## 유효 사용자 ID

유효 사용자 ID는 여러 파일 시스템 및 권한 검사에 쓰이는 사용자 자격 증명입니다. 일반적으로 실제 UID와 일치합니다. 적용되는 setuid 프로그램을 실행하면 대신 실행 파일 소유자에서 초기화될 수 있습니다.

예를 들어 신중하게 설계된 비밀번호 유틸리티는 보호된 인증 데이터를 갱신하기 위해 높은 유효 UID로 실행될 수 있습니다. 프로그램은 여전히 호출자, 요청 계정, PAM 결과, 다른 문맥에 따라 정책을 적용해야 합니다. 유효 UID를 가졌다고 요청한 모든 작업이 자동으로 정당해지는 것은 아닙니다.

:::single-choice{#process-permissions-effective-uid} 프로세스를 대신한 여러 접근 제어 결정에 사용되는 사용자 ID는 무엇인가요?

::option[유효 사용자 ID]{#process-permissions-effective-active .correct explanation="유효 UID는 여러 권한 검사에서 확인하는 활성 사용자 자격 증명입니다."}
::option[저장 사용자 ID만 사용]{#process-permissions-effective-saved-only explanation="저장 ID는 자격 증명 전환을 지원하지만 일반적으로 접근 검사의 활성 신원은 아닙니다."}
::option[현재 디렉터리에 저장된 UID]{#process-permissions-effective-directory explanation="파일 시스템 소유권은 객체 메타데이터이며 프로세스의 활성 사용자 자격 증명이 아닙니다."}
:::

## 저장 Set-User-ID

저장 set-user-ID는 시스템 호출 규칙에 따라 프로그램이 나중에 복원할 수 있는 신원을 유지하게 합니다. 권한 프로그램은 유효 UID를 권한이 더 낮은 값으로 잠시 바꾸고 낮은 권한으로 일반 작업을 수행한 뒤 좁은 범위의 작업에만 저장 신원을 복원할 수 있습니다.

올바르게 구현하면 프로그램 전체에서 높은 권한을 유지하는 것보다 안전합니다. 더 이상 필요하지 않을 때 권한을 영구적으로 버리고 모든 자격 증명 변경 호출의 실패 여부를 확인해야 합니다.

:::single-choice{#process-permissions-saved-uid} 권한 프로그램이 저장 set-user-ID를 유지할 수 있는 이유는 무엇인가요?

::option[통제된 권한 단계와 비권한 단계에서 유효 신원을 전환하기 위해]{#process-permissions-saved-switch .correct explanation="저장 신원은 일시적인 권한 축소와 허용된 나중 복원을 지원할 수 있습니다."}
::option[읽는 모든 파일에 해당 UID를 자동으로 할당하기 위해]{#process-permissions-saved-file-owner explanation="파일을 읽어도 소유권이 프로세스의 저장 UID로 바뀌지 않습니다."}
::option[프로세스의 시스템 계정 데이터베이스를 대체하기 위해]{#process-permissions-saved-database explanation="프로세스 자격 증명은 계정 레코드나 이름 서비스 데이터를 대체하지 않습니다."}
:::

## 사용자 ID는 자격 증명 집합의 일부일 뿐

프로세스에는 실제, 유효, 저장, 보조 그룹 자격 증명도 있습니다. 파일 시스템 ID, capabilities, 네임스페이스, 보안 모듈, ACL, 마운트 옵션, 서비스 정책이 권한에 더 영향을 줄 수 있습니다. 따라서 “UID가 허용한다”는 설명은 완전한 설명의 일부일 때가 많습니다.

Linux에서는 `ps`와 `/proc/PROCESS/status` 같은 도구로 자격 증명을 확인합니다. 필드 제공 여부와 표시 형식이 다르므로 로컬 문서를 확인하고 공유 시스템에서 단순 실험을 위해 자격 증명을 바꾸지 마세요.

:::single-choice{#process-permissions-ordinary-identities} 권한 전환이 없는 대부분의 일반 명령에서 실제 UID와 유효 UID는 어떻게 비교되나요?

::option[유효 UID는 항상 0입니다.]{#process-permissions-effective-root explanation="일반 명령은 자동으로 root의 UID를 받지 않습니다."}
::option[실제 UID는 항상 실행 파일 소유자와 같습니다.]{#process-permissions-real-file-owner explanation="실행 파일 소유자는 setuid 동작에 영향을 주며 일반 실제 UID에는 영향을 주지 않습니다."}
::option[일반적으로 호출 사용자의 UID와 서로 일치합니다.]{#process-permissions-uids-match .correct explanation="Setuid나 명시적인 자격 증명 변경이 없으면 일반 프로세스는 보통 일치하는 실제 및 유효 신원으로 실행됩니다."}
:::

## 요약

이제 Linux 프로세스가 여러 사용자 신원을 가질 수 있는 이유를 설명할 수 있습니다.

1. 실제 UID로 원래 호출자를 식별할 수 있습니다.
2. 유효 UID를 활성 권한 검사와 연결할 수 있습니다.
3. 저장 신원으로 통제된 권한 전환을 이해할 수 있습니다.
4. 그룹 ID와 추가 보안 메커니즘을 전체 결정의 일부로 고려할 수 있습니다.
