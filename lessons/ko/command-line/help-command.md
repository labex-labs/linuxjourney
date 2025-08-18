---
index: 15
lang: "ko"
title: "help"
meta_title: "help - Command Line"
meta_description: "Bash 에서 'help' 명령을 사용하여 빠른 명령줄 지원을 받는 방법을 배웁니다. 내장 명령을 이해하고 Linux 프로그램에 대한 옵션을 찾습니다."
meta_keywords: "Linux help 명령, Bash help, 명령줄 도움말, Linux 명령, 초보자 Linux, Linux 튜토리얼, Bash 튜토리얼"
---

## Lesson Content

Linux 에는 명령 사용법을 이해하거나 명령에 사용할 수 있는 플래그를 확인하는 데 도움이 되는 훌륭한 내장 도구가 있습니다. `help`라는 도구는 다른 Bash 명령 (예: `echo`, `logout`, `pwd`) 에 대한 도움말을 제공하는 내장 Bash 명령입니다.

```bash
help echo
```

이것은 `echo`를 실행할 때 사용할 수 있는 설명과 옵션을 제공합니다. 다른 실행 가능한 프로그램의 경우 `--help` 또는 이와 유사한 옵션을 갖는 것이 관례입니다.

```bash
echo --help
```

실행 파일을 배포하는 모든 개발자가 이 표준을 따르지는 않지만, 프로그램에 대한 도움말을 찾는 가장 좋은 방법일 것입니다.

## Exercise

`echo` 명령, `logout` 명령 및 `pwd` 명령에 대해 `help`를 실행하십시오.

## Quiz Question

내장 Bash 명령에 대한 빠른 명령줄 도움말을 어떻게 얻을 수 있습니까?

## Quiz Answer

help
