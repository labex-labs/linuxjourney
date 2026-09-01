---
lesson_id: "filesystem-types"
course_id: "filesystem"
lang: "ko"
order_index: 2
title: "파일 시스템 유형"
description: "리눅스 VFS가 로컬, 네트워크 및 가상 파일 시스템을 하나의 인터페이스로 제공하는 방법을 알아봅니다."
meta_title: "파일 시스템 유형 - 파일 시스템"
meta_description: "ext4, Btrfs 및 XFS를 비롯한 리눅스 파일 시스템 유형을 살펴봅니다. 저널링과 가상 파일 시스템(VFS)의 핵심 개념을 설명합니다."
meta_keywords: "리눅스 파일 시스템 유형, 파일 시스템 종류, ext4, Btrfs, XFS, 저널링, VFS, 리눅스 튜토리얼"
---

리눅스는 서로 다른 디스크 형식, 네트워크 프로토콜, 일관성 모델, 기능 및 운영 도구를 갖춘 여러 파일 시스템 구현을 지원합니다. 적합한 선택은 배포판 지원, 작업 부하, 복구 요구 사항, 저장 장치 토폴로지 및 관리자의 경험에 따라 달라집니다.

## 가상 파일 시스템 계층

커널의 가상 파일 시스템(VFS) 계층은 열기, 읽기, 쓰기, 이름 변경 및 권한 확인 같은 공통 작업을 제공합니다. 각 파일 시스템 구현은 이러한 작업을 자체 데이터 구조와 백업 저장소에 연결합니다.

따라서 하나의 프로세스가 공통 경로 이름 및 파일 디스크립터 모델을 통해 ext4, XFS, NFS, tmpfs 및 procfs에 접근할 수 있습니다. 그렇다고 모든 파일 시스템의 기능이나 동작이 같아지는 것은 아닙니다. 대소문자 구분, 잠금, 권한, 이름 변경 보장, 확장 속성 및 오류 처리 방식은 서로 다를 수 있습니다.

:::single-choice{#filesystem-types-vfs-role} 리눅스 VFS의 주된 역할은 무엇입니까?

::option[마운트된 모든 파일 시스템을 디스크의 ext4로 변환합니다.]{#filesystem-types-vfs-convert-ext4 explanation="이 추상화는 서로 다른 파일 시스템 구현과 형식을 그대로 유지합니다."}
::option[애플리케이션이 쓰기 전에 모든 파일을 백업합니다.]{#filesystem-types-vfs-backup explanation="VFS는 작업을 전달하며 자동 백업 기록을 제공하지 않습니다."}
::option[여러 파일 시스템 구현에 공통 커널 파일 작업을 제공합니다.]{#filesystem-types-vfs-common-interface .correct explanation="VFS를 통해 애플리케이션은 공통 시스템 호출을 사용하고 각 파일 시스템은 기반 동작을 구현합니다."}
:::

## 저널링과 충돌 일관성

저널링 파일 시스템은 선택한 업데이트를 저널에 기록하여 충돌 후 미완료 트랜잭션을 재실행하거나 버릴 수 있게 합니다. 저널링의 주된 목적은 전체 검사보다 빠르게 파일 시스템 구조의 일관성을 복원하는 것입니다.

최근 애플리케이션 데이터가 보존되었거나, 여러 파일에 걸친 애플리케이션 트랜잭션이 유효하거나, 저장 하드웨어가 완료된 모든 쓰기를 따랐다는 사실까지 보장하지는 않습니다. 파일 시스템은 서로 다른 데이터 모드와 순서 보장을 제공하며 애플리케이션은 적절한 플러시 및 원자적 업데이트 패턴을 사용해야 합니다. 저널은 백업이 아니며 삭제, 악성 코드 또는 장치 장애로부터 보호하지 않습니다.

:::single-choice{#filesystem-types-journal-scope} 파일 시스템 저널링이 충돌 후 복구하는 데 주로 도움이 되는 것은 무엇입니까?

::option[일관된 파일 시스템 메타데이터와 기록된 트랜잭션입니다.]{#filesystem-types-journal-consistency .correct explanation="저널 재실행은 파일 시스템 구조를 일관된 상태로 되돌리는 데 도움을 줍니다."}
::option[모든 사용자 문서의 모든 과거 버전입니다.]{#filesystem-types-journal-versions explanation="저널은 버전이 있는 백업 저장소가 아닙니다."}
::option[물리적으로 파괴된 저장 장치의 데이터입니다.]{#filesystem-types-journal-hardware-loss explanation="장치 손실에서 복구하려면 장애 장치 외부의 중복성이나 백업이 필요합니다."}
:::

## 일반적인 로컬 파일 시스템

- **ext4**는 리눅스 배포판과 복구 도구에서 널리 지원하는 성숙한 저널링 파일 시스템입니다.
- **XFS**는 대규모 파일 시스템과 병렬 입출력 작업 부하에 흔히 선택되는 확장성 높은 저널링 파일 시스템입니다.
- **Btrfs**는 체크섬, 하위 볼륨, 스냅샷 및 통합 다중 장치 기능을 갖춘 쓰기 시 복사 파일 시스템입니다.

기능은 운영 환경과 함께 고려해야 합니다. Btrfs 스냅샷은 처음에 소스와 저장 공간을 공유하므로 같은 장애 장치에 남아 있다면 독립적인 백업이 아닙니다. XFS와 ext4는 확장, 축소, 복구 및 튜닝 기능이 서로 다릅니다. 루트 파일 시스템을 선택하거나 변경하기 전에 설치된 커널, 부팅 환경 및 복구 도구의 지원 여부를 확인하십시오.

:::single-choice{#filesystem-types-btrfs-snapshot} 같은 장치에 있는 Btrfs 스냅샷이 완전한 백업이 아닌 이유는 무엇입니까?

::option[스냅샷이 항상 원본 하위 볼륨을 즉시 삭제하기 때문입니다.]{#filesystem-types-snapshot-deletes explanation="스냅샷은 다른 하위 볼륨 뷰를 만들며 본질적으로 소스를 제거하지 않습니다."}
::option[원본과 같은 저장 장치 장애 영역을 공유하기 때문입니다.]{#filesystem-types-snapshot-failure-domain .correct explanation="장치 손실이나 심각한 파일 시스템 손상이 소스와 로컬 스냅샷에 모두 영향을 줄 수 있습니다."}
::option[Btrfs가 파일을 하나보다 많이 표현할 수 없기 때문입니다.]{#filesystem-types-btrfs-one-file explanation="Btrfs는 디렉터리 트리와 여러 파일을 위한 범용 파일 시스템입니다."}
:::

## 상호 운용, 네트워크 및 가상 파일 시스템

리눅스는 FAT 계열, exFAT 및 NTFS 같은 상호 운용 형식을 마운트할 수 있지만 유닉스 소유권, 권한, 링크 및 파일 이름 의미 체계가 서로 다릅니다. 마운트 옵션과 드라이버 구현에 따라 리눅스가 누락된 기능을 표시하는 방식이 결정됩니다.

NFS와 SMB 같은 네트워크 파일 시스템은 서버와 네트워크 프로토콜에 의존하며 고유한 캐싱 및 식별자 규칙이 있습니다. tmpfs, procfs 및 sysfs 같은 가상 파일 시스템은 일반적인 영구 디스크 형식을 사용하지 않습니다. tmpfs는 휘발성 데이터를 메모리가 뒷받침하는 페이지에 저장하고, procfs와 sysfs는 커널 인터페이스를 노출합니다.

:::single-choice{#filesystem-types-procfs-category} procfs를 가장 잘 설명한 것은 무엇입니까?

::option[이동식 미디어를 위한 윈도우 상호 교환 형식입니다.]{#filesystem-types-procfs-windows explanation="FAT나 exFAT가 그 용도에 더 가깝고 procfs는 리눅스 커널 인터페이스입니다."}
::option[프로세스와 커널 인터페이스를 노출하는 가상 파일 시스템입니다.]{#filesystem-types-procfs-virtual .correct explanation="procfs는 일반 영구 파일을 디스크에 저장하지 않고 실시간 커널 뷰를 생성합니다."}
::option[데이터베이스 볼륨용 저널링 디스크 파일 시스템입니다.]{#filesystem-types-procfs-journal explanation="procfs에는 일반적인 디스크 저널이나 데이터 볼륨 역할이 없습니다."}
:::

## 활성 유형 확인하기

다음 명령으로 마운트된 파일 시스템 유형을 표시합니다.

```bash
$ findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS
```

마운트된 공간 사용량은 `df -T`, 블록 장치와 감지된 파일 시스템 서명은 `lsblk -f`, 실행 중인 커널이 지원하거나 알고 있는 유형은 `/proc/filesystems`에서도 확인할 수 있습니다. 각 도구는 서로 다른 질문에 답합니다. 마운트되지 않은 파일 시스템은 일반적인 마운트 파일 시스템 목록에 나타나지 않습니다.

:::single-choice{#filesystem-types-findmnt-output} 이 수업에서 대상, 소스, 유형 및 옵션과 함께 마운트된 파일 시스템을 직접 나열하는 명령은 무엇입니까?

::option[`findmnt -o TARGET,SOURCE,FSTYPE,OPTIONS`]{#filesystem-types-findmnt .correct explanation="findmnt는 마운트 테이블을 읽고 요청한 마운트 파일 시스템 필드를 형식화합니다."}
::option[`lsblk -o NAME,SIZE,MODEL,SERIAL,ROTA`]{#filesystem-types-mkfs-destructive explanation="이 명령은 적용된 마운트 파일 시스템 유형과 옵션이 아니라 블록 장치 하드웨어 정보를 나열합니다."}
::option[`cat /proc/filesystems | sort --unique`]{#filesystem-types-rm-proc explanation="이 명령은 적용된 마운트 소스와 옵션이 아니라 커널이 지원하는 파일 시스템 유형을 보고합니다."}
:::

폐기 가능한 저장 장치에서 [리눅스 파티션과 파일 시스템 관리하기](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)를 사용해 유형, 마운트 옵션 및 검색 뷰를 비교해 보십시오.

## 요약

이제 모든 파일 시스템의 의미가 같다고 가정하지 않고 여러 범주를 비교할 수 있습니다.

1. VFS를 여러 구현에 공통으로 제공되는 작업과 연결합니다.
2. 저널링을 백업이 아니라 충돌 일관성 지원으로 취급합니다.
3. 지원되는 작업과 작업 부하를 기준으로 ext4, XFS 및 Btrfs를 비교합니다.
4. 로컬 디스크, 네트워크, 상호 운용 및 가상 파일 시스템을 구분합니다.
5. 마운트 및 블록 장치 도구로 서로 다른 목록 질문에 답합니다.
