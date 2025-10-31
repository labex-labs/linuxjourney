---
index: 7
lang: "ko"
title: "/etc/fstab"
meta_title: "/etc/fstab - 파일 시스템"
meta_description: "리눅스에서 /etc/fstab 파일을 사용하여 부팅 시 파일 시스템을 자동으로 마운트하는 방법을 알아보세요. 이 가이드는 fstab 구문, etc fstab 파일 안전하게 편집하는 방법, 시스템 시작 시 역할에 대해 다룹니다."
meta_keywords: "fstab, fstab 리눅스, etc fstab, /etc/fstab, fstab 파일, 파일 시스템 마운트, 리눅스 부팅, fstab 튜토리얼"
---

## Lesson Content

Linux 에서 부팅 시 파일 시스템을 자동으로 마운트하려면 `/etc/fstab`에 위치한 특수 설정 파일에 구성해야 합니다. `fstab`은 "filesystem table"의 약자이며, 이 파일은 시스템이 부팅 과정에서 마운트해야 하는 파일 시스템의 영구 목록을 포함합니다. **fstab linux** 구성을 이해하는 것은 모든 시스템 관리자에게 핵심적인 기술입니다.

### /etc/fstab이란 무엇인가

`/etc/fstab` 파일은 시스템 시작 시 마운트해야 할 모든 사용 가능한 디스크 파티션 및 반드시 디스크 기반이 아닌 다른 유형의 파일 시스템과 데이터 소스를 정의하는 시스템 구성 파일입니다. 시스템은 시작 시 이 파일을 참조하여 어떤 파일 시스템을 자동으로 마운트할지 결정합니다.

다음은 일반적인 **fstab file**의 예입니다.

```plaintext
pete@icebox:~$ cat /etc/fstab
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /               ext4    relatime,errors=remount-ro 0       1
UUID=78d203a0-7c18-49bd-9e07-54f44cdb5726 /home           xfs     relatime        0       2
UUID=22c3d34b-467e-467c-b44d-f03803c2c526 none            swap    sw              0       0
```

### fstab 파일 구조

**etc fstab** 파일의 각 줄은 하나의 파일 시스템을 나타내며 공백이나 탭으로 구분된 여섯 개의 필드로 구성됩니다. 각 필드가 무엇을 의미하는지 분석해 보겠습니다.

- **장치 식별자 (Device Identifier)**: 마운트할 장치를 지정합니다. 최신 시스템은 장치 이름 (예: `/dev/sda1`) 이 변경될 때 발생하는 문제를 피하기 위해 UUID(Universally Unique Identifier) 를 사용합니다.
- **마운트 지점 (Mount Point)**: 장치가 마운트될 파일 시스템 내의 디렉터리입니다 (예: `/` 또는 `/home`).
- **파일 시스템 유형 (Filesystem Type)**: 장치에 있는 파일 시스템의 유형으로, `ext4`, `xfs`, `btrfs`, 또는 `swap` 등이 있습니다.
- **옵션 (Options)**: 파일 시스템이 마운트되는 방식을 제어하는 마운트 옵션입니다. 일반적인 옵션으로는 `defaults`, `relatime`, `errors=remount-ro` 등이 있습니다. 전체 목록은 `mount` man 페이지를 참조하십시오.
- **덤프 (Dump)**: 이 필드는 `dump` 유틸리티가 파일 시스템을 백업해야 하는지 여부를 결정하는 데 사용됩니다. 값 `0`은 무시됨을 의미하며, 이는 안전한 기본값입니다.
- **순서 (Pass)**: 이 필드는 `fsck`가 부팅 시 파일 시스템을 확인하는 순서를 결정하는 데 사용됩니다. 루트 파일 시스템 (`/`) 은 `1`이어야 하고, 다른 파일 시스템은 `2`여야 하며, 값 `0`은 해당 파일 시스템이 확인되지 않음을 의미합니다.

### /etc/fstab 편집 방법

루트 권한이 있는 텍스트 편집기를 사용하여 `/etc/fstab` 파일을 직접 수정하여 항목을 추가할 수 있습니다. 이 파일을 편집할 때는 극도로 주의해야 합니다. **fstab**에 잘못된 항목이 있으면 시스템이 올바르게 부팅되지 않을 수 있습니다. 변경하기 전에 파일을 백업하는 것이 항상 좋은 습관입니다. 변경 사항을 저장한 후에는 재부팅 없이 `sudo mount -a` 명령을 실행하여 `/etc/fstab`에 나열된 모든 파일 시스템을 마운트함으로써 변경 사항을 테스트할 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 실습 경험은 파일 시스템을 관리하고 시스템 시작 시 올바르게 마운트되도록 보장하는 방법을 이해하는 데 매우 중요합니다. Linux 파일 시스템 관리 및 `/etc/fstab` 파일에 대한 이해를 강화하기 위한 실습 랩은 다음과 같습니다.

1. **[Linux 파티션 및 파일 시스템 관리](https://labex.io/ko/labs/comptia-manage-linux-partitions-and-filesystems-590845)** - 파티션을 생성하고, 포맷하고, 마운트하고, `/etc/fstab`을 사용하여 영구 마운트를 구성하는 연습을 합니다.
2. **[Linux 에서 스왑 파일 생성 및 활성화](https://labex.io/ko/labs/comptia-create-and-activate-a-swap-file-in-linux-590858)** - 종종 `/etc/fstab` 항목을 포함하는 스왑 파일을 생성하고 활성화하는 필수 관리 작업을 배웁니다.

이 랩들은 실제 시나리오에서 파일 시스템 마운트 및 구성 개념을 적용하고 Linux 에서 디스크 리소스 관리에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

파일 시스템이 마운트되는 방식을 정의하는 데 사용되는 파일은 무엇입니까? (전체 경로를 제공하십시오. 대소문자를 구분합니다.)

## Quiz Answer

/etc/fstab
