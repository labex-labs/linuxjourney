---
index: 11
lang: "ko"
title: "join 및 split"
meta_title: "join 및 split - Text-Fu"
meta_description: "Linux 의 'join' 및 'split' 명령을 사용하여 파일을 조작하는 방법을 배우세요. 공통 필드를 기준으로 파일을 결합하고 큰 파일을 효율적으로 분할하는 방법을 이해하세요. 실용적인 예제와 팁을 얻으세요."
meta_keywords: "Linux join 명령, Linux split 명령, 파일 조작, Linux 튜토리얼, 명령줄, 초보자 Linux, Linux 가이드"
---

## Lesson Content

`join` 명령을 사용하면 공통 필드를 기준으로 여러 파일을 함께 조인할 수 있습니다:

두 개의 파일을 함께 조인하고 싶다고 가정해 봅시다:

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

```bash
$ join file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

파일이 어떻게 조인되었는지 보이시나요? 기본적으로 첫 번째 필드를 기준으로 조인되며, 필드는 동일해야 합니다. 동일하지 않으면 정렬할 수 있습니다. 이 경우 파일은 1, 2, 3 을 통해 조인됩니다.

다음 파일들을 어떻게 조인할까요?

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

이 파일을 조인하려면 조인할 필드를 지정해야 합니다. 이 경우 `file1.txt`의 필드 2 와 `file2.txt`의 필드 1 을 원하므로 명령은 다음과 같습니다:

```bash
$ join -1 2 -2 1 file1.txt file2.txt
1 John Doe
2 Jane Doe
3 Mary Sue
```

`-1`은 `file1.txt`를, `-2`는 `file2.txt`를 나타냅니다. 꽤 멋지죠. `split` 명령으로 파일을 여러 파일로 분할할 수도 있습니다:

```bash
split somefile
```

이렇게 하면 파일이 여러 파일로 분할됩니다. 기본적으로 1000 줄 제한에 도달하면 분할됩니다. 파일 이름은 기본적으로 `x**`입니다.

## Exercise

연습은 완벽을 만듭니다! 다음은 텍스트 파일을 조인하고 조작하는 이해를 강화하기 위한 실습입니다:

1. **[Linux join Command: File Joining](https://labex.io/ko/labs/linux-linux-join-command-file-joining-219193)** - 이 실습은 `join` 명령에 대한 직접적이고 실질적인 소개를 제공하여, 수업에서 논의된 대로 공통 필드를 기반으로 두 개의 정렬된 텍스트 파일에서 줄을 병합하는 연습을 할 수 있도록 합니다.
2. **[Processing Employees Data](https://labex.io/ko/labs/linux-processing-employees-data-388132)** - `join` 및 `awk`와 같은 다른 강력한 Linux 명령줄 유틸리티에 대한 지식을 적용하여 여러 소스의 데이터를 결합하고 처리하여 실제 데이터 분석 시나리오를 시뮬레이션합니다.
3. **[Sequence Control and Pipeline](https://labex.io/ko/labs/linux-sequence-control-and-pipeline-17994)** - 명령 실행 시퀀스를 제어하고, 파이프라인을 활용하며, 강력한 텍스트 처리 도구를 사용하여 명령줄 효율성과 데이터 조작 기술을 향상시키세요. 이는 `join`의 데이터 결합 기능을 보완합니다.

이러한 실습은 실제 시나리오에서 텍스트 파일 조작 및 데이터 결합 개념을 적용하고 Linux 명령줄 도구에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`cat`, `dog`, `cow`라는 이름의 파일을 조인하려면 어떤 명령을 사용해야 합니까?

## Quiz Answer

join cat dog cow
