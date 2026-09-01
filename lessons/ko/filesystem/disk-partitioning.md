---
lesson_id: "disk-partitioning"
course_id: "filesystem"
lang: "ko"
order_index: 4
title: "디스크 파티셔닝"
description: "`parted`로 파티션 경계를 검사, 생성 및 조정할 때 검증을 우선하는 작업 흐름을 알아봅니다."
meta_title: "디스크 파티셔닝 - 파일 시스템"
meta_description: "parted 명령을 이용한 리눅스 디스크 파티셔닝을 알아봅니다. sudo parted -l로 파티션을 확인하고 생성 및 크기 조정하는 방법과 그래픽 도구 GParted를 설명합니다."
meta_keywords: "리눅스 디스크 파티셔닝, parted 명령어, sudo parted -l, GParted, fdisk, 디스크 관리, 파티션 생성, 파티션 크기 조정"
---

파티션 편집은 저장 공간의 경계를 정의하는 지도를 변경합니다. 장치, 시작 또는 끝을 잘못 지정하면 기존 데이터에 접근할 수 없게 되거나 중요한 메타데이터를 덮어쓸 수 있습니다. 폐기 가능한 가상 디스크에서만 연습하고 중요한 저장 장치를 수정하기 전에는 별도로 검증한 백업을 유지하십시오.

## 도구 선택하기

일반적인 도구는 다음과 같습니다.

- `fdisk`: MBR과 GPT를 지원하는 util-linux의 터미널 파티션 편집기
- `parted`: GPT, MBR 및 다른 테이블 형식을 위한 터미널 및 스크립트형 편집기
- `gdisk`: GPT 중심의 대화형 편집기
- GParted: 그래픽 파티션 및 파일 시스템 프런트엔드

도구 지원은 계속 발전하므로 로컬 설명서와 배포판 문서를 사용하십시오. 그래픽 인터페이스라고 해서 파괴적인 작업이 안전해지는 것은 아닙니다. 같은 디스크 메타데이터를 변경합니다.

:::single-choice{#disk-partitioning-fdisk-gpt} 현재 리눅스 `fdisk`에 대한 정확한 설명은 무엇입니까?

::option[MBR과 GPT 파티션 테이블을 모두 지원합니다.]{#disk-partitioning-fdisk-supports-gpt .correct explanation="현재 util-linux fdisk는 DOS/MBR과 GPT를 비롯한 여러 레이블 유형을 편집할 수 있습니다."}
::option[GPT만 편집할 수 있고 MBR은 편집할 수 없습니다.]{#disk-partitioning-fdisk-only-gpt explanation="GPT 중심의 `gdisk`가 이 설명에 더 가깝고 fdisk는 여러 레이블 유형을 지원합니다."}
::option[파일 시스템은 만들지만 파티션 항목은 편집할 수 없습니다.]{#disk-partitioning-fdisk-filesystem-only explanation="핵심 목적은 파티션 테이블을 보고 편집하는 것입니다."}
:::

## 대상 식별 및 정지

읽기 전용 목록부터 확인합니다.

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,TRAN,PTTYPE,FSTYPE,MOUNTPOINTS
$ findmnt --real
$ sudo parted --list
```

`/dev/sdX`만 보지 말고 영구 식별 정보, 모델, 일련번호, 크기, 전송 방식 및 토폴로지로 전체 장치를 확인합니다. 그런 다음 마운트된 파일 시스템, 스왑, LVM, RAID, 암호화, 컨테이너, 가상 머신, 데이터베이스 및 열린 파일 디스크립터 등 모든 사용자를 식별합니다.

각 계층의 문서화된 절차에 따라 관련 계층을 모두 마운트 해제하거나 비활성화하십시오. 도구가 성공적으로 열린다는 이유만으로 실행 중인 시스템 디스크의 파티션 테이블을 편집하지 마십시오. 기존 테이블을 복원 가능한 형태로 기록하고 백업이 다른 장애 영역에 있는지 확인하십시오.

:::single-choice{#disk-partitioning-target-identity} `/dev/sdb` 같은 장치 이름만으로 대상을 확인하기에 부족한 이유는 무엇입니까?

::option[리눅스가 전체 디스크를 `/dev` 아래에 절대 노출하지 않기 때문입니다.]{#disk-partitioning-no-whole-disks explanation="전체 디스크에는 일반적으로 `/dev` 아래의 블록 노드가 있습니다."}
::option[장치나 토폴로지가 바뀌면 열거 이름도 바뀔 수 있기 때문입니다.]{#disk-partitioning-enumeration-changes .correct explanation="문자는 검색 순서에 따라 배정되므로 나중 세션에는 다른 디스크를 가리킬 수 있습니다."}
::option[파티션 도구가 피연산자로 파일 시스템 UUID만 허용하기 때문입니다.]{#disk-partitioning-only-uuid explanation="편집기는 일반적으로 식별 정보를 확인한 전체 블록 장치 경로를 대상으로 작동합니다."}
:::

## `parted`에서 장치 하나 검사하기

명시적으로 검증한 전체 장치를 엽니다.

```bash
$ sudo parted /dev/VERIFIED-DISK
```

그런 다음 일관된 표시 단위를 선택하고 테이블을 출력합니다.

```text
(parted) unit MiB
(parted) print free
```

`print free`는 현재 항목과 할당되지 않은 영역을 보여 줍니다. Parted 명령은 최종 “저장” 작업을 기다리지 않고 디스크 메타데이터를 즉시 갱신할 수 있으므로 대화형 프롬프트를 실시간 쓰기 접근으로 취급하십시오.

:::single-choice{#disk-partitioning-print-free} `parted`의 `print free`가 표시하는 데 도움을 주는 것은 무엇입니까?

::option[파일 시스템을 안전하게 축소하기 위해 삭제할 수 있는 파일입니다.]{#disk-partitioning-free-files explanation="Parted는 파일 시스템 수준의 파일 할당이 아니라 파티션 레이아웃을 읽습니다."}
::option[원격 시스템에 저장된 모든 백업입니다.]{#disk-partitioning-remote-backups explanation="원격 백업 목록은 파티션 편집기의 범위 밖입니다."}
::option[기존 파티션 항목과 할당되지 않은 영역입니다.]{#disk-partitioning-free-regions .correct explanation="이 뷰는 현재 테이블과 남은 간격을 바탕으로 경계를 선택하는 데 도움을 줍니다."}
:::

## 파티션 항목 만들기

정확한 `mkpart` 구문은 테이블 유형에 따라 다릅니다. MiB 단위를 사용하는 GPT 예시는 다음과 같습니다.

```text
(parted) mkpart data ext4 1MiB 5000MiB
```

이 명령은 이름, 제안 콘텐츠 유형, 시작 및 끝을 가진 파티션 항목을 만듭니다. ext4 파일 시스템을 만들지는 **않습니다**. 포맷은 커널이 의도한 새 파티션을 인식하고 그 식별 정보가 검증된 후에만 수행하는 별도의 파괴적 단계입니다.

도구가 권장하는 정렬을 사용하고 끝점이 포함되는지와 반올림 방식을 이해하십시오. `print`와 `lsblk`로 결과를 검사하고 요청한 십진 경계가 정확히 기록되었다고 가정하지 마십시오.

:::single-choice{#disk-partitioning-mkpart-effect} `parted`의 `mkpart`가 만드는 것은 무엇입니까?

::option[홈 디렉터리가 들어 있고 마운트된 ext4 파일 시스템입니다.]{#disk-partitioning-mounted-filesystem explanation="포맷과 마운트는 파티션 생성 후의 별도 작업입니다."}
::option[이전 파티션 내용의 완전한 백업입니다.]{#disk-partitioning-automatic-backup explanation="파티션 편집기는 복구 백업을 자동으로 만들지 않습니다."}
::option[파일 시스템을 포맷하지 않은 파티션 테이블 항목입니다.]{#disk-partitioning-entry-only .correct explanation="파일 시스템 유형 인수는 파티션 메타데이터에 영향을 주지만 `mkfs`를 실행하지는 않습니다."}
:::

## 경계와 콘텐츠 크기 조정

`resizepart NUMBER END`는 파티션의 끝 경계만 옮깁니다. 그 안의 파일 시스템이나 다른 구조의 크기는 조정하지 않습니다.

순서가 매우 중요합니다.

- 확장할 때는 먼저 포함하는 파티션이나 논리 장치를 확장한 다음 파일 시스템 전용 도구로 파일 시스템을 확장합니다.
- 축소할 때는 파일 시스템이 축소를 지원하는지 확인하고 온라인 또는 오프라인 요구 사항에 따라 먼저 파일 시스템을 축소한 다음, 새 끝을 넘지 않도록 포함하는 경계를 줄입니다.

일부 파일 시스템은 축소할 수 없습니다. 암호화, LVM, RAID 및 중첩 레이아웃에는 순서를 지켜야 하는 계층이 더 많습니다. 장치가 사용 중이면 커널이 변경된 테이블을 다시 읽지 못할 수 있으므로 새 레이아웃을 사용하기 전에 제어된 재부팅이 필요할 수 있습니다.

:::single-choice{#disk-partitioning-shrink-order} 파일 시스템이 축소를 지원할 때 활성 파일 시스템 데이터를 잘라내지 않는 순서는 무엇입니까?

::option[먼저 파티션을 줄인 다음 파일 시스템이 들어맞는지 확인합니다.]{#disk-partitioning-shrink-partition-first explanation="컨테이너부터 줄이면 파일 시스템 구조와 데이터가 잘릴 수 있습니다."}
::option[먼저 파일 시스템을 축소한 다음 그것을 포함하는 파티션 경계를 줄입니다.]{#disk-partitioning-shrink-filesystem-first .correct explanation="바깥 블록 장치를 줄이기 전에 콘텐츠가 더 작은 범위 안에 들어가야 합니다."}
::option[파티션 테이블을 삭제한 뒤 파일 시스템이 다시 만들게 합니다.]{#disk-partitioning-delete-table explanation="파일 시스템은 일반적인 축소 과정에서 안전한 파티션 테이블을 재구성하지 않습니다."}
:::

[리눅스 파티션과 파일 시스템 관리하기](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)는 지정된 보조 가상 디스크에서 사용하고 호스트 디스크로 대체하지 마십시오.

## 요약

이제 파티션 편집을 계층적이고 파괴적인 저장 장치 작업으로 설명할 수 있습니다.

1. 실제 테이블과 작업 흐름을 지원하는 도구를 선택합니다.
2. 영구적인 디스크 식별 정보를 검증하고 모든 사용자를 비활성화합니다.
3. 쓰기 전에 단위, 항목 및 빈 영역을 검사합니다.
4. `mkpart`가 파일 시스템을 만들지 않는다는 점을 기억합니다.
5. 안전한 순서에 따라 내부 콘텐츠와 외부 경계의 크기를 조정합니다.
