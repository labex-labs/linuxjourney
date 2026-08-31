---
lesson_id: "cat-command"
course_id: "command-line"
lang: "ko"
order_index: 7
title: "cat"
description: "cat 명령어로 파일 내용을 안전하게 표시하고 연결하며 리디렉션하는 방법을 배웁니다."
meta_title: "cat - 명령어 라인"
meta_description: "파일 보기, 파일 연결, 줄 번호 매기기, 파일 생성 및 안전한 리디렉션 사용 예제로 배우는 Linux cat 명령어."
meta_keywords: "리눅스 cat 명령어, cat 명령어, 리눅스 파일 보기, 파일 연결, cat -n, cat -b, cat 리디렉션, 리눅스 cat"
---

파일을 식별하는 방법을 배웠으니 이제 내용을 읽어 봅시다. `cat` 명령어는 파일을 표시하고 내용을 이어 붙이며, 이름은 "concatenate"의 줄임말입니다.

## 파일 내용 보기

`cat` 명령어의 가장 기본적인 용도는 단일 파일의 내용을 터미널에 직접 출력하는 것입니다.

```bash
$ cat myfile.txt
```

이 명령어는 파일 전체를 표준 출력으로 보냅니다. 짧은 텍스트에는 적합하지만 긴 파일은 너무 빨리 지나갈 수 있습니다.

:::single-choice{#display-short-file}
`myfile.txt` 전체를 터미널에 표시하는 명령어는 무엇인가요?

::option[`file myfile.txt`]{#classify-myfile explanation="`file`은 예상 파일 유형을 알려 줄 뿐 파일에 저장된 전체 텍스트를 출력하지 않습니다."}
::option[`touch myfile.txt`]{#update-myfile explanation="`touch`는 타임스탬프를 갱신하거나 없는 파일을 만들며 파일 내용을 표시하지 않습니다."}
::option[`cat myfile.txt`]{#display-myfile .correct explanation="`cat`은 `myfile.txt`를 읽어 표준 출력으로 보내며, 여기서는 터미널에 표시됩니다."}
:::

## 파일 연결하기

이름 그대로 `cat`은 여러 파일을 연결(concatenate)하여 결합된 출력을 보여줄 수 있습니다. 지정한 순서대로 파일을 읽고 순차적으로 출력합니다.

```bash
$ cat dogfile birdfile
```

이 명령어는 먼저 `dogfile`의 내용을 출력하고 바로 이어서 `birdfile`의 내용을 출력합니다. 결합된 출력을 새 파일에 저장하려면 `>`로 표준 출력을 리디렉션합니다.

```bash
$ cat dogfile birdfile > animals
```

쉘은 `cat`을 실행하기 전에 `animals`를 만들거나 비운 뒤 결합된 출력을 그곳으로 보냅니다. 입력 파일 중 하나를 목적지로 사용하면 `cat`이 읽기 전에 파일이 비워질 수 있으므로 피해야 합니다.

:::single-choice{#combine-files-in-order}
`part1` 다음에 `part2`가 오도록 결합해 새로 만들거나 교체한 `whole`에 쓰는 명령어는 무엇인가요?

::option[`cat whole > part1 part2`]{#reverse-redirection explanation="리디렉션 목적지는 하나뿐이고 다른 단어는 `cat`의 피연산자가 됩니다. 요청한 입출력 순서를 나타내지 않습니다."}
::option[`cat part1 part2 > whole`]{#ordered-inputs .correct explanation="`cat`이 두 파일을 적힌 순서대로 출력하고 `>`가 그 결합된 출력을 `whole`로 보냅니다."}
::option[`cat part2 part1 > whole`]{#reverse-inputs explanation="같은 두 입력을 쓰지만 `part1`보다 `part2`를 먼저 읽습니다. 피연산자 순서가 출력 순서를 결정합니다."}
:::

## 터미널 입력을 파일로 읽기

`cat`을 출력 리디렉션 연산자(`>`)와 함께 사용하여 새 파일을 만들 수도 있습니다. 터미널에서 직접 텍스트를 파일에 빠르게 쓸 수 있는 방법입니다.

```bash
$ cat > newfile.txt
```

이 명령어를 실행한 후 텍스트를 입력할 수 있습니다. 새 줄에서 `Ctrl+D`를 눌러 저장하고 종료하세요. 이렇게 하면 입력한 텍스트로 `newfile.txt`가 생성됩니다. 기존 파일에 `>`를 사용하면 완전히 덮어쓰므로 주의하세요.

덮어쓰지 않고 파일에 덧붙이려면 `>>`를 사용하세요.

```bash
$ cat >> notes.txt
```

:::single-choice{#append-terminal-input}
기존 `notes.txt`의 끝에 텍스트를 더 입력하려 합니다. 파일을 비우지 않고 작업을 시작하는 명령어는 무엇인가요?

::option[`cat > notes.txt`]{#overwrite-notes explanation="`>` 하나는 목적지를 먼저 비운 뒤 입력을 리디렉션하므로 기존 텍스트가 사라집니다."}
::option[`cat >> notes.txt`]{#append-notes .correct explanation="`>>`는 목적지를 추가 모드로 열어 `cat`이 읽은 텍스트를 기존 내용 뒤에 붙입니다."}
::option[`cat notes.txt > notes.txt`]{#same-input-output explanation="같은 파일을 입력과 `>` 목적지로 쓰면 `cat`이 읽기 전에 파일이 비워질 수 있어 안전한 추가 방식이 아닙니다."}
:::

## 출력 형식 조정하기

`cat` 명령어에는 동작을 변경하는 여러 옵션이 있습니다.

- `-n`: 모든 출력 줄에 1부터 번호를 매깁니다.
- `-b`: 빈 줄을 제외한 출력 줄에만 번호를 매깁니다.
- `-s`: 여러 개의 빈 줄을 하나의 빈 줄로 압축합니다.
- `-A`: 출력하지 않는 문자, 탭, 줄 끝 문자를 표시합니다.

예시:

```bash
$ cat -n script.sh
$ cat -b notes.txt
$ cat -s messy.txt
```

:::single-choice{#number-nonempty-lines}
`notes.txt`에서 비어 있지 않은 출력 줄에만 번호를 매기는 명령어는 무엇인가요?

::option[`cat -b notes.txt`]{#number-nonblank .correct explanation="`-b`는 비어 있지 않은 출력 줄에 번호를 매기고 빈 줄에는 번호를 붙이지 않습니다."}
::option[`cat -n notes.txt`]{#number-all-lines explanation="`-n`은 빈 줄을 포함한 모든 출력 줄에 번호를 매기므로 조건에 맞지 않습니다."}
::option[`cat -s notes.txt`]{#squeeze-blank-lines explanation="`-s`는 연속된 빈 줄을 하나로 줄일 뿐 줄 번호를 추가하지 않습니다."}
:::

## 긴 파일에 적합한 뷰어 선택하기

짧은 파일에는 `cat`을 사용하세요. 긴 파일은 `less`를 사용해 스크롤, 검색, 종료가 가능하며 터미널이 넘치지 않습니다.

```bash
$ less /var/log/syslog
```

:::single-choice{#choose-viewer-for-long-file}
긴 로그 파일을 대화형으로 읽기에 더 적합한 명령어는 무엇인가요?

::option[`less /var/log/syslog`]{#page-through-log .correct explanation="`less`는 스크롤과 검색, 제어된 종료를 제공하므로 긴 파일을 대화형으로 읽기에 알맞습니다."}
::option[`cat /var/log/syslog`]{#print-entire-log explanation="`cat`은 로그 전체를 한꺼번에 터미널에 써서 살펴보기 전에 긴 내용이 지나갈 수 있습니다."}
::option[`touch /var/log/syslog`]{#update-log-time explanation="`touch`는 타임스탬프를 바꾸며 권한이 필요할 수 있습니다. 로그를 읽는 명령어가 아닙니다."}
:::

파일 내용을 표시하고 결합하는 방법을 연습하려면 다음 실습을 활용해 보세요.

1. **[Linux cat 명령어: 파일 연결하기](https://labex.io/ko/labs/linux-linux-cat-command-file-concatenating-210986)** - `cat` 명령어로 텍스트 파일을 보고, 연결하고, 조작하는 방법을 배우며 명령어 라인에서 효율적인 텍스트 파일 처리를 익히세요.
2. **[Linux에서 로그 및 설정 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - `cat` 같은 명령어를 사용해 시스템 로그와 설정 파일을 효율적으로 보고 탐색하며 중요한 정보를 추출하는 연습을 하세요.

## 요약

이제 안전한 리디렉션을 선택하면서 `cat`으로 파일 내용을 표시하고 결합할 수 있습니다.

1. 짧은 파일의 전체 내용을 표시할 수 있습니다.
2. 원하는 순서로 파일을 연결할 수 있습니다.
3. 목적지를 의도적으로 교체하거나 내용을 추가할 수 있습니다.
4. 출력 줄에 번호를 매기거나 단순화할 수 있습니다.
5. 대화형 읽기에 더 적합할 때 `less`를 선택할 수 있습니다.
