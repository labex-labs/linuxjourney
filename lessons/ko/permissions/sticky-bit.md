---
lesson_id: "sticky-bit"
course_id: "permissions"
lang: "ko"
order_index: 8
title: "Sticky 비트"
description: "sticky 비트가 /tmp 같은 공유 쓰기 가능 디렉터리의 항목을 보호하는 방법을 배웁니다."
meta_title: "Sticky 비트 - Permissions"
meta_description: "Linux 및 Unix 파일 권한에서 sticky 비트의 목적을 알아봅니다. /tmp 같은 공유 디렉터리의 파일을 보호하고 chmod로 설정하는 방법을 배웁니다."
meta_keywords: "sticky 비트, sticky bit linux, unix 파일 권한 sticky 비트, chmod +t, /tmp 디렉터리, 파일 권한, linux 보안"
---

쓰기 가능한 디렉터리는 일반적으로 권한 있는 사용자가 파일 자체를 소유하지 않아도 안의 항목을 제거하거나 이름을 바꿀 수 있게 합니다. sticky 비트는 소유권 제한을 추가하여 공유 쓰기 가능 디렉터리를 더 안전하게 만듭니다.

## Sticky 비트가 제거를 제한하는 방식

디렉터리에 sticky 비트가 설정되면 Linux는 일반적으로 적절한 권한이 있는 프로세스, 디렉터리 소유자 또는 항목 소유자만 항목을 제거하거나 이름을 바꾸도록 허용합니다. 일반 디렉터리 쓰기 및 검색 권한도 여전히 필요합니다.

이 제한은 디렉터리 항목을 다룹니다. 파일 권한이 허용한다면 파일 소유자가 파일 내용을 편집하는 일을 막지 않고 디렉터리를 비공개로 만들지도 않습니다.

:::single-choice{#sticky-bit-removal-rule} Sticky가 설정된 공유 디렉터리에서 특정 항목을 일반적으로 제거할 수 있는 일반 사용자는 누구인가요?

::option[디렉터리 목록을 볼 수 있는 모든 사용자]{#sticky-bit-any-reader explanation="디렉터리 읽기 권한은 이름을 노출할 수 있지만 sticky 소유권 제한을 우회하지 않습니다."}
::option[필요한 디렉터리 접근 권한을 가진 항목 소유자]{#sticky-bit-entry-owner .correct explanation="항목 소유자는 sticky 디렉터리 규칙에서 일반적으로 허용되는 신원 중 하나입니다."}
::option[항목 그룹의 구성원만 가능]{#sticky-bit-entry-group explanation="그룹 멤버십만으로는 sticky 비트가 정의한 소유권 예외가 되지 않습니다."}
:::

## /tmp에서 비트 알아보기

시스템 임시 디렉터리가 흔한 예입니다.

```bash
$ ls -ld /tmp
drwxrwxrwt 17 root root 4096 Dec 15 11:45 /tmp
```

마지막 소문자 `t`는 기타 사용자 실행 위치에 있습니다. sticky 비트와 기타 사용자 실행 권한이 모두 있음을 뜻합니다. 대문자 `T`는 sticky 비트가 설정되었지만 기타 사용자 실행 권한은 없다는 뜻입니다.

`/tmp`는 일반적으로 모두가 쓰고 검색할 수 있으므로 여러 사용자가 항목을 만들 수 있습니다. sticky 비트는 디렉터리가 모두에게 쓰기 가능하다는 이유만으로 일반 사용자가 다른 사용자의 항목을 제거하지 못하게 합니다. 예측 가능한 이름, 안전하지 않은 링크, 약한 파일 모드는 별도의 위험이므로 애플리케이션은 여전히 임시 객체를 안전하게 만들어야 합니다.

:::single-choice{#sticky-bit-lowercase-t} 디렉터리 모드 끝의 소문자 `t`는 무엇을 나타내나요?

::option[Sticky와 기타 사용자 실행이 모두 설정되어 있습니다.]{#sticky-bit-t-with-execute .correct explanation="소문자 `t`는 sticky 특수 비트와 일반 기타 사용자 실행 비트를 결합합니다."}
::option[Sticky는 설정되었지만 기타 사용자 실행은 없습니다.]{#sticky-bit-t-without-execute explanation="이 조합은 대문자 `T`로 표시됩니다."}
::option[Setgid와 그룹 실행이 모두 설정되어 있습니다.]{#sticky-bit-setgid-position explanation="Setgid는 마지막 기타 사용자 위치가 아니라 그룹 실행 위치에 나타납니다."}
:::

## Sticky 비트 설정하고 제거하기

기호 방식으로 비트를 설정합니다.

```bash
$ chmod +t shared-directory
```

선행 특수 비트 8진수 숫자에서 sticky는 `1`을 더합니다.

```bash
$ chmod 1777 shared-directory
```

선행 `1`은 sticky를 설정하고 `777`은 일반 모드를 제공합니다. 이 모드는 디렉터리를 모든 로컬 사용자가 의도적으로 공유할 때만 적절합니다. 팀 디렉터리에는 더 좁은 그룹 권한이 나을 수 있습니다. `chmod -t shared-directory`로 sticky 비트만 제거합니다.

:::single-choice{#sticky-bit-octal-value} Sticky 비트를 나타내는 선행 8진수 값은 무엇인가요?

::option[`2`]{#sticky-bit-value-two explanation="선행 `2`는 setgid를 나타냅니다."}
::option[`1`]{#sticky-bit-value-one .correct explanation="Sticky 비트는 선행 특수 비트 숫자에 `1`을 더합니다."}
::option[`4`]{#sticky-bit-value-four explanation="선행 `4`는 setuid를 나타냅니다."}
:::

## 전체 디렉터리 정책 검증하기

Sticky는 쓰기나 검색 접근을 부여하지 않습니다. 일반 권한이 디렉터리 수정을 허용한 뒤 제거와 이름 변경을 제한할 뿐입니다. 디렉터리 소유자, 그룹, 일반 모드, ACL, 마운트 문맥을 함께 확인하세요. 작동 중인 시스템의 `/tmp`를 바꾸지 말고 격리된 환경의 비권한 계정으로 시험합니다.

:::single-choice{#sticky-bit-access-scope} Sticky 비트를 추가하면 쓰기 불가능한 디렉터리가 다른 사용자에게 쓰기 가능해지나요?

::option[예. sticky는 모든 클래스에 쓰기를 자동으로 추가합니다.]{#sticky-bit-adds-write explanation="특수 비트는 소유자, 그룹, 기타 사용자 쓰기 비트를 다시 쓰지 않습니다."}
::option[예. sticky는 디렉터리의 기타 사용자 권한 묶음을 비활성화합니다.]{#sticky-bit-disables-other explanation="기타 사용자 묶음은 일반 접근 검사에 계속 참여합니다."}
::option[아니요. 일반 쓰기 및 검색 권한이 여전히 접근을 제어합니다.]{#sticky-bit-no-write-grant .correct explanation="Sticky는 일부 제거 및 이름 변경 작업을 제한하지만 없는 일반 권한을 추가하지 않습니다."}
:::

연습하려면 일회용 공유 디렉터리를 만들고 적절한 일반 모드와 sticky 비트를 설정한 뒤 비권한 사용자 두 명으로 항목 제거를 시험하세요. [파일 삭제 및 이동](https://labex.io/ko/labs/linux-delete-and-move-files-7777) 실습으로 기본 이름 변경 및 삭제 작업을 강화할 수 있습니다.

## 요약

이제 공유 디렉터리의 sticky 비트를 설명하고 검증할 수 있습니다.

1. Sticky를 제거 및 이름 변경의 소유권 제한과 연결할 수 있습니다.
2. 긴 목록에서 소문자 `t`와 대문자 `T`를 알아볼 수 있습니다.
3. 기호 방식이나 선행 8진수 값 `1`로 비트를 설정할 수 있습니다.
4. Sticky를 일반 디렉터리 권한과 함께 평가할 수 있습니다.
