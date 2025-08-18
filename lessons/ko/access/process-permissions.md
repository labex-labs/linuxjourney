---
lang: "ko"
title: "프로세스 권한"
meta_description: "Linux 프로세스 권한에 대해 알아보세요. 실제, 유효, 저장된 사용자 ID 를 포함합니다. UID 가 보안 및 명령 실행에 미치는 영향을 이해하세요. 오늘 학습을 시작하세요!"
meta_keywords: "Linux 프로세스 권한, 실제 UID, 유효 UID, 저장된 UID, Linux 보안, passwd 명령, Linux 튜토리얼, 초보자 Linux"
---

## Lesson Content

잠시 프로세스 권한에 대해 이야기해 봅시다. SUID 권한 비트가 활성화된 `passwd` 명령을 실행하면 root 로 프로그램이 실행된다고 말씀드렸던 것을 기억하시나요? 맞습니다. 하지만 일시적으로 root 권한을 얻었으니 다른 사용자의 비밀번호를 수정할 수 있다는 의미일까요? 아닙니다, 다행히도 그렇지 않습니다!

이는 Linux 가 구현하는 여러 UID 때문입니다. 모든 프로세스에는 세 가지 UID 가 연결되어 있습니다:

프로세스를 시작하면 해당 프로세스를 실행한 사용자 또는 그룹과 동일한 권한으로 실행됩니다. 이를 **유효 사용자 ID(effective user ID)**라고 합니다. 이 UID 는 프로세스에 접근 권한을 부여하는 데 사용됩니다. 따라서 Bob 이 `touch` 명령을 실행했다면, 프로세스는 Bob 으로 실행되고 그가 생성한 모든 파일은 그의 소유가 될 것입니다.

또 다른 UID 는 **실제 사용자 ID(real user ID)**입니다. 이는 프로세스를 시작한 사용자의 ID 입니다. 이들은 프로세스를 시작한 사용자가 누구인지 추적하는 데 사용됩니다.

마지막 UID 는 **저장된 사용자 ID(saved user ID)**입니다. 이는 프로세스가 유효 UID 와 실제 UID 사이를 전환할 수 있도록 하며, 그 반대도 가능합니다. 이는 프로세스가 항상 상승된 권한으로 실행되기를 원하지 않기 때문에 유용합니다. 특정 시점에 특별 권한을 사용하는 것이 좋은 관행입니다.

이제 `passwd` 명령을 다시 살펴보면서 이 모든 것을 종합해 봅시다.

`passwd` 명령을 실행할 때, 유효 UID 는 사용자 ID 입니다. 예를 들어, 지금은 500 이라고 가정해 봅시다. 아, 하지만 잠시만요, `passwd` 명령에는 SUID 권한이 활성화되어 있다는 것을 기억하세요. 따라서 이 명령을 실행하면 유효 UID 는 이제 0 이 됩니다 (0 은 root 의 UID 입니다). 이제 이 프로그램은 root 로서 파일에 접근할 수 있습니다.

만약 당신이 약간의 권력을 맛보고 Sally 의 비밀번호를 수정하고 싶다고 가정해 봅시다. Sally 는 UID 600 을 가지고 있습니다. 음, 당신은 운이 없을 것입니다. 다행히도 프로세스에는 당신의 실제 UID, 이 경우 500 이 있습니다. 프로세스는 당신의 UID 가 500 이라는 것을 알고 있으므로 UID 600 의 비밀번호를 수정할 수 없습니다. (물론, 당신이 머신의 슈퍼유저이고 모든 것을 제어하고 변경할 수 있다면 이것은 항상 우회됩니다).

`passwd`를 실행했으므로, 프로세스는 당신의 실제 UID 를 사용하여 시작하고 파일 소유자 (유효 UID) 의 UID 를 저장하여 두 UID 사이를 전환할 수 있습니다. 필요하지 않다면 root 접근 권한으로 모든 파일을 수정할 필요가 없습니다.

대부분의 경우 실제 UID 와 유효 UID 는 동일하지만, `passwd` 명령과 같은 경우에는 변경됩니다.

## Exercise

아직 프로세스에 대해 논의하지 않았지만, 이 변경 사항이 실시간으로 발생하는 것을 여전히 확인할 수 있습니다:

1. Open one terminal window and run the command: `watch -n 1 "ps aux | grep passwd"`. This will watch for the `passwd` process.
2. Open a second terminal window and run: `passwd`.
3. Look at the first terminal window; you'll see a process come up for `passwd`. The first column in the process table is the effective user ID. Lo and behold, it's the root user!

## Quiz Question

어떤 UID 가 접근 권한을 부여할지 결정합니까?

## Quiz Answer

effective
