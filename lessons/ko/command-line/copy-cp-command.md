---
lesson_id: "copy-cp-command"
course_id: "command-line"
lang: "ko"
order_index: 10
title: "cp (복사)"
description: "덮어쓰기와 속성 보존 방식을 제어하면서 파일과 디렉터리 트리를 복사하는 방법을 배웁니다."
meta_title: "cp (복사) - 명령어 라인"
meta_description: "파일, 디렉터리, 다중 파일, 와일드카드, 백업 및 cp -r, cp -i, cp -p 같은 옵션을 사용한 Linux cp 명령어 예제를 배워보세요."
meta_keywords: "linux cp 명령어, cp 명령어, 파일 복사 linux, cp -r, cp -i, cp -p, cp -a, cp -u, 재귀 복사, linux 와일드카드"
---

`cp` 명령어는 Linux에서 파일과 디렉터리를 복사하는 표준 도구입니다. 원본 파일을 그대로 두고 새 복사본을 만듭니다. 기본 구문은 다음과 같습니다:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

한 개의 파일을 다른 파일로, 하나 이상의 파일을 디렉터리로, 또는 적절한 옵션을 사용해 전체 디렉터리 트리를 복사할 수 있습니다.

## 파일 하나 복사하기

파일을 복사하려면 원본 파일과 대상 디렉터리 또는 경로를 지정합니다.

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

이 예제에서 `mycoolfile`은 원본 파일이고, `/home/pete/Documents/cooldocs`는 대상 디렉터리입니다. 또한 파일을 복사하면서 대상 위치에서 새 이름을 지정할 수도 있습니다.

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

대상이 기존 디렉터리라면 복사된 파일은 원래 이름을 유지합니다. 대상이 파일 이름이라면 `cp`는 그 새 이름으로 복사본을 만듭니다.

:::single-choice{#copy-file-under-new-name}
`draft.txt`를 유지하면서 `final.txt`라는 이름의 파일로 복사하는 명령어는 무엇인가요?

::option[`mv draft.txt final.txt`]{#move-draft explanation="`mv`는 원래 경로 이름을 바꾸거나 이동하므로 원본을 그대로 남기지 않습니다."}
::option[`cp final.txt draft.txt`]{#copy-reversed explanation="원본과 목적지가 뒤바뀌어 `final.txt`에서 `draft.txt`로 복사합니다."}
::option[`cp draft.txt final.txt`]{#copy-draft .correct explanation="`cp`는 `draft.txt`를 읽어 `final.txt`를 만들거나 교체하며 원본은 계속 남겨 둡니다."}
:::

## 여러 파일을 디렉터리에 복사하기

여러 파일을 같은 디렉터리에 복사하려면 모든 원본 파일을 먼저 나열하고 마지막에 대상 디렉터리를 적습니다.

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

원본이 두 개 이상일 때 마지막 인수는 반드시 디렉터리여야 합니다.

:::single-choice{#copy-multiple-files}
`a.txt`와 `b.txt`를 기존 `archive/` 디렉터리에 복사하는 명령어는 무엇인가요?

::option[`cp archive/ a.txt b.txt`]{#destination-first explanation="이 형태에서는 목적지 디렉터리가 끝에 와야 하며, 먼저 두면 피연산자 해석이 달라집니다."}
::option[`cp a.txt b.txt archive/`]{#destination-last .correct explanation="원본이 여러 개일 때 마지막의 기존 디렉터리가 앞선 모든 파일의 목적지가 됩니다."}
::option[`cp a.txt archive/ b.txt`]{#destination-middle explanation="모든 원본은 목적지 앞에 와야 하므로 기존 디렉터리는 마지막 피연산자여야 합니다."}
:::

## 와일드카드로 파일 선택하기

와일드카드는 패턴에 따라 여러 파일을 선택하는 데 도움을 주는 특수 문자로, 매우 유용합니다.

- `*`: 임의의 문자 시퀀스와 일치합니다.
- `?`: 임의의 한 문자와 일치합니다.
- `[]`: 대괄호 안의 문자 중 하나와 일치합니다.

예를 들어, 현재 위치에서 모든 JPEG 이미지를 `Pictures` 디렉터리로 복사하려면:

```bash
$ cp *.jpg /home/pete/Pictures
```

중요한 데이터가 있는 목적지에 대량 복사하기 전에는 일치 항목을 미리 확인합니다.

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

:::single-choice{#preview-copy-pattern}
`*.jpg`를 복사하기 전에 현재 패턴과 일치하는 숨김 항목 이외의 이름을 보여 주는 명령어는 무엇인가요?

::option[`cp *.jpg`]{#copy-no-destination explanation="여러 이름이 일치하면 명확한 목적지 없이 복사를 시도하므로 미리보기 작업이 아닙니다."}
::option[`ls *.jpg`]{#list-jpg-matches .correct explanation="쉘이 `ls`에도 같은 패턴을 확장하므로 복사 전에 일치하는 이름을 확인할 수 있습니다."}
::option[`file '*.jpg'`]{#quoted-jpg-pattern explanation="따옴표가 와일드카드 확장을 막아 `file`에 문자 그대로 `*.jpg`가 전달됩니다."}
:::

## 디렉터리 트리 복사하기

옵션 없이 `cp`로 디렉터리를 복사하려 하면 오류가 발생합니다. 디렉터리와 그 안의 모든 내용을 포함해 복사하려면 `-r` (재귀) 플래그를 사용해야 합니다.

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

이 명령은 `Pumpkin` 디렉터리와 그 안의 모든 내용을 `Documents` 디렉터리로 복사합니다.

일반 Linux 시스템에서는 `-R`도 같은 재귀 목적을 가집니다:

```bash
$ cp -R website /home/pete/backups/
```

백업 방식 복사에는 아카이브 모드인 `-a`가 유용합니다. 링크와 여러 파일 속성을 보존하면서 재귀적으로 복사합니다.

```bash
$ cp -a project/ project-backup/
```

:::single-choice{#archive-directory-tree}
링크와 여러 속성을 보존하면서 `project/`를 백업 방식으로 재귀 복사하려면 어떤 명령어가 적합한가요?

::option[`cp -p project/ project-backup/`]{#preserve-directory-only explanation="`-p`는 선택한 속성을 보존하지만 그 자체로 디렉터리 복사를 재귀적으로 만들지는 않습니다."}
::option[`cp -u project/ project-backup/`]{#update-directory-only explanation="`-u`는 목적지 상태에 따라 복사 시점을 제어하지만 재귀 복사를 활성화하지 않습니다."}
::option[`cp -a project/ project-backup/`]{#archive-project .correct explanation="아카이브 모드는 재귀 복사를 포함하고 링크와 폭넓은 속성을 보존합니다."}
:::

## 덮어쓰기 제어하기

기본적으로 `cp`는 대상에 같은 이름의 파일이 있으면 덮어씁니다. 실수로 데이터 손실을 막으려면 `-i` (대화형) 플래그를 사용해 덮어쓰기 전에 확인을 요청할 수 있습니다.

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

기존 대상 파일을 덮어쓰지 않으려면 `-n`을 사용합니다.

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

`-f`는 기존 목적지를 쓰기용으로 열 수 없을 때 삭제한 뒤 복사를 다시 시도하게 합니다. 대상을 신중히 확인하는 일을 대신하지 않으며, 쉘 별칭이 `-i` 같은 옵션을 추가할 수도 있습니다.

:::single-choice{#skip-existing-destination}
`report.txt`를 `backup/`에 복사하되 같은 이름의 목적지가 이미 있으면 건너뛰는 명령어는 무엇인가요?

::option[`cp -n report.txt backup/`]{#no-clobber-report .correct explanation="`-n`은 `cp`가 기존 목적지 파일을 덮어쓰지 않게 합니다."}
::option[`cp -i report.txt backup/`]{#interactive-report explanation="`-i`는 덮어쓰기 전에 묻기 때문에 결과가 응답에 달려 있습니다."}
::option[`cp -f report.txt backup/`]{#force-report explanation="`-f`는 목적지 교체를 시도하며 덮어쓰기 금지 동작을 제공하지 않습니다."}
:::

## 파일 보존 또는 새로 고치기

원본 파일의 모드와 허용되는 소유권, 타임스탬프를 보존하려면 `-p`를 사용합니다.

```bash
$ cp -p mycoolfile /home/pete/backups/
```

`-u` 옵션은 원본 파일이 대상 파일보다 새롭거나 대상 파일이 없을 때만 복사합니다.

```bash
$ cp -u *.txt /home/pete/Documents/
```

그 밖에 자주 쓰는 옵션은 다음과 같습니다.

- `-f`: 필요 시 먼저 대상을 삭제하여 강제로 덮어씁니다.
- `-v`: 복사 중인 각 파일을 보여줍니다.

파일과 디렉터리 트리 복사를 연습하려면 다음 실습을 활용해 보세요.

1. **[Linux cp 명령어: 파일 복사](https://labex.io/ko/labs/linux-linux-cp-command-file-copying-209744)** - 기본 사용법, 재귀 복사, 속성 보존, 와일드카드 사용 등 고급 옵션을 연습하며 파일과 디렉터리를 효율적으로 복사하는 방법을 익히세요.
2. **[파일과 디렉터리 정리하기](https://labex.io/ko/labs/linux-organizing-files-and-directories-387877)** - `cp`, `mv`, `rm` 명령어를 사용해 프로젝트 구조를 정리하고 파일을 이동하며 불필요한 디렉터리를 정리하는 필수 Linux 파일 관리 기술을 연습하세요.

## 요약

이제 목적지 처리 방식을 제어하면서 파일과 디렉터리 트리를 복사할 수 있습니다.

1. 원본 피연산자를 목적지 앞에 배치할 수 있습니다.
2. 대량 복사 전에 와일드카드 일치 항목을 미리 볼 수 있습니다.
3. 디렉터리 트리를 재귀 또는 아카이브 모드로 복사할 수 있습니다.
4. 기존 목적지를 확인하거나 건너뛰거나 의도적으로 교체할 수 있습니다.
5. 필요할 때 속성을 보존하거나 더 새로운 원본만 복사할 수 있습니다.
