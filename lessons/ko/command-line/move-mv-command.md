---
index: 11
lang: "ko"
title: "mv (이동)"
meta_title: "mv (이동) - 명령줄"
meta_description: "Linux mv 명령을 사용하여 파일/디렉토리를 이동하고 이름을 변경하는 방법을 배웁니다. 옵션을 이해하고 덮어쓰기를 방지합니다. Linux 여정을 시작하세요!"
meta_keywords: "mv command, Linux mv, move files Linux, rename files Linux, Linux tutorial, beginner, Linux guide"
---

## Lesson Content

파일을 이동하고 이름을 변경하는 데 사용됩니다. 플래그와 기능 면에서 `cp` 명령과 매우 유사합니다.

다음과 같이 파일 이름을 변경할 수 있습니다:

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

`cp`와 마찬가지로 파일이나 디렉토리를 `mv`하면 동일한 디렉토리의 모든 것을 덮어씁니다. 따라서 덮어쓰기 전에 프롬프트를 표시하려면 `-i` 플래그를 사용할 수 있습니다.

```bash
mv -i directory1 directory2
```

파일을 `mv`하여 이전 파일을 덮어쓰고 싶다고 가정해 봅시다. 해당 파일의 백업을 만들 수도 있으며, 이전 버전의 이름이 `~`로 변경됩니다.

```bash
mv -b directory1 directory2
```

## Exercise

파일 이름을 변경한 다음 해당 파일을 다른 디렉토리로 이동합니다.

`mv` 명령을 직접 실습하려면 다음 대화형 랩을 시도해 보세요:

- [Linux mv Command: File Moving and Renaming](https://labex.io/ko/labs/linux-linux-mv-command-file-moving-and-renaming-209743)

## Quiz Question

`cat`이라는 파일의 이름을 `dog`으로 어떻게 변경합니까?

## Quiz Answer

mv cat dog
