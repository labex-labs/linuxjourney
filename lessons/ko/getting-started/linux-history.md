---
lesson_id: "linux-history"
course_id: "getting-started"
lang: "ko"
order_index: 1
title: "리눅스 역사"
description: "UNIX, GNU, 리눅스 커널이 오늘날의 리눅스 시스템에 어떻게 기여했는지 배웁니다."
meta_title: "리눅스 역사 - 시작하기"
meta_description: "리눅스의 역사를 탐구하며 리눅스 여정을 시작하세요. UNIX 로부터의 기원, GNU 프로젝트, 리누스 토발즈의 리눅스 커널 개발에 대해 알아보세요."
meta_keywords: "리눅스 역사, 리눅스 연혁, 리눅스 입문, UNIX, GNU 프로젝트, 리누스 토발즈, 리눅스 커널, 초보자 리눅스"
---

**Linux Journey**에 오신 것을 환영합니다! 강력한 리눅스의 세계를 배우고 싶다면 잘 찾아오셨습니다. 저는 여러분의 안내자 Penguin Pete입니다. 먼저 **리눅스의 역사**를 간단히 살펴봅시다.

## 리눅스의 선구자들

리눅스가 만들어진 과정을 이해하려면 벨 연구소의 켄 톰슨과 데니스 리치가 UNIX 운영체제를 개발한 1969년으로 거슬러 올라가야 합니다. UNIX는 나중에 C 프로그래밍 언어로 다시 작성되었고, 그 덕분에 이식성이 높아져 널리 보급되었습니다.

![Unix 타임라인](https://file.labex.io/images/ed9c245d-e8be-4287-bf34-67750b042542.jpg)

:::single-choice{#understand-unix-portability} UNIX를 C로 다시 작성해 얻은 중요한 결과는 무엇인가요?

::option[GNU 시스템용 자유 커널이 되었습니다.]{#unix-became-gnu-kernel explanation="UNIX는 GNU 프로젝트보다 먼저 존재했으며 GNU의 커널이 아니었습니다. GNU는 나중에 Hurd라는 별도 커널을 개발하기 시작했습니다."}
::option[서로 다른 하드웨어 시스템으로 옮기기 쉬워졌습니다.]{#portable-across-hardware .correct explanation="UNIX를 C로 작성해 이식성이 높아졌고 원래 하드웨어 밖으로 널리 보급될 수 있었습니다."}
::option[벨 연구소에서만 쓰는 명령 쉘이 되었습니다.]{#unix-became-shell explanation="UNIX는 단순한 쉘이 아니라 운영체제입니다. C로 다시 작성한 덕분에 벨 연구소 밖에서도 채택되었습니다."}
:::

10여 년 뒤 리처드 스톨먼은 GNU 프로젝트를 시작했습니다. GNU는 "GNU's Not UNIX"의 재귀적 약자로, 완전히 자유롭고 오픈 소스인 UNIX 계열 운영체제를 만드는 것이 목표였습니다. GNU는 수많은 필수 구성 요소와 GNU 일반 공중 사용 허가서(GPL)를 만들었지만, 자체 커널인 GNU Hurd는 리눅스가 등장했을 때 일반 용도로 사용할 준비가 되지 않았습니다.

:::single-choice{#identify-gnu-missing-component} 리눅스가 등장했을 때 준비되지 않았던 GNU의 주요 구성 요소는 무엇인가요?

::option[실사용 가능한 커널]{#gnu-kernel .correct explanation="GNU는 여러 시스템 구성 요소를 만들었지만 자체 커널인 GNU Hurd는 일반 용도로 사용할 준비가 되지 않았습니다."}
::option[자유 소프트웨어 라이선스]{#gnu-license explanation="GNU 프로젝트는 이미 GNU 일반 공중 사용 허가서를 만들었습니다. 빠진 시스템 구성 요소는 사용할 수 있는 커널이었습니다."}
::option[필수 시스템 도구]{#gnu-tools explanation="GNU는 이미 여러 필수 도구를 만들었으며 커널이 시스템의 주요 미완성 부분으로 남아 있었습니다."}
:::

## 커널의 역할

커널은 운영체제의 핵심 구성 요소입니다. 하드웨어와 소프트웨어가 통신하도록 다리 역할을 하며 CPU, 메모리, 주변 장치 같은 시스템 자원을 관리합니다. 완전한 운영체제에는 사용자가 다루는 도구와 애플리케이션뿐 아니라 이 자원 관리 핵심이 필요합니다.

:::single-choice{#recognize-kernel-role} 운영체제 커널이 담당하는 일은 무엇인가요?

::option[쉘에 입력되는 모든 명령어를 작성합니다.]{#write-shell-commands explanation="쉘 명령어는 사용자나 스크립트가 제공합니다. 커널은 프로그램이 명령어를 실행할 때 필요한 저수준 자원을 제공합니다."}
::option[설치된 모든 애플리케이션의 라이선스를 선택합니다.]{#choose-software-licenses explanation="애플리케이션 라이선스는 소프트웨어 작성자와 배포자가 선택하며 커널의 자원 관리 작업이 아닙니다."}
::option[CPU, 메모리와 연결된 장치를 관리합니다.]{#manage-system-resources .correct explanation="커널은 하드웨어 자원을 관리해 소프트웨어가 사용하게 합니다. CPU 시간, 메모리, 장치가 대표적인 예입니다."}
:::

## 리눅스 커널의 탄생

1991년 핀란드 학생 리누스 토발즈는 개인 프로젝트로 새 커널을 개발하기 시작했습니다. 이 커널이 리눅스 커널이 되었습니다. 1992년에 리눅스가 자유 소프트웨어로 공개된 뒤 거의 완성된 GNU 시스템과 결합해 흔히 GNU/Linux라고 부르는 완전한 자유 운영체제를 만들 수 있었습니다. 이는 **리눅스 역사**의 중요한 전환점이었습니다.

![2018년의 리누스 토발즈](https://file.labex.io/images/3e1311fd-b8ca-45e7-8d02-9aac6377bb36.jpg)

_2018년의 리누스 토발즈 (출처: [Wikipedia](https://en.wikipedia.org/wiki/Linus_Torvalds))_

:::single-choice{#identify-linux-kernel-creator} 1991년에 리눅스 커널 개발을 시작한 사람은 누구인가요?

::option[리처드 스톨먼]{#richard-stallman explanation="리처드 스톨먼은 GNU 프로젝트를 시작했습니다. GNU가 여러 시스템 구성 요소를 제공했지만 리눅스 커널은 리누스 토발즈가 시작했습니다."}
::option[데니스 리치]{#dennis-ritchie explanation="데니스 리치는 UNIX와 C 프로그래밍 언어 개발에 기여했습니다. 리눅스 커널 프로젝트는 나중에 리누스 토발즈가 시작했습니다."}
::option[리누스 토발즈]{#linus-torvalds .correct explanation="리누스 토발즈는 1991년에 커널 프로젝트를 시작했고, 이 프로젝트가 리눅스 커널이 되었습니다."}
:::

**리눅스 여정**을 계속하려면 다음 실습에서 기본 명령어를 연습하며 커맨드 라인 환경에 익숙해져 보세요.

1. **[Linux 시작하기](https://labex.io/ko/labs/linux-getting-started-with-linux-446315)** - `echo`, `date` 같은 필수 터미널 명령어와 기본 계산법을 배우며 리눅스를 시작합니다.
2. **[첫 번째 Linux 실습](https://labex.io/ko/labs/linux-your-first-linux-lab-270253)** - 리눅스에서 고전적인 "Hello, World!" 프로그램과 기본 명령어를 익힙니다.
3. **[개인화된 터미널 인사말 만들기](https://labex.io/ko/labs/linux-create-personalized-terminal-greeting-446322)** - 기본 터미널 명령어로 자신만의 환영 메시지를 만듭니다.

## 요약

이제 UNIX, GNU, 리눅스 커널이 현대 리눅스 시스템에 어떻게 기여했는지 설명할 수 있습니다.

1. UNIX의 이식성이 중요했던 이유를 설명할 수 있습니다.
2. 커널이 GNU의 주요 미완성 구성 요소였음을 알 수 있습니다.
3. 시스템 자원을 관리하는 커널의 역할을 설명할 수 있습니다.
4. 리눅스 커널의 창시자가 리누스 토발즈임을 알 수 있습니다.
