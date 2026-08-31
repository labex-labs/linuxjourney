---
lesson_id: "creating-filesystems"
course_id: "filesystem"
lang: "ko"
order_index: 5
title: "파일 시스템 만들기"
description: "블록 장치 대상을 검증하고 형식별 도구로 파일 시스템을 만드는 방법을 알아봅니다."
meta_title: "파일 시스템 만들기 - 파일 시스템"
meta_description: "mkfs 명령으로 리눅스 파티션에 파일 시스템을 만드는 방법을 알아봅니다. 대상 검증, ext4 포맷 및 디스크 관리의 필수 단계를 설명합니다."
meta_keywords: "mkfs, 파일 시스템 만들기, ext4, 리눅스 파티셔닝, 리눅스 튜토리얼, 디스크 관리, 리눅스 디스크 포맷"
---

파일 시스템을 만들면 블록 장치에 새로운 할당 및 메타데이터 구조를 기록합니다. 단순한 레이블 변경이 아니라 파괴적인 초기화 단계입니다. 연습에는 폐기 가능한 저장 장치만 사용하고, 중요한 데이터가 있었던 장치를 포맷하기 전에는 검증된 백업을 유지하십시오.

## `mkfs` 이해하기

`mkfs`는 일반적으로 `mkfs.ext4`, `mkfs.xfs` 또는 `mkfs.btrfs` 같은 파일 시스템별 프로그램으로 작업을 전달하는 프런트엔드입니다. 일반 명령은 다음과 같은 형태입니다.

```bash
$ sudo mkfs -t ext4 /dev/VERIFIED-PARTITION
```

자리표시자는 검증한 후에만 실제 경로로 바꿔야 합니다. 동등한 형식별 구문은 일반적으로 다음과 같습니다.

```bash
$ sudo mkfs.ext4 /dev/VERIFIED-PARTITION
```

지원 옵션, 기본값, 기능 집합 및 덮어쓰기 확인 방식은 구현마다 다릅니다. 모든 `mkfs` 백엔드가 같다고 가정하지 말고 정확한 포맷 도구의 로컬 설명서를 읽으십시오.

:::single-choice{#creating-filesystems-mkfs-role}
`mkfs -t ext4 TARGET`이 요청하는 작업은 무엇입니까?

::option[기존 파일 시스템을 변경하지 않고 마운트합니다.]{#creating-filesystems-mount-existing explanation="마운트는 별도 작업이며 mkfs는 장치 내 메타데이터를 초기화합니다."}
::option[대상에 ext4 파일 시스템 구조를 만듭니다.]{#creating-filesystems-create-ext4 .correct explanation="프런트엔드는 지정한 블록 장치에 ext4 포맷 구현을 선택합니다."}
::option[현재 마운트된 모든 파일 시스템을 나열합니다.]{#creating-filesystems-list-mounted explanation="읽기 전용 마운트 목록은 `findmnt` 같은 도구로 확인합니다."}
:::

## 모든 저장 장치 계층 검증하기

포맷하기 전에 모델, 일련번호, 크기, 토폴로지, 영구 링크 및 의도한 역할로 대상을 식별합니다.

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS
$ findmnt --real
$ sudo wipefs --no-act /dev/VERIFIED-PARTITION
```

`wipefs --no-act`는 인식된 서명을 지우지 않고 보고합니다. 스왑, LVM, RAID, 암호화, 가상 머신, 컨테이너 및 애플리케이션의 사용 여부도 확인하십시오. `MOUNTPOINTS`가 비어 있어도 장치가 사용 중일 수 있습니다.

각 계층의 전용 도구로 관련 계층을 모두 마운트 해제하거나 비활성화하십시오. 열거 이름은 바뀔 수 있으므로 포맷 도구를 실행하기 직전에 식별 정보를 다시 확인합니다.

:::single-choice{#creating-filesystems-wipefs-no-act}
이 작업 흐름에서 `wipefs --no-act TARGET`이 제공하는 것은 무엇입니까?

::option[인식된 서명의 읽기 전용 보고서입니다.]{#creating-filesystems-signature-report .correct explanation="no-act 모드는 기존 파일 시스템, 파티션 테이블, RAID 또는 다른 서명을 제거하지 않고 확인하는 데 도움을 줍니다."}
::option[마운트할 준비가 된 새 빈 파일 시스템입니다.]{#creating-filesystems-wipefs-formats explanation="서명 검사는 새 파일 시스템을 초기화하지 않습니다."}
::option[어떤 프로세스도 대상을 사용하지 않는다는 보장입니다.]{#creating-filesystems-wipefs-no-users explanation="사용 여부는 마운트와 더 넓은 저장 장치 스택 전체에서 별도로 확인해야 합니다."}
:::

## 파일 시스템을 신중하게 선택하기

배포판, 부팅 환경, 백업 도구, 복구 도구 및 작업 부하가 지원하는 유형을 선택하십시오. 필요한 한계, 스냅샷, 체크섬, 할당량, 암호화 계층, 확장 또는 축소 동작 및 플랫폼 간 접근을 고려합니다.

인기만을 이유로 형식을 선택하지 마십시오. 예를 들어 ext4, XFS 및 Btrfs는 운영 기능과 복구 절차가 서로 다릅니다. 상호 운용을 위한 이동식 장치에는 유닉스 권한 의미 체계가 다른 형식이 필요할 수 있습니다.

:::single-choice{#creating-filesystems-type-choice}
파일 시스템 유형을 선택하는 올바른 기준은 무엇입니까?

::option[입력할 이름이 가장 짧은 유형입니다.]{#creating-filesystems-shortest-name explanation="명령 길이는 내구성, 기능 또는 지원 여부를 알려 주지 않습니다."}
::option[앞으로 저장 장치 장애가 절대 없다는 약속입니다.]{#creating-filesystems-no-failure explanation="어떤 파일 시스템도 하드웨어 장애나 백업의 필요성을 없애지 못합니다."}
::option[작업 부하 요구 사항과 지원되는 백업, 부팅 및 복구 도구입니다.]{#creating-filesystems-supported-workflow .correct explanation="형식은 기술 요구 사항과 환경의 운영 및 복구 능력에 모두 맞아야 합니다."}
:::

## 레이블, UUID 및 검증

포맷 도구는 일반적으로 파일 시스템 UUID를 생성하고 사람이 읽을 수 있는 레이블도 설정할 수 있습니다. 환경에서 충분히 고유한 레이블을 사용하고, 복제된 파일 시스템을 함께 마운트할 때 충돌하는 식별자가 유지되지 않도록 하십시오.

성공적으로 생성한 후 마운트하지 않고 검사합니다.

```bash
$ lsblk -f /dev/VERIFIED-PARTITION
$ sudo blkid /dev/VERIFIED-PARTITION
```

나중의 마운트 설정을 위해 UUID를 기록하십시오. 파일 시스템을 만들어도 마운트되거나, 애플리케이션 디렉터리가 만들어지거나, 백업 데이터가 채워지거나, 부팅 후에도 자동으로 유지되지는 않습니다.

:::single-choice{#creating-filesystems-after-mkfs}
파일 시스템을 만든 뒤에도 별도로 수행해야 하는 단계는 무엇입니까?

::option[의도한 디렉터리에 마운트합니다.]{#creating-filesystems-mount-separate .correct explanation="포맷은 파일 시스템 구조를 기록하고 마운트는 그 파일 시스템을 보이는 디렉터리 트리에 연결합니다."}
::option[블록 장치에 용량 자체를 할당합니다.]{#creating-filesystems-capacity explanation="기반 파티션이나 논리 장치가 이미 포맷할 용량을 제공합니다."}
::option[커널의 `/dev` 디렉터리를 처음부터 만듭니다.]{#creating-filesystems-create-dev explanation="장치 노드 관리는 한 대상을 포맷하는 작업과 독립적입니다."}
:::

[리눅스 파티션과 파일 시스템 관리하기](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)는 실습의 폐기 가능한 보조 디스크에서만 사용하십시오.

## 요약

이제 파일 시스템 생성을 검증을 거치는 파괴적 작업으로 설명할 수 있습니다.

1. `mkfs`를 형식별 도구로 작업을 전달하는 프런트엔드로 취급합니다.
2. 영구 식별 정보, 서명 및 모든 활성 사용자를 검증합니다.
3. 지원 및 복구 요구 사항에 따라 파일 시스템을 선택합니다.
4. 마운트하기 전에 생성된 유형, 레이블 및 UUID를 검사합니다.
