---
index: 17
lang: "ko"
title: "whatis"
meta_title: "whatis - 명령어 라인"
meta_description: "Linux 의 whatis 명령어를 알아보세요. linux whatis 명령어가 다른 명령어에 대한 한 줄 설명을 제공하여 명령줄 탐색에 필수적인 도구임을 확인하세요."
meta_keywords: "리눅스 whatis 명령어, whatis 리눅스, 리눅스 whatis 명령어, whatis 명령어 리눅스, 리눅스 whatis, 명령줄, 리눅스 명령어"
---

## Lesson Content

Linux 명령줄을 탐색하다 보면 방대한 수의 명령어를 접하게 될 것입니다. 특정 명령어가 무엇을 하는지 잊어버리는 것은 당연합니다. 다행히도 이를 도와줄 간단한 유틸리티가 있습니다.

### Linux 에서 whatis 명령어란 무엇인가

Linux 의 `whatis` 명령어는 해당 명령어의 매뉴얼 (man) 페이지에서 직접 가져온 간결한 한 줄 설명을 표시합니다. 전체 매뉴얼 페이지를 읽지 않고도 명령어의 주요 기능을 빠르게 상기할 수 있는 방법입니다. **linux whatis** 명령어를 터미널을 위한 빠른 사전이라고 생각하시면 됩니다.

### whatis 명령어 사용 방법

**whatis command linux** 사용법은 간단합니다. `whatis`를 입력한 다음 알고 싶은 명령어 이름을 입력하기만 하면 됩니다. 예를 들어, `cat` 명령어에 대해 잘 모르겠다면 다음을 실행할 수 있습니다.

```bash
whatis cat
```

그러면 "cat - 파일을 연결하고 표준 출력으로 출력"과 같은 짧은 설명이 반환됩니다.

### 출력 이해하기

**linux whatis command**가 제공하는 설명은 명령어 매뉴얼 페이지의 NAME 섹션에서 직접 가져온 것입니다. 이는 정보가 정확하고 시스템 문서와 일관됨을 보장합니다. 만약 어떤 명령어가 여러 섹션에 걸쳐 여러 매뉴얼 페이지를 가지고 있다면, `whatis`는 각 항목에 대한 줄을 표시하여 다양한 맥락을 이해하는 데 도움을 줄 수 있습니다.

## Exercise

연습이 완벽을 만듭니다! `whatis` 명령어에 대한 특정 실습은 없지만, 명령어와 파일에 대한 정보를 찾는 방법을 이해하는 것은 매우 중요합니다. 다음은 Linux 에서 명령어와 파일을 찾는 이해도를 높이기 위한 실습 랩입니다.

1. **[Linux which 명령어: 명령어 위치 찾기](https://labex.io/ko/labs/linux-linux-which-command-command-locating-215210)** - `which` 명령어를 사용하여 실행 파일을 찾고 시스템 PATH 내의 명령어 우선순위를 이해하는 연습을 해보세요.
2. **[Linux whereis 명령어: 파일 및 명령어 찾기](https://labex.io/ko/labs/linux-linux-whereis-command-file-and-command-finding-215211)** - `whereis`를 사용하여 명령어의 바이너리, 소스 및 매뉴얼 페이지를 찾아 명령어가 구성되는 방식에 대한 이해를 심화하세요.
3. **[중요 시스템 리소스 발견하기](https://labex.io/ko/labs/linux-discover-critical-system-resources-388032)** - 이 챌린지는 `which`, `whereis`, `find`를 결합하여 파일 시스템을 효율적으로 탐색하고 중요한 시스템 리소스를 찾는 데 도움을 줍니다.

이러한 랩은 명령어 및 파일 검색 개념을 실제 시나리오에 적용하고 필수적인 Linux 유틸리티에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

명령어에 대한 작은 설명을 보려면 어떤 명령어를 사용할 수 있습니까? 영어로 대답하고 소문자에 주의하십시오.

## Quiz Answer

whatis
