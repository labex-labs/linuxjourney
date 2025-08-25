---
index: 10
lang: "ko"
title: "cp (복사)"
meta_title: "cp (복사) - 명령줄"
meta_description: "Linux cp 명령어를 사용하여 파일과 디렉토리를 복사하는 방법을 배우세요. -r 옵션과 와일드카드를 이해하세요. 오늘 Linux 여정을 시작하세요!"
meta_keywords: "cp 명령어, 파일 복사 Linux, Linux 튜토리얼, 초보자 Linux, cp -r, Linux 와일드카드, Linux 가이드"
---

## Lesson Content

이제 이 파일들을 복사해 봅시다. 다른 운영 체제에서 파일을 복사하여 붙여넣는 것과 마찬가지로, 셸은 훨씬 더 간단한 방법을 제공합니다.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile`은 복사하려는 파일이고, `/home/pete/Documents/cooldocs`는 파일을 복사할 위치입니다.

여러 파일과 디렉토리를 복사할 수 있으며, 와일드카드를 사용할 수도 있습니다. 와일드카드는 패턴 기반 선택을 대체할 수 있는 문자이며, 검색에 더 많은 유연성을 제공합니다. 모든 명령에서 와일드카드를 사용하여 더 많은 유연성을 얻을 수 있습니다.

- `*` 와일드카드의 와일드카드이며, 모든 단일 문자 또는 모든 문자열을 나타내는 데 사용됩니다.
- `?` 한 문자를 나타내는 데 사용됩니다.
- `[]` 괄호 안의 모든 문자를 나타내는 데 사용됩니다.

```bash
cp *.jpg /home/pete/Pictures
```

이 명령은 현재 디렉토리의 `.jpg` 확장자를 가진 모든 파일을 `Pictures` 디렉토리로 복사합니다.

유용한 명령은 `-r` 플래그를 사용하는 것입니다. 이 플래그는 디렉토리 내의 파일과 디렉토리를 재귀적으로 복사합니다.

몇 개의 파일이 포함된 디렉토리를 `Documents` 디렉토리로 `cp` 해보세요. 작동하지 않았죠? 그 이유는 `-r` 명령을 사용하여 내부의 파일과 디렉토리도 함께 복사해야 하기 때문입니다.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

한 가지 주의할 점은, 동일한 파일 이름을 가진 디렉토리로 파일을 복사하면, 해당 파일은 복사하려는 내용으로 덮어쓰여진다는 것입니다. 실수로 덮어쓰여지는 것을 원치 않는 파일이 있다면 좋지 않습니다. 파일을 덮어쓰기 전에 프롬프트를 표시하려면 `-i` 플래그 (대화형) 를 사용할 수 있습니다.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux 에서 파일과 디렉토리를 복사하는 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux cp 명령어: 파일 복사](https://labex.io/ko/labs/linux-linux-cp-command-file-copying-209744)** - 기본 사용법, 재귀 복사, 속성 유지, 와일드카드 사용과 같은 고급 옵션을 연습하여 파일과 디렉토리를 효율적으로 복사합니다.
2. **[파일 및 디렉토리 구성](https://labex.io/ko/labs/linux-organizing-files-and-directories-387877)** - `cp`, `mv`, `rm` 명령어를 사용하여 프로젝트 구조를 구성하고, 파일을 이동하고, 불필요한 디렉토리를 정리함으로써 필수적인 Linux 파일 관리 기술을 연습합니다.

이 랩들은 실제 시나리오에 개념을 적용하고 Linux 에서 파일 복사 및 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

디렉토리를 복사하기 위해 어떤 플래그를 지정해야 합니까?

## Quiz Answer

-r
