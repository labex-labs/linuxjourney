---
lesson_id: "anatomy-of-a-disk"
course_id: "filesystem"
lang: "ko"
order_index: 3
title: "디스크의 구조"
description: "블록 장치, 파티션 테이블, 파티션 및 파일 시스템이 서로 다른 저장 장치 계층을 이루는 방법을 알아봅니다."
meta_title: "디스크의 구조 - 파일 시스템"
meta_description: "리눅스 디스크의 구조를 살펴봅니다. 운영체제에 디스크 파티션 구성을 알려 주는 MBR 및 GPT 파티션 테이블과 각 저장 계층을 설명합니다."
meta_keywords: "리눅스 디스크, 리눅스 파티션, 파티션 유형, MBR, GPT, 파티션 테이블, 파일 시스템, 디스크 구조"
---

저장 장치는 `/dev/sda` 또는 `/dev/nvme0n1` 같은 블록 장치로 노출됩니다. 그 안에는 하위 블록 장치로 노출되는 영역을 설명하는 항목으로 구성된 파티션 테이블이 있을 수 있습니다. 파티션에는 파일 시스템, 스왑 서명, RAID 멤버, 암호화 컨테이너, 논리 볼륨의 물리 볼륨 또는 다른 데이터 형식이 들어갈 수 있습니다.

이 계층들은 서로 독립적입니다. 모든 디스크에 파티션 테이블이 있는 것은 아니고, 모든 파티션에 파일 시스템이 있는 것도 아니며, 파일 시스템은 논리 볼륨이나 전체 장치에 위치할 수도 있습니다.

## 파티션 테이블과 경계

파티션 테이블은 시작 위치, 길이, 유형 식별자 및 파티션 방식별 속성을 기록합니다. 커널은 이를 읽어 `/dev/sda1` 또는 `/dev/nvme0n1p1` 같은 파티션 블록 장치를 만듭니다.

일반적인 레이아웃에서는 파티션 경계가 겹치면 안 됩니다. 모든 항목 밖의 공간은 파티션 테이블 관점에서 할당되지 않은 영역이지만 오래된 서명이나 데이터가 여전히 남아 있을 수 있습니다. 테이블을 변경해도 파일 시스템의 내용이 새 경계에 맞게 자동으로 이동하지는 않습니다.

:::single-choice{#anatomy-disk-partition-table-role} 운영체제에 디스크 파티션의 시작과 끝을 알려 주는 것은 무엇입니까?

::option[현재 셸의 작업 디렉터리입니다.]{#anatomy-disk-shell-directory explanation="셸 경로는 디스크의 파티션 경계와 관련이 없습니다."}
::option[디스크의 파티션 테이블입니다.]{#anatomy-disk-table-boundaries .correct explanation="파티션 항목은 커널이 하위 블록 장치로 노출할 수 있는 영역을 설명합니다."}
::option[사용자 계정의 기본 그룹입니다.]{#anatomy-disk-user-group explanation="계정 자격 증명은 디스크 구조나 파티션 레이아웃을 정의하지 않습니다."}
:::

## MBR 파티셔닝

레거시 DOS/MBR 방식은 첫 번째 논리 섹터에 기본 테이블을 저장합니다. 이 테이블에는 주 파티션 항목이 네 개 있습니다. 한 항목은 연결된 논리 파티션 열의 컨테이너 역할을 하는 확장 파티션을 설명할 수 있어, 사용 가능한 영역을 네 개보다 많이 만들 수 있습니다.

32비트 섹터 주소와 512바이트 논리 섹터를 사용할 때 MBR의 흔히 언급되는 한계는 약 2 TiB입니다. 정확한 주소 지정 범위는 섹터 크기와 도구 지원에 따라 달라집니다. MBR에는 GPT의 중복 헤더 및 테이블 사본과 파티션별 GUID도 없습니다.

:::single-choice{#anatomy-disk-mbr-more-than-four} MBR에서 사용 가능한 파티션을 네 개보다 많이 만들 수 있게 하는 구조는 무엇입니까?

::option[주 파티션 항목을 더 담는 저널 파티션입니다.]{#anatomy-disk-mbr-journal explanation="파일 시스템 저널링은 네 항목으로 된 MBR 테이블과 관련이 없습니다."}
::option[논리 파티션을 담는 확장 파티션입니다.]{#anatomy-disk-mbr-extended .correct explanation="주 항목 하나가 확장 컨테이너를 정의하고 그 안에서 논리 파티션이 연결됩니다."}
::option[항목의 번호를 다시 매기는 파일 시스템 슈퍼블록입니다.]{#anatomy-disk-mbr-superblock explanation="파일 시스템 메타데이터는 디스크 파티션 테이블을 확장하지 않습니다."}
:::

## GPT 파티셔닝

GUID 파티션 테이블(GPT)은 64비트 논리 블록 주소를 사용하며, 일반적으로 디스크 시작 부분 근처에 주 헤더와 항목 배열을, 끝 부분 근처에 백업 사본을 저장합니다. 보호 MBR은 구형 MBR 전용 소프트웨어가 디스크를 빈 것으로 취급하지 않도록 돕습니다.

각 GPT 항목에는 파티션 유형 GUID와 고유 파티션 GUID가 있습니다. 따라서 GPT에 파티션 유형이 하나만 있는 것은 아닙니다. 사용할 수 있는 항목 수는 할당된 테이블과 도구가 결정하며 일반적으로 네 개보다 훨씬 많고 확장 또는 논리 파티션이 필요하지 않습니다.

GPT는 보통 UEFI 부팅 디스크에 사용되지만 파티셔닝과 펌웨어 부팅 모드는 서로 다른 개념입니다. UEFI 시스템에는 적절한 부팅 파일과 EFI 시스템 파티션도 필요합니다. GPT만으로 디스크가 부팅 가능해지지는 않습니다.

:::single-choice{#anatomy-disk-gpt-identifiers} GPT 파티션 항목에는 어떤 식별자가 들어 있습니까?

::option[유형 GUID와 고유 파티션 GUID입니다.]{#anatomy-disk-gpt-guids .correct explanation="유형은 의도된 용도를 설명하고 고유 GUID는 해당 파티션 항목을 식별합니다."}
::option[모든 GPT 파티션이 공유하는 하나의 범용 유형만 있습니다.]{#anatomy-disk-gpt-one-type explanation="GPT는 다양한 파티션 용도를 위한 여러 유형 GUID를 정의합니다."}
::option[파티션을 만든 사용자의 로그인 UID와 GID입니다.]{#anatomy-disk-gpt-user-ids explanation="파일 시스템 계정 식별자는 GPT 파티션 식별 필드가 아닙니다."}
:::

## 파일 시스템 구조는 형식마다 다름

파티셔닝 후 파일 시스템 생성 도구는 해당 파일 시스템이 정의한 구조를 기록합니다. 여러 형식에는 슈퍼블록, 할당 메타데이터, 디렉터리 레코드 및 데이터 익스텐트 또는 블록 같은 개념이 있지만 레이아웃, 중복성 및 용어는 서로 다릅니다.

예를 들어 ext 파일 시스템은 inode와 블록 그룹을 사용하지만 다른 파일 시스템은 서로 다른 트리나 할당 구조로 메타데이터를 구성합니다. “부트 블록, 슈퍼블록 하나, inode 테이블, 데이터 블록”이라는 단순한 도식을 모든 파일 시스템에 적용하지 마십시오.

:::single-choice{#anatomy-disk-filesystem-layer} 파티션을 만들면 그 안에 파일 시스템도 자동으로 생성됩니까?

::option[아닙니다. 포맷이나 다른 명시적인 용도 지정은 별도 단계입니다.]{#anatomy-disk-partition-not-filesystem .correct explanation="파티션 테이블은 블록 영역만 정의하며 그 내용은 독립적으로 남습니다."}
::option[그렇습니다. 모든 파티션은 자동으로 ext4로 포맷됩니다.]{#anatomy-disk-auto-ext4 explanation="파티셔닝 도구가 보편적으로 ext4 파일 시스템을 만들지는 않습니다."}
::option[그렇습니다. GPT 항목 자체가 마운트된 디렉터리입니다.]{#anatomy-disk-gpt-mounted explanation="파티션 항목은 저장 공간을 설명하며 파일 시스템 마운트 지점이 아닙니다."}
:::

## 현재 레이아웃 검사하기

변경하기 전에 읽기 전용 뷰를 사용합니다.

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,PTTYPE,PARTTYPE,FSTYPE,MOUNTPOINTS
$ sudo parted --list
```

`PTTYPE`은 감지된 파티션 테이블 방식을, `PARTTYPE`은 파티션 유형 식별자를, `FSTYPE`은 감지된 콘텐츠 서명을 설명합니다. 감지 결과는 증거일 뿐 콘텐츠가 정상적이거나 마운트해도 안전하다는 보장은 아닙니다.

장치 이름은 바뀔 수 있고 오래된 서명이 감지를 혼란스럽게 할 수 있습니다. 파티셔닝 도구를 쓰기 모드로 열기 전에 모델, 일련번호, 크기, 전송 방식, 영구 링크, 활성 마운트, 스왑, RAID, LVM, 암호화 및 백업을 확인하십시오.

:::single-choice{#anatomy-disk-lsblk-fields} 감지된 파일 시스템 콘텐츠를 파티션 테이블 방식과 구분하는 `lsblk` 필드는 무엇입니까?

::option[`FSTYPE`]{#anatomy-disk-fstype .correct explanation="`FSTYPE`은 감지된 파일 시스템 또는 인식된 다른 콘텐츠 서명을 보고하고 `PTTYPE`은 테이블 방식을 보고합니다."}
::option[`NAME`]{#anatomy-disk-name-field explanation="`NAME`은 커널 블록 장치 항목에 이름을 붙이며 콘텐츠 형식을 구체적으로 식별하지 않습니다."}
::option[`SIZE`]{#anatomy-disk-size-field explanation="크기는 파일 시스템 유형이 아니라 용량을 보고합니다."}
:::

이 계층을 연습할 때는 [리눅스 파티션과 파일 시스템 관리하기](https://labex.io/labs/comptia-manage-linux-partitions-and-filesystems-590845)를 폐기 가능한 저장 장치에서만 사용하십시오.

## 요약

이제 디스크 레이아웃 메타데이터를 그 안에 저장된 데이터 형식과 구분할 수 있습니다.

1. 전체 장치와 하위 파티션 장치를 식별합니다.
2. MBR 확장 파티션을 레거시 네 항목 한계와 연결합니다.
3. GPT를 중복 테이블 및 파티션별 GUID와 연결합니다.
4. 파일 시스템 생성과 파티션 생성을 별개로 취급합니다.
5. 변경 전에 모든 저장 장치 계층과 활성 사용자를 검사합니다.
