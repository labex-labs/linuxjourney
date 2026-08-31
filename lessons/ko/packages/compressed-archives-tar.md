---
lesson_id: "compressed-archives-tar"
course_id: "packages"
lang: "ko"
order_index: 3
title: "tar와 gzip"
description: "`tar`로 파일을 아카이브하고, `gzip`으로 스트림을 압축하며, 안전하게 풀기 전에 아카이브를 검사하는 방법을 알아봅니다."
meta_title: "tar와 gzip - 패키지"
meta_description: "리눅스에서 tar와 gzip을 사용하는 방법을 알아봅니다. 아카이브 생성과 해제, tar와 gzip의 차이, tar.gz 파일 압축 및 안전한 관리 방법을 익힙니다."
meta_keywords: "tar와 gzip, tar 압축, gzip tar, tar.gz 압축, 리눅스 아카이브, 파일 압축, tar 명령어, gzip 명령어, 리눅스 튜토리얼"
---

아카이브와 압축은 서로 다른 문제를 해결합니다. 아카이브는 디렉터리 트리와 그 메타데이터를 하나의 스트림으로 결합합니다. 압축은 스트림의 크기를 줄이도록 인코딩합니다. `.tar.gz` 파일은 관례상 gzip으로 스트림을 압축한 tar 아카이브입니다.

## `gzip`으로 단일 스트림 압축하기

기본적으로 `gzip`은 파일을 압축하고 원래 이름을 `.gz` 파일로 바꿉니다.

```bash
$ gzip report.txt
```

일반적으로 `report.txt.gz`를 성공적으로 만든 뒤 `report.txt`를 제거합니다. 다음 명령으로 압축을 풉니다.

```bash
$ gunzip report.txt.gz
```

지원되는 환경에서 입력 파일을 유지하려면 `gzip -k report.txt`를 사용하고, 명시적으로 제어해야 한다면 표준 스트림을 사용하십시오. 파일 이름 확장자는 관례일 뿐 실제 형식의 증거는 아닙니다. `file` 같은 도구로 내용을 검사할 수 있습니다.

:::single-choice{#tar-gzip-gzip-role}
이 수업에서 `gzip`의 주된 역할은 무엇입니까?

::option[파일 메타데이터와 함께 디렉터리 트리를 하나의 아카이브로 결합합니다.]{#tar-gzip-directory-archive explanation="gzip 압축을 적용하기 전에 tar가 이 아카이브 역할을 수행합니다."}
::option[하나의 입력 스트림을 압축합니다.]{#tar-gzip-compress-stream .correct explanation="gzip은 하나의 바이트 스트림을 변환하며 디렉터리 계층 구조 자체를 인코딩하지는 않습니다."}
::option[패키지 데이터베이스에 의존성 메타데이터를 설치합니다.]{#tar-gzip-package-install explanation="압축은 네이티브 패키지 설치 및 의존성 추적과 별개의 작업입니다."}
:::

## Tar 아카이브 만들기

다음 명령으로 압축하지 않은 아카이브를 만듭니다.

```bash
$ tar -cvf project.tar file1 file2 directory1
```

- `-c`는 새 아카이브를 만듭니다.
- `-v`는 처리 중인 멤버를 나열하며 선택 사항입니다.
- `-f project.tar`는 아카이브 파일 이름을 지정합니다. `-f`는 인수를 하나 소비하므로 파일 이름을 바로 옆에 두십시오.

경로는 아카이브 멤버 이름으로 저장됩니다. 의도한 작업 디렉터리에서 아카이브를 만들고 비밀 정보, 캐시, 소켓 또는 광범위한 절대 경로가 뜻하지 않게 포함되지 않도록 주의하십시오.

:::single-choice{#tar-gzip-create-option}
새 아카이브를 만드는 `tar` 옵션은 무엇입니까?

::option[`-x`]{#tar-gzip-option-extract explanation="`-x` 작업은 아카이브 멤버를 추출합니다."}
::option[`-c`]{#tar-gzip-option-create .correct explanation="생성 작업은 지정한 입력으로 새 아카이브를 기록합니다."}
::option[`-t`]{#tar-gzip-option-list explanation="`-t` 작업은 멤버를 추출하지 않고 목록을 표시합니다."}
:::

## Gzip으로 압축된 Tar 아카이브 만들기

GNU tar를 비롯한 여러 구현은 `-z` 옵션으로 gzip을 호출할 수 있습니다.

```bash
$ tar -czvf project.tar.gz file1 file2 directory1
```

결과는 gzip으로 압축된 하나의 tar 스트림입니다. 압축은 아카이브를 암호화하지 않으며, 파일을 읽고 압축을 풀 수 있는 사람에게 내용을 숨기지도 않습니다. 기밀성이 필요하다면 적절한 인증 암호화 작업 흐름을 사용하고 키를 별도로 관리하십시오.

:::single-choice{#tar-gzip-z-option}
위 `tar` 명령에서 `-z`는 무엇을 요청합니까?

::option[제로 지식 키를 사용해 아카이브를 암호화합니다.]{#tar-gzip-z-encrypt explanation="tar와 gzip 어느 쪽도 이 옵션으로 암호화를 제공하지 않습니다."}
::option[길이가 0인 모든 멤버를 버립니다.]{#tar-gzip-z-zero explanation="이 옵션은 gzip을 선택하며 크기에 따라 아카이브 멤버를 걸러내지 않습니다."}
::option[아카이브 스트림을 gzip으로 처리합니다.]{#tar-gzip-z-gzip .correct explanation="z 옵션은 tar의 아카이브 작업을 gzip 압축 또는 해제와 연결합니다."}
:::

## 추출하기 전에 목록 확인하기

다른 사람이 제공한 아카이브는 신뢰할 수 없는 입력으로 취급하십시오. 먼저 멤버 이름을 나열합니다.

```bash
$ tar -tzf download.tar.gz
```

예상하지 못한 절대 경로, `..` 경로 순회 구성 요소, 의심스러운 심볼릭 링크나 하드 링크, 장치 파일 및 중요 파일을 덮어쓸 이름이 있는지 확인하십시오. 최신 tar 구현에는 보호 기능이 있지만 동작과 옵션은 구현마다 다르며, 추출하면 여전히 공격자가 정한 이름과 내용이 생성됩니다.

새로 만든 비특권 스테이징 디렉터리에 추출합니다.

```bash
$ mkdir extraction-stage
$ tar -xzf download.tar.gz -C extraction-stage
```

검토하지 않은 아카이브를 root로 추출하지 마십시오. 생성된 내용을 확인한 다음 선택한 파일만 최종 위치로 옮기십시오.

:::single-choice{#tar-gzip-list-before-extract}
아카이브 멤버를 추출하지 않고 나열하는 작업은 무엇입니까?

::option[`tar -czf download.tar.gz .`]{#tar-gzip-create-download explanation="이 명령은 현재 디렉터리에서 아카이브를 만들거나 기존 아카이브를 교체합니다."}
::option[`tar -xzf download.tar.gz`]{#tar-gzip-extract-download explanation="`-x` 작업은 대상 디렉터리에 멤버를 기록합니다."}
::option[`tar -tzf download.tar.gz`]{#tar-gzip-list-members .correct explanation="`-t` 작업은 멤버 표를 읽어 표시하고 `-z`는 gzip을 처리합니다."}
:::

## 기타 압축 형식

tar 구현은 bzip2 및 xz 같은 압축 도구와 함께 작동할 수 있으며, GNU tar에서는 일반적으로 각각 `-j`와 `-J`로 선택합니다. 형식 지원 및 자동 감지 방식은 서로 다르므로 `tar --help` 또는 로컬 설명서를 확인하십시오. ZIP은 별도의 아카이브 형식이며 `zip`과 `unzip` 같은 도구로 다룹니다.

:::single-choice{#tar-gzip-archive-confidentiality}
gzip 압축을 적용하면 tar 아카이브의 기밀성이 보장됩니까?

::option[아닙니다. 파일을 읽을 수 있는 사람은 일반적으로 압축도 풀 수 있습니다.]{#tar-gzip-not-encryption .correct explanation="압축은 표현 방식과 크기를 바꾸지만 접근 제어나 암호학적 기밀성을 제공하지 않습니다."}
::option[그렇습니다. gzip이 파일 이름에서 암호화 키를 파생합니다.]{#tar-gzip-filename-key explanation="gzip에는 그러한 암호화 메커니즘이 없습니다."}
::option[그렇습니다. tar가 gzip에 전달하기 전에 모든 멤버를 암호화합니다.]{#tar-gzip-tar-encrypt explanation="tar는 멤버를 아카이브하지만 내용을 자동으로 암호화하지 않습니다."}
:::

[파일 패키징과 압축](https://labex.io/labs/linux-file-packaging-and-compression-385413)에서 폐기해도 되는 파일로 연습한 다음, [tar로 백업 생성 및 복원하기](https://labex.io/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)에서 검사와 스테이징 절차를 적용해 보십시오.

## 요약

이제 tar 아카이브와 gzip 압축을 안전하게 결합할 수 있습니다.

1. tar 아카이브와 gzip 압축을 구분합니다.
2. `-c`로 아카이브를 만들고 `-z`로 gzip 스트림을 처리합니다.
3. `-x`로 추출하기 전에 `-t`로 멤버를 나열합니다.
4. 신뢰할 수 없는 콘텐츠는 비특권 스테이징 디렉터리에 추출합니다.
5. 압축과 암호화는 서로 다른 기능으로 취급합니다.
