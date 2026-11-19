---
lesson_id: "linux-service-accounts"
course_id: "linux-hardening"
lang: "ko"
order_index: 2
title: "서비스 계정"
description: "Linux 프로세스가 어떤 계정으로 실행되는지 확인하고 해당 계정의 접근 권한을 파악하는 방법을 알아봅니다."
meta_title: "서비스 계정 - Linux 보안 강화"
meta_description: "Linux 프로세스가 어떤 계정으로 실행되는지 확인하고 해당 계정의 접근 권한을 파악하는 방법을 알아봅니다."
meta_keywords: "서비스 계정, Linux 보안 강화, 사이버 보안, Linux Journey"
---

웹 서버는 프로세스로 시작됩니다. Linux는 각 프로세스에 실행 주체를 연결하고, 이를 바탕으로 프로그램이 읽거나 변경할 수 있는 항목을 판단합니다. **서비스 계정**은 프로그램을 실행하기 위해 따로 마련한 계정입니다.

## 프로세스 실행 계정 확인하기

일반 터미널에서 `$$`는 셸의 프로세스 ID입니다. 이 값을 사용해 지금 쓰는 셸의 실행 계정을 확인할 수 있습니다. `-p` 옵션은 해당 프로세스를 선택하고 `-o`는 표시할 열을 지정합니다. 등호를 붙이면 열 제목을 생략합니다.

```bash
$ ps -p "$$" -o user=,comm=
```

LabEx 터미널에서는 계정이 `labex`일 수 있습니다. 명령 열에는 셸 프로그램의 이름이 나옵니다. 서비스를 누가 시작했든 서비스 프로세스의 같은 필드를 보면 어떤 계정으로 실행 중인지 알 수 있습니다.

:::single-choice{#linux-service-accounts-process-user} 선택한 프로세스의 실행 계정을 보여 주는 필드는 무엇인가요?

::option[-p에 전달한 프로세스 ID입니다.]{#linux-service-accounts-process-user-a explanation="프로세스 ID는 실행 중인 프로세스 하나를 선택합니다."}
::option[마지막 열의 명령 이름입니다.]{#linux-service-accounts-process-user-c explanation="이 열에는 실행 중인 프로그램의 이름이 표시됩니다."}
::option[ps가 출력한 사용자 필드입니다.]{#linux-service-accounts-process-user-b .correct explanation="사용자 필드에는 프로세스를 실행하는 계정이 표시됩니다."}
:::

![LabEx 셸 프로세스와 실행 계정 labex를 보여 주는 ps 출력](https://cdn.jsdelivr.net/gh/labex-labs/linuxjourney@master/images/lessons/linux-hardening/linux-service-accounts/shell-identity.png)

## 전용 계정 만들기

페이지를 읽고 자체 로그에 쓰기만 하는 웹 서비스를 생각해 보세요. 전용 `site-web` 계정에 그 두 권한을 줄 수 있습니다. 관리자 계정의 넓은 권한으로 실행하면 프로그램이 필요 이상으로 호스트를 변경할 수 있게 됩니다.

:::single-choice{#linux-service-accounts-isolate-service} 해당 서비스의 작업에 어떤 접근 계획이 맞나요?

::option[site-web이 모든 사용자의 파일을 수정하도록 허용합니다.]{#linux-service-accounts-isolate-service-b explanation="해당 서비스에는 그런 범위의 권한이 필요한 작업이 없습니다."}
::option[site-web이 페이지를 읽고 자체 로그에 쓰도록 허용합니다.]{#linux-service-accounts-isolate-service-a .correct explanation="이 권한은 앞서 설명한 두 작업에 필요합니다."}
::option[site-web이 모든 요청을 관리자 권한으로 처리하도록 허용합니다.]{#linux-service-accounts-isolate-service-c explanation="대부분의 요청은 서비스의 제한된 권한만으로 처리할 수 있습니다."}
:::

## 프로세스가 여러 개일 때 확인하기

서비스에 따라 역할별로 여러 프로세스를 사용합니다. 어느 권한이 적용되는지 설명하려면 요청을 실제로 처리하는 프로세스를 확인하세요. 실행 계정을 바꿨다면 서비스가 여전히 필요한 입력을 읽고 필요한 곳에만 쓸 수 있는지 확인합니다.

:::single-choice{#linux-service-accounts-verify-identity} 유지보수 도구에서 감독 프로세스의 계정이 root라고 표시합니다. 어떤 계정이 웹 요청을 처리하는지 알아보려면 무엇을 확인해야 하나요?

::option[요청을 처리하는 워커 프로세스의 실행 계정입니다.]{#linux-service-accounts-verify-identity-c .correct explanation="실제 작업을 수행하는 프로세스를 살펴보면 해당 작업에 사용되는 계정을 알 수 있습니다."}
::option[서비스 설정 파일의 이름만 확인합니다.]{#linux-service-accounts-verify-identity-a explanation="파일 이름으로는 워커의 실행 계정을 알 수 없습니다."}
::option[터미널을 연 사람의 이름을 확인합니다.]{#linux-service-accounts-verify-identity-b explanation="터미널 사용자와 서비스를 실행하는 계정은 다를 수 있습니다."}
:::

## 요약

이제 Linux 프로세스가 어느 계정으로 실행되는지 확인할 수 있습니다.

1. ps 출력에서 프로세스의 사용자를 찾습니다.
2. 서비스의 작업에 맞는 권한을 선택합니다.
3. 여러 프로세스로 동작하는 서비스에서는 해당 작업을 맡은 프로세스를 확인합니다.
