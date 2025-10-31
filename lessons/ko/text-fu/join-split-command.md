---
index: 11
lang: "ko"
title: "결합 및 분할"
meta_title: "결합 및 분할 - Text-Fu"
meta_description: "Linux 의 join 및 split 명령 사용법을 마스터하세요. 공통 필드를 기반으로 파일을 효율적으로 결합하고 큰 파일을 더 작은 부분으로 분할하는 방법을 배웁니다. 이 가이드는 cat, dog, cow 와 같은 파일 결합에 사용할 명령과 기타 실용적인 예를 다룹니다."
meta_keywords: "리눅스 파일 결합, 파일 결합에 사용할 명령, 리눅스 join 명령어, 리눅스 split 명령어, 파일 조작, 명령줄, 텍스트 처리"
---

## Lesson Content

Linux 에서 텍스트 파일을 관리하고 조작하는 것은 일반적인 작업입니다. 이를 위한 두 가지 강력한 유틸리티는 `join`과 `split`입니다. `join` 명령어는 공통 필드를 기반으로 두 파일의 줄을 병합하고, `split`은 큰 파일을 더 작고 관리하기 쉬운 조각으로 나눕니다.

### 공통 필드를 기준으로 파일 결합하기

`join` 명령어는 **linux join files**를 수행해야 할 때 기본적인 도구입니다. 기본적으로 이 명령어는 정렬된 두 파일의 줄을 동일한 첫 번째 필드를 기준으로 결합합니다.

예를 들어, 병합하려는 두 개의 파일이 있다고 가정해 보겠습니다.

```plaintext
file1.txt
1 John
2 Jane
3 Mary

file2.txt
1 Doe
2 Doe
3 Sue
```

`join` 명령어를 사용하면 다음과 같이 쉽게 결합할 수 있습니다.

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

보시다시피, 파일들은 공통된 첫 번째 필드 (1, 2, 3) 를 사용하여 결합되었습니다. `join`이 올바르게 작동하려면 두 파일의 조인 필드가 정렬되어 있어야 합니다.

### 다른 조인 필드 지정하기

공통 필드가 첫 번째 열이 아니라면 어떻게 해야 할까요? `join`에게 사용할 필드를 알려줄 수 있습니다. 다음 파일들을 고려해 보세요.

```plaintext
file1.txt
John 1
Jane 2
Mary 3

file2.txt
1 Doe
2 Doe
3 Sue
```

여기서는 `file1.txt`의 두 번째 필드와 `file2.txt`의 첫 번째 필드를 기준으로 조인해야 합니다. 명령어는 다음과 같습니다.

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1 2` 플래그는 첫 번째 파일의 두 번째 필드를 지정하고, `-2 1` 플래그는 두 번째 파일의 첫 번째 필드를 지정합니다.

### 대용량 파일 분할하기

`split` 명령어는 결합의 반대 작업을 수행합니다. 즉, 큰 파일을 더 작은 파일로 나눕니다.

```bash
$ split somefile
```

기본적으로 이 명령어는 1000 줄 제한에 도달하면 `somefile`을 `xaa`, `xab` 등으로 이름 붙여진 새 파일로 분할합니다. `-l` 플래그를 사용하여 다른 줄 수를 지정하거나 `-b` 플래그를 사용하여 파일 크기별로 분할하는 등 이 동작을 사용자 지정할 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! 텍스트 파일 결합 및 조작에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux join 명령어: 파일 결합](https://labex.io/ko/labs/linux-linux-join-command-file-joining-219193)** - 이 랩은 `join` 명령어에 대한 직접적인 실습 소개를 제공하여, 레슨에서 논의된 것처럼 공통 필드를 기반으로 두 개의 정렬된 텍스트 파일에서 줄을 병합하는 연습을 할 수 있게 합니다.
2. **[직원 데이터 처리](https://labex.io/ko/labs/linux-processing-employees-data-388132)** - `join` 및 `awk`와 같은 강력한 Linux 명령줄 유틸리티에 대한 지식을 적용하여 여러 소스의 데이터를 결합하고 처리함으로써 실제 데이터 분석 시나리오를 시뮬레이션합니다.
3. **[시퀀스 제어 및 파이프라인](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령 실행 시퀀스를 제어하고, 파이프라인을 활용하며, 강력한 텍스트 처리 도구를 활용하는 방법을 학습하여 명령줄 효율성과 데이터 조작 기술을 향상시키세요. 이는 `join`의 데이터 결합 기능과 상호 보완적입니다.

이러한 랩들은 텍스트 파일 조작 및 데이터 결합 개념을 실제 시나리오에 적용하고 Linux 명령줄 도구에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

cat, dog, cow 라는 이름의 파일을 결합하려면 어떤 명령어를 사용해야 합니까? 전체 명령어를 영어로 제공해 주세요. 명령어와 파일 이름은 모두 소문자여야 합니다.

## Quiz Answer

join cat dog cow
