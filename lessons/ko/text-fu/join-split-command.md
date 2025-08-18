---
lang: "ko"
title: "join 및 split"
meta_title: "join 및 split - Text-Fu"
meta_description: "Linux 의 'join' 및 'split' 명령을 사용하여 파일을 조작하는 방법을 배웁니다. 공통 필드를 기준으로 파일을 결합하고 큰 파일을 효율적으로 분할하는 방법을 이해합니다. 실용적인 예제와 팁을 얻으세요."
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

`-1`은 `file1.txt`를, `-2`는 `file2.txt`를 나타냅니다. 꽤 유용하죠. `split` 명령을 사용하여 파일을 여러 파일로 분할할 수도 있습니다:

```bash
split somefile
```

이렇게 하면 파일이 여러 파일로 분할됩니다. 기본적으로 1000 줄 제한에 도달하면 분할됩니다. 파일 이름은 기본적으로 `x**`입니다.

## Exercise

각 파일에 다른 수의 줄이 있는 두 파일을 조인해 보세요. 어떤 일이 발생하나요?

## Quiz Question

`cat`, `dog`, `cow`라는 이름의 파일을 조인하려면 어떤 명령을 사용해야 할까요?

## Quiz Answer

join cat dog cow
