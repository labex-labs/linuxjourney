---
lesson_id: "kernel-logging"
course_id: "logging"
lang: "ko"
order_index: 4
title: "커널 로깅"
description: "dmesg와 journalctl로 현재 및 보존된 리눅스 커널 메시지를 조회하는 방법을 알아봅니다."
meta_title: "커널 로깅 - 로깅"
meta_description: "/var/log/kern.log와 dmesg를 포함한 리눅스 커널 로그를 살펴봅니다. 부팅 메시지와 하드웨어 드라이버 정보를 확인하고 시스템 문제를 해결하는 방법을 알아봅니다."
meta_keywords: "커널 로그, kern.log, /var/log/kern.log, 리눅스 커널 로그, dmesg, 리눅스 로깅, 부팅 메시지, 커널 이벤트"
---

커널은 부팅, 드라이버, 장치, 파일시스템, 네트워킹, 메모리 및 장애에 관한 메시지를 내보냅니다. 이러한 레코드는 저수준 증상을 설명할 수 있지만, 경고 문자열 하나만으로 하드웨어 결함이 입증되지는 않습니다.

## 커널 링 버퍼 읽기

`dmesg`는 커널 링 버퍼의 메시지를 읽습니다.

```bash
$ dmesg --human
```

버퍼의 용량은 유한하므로 새 메시지가 오래된 메시지를 덮어쓸 수 있습니다. 접근이 권한 있는 사용자로 제한될 수도 있습니다. 지원하는 구현체에서는 `dmesg --follow`로 새 커널 메시지를 추적할 수 있으며, 제한된 재현 작업이 끝나면 추적을 중지합니다.

:::single-choice{#kernel-log-ring-buffer-limit}
오래된 커널 이벤트가 현재 `dmesg` 출력에 없을 수 있는 이유는 무엇입니까?

::option[커널 이벤트는 한 글자만 담을 수 있기 때문입니다.]{#kernel-log-one-character explanation="커널 메시지는 일반적인 진단 텍스트와 메타데이터를 담을 수 있습니다."}
::option[`dmesg`가 표시한 모든 줄을 영구적으로 삭제하기 때문입니다.]{#kernel-log-display-deletes explanation="일반적인 읽기 작업은 표시한 커널 메시지를 모두 소비하지 않습니다."}
::option[유한한 링 버퍼에서 이벤트가 덮어써졌을 수 있기 때문입니다.]{#kernel-log-overwritten .correct explanation="메모리 내 버퍼는 제한된 양의 커널 메시지 데이터만 보존합니다."}
:::

## 읽기 쉬운 타임스탬프 사용하기

원시 커널 타임스탬프는 일반적으로 부팅 시점을 기준으로 합니다. `dmesg --ctime` 또는 `--human`은 실제 시각으로 렌더링할 수 있지만, 변환된 값은 시계 이력에 의존하며 부팅 후 시계가 변경됐다면 정확하지 않을 수 있습니다. 정확한 순서가 중요할 때는 부팅 기준 시간도 보존하십시오.

:::single-choice{#kernel-log-timestamp-caution}
변환된 `dmesg` 실제 시각을 주의해서 다뤄야 하는 이유는 무엇입니까?

::option[항상 다른 시스템의 시간을 나타내기 때문입니다.]{#kernel-log-other-machine explanation="로컬에서 계산되지만 시계 변경이 변환에 영향을 줄 수 있습니다."}
::option[변할 수 있는 시계에 부팅 기준 시간을 매핑하기 때문입니다.]{#kernel-log-clock-change .correct explanation="시간 동기화나 수동 시계 변경으로 렌더링된 실제 시각이 오해를 일으킬 수 있습니다."}
::option[시간 대신 파일시스템 여유 공간을 표시하기 때문입니다.]{#kernel-log-free-space explanation="타임스탬프 옵션은 저장 공간이 아니라 시간을 표시합니다."}
:::

## 영구 커널 레코드 조회하기

systemd 호스트에서 현재 부팅의 커널 레코드를 조회합니다.

```bash
$ journalctl -k -b
```

영구 저널 저장소가 이전 부팅을 보존했다면 부팅 목록을 확인하고 하나를 선택합니다.

```bash
$ journalctl --list-boots
$ journalctl -k -b -1
```

전통적인 syslog 라우팅은 `/var/log/kern.log`나 다른 파일을 만들 수 있지만 설정에 따라 다릅니다. 저장된 `/var/log/dmesg` 파일 역시 보편적이지 않으며 부팅 시점의 스냅샷만 나타낼 수 있습니다.

:::single-choice{#kernel-log-previous-boot}
보존된 이전 부팅의 커널 메시지를 요청하는 명령은 무엇입니까?

::option[`journalctl -u kernel -f`]{#kernel-log-unit-follow explanation="커널 메시지는 -k로 선택하며 추적 옵션은 이전 부팅을 선택하지 않습니다."}
::option[`dmesg --clear`]{#kernel-log-clear explanation="지우기 작업은 버퍼 상태를 바꾸며 이전 부팅을 검색하지 않습니다."}
::option[`journalctl -k -b -1`]{#kernel-log-previous .correct explanation="커널 필터와 부팅 오프셋 -1을 함께 사용하면 보존된 직전 부팅을 선택합니다."}
:::

## 커널 이벤트 조사하기

해당 시점의 부팅, 타임스탬프, 장치, 하위 시스템 및 수행 중이던 동작을 파악합니다. 주변 커널 및 서비스 레코드를 조회한 다음 하드웨어 목록과 현재 상태를 비교합니다.

```bash
$ journalctl -k -b --since '10 minutes ago'
$ lspci -k
$ lsblk
```

해당 하위 시스템과 관련 있는 도구만 사용하십시오. 드라이버를 다시 불러오거나 장치의 바인딩을 해제하거나 재부팅하기 전에 저장소, 네트워크, 콘솔 및 서비스에 미칠 영향을 평가하고 복구 접근 경로를 보존합니다.

:::single-choice{#kernel-log-warning-response}
커널 경고 한 줄에 대한 가장 좋은 대응은 무엇입니까?

::option[불러온 모든 드라이버를 즉시 언로드합니다.]{#kernel-log-unload-all explanation="중요 장치를 중단할 수 있으며 경고의 원인을 격리하지 못합니다."}
::option[전체 시스템을 교체해야 한다고 가정합니다.]{#kernel-log-replace-machine explanation="레코드 하나만으로는 그런 결론을 내릴 증거가 충분하지 않습니다."}
::option[주변 이벤트 및 현재 하위 시스템 상태와 연관 지어 분석합니다.]{#kernel-log-correlate .correct explanation="수정 작업을 선택하기 전에 맥락과 재현 가능한 영향을 확인해야 합니다."}
:::

## 요약

이제 현재 커널 버퍼의 메시지와 보존된 커널 로그를 구분할 수 있습니다.

1. `dmesg`로 유한한 링 버퍼를 읽습니다.
2. 부팅 기준 및 변환된 타임스탬프를 주의해서 해석합니다.
3. `journalctl -k`로 현재 또는 이전 부팅을 조회합니다.
4. 변경을 일으키는 작업 전에 커널 메시지를 다른 정보와 연관 지어 분석합니다.
