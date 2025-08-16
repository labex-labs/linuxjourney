---
lang: "ko"
title: "cp (복사)"
description: "Linux cp 명령을 사용하여 파일과 디렉토리를 복사하는 방법을 배우세요. -r 및 와일드카드와 같은 옵션을 이해하세요. 오늘 Linux 여정을 시작하세요!"
keywords: "cp command, copy files Linux, Linux tutorial, beginner Linux, cp -r, Linux wildcards, Linux guide"
---

## Lesson Content

이제 이 파일들을 복사해 봅시다. 다른 운영 체제에서 파일을 복사하여 붙여넣는 것과 마찬가지로, 셸은 훨씬 더 간단한 방법을 제공합니다.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

`mycoolfile`은 복사하려는 파일이고, `/home/pete/Documents/cooldocs`는 파일을 복사할 위치입니다.

여러 파일과 디렉토리를 복사할 수 있으며, 와일드카드를 사용할 수도 있습니다. 와일드카드는 패턴 기반 선택을 위해 대체될 수 있는 문자이며, 검색에 더 많은 유연성을 제공합니다. 모든 명령에서 와일드카드를 사용하여 더 많은 유연성을 얻을 수 있습니다.

- `*` 와일드카드 중의 와일드카드이며, 모든 단일 문자 또는 모든 문자열을 나타내는 데 사용됩니다.
- `?` 한 문자를 나타내는 데 사용됩니다.
- `[]` 괄호 안의 모든 문자를 나타내는 데 사용됩니다.

```bash
cp *.jpg /home/pete/Pictures
```

이것은 현재 디렉토리의 `.jpg` 확장자를 가진 모든 파일을 `Pictures` 디렉토리로 복사합니다.

유용한 명령은 `-r` 플래그를 사용하는 것입니다. 이것은 디렉토리 내의 파일과 디렉토리를 재귀적으로 복사합니다.

두어 개의 파일이 포함된 디렉토리를 `Documents` 디렉토리로 `cp` 해보세요. 작동하지 않았죠? 그것은 `-r` 명령으로 내부의 파일과 디렉토리도 함께 복사해야 하기 때문입니다.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

한 가지 유의할 점은, 동일한 파일 이름을 가진 디렉토리로 파일을 복사하면, 해당 파일은 복사하는 내용으로 덮어쓰여진다는 것입니다. 실수로 덮어쓰여지는 것을 원치 않는 파일이 있다면 좋지 않습니다. 파일을 덮어쓰기 전에 프롬프트를 표시하려면 `-i` 플래그 (interactive) 를 사용할 수 있습니다.

```bash
cp -i mycoolfile /home/pete/Pictures
```

## Exercise

두어 개의 파일을 복사하세요; 중요한 것을 덮어쓰지 않도록 주의하세요.

## Quiz Question

디렉토리를 복사하기 위해 어떤 플래그를 지정해야 합니까?

## Quiz Answer

-r
