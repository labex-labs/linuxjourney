---
lesson_id: "remove-rm-command"
course_id: "command-line"
lang: "ko"
order_index: 13
title: "rm (삭제)"
description: "대상을 확인하고 안전한 옵션을 선택하면서 파일과 디렉터리를 제거하는 방법을 배웁니다."
meta_title: "rm (삭제) - 커맨드 라인"
meta_description: "파일 삭제, 디렉토리 제거, rm -r, rm -i 사용법과 rm -rf 실수 방지를 위한 안전한 예제로 Linux rm 명령어를 배워보세요."
meta_keywords: "linux rm 명령어, rm 명령어, rm -r, rm -i, rm -f, rm -rf, 리눅스 파일 삭제, 리눅스 디렉토리 제거, rmdir"
---

`rm` 명령어는 파일 시스템 항목을 제거합니다. 커맨드 라인 삭제는 보통 데스크톱 휴지통으로 보내지 않으며 `rm`에는 실행 취소 기능이 없으므로 실행 전에 모든 대상을 확인해야 합니다.

기본 문법은 다음과 같습니다.

```bash
rm [OPTIONS] FILE...
```

## 파일 제거하기

한 개의 파일을 삭제하려면 파일 이름을 `rm`에 전달하면 됩니다.

```bash
$ rm file1
```

```bash
$ rm notes.txt old-report.txt draft.md
```

Enter를 누르기 전에 철자와 위치를 확인하세요. 삭제 후 파일 시스템 복구 도구에 의존하는 것보다 백업이나 버전 관리 복사본이 더 확실한 복구 방법입니다.

:::single-choice{#remove-one-file}
대상을 확인한 뒤 `old-report.txt` 파일을 제거하는 명령어는 무엇인가요?

::option[`rm old-report.txt`]{#rm-report .correct explanation="`rm`은 지정한 파일 항목을 제거하며 보통 휴지통에 넣지 않습니다."}
::option[`rmdir old-report.txt`]{#rmdir-report explanation="`rmdir`은 일반 파일이 아닌 빈 디렉터리에 사용하므로 이 대상에 맞지 않습니다."}
::option[`mv old-report.txt`]{#mv-report explanation="`mv`는 목적지가 필요하고 경로를 바꿀 뿐 삭제하지 않으므로 이 불완전한 명령어는 요청을 수행하지 않습니다."}
:::

## 와일드카드 대상 미리 보기

셸 와일드카드를 사용하면 여러 파일을 한꺼번에 지정할 수 있습니다. 예를 들어, 현재 디렉토리의 모든 `.tmp` 파일을 삭제하려면 다음과 같이 합니다:

```bash
$ rm *.tmp
```

와일드카드와 함께 `rm`을 사용하기 전에는 `ls`로 삭제 대상 파일을 미리 확인하는 것이 안전합니다.

```bash
$ ls *.tmp
cache.tmp  test.tmp
$ rm *.tmp
```

셸이 `rm` 실행 전에 `*.tmp`를 확장한다는 점을 기억하세요. 패턴이 예상보다 많은 파일과 일치하면 `rm`은 모두를 받게 됩니다.

:::single-choice{#preview-removal-pattern}
`*.tmp`를 제거하기 전에 삭제 없이 패턴이 선택한 숨김 항목 이외의 경로를 보여 주는 명령어는 무엇인가요?

::option[`rm -v *.tmp`]{#verbose-remove explanation="상세 모드는 제거하면서 작업을 보고하므로 읽기 전용 미리보기가 아닙니다."}
::option[`ls '*.tmp'`]{#quoted-pattern explanation="따옴표가 와일드카드 확장을 막아 의도한 대상 대신 `*`가 든 문자 그대로의 이름을 찾습니다."}
::option[`ls *.tmp`]{#list-temp-matches .correct explanation="쉘이 `ls`의 `*.tmp`도 확장하므로 제거 전에 같은 숨김 항목 이외의 일치 집합을 확인할 수 있습니다."}
:::

## 확인 요청하기

더 안전한 방법으로 `-i` 옵션을 사용하면 파일 하나하나를 삭제하기 전에 확인을 요청합니다.

```bash
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
```

GNU `rm`의 `-I`는 덜 번거로운 보호 장치로, 세 개보다 많은 파일을 제거하거나 재귀 작업을 할 때 한 번만 묻습니다.

:::single-choice{#confirm-each-removal}
지정한 파일을 각각 제거하기 전에 확인을 요청하는 명령어는 무엇인가요?

::option[`rm -i important.txt`]{#interactive-important .correct explanation="`-i`는 각 제거 전에 물어보므로 작업을 거부할 기회를 줍니다."}
::option[`rm -f important.txt`]{#force-important explanation="`-f`는 질문을 없애고 없는 피연산자를 무시하므로 확인을 추가하지 않습니다."}
::option[`rm -v important.txt`]{#verbose-important explanation="`-v`는 제거한 항목을 보고하지만 먼저 승인을 요청하지 않습니다."}
:::

## -f로 없는 파일 무시하기

`-f` 옵션은 "force"를 의미합니다. 존재하지 않는 파일을 무시하고 확인을 요청하지 않습니다.

```bash
$ rm -f old-cache.txt
```

스크립트에서 파일이 이미 없어도 정리를 계속해야 할 때 유용합니다. `-f`는 일부 안전 확인 메시지도 숨기므로 실수를 감출 수 있습니다.

## 디렉터리 제거하기

기본적으로 `rm`은 디렉토리를 삭제할 수 없습니다.

```bash
$ rm projects
rm: cannot remove 'projects': Is a directory
```

디렉토리와 그 안의 모든 내용을 삭제하려면 재귀적 삭제를 의미하는 `-r` 또는 `-R` 옵션을 사용하세요.

```bash
$ rm -r old-project
```

빈 디렉터리는 더 좁은 범위의 `rmdir`로 제거할 수 있습니다.

```bash
$ rmdir empty-directory
```

`rmdir`는 디렉터리가 비어 있지 않으면 실패하므로 내부 항목을 재귀적으로 삭제하지 않습니다.

:::single-choice{#remove-empty-directory-only}
`old-cache/`가 비어 있을 때만 제거하는 명령어는 무엇인가요?

::option[`rm -r old-cache/`]{#recursive-cache explanation="재귀 `rm`은 디렉터리와 내용을 제거하므로 빈 디렉터리 조건을 강제하지 않습니다."}
::option[`rmdir old-cache/`]{#rmdir-cache .correct explanation="`rmdir`는 빈 디렉터리에서만 성공하므로 내부 파일을 재귀 삭제하지 않습니다."}
::option[`rm -f old-cache/`]{#force-cache explanation="`-f`는 일반 `rm`으로 디렉터리를 제거하게 하지 않으며 비어 있는지 확인하는 대신 보호 장치를 줄입니다."}
:::

## 재귀 제거 확인하기

재귀 삭제는 전체 트리를 제거하므로 위험합니다. 항상 다음을 확인하세요:

- 현재 위치가 예상한 디렉토리인지? `pwd`를 사용하세요.
- `ls -ld -- TARGET`이 의도한 최상위 경로를 보여주는지 확인하세요.
- 와일드카드가 올바르게 확장되었는지? `ls`로 미리 확인하세요.
- 경로가 절대 경로인지 상대 경로인지? `/tmp/cache`와 `tmp/cache`는 매우 다릅니다.
- 실수로 공백이 있는지? `rm -rf old-project`와 `rm -rf old project`는 다른 경로를 대상으로 합니다.

하이픈으로 시작할 수 있는 대상 앞에는 옵션으로 오해하지 않도록 `--`를 사용합니다.

```bash
$ rm -- -old-name
```

권한 오류가 난다는 이유만으로 곧바로 `sudo`를 사용하지 마세요. 먼저 대상과 계정이 상위 디렉터리를 수정할 수 없는 이유를 확인합니다. 관리자 권한의 재귀 삭제는 운영체제나 다른 사용자의 데이터를 손상시킬 수 있습니다.

성공한 제거 항목을 보고 싶다면 `-v`를 사용합니다.

```bash
$ rm -rv old-project
removed 'old-project/notes.txt'
removed directory 'old-project'
```

:::single-choice{#remove-nonempty-tree}
전체 대상을 확인한 뒤 일반 확인 동작은 유지하면서 `old-project/`와 그 아래 모든 항목을 제거하는 명령어는 무엇인가요?

::option[`rm old-project/`]{#plain-rm-project explanation="일반 `rm`은 디렉터리 안으로 내려가지 않으므로 비어 있지 않은 트리를 제거할 수 없습니다."}
::option[`rm -r old-project/`]{#recursive-old-project .correct explanation="`-r`은 디렉터리 트리를 재귀 제거하며 `-rf`와 달리 질문을 없애는 `-f`를 추가하지 않습니다."}
::option[`rmdir old-project/`]{#rmdir-project explanation="`rmdir`는 빈 디렉터리만 제거하므로 프로젝트 안에 항목이 남아 있으면 실패합니다."}
:::

통제된 환경에서 제거를 연습하려면 다음 실습을 활용해 보세요.

1. **[Linux rm 명령어: 파일 삭제](https://labex.io/ko/labs/linux-linux-rm-command-file-removing-209741)** - `rm` 명령어와 `-r`, `-i` 같은 다양한 옵션을 사용해 파일과 디렉토리를 삭제하는 방법을 배우고 안전하고 효과적인 파일 삭제를 연습하세요.
2. **[파일과 디렉토리 정리하기](https://labex.io/ko/labs/linux-organizing-files-and-directories-387877)** - 불필요한 디렉토리를 정리하는 등 필수 Linux 파일 관리 기술을 실습하는 도전 과제입니다.

## 요약

이제 모든 대상을 되돌릴 수 없는 것으로 다루면서 파일 시스템 항목을 제거할 수 있습니다.

1. 제거 전에 파일 경로를 확인할 수 있습니다.
2. 읽기 전용 명령어로 와일드카드 확장을 미리 볼 수 있습니다.
3. `-i` 또는 `-I`로 확인을 요청할 수 있습니다.
4. 디렉터리가 비어 있어야 할 때 `rmdir`를 선택할 수 있습니다.
5. 재귀 제거 전에 전체 대상을 검증할 수 있습니다.
