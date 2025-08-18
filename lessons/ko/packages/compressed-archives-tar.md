---
index: 3
lang: "ko"
title: "tar 및 gzip"
meta_title: "tar 및 gzip - 패키지"
meta_description: "Linux 에서 tar 와 gzip 을 사용하여 파일 보관 및 압축하는 방법을 배우세요. 파일 생성, 추출 및 압축을 위한 명령어를 이해하세요. 이 초보자 가이드로 시작하세요!"
meta_keywords: "tar, gzip, Linux 아카이빙, 파일 압축, tar 명령어, gzip 명령어, Linux 튜토리얼, 초보자 Linux"
---

## Lesson Content

패키지 설치와 다양한 관리자에 대해 알아보기 전에, 파일 보관 및 압축에 대해 논의해야 합니다. 인터넷에서 소프트웨어를 찾을 때 이러한 것들을 접할 가능성이 높기 때문입니다.

아마도 파일 아카이브가 무엇인지 이미 알고 계실 것입니다. .rar 및 .zip 과 같은 파일 형식을 접해 보셨을 것입니다. 이것들은 파일의 아카이브입니다. 그 안에는 많은 파일이 포함되어 있지만, 아카이브라고 알려진 매우 깔끔한 단일 파일 형태로 제공됩니다.

### Compressing files with gzip

gzip 은 Linux 에서 파일을 압축하는 데 사용되는 프로그램입니다. 파일은 .gz 확장자로 끝납니다.

파일을 압축하려면:

```bash
gzip mycoolfile
```

파일의 압축을 해제하려면:

```bash
gunzip mycoolfile.gz
```

### Creating archives with tar

안타깝게도 gzip 은 여러 파일을 하나의 아카이브에 추가할 수 없습니다. 다행히도 tar 프로그램이 이 기능을 제공합니다. tar 를 사용하여 아카이브를 생성하면 .tar 확장자를 갖게 됩니다.

```bash
tar cvf mytarfile.tar mycoolfile1 mycoolfile2
```

- `c` - 생성 (create)
- `v` - 프로그램이 상세하게 작동하도록 지시하고 진행 상황을 볼 수 있도록 함 (verbose)
- `f` - tar 파일의 파일 이름은 이 옵션 뒤에 와야 합니다. tar 파일을 생성하는 경우 이름을 지정해야 합니다.

### Unpacking archives with tar

tar 파일의 내용을 추출하려면 다음을 사용하십시오:

```bash
tar xvf mytarfile.tar
```

- `x` - 추출 (extract)
- `v` - 프로그램이 상세하게 작동하도록 지시하고 진행 상황을 볼 수 있도록 함 (verbose)
- `f` - 추출하려는 파일 (file)

### Compressing/uncompressing archives with tar and gzip

`mycompressedarchive.tar.gz`와 같이 압축된 tar 파일을 자주 보게 될 것입니다. 이 경우 외부에서부터 작업하면 됩니다. 먼저 `gunzip`으로 압축을 해제한 다음 tar 파일의 압축을 풀 수 있습니다. 또는 tar 와 함께 **z** 옵션을 사용하여 gzip 또는 gunzip 유틸리티를 사용하도록 지시할 수도 있습니다.

압축된 tar 파일을 생성:

```bash
tar czf myfile.tar.gz
```

압축 해제 및 압축 풀기:

```bash
tar xzf file.tar
```

기억하는 데 도움이 필요하다면: e**X**tract all **Z**ee **F**iles!

tar 는 매우 중요하지만 항상 기억하기 어려운 명령어 중 하나입니다. 관련 xkcd: <https://xkcd.com/1168/>

### Other Utilities

Linux 를 사용하는 동안 bzip2, compress, zip, unzip 등과 같은 다른 아카이브 및 압축 유형을 접하게 될 것입니다. 이들은 다소 덜 일반적이지만, 다른 유틸리티에는 다른 명령이 필요하다는 점을 명심하십시오.

## Exercise

tar 문서를 숙지하고 manpage 에서 사용 가능한 다른 옵션들을 살펴보십시오.

## Quiz Question

아카이브를 생성하는 데 사용되는 tar 플래그는 무엇입니까?

## Quiz Answer

c
