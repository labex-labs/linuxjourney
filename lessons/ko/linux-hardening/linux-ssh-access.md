---
lesson_id: "linux-ssh-access"
course_id: "linux-hardening"
lang: "ko"
order_index: 6
title: "SSH 접근"
description: "SSH 서버의 신원, 사용자 인증, 로그인 접근 정책을 구분하는 방법을 알아봅니다."
meta_title: "SSH 접근 - Linux 보안 강화"
meta_description: "SSH 서버의 신원, 사용자 인증, 로그인 접근 정책을 구분하는 방법을 알아봅니다."
meta_keywords: "SSH 접근, Linux 보안 강화, 사이버 보안, Linux Journey"
---

유지보수에 SSH를 사용하면 연결의 양쪽에서 확인할 사항이 있습니다. 클라이언트는 어느 서버에 연결했는지 확인해야 합니다. 서버는 해당 계정에 로그인 권한이 있는지 확인해야 합니다.

## 서버 신원 확인하기

SSH 서버는 **호스트 키**를 제시합니다. 클라이언트는 이 키를 해당 호스트에 대해 이미 알고 있는 키와 비교할 수 있습니다. 키가 예기치 않게 바뀌었다면 팀의 호스트 목록이나 신뢰할 수 있는 채널에서 연락한 유지보수 담당자 등 승인된 독립 출처를 통해 새 키를 확인하세요.

:::single-choice{#linux-ssh-access-unexpected-key} 클라이언트가 서버의 호스트 키가 바뀌었다고 알립니다. 무엇을 먼저 확인해야 하나요?

::option[신뢰할 수 있는 출처에서 새 호스트 키가 예상한 값인지 확인합니다.]{#linux-ssh-access-unexpected-key-b .correct explanation="연결을 신뢰하기 전에 서버의 신원을 검증할 수 있습니다."}
::option[하나가 될 때까지 사용자 이름을 여러 개 시도합니다.]{#linux-ssh-access-unexpected-key-a explanation="사용자 이름으로는 서버의 신원을 검증할 수 없습니다."}
::option[저장된 호스트 키를 모두 삭제하고 계속합니다.]{#linux-ssh-access-unexpected-key-c explanation="키가 바뀐 이유를 확인하기 전에 이미 알고 있던 신원 정보를 버리게 됩니다."}
:::

## 사용자의 접근 권한 확인하기

사용자 키로 클라이언트가 해당 계정으로 접속할 권한이 있음을 증명할 수 있습니다. 호스트 키는 서버가 어느 서버인지 확인하는 데 쓰입니다. 서버 정책으로 허용하는 계정과 인증 방식을 제한할 수 있습니다. 이 실습 예시에서 `ops`는 키 기반 인증으로 로그인합니다.

:::single-choice{#linux-ssh-access-distinguish-keys} 서버가 ops의 사용자 키를 검사할 때 누구의 신원을 확인하나요?

::option[공개 웹 페이지의 이름입니다.]{#linux-ssh-access-distinguish-keys-b explanation="웹 콘텐츠는 SSH 인증과 별개입니다."}
::option[자신의 신원을 증명하는 서버입니다.]{#linux-ssh-access-distinguish-keys-c explanation="서버 신원은 클라이언트가 호스트 키로 확인합니다."}
::option[ops로 로그인하려는 클라이언트입니다.]{#linux-ssh-access-distinguish-keys-a .correct explanation="사용자 인증은 클라이언트가 사용하려는 계정에 대한 확인입니다."}
:::

## 유지보수 경로 확보하기

승인된 SSH 정책 변경을 적용하기 전에 사용할 계정과 접근 방식을 합의하세요. 테스트 연결을 별도로 열고, 의도한 방식으로 로그인할 수 있을 때까지 기존 복구 경로를 유지하세요. 변경 후에도 이전에 열린 세션은 계속 유지되지만 새 로그인은 실패할 수 있습니다.

:::single-choice{#linux-ssh-access-test-new-login} 정책을 바꾼 뒤 기존 세션이 그대로 열려 있습니다. 유지보수 담당자가 여전히 로그인할 수 있는지 어떻게 확인하나요?

::option[ping 응답만 확인합니다.]{#linux-ssh-access-test-new-login-a explanation="네트워크 응답만으로는 SSH 인증이 성공했는지 알 수 없습니다."}
::option[의도한 계정과 방식으로 새로 승인된 SSH 세션을 엽니다.]{#linux-ssh-access-test-new-login-c .correct explanation="이후 로그인에 적용될 정책을 직접 검사합니다."}
::option[이전 세션을 유휴 상태로 유지합니다.]{#linux-ssh-access-test-new-login-b explanation="그 세션은 변경 전 조건에 따라 인증되었습니다."}
:::

## 요약

이제 SSH 유지보수에 사용하는 신원과 접근 방식을 확인할 수 있습니다.

1. 호스트 키로 서버의 신원을 검증합니다.
2. 서버 신원 확인과 사용자 인증을 구분합니다.
3. 변경 후 승인된 새 연결로 검증합니다.
