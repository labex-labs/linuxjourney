---
index: 10
lang: "ko"
title: "cp (복사)"
meta_title: "cp (복사) - 명령어 라인"
meta_description: "파일, 디렉터리, 다중 파일, 와일드카드, 백업 및 cp -r, cp -i, cp -p 같은 옵션을 사용한 Linux cp 명령어 예제를 배워보세요."
meta_keywords: "linux cp 명령어, cp 명령어, 파일 복사 linux, cp -r, cp -i, cp -p, cp -a, cp -u, 재귀 복사, linux 와일드카드"
---

## Lesson Content

`cp` 명령어는 Linux에서 파일과 디렉터리를 복사하는 표준 도구입니다. 원본 파일을 그대로 두고 새 복사본을 만듭니다. 기본 구문은 다음과 같습니다:

```bash
cp [OPTIONS] SOURCE DESTINATION
```

한 개의 파일을 다른 파일로, 하나 이상의 파일을 디렉터리로, 또는 적절한 옵션을 사용해 전체 디렉터리 트리를 복사할 수 있습니다.

### 기본 파일 복사

파일을 복사하려면 원본 파일과 대상 디렉터리 또는 경로를 지정합니다.

```bash
$ cp mycoolfile /home/pete/Documents/cooldocs
```

이 예제에서 `mycoolfile`은 원본 파일이고, `/home/pete/Documents/cooldocs`는 대상 디렉터리입니다. 또한 파일을 복사하면서 대상 위치에서 새 이름을 지정할 수도 있습니다.

```bash
$ cp mycoolfile /home/pete/Documents/mycoolfile_backup
```

대상이 기존 디렉터리라면 복사된 파일은 원래 이름을 유지합니다. 대상이 파일 이름이라면 `cp`는 그 새 이름으로 복사본을 만듭니다.

### 여러 파일을 디렉터리에 복사하기

여러 파일을 같은 디렉터리에 복사하려면 모든 원본 파일을 먼저 나열하고 마지막에 대상 디렉터리를 적습니다.

```bash
$ cp report.txt notes.txt summary.txt /home/pete/Documents/
```

원본이 두 개 이상일 때 마지막 인수는 반드시 디렉터리여야 합니다.

### 와일드카드를 사용한 대량 복사

와일드카드는 패턴에 따라 여러 파일을 선택하는 데 도움을 주는 특수 문자로, 매우 유용합니다.

- `*`: 임의의 문자 시퀀스와 일치합니다.
- `?`: 임의의 한 문자와 일치합니다.
- `[]`: 대괄호 안의 문자 중 하나와 일치합니다.

예를 들어, 현재 위치에서 모든 JPEG 이미지를 `Pictures` 디렉터리로 복사하려면:

```bash
$ cp *.jpg /home/pete/Pictures
```

복사 전에 일치하는 파일을 미리 확인할 수도 있습니다:

```bash
$ ls *.jpg
beach.jpg  lunch.jpg  profile.jpg
$ cp *.jpg /home/pete/Pictures
```

### 디렉터리를 재귀적으로 복사하기

옵션 없이 `cp`로 디렉터리를 복사하려 하면 오류가 발생합니다. 디렉터리와 그 안의 모든 내용을 포함해 복사하려면 `-r` (재귀) 플래그를 사용해야 합니다.

```bash
$ cp -r Pumpkin/ /home/pete/Documents
```

이 명령은 `Pumpkin` 디렉터리와 그 안의 모든 내용을 `Documents` 디렉터리로 복사합니다.

일반 Linux 시스템에서는 `-R`도 같은 재귀 목적을 가집니다:

```bash
$ cp -R website /home/pete/backups/
```

### 파일 덮어쓰기 처리

기본적으로 `cp`는 대상에 같은 이름의 파일이 있으면 덮어씁니다. 실수로 데이터 손실을 막으려면 `-i` (대화형) 플래그를 사용해 덮어쓰기 전에 확인을 요청할 수 있습니다.

```bash
$ cp -i mycoolfile /home/pete/Pictures
cp: overwrite '/home/pete/Pictures/mycoolfile'? n
```

반대로, 프롬프트 없이 강제로 덮어쓰려면 `-f` 옵션을 사용합니다. 스크립트에서 사용자 상호작용이 불가능할 때 유용합니다.

```bash
$ cp -f mycoolfile /home/pete/Pictures
```

또 다른 유용한 안전 옵션은 `-n`으로, "덮어쓰기 금지"를 의미하며 기존 대상 파일을 덮어쓰지 않습니다.

```bash
$ cp -n mycoolfile /home/pete/Pictures
```

### -p 옵션으로 파일 속성 보존하기

파일을 복사할 때 보통 수정 시간과 소유권 같은 메타데이터가 갱신됩니다. 원본 속성을 유지하려면 `-p` 옵션을 사용하세요.

`cp -p` 옵션은 백업이나 타임스탬프 보존이 중요한 파일 이동 시 특히 유용합니다.

```bash
$ cp -p mycoolfile /home/pete/backups/
```

이 명령은 `mycoolfile`을 모드, 허용되는 소유권, 타임스탬프를 보존하며 복사합니다.

### -a 옵션으로 아카이브 복사하기

`-a` 옵션은 아카이브를 의미하며, 많은 속성을 보존하고 재귀적으로 복사하기 때문에 백업용 디렉터리 복사에 자주 사용됩니다.

```bash
$ cp -a project/ project-backup/
```

일상적인 백업에서는 여러 옵션을 조합하는 것보다 `cp -a`가 더 편리합니다.

### -u 옵션으로 최신 파일만 복사하기

`-u` 옵션은 원본 파일이 대상 파일보다 새롭거나 대상 파일이 없을 때만 복사합니다.

```bash
$ cp -u *.txt /home/pete/Documents/
```

이미 최신인 파일을 다시 쓰지 않고 폴더를 갱신할 때 유용합니다.

### 자주 사용하는 cp 옵션

가장 자주 사용하는 옵션은 다음과 같습니다:

- `-r` 또는 `-R`: 디렉터리를 재귀적으로 복사합니다.
- `-i`: 덮어쓰기 전에 확인을 요청합니다.
- `-f`: 필요 시 먼저 대상을 삭제하여 강제로 덮어씁니다.
- `-n`: 기존 파일을 덮어쓰지 않습니다.
- `-p`: 모드, 허용되는 소유권, 타임스탬프를 보존합니다.
- `-a`: 아카이브 모드로, 디렉터리 트리를 보존하는 데 유용합니다.
- `-u`: 원본이 대상보다 새로울 때만 복사합니다.
- `-v`: 복사 중인 각 파일을 보여줍니다.

### 자주 묻는 질문

**왜 cp가 내 파일을 덮어썼나요?** 기본적으로 `cp`는 같은 이름의 대상 파일을 덮어씁니다. 먼저 묻도록 하려면 `cp -i`를, 덮어쓰지 않으려면 `cp -n`을 사용하세요.

**왜 cp가 디렉터리를 복사하지 못하나요?** 디렉터리는 재귀 복사가 필요합니다. `cp -r source-dir destination-dir`을 사용하세요.

**cp와 mv의 차이는 무엇인가요?** `cp`는 복사본을 만들고 원본을 유지합니다. `mv`는 원본을 이동하거나 이름을 바꿉니다.

**백업용으로 cp -r과 cp -a 중 어느 것을 써야 하나요?** 단순 재귀 복사는 `cp -r`을, 더 많은 파일 속성을 보존하는 백업 스타일 복사는 `cp -a`를 사용하세요.

## Exercise

연습이 완벽을 만듭니다! Linux에서 파일과 디렉터리 복사를 이해하는 데 도움이 되는 실습 랩입니다:

1. **[Linux cp 명령어: 파일 복사](https://labex.io/ko/labs/linux-linux-cp-command-file-copying-209744)** - 기본 사용법, 재귀 복사, 속성 보존, 와일드카드 사용 등 고급 옵션을 연습하며 파일과 디렉터리를 효율적으로 복사하는 방법을 익히세요.
2. **[파일과 디렉터리 정리하기](https://labex.io/ko/labs/linux-organizing-files-and-directories-387877)** - `cp`, `mv`, `rm` 명령어를 사용해 프로젝트 구조를 정리하고 파일을 이동하며 불필요한 디렉터리를 정리하는 필수 Linux 파일 관리 기술을 연습하세요.

이 랩들은 실제 상황에서 개념을 적용하고 Linux에서 파일 복사 및 관리를 자신 있게 수행할 수 있도록 도와줍니다.

## Quiz Question

디렉터리를 복사하려면 어떤 플래그를 지정해야 하나요?

## Quiz Answer

-r
