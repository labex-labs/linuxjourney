---
index: 11
lang: "ko"
title: "mv (이동)"
meta_title: "mv (이동) - 명령줄"
meta_description: "파일 이동, 파일 및 디렉터리 이름 변경, 여러 파일 이동, 덮어쓰기 방지 예제를 통해 Linux mv 명령어를 배워보세요."
meta_keywords: "linux mv 명령어, mv 명령어, linux 파일 이동, linux 파일 이름 변경, linux 디렉터리 이름 변경, mv -i, mv -n, mv -t"
---

## Lesson Content

`mv` 명령어는 "move"의 약자로, 모든 Linux 환경에서 기본적인 유틸리티입니다. 주된 용도는 두 가지로, 파일이나 디렉터리의 이름을 변경하거나 다른 위치로 이동하는 것입니다.

기본 구문은 다음과 같습니다:

```bash
mv [OPTIONS] SOURCE DESTINATION
```

복사본을 만드는 `cp`와 달리, `mv`는 원본 항목이 위치하는 곳이나 이름을 변경합니다.

### 파일 및 디렉터리 이름 변경

`mv`의 가장 일반적인 용도 중 하나는 이름 변경입니다. 구문은 간단하며, 기존 이름과 새 이름을 지정하면 됩니다.

파일 이름을 변경하려면:

```bash
$ mv oldfile newfile
```

이와 같은 방식으로 디렉터리 이름도 변경할 수 있습니다:

```bash
$ mv old_directory_name new_directory_name
```

### 파일 및 디렉터리 이동

`mv` 명령어의 또 다른 핵심 기능은 항목을 한 위치에서 다른 위치로 이동하는 것입니다.

단일 파일을 다른 디렉터리로 이동하려면:

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

### mv 명령어의 중요한 옵션들

기본적으로, 같은 이름의 파일이 이미 존재하는 위치로 파일을 이동하면 `mv`는 경고 없이 덮어씁니다. 실수로 데이터가 손실되는 것을 방지하려면 다음 옵션들을 사용할 수 있습니다:

- **-i (대화형)**: 매우 중요한 안전 기능입니다. 기존 파일을 덮어쓰기 전에 확인을 요청합니다.

  ```bash
  $ mv -i source_file destination_directory
  ```

- **-b (백업)**: 파일을 덮어쓰려 하지만 이전 버전을 보존하고 싶을 때 이 옵션을 사용하면 대상 파일의 백업을 만듭니다. 백업 파일은 일반적으로 물결표(`~`) 접미사가 붙습니다.

  ```bash
  $ mv -b file1 directory_with_file1
  ```

- **-v (상세 출력)**: 이 옵션은 `mv` 명령어가 수행하는 작업을 출력하여, 이동하거나 이름을 변경하는 각 파일을 보여줍니다.

  ```bash
  $ mv -v file1 file2 somedirectory/
  ```

또 다른 유용한 옵션은 `-n`으로, 덮어쓰기를 하지 않도록 합니다.

```bash
$ mv -n source_file destination_directory
```

### 자주 쓰이는 mv 예제

파일 이름 변경:

```bash
$ mv draft.txt final.txt
```

디렉터리 이동:

```bash
$ mv project /home/pete/Documents/
```

모든 텍스트 파일을 폴더로 이동:

```bash
$ mv *.txt notes/
```

많은 파일을 이동하기 전에 `ls`로 와일드카드 매칭을 미리 확인하세요.

### 자주 묻는 질문

**mv가 파일을 복사하나요?** 아니요. `mv`는 원본 항목을 이동하거나 이름을 변경합니다.

**mv가 파일을 덮어쓸 수 있나요?** 네. 덮어쓰기 전에 묻도록 하려면 `mv -i`를, 덮어쓰지 않으려면 `mv -n`을 사용하세요.

**디렉터리를 이동할 때 mv -r이 필요한가요?** 아니요. `mv`는 `-r` 없이도 디렉터리를 이동합니다.

## Exercise

연습이 완벽을 만듭니다! `mv` 같은 Linux 명령어를 숙달하려면 직접 해보는 경험이 중요합니다. 다음 실습을 통해 실제 환경에서 파일과 디렉터리를 이동하고 이름을 변경하는 방법을 확실히 익히세요:

1. **[Linux mv 명령어: 파일 이동 및 이름 변경](https://labex.io/ko/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - `mv` 명령어를 사용해 파일과 디렉터리를 이동하고 이름을 변경하는 연습을 하며, 다양한 옵션과 동작 방식을 이해합니다.
2. **[파일 및 디렉터리 정리하기](https://labex.io/ko/labs/linux-organizing-files-and-directories-387877)** - `mv`(및 `cp`, `rm`) 명령어를 활용해 프로젝트 구조를 정리하고 파일을 이동하며 디렉터리를 정리하는 실전 과제를 수행합니다.

이 실습들은 실제 시나리오에서 개념을 적용하고 `mv` 명령어를 사용한 파일 및 디렉터리 관리에 자신감을 쌓는 데 도움이 될 것입니다.

## Quiz Question

`mv` 명령어를 사용하여 `cat`이라는 파일 이름을 `dog`으로 변경하려면 어떻게 명령어를 입력해야 할까요? 전체 명령어를 작성해 주세요. 답변은 대소문자를 구분하며 영어 소문자로 입력해야 합니다.

## Quiz Answer

mv cat dog
