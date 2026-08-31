---
lesson_id: "rsync"
course_id: "network-sharing"
lang: "ko"
order_index: 2
title: "rsync"
description: "rsync로 안전한 로컬 또는 SSH 기반 디렉터리 동기화를 미리 보고 실행하며 검증하는 방법을 알아봅니다."
meta_title: "rsync - 네트워크 공유"
meta_description: "리눅스의 강력한 rsync 명령으로 파일 동기화, 원격 데이터 전송 및 신뢰할 수 있는 백업을 수행하는 방법을 알아봅니다."
meta_keywords: "rsync, 리눅스 rsync, 파일 동기화, 데이터 백업, 원격 동기화, rsync 명령, 리눅스 파일 전송"
---

`rsync`는 변경되지 않은 데이터를 불필요하게 전송하지 않으면서 파일과 디렉터리 트리를 동기화합니다. 효율적이라고 해서 모든 실행이 안전한 것은 아닙니다. 소스 구문, 후행 슬래시, 메타데이터, 제외 규칙 및 삭제 정책이 결과를 결정합니다.

## 소스와 대상 읽기

로컬에서 `source/`의 내용을 `destination/`으로 동기화합니다.

```bash
$ rsync -a -- source/ destination/
```

`source/`의 후행 슬래시는 “이 디렉터리의 내용을 복사”한다는 뜻입니다. 슬래시가 없는 `rsync -a source destination/`은 `destination/source`를 만들거나 갱신합니다. 슬래시 위치를 바꿀 때는 항상 결과 경로를 미리 확인하십시오.

:::single-choice{#rsync-source-trailing-slash}
`rsync -a source/ destination/`에서 소스의 후행 슬래시는 무엇을 뜻합니까?

::option[전송 성공 후 소스를 삭제합니다.]{#rsync-delete-source explanation="소스를 제거하려면 별도의 명시적인 옵션과 정책이 필요합니다."}
::option[`source`의 내용을 대상에 복사합니다.]{#rsync-copy-contents .correct explanation="소스 슬래시를 제거하면 대상의 최상위 디렉터리 배치가 달라집니다."}
::option[대상을 원격 Windows 공유로 해석합니다.]{#rsync-windows-share explanation="슬래시는 전송 방식이 아니라 디렉터리 내용을 제어합니다."}
:::

## 아카이브 모드 이해하기

아카이브 모드 `-a`는 흔히 `-rlptgoD`로 요약되는 재귀 및 메타데이터 보존 옵션 모음과 같습니다. 권한과 플랫폼이 지원하는 범위에서 심볼릭 링크, 권한, 수정 시간, 그룹, 소유자 및 장치나 특수 파일을 보존합니다.

아카이브 모드만으로는 하드 링크, ACL 또는 확장 속성이 보존되지 않습니다. 일반적으로 각각 `-H`, `-A` 및 `-X`가 필요합니다. 또한 아카이브 모드 자체는 이전 버전을 만들지 않습니다.

:::single-choice{#rsync-archive-limit}
`-a`만으로 포함되지 않는 메타데이터는 무엇입니까?

::option[하드 링크 관계입니다.]{#rsync-hard-links .correct explanation="하드 링크를 보존하려면 별도의 -H 옵션이 필요합니다."}
::option[디렉터리 재귀 순회입니다.]{#rsync-archive-recursion explanation="아카이브 모드에는 재귀 순회가 포함됩니다."}
::option[수정 시간입니다.]{#rsync-archive-times explanation="아카이브 모드에는 시간 보존이 포함됩니다."}
:::

## 전송 미리 보기

결과가 중요한 동기화를 실행하기 전에 항목별 변경 내용과 함께 시험 실행합니다.

```bash
$ rsync -a --dry-run --itemize-changes -- source/ destination/
```

시험 실행은 현재 스캔을 바탕으로 동작을 예측하지만 실제 명령 전까지 파일이 바뀌지 않는다고 보장하지 않습니다. 정확한 명령을 저장하고 검토한 뒤 양쪽 끝점을 확인한 후에만 `--dry-run`을 제거해 실행합니다.

:::single-choice{#rsync-dry-run-purpose}
`--dry-run --itemize-changes`는 무엇을 제공합니까?

::option[다른 장치에 영구 보존되는 스냅샷입니다.]{#rsync-dry-backup explanation="시험 실행은 데이터를 복사하거나 독립적인 보존 사본을 만들지 않습니다."}
::option[소스 파일이 이후에 변경될 수 없다는 보장입니다.]{#rsync-dry-lock explanation="미리 보기는 소스 트리를 잠그지 않습니다."}
::option[rsync가 현재 계획한 변경의 미리 보기입니다.]{#rsync-dry-preview .correct explanation="항목별 시험 실행 출력은 변경 전에 경로와 메타데이터 결정을 보여 줍니다."}
:::

## SSH를 통해 동기화하기

익숙한 원격 피연산자로 원격 호스트에 보내거나 원격 호스트에서 가져옵니다.

```bash
$ rsync -a -- source/ alice@example.net:/srv/data/
$ rsync -a -- alice@example.net:/srv/data/ destination/
```

현대의 rsync는 보통 이 형식에 SSH를 사용하지만 설정된 원격 셸, 호스트 키, 계정 권한 및 원격 rsync 설치 여부를 확인하십시오. `-z` 압축은 제한된 링크에서 압축 가능한 데이터에 도움이 될 수 있지만 이미 압축된 데이터에는 CPU를 낭비할 수 있습니다.

:::single-choice{#rsync-pull-direction}
원격 데이터를 로컬 디렉터리로 가져오는 피연산자 순서는 무엇입니까?

::option[`rsync -a local/ host:/data/`]{#rsync-local-first explanation="이 순서는 로컬 내용을 원격 대상으로 보냅니다."}
::option[`rsync --delete host local`]{#rsync-missing-path explanation="표시된 원격 경로 구문을 표현하지 못하며 관련 없는 파괴적 옵션까지 추가합니다."}
::option[`rsync -a host:/data/ local/`]{#rsync-remote-first .correct explanation="원격 트리가 소스이고 로컬 트리가 대상입니다."}
:::

## 삭제를 파괴적 작업으로 다루기

`--delete`는 동기화 범위 안에서 소스에 없는 대상 항목을 제거합니다. 끝점을 반대로 지정하거나 슬래시를 잘못 쓰거나 제외 규칙이 틀리면 유효한 데이터가 지워질 수 있습니다. 테스트 대상을 상대로 미리 보고, 복구 가능한 백업을 확보하고, 마운트 상태를 검토하며, 승인 전에 최대 삭제 제한도 고려하십시오.

실제 실행 후에는 종료 상태와 로그를 조사하고 예상 파일 수와 메타데이터를 비교하며 대표 콘텐츠나 복원을 테스트합니다. rsync 동기화만으로는 원치 않는 삭제나 손상도 복제되므로 완전한 백업 전략이 아닙니다.

:::single-choice{#rsync-delete-effect}
`--delete`는 동기화 중 무엇을 할 수 있습니까?

::option[전송되는 모든 파일을 SSH 호스트 키로 암호화합니다.]{#rsync-delete-encrypt explanation="삭제 정책은 파일 암호화와 관계없습니다."}
::option[대상 파일시스템의 모든 변경을 막습니다.]{#rsync-delete-readonly explanation="이 옵션은 명시적으로 추가 대상 변경을 허용합니다."}
::option[선택한 소스 범위에 없는 대상 항목을 제거합니다.]{#rsync-delete-destination .correct explanation="대상의 구성원을 소스와 일치시키므로 검토한 미리 보기와 복구 계획이 필요합니다."}
:::

## 요약

이제 파괴적인 예외 상황을 숨기지 않고 `rsync` 작업을 미리 보고 검증할 수 있습니다.

1. 후행 슬래시로 의도한 디렉터리 배치를 표현합니다.
2. 필요하면 아카이브 모드가 포함하지 않는 메타데이터 옵션을 추가합니다.
3. 실제 동기화 전에 항목별 시험 실행 출력을 검토합니다.
4. SSH 신원과 끝점 방향을 검증합니다.
5. 삭제와 백업 보존을 명시적인 정책으로 다룹니다.
