---
lesson_id: "device-types"
course_id: "devices"
lang: "ko"
order_index: 2
title: "장치 유형"
description: "문자 및 블록 장치 노드를 파이프, 소켓 및 일반 파일 시스템 객체와 구분하는 방법을 알아봅니다."
meta_title: "장치 유형 - 장치"
meta_description: "문자, 블록, 파이프 및 소켓 장치를 비롯한 리눅스 장치 유형을 살펴봅니다. ls -l /dev로 장치 파일을 식별하고 주 번호와 부 번호의 역할을 이해합니다."
meta_keywords: "리눅스 장치, 리눅스 장치 유형, 장치 파일, 문자 장치, 블록 장치, 주 번호 부 번호, /dev 디렉터리"
---

`ls -l` 모드의 첫 번째 문자는 객체의 파일 시스템 유형을 나타냅니다. `/dev` 아래에서 문자 특수 파일과 블록 특수 파일은 장치 노드입니다. 파이프와 유닉스 도메인 소켓 노드도 그곳에 나타날 수 있지만, 하드웨어 장치 노드가 아니라 프로세스 간 통신 객체입니다.

```text
$ ls -l /dev/null /dev/sda /run/systemd/journal/dev-log /tmp/example-fifo
crw-rw-rw- 1 root root 1, 3 ... /dev/null
brw-rw---- 1 root disk 8, 0 ... /dev/sda
srw-rw-rw- 1 root root      ... /run/systemd/journal/dev-log
prw------- 1 user user      ... /tmp/example-fifo
```

항목과 권한은 시스템마다 다릅니다. 이 예시는 유형 문자만 보여 줍니다.

## 문자 장치 노드

`c`는 문자 장치를 나타냅니다. 문자 장치는 일반적으로 주소를 지정할 수 있는 고정 크기 저장 블록이 아니라 스트림 지향 또는 장치별 인터페이스를 노출합니다. 터미널과 `/dev/null` 같은 의사 장치가 그 예입니다.

“문자”라고 해서 각 시스템 호출이 정확히 한 문자만 전송해야 하는 것은 아닙니다. 애플리케이션은 버퍼를 읽거나 쓸 수 있으며, 블로킹, 프레이밍 및 제어 동작은 드라이버가 정의합니다.

:::single-choice{#device-types-character-marker} 문자 장치 노드를 나타내는 첫 번째 모드 문자는 무엇입니까?

::option[`b`]{#device-types-marker-block explanation="`b` 표시는 블록 장치 노드를 나타냅니다."}
::option[`p`]{#device-types-marker-pipe explanation="`p` 표시는 FIFO, 즉 이름 있는 파이프를 나타냅니다."}
::option[`c`]{#device-types-marker-character .correct explanation="문자 특수 파일은 긴 목록 모드의 시작 부분에 `c`로 표시됩니다."}
:::

## 블록 장치 노드

`b`는 블록 장치를 나타냅니다. 블록 장치는 커널의 블록 계층을 통해 블록 단위로 주소 지정 가능한 저장 공간을 제공하며, 버퍼링된 입출력, 파티셔닝 및 파일 시스템 같은 작업을 지원할 수 있습니다. 디스크, 파티션 및 논리 볼륨에는 일반적으로 블록 노드가 있습니다.

블록 노드는 마운트된 파일 시스템이 아닙니다. 저장 장치 또는 논리 영역을 나타내며, 그 위에 파일 시스템을 만들고 별도로 마운트할 수 있습니다. 잘못된 블록 노드에 원시 데이터를 쓰면 파티션 테이블, 파일 시스템 또는 사용자 데이터가 파괴될 수 있습니다.

:::single-choice{#device-types-block-marker} 첫 번째 모드 문자 `b`는 무엇을 나타냅니까?

::option[백그라운드 셸 작업입니다.]{#device-types-background-job explanation="셸 작업 상태는 파일 시스템 유형 문자로 인코딩되지 않습니다."}
::option[블록 장치 인터페이스입니다.]{#device-types-block-device .correct explanation="블록 특수 파일은 커널 블록 하위 시스템을 통해 주소 지정 가능한 저장 공간을 노출합니다."}
::option[끊어진 심볼릭 링크입니다.]{#device-types-broken-link explanation="대상의 존재 여부와 관계없이 심볼릭 링크는 `l`을 사용합니다."}
:::

## FIFO와 소켓 노드

`p`는 이름 있는 파이프라고도 하는 FIFO를 나타냅니다. FIFO는 프로세스가 통신할 수 있는 이름 있는 바이트 스트림을 제공합니다. 소비된 데이터는 FIFO 노드에 영구적으로 저장되지 않습니다.

`s`는 유닉스 도메인 소켓 노드를 나타냅니다. 로컬 소켓 엔드포인트에 이름을 붙이며 연결 지향 또는 데이터그램 통신, 디스크립터 전달 및 피어 자격 증명 기능을 지원할 수 있습니다. 인터넷 주소를 사용하는 네트워크 소켓에는 파일 시스템 노드가 반드시 있는 것은 아닙니다.

FIFO와 유닉스 소켓 노드는 모두 하드웨어 드라이버를 선택하는 데 장치 주 번호와 부 번호를 사용하지 않습니다.

:::single-choice{#device-types-pipe-socket-distinction} 이 IPC 객체 유형을 올바르게 구분한 설명은 무엇입니까?

::option[`p`는 디스크 파티션을, `s`는 솔리드 스테이트 저장 장치를 나타냅니다.]{#device-types-storage-letters explanation="파티션은 일반적으로 블록 장치이며 이 문자들은 저장 기술을 나타내지 않습니다."}
::option[`p`는 FIFO를, `s`는 유닉스 도메인 소켓 노드를 나타냅니다.]{#device-types-p-and-s .correct explanation="이들은 로컬 프로세스 간 통신에 사용되는 서로 다른 파일 시스템 객체 유형입니다."}
::option[두 유형 모두 주 번호를 통해 커널 블록 드라이버를 식별합니다.]{#device-types-ipc-major explanation="FIFO와 소켓 노드는 문자 또는 블록 장치 노드가 아닙니다."}
:::

## 장치 주 번호와 부 번호

문자 및 블록 장치 노드는 주 번호와 부 번호로 나뉜 장치 번호를 저장합니다. 긴 목록에서는 이 번호가 일반 파일 크기 열을 대신합니다.

```text
brw-rw---- 1 root disk 8, 0 ... /dev/sda
```

이 번호 쌍은 노드가 어느 등록 장치 인터페이스와 인스턴스를 가리키는지 커널에 알려 줍니다. 주 번호는 드라이버 또는 장치 클래스와 연결되고, 부 번호는 드라이버가 해석합니다. “부 번호 0은 항상 첫 번째 드라이브를 뜻한다” 같은 가정을 하드 코딩하지 마십시오. 매핑은 하위 시스템과 커널 인터페이스에 따라 달라집니다.

다음 명령으로 유형과 장치 번호를 명시적으로 표시합니다.

```bash
$ stat -c 'type=%F major=%t minor=%T path=%n' /dev/null
```

GNU `stat`은 `%t`와 `%T` 값을 16진수로 표시합니다.

:::single-choice{#device-types-major-minor-scope} 커널 장치 인터페이스를 식별하는 데 주 번호와 부 번호를 사용하는 객체는 무엇입니까?

::option[모든 일반 파일과 디렉터리입니다.]{#device-types-all-files explanation="일반 파일은 장치 노드의 주 번호와 부 번호 쌍 대신 크기 및 파일 시스템 메타데이터를 사용합니다."}
::option[대상이 없는 심볼릭 링크만 해당합니다.]{#device-types-broken-symlinks explanation="심볼릭 링크는 경로 텍스트를 저장하며 대상이 없어도 장치 노드가 되지 않습니다."}
::option[문자 및 블록 장치 노드입니다.]{#device-types-device-number-nodes .correct explanation="이 특수 inode 메타데이터에는 드라이버 인터페이스로 전달되는 장치 번호가 들어 있습니다."}
:::

## 요약

이제 모든 특수 파일 시스템 유형을 하드웨어 장치로 오해하지 않고 해석할 수 있습니다.

1. `c`는 문자 장치 노드, `b`는 블록 장치 노드로 읽습니다.
2. `p`는 FIFO, `s`는 유닉스 도메인 소켓 노드로 읽습니다.
3. 주 번호와 부 번호는 장치 노드에만 연결합니다.
4. 원시 블록 장치 접근은 잠재적으로 파괴적인 작업으로 취급합니다.
