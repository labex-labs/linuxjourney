---
index: 8
lang: "ko"
title: "head"
meta_title: "head - 텍스트 기술"
meta_description: "Linux 'head' 명령을 사용하여 파일의 시작 부분을 보는 방법을 배우세요. 줄 수를 위한 -n 과 같은 옵션을 이해하세요. 필수 Linux 명령 튜토리얼입니다."
meta_keywords: "head 명령, Linux head, 파일 시작 보기, Linux 튜토리얼, Linux 명령, 초보자 Linux, head -n, Linux 가이드"
---

## Lesson Content

아주 긴 파일이 있다고 가정해 봅시다. 사실, 선택할 수 있는 파일이 많습니다. `cat /var/log/syslog` 명령을 실행해 보세요. 수많은 페이지의 텍스트를 볼 수 있을 것입니다. 이 텍스트 파일에서 처음 몇 줄만 보고 싶다면 어떻게 해야 할까요? `head` 명령으로 그렇게 할 수 있습니다. 기본적으로 `head` 명령은 파일의 처음 10 줄을 보여줍니다.

```bash
head /var/log/syslog
```

원하는 대로 줄 수를 수정할 수도 있습니다. 예를 들어, 처음 15 줄을 보고 싶다고 가정해 봅시다.

```bash
head -n 15 /var/log/syslog
```

`-n` 플래그는 "줄 수 (number of lines)"를 의미합니다.

## Exercise

연습이 완벽을 만듭니다! 다음은 파일의 시작 부분을 보고 일반 텍스트 파일을 조작하는 이해를 강화하기 위한 실습 랩입니다:

1. **[Linux head 명령: 파일 시작 부분 표시](https://labex.io/ko/labs/linux-linux-head-command-file-beginning-display-214302)** - 이 랩은 `head` 명령을 사용하여 텍스트 파일의 초기 줄을 표시하고 줄 수를 수정하는 방법을 안내합니다.
2. **[Linux 에서 로그 및 구성 파일 보기](https://labex.io/ko/labs/linux-viewing-log-and-configuration-files-in-linux-387914)** - 시스템 로그 및 구성 파일과 같이 `head`와 같은 명령이 자주 필요한 텍스트 파일을 효율적으로 보고 탐색하기 위한 필수 Linux 명령줄 기술을 연습합니다.
3. **[신속한 위협 탐지](https://labex.io/ko/labs/linux-rapid-threat-detection-387930)** - `head` (및 `tail`) 에 대한 지식을 적용하여 최근 로그 항목을 신속하게 추출하고 분석하여 실제 사이버 보안 분석을 시뮬레이션합니다.

이러한 랩은 실제 시나리오에 개념을 적용하고 Linux 에서 텍스트 파일 보기 및 분석에 대한 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

`head` 명령으로 보고 싶은 줄 수를 변경하려면 어떤 플래그를 사용해야 합니까?

## Quiz Answer

-n
