---
index: 14
lang: "ko"
title: "찾기"
meta_title: "find 명령어 - 명령줄"
meta_description: "리눅스 find 명령어에 대한 종합 가이드입니다. 이름, 유형 등으로 파일과 디렉토리를 찾는 find 명령줄 사용법을 배우세요. 강력한 리눅스 find 유틸리티로 파일 관리 기술을 향상시키세요."
meta_keywords: "find 명령어, 리눅스 find 명령어, find, 리눅스 find, 리눅스 find 명령어, 파일 검색, 디렉토리 검색, 리눅스 튜토리얼"
---

## Lesson Content

시스템에 수많은 파일이 있을 때 특정 파일을 찾는 것은 어려울 수 있습니다. 다행히도 이를 위해 사용할 수 있는 강력한 유틸리티가 있습니다. 바로 `find` 명령어입니다. 이 도구는 효율적인 파일 관리에 필수적입니다.

### Find 명령어 사용법

The basic syntax for the `find command line` is `find [path] [expression]`. 검색할 디렉토리와 찾고자 하는 항목에 대한 기준을 지정해야 합니다.

예를 들어, `/home` 디렉토리와 그 모든 하위 디렉토리에서 `puppies.jpg`라는 파일을 찾으려면 다음을 사용합니다.

```bash
find /home -name puppies.jpg
```

The `find command in linux` is highly flexible, allowing for many different search expressions.

### 이름 및 유형별 검색

The `find command`의 가장 일반적인 용도 중 하나는 파일 이름으로 검색하는 것입니다. 위에서 보았듯이, `-name` 옵션을 사용하여 찾고자 하는 파일의 정확한 이름을 지정할 수 있습니다.

You can also specify the type of item you are searching for. The `-type` option is used for this purpose. For instance, if you want to find a directory instead of a file, you can use `d`.

```bash
find /home -type d -name MyFolder
```

In this command, we set the type to `d` for directory and are searching for an item named `MyFolder`. To search specifically for regular files, you would use `-type f`.

### 재귀적 검색

The `find command linux` users appreciate is its recursive nature. When you specify a starting directory, `find` doesn't just look in that single directory; it automatically searches through all subdirectories contained within it. This makes it an incredibly thorough tool for locating items anywhere in a directory tree.

## Exercise

Practice is key to mastering the `find command in linux`. These hands-on labs will help you reinforce your understanding of finding files and directories:

1.  **[Linux find Command: File Searching](https://labex.io/ko/labs/linux-linux-find-command-file-searching-219191)** - 이 실습은 다양한 기준에 따라 파일과 디렉토리를 검색하고 찾는 데 유용한 `find` 명령어에 대한 소개를 제공합니다. `find`를 사용하여 특정 파일을 찾는 연습을 하게 됩니다.
2.  **[Discover Critical System Resources](https://labex.io/ko/labs/linux-discover-critical-system-resources-388032)** - `find`를 포함하여 파일과 실행 파일을 찾는 데 필수적인 Linux 명령어를 배웁니다. 파일 시스템을 효율적으로 탐색하고 중요한 시스템 리소스를 찾는 연습을 하게 됩니다.

These labs will help you apply the concepts in real scenarios and build confidence with using the `find` command effectively.

## Quiz Question

What option should you specify for the `find` command to search by name? Please answer using only the English option, paying attention to the required format (e.g., -option).

## Quiz Answer

-name
