---
index: 5
lang: "ko"
title: "인증 로깅"
meta_title: "인증 로깅 - 로깅"
meta_description: "/var/log/auth.log 파일을 검토하여 Linux 인증 로깅을 살펴보세요. 이 가이드는 초보자가 사용자 로그인 이벤트, 인증 방법 및 액세스 문제를 해결하여 Linux 보안을 개선하는 방법을 이해하도록 돕습니다."
meta_keywords: "Linux 인증, auth.log, Linux 로깅, 사용자 로그인, Linux 보안, 시스템 권한 부여, 로그인 문제 해결, 인증 방법, 초보자, 튜토리얼, 가이드, 보안 로그"
---

## Lesson Content

Linux 에서는 누가, 어떻게 시스템에 접근하는지 추적하는 것이 보안 및 문제 해결에 매우 중요합니다. 이 과정은 사용자 로그인 및 사용된 방법과 같은 모든 권한 부여 관련 이벤트를 기록하는 인증 로깅을 통해 관리됩니다.

### auth.log 파일

Ubuntu 와 같은 Debian 기반 시스템에서는 이 활동을 추적하는 주요 파일은 `/var/log/auth.log`입니다. 이 로그 파일에는 성공 및 실패한 사용자 로그인 시도와 트리거된 모든 인증 메커니즘을 포함한 시스템 권한 부여 정보가 들어 있습니다. 이 파일을 검토하는 것은 로그인 문제를 진단하거나 보안 사고를 조사하는 핵심 단계입니다.

다음은 `auth.log` 파일의 샘플 조각입니다.

```plaintext
Jan 31 10:37:50 icebox pkexec: pam_unix(polkit-1:session): session opened for user root by (uid=1000)
```

### 로그 항목 이해하기

로그의 각 줄은 유용한 세부 정보를 제공합니다. 위의 예에서:

- **`Jan 31 10:37:50`**: 이벤트 발생 시간입니다.
- **`icebox`**: 이벤트가 발생한 머신의 호스트 이름입니다.
- **`pkexec`**: 이벤트를 시작한 프로그램입니다.
- **`pam_unix(polkit-1:session)`**: 사용된 인증 모듈 및 서비스입니다.
- **`session opened for user root by (uid=1000)`**: 수행된 작업—UID 가 `1000`인 사용자에 의해 `root` 사용자에 대한 세션이 열렸습니다.

### 대체 로그 파일

인증 로그의 위치는 Linux 배포판마다 다를 수 있다는 점에 유의해야 합니다. 예를 들어, CentOS 및 Fedora 와 같은 Red Hat 기반 시스템에서는 이러한 이벤트가 일반적으로 `/var/log/auth.log` 대신 `/var/log/secure`에 기록됩니다.

## Exercise

연습이 완벽을 만듭니다! 사용자 인증 및 계정 관리에 대한 이해를 강화하기 위한 실습 랩이 있습니다.

1. **[Linux 에서 사용자 계정 및 Sudo 권한 구성](https://labex.io/ko/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - 암호 정책 적용, 사용자 계정 잠금/잠금 해제, root 계정 보안 강화, 관리 권한 부여 연습. 이 모든 것은 인증 보안을 이해하는 데 중요합니다.

이 랩들은 실제 시나리오에 개념을 적용하고 Linux 사용자 및 보안 관리에 대한 자신감을 구축하는 데 도움이 될 것입니다.

## Quiz Question

Debian 기반 시스템에서 사용자 인증에 사용되는 로그 파일의 이름은 무엇입니까? 파일 이름만 사용하여 답변하십시오. 대소문자를 구분합니다.

## Quiz Answer

auth.log
