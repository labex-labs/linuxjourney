---
index: 2
lang: "ko"
title: "rsync"
meta_title: "rsync - 네트워크 공유"
meta_description: "효율적인 파일 동기화, 원격 데이터 전송 및 안정적인 백업을 위해 강력한 Linux rsync 명령어를 사용하는 방법을 알아보세요. 이 가이드는 주요 rsync 명령어와 옵션을 다룹니다."
meta_keywords: "rsync, 리눅스 rsync, 파일 동기화, 데이터 백업, 원격 동기화, rsync 명령어, 리눅스 파일 전송, rsync 튜토리얼"
---

## Lesson Content

### rsync 란 무엇인가?

서로 다른 호스트 간에 데이터를 복사하는 데 필수적인 또 다른 도구는 `rsync`이며, 이는 원격 동기화 (remote synchronization) 를 의미합니다. `scp`와 유사하지만, `rsync`는 매우 효율적인 핵심적인 차이점을 가지고 있습니다. 이 도구는 델타 전송 알고리즘 (delta-transfer algorithm) 을 사용하여 대상에 기존 데이터가 있는지 지능적으로 확인하고 변경된 파일 부분만 전송합니다.

예를 들어, 대용량 파일 전송이 중단된 경우, `rsync`는 처음부터 다시 시작하는 대신 파일의 나머지 부분만 전송하여 복사를 재개할 수 있습니다. 이는 불안정한 네트워크 연결에 대해 강력한 선택이 되게 합니다.

### rsync 의 주요 기능

`rsync`의 효율성은 스마트한 최적화에서 비롯됩니다. 이 도구는 체크섬을 사용하여 파일 무결성을 확인하여 복사된 데이터가 전송 중에 손상되지 않았는지 확인합니다. 이러한 기능은 상당한 유연성을 제공하여 `rsync`를 다음을 위한 이상적인 도구로 만듭니다.

- 디렉터리 동기화 (원격 및 로컬 모두)
- 증분 데이터 백업 생성
- 대용량 데이터 전송 효율적으로 처리

### 일반적인 rsync 옵션

여러 옵션을 사용하여 `rsync` 명령의 동작을 수정할 수 있습니다. 가장 일반적으로 사용되는 옵션은 다음과 같습니다.

- `-v`: 자세한 출력 (Verbose), 전송 중인 파일을 표시합니다.
- `-r`: 재귀적 (Recursive), 전체 디렉터리를 복사하는 데 필요합니다.
- `-h`: 사람이 읽기 쉬운 출력 (Human-readable), 숫자를 더 이해하기 쉬운 형식 (예: KB, MB) 으로 표시합니다.
- `-z`: 전송 중 파일 데이터를 압축하여 느린 연결에 매우 유용합니다.
- `-a`: 아카이브 모드 (Archive mode), 권한, 소유권 및 타임스탬프를 보존하기 위해 여러 옵션 (`-rlptgoD`) 을 결합하는 편리한 단축키입니다.

### rsync 사용 예시

#### 동일 호스트에서 파일 동기화

로컬 머신에서 두 디렉터리를 동기화하기 위해 `rsync`를 사용할 수 있습니다. 이는 로컬 백업을 만드는 데 유용합니다.

```bash
rsync -avh /my/local/directory/one/ /my/local/directory/two/
```

#### 원격 호스트에서 로컬 호스트로 파일 동기화

원격 서버에서 로컬 머신으로 파일을 가져오려면 먼저 원격 소스를 지정합니다.

```bash
rsync -avh username@remotehost.com:/remote/directory/ /local/directory/
```

#### 로컬 호스트에서 원격 호스트로 파일 동기화

로컬 머신에서 원격 서버로 파일을 푸시하려면 먼저 로컬 소스를 지정합니다.

```bash
rsync -avh /local/directory/ username@remotehost.com:/remote/directory/
```

## Exercise

이 주제에 대한 특정 실습은 없지만, 관련 Linux 기술 및 개념을 연습하기 위해 포괄적인 [Linux 학습 경로](https://labex.io/ko/learn/linux)를 살펴보는 것을 권장합니다.

## Quiz Question

효율적인 데이터 백업을 만드는 데 특히 유용한 델타 전송 알고리즘으로 알려진 명령어는 무엇입니까? 대소문자를 구분하여 영어로 답변하십시오.

## Quiz Answer

rsync
