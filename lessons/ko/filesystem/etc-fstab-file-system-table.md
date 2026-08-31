---
lesson_id: "etc-fstab-file-system-table"
course_id: "filesystem"
lang: "ko"
order_index: 7
title: "/etc/fstab"
description: "`/etc/fstab`에 영구적인 파일 시스템 및 스왑 연결을 정의하고 안전하게 검증하는 방법을 알아봅니다."
meta_title: "/etc/fstab - 파일 시스템"
meta_description: "리눅스의 /etc/fstab 파일로 부팅 시 파일 시스템을 자동 마운트하는 방법을 알아봅니다. fstab 구문, 안전한 편집 및 시스템 시작 과정에서의 역할을 설명합니다."
meta_keywords: "fstab, 리눅스 fstab, /etc/fstab, fstab 파일, 파일 시스템 마운트, 리눅스 부팅, fstab 튜토리얼"
---

파일 시스템 테이블인 `/etc/fstab`은 시스템 도구가 마운트하거나 활성화할 수 있는 파일 시스템, 스왑 영역, 바인드 마운트, 네트워크 소스 및 기타 연결을 선언합니다. 항목은 부팅 과정에 참여할 수 있지만 `noauto`, 자동 마운트 통합 및 서비스 관리자 정책 같은 옵션에 따라 언제 또는 실제로 실행되는지가 달라집니다.

## 여섯 필드

일반적인 항목에는 공백으로 구분된 여섯 필드가 있습니다.

```text
UUID=130b882f-7d79-436d-a096-1e594c92bb76 /data ext4 defaults,nosuid,nodev 0 2
```

1. **소스**: 장치 경로, `UUID=`, `LABEL=`, 네트워크 소스 또는 지원되는 다른 지정 방식입니다.
2. **대상**: 마운트 지점이며, 스왑 같은 용도에서는 적절한 경우 `none`을 사용합니다.
3. **유형**: 파일 시스템 유형, `swap`, `none` 또는 허용된 자동 유형입니다.
4. **옵션**: 마운트 보조 도구와 통합 계층이 해석하는 쉼표 구분 목록입니다.
5. **dump 필드**: 역사적으로 `dump` 백업 유틸리티의 참여 여부를 제어하며, 일반적으로 `0`은 참여하지 않음을 뜻합니다.
6. **pass 필드**: 적용 가능한 경우 부팅 시 `fsck` 순서를 제어하며, `0`은 이 메커니즘을 통한 자동 검사를 비활성화합니다.

필드 안의 공백은 fstab 구문에 따라 공백의 경우 `\040`처럼 이스케이프해야 합니다. 필드 밖의 `#`은 주석을 시작합니다.

:::single-choice{#fstab-field-count}
일반적인 `/etc/fstab` 항목에는 필드가 몇 개 있습니까?

::option[네 개입니다.]{#fstab-four-fields explanation="소스, 대상, 유형 및 옵션 뒤에 dump와 pass 필드가 이어집니다."}
::option[여덟 개입니다.]{#fstab-eight-fields explanation="여덟 개는 fstab 레코드 하나의 표준 필드 수가 아닙니다."}
::option[여섯 개입니다.]{#fstab-six-fields .correct explanation="전통적인 형식은 소스, 대상, 유형, 옵션, dump 및 pass 필드로 구성됩니다."}
:::

## 안정적인 소스 식별자

로컬 파일 시스템에서는 파일 시스템 UUID가 `/dev/sdX` 열거 이름보다 안정적인 경우가 많습니다.

```bash
$ lsblk -f
$ sudo blkid
```

`UUID=...`는 해당 식별자가 의도한 파일 시스템에 속하는지 확인한 뒤에만 사용하십시오. 다시 포맷하면 새 UUID가 생성되고 블록 수준 복제는 같은 UUID를 복사할 수 있습니다. `PARTUUID=`는 파일 시스템이 아니라 파티션 테이블 항목을 식별하며 의미가 다릅니다.

:::single-choice{#fstab-uuid-source}
소스 필드의 `UUID=...`는 일반적으로 무엇을 식별합니까?

::option[마운트 지점을 소유한 사용자 계정입니다.]{#fstab-user-uuid explanation="계정 식별자는 파일 시스템 UUID 소스 구문으로 선택하지 않습니다."}
::option[해당 UUID를 가진 파일 시스템 메타데이터입니다.]{#fstab-filesystem-uuid .correct explanation="mount는 열거 이름에 의존하지 않고 파일 시스템 식별자를 사용 가능한 블록 장치로 해석합니다."}
::option[마지막으로 파일 시스템을 마운트 해제한 프로세스입니다.]{#fstab-process-uuid explanation="프로세스 기록은 이 소스 필드에 인코딩되지 않습니다."}
:::

## 마운트 옵션과 검사 필드

`defaults`는 구현에서 정의한 일반적인 옵션 집합으로 확장되며 모든 마운트에 가장 안전한 정책인 것은 아닙니다. 읽기 전용 접근이나 장치 노드 및 setuid 동작 제한처럼 신뢰 수준과 작업 부하에 맞는 옵션을 추가하십시오. 네트워크와 이동식 파일 시스템에는 부팅이 예상치 못하게 멈추지 않도록 시간 제한, 의존성 또는 장애 허용 정책이 필요할 수 있습니다.

`fsck`가 지원하는 파일 시스템에서 루트 파일 시스템은 일반적으로 pass `1`을 사용하고 검사할 다른 로컬 파일 시스템은 pass `2`를 사용합니다. 일부 유형은 일반 부팅 시 fsck를 사용하지 않는 등 파일 시스템별 관행이 다를 수 있으므로 `2`를 기계적으로 지정하지 말고 설치된 파일 시스템과 배포판 문서를 따르십시오.

:::single-choice{#fstab-pass-zero}
여섯 번째 필드의 값 `0`은 무엇을 요청합니까?

::option[해당 항목을 fstab 기반 자동 fsck 순서에서 제외합니다.]{#fstab-pass-zero-skip .correct explanation="pass 0은 이 필드가 제어하는 부팅 시 검사 순서에서 항목을 제외합니다."}
::option[모든 상황에서 파일 시스템을 읽기 전용으로 마운트합니다.]{#fstab-pass-zero-readonly explanation="읽기 전용 동작은 마운트 옵션 필드에 지정합니다."}
::option[부팅할 때마다 파일 시스템을 지웁니다.]{#fstab-pass-zero-erase explanation="pass 필드는 파일 시스템을 포맷하거나 지우지 않습니다."}
:::

## 복구 경로를 마련하고 편집하기

잘못된 루트, 부팅 또는 필수 네트워크 항목은 시작 과정을 중단시킬 수 있습니다. 편집하기 전에 다음을 수행하십시오.

1. 최신 백업과 콘솔 또는 복구 접근을 확인합니다.
2. 권한을 유지하면서 기존 파일을 복사합니다.
3. 소스 식별 정보를 검증하고 의도한 마운트 지점을 만듭니다.
4. 범위가 좁은 변경 하나만 수행합니다.
5. 재부팅 전에 검증하고 테스트합니다.

누구나 읽을 수 있는 fstab 항목에 자격 증명을 직접 넣지 마십시오. 해당 마운트 보조 도구가 제공하는 보호된 자격 증명 메커니즘을 사용합니다.

:::single-choice{#fstab-editing-recovery}
중요한 fstab 항목을 변경하기 전에 복구 접근을 확인해야 하는 이유는 무엇입니까?

::option[fstab 편집이 항상 파티션 테이블을 즉시 지우기 때문입니다.]{#fstab-no-partition-erase explanation="텍스트 편집 자체는 디스크 파티션을 다시 쓰지 않지만 이후 마운트에는 영향이 있을 수 있습니다."}
::option[다른 운영체제에서만 파일을 편집할 수 있기 때문입니다.]{#fstab-other-os-only explanation="적절한 권한과 안전 조치를 사용하면 리눅스에서 편집할 수 있습니다."}
::option[잘못된 항목 때문에 정상 부팅이 사용 가능한 시스템 상태에 도달하지 못할 수 있기 때문입니다.]{#fstab-boot-failure .correct explanation="중요한 마운트 실패는 비상 모드로 진입하거나 의존 서비스의 시작을 막을 수 있습니다."}
:::

## 성공을 가정하지 않고 검증하기

지원되는 경우 정적 검사부터 시작합니다.

```bash
$ sudo findmnt --verify --verbose
```

그런 다음 통제된 조건에서 특정 새 항목을 테스트하고 `findmnt`로 확인하며, 테스트가 임시였다면 마운트 해제합니다. `mount -a`는 여러 대상 항목을 실제로 시도하여 네트워크에 연결하거나 의도하지 않은 소스를 연결할 수 있습니다. 이미 마운트된 항목과 `noauto` 항목도 건너뛰므로 무해한 구문 검사기도 아니고 완전한 증명도 아닙니다.

systemd 기반 시스템에서는 fstab을 편집한 뒤 관리자 설정을 다시 불러와 생성된 마운트 단위를 갱신하고, 로컬 문서에 따라 의존성과 부팅 동작을 검증하십시오.

:::single-choice{#fstab-mount-a-limit}
`mount -a`만으로 fstab을 완전히 검증할 수 없는 이유는 무엇입니까?

::option[나열된 모든 장치를 마운트하기 전에 항상 다시 포맷하기 때문입니다.]{#fstab-mount-a-formats explanation="mount는 일반적으로 파일 시스템을 만들지 않습니다."}
::option[항목을 건너뛸 수 있고 구문만 검사하는 대신 광범위한 실제 마운트 작업을 수행하기 때문입니다.]{#fstab-mount-a-incomplete .correct explanation="이미 마운트되었거나 `noauto`인 레코드는 테스트되지 않을 수 있고 대상 소스에는 실제 영향이 생길 수 있습니다."}
::option[셸 기록만 읽고 fstab은 무시하기 때문입니다.]{#fstab-mount-a-history explanation="이 명령은 대상 항목을 찾기 위해 fstab을 참조합니다."}
:::

[리눅스 파티션과 파일 시스템 관리하기](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)에서 복구에 안전한 실습용 보조 저장 장치를 사용해 연습하십시오.

## 요약

이제 영구 파일 시스템 테이블 항목을 읽고 검증할 수 있습니다.

1. 소스, 대상, 유형, 옵션, dump 및 pass 필드를 해석합니다.
2. 의도한 식별 의미에 맞는 검증된 식별자를 선택합니다.
3. 실제 파일 시스템에 맞는 마운트 및 검사 정책을 선택합니다.
4. 복구 접근을 유지하고 범위가 좁은 변경 하나를 수행합니다.
5. 정적 검증, 대상별 마운트 및 부팅 정책 확인을 함께 사용합니다.
