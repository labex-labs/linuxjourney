---
index: 3
lang: "ko"
title: "tar 와 gzip"
meta_title: "tar 와 gzip - 패키지"
meta_description: "Linux 에서 tar 와 gzip 사용에 대한 종합 가이드입니다. tar 압축, 아카이브 생성 및 추출 방법, gzip 과 tar 의 차이점을 알아보세요. tar gz 파일 압축 및 소프트웨어 패키지 관리를 위한 명령어를 마스터하세요."
meta_keywords: "tar 와 gzip, tar 압축, gzip tar, tar gz 압축, gzip 과 tar, 리눅스 아카이빙, 파일 압축, tar 명령어, gzip 명령어, 리눅스 튜토리얼"
---

## Lesson Content

패키지 관리자로 넘어가기 전에 파일 보관 (아카이빙) 과 압축의 개념을 이해하는 것이 중요합니다. 온라인에서 소프트웨어를 다운로드할 때, 종종 보관 및 압축된 형식으로 패키징된 것을 발견하게 될 것입니다. 이 레슨에서는 이 목적을 위한 두 가지 기본 유틸리티인 `tar`와 `gzip`에 중점을 둡니다.

### 아카이빙 대 압축 이해하기

아카이빙과 압축을 구별하는 것이 중요합니다. **아카이빙**은 여러 파일과 디렉토리를 아카이브라고 불리는 단일 파일로 결합하는 과정입니다. 이는 파일 그룹을 더 쉽게 관리하고 전송할 수 있게 해줍니다. 반면에 **압축**은 디스크 공간을 절약하고 전송 속도를 높이기 위해 파일 크기를 줄이는 과정입니다. `tar` 유틸리티는 아카이빙에 사용되며, `gzip`은 압축에 사용됩니다. 종종 `gzip과 tar`가 함께 사용되는 것을 볼 수 있습니다.

### gzip 을 사용하여 단일 파일 압축하기

`gzip` 프로그램은 Linux 에서 개별 파일을 압축하는 데 사용됩니다. `gzip`으로 파일을 압축하면 `.gz` 확장자를 가진 파일로 대체됩니다.

파일을 압축하려면:

```bash
gzip mycoolfile
```

이렇게 하면 `mycoolfile.gz`가 생성되고 원본 파일은 제거됩니다. 파일을 압축 해제하려면 `gunzip`을 사용할 수 있습니다.

```bash
gunzip mycoolfile.gz
```

### tar 를 사용하여 아카이브 생성하기

`gzip`은 압축에 유용하지만 여러 파일을 단일 아카이브로 묶을 수는 없습니다. 이를 위해 `tar`(Tape Archive) 유틸리티를 사용합니다. `tar`로 생성된 파일은 종종 "tarball"이라고 불리며 `.tar` 확장자를 가집니다.

여러 파일을 포함하는 새 아카이브를 생성하려면:

```bash
tar cvf myarchive.tar file1 file2 directory1
```

옵션을 분석해 보겠습니다:

- `c`: 새 아카이브를 **c**reate(생성) 합니다.
- `v`: **v**erbose 모드로, 처리되는 파일을 나열합니다.
- `f`: **f**ile 로, 다음 인수가 아카이브 파일 이름임을 지정합니다.

### tar 와 gzip 결합의 강력함

진정한 강력함은 `tar와 gzip`을 함께 사용할 때 나옵니다. 먼저 `.tar` 아카이브를 생성한 다음 `gzip`으로 압축하여 `.tar.gz` 파일을 만들 수 있습니다. 그러나 `tar`는 `z` 옵션을 사용하여 단일 단계에서 `tar 압축`을 처리하는 편리한 방법을 제공합니다. 이 과정은 때때로 `gzip tar` 아카이브를 생성하는 것으로 언급됩니다.

`.tar.gz` 파일을 압축하는 일반적인 방법인 압축된 아카이브를 생성하려면:

```bash
tar czvf myarchive.tar.gz file1 file2 directory1
```

여기서 `z` 옵션은 `tar`에게 압축에 `gzip`을 사용하도록 지시합니다.

### tar 및 gzip 아카이브 추출하기

아카이브에서 파일을 추출하려면 `x` 옵션을 사용합니다.

단순한 `.tar` 아카이브를 추출하려면:

```bash
tar xvf myarchive.tar
```

`.tar.gz` 아카이브를 하나의 명령으로 압축 해제하고 추출하려면 `z` 옵션을 다시 추가하기만 하면 됩니다.

```bash
tar xzvf myarchive.tar.gz
```

추출 옵션을 검토해 보겠습니다:

- `x`: 아카이브에서 파일을 **e**xtract(추출) 합니다.
- `z`: **g**z**ip**을 사용하여 아카이브를 압축 해제합니다.
- `v`: **v**erbose 모드로, 추출되는 파일을 나열합니다.
- `f`: 추출할 아카이브 파일을 지정하는 **f**ile 입니다.

이것에 대한 유용한 암기법은 다음과 같습니다: e**X**tract **Z**ee **V**ery **F**ast!

`tar`는 매우 필수적이지만 종종 잊혀지는 명령어입니다. 관련 xkcd: `https://xkcd.com/1168`

### 기타 유틸리티

`tar`와 `gzip`이 매우 일반적이지만, Linux 여정에서 다른 아카이빙 및 압축 형식을 접하게 될 것입니다. 여기에는 `bzip2`(`.bz2` 파일을 생성하고 `tar`에서 `j` 플래그를 사용) 및 `xz`( `J` 플래그로 `.xz` 파일을 생성) 와 익숙한 `zip`/`unzip` 유틸리티가 포함됩니다. 각각 고유한 명령 세트와 압축률이 있지만 기본 개념은 동일하게 유지됩니다.

## Exercise

연습이 완벽을 만듭니다! 파일 아카이빙 및 압축에 대한 이해를 강화하기 위한 몇 가지 실습 랩이 있습니다:

1. **[파일 패키징 및 압축](https://labex.io/ko/labs/linux-file-packaging-and-compression-385413)** - tar, gzip, zip 과 같은 도구를 사용하여 필수적인 Linux 파일 압축 및 패키징 기술을 배웁니다.
2. **[Linux 에서 tar 를 사용하여 백업 생성 및 복원](https://labex.io/ko/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - tar 명령을 사용하여 파일 시스템 백업을 생성하고 복원하는 실습 경험을 쌓습니다.
3. **[시스템 로그 백업](https://labex.io/ko/labs/linux-backup-system-log-17989)** - tar 명령과 날짜 형식을 사용하여 시스템 로그 파일을 백업하는 필수 기술을 배웁니다.

이러한 랩은 실제 시나리오에서 아카이빙 및 압축 개념을 적용하고 Linux 에서 파일을 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

아카이브를 만드는 데 사용되는 tar 플래그는 무엇입니까? 단일 소문자 영어 문자로 답하십시오.

## Quiz Answer

c
