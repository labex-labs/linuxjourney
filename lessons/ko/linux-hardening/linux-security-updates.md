---
lesson_id: "linux-security-updates"
course_id: "linux-hardening"
lang: "ko"
order_index: 7
title: "보안 업데이트"
description: "설치 가능한 패키지 업데이트를 검토하고 승인된 유지보수 후에 서비스를 확인하는 방법을 알아봅니다."
meta_title: "보안 업데이트 - Linux 보안 강화"
meta_description: "설치 가능한 패키지 업데이트를 검토하고 승인된 유지보수 후에 서비스를 확인하는 방법을 알아봅니다."
meta_keywords: "보안 업데이트, Linux 보안 강화, 사이버 보안, Linux Journey"
---

보안 업데이트는 설치된 소프트웨어의 결함을 바로잡을 수 있습니다. 먼저 설치된 버전과 운영체제에서 제공하는 수정 사항을 확인하세요. 사용자가 이용하는 서비스에 미칠 영향을 고려해 변경을 계획합니다.

## 설치 가능한 업데이트 확인하기

Ubuntu 실습 호스트에서 다음 읽기 전용 명령을 실행하면 APT가 업그레이드할 수 있다고 판단하는 패키지를 나열합니다. 이 명령은 호스트에 이미 있는 패키지 정보를 사용합니다.

```bash
$ apt list --upgradable
```

목록에 나온 패키지는 현재 패키지 정보에 더 새로운 후보 버전이 있다는 뜻입니다. 필요한 수정이 그 업데이트에 포함되어 있는지는 배포판의 보안 공지를 확인하세요. 패키지 정보가 오래되어도 목록이 비어 있을 수 있습니다.

:::single-choice{#linux-security-updates-candidate-is-listed} 이 목록에 패키지가 나옵니다. 무엇을 알 수 있나요?

::option[업데이트가 이미 적용되었습니다.]{#linux-security-updates-candidate-is-listed-a explanation="이 목록은 업그레이드할 수 있는 후보를 보여 줍니다."}
::option[APT가 설치된 패키지보다 새 후보 버전을 알고 있습니다.]{#linux-security-updates-candidate-is-listed-b .correct explanation="현재 로컬 패키지 정보에 나타난 결과입니다."}
::option[새 후보 버전은 모두 보안 업데이트입니다.]{#linux-security-updates-candidate-is-listed-c explanation="업데이트가 제공된 이유는 배포판의 공지를 확인하세요."}
:::

## 변경 계획 세우기

승인된 변경에는 서비스, 목표 버전, 유지보수 시간대를 명시해야 합니다. 일부 업데이트는 서비스를 다시 시작하거나 호스트를 재부팅해야 적용됩니다. 호스트를 변경하기 전에 검증에 사용할 요청과 복구 방법을 정하세요.

:::single-choice{#linux-security-updates-reboot-check} 패키지 업데이트로 오래 실행 중인 서비스가 사용하는 코드가 수정됩니다. 설치 후 무엇을 확인해야 하나요?

::option[업데이트된 코드를 사용하려면 서비스를 다시 시작해야 하는지 확인합니다.]{#linux-security-updates-reboot-check-a .correct explanation="실행 중인 프로세스에는 여전히 이전 코드가 로드되어 있을 수 있습니다."}
::option[설치 전에 패키지 목록에 업데이트가 나왔는지 확인합니다.]{#linux-security-updates-reboot-check-b explanation="설치 가능 여부는 유지보수 계획에 도움이 됩니다. 프로세스에 어떤 버전이 로드되어 있는지는 따로 확인해야 합니다."}
::option[패키지 목록에 더 이상 업그레이드할 항목이 없는지 확인합니다.]{#linux-security-updates-reboot-check-c explanation="패키지 목록이 최신이어도 프로세스가 업데이트된 코드를 다시 로드하지 않았을 수 있습니다."}
:::

## 결과 검증하기

설치된 버전이 승인된 목표 버전과 일치하는지 확인하세요. 사용자가 접속하는 경로에서 서비스를 검사하고 결과를 기록하세요. 실행 중인 구성 요소를 수정했다면 업데이트된 버전이 실제로 사용되는지도 확인합니다.

:::single-choice{#linux-security-updates-security-verification} 서비스 업데이트를 완료했다고 판단할 가장 좋은 근거 두 가지는 무엇인가요?

::option[목록을 보는 명령이 두 번 실행됩니다.]{#linux-security-updates-security-verification-a explanation="목록을 반복해서 출력해도 서비스가 동작하는지는 알 수 없습니다."}
::option[유지보수 티켓의 제목이 바뀌었습니다.]{#linux-security-updates-security-verification-b explanation="제목은 실행 상태를 보여 주지 않습니다."}
::option[승인된 버전이 사용 중이고 대표 요청이 성공합니다.]{#linux-security-updates-security-verification-c .correct explanation="소프트웨어 상태와 사람들이 이용하는 서비스의 동작을 모두 검증합니다."}
:::

## 두 가지 버전 정보 읽기

설치된 패키지와 요청을 처리하는 프로그램은 일시적으로 서로 다른 버전일 수 있습니다. 예를 들어 패키지 목록에 수정 버전이 표시되어도 업데이트 전에 시작한 프로세스가 계속 실행 중일 수 있습니다. 실행 중인 프로세스를 확인한 뒤 검토를 마무리하세요.

:::single-choice{#linux-security-updates-final-application} 설치된 버전에는 수정 사항이 반영되었지만 이전 프로세스가 남아 있습니다. 무엇을 더 확인해야 하나요?

::option[장비의 다른 모든 프로세스도 교체해야 하는지 확인합니다.]{#linux-security-updates-final-application-c explanation="확인할 대상은 업데이트한 서비스와 승인된 유지보수 요구 사항입니다."}
::option[업데이트된 프로그램이 실제로 요청을 처리하는지 확인합니다.]{#linux-security-updates-final-application-a .correct explanation="패키지 목록은 설치된 파일을 확인하는 데 쓰이고, 프로세스 검사는 현재 동작하는 서비스를 확인하는 데 쓰입니다."}
::option[업데이트 패키지가 있었는지 확인합니다.]{#linux-security-updates-final-application-b explanation="설치된 패키지에 이미 수정된 버전이 표시됩니다."}
:::

## 요약

이제 업데이트 후보를 확인하고 결과를 검증하기까지의 과정을 살펴볼 수 있습니다.

1. 설치 가능한 업데이트와 이미 적용한 변경을 구분합니다.
2. 계획에 재시작과 복구 방법을 포함합니다.
3. 실행 중인 버전과 서비스가 예상대로 동작하는지 확인합니다.
