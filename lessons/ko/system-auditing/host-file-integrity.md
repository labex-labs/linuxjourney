---
lesson_id: "host-file-integrity"
course_id: "system-auditing"
lang: "ko"
order_index: 3
title: "파일 무결성"
description: "해시와 메타데이터를 사용해 파일 내용과 권한을 비교하는 방법을 알아봅니다."
meta_title: "파일 무결성 - 시스템 감사"
meta_description: "해시와 메타데이터를 사용해 파일 내용과 권한을 비교하는 방법을 알아봅니다."
meta_keywords: "파일 무결성, 시스템 감사, 사이버 보안, Linux Journey"
---

무결성 검사는 파일이 여전히 기준과 일치하는지 확인하는 작업입니다. 내용과 메타데이터를 각각 확인하세요. 내용은 파일에 들어 있는 바이트입니다. **메타데이터**에는 접근 권한 같은 정보가 포함됩니다.

## 내용 해시 기록하기

빈 실습 폴더에서 작은 설정 파일을 만드세요. 리디렉션은 이름이 같은 기존 파일을 덮어쓰므로 새 폴더를 사용합니다.

```bash
$ printf '%s\n' 'mode=preview' > site.conf
$ sha256sum site.conf
```

첫 번째 필드는 **해시**입니다. 파일의 바이트로 계산한 고정 길이 값입니다. 나중에 같은 파일에 같은 방법을 사용하세요. 해시가 달라지면 입력 바이트가 달라졌다는 뜻입니다.

:::single-choice{#host-file-integrity-changed-hash} 파일을 편집한 뒤 SHA-256 값이 바뀌었습니다. 비교 결과가 무엇을 보여 주나요?

::option[파일의 내용이 이전에 측정한 바이트와 다릅니다.]{#host-file-integrity-changed-hash-a .correct explanation="계산에 사용하는 내용이 달라지면 해시도 바뀝니다."}
::option[편집 작업은 반드시 승인되지 않은 변경이었습니다.]{#host-file-integrity-changed-hash-b explanation="승인 여부는 별도로 확인해야 합니다."}
::option[어떤 계정의 권한이 확실히 바뀌었습니다.]{#host-file-integrity-changed-hash-c explanation="내용 해시에는 권한이 기록되지 않습니다."}
:::

## 파일 권한 기록하기

Linux에서 `stat -c`는 선택한 메타데이터를 출력합니다. `%a`는 권한 모드를 숫자로, `%n`은 파일 이름을 출력합니다.

```bash
$ stat -c '%a %n' site.conf
```

처음의 모드는 파일을 어떻게 만들었는지에 따라 달라질 수 있습니다. 나중에 두 속성을 모두 비교할 수 있도록 내용 해시와 함께 기록하세요.

:::single-choice{#host-file-integrity-mode-vs-content} 해시는 기준과 일치하고 stat은 다른 모드를 표시합니다. 이 검사 결과에 따르면 무엇이 바뀌었나요?

::option[파일의 바이트가 바뀌었고 모드는 그대로입니다.]{#host-file-integrity-mode-vs-content-a explanation="해시는 일치하고 모드가 다릅니다."}
::option[파일이 반드시 삭제되었습니다.]{#host-file-integrity-mode-vs-content-c explanation="두 검사 모두 해당 파일의 정보를 반환했습니다."}
::option[권한이 바뀌었고 관찰한 내용 해시는 그대로입니다.]{#host-file-integrity-mode-vs-content-b .correct explanation="두 도구는 서로 다른 속성을 측정합니다."}
:::

## 모드 변경 검사하기

다음 명령은 실습용 파일의 권한을 `640`으로 바꿉니다. 소유자에게는 읽기와 쓰기 권한을, 그룹에는 읽기 권한을 부여합니다. 두 검사를 다시 실행해 결과를 비교하세요.

```bash
$ chmod 640 site.conf
$ stat -c '%a %n' site.conf
$ sha256sum site.conf
```

모드는 640으로 표시되고 내용 해시는 처음 측정값과 일치해야 합니다.

:::single-choice{#host-file-integrity-repeat-check} 나중에 파일 안의 mode=preview를 바꿨다면 어느 검사에서 변경을 감지할 수 있나요?

::option[stat으로 확인한 파일 이름만 봅니다.]{#host-file-integrity-repeat-check-a explanation="내용을 편집해도 이름은 그대로일 수 있습니다."}
::option[SHA-256을 다시 계산해 처음 값과 비교합니다.]{#host-file-integrity-repeat-check-c .correct explanation="내용이 바뀌면 해시가 달라집니다."}
::option[소유자 권한에 해당하는 숫자만 봅니다.]{#host-file-integrity-repeat-check-b explanation="대부분의 내용 편집은 권한 변경과 별개입니다."}
:::

![내용 해시가 유지된 상태에서 권한 모드가 640으로 바뀐 LabEx 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/system-auditing/host-file-integrity/mode-vs-content.png)

## 요약

이제 파일 내용과 접근 권한을 각각 비교할 수 있습니다.

1. SHA-256 내용 해시를 기록합니다.
2. stat으로 모드를 읽습니다.
3. 권한 변경의 결과를 확인합니다.
