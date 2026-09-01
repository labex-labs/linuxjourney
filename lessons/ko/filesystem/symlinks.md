---
lesson_id: "symlinks"
course_id: "filesystem"
lang: "ko"
order_index: 12
title: "심볼릭 링크"
description: "심볼릭 링크와 하드 링크가 경로 해석, inode 식별 정보 및 파일 시스템 범위에서 어떻게 다른지 알아봅니다."
meta_title: "심볼릭 링크 - 파일 시스템"
meta_description: "리눅스 심볼릭 링크와 하드 링크를 살펴봅니다. ln 명령으로 링크를 만들고 ls로 링크 수를 확인하며 두 링크 유형의 차이를 이해합니다."
meta_keywords: "리눅스 심볼릭 링크, 하드 링크, ln 명령어, 심볼릭 링크, ls 링크, 리눅스 링크 수, 리눅스 파일 시스템"
---

디렉터리 항목은 inode에 이름을 부여합니다. 하드 링크는 같은 inode를 위한 다른 디렉터리 항목을 만들고, 심볼릭 링크는 해석할 경로 이름을 내용으로 가진 별도의 inode를 만듭니다. 이 차이에 따라 식별 정보, 수명 및 파일 시스템 간 동작이 결정됩니다.

## 심볼릭 링크 만들고 검사하기

`ln -s TARGET LINK_NAME`으로 심볼릭 링크를 만듭니다.

```bash
$ printf '%s\n' 'example' > myfile
$ ln -s -- myfile myfilelink
$ ls -li myfile myfilelink
151   -rw-r--r-- 1 user user 8 ... myfile
93403 lrwxrwxrwx 1 user user 6 ... myfilelink -> myfile
```

심볼릭 링크는 자체 inode를 가지며 `myfile`이라는 텍스트를 저장합니다. 프로그램이 `myfilelink`를 따르면 경로 이름 해석이 대상으로 계속됩니다. 링크를 따르지 않고 저장된 텍스트를 표시합니다.

```bash
$ readlink myfilelink
```

:::single-choice{#symlinks-create-symbolic} 대상 텍스트가 `myfile`인 심볼릭 링크 `myfilelink`를 만드는 명령은 무엇입니까?

::option[`ln -s -- myfile myfilelink`]{#symlinks-ln-s .correct explanation="`-s` 옵션은 심볼릭 링크를 요청하며 그 뒤에 대상과 새 링크 이름을 지정합니다."}
::option[`ln -- myfile myfilelink`]{#symlinks-ln-hard explanation="`-s`가 없으면 `ln`은 기존 inode에 대한 하드 링크를 요청합니다."}
::option[`readlink myfile myfilelink`]{#symlinks-readlink-create explanation="readlink는 심볼릭 링크를 검사하며 링크를 만들지 않습니다."}
:::

## 상대 및 절대 심볼릭 링크 대상

절대 대상은 `/`에서 시작합니다. 상대 대상은 나중에 누군가 열 때 셸의 현재 디렉터리가 아니라 심볼릭 링크를 포함한 디렉터리를 기준으로 해석됩니다.

```bash
$ mkdir -p tree/data tree/current
$ printf '%s\n' 'value' > tree/data/item
$ ln -s ../data/item tree/current/item
```

`tree` 계층 전체를 옮기면 이 상대 관계가 유지됩니다. 링크나 대상만 옮기면 끊어질 수 있습니다. 심볼릭 링크는 존재하지 않는 대상을 포함할 수 있으며 이를 끊어진 링크라고 합니다.

:::single-choice{#symlinks-relative-resolution} 상대 심볼릭 링크 대상은 어디를 기준으로 해석됩니까?

::option[링크를 만든 사용자의 홈 디렉터리입니다.]{#symlinks-creator-home explanation="생성자 식별 정보가 영구적인 해석 기준이 되지는 않습니다."}
::option[처음 목록을 표시한 셸의 현재 디렉터리입니다.]{#symlinks-listing-shell explanation="목록 컨텍스트는 저장된 대상 관계를 다시 쓰지 않습니다."}
::option[심볼릭 링크를 포함한 디렉터리입니다.]{#symlinks-containing-directory .correct explanation="경로 순회는 심볼릭 링크의 위치에서 저장된 상대 텍스트를 대입합니다."}
:::

## 하드 링크 만들기

`-s` 없이 기존 일반 파일에 다른 이름을 만듭니다.

```bash
$ ln -- myfile myhardlink
$ ls -li myfile myhardlink
151 -rw-r--r-- 2 user user 8 ... myfile
151 -rw-r--r-- 2 user user 8 ... myhardlink
```

두 이름은 같은 파일 시스템과 inode 번호에 매핑됩니다. 링크 수는 2가 됩니다. 어느 이름도 본질적으로 “원본”은 아닙니다. 한 이름을 통해 내용을 변경하면 공유 객체가 바뀌고 이름 하나를 제거해도 다른 이름은 남습니다.

inode 번호는 해당 파일 시스템 안에서만 의미가 있으므로 하드 링크는 파일 시스템 경계를 넘을 수 없습니다. 리눅스는 순환과 보안 문제를 막기 위해 일반 사용자가 디렉터리에 하드 링크를 만들지 못하게 하고 자신이 소유하지 않은 파일의 링크도 제한할 수 있습니다.

:::single-choice{#symlinks-hard-link-inode} 일반 파일 하나를 가리키는 두 하드 링크가 공유하는 것은 무엇입니까?

::option[비슷한 파일 이름만 공유하고 파일 데이터는 별개입니다.]{#symlinks-separate-data explanation="이는 하드 링크가 아니라 독립적인 사본을 설명합니다."}
::option[별도 심볼릭 링크 inode 안에 저장된 경로 이름입니다.]{#symlinks-stored-path explanation="경로 텍스트는 심볼릭 링크를 정의하는 메커니즘입니다."}
::option[같은 inode와 파일 내용입니다.]{#symlinks-same-inode .correct explanation="각 디렉터리 항목은 동일한 파일 시스템 객체에 이름을 붙입니다."}
:::

## 수명과 삭제

심볼릭 링크를 제거하면 대상이 아니라 링크 객체가 제거됩니다.

```bash
$ rm -- myfilelink
```

하드 링크 이름을 제거하면 공유 inode의 링크 수가 감소합니다. 링크 수가 0이 되고 열린 파일 기술이나 다른 파일 시스템 참조도 객체를 유지하지 않을 때만 파일 시스템이 객체를 회수할 수 있습니다.

디렉터리를 가리키는 심볼릭 링크를 제거할 때는 끝에 슬래시를 붙이지 마십시오. 명령에 따라 끝 슬래시 경로 해석이 디렉터리 의미를 따를 수 있습니다. `ls -ld -- LINK`로 검사하고 링크 이름을 의도적으로 제거하십시오.

:::single-choice{#symlinks-remove-symbolic} 심볼릭 링크 자체를 제거하면 일반적으로 어떻게 됩니까?

::option[심볼릭 링크 inode와 이름이 제거되고 대상은 남습니다.]{#symlinks-remove-link-only .correct explanation="심볼릭 링크를 해제해도 저장된 대상 텍스트가 가리키는 객체에는 작업하지 않습니다."}
::option[대상과 대상을 가리키는 모든 하드 링크가 자동으로 지워집니다.]{#symlinks-remove-target explanation="심볼릭 링크는 별도의 파일 시스템 객체이며 대상을 소유하지 않습니다."}
::option[제거 전에 대상이 심볼릭 링크 안으로 복사됩니다.]{#symlinks-copy-target explanation="제거 작업은 대상 내용을 링크 안에 보존하지 않습니다."}
:::

## 안전하게 링크 따르기

심볼릭 링크는 특권 프로그램을 예상 디렉터리 밖으로 리디렉션하거나 검증과 사용 사이에 바뀔 수 있습니다. 안전한 프로그램은 확인한 뒤 여는 경로 이름 경쟁을 피하고 언어와 운영체제에 맞는 디렉터리 상대, 링크 비추적 또는 제한된 해석 인터페이스를 사용해야 합니다.

일반적인 검사에는 다음 명령을 사용합니다.

- `ls -ld LINK`는 링크 자체를 보여 줍니다.
- `readlink LINK`는 저장된 대상 텍스트를 출력합니다.
- `stat LINK`는 일반적으로 링크 메타데이터를 보고하고 GNU coreutils의 `stat -L LINK`는 링크를 따릅니다.
- `find -L`은 링크를 따라가므로 순환을 만날 수 있습니다. 의도한 경우에만 사용하십시오.

`lrwxrwxrwx`로 표시되는 권한은 일반적인 접근 허용을 뜻하지 않습니다. 접근은 디렉터리 순회, 링크 추적 정책 및 대상 권한에 따라 결정되며 일부 보호 디렉터리 규칙에서는 심볼릭 링크 소유권도 중요합니다.

:::single-choice{#symlinks-readlink-output} `readlink LINK`는 기본적으로 무엇을 출력합니까?

::option[심볼릭 링크에 저장된 경로 이름 텍스트입니다.]{#symlinks-readlink-target-text .correct explanation="대상 파일의 내용을 읽지 않고 링크 객체를 검사합니다."}
::option[대상 일반 파일의 전체 바이트 내용입니다.]{#symlinks-readlink-file-content explanation="대상 내용은 의도적으로 해석한 뒤 파일 읽기 명령을 사용하십시오."}
::option[파일 시스템 전체의 모든 하드 링크입니다.]{#symlinks-readlink-all-hard explanation="하드 링크를 찾으려면 inode를 인식하는 파일 시스템 검색이 필요하며 심볼릭 링크 대상 텍스트와 관련이 없습니다."}
:::

[리눅스 파일과 디렉터리 관리하기](https://labex.io/labs/comptia-manage-files-and-directories-in-linux-590835)에서 폐기 가능한 파일로 링크를 연습하고 inode 번호를 비교해 보십시오.

## 요약

이제 올바른 종류의 파일 시스템 링크를 선택하고 검사할 수 있습니다.

1. 경로 기반 심볼릭 링크에는 `ln -s TARGET LINK`를 사용합니다.
2. 상대 대상은 링크를 포함한 디렉터리에서 해석합니다.
3. 같은 파일 시스템의 inode에 다른 이름을 만들 때는 `ln EXISTING LINK`를 사용합니다.
4. 심볼릭 링크 해제와 하드 링크 해제를 구분합니다.
5. 특권 또는 재귀 작업에서 안전하지 않은 링크 추적을 피합니다.
