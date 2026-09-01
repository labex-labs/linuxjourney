---
lesson_id: "paste-command"
course_id: "text-fu"
lang: "ko"
order_index: 7
title: "paste"
description: "paste로 대응하는 줄을 병합하거나 구성 가능한 구분 기호를 사용해 줄을 직렬화하는 방법을 배웁니다."
meta_title: "paste - Text-Fu"
meta_description: "Linux paste 명령어를 사용하여 파일 줄을 병합하는 방법을 배웁니다. 이 필수 Linux 명령어 튜토리얼을 통해 구분 기호를 발견하고 파일을 결합하세요."
meta_keywords: "Linux paste 명령어, paste 명령어 튜토리얼, 파일 줄 병합, Linux 명령어, 초보자 Linux, Linux 가이드"
---

`paste` 명령어는 줄을 열 형태로 결합합니다. 기본적으로 각 입력 파일에서 한 줄씩 가져와 탭으로 연결하고 모든 입력이 파일 끝에 이를 때까지 반복합니다.

## 파일을 나란히 병합하기

작은 파일 두 개를 만듭니다.

```bash
$ printf 'alice\nbob\n' > names.txt
$ printf 'admin\nviewer\n' > roles.txt
```

두 파일을 `paste`에 전달합니다.

```bash
$ paste names.txt roles.txt
alice	admin
bob	viewer
```

열 사이에 보이는 간격은 탭입니다. 한 파일 전체를 쓴 다음 다른 파일을 쓰는 `cat`과 달리 `paste`는 서로 대응하는 입력 줄을 결합합니다.

:::single-choice{#paste-corresponding-lines} `first.txt`에는 `A`와 `B`가, `second.txt`에는 `1`과 `2`가 차례로 들어 있습니다. 기본적으로 `paste first.txt second.txt`는 무엇을 출력하나요?

::option[`A`, `B`, `1`, `2`를 연속된 네 줄에 출력합니다.]{#paste-concatenated-files explanation="파일을 차례로 쓰는 동작과 비슷합니다. `paste`는 대신 대응하는 줄을 결합합니다."}
::option[`A`, `B`, `1`, `2`를 구분 기호 없이 한 줄에 출력합니다.]{#paste-one-line-no-separator explanation="한 줄 직렬화에는 `-s`가 필요하며 기본 구분 기호는 빈 문자열이 아니라 탭입니다."}
::option[`A`와 `1`, 다음 줄에 `B`와 `2`를 탭으로 구분해 출력합니다.]{#paste-parallel-result .correct explanation="기본 병렬 모드는 각 출력 줄마다 각 파일에서 한 줄을 가져오고 필드를 탭으로 구분합니다."}
:::

## 구분 기호 선택하기

기본 탭 구분 기호를 바꾸려면 `-d LIST`를 사용합니다. 콜론을 사용하려면 다음과 같이 실행합니다.

```bash
$ paste -d ':' names.txt roles.txt
alice:admin
bob:viewer
```

쉘에서 의미가 있는 구분 기호는 따옴표로 묶으세요. 목록에 여러 문자가 있으면 `paste`는 여러 구분 기호를 순환할 수 있지만 두 열을 만들 때는 한 문자가 가장 간단합니다.

:::single-choice{#paste-colon-delimiter} `names.txt`와 `roles.txt`의 대응하는 줄을 콜론으로 연결하는 명령어는 무엇인가요?

::option[`paste -d ':' names.txt roles.txt`]{#paste-colon-files .correct explanation="`-d` 옵션은 각 필드 쌍 사이의 기본 탭을 지정한 콜론으로 바꿉니다."}
::option[`paste -s ':' names.txt roles.txt`]{#paste-serial-colon-operand explanation="`-s`는 직렬 모드를 선택하며 `:`는 구분 기호가 아니라 또 다른 입력 경로로 처리됩니다."}
::option[`paste names.txt ':' roles.txt`]{#paste-colon-file-operand explanation="`-d`가 없으면 모든 피연산자는 입력 파일로 처리되므로 이름이 `:`인 파일을 열려고 합니다."}
:::

## 한 파일의 줄을 직렬화하기

`-s` 옵션은 각 입력 파일을 직렬로 처리하여 그 줄들을 하나의 출력 줄로 연결합니다. 한 줄에 한 단어가 있는 파일을 만듭니다.

```bash
$ printf 'The\nquick\nbrown\nfox\n' > words.txt
$ paste -s words.txt
The	quick	brown	fox
```

구분 기호를 고르려면 `-s`와 `-d`를 함께 사용합니다.

```bash
$ paste -s -d ' ' words.txt
The quick brown fox
```

`-s`와 함께 여러 파일을 지정하면 각 파일은 별도의 출력 줄이 됩니다.

:::single-choice{#paste-serialize-with-spaces} `words.txt`의 모든 줄을 공백으로 구분된 하나의 출력 줄로 연결하는 명령어는 무엇인가요?

::option[`paste -d ' ' words.txt`]{#paste-parallel-one-file explanation="기본 병렬 모드에서는 입력 파일이 하나여도 입력 줄마다 출력 줄 하나가 만들어집니다. 파일 사이에서 연결할 대상이 없어 구분 기호는 쓰이지 않습니다."}
::option[`paste -s words.txt roles.txt`]{#paste-two-serial-files explanation="두 파일을 기본 탭으로 각각 직렬화하므로 요청한 한 파일의 공백 구분 결과가 아니라 출력 줄 두 개가 만들어집니다."}
::option[`paste -s -d ' ' words.txt`]{#paste-serial-spaces .correct explanation="`-s`는 파일의 줄을 직렬화하고 `-d ' '`는 줄 사이에 공백을 사용합니다."}
:::

## 길이가 다른 입력 처리하기

병렬 입력 파일의 줄 수가 다르면 `paste`는 가장 긴 파일이 끝날 때까지 계속합니다. 짧은 파일에서 빠진 값은 빈 필드가 됩니다.

```bash
$ printf 'A\nB\nC\n' > letters.txt
$ printf '1\n2\n' > numbers.txt
$ paste -d ':' letters.txt numbers.txt
A:1
B:2
C:
```

:::single-choice{#paste-unequal-files} 병렬 `paste`에 전달한 한 파일이 다른 파일보다 먼저 끝나면 어떻게 되나요?

::option[가장 긴 입력이 끝날 때까지 해당 파일에 빈 필드를 사용합니다.]{#paste-empty-fields .correct explanation="병렬 모드는 모든 파일이 소진될 때까지 계속하며 짧은 입력에서 빠진 줄을 빈 필드로 나타냅니다."}
::option[즉시 멈추고 남은 줄을 버립니다.]{#paste-stop-shortest explanation="`paste`는 가장 긴 입력까지 계속하므로 다른 파일이 끝났다는 이유로 남은 줄을 버리지 않습니다."}
::option[짧은 파일을 처음부터 반복합니다.]{#paste-repeat-shorter explanation="입력 레코드를 순환하지 않습니다. 소진된 입력은 빈 필드를 제공합니다."}
:::

## 표준 입력에서 입력 하나 읽기

파일 피연산자로 `-`를 사용하면 그 위치의 입력을 표준 입력에서 읽습니다.

```bash
$ printf 'admin\nviewer\n' | paste -d ':' names.txt -
alice:admin
bob:viewer
```

:::single-choice{#paste-stdin-operand} `producer | paste names.txt -`에서 `-` 피연산자는 무엇을 의미하나요?

::option[병합한 결과를 표준 오류에 씁니다.]{#paste-write-stderr explanation="여기서 하이픈은 입력 소스를 나타내며 출력 스트림을 리디렉션하지 않습니다."}
::option[두 열 사이의 구분 기호를 제거합니다.]{#paste-remove-delimiter explanation="구분 기호는 `-d`로 선택합니다. 하이픈은 구분 기호를 바꾸지 않습니다."}
::option[해당 입력 열을 표준 입력에서 읽습니다.]{#paste-read-stdin .correct explanation="하이픈은 `paste`에 해당 피연산자 위치에서 표준 입력을 사용하라고 지시합니다."}
:::

줄 단위 데이터 병합을 연습하려면 다음 실습을 진행해 보세요.

1. **[간단한 텍스트 처리](https://labex.io/ko/labs/linux-simple-text-processing-18004)** - `tr`, `col`, `join`, `paste` 같은 강력한 명령어로 텍스트 데이터를 효율적으로 조작하고 분석합니다.

## 요약

이제 예측 가능한 정렬과 구분 기호로 줄 단위 입력을 결합할 수 있습니다.

1. 여러 파일에서 대응하는 줄을 병합할 수 있습니다.
2. `-d`로 기본 탭 구분 기호를 바꿀 수 있습니다.
3. `-s`로 한 파일의 줄을 직렬화할 수 있습니다.
4. 짧은 입력에서 생기는 빈 필드를 해석할 수 있습니다.
5. 입력 하나가 표준 입력에서 올 때 `-`를 사용할 수 있습니다.
