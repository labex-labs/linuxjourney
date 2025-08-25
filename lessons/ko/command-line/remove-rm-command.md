---
index: 13
lang: "ko"
title: "rm (제거)"
meta_title: "rm (제거) - 명령줄"
meta_description: "`rm` 명령을 사용하여 Linux에서 파일과 디렉토리를 안전하게 삭제하는 방법을 배웁니다. `-f`, `-i`, `-r` 및 `rmdir`과 같은 옵션을 이해합니다. Linux 여정을 시작하세요!"
meta_keywords: "rm command, delete files Linux, remove directories, Linux tutorial, beginner Linux, rmdir, Linux guide"
---

## Lesson Content

이제 파일이 너무 많다고 생각합니다. 몇 개를 제거해 봅시다. 파일을 제거하려면 `rm` 명령을 사용할 수 있습니다. `rm` (remove) 명령은 파일과 디렉토리를 삭제하는 데 사용됩니다.

```bash
rm file1
```

`rm`을 사용할 때는 주의하십시오. 제거된 파일을 검색할 수 있는 마법의 휴지통은 없습니다. 일단 사라지면 영원히 사라지므로 조심하십시오.

다행히도 몇 가지 안전 조치가 마련되어 있어 일반 사용자가 중요한 파일을 쉽게 제거할 수는 없습니다. 쓰기 방지된 파일은 삭제하기 전에 확인 메시지를 표시합니다. 디렉토리가 쓰기 방지되어 있으면 쉽게 제거되지 않습니다.

이제 그런 것에 신경 쓰지 않는다면, 많은 파일을 완전히 제거할 수 있습니다.

```bash
rm -f file1
```

`-f` 또는 force 옵션은 `rm`에게 쓰기 방지 여부에 관계없이 모든 파일을 사용자에게 묻지 않고 제거하도록 지시합니다 (적절한 권한이 있는 한).

```bash
rm -i file
```

다른 많은 명령과 마찬가지로 `-i` 플래그를 추가하면 실제로 파일이나 디렉토리를 제거할 것인지 묻는 메시지가 표시됩니다.

```bash
rm -r directory
```

기본적으로 디렉토리를 `rm`할 수 없습니다. 해당 디렉토리의 모든 파일과 하위 디렉토리를 제거하려면 `-r` 플래그(recursive)를 추가해야 합니다.

`rmdir` 명령으로 디렉토리를 제거할 수 있습니다.

```bash
rmdir directory
```

## Exercise

연습이 완벽을 만듭니다! 다음은 Linux에서 파일 및 디렉토리 제거에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux rm Command: File Removing](https://labex.io/ko/labs/linux-linux-rm-command-file-removing-209741)** - `-r` 및 `-i`와 같은 다양한 옵션을 포함하여 파일 및 디렉토리 제거를 위한 `rm` 명령 사용법을 배우고 안전하고 효과적인 파일 삭제를 연습합니다.
2. **[Organizing Files and Directories](https://labex.io/ko/labs/linux-organizing-files-and-directories-387877)** - 실용적인 챌린지에서 불필요한 디렉토리를 정리하기 위해 `rm`을 사용하는 것을 포함하여 필수적인 Linux 파일 관리 기술을 연습합니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux에서 파일 및 디렉토리를 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`myfile`이라는 파일을 어떻게 제거합니까?

## Quiz Answer

rm myfile