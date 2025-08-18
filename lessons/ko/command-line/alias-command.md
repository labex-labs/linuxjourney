---
index: 18
lang: "ko"
title: "alias"
meta_title: "alias - Command Line"
meta_description: "일반적인 명령에 대한 Linux 별칭을 만들고 관리하는 방법을 알아보세요. .bashrc 에서 임시 및 영구 별칭 설정을 알아보세요. 명령줄 효율성을 향상시키세요!"
meta_keywords: "Linux alias, bash alias, unalias command, .bashrc, Linux tutorial, command line, beginner Linux, Linux guide"
---

## Lesson Content

때로는 명령을 입력하는 것이 매우 반복적이거나, 긴 명령을 여러 번 입력해야 하는 경우 해당 명령에 사용할 수 있는 별칭 (alias) 을 사용하는 것이 가장 좋습니다. 명령에 대한 별칭을 만들려면 별칭 이름을 지정하고 해당 명령으로 설정하면 됩니다.

```bash
alias foobar='ls -la'
```

이제 `ls -la`를 입력하는 대신 `foobar`를 입력하면 해당 명령이 실행됩니다. 아주 멋진 기능이죠. 이 명령은 재부팅 후 별칭을 저장하지 않으므로, 재부팅 후에도 유지하려면 다음 위치에 영구 별칭을 추가해야 합니다.

```plaintext
~/.bashrc
```

또는 유사한 파일에 추가해야 합니다.

`unalias` 명령으로 별칭을 제거할 수 있습니다.

```bash
unalias foobar
```

## Exercise

별칭 몇 개를 생성한 다음 제거하십시오.

## Quiz Question

별칭을 만드는 데 사용되는 명령은 무엇입니까?

## Quiz Answer

alias
