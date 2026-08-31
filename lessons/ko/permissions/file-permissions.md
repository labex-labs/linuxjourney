---
lesson_id: "file-permissions"
course_id: "permissions"
lang: "ko"
order_index: 1
title: "파일 권한"
description: "Linux 파일 형식과 소유자, 그룹, 기타 사용자 권한 비트를 읽는 방법을 배웁니다."
meta_title: "파일 권한 - Permissions"
meta_description: "Linux 파일 권한을 배웁니다. 사용자, 그룹, 기타 사용자의 rwx 비트를 이해하고 ls -l 출력과 파일 모드를 익혀 보세요."
meta_keywords: "파일 권한, linux 파일 권한, linux 학습, linux 튜토리얼, rwx 권한, ls -l 명령, 파일 모드, linux 가이드"
---

Linux는 많은 자원을 파일과 유사한 인터페이스로 나타내며 각 파일 시스템 객체에는 접근을 제어하는 메타데이터가 있습니다. 이 메타데이터를 읽는 것은 파일과 디렉터리를 안전하게 다루는 기초입니다.

## 긴 목록 읽기

`ls -l`로 긴 목록을 표시합니다.

```bash
$ ls -ld Desktop/
drwxr-xr-x 2 pete penguins 4096 Dec 1 11:45 Desktop/
```

첫 번째 필드 `drwxr-xr-x`는 파일 형식 문자 하나와 권한 문자 아홉 개를 결합합니다. 목록은 `pete`가 소유자이고 `penguins`가 디렉터리와 연결된 그룹임도 나타냅니다.

첫 문자는 객체 형식을 설명합니다. 흔한 값은 다음과 같습니다.

- `-`: 일반 파일
- `d`: 디렉터리
- `l`: 심볼릭 링크

다른 특수 파일 형식도 있습니다. 나머지 아홉 문자는 접근 권한입니다.

```text
d | rwx | r-x | r-x
```

:::single-choice{#file-permissions-type-character}
`drwxr-xr-x`에서 첫 번째 `d`는 무엇을 나타내나요?

::option[객체가 심볼릭 링크입니다.]{#file-permissions-type-link explanation="심볼릭 링크는 일반적으로 파일 형식 위치에 `l`로 표시됩니다."}
::option[객체가 디렉터리입니다.]{#file-permissions-type-directory .correct explanation="첫 문자는 파일 형식이며 `d`는 디렉터리를 식별합니다."}
::option[소유자에게 삭제 권한이 있습니다.]{#file-permissions-type-delete explanation="Linux 모드 문자열은 `d`를 삭제 권한으로 사용하지 않으며 첫 위치는 객체 형식을 설명합니다."}
:::

## r, w, x 이해하기

각 권한 세 글자는 다음 문자를 사용합니다.

- `r`: 읽기 권한 부여
- `w`: 쓰기 권한 부여
- `x`: 실행 권한 부여
- `-`: 해당 권한 없음

일반 파일에서 읽기는 내용 접근, 쓰기는 내용 수정, 실행은 커널이 프로그램으로 실행을 시도하도록 허용합니다. 파일 형식, 인터프리터 줄, 마운트 옵션 또는 다른 보안 제어가 허용하지 않으면 실행은 여전히 실패할 수 있습니다.

디렉터리에서는 디렉터리 항목에 대한 의미를 갖습니다.

- 읽기: 디렉터리의 이름 목록 표시 허용
- 쓰기: 일반적으로 실행 권한과 함께 항목 생성 또는 제거 허용
- 실행: 검색 권한이라고도 하며 디렉터리를 통과하고 이름으로 항목에 접근하도록 허용

파일 삭제는 주로 파일 자체의 쓰기 비트가 아니라 상위 디렉터리 권한의 지배를 받습니다.

:::single-choice{#file-permissions-directory-execute}
디렉터리의 실행 권한은 주로 무엇을 허용하나요?

::option[디렉터리에 저장된 모든 일반 파일 실행]{#file-permissions-directory-run-files explanation="디렉터리 실행 비트는 안의 각 파일에 실행 권한을 부여하지 않습니다."}
::option[디렉터리 안 모든 파일 내용 변경]{#file-permissions-directory-edit-files explanation="파일 내용 쓰기는 파일 권한과 다른 접근 제어에 따라 달라집니다."}
::option[디렉터리를 통과하고 이름으로 항목에 접근]{#file-permissions-directory-search .correct explanation="디렉터리 실행, 즉 검색 권한은 해당 디렉터리를 통한 경로 탐색을 허용합니다."}
:::

## 소유자, 그룹, 기타 사용자 클래스

모드 문자 아홉 개는 고정된 순서의 세 묶음으로 구성됩니다.

1. **소유자**: 프로세스의 유효 사용자 ID가 파일 소유자와 일치할 때 사용되는 권한
2. **그룹**: 적용 가능한 프로세스 그룹 ID가 파일 그룹과 일치할 때 사용되는 권한
3. **기타 사용자**: 앞의 두 클래스가 모두 일치하지 않을 때 사용되는 권한

커널은 적용 가능한 클래스 하나를 선택하며 가장 허용적인 결과를 찾기 위해 세 묶음을 결합하지 않습니다. 접근 제어 목록, 마운트 옵션, 기능, 강제 접근 제어 같은 추가 메커니즘이 최종 결정에 더 영향을 줄 수 있습니다.

예제에서 소유자 묶음은 `rwx`, 그룹과 기타 사용자는 모두 `r-x`입니다. 소유자는 디렉터리를 읽고 쓰고 검색할 수 있습니다. 그룹과 기타 사용자는 읽고 검색할 수 있지만 일반 모드 비트를 통해 항목을 만들거나 제거할 수는 없습니다.

:::single-choice{#file-permissions-triplet-order}
파일 형식 문자 뒤에 권한 세 묶음은 어떤 순서로 나타나나요?

::option[그룹, 소유자, 기타 사용자]{#file-permissions-order-group-first explanation="그룹 묶음은 첫 번째가 아니라 두 번째입니다."}
::option[기타 사용자, 그룹, 소유자]{#file-permissions-order-other-first explanation="기타 사용자 묶음은 마지막이고 소유자 묶음은 첫 번째입니다."}
::option[소유자, 그룹, 기타 사용자]{#file-permissions-order-owner-first .correct explanation="권한 문자 아홉 개는 항상 소유자, 그룹, 기타 사용자 순서입니다."}
:::

:::single-choice{#file-permissions-example-group}
`drwxr-xr-x`에서 그룹 클래스는 어떤 일반 권한을 갖나요?

::option[읽기와 쓰기]{#file-permissions-group-read-write explanation="그룹 묶음은 `r-x`이므로 쓰기 위치에 `-`가 있습니다."}
::option[쓰기와 실행]{#file-permissions-group-write-execute explanation="그룹 묶음의 첫 위치에는 `w`가 아니라 `r`이 있습니다."}
::option[읽기와 실행]{#file-permissions-group-read-execute .correct explanation="가운데 묶음 `r-x`는 읽기와 실행을 허용하고 쓰기는 허용하지 않습니다."}
:::

격리된 환경에서 개념을 강화하려면 [Linux 사용자 그룹과 파일 권한](https://labex.io/ko/labs/linux-linux-user-group-and-file-permissions-18002) 실습을 진행해 보세요. 모드를 읽고 소유권과 권한을 변경하는 방법을 연습합니다.

## 요약

이제 Linux 긴 목록의 기본 권한 필드를 해석할 수 있습니다.

1. 파일 형식 문자와 권한 비트 아홉 개를 분리할 수 있습니다.
2. 객체가 파일인지 디렉터리인지에 따라 `r`, `w`, `x`를 해석할 수 있습니다.
3. 모드를 소유자, 그룹, 기타 사용자 묶음으로 나눌 수 있습니다.
4. 권한 묶음을 `ls -l`이 표시한 소유자 및 그룹과 연결할 수 있습니다.
