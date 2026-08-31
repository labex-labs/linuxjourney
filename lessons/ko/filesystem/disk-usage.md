---
lesson_id: "disk-usage"
course_id: "filesystem"
lang: "ko"
order_index: 9
title: "디스크 사용량"
description: "`df`와 `du`가 파일 시스템 블록 및 inode 소비를 서로 다른 관점에서 측정하는 방법을 알아봅니다."
meta_title: "디스크 사용량 - 파일 시스템"
meta_description: "df와 du 명령으로 리눅스 디스크 사용량과 여유 공간을 확인하는 방법을 알아봅니다. df -i를 통한 inode 사용량과 공간을 차지하는 파일 분석을 설명합니다."
meta_keywords: "df 명령어, du 명령어, 리눅스 디스크 사용량, 여유 공간 확인, df -i, 디스크 관리, 파일 시스템 사용량"
---

파일 시스템 용량에는 데이터 블록과 inode 같은 메타데이터 객체라는 두 가지 이상의 한계가 있습니다. `df`는 파일 시스템 관점의 할당을 보고하고 `du`는 도달 가능한 경로 이름을 순회하여 그 경로에 귀속된 사용량을 합산합니다. 두 값은 서로 다른 질문에 답하므로 일치할 필요가 없습니다.

## `df`로 파일 시스템 용량 확인하기

마운트된 파일 시스템 유형과 사람이 읽기 쉬운 블록 수치를 표시합니다.

```bash
$ df -hT
Filesystem     Type  Size  Used Avail Use% Mounted on
/dev/sda1      ext4  6.2G  2.3G  3.6G  40% /
```

`Size`, `Used` 및 `Avail`은 파일 시스템 회계 정보에서 가져옵니다. 예약 블록, 메타데이터, 할당 정책, 할당량 또는 반올림 때문에 사용 가능 공간이 전체 용량에서 사용량을 뺀 값보다 작을 수 있습니다. 경로가 포함된 파일 시스템을 보고하려면 해당 경로에 `df`를 실행합니다.

```bash
$ df -hT /var/log
```

:::single-choice{#disk-usage-df-scope}
`df`가 주로 보고하는 것은 무엇입니까?

::option[한 디렉터리 안의 각 파일 바이트 내용입니다.]{#disk-usage-df-file-content explanation="디렉터리 트리 회계는 `du` 같은 도구의 역할입니다."}
::option[파일 시스템 수준의 용량, 사용량 및 사용 가능 공간입니다.]{#disk-usage-df-filesystem .correct explanation="df는 모든 경로 이름을 순회하지 않고 마운트된 파일 시스템의 할당 통계를 조회합니다."}
::option[디스크 레이블에 인쇄된 물리 크기만 보고합니다.]{#disk-usage-df-physical-label explanation="수치는 단순한 하드웨어 표기 용량이 아니라 파일 시스템 회계 정보를 설명합니다."}
:::

## Inode 용량

inode와 유사한 객체를 할당하는 파일 시스템은 블록이 남아 있어도 inode가 고갈될 수 있습니다.

```bash
$ df -i /var
```

작은 파일이 매우 많으면 사용 가능한 inode를 모두 소비할 수 있습니다. 큰 파일 하나를 삭제하면 많은 블록이 해제되지만 일반적으로 inode는 하나만 해제됩니다. 필요 없는 작은 파일을 여러 개 삭제하면 inode 압력을 완화할 수 있습니다. 일부 파일 시스템은 메타데이터를 동적으로 할당하고 이러한 개념을 다르게 보고합니다.

:::single-choice{#disk-usage-inode-exhaustion}
파일 시스템에 여유 블록이 있지만 여유 inode가 없으면 어떤 일이 생길 수 있습니까?

::option[모든 기존 파일의 크기가 자동으로 두 배가 됩니다.]{#disk-usage-inode-double explanation="inode 고갈은 새 메타데이터 할당을 막을 뿐 기존 콘텐츠를 확장하지 않습니다."}
::option[새 파일 생성이 실패할 수 있습니다.]{#disk-usage-inode-create-fail .correct explanation="파일 데이터 공간이 남아 있어도 새 파일 시스템 객체에는 메타데이터가 필요합니다."}
::option[파일 시스템이 스왑으로 변환됩니다.]{#disk-usage-inode-swap explanation="리소스 고갈로 파일 시스템 유형이 바뀌지는 않습니다."}
:::

## `du`로 경로 사용량 확인하기

한 디렉터리 아래에서 도달 가능한 할당 공간을 요약합니다.

```bash
$ du -sh /var/log
```

한 파일 시스템 안에서 바로 아래의 하위 항목을 비교합니다.

```bash
$ sudo du -xhd1 /var | sort -h
```

여기에 나온 GNU 옵션은 각각 사람이 읽기 쉬운 출력, 최대 깊이 1 및 한 파일 시스템을 뜻합니다. 권한 때문에 일부 하위 트리가 보이지 않으면 합계가 불완전할 수 있습니다. `du`는 기본적으로 하드 링크된 파일을 한 번만 셀 수 있고, 겉보기 크기와 할당된 블록을 구분하며, 옵션에 따라 희소 파일을 다르게 처리합니다.

:::single-choice{#disk-usage-du-purpose}
`/var/log` 아래의 할당 사용량을 요약하는 명령은 무엇입니까?

::option[`df -i /var/log`]{#disk-usage-df-inodes explanation="이 명령은 해당 경로가 포함된 파일 시스템의 inode 통계를 보고합니다."}
::option[`du -sh /var/log`]{#disk-usage-du-summary .correct explanation="du는 지정한 트리를 순회하고 `-s`는 사람이 읽기 쉬운 단위로 요약 하나를 출력합니다."}
::option[`mount -a /var/log`]{#disk-usage-mount-a explanation="마운트는 읽기 전용 디렉터리 사용량 요약과 관련이 없습니다."}
:::

## `df`와 `du`가 다른 이유

일반적인 원인은 다음과 같습니다.

- 프로세스가 삭제된 파일을 계속 열고 있어 `du`가 찾을 경로 이름은 없지만 블록은 할당된 상태
- 파일 시스템 메타데이터, 예약 공간, 저널, reflink, 스냅샷 또는 압축이 회계에 영향
- 순회한 트리 안에 다른 파일 시스템이 마운트됨
- 권한 때문에 `du`가 일부 디렉터리를 읽지 못함
- 희소 파일의 겉보기 크기와 할당된 크기가 다름

삭제됐지만 열린 파일은 권한이 있는 상태에서 `lsof +L1` 같은 도구로 프로세스를 검사하십시오. 알 수 없는 디스크립터를 잘라내지 말고 정상 절차에 따라 책임 있는 서비스를 재시작하거나 신호를 보내십시오.

:::single-choice{#disk-usage-deleted-open-file}
`df`에는 사용 중으로 나타나지만 경로 기반 `du`가 찾지 못하는 공간이 생길 수 있는 이유는 무엇입니까?

::option[`df`가 항상 모든 파일 크기에 2를 곱하기 때문입니다.]{#disk-usage-df-doubles explanation="그러한 보편적인 배수 규칙은 없습니다."}
::option[삭제된 파일이 실행 중인 프로세스에 열린 채 할당되어 있을 수 있기 때문입니다.]{#disk-usage-open-deleted .correct explanation="디렉터리 항목은 사라졌지만 마지막 열린 참조가 닫힐 때까지 파일 시스템이 블록을 유지합니다."}
::option[`du`가 파일을 센 뒤 자동으로 삭제하기 때문입니다.]{#disk-usage-du-deletes explanation="du는 회계 도구이며 순회한 파일을 제거하지 않습니다."}
:::

## 상황을 악화시키지 않고 조사하기

`df`가 가득 찼다고 보고한 파일 시스템에서 시작하고 `findmnt`로 마운트 대상을 식별한 뒤 같은 파일 시스템 안에서 `du` 검색 범위를 좁힙니다. 스냅샷, 컨테이너 계층, 로그, 패키지 캐시 및 애플리케이션 보존 정책을 고려하십시오. 크다는 이유만으로 파일을 삭제하지 말고 먼저 소유권, 백업, 규정 준수 및 서비스 동작을 확인합니다.

:::single-choice{#disk-usage-safe-investigation}
큰 파일을 찾았을 때 가장 안전한 대응은 무엇입니까?

::option[서비스가 쓰는 동안 즉시 삭제합니다.]{#disk-usage-delete-immediately explanation="필요한 데이터가 손실될 수 있고 파일이 열린 채라면 공간이 해제되지 않을 수도 있습니다."}
::option[그 파일이 있는 장치에 `mkfs`를 실행합니다.]{#disk-usage-mkfs-device explanation="포맷은 파일 하나의 증가 문제를 해결하는 대신 파일 시스템을 파괴합니다."}
::option[변경하기 전에 소유자와 보존 역할을 식별합니다.]{#disk-usage-review-large-file .correct explanation="크기만으로 파일을 버려도 되는지 또는 잘라도 안전한지 판단할 수 없습니다."}
:::

## 요약

이제 파일 시스템 공간 보고와 경로 기반 공간 보고를 조정해 이해할 수 있습니다.

1. 마운트된 파일 시스템의 블록 용량에는 `df`를 사용합니다.
2. 지원되는 경우 inode 압력에는 `df -i`를 사용합니다.
3. 범위가 제한된 `du` 순회로 도달 가능한 경로 사용량을 귀속합니다.
4. 삭제됐지만 열린 파일과 파일 시스템별 회계 차이를 조사합니다.
5. 데이터를 삭제하기 전에 소유권과 보존 정책을 적용합니다.
