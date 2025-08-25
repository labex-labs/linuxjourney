---
index: 3
lang: "ko"
title: "tar 및 gzip"
meta_title: "tar 및 gzip - 패키지"
meta_description: "Linux 에서 파일 아카이빙 및 압축을 위해 tar 와 gzip 을 사용하는 방법을 배웁니다. 파일 생성, 추출 및 압축을 위한 명령어를 이해합니다. 이 초보자 가이드로 시작하세요!"
meta_keywords: "tar, gzip, Linux 아카이빙, 파일 압축, tar 명령어, gzip 명령어, Linux 튜토리얼, 초보자 Linux"
---

## Lesson Content

패키지 설치와 다양한 관리자에 대해 알아보기 전에, 파일 아카이빙 및 압축에 대해 논의해야 합니다. 인터넷에서 소프트웨어를 찾을 때 이들을 접할 가능성이 높기 때문입니다.

파일 아카이브가 무엇인지 이미 알고 있을 것입니다. .rar 및 .zip 과 같은 파일 형식을 접했을 가능성이 높습니다. 이들은 파일의 아카이브입니다. 그 안에는 많은 파일이 포함되어 있지만, 아카이브라고 알려진 매우 깔끔한 단일 파일 형태로 제공됩니다.

### gzip 으로 파일 압축하기

gzip 은 Linux 에서 파일을 압축하는 데 사용되는 프로그램이며, .gz 확장자로 끝납니다.

파일을 압축하려면:

```bash
gzip mycoolfile
```

파일 압축을 해제하려면:

```bash
gunzip mycoolfile.gz
```

### tar 로 아카이브 생성하기

안타깝게도 gzip 은 여러 파일을 하나의 아카이브에 추가할 수 없습니다. 다행히 tar 프로그램이 이 기능을 제공합니다. tar 를 사용하여 아카이브를 생성하면 .tar 확장자를 갖게 됩니다.

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - 생성 (create)
- `v` - 프로그램이 상세하게 작동 상황을 보여주도록 지시
- `f` - tar 파일의 파일명은 이 옵션 뒤에 와야 합니다. tar 파일을 생성하는 경우 이름을 지정해야 합니다.

### tar 로 아카이브 압축 해제하기

tar 파일의 내용을 추출하려면 다음을 사용합니다:

```bash
tar xvf mytarfile.tar
```

- `x` - 추출 (extract)
- `v` - 프로그램이 상세하게 작동 상황을 보여주도록 지시
- `f` - 추출하려는 파일

### tar 와 gzip 으로 아카이브 압축/압축 해제하기

`mycompressedarchive.tar.gz`와 같이 압축된 tar 파일을 자주 볼 수 있습니다. 이 경우 외부에서부터 작업하면 됩니다. 먼저 `gunzip`으로 압축을 해제한 다음 tar 파일의 압축을 풀 수 있습니다. 또는 tar 와 함께 **z** 옵션을 사용할 수도 있습니다. 이 옵션은 gzip 또는 gunzip 유틸리티를 사용하도록 지시합니다.

압축된 tar 파일 생성:

```bash
tar czf myfile.tar.gz
```

압축 해제 및 압축 풀기:

```bash
tar xzf file.tar
```

기억하는 데 도움이 필요하다면: e**X**tract all **Z**ee **F**iles!

tar 는 매우 중요하지만 항상 기억하기 어려운 명령어 중 하나입니다. 관련 xkcd: `https://xkcd.com/1168`

### 기타 유틸리티

Linux 를 사용하는 동안 bzip2, compress, zip, unzip 등과 같은 다른 아카이브 및 압축 유형을 접하게 될 것입니다. 이들은 덜 일반적이지만, 다른 유틸리티에는 다른 명령어가 필요하다는 점을 명심하십시오.

## Exercise

연습이 완벽을 만듭니다! 파일 아카이빙 및 압축에 대한 이해를 강화하기 위한 실습 랩입니다:

1. **[파일 패키징 및 압축](https://labex.io/ko/labs/linux-file-packaging-and-compression-385413)** - tar, gzip, zip 과 같은 도구를 사용하여 필수 Linux 파일 압축 및 패키징 기술을 배웁니다.
2. **[Linux 에서 tar 로 백업 생성 및 복원](https://labex.io/ko/labs/comptia-create-and-restore-a-backup-with-tar-in-linux-590843)** - tar 명령어를 사용하여 파일 시스템 백업을 생성하고 복원하는 실습 경험을 얻습니다.
3. **[시스템 로그 백업](https://labex.io/ko/labs/linux-backup-system-log-17989)** - tar 명령어와 날짜 형식을 사용하여 시스템 로그 파일을 백업하는 필수 기술을 배웁니다.

이 랩들은 실제 시나리오에서 아카이빙 및 압축 개념을 적용하고 Linux 에서 파일을 관리하는 데 자신감을 키우는 데 도움이 될 것입니다.

## Quiz Question

아카이브를 생성하는 데 사용되는 tar 플래그는 무엇입니까?

## Quiz Answer

c
