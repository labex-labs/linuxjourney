---
lesson_id: "mounting-and-unmounting-filesystems"
course_id: "filesystem"
lang: "ko"
order_index: 6
title: "mount와 umount"
description: "검증된 소스와 마운트 지점을 사용해 파일 시스템을 연결하고 검사하며 안전하게 분리하는 방법을 알아봅니다."
meta_title: "mount와 umount - 파일 시스템"
meta_description: "리눅스에서 mount와 umount 명령으로 파일 시스템을 연결하고 분리하는 방법을 알아봅니다. 장치 마운트, 안전한 sudo umount 절차 및 UUID 사용을 설명합니다."
meta_keywords: "mount, umount, sudo umount, 리눅스 마운트 해제, 파일 시스템 마운트, 장치 마운트 해제, 리눅스 UUID, 마운트 지점"
---

마운트는 파일 시스템을 보이는 네임스페이스의 디렉터리에 연결합니다. 소스는 블록 장치, 네트워크 내보내기, 가상 파일 시스템, 바인드 소스 또는 구현별 객체일 수 있습니다. 대상 디렉터리를 마운트 지점이라고 합니다.

## 마운트 지점 준비 및 검사

로컬 정책에 따라 의도적으로 이름을 정한 디렉터리를 만듭니다.

```bash
$ sudo mkdir -p /mnt/mydrive
```

마운트하기 전에 검사합니다.

```bash
$ findmnt --target /mnt/mydrive
$ sudo ls -la /mnt/mydrive
```

비어 있지 않은 디렉터리에 마운트하면 마운트 해제할 때까지 기존 항목이 새 파일 시스템 뒤에 가려집니다. 삭제되는 것은 아닙니다. 애플리케이션이 혼란을 겪고 디스크 공간이 보이지 않게 소비될 수 있으므로 비어 있는 전용 마운트 지점을 사용하십시오.

:::single-choice{#mount-umount-nonempty-target}
다른 파일 시스템을 디렉터리에 마운트하면 그 안의 기존 파일은 어떻게 됩니까?

::option[새 파일 시스템으로 자동 복사됩니다.]{#mount-umount-copied-files explanation="마운트는 네임스페이스 연결을 변경하며 디렉터리 내용을 이동하지 않습니다."}
::option[커널이 영구적으로 삭제합니다.]{#mount-umount-erased-files explanation="파일은 삭제된 것이 아니라 가려진 것이므로 일반적으로 마운트 해제 후 다시 나타납니다."}
::option[마운트를 분리할 때까지 가려집니다.]{#mount-umount-hidden-files .correct explanation="기반 디렉터리는 그대로 있지만 경로 조회가 마운트된 파일 시스템으로 넘어갑니다."}
:::

## 검증된 파일 시스템 마운트하기

소스 식별 정보, 감지된 유형 및 예상 내용을 확인한 뒤 명시적으로 마운트합니다.

```bash
$ sudo mount -t ext4 /dev/VERIFIED-PARTITION /mnt/mydrive
```

`-t` 옵션은 파일 시스템 구현을 지정합니다. mount는 종종 유형을 감지할 수 있지만 유형과 검토한 옵션을 명시하면 의도가 더 분명해집니다. 신뢰할 수 없거나 이동식인 콘텐츠에는 작업 부하에 맞을 때 `ro`, `nosuid`, `nodev` 및 `noexec` 같은 제한 옵션을 고려하십시오. 각 옵션에는 한계가 있으므로 완전한 샌드박스로 취급해서는 안 됩니다.

실제로 마운트된 내용을 검증합니다.

```bash
$ findmnt --target /mnt/mydrive -o TARGET,SOURCE,FSTYPE,OPTIONS
```

마운트는 네임스페이스 범위에 속합니다. 컨테이너나 비공개 서비스 네임스페이스에서 만든 마운트는 다른 프로세스의 뷰에 나타나지 않을 수 있습니다.

:::single-choice{#mount-umount-mount-role}
이 작업 흐름에서 `mount` 명령은 무엇을 합니까?

::option[새 파일 시스템을 만들고 소스를 지웁니다.]{#mount-umount-format-source explanation="파일 시스템 생성은 별도의 파괴적인 `mkfs` 작업입니다."}
::option[파일 시스템 소스를 마운트 네임스페이스의 디렉터리에 연결합니다.]{#mount-umount-attach-filesystem .correct explanation="그 뒤 대상 아래의 경로 조회가 연결된 파일 시스템으로 들어갑니다."}
::option[디스크의 파티션 경계를 변경합니다.]{#mount-umount-change-partitions explanation="파티션 테이블 편집은 네임스페이스 마운트와 별개입니다."}
:::

## 파일 시스템 UUID 사용하기

`/dev/sdb2` 같은 열거 이름은 바뀔 수 있습니다. 다음 명령으로 파일 시스템 식별자를 확인합니다.

```bash
$ lsblk -f
$ sudo blkid
```

그런 다음 검증된 파일 시스템을 UUID로 마운트합니다.

```bash
$ sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mnt/mydrive
```

UUID는 파일 시스템을 식별하며 반드시 물리 디스크를 식별하는 것은 아닙니다. 다시 포맷하면 바뀌고 복제하면 중복될 수 있습니다. 원본과 복제본을 같은 시스템에 연결하기 전에 고유성을 확인하십시오.

:::single-choice{#mount-umount-uuid-benefit}
영구 설정에서 파일 시스템 UUID가 `/dev/sdX`보다 더 적합한 경우가 많은 이유는 무엇입니까?

::option[모든 저장 장치의 장애를 영구히 막기 때문입니다.]{#mount-umount-uuid-no-failure explanation="식별자는 중복성, 무결성 복구 또는 백업을 제공하지 않습니다."}
::option[복제된 파일 시스템의 식별자가 다름을 보장하기 때문입니다.]{#mount-umount-uuid-clone-unique explanation="블록 수준 복제는 UUID도 복사하여 충돌을 만들 수 있습니다."}
::option[현재 열거 순서가 아니라 파일 시스템 식별 정보에 연결되기 때문입니다.]{#mount-umount-uuid-identity .correct explanation="블록 장치 경로가 바뀌어도 파일 시스템 메타데이터는 UUID를 유지합니다."}
:::

## 안전하게 마운트 해제하기

정확한 마운트 지점으로 분리합니다.

```bash
$ sudo umount /mnt/mydrive
```

명령 이름은 첫 번째 `n`이 없는 `umount`입니다. 성공적인 마운트 해제는 커널이 필요한 쓰기 반영을 완료하고 참조가 허용하는 경우 파일 시스템을 분리합니다. 저장 장치의 연결을 끊기 전에 `findmnt`로 분리 여부를 확인하십시오.

이동식 미디어에서는 마운트 해제 성공이 항상 안전한 제거의 마지막 작업은 아닙니다. 데스크톱 저장 장치 스택은 장치 캐시를 플러시하고 USB 장치를 비활성화하는 꺼내기 또는 전원 끄기 작업을 제공할 수 있습니다. 플랫폼과 하드웨어의 절차를 따르십시오.

:::single-choice{#mount-umount-command-name}
`/mnt/mydrive`를 분리하는 명령은 무엇입니까?

::option[`umount /mnt/mydrive`]{#mount-umount-umount-correct .correct explanation="`umount`는 지정한 대상에 마운트된 파일 시스템을 분리합니다."}
::option[`unmount /mnt/mydrive`]{#mount-umount-unmount-spelling explanation="표준 명령 이름에는 첫 번째 `n`이 없습니다."}
::option[`mkfs /mnt/mydrive`]{#mount-umount-mkfs-target explanation="mkfs는 파일 시스템 구조를 만들며 분리에 사용해서는 안 됩니다."}
:::

## 사용 중인 파일 시스템 진단하기

열린 파일, 프로세스 작업 디렉터리, 중첩 마운트, 스왑 또는 다른 저장 장치 계층처럼 네임스페이스에 활성 참조가 남아 있으면 마운트 해제가 실패합니다. 즉시 강제하지 말고 조사하십시오.

```bash
$ findmnt --submounts /mnt/mydrive
$ sudo fuser -vm /mnt/mydrive
```

셸을 트리 밖으로 이동하고, 책임 있는 애플리케이션을 정상적으로 중지하며, 부모보다 먼저 하위 마운트를 해제하십시오. 지연 마운트 해제와 강제 옵션에는 특수한 의미가 있고 활성 참조를 남기거나 데이터 손실 위험을 일으킬 수 있습니다. 문서화된 복구 근거가 있을 때만 사용하십시오.

:::single-choice{#mount-umount-busy-cause}
`umount`가 파일 시스템이 사용 중이라고 보고할 수 있는 조건은 무엇입니까?

::option[마운트 지점 디렉터리 이름에 소문자가 포함되어 있습니다.]{#mount-umount-lowercase explanation="경로의 대소문자만으로는 활성 파일 시스템 참조가 생기지 않습니다."}
::option[프로세스의 현재 작업 디렉터리가 마운트 안에 있습니다.]{#mount-umount-cwd-busy .correct explanation="프로세스가 마운트된 파일 시스템 안의 참조를 유지해 일반적인 분리를 막습니다."}
::option[파일 시스템 UUID가 장치 이름보다 깁니다.]{#mount-umount-uuid-length explanation="식별자 문자열 길이는 사용 중 상태 확인과 관련이 없습니다."}
:::

[리눅스 파티션과 파일 시스템 관리하기](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)에서 지정된 폐기 가능한 저장 장치를 사용해 연습하십시오.

## 요약

이제 검증 가능한 범위에서 파일 시스템을 연결하고 분리할 수 있습니다.

1. 비어 있는 전용 마운트 지점을 사용합니다.
2. 소스, 유형, 옵션 및 결과 마운트를 검증합니다.
3. 영구 참조에는 고유한 파일 시스템 식별자를 우선 사용합니다.
4. 대상으로 마운트 해제하고 제거하기 전에 분리 여부를 확인합니다.
5. 사용 중인 파일 시스템을 강제로 분리하지 말고 활성 참조를 진단합니다.
