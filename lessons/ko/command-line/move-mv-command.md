---
index: 11
lang: "ko"
title: "mv (이동)"
meta_title: "mv (이동) - 명령줄"
meta_description: "Linux 의 mv 명령어에 대한 종합 가이드입니다. bash mv 명령어를 사용하여 파일 및 디렉토리를 이동 및 이름 변경하는 방법, linux mv -t 와 같은 옵션 사용법, 실수로 덮어쓰는 것을 방지하는 방법을 알아보세요."
meta_keywords: "mv 명령어, linux mv 명령어, linux mv, bash mv, mv -r linux, linux mv -t, 파일 이동, 파일 이름 변경, linux 명령줄"
---

## Lesson Content

Linux 환경에서 "move"의 약자인 `mv` 명령어는 기본적인 유틸리티입니다. 이 명령어는 파일이나 디렉터리의 이름을 바꾸는 것과 다른 위치로 이동시키는 두 가지 주요 목적을 수행합니다. 그 기능은 여러 면에서 `cp` 명령어와 유사합니다.

### 파일 및 디렉터리 이름 바꾸기

`linux mv command`의 가장 일반적인 용도 중 하나는 이름 바꾸기입니다. 구문은 간단합니다. 이전 이름과 새 이름을 지정합니다.

파일 이름 바꾸기:

```bash
mv oldfile newfile
```

이와 동일한 논리가 디렉터리 이름 바꾸기에도 적용됩니다.

```bash
mv old_directory_name new_directory_name
```

### 파일 및 디렉터리 이동

`mv` 명령어의 또 다른 핵심 기능은 항목을 한 위치에서 다른 위치로 이동하는 것입니다.

단일 파일을 다른 디렉터리로 이동하려면:

```bash
mv file2 /home/pete/Documents
```

여러 파일을 한 번에 이동할 수도 있습니다. 소스 파일 목록을 모두 나열한 다음 대상 디렉터리를 지정합니다.

```bash
mv file_1 file_2 /somedirectory
```

이를 위한 유용한 옵션은 `linux mv -t`로, 대상 디렉터리를 먼저 지정할 수 있습니다. 이는 많은 파일을 이동할 때 더 명확할 수 있습니다.

```bash
mv -t /somedirectory file_1 file_2
```

`cp` 명령어와 달리 디렉터리를 이동하기 위해 `-r` 플래그가 필요하지 않습니다. `bash mv` 명령어는 기본적으로 디렉터리를 처리합니다. 일부 사용자는 `mv -r linux`를 검색하지만, 이 옵션은 `mv`로 디렉터리를 이동하는 데 필요하지 않습니다.

### mv 명령어의 중요 옵션

기본적으로 파일을 같은 이름의 파일이 이미 존재하는 대상으로 이동하면 `mv`는 경고 없이 덮어씁니다. 실수로 인한 데이터 손실을 방지하기 위해 다음 옵션을 사용할 수 있습니다.

- **-i (대화형)**: 이것은 중요한 안전 기능입니다. 기존 파일을 덮어쓰기 전에 확인 메시지를 표시합니다.

  ```bash
  mv -i source_file destination_directory
  ```

- **-b (백업)**: 파일을 덮어쓰려고 하지만 이전 버전을 보관하고 싶은 경우, 이 옵션은 대상 파일의 백업을 생성합니다. 백업은 일반적으로 물결표 (`~`) 접미사로 이름이 바뀝니다.

  ```bash
  mv -b file1 directory_with_file1
  ```

- **-v (자세히)**: 이 옵션은 `mv` 명령어가 수행하는 작업을 출력하여 이동하거나 이름을 바꾸는 각 파일을 보여줍니다.

  ```bash
  mv -v file1 file2 /somedirectory
  ```

`mv command`를 마스터하는 것은 명령줄에서 효율적인 파일 관리를 위해 필수적입니다.

## Exercise

연습이 완벽하게 만듭니다! `mv`와 같은 Linux 명령어를 마스터하는 데는 실습 경험이 중요합니다. 이 실습들은 실제 환경에서 파일 및 디렉터리를 이동하고 이름을 바꾸는 `mv` 명령어에 대한 이해를 확고히 하는 데 도움이 될 것입니다.

1.  **[Linux mv 명령어: 파일 이동 및 이름 바꾸기](https://labex.io/ko/labs/linux-linux-mv-command-file-moving-and-renaming-209743)** - `mv` 명령어를 사용하여 파일 및 디렉터리의 이름을 바꾸고 이동하는 방법, 다양한 옵션 및 동작 이해에 대해 연습합니다.
2.  **[파일 및 디렉터리 정리](https://labex.io/ko/labs/linux-organizing-files-and-directories-387877)** - `mv`(및 `cp`, `rm`) 지식을 실제 과제에 적용하여 프로젝트 구조를 정리하고, 파일을 이동하고, 디렉터리를 정리합니다.

이 실습들은 실제 시나리오에서 개념을 적용하고 `mv` 명령어를 사용한 파일 및 디렉터리 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`mv` 명령어를 사용하여 `cat`이라는 파일을 `dog`로 이름을 바꾸려면 어떻게 해야 합니까? 전체 명령어를 제공해 주십시오. 참고: 답변은 대소문자를 구분하며 소문자 영어로 입력해야 합니다.

## Quiz Answer

mv cat dog
