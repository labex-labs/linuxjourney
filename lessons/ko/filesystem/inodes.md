---
lesson_id: "inodes"
course_id: "filesystem"
lang: "ko"
order_index: 11
title: "Inode"
description: "inode 번호가 디렉터리 이름을 파일 시스템 객체의 메타데이터 및 데이터와 연결하는 방법을 알아봅니다."
meta_title: "Inode - 파일 시스템"
meta_description: "리눅스 inode의 개념을 살펴봅니다. inode가 파일 메타데이터를 관리하는 방식과 df -i 및 ls -li로 inode 사용량을 확인하는 방법을 알아봅니다."
meta_keywords: "리눅스 inode, inode, inode 번호, 파일 시스템, df -i, ls -li, stat"
---

inode 기반 유닉스 파일 시스템에서 디렉터리는 각 항목 이름을 inode 번호에 매핑합니다. inode는 파일 시스템 객체를 나타내며 그 데이터를 찾고 해석하는 데 필요한 메타데이터를 기록합니다. 따라서 경로 이름은 객체 자체의 주 식별자로 저장되지 않습니다.

## Inode와 함께 저장되는 메타데이터

inode와 관련된 일반적인 메타데이터는 다음과 같습니다.

- 객체 유형 및 권한 모드
- 사용자 및 그룹 소유권
- 논리 크기 및 할당 블록 회계
- 하드 링크 수
- 접근, 수정 및 상태 변경 타임스탬프
- 파일 데이터 또는 파일 시스템별 익스텐트 구조에 대한 참조

inode에는 일반적으로 디렉터리 항목의 이름이 저장되지 않습니다. 파일 시스템은 형식별 구조를 통해 확장 속성, 접근 제어 목록, 생성 시간, 인라인 데이터 또는 다른 정보를 저장할 수도 있습니다.

`ctime`은 inode 상태 변경 시간이며 반드시 파일 생성 시간은 아닙니다. 별도의 생성 타임스탬프는 선택 사항이며 제공되지 않을 수 있습니다.

:::single-choice{#inodes-name-location}
일반 파일의 경로 이름 구성 요소는 보통 어디에서 inode 번호와 연결됩니까?

::option[프로세스 스케줄러입니다.]{#inodes-scheduler-name explanation="CPU 스케줄링 상태는 파일 시스템 경로 조회를 구현하지 않습니다."}
::option[디렉터리 항목입니다.]{#inodes-directory-entry .correct explanation="디렉터리는 해당 파일 시스템 안에서 이름을 inode 번호에 매핑합니다."}
::option[디스크의 파티션 테이블입니다.]{#inodes-partition-name explanation="파티션 테이블은 개별 파일 이름이 아니라 저장 공간 영역을 매핑합니다."}
:::

## Inode 번호와 파일 시스템 범위

다음 명령으로 inode 번호를 표시합니다.

```bash
$ ls -li
```

첫 번째 필드가 inode 번호입니다. 객체 하나를 더 자세히 검사합니다.

```bash
$ stat path
```

inode 번호는 특정 시점의 한 파일 시스템 안에서만 고유합니다. 다른 파일 시스템에 같은 번호가 있을 수 있고 inode가 해제된 뒤 번호를 다시 사용할 수도 있습니다. 객체를 안정적으로 식별하려면 inode 번호만 사용하지 말고 파일 시스템 식별 정보와 inode 번호를 함께 사용하십시오.

:::single-choice{#inodes-number-scope}
inode 번호는 어느 범위에서 객체 식별자입니까?

::option[전 세계 모든 리눅스 시스템에서 영원히 고유합니다.]{#inodes-global-forever explanation="inode 할당은 파일 시스템에 국한되며 식별자를 다시 사용할 수 있습니다."}
::option[특정 시점의 한 파일 시스템 안입니다.]{#inodes-one-filesystem .correct explanation="다른 파일 시스템에서 같은 번호를 사용할 수 있고 해제된 inode 번호는 나중에 재사용될 수 있습니다."}
::option[파일을 만든 셸 프로세스 안에서만 고유합니다.]{#inodes-shell-scope explanation="inode 식별 정보는 하나의 셸이 아니라 파일 시스템이 유지합니다."}
:::

## 하드 링크와 열린 참조

여러 디렉터리 항목이 같은 inode를 가리킬 수 있으며 이를 하드 링크라고 합니다. 하드 링크를 하나 더 만들면 객체의 링크 수가 증가합니다. 이름 하나를 제거하면 링크 수가 감소하지만 다른 링크가 남아 있는 동안 데이터는 삭제되지 않습니다.

마지막 디렉터리 항목을 제거한 뒤에도 열린 파일은 마지막 프로세스 참조가 닫힐 때까지 할당된 상태로 남습니다. 링크 수가 0이어도 파일 디스크립터를 통해 계속 접근할 수 있습니다. 이 때문에 열린 대용량 로그를 삭제해도 `df` 사용량이 즉시 줄지 않을 수 있습니다.

:::single-choice{#inodes-unlinked-open-file}
링크가 해제된 파일의 리소스는 일반적으로 언제 해제됩니까?

::option[하드 링크 이름 하나를 제거한 직후입니다.]{#inodes-one-link-removed explanation="다른 하드 링크나 열린 참조가 객체를 유지할 수 있습니다."}
::option[전체 파일 시스템을 다시 포맷할 때만 해제됩니다.]{#inodes-reformat-only explanation="일반적인 링크 해제와 닫기 작업이 사용되지 않는 inode와 블록을 회수합니다."}
::option[링크 수가 0이고 마지막 열린 참조가 닫힌 뒤입니다.]{#inodes-zero-links-no-opens .correct explanation="디렉터리 이름과 프로세스 파일 디스크립터는 inode에 대한 독립적인 참조입니다."}
:::

## Inode 용량

유한하거나 보고 가능한 inode 풀을 가진 파일 시스템에서는 수백만 개의 작은 파일 때문에 데이터 블록보다 메타데이터 용량이 먼저 고갈될 수 있습니다. 다음 명령으로 마운트된 파일 시스템의 inode 회계를 검사합니다.

```bash
$ df -i
```

여유 inode가 없으면 `df -h`에 여유 블록이 표시되어도 새 파일 생성이 실패할 수 있습니다. 할당 방식은 서로 다릅니다. 일부 파일 시스템은 생성 시 inode 구조를 미리 할당하지만 다른 파일 시스템은 메타데이터를 동적으로 관리하고 inode 용량을 다르게 보고할 수 있습니다.

:::single-choice{#inodes-df-i-purpose}
파일 시스템이 inode 회계를 제공할 때 `df -i`가 보고하는 것은 무엇입니까?

::option[inode 순서로 모든 파일의 내용을 보고합니다.]{#inodes-df-i-content explanation="df는 전체 파일 시스템 통계를 보고하며 파일 내용을 읽지 않습니다."}
::option[사용 중인 inode와 사용 가능한 inode 용량입니다.]{#inodes-df-i-capacity .correct explanation="inode 뷰는 데이터 블록과 별개인 메타데이터 객체 고갈을 진단하는 데 도움을 줍니다."}
::option[디스크 펌웨어 버전입니다.]{#inodes-df-i-firmware explanation="펌웨어 목록은 inode 사용량과 관련이 없습니다."}
:::

## 파일 시스템별 데이터 매핑

모든 inode가 정확히 12개의 직접 포인터와 3개의 간접 포인터를 가진다고 가정하지 마십시오. 이는 일부 고전적인 파일 시스템 레이아웃을 설명하는 데는 유용하지만 최신 ext4는 익스텐트를 사용할 수 있고 XFS, Btrfs 및 다른 파일 시스템은 서로 다른 구조를 사용합니다. 인라인 데이터, 압축 또는 쓰기 시 복사 익스텐트도 관계를 바꿉니다.

내부 매핑이 중요할 때는 파일 시스템별 진단 도구를 읽기 전용 또는 문서화된 모드로만 사용하십시오. 일반적인 관리에는 `stat`, `find -inum`, `df -i` 및 링크를 인식하는 도구가 더 안전한 추상화를 제공합니다.

:::single-choice{#inodes-layout-portability}
모든 inode에 하나의 고정 포인터 레이아웃이 있다고 가정해서는 안 되는 이유는 무엇입니까?

::option[inode가 어떤 방식으로도 파일 데이터를 참조하지 않기 때문입니다.]{#inodes-no-data-reference explanation="메커니즘은 달라도 파일 시스템은 객체를 콘텐츠와 연결해야 합니다."}
::option[파일 시스템 구현마다 서로 다른 익스텐트, 트리 및 인라인 데이터 구조를 사용하기 때문입니다.]{#inodes-format-specific-layout .correct explanation="inode에서 콘텐츠로의 디스크 내 매핑은 각 파일 시스템 형식의 일부입니다."}
::option[파일 소유자가 inode 레이아웃을 각각 선택하기 때문입니다.]{#inodes-owner-layout explanation="메타데이터 구조는 파일 시스템 구현과 형식이 결정합니다."}
:::

[리눅스 파일과 디렉터리 관리하기](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835)에서 폐기 가능한 파일의 inode 번호와 링크 수를 비교해 보십시오.

## 요약

이제 경로 이름, inode, 링크 및 파일 시스템 용량의 관계를 설명할 수 있습니다.

1. 디렉터리 항목을 이름에서 inode 번호로의 매핑으로 취급합니다.
2. `ctime`을 생성 시간으로 오해하지 않고 메타데이터와 타임스탬프를 읽습니다.
3. inode 번호의 범위를 특정 시점의 한 파일 시스템으로 한정합니다.
4. 하드 링크와 열린 파일 디스크립터를 모두 고려합니다.
5. 하나의 범용 포인터 레이아웃 대신 파일 시스템별 모델을 사용합니다.
