---
index: 10
lang: "ko"
title: "cp (복사)"
meta_title: "cp (복사) - 명령줄"
meta_description: "Linux cp 명령을 마스터하여 파일과 디렉터리를 복사하는 방법을 알아보세요. 이 가이드는 재귀적 복사 (-r), cp -p 플래그를 사용한 속성 보존, cp -f 플래그를 사용한 덮어쓰기 강제 실행과 같은 필수 옵션을 다룹니다. Linux 에서 cp -p 가 파일 메타데이터 유지에 도움이 되는 이유를 학습하세요."
meta_keywords: "cp 명령어, 리눅스 파일 복사, 리눅스 cp -p, cp -p 플래그, 리눅스 cp -p, cp -f 플래그, 재귀적 복사, cp -r, 리눅스 와일드카드, 리눅스 명령줄"
---

## Lesson Content

cp 명령어는 Linux 에서 파일과 디렉터리를 복사하는 표준 도구입니다. 기본 구문은 `cp [소스] [대상]`입니다.

### 기본 파일 복사

파일을 복사하려면 소스 파일과 대상 디렉터리 또는 경로를 지정합니다.

```bash
cp mycoolfile /home/pete/Documents/cooldocs
```

이 예시에서 `mycoolfile`은 소스 파일이고, `/home/pete/Documents/cooldocs`는 대상 디렉터리입니다. 파일을 복사하면서 대상에서 새 이름을 지정할 수도 있습니다.

```bash
cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

### 일괄 복사를 위한 와일드카드 사용

와일드카드는 패턴을 기반으로 여러 파일을 선택하는 데 도움이 되는 특수 문자이며, 뛰어난 유연성을 제공합니다.

- `*`: 모든 문자 시퀀스와 일치합니다.
- `?`: 단일 문자와 일치합니다.
- `[]`: 대괄호 안에 있는 문자 중 하나와 일치합니다.

예를 들어, 현재 위치의 모든 JPEG 이미지를 `Pictures` 디렉터리로 복사하려면 다음과 같이 합니다.

```bash
cp *.jpg /home/pete/Pictures
```

### 디렉터리 재귀적 복사

옵션 없이 `cp`를 사용하여 디렉터리를 복사하려고 하면 오류가 발생합니다. 디렉터리와 모든 하위 디렉터리를 포함한 모든 내용을 복사하려면 `-r` (재귀) 플래그를 사용해야 합니다.

```bash
cp -r Pumpkin/ /home/pete/Documents
```

이 명령어는 `Pumpkin` 디렉터리와 그 안의 모든 것을 `Documents` 디렉터리로 복사합니다.

### 파일 덮어쓰기 처리

기본적으로 `cp`는 이름이 같은 파일이 대상에 있으면 덮어씁니다. 실수로 인한 데이터 손실을 방지하려면 덮어쓰기 전에 확인 메시지를 표시하는 `-i` (대화형) 플래그를 사용하십시오.

```bash
cp -i mycoolfile /home/pete/Pictures
```

반대로, 프롬프트 없이 덮어쓰기를 강제하려면 `cp -f` 플래그를 사용할 수 있습니다. 이는 사용자 상호 작용이 불가능한 스크립트에서 유용합니다.

```bash
cp -f mycoolfile /home/pete/Pictures
```

### cp -p 를 사용한 파일 속성 보존

파일을 복사할 때 수정 시간 및 소유권과 같은 메타데이터는 일반적으로 업데이트됩니다. 이러한 원래 속성을 보존하려면 `cp -p` 플래그가 필수적입니다. `linux에서 cp -p 사용`은 내용뿐만 아니라 메타데이터에서도 복사본이 정확한 복제본이 되도록 보장합니다.

`cp -p 플래그`는 백업을 수행하거나 타임스탬프 보존이 중요한 파일을 마이그레이션할 때 특히 유용합니다.

```bash
cp -p mycoolfile /home/pete/backups/
```

이 명령어는 `linux cp -p`를 사용하여 `mycoolfile`을 복사하면서 모드, 소유권 및 타임스탬프를 보존하는 방법을 보여줍니다.

## Exercise

연습이 완벽을 만듭니다! Linux 에서 파일 및 디렉터리 복사에 대한 이해를 강화하기 위한 실습 랩이 있습니다:

1.  **[Linux cp 명령어: 파일 복사](https://labex.io/ko/labs/linux-linux-cp-command-file-copying-209744)** - 기본 사용법, 재귀적 복사, 속성 보존과 같은 고급 옵션 및 와일드카드를 사용하여 파일과 디렉터리를 효율적으로 복사하는 방법을 연습합니다.
2.  **[파일 및 디렉터리 정리](https://labex.io/ko/labs/linux-organizing-files-and-directories-387877)** - `cp`, `mv`, `rm` 명령어를 사용하여 프로젝트 구조를 정리하고, 파일을 이동하고, 불필요한 디렉터리를 정리하여 필수적인 Linux 파일 관리 기술을 연습합니다.

이 랩들은 실제 시나리오에서 개념을 적용하고 Linux 에서 파일 복사 및 관리에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

디렉터리를 복사하려면 지정해야 하는 플래그는 무엇입니까?

## Quiz Answer

-r
