---
lang: "ko"
title: "head"
meta_title: "head - Text-Fu"
meta_description: "Linux 'head' 명령을 사용하여 파일의 시작 부분을 보는 방법을 배웁니다. 줄 수를 위한 -n 과 같은 옵션을 이해합니다. 필수 Linux 명령 튜토리얼입니다."
meta_keywords: "head command, Linux head, 파일 시작 보기, Linux 튜토리얼, Linux commands, 초보자 Linux, head -n, Linux 가이드"
---

## Lesson Content

매우 긴 파일이 있다고 가정해 봅시다. 사실, 선택할 수 있는 파일이 많습니다. `cat /var/log/syslog`를 실행해 보세요. 수많은 페이지의 텍스트를 볼 수 있을 것입니다. 이 텍스트 파일의 처음 몇 줄만 보고 싶다면 어떻게 해야 할까요? `head` 명령을 사용하면 됩니다. 기본적으로 `head` 명령은 파일의 처음 10 줄을 보여줍니다.

```bash
head /var/log/syslog
```

원하는 줄 수로 변경할 수도 있습니다. 예를 들어, 처음 15 줄을 보고 싶다고 가정해 봅시다.

```bash
head -n 15 /var/log/syslog
```

`-n` 플래그는 "number of lines"를 의미합니다.

## Exercise

다음 명령은 무엇을 하며 그 이유는 무엇입니까?

```bash
head -c 15 /var/log/syslog
```

## Quiz Question

`head` 명령으로 보고 싶은 줄 수를 변경하려면 어떤 플래그를 사용해야 합니까?

## Quiz Answer

-n
