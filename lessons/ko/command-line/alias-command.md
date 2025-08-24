---
index: 18
lang: "ko"
title: "alias"
meta_title: "alias - 명령줄"
meta_description: "일반적인 명령어를 위한 Linux 별칭을 생성하고 관리하는 방법을 배우세요. .bashrc 에서 임시 및 영구 별칭 설정을 알아보세요. 명령줄 효율성을 향상시키세요!"
meta_keywords: "Linux alias, bash alias, unalias command, .bashrc, Linux tutorial, command line, beginner Linux, Linux guide"
---

## Lesson Content

명령어를 입력하는 것이 반복적이거나, 긴 명령어를 여러 번 입력해야 할 때가 있습니다. 이럴 때는 해당 명령어에 사용할 수 있는 별칭 (alias) 을 만드는 것이 가장 좋습니다. 명령어에 대한 별칭을 만들려면 별칭 이름을 지정하고 명령어를 설정하면 됩니다.

```bash
alias foobar='ls -la'
```

이제 `ls -la`를 입력하는 대신 `foobar`를 입력하면 해당 명령어가 실행됩니다. 정말 멋진 기능이죠. 이 명령어는 재부팅 후에는 별칭을 저장하지 않는다는 점을 명심하세요. 재부팅 후에도 별칭을 유지하려면 다음 파일에 영구 별칭을 추가해야 합니다:

```plaintext
~/.bashrc
```

또는 유사한 파일에 추가해야 합니다.

`unalias` 명령어를 사용하여 별칭을 제거할 수 있습니다:

```bash
unalias foobar
```

## Exercise

몇 개의 별칭을 생성한 다음 제거하세요.

Linux 명령줄 기본 사항에 대한 추가 실습을 위해 다음 대화형 랩을 살펴보세요:

- [Linux Directory Navigation](https://labex.io/ko/labs/linux-directory-navigation-387844)
- [Linux ls Command: Content Listing](https://labex.io/ko/labs/linux-linux-ls-command-content-listing-219205)

## Quiz Question

별칭을 만드는 데 사용되는 명령어는 무엇입니까?

## Quiz Answer

alias
