---
lang: "ko"
title: "mv (이동)"
meta_description: "Linux mv 명령을 사용하여 파일/디렉토리를 이동하고 이름을 변경하는 방법을 배웁니다. 옵션을 이해하고 덮어쓰기를 방지합니다. Linux 여정을 시작하세요!"
meta_keywords: "mv command, Linux mv, 파일 이동 Linux, 파일 이름 변경 Linux, Linux 튜토리얼, 초보자, Linux 가이드"
---

## Lesson Content

파일을 이동하고 이름을 변경하는 데 사용됩니다. 플래그 및 기능 면에서 `cp` 명령과 매우 유사합니다.

파일 이름을 다음과 같이 변경할 수 있습니다:

```bash
mv oldfile newfile
```

또는 파일을 다른 디렉토리로 실제로 이동할 수 있습니다:

```bash
mv file2 /home/pete/Documents
```

그리고 하나 이상의 파일을 이동할 수 있습니다:

```bash
mv file_1 file_2 /somedirectory
```

디렉토리 이름도 변경할 수 있습니다:

```bash
mv directory1 directory2
```

`cp`와 마찬가지로, 파일이나 디렉토리를 `mv`하면 동일한 디렉토리의 모든 것을 덮어씁니다. 따라서 덮어쓰기 전에 확인 메시지를 표시하려면 `-i` 플래그를 사용할 수 있습니다.

```bash
mv -i directory1 directory2
```

이전 파일을 덮어쓰도록 `mv`하고 싶다고 가정해 봅시다. 해당 파일의 백업을 만들 수도 있으며, 이전 버전의 이름이 `~`로 변경됩니다.

```bash
mv -b directory1 directory2
```

## Exercise

파일 이름을 변경한 다음, 해당 파일을 다른 디렉토리로 이동합니다.

## Quiz Question

`cat`이라는 파일의 이름을 `dog`으로 어떻게 변경합니까?

## Quiz Answer

mv cat dog
