---
lesson_id: "move-mv-command"
course_id: "command-line"
lang: "ko"
order_index: 11
title: "mv (이동)"
description: "의도하지 않은 덮어쓰기를 피하면서 파일과 디렉터리의 이름을 바꾸거나 이동하는 방법을 배웁니다."
meta_title: "mv (이동) - 명령줄"
meta_description: "파일 이동, 파일 및 디렉터리 이름 변경, 여러 파일 이동, 덮어쓰기 방지 예제를 통해 Linux mv 명령어를 배워보세요."
meta_keywords: "linux mv 명령어, mv 명령어, linux 파일 이동, linux 파일 이름 변경, linux 디렉터리 이름 변경, mv -i, mv -n, mv -t"
---

`mv` 명령어는 파일이나 디렉터리 이름을 바꾸거나 다른 위치로 이동합니다. `cp`와 달리 성공적으로 이동한 뒤 원래 경로 이름을 남겨 두지 않습니다.

기본 구문은 다음과 같습니다:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

## 파일 및 디렉터리 이름 바꾸기

`mv`의 가장 일반적인 용도 중 하나는 이름 변경입니다. 구문은 간단하며, 기존 이름과 새 이름을 지정하면 됩니다.

파일 이름을 변경하려면:

```bash
$ mv oldfile newfile
```

이와 같은 방식으로 디렉터리 이름도 변경할 수 있습니다:

```bash
$ mv old_directory_name new_directory_name
```

:::single-choice{#rename-file-with-mv} 현재 디렉터리에서 `cat`을 `dog`으로 이름 바꾸는 명령어는 무엇인가요?

::option[`mv cat dog`]{#rename-cat .correct explanation="`mv`는 `cat`을 원본 경로로, `dog`을 새 목적지 경로로 처리합니다."}
::option[`mv dog cat`]{#rename-dog explanation="피연산자 순서가 반대이므로 기존 `dog`을 `cat`으로 바꾸려고 시도합니다."}
::option[`cp cat dog`]{#copy-cat explanation="`cp`는 `cat`을 유지하면서 `dog`이라는 복사본을 만들므로 요청한 이름 변경이 아닙니다."}
:::

## 항목을 디렉터리로 이동하기

마지막 피연산자가 기존 디렉터리이면 `mv`는 원본을 그 안으로 이동합니다.

```bash
$ mv file2 /home/pete/Documents
```

여러 파일을 한 번에 이동할 수도 있습니다. 모든 원본 파일을 나열한 다음 대상 디렉터리를 지정하면 됩니다:

```bash
$ mv file_1 file_2 somedirectory/
```

GNU/Linux 시스템에서는 `-t` 옵션이 유용한데, 이 옵션은 대상 디렉터리를 먼저 지정할 수 있게 해줍니다. 많은 파일을 이동할 때 더 명확할 수 있습니다.

```bash
$ mv -t somedirectory/ file_1 file_2
```

`cp` 명령어와 달리, 디렉터리를 이동할 때 재귀 옵션이 필요하지 않습니다. `mv`는 기본적으로 디렉터리를 처리합니다.

:::single-choice{#move-multiple-files} `file_1`과 `file_2`를 기존 `archive/` 디렉터리로 모두 이동하는 명령어는 무엇인가요?

::option[`mv archive/ file_1 file_2`]{#target-first-without-option explanation="GNU `-t`가 없으면 여러 원본을 이동할 때 대상 디렉터리는 마지막에 와야 합니다."}
::option[`mv -r file_1 file_2 archive/`]{#recursive-move explanation="`mv`는 파일이나 디렉터리를 옮길 때 `-r`을 사용하지 않습니다. 일반 다중 원본 형식으로 충분합니다."}
::option[`mv file_1 file_2 archive/`]{#target-last .correct explanation="원본이 여러 개면 기존 대상 디렉터리를 마지막 피연산자로 두어 두 파일을 모두 받게 합니다."}
:::

## 기존 목적지 제어하기

기본적으로 `mv`는 기존 목적지를 교체할 수 있습니다. 이동 전에 원본과 목적지 경로를 조사하고 필요에 따라 덮어쓰기 정책을 선택합니다.

- `-i`: 기존 목적지를 교체하기 전에 확인을 요청합니다.

  ```bash
  $ mv -i source_file destination_directory
  ```

- `-n`: 기존 목적지를 덮어쓰지 않습니다.

  ```bash
  $ mv -n source_file destination_directory
  ```

- `-b`: GNU/Linux에서 교체될 목적지의 백업을 만듭니다. 기본 백업 접미사는 일반적으로 `~`입니다.

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- `-v`: 각 이동 작업을 출력합니다.

```bash
$ mv -v file1 file2 somedirectory/
```

:::single-choice{#move-without-overwriting} 기존 목적지를 덮어쓰지 않을 때만 `draft.txt`를 `finished/`로 이동하는 명령어는 무엇인가요?

::option[`mv -i draft.txt finished/`]{#interactive-draft explanation="`-i`는 목적지가 있을 때 물어보며 사용자가 승인하면 덮어쓸 수도 있습니다."}
::option[`mv -b draft.txt finished/`]{#backup-draft explanation="`-b`는 기존 목적지를 백업하면서 교체를 허용하므로 덮어쓰기를 막지 않습니다."}
::option[`mv -n draft.txt finished/`]{#no-clobber-draft .correct explanation="`-n`은 기존 목적지를 덮어쓰게 되는 이동을 건너뜁니다."}
:::

## 디렉터리와 와일드카드 일치 항목 이동하기

디렉터리는 `-r` 없이 이동할 수 있습니다.

```bash
$ mv project /home/pete/Documents/
```

셸 와일드카드로 여러 원본을 선택할 수 있습니다.

```bash
$ ls *.txt
$ mv *.txt notes/
```

`ls`로 일치 항목을 미리 보면 여러 경로를 변경하기 전에 지나치게 넓은 패턴을 찾을 수 있습니다.

:::single-choice{#move-directory-without-recursion} `project/` 디렉터리를 `/srv/archive/` 안으로 이동하는 명령어는 무엇인가요?

::option[`mv -r project/ /srv/archive/`]{#recursive-project explanation="`mv`는 이 작업에 `-r`이 필요하지도 이를 지원하지도 않습니다. 일반 이동으로 디렉터리를 처리합니다."}
::option[`mv project/ /srv/archive/`]{#move-project .correct explanation="일반 `mv` 구문은 재귀 플래그 없이 디렉터리를 기존 대상 디렉터리로 이동합니다."}
::option[`cp project/ /srv/archive/`]{#copy-project explanation="일반 `cp`는 디렉터리를 이동하지 않고 복사에도 재귀 옵션이 필요하며 원본도 남습니다."}
:::

:::single-choice{#preview-text-file-move} `mv *.txt notes/`를 실행할 예정입니다. 같은 와일드카드가 선택할 경로를 미리 보여 주는 명령어는 무엇인가요?

::option[`ls '*.txt'`]{#literal-text-pattern explanation="따옴표가 `*` 확장을 막아 이동 대상을 미리 보는 대신 별표가 들어간 문자 그대로의 이름을 찾습니다."}
::option[`ls *.txt`]{#list-text-matches .correct explanation="쉘이 `mv`에서와 마찬가지로 `ls`의 `*.txt`를 확장하므로 숨김 항목 이외의 선택된 이름을 먼저 확인할 수 있습니다."}
::option[`mv -v *.txt notes/`]{#verbose-text-move explanation="상세 모드는 이동하는 동안 작업을 보고하며 읽기 전용 미리보기 대신 실제 이동을 수행합니다."}
:::

항목 이동과 이름 바꾸기를 연습하려면 다음 실습을 활용해 보세요.

1. **[Linux mv 명령어: 파일 이동 및 이름 변경](https://labex.io/ko/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - `mv` 명령어를 사용해 파일과 디렉터리를 이동하고 이름을 변경하는 연습을 하며, 다양한 옵션과 동작 방식을 이해합니다.
2. **[파일 및 디렉터리 정리하기](https://labex.io/ko/labs/linux-organizing-files-and-directories-387877)** - `mv`(및 `cp`, `rm`) 명령어를 활용해 프로젝트 구조를 정리하고 파일을 이동하며 디렉터리를 정리하는 실전 과제를 수행합니다.

## 요약

이제 기존 목적지를 보호하면서 파일이나 디렉터리의 이름을 바꾸고 이동할 수 있습니다.

1. 원본을 새 경로 이름 앞에 배치할 수 있습니다.
2. 여러 원본 뒤에 대상 디렉터리를 둘 수 있습니다.
3. 목적지를 교체하기 전에 묻거나 건너뛰거나 백업할 수 있습니다.
4. 재귀 옵션 없이 디렉터리를 이동할 수 있습니다.
5. 대량 이동 전에 와일드카드 일치 항목을 미리 볼 수 있습니다.
