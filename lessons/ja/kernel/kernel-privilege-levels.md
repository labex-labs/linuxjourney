---
lesson_id: "kernel-privilege-levels"
course_id: "kernel"
lang: "ja"
order_index: 2
title: "権限レベル"
description: "processor privilege がユーザー実行と信頼されたカーネル実行を分離する仕組みを学びます。"
meta_title: "権限レベル - カーネル"
meta_description: "Linux の権限レベルの核となる概念を探ります。このレッスンでは、カーネルモードとユーザモードの違い、保護リングの役割、システムコールがハードウェアへの特権アクセスをどのように提供するかを解説します。カーネルがセキュリティとカーネル権限を管理する方法を理解しましょう。"
meta_keywords: "Linux 権限レベル，カーネルモード，ユーザモード，保護リング，システムコール，特権アクセス，カーネル権限，カーネルモードとユーザモードの違い，Linux セキュリティ"
---

processor は、機密性の高い instruction と memory access を制限する privilege mode を提供します。Linux はこの hardware boundary を使い、通常の application failure が kernel memory を直接上書きしたり、device を再設定したりできないようにします。privileged execution への遷移はカーネルが制御します。

## User Mode

通常の process は、自身の virtual address space 内で user mode として実行されます。自由に計算でき、カーネルが許可した memory mapping へアクセスできます。その範囲は大きくなり得るため、user mode は「少量の memory しか使えない」という意味ではありません。任意の physical memory、別 process の private mapping、privileged processor control へ直接アクセスすることはできません。

page table と protection bit が memory access を強制します。thread が無効または許可されない address を参照すると、processor は kernel へ trap し、カーネルが有効な page fault を解決するか、`SIGSEGV` などの signal を配送します。

:::single-choice{#kernel-privilege-user-mode-memory}
user-mode process が通常直接アクセスできる memory はどれですか？

::option[すべての physical RAM address と kernel memory。]{#kernel-privilege-all-physical explanation="そのようなアクセスは privilege と virtual-memory protection によって防がれます。"}
::option[process 起動時に選ばれた一つの固定 byte だけ。]{#kernel-privilege-one-byte explanation="非特権のままでも、多数の mapped region を持てます。"}
::option[自身の virtual address space 内で許可された mapping。]{#kernel-privilege-own-mappings .correct explanation="hardware page protection により、適切な access で確立された mapping だけに制限されます。"}
:::

## Kernel Mode

kernel mode では、memory management、scheduling、interrupt handling、driver に必要な privileged instruction の実行と、保護された kernel mapping へのアクセスができます。x86 での Linux の分離は、通常 kernel を ring 0、user process を ring 3 と説明します。Linux は通常、process の一般的な分離に ring 1 と 2 を使いません。

ほかの architecture は exception level など、異なる名前と仕組みを使います。virtualization が加わると、hypervisor と guest の関係は単純な二つの ring の図に収まりません。重要なのは x86 の ring 番号そのものではなく、管理された privilege です。

:::single-choice{#kernel-privilege-x86-kernel-ring}
Linux カーネルを通常実行する x86 protection ring はどれですか？

::option[Ring 3。]{#kernel-privilege-ring-three explanation="Ring 3 は慣例的な user-mode privilege level です。"}
::option[Ring 0。]{#kernel-privilege-ring-zero .correct explanation="カーネルは従来の x86 で最も privilege の高い ring を使います。"}
::option[Ring 7。]{#kernel-privilege-ring-seven explanation="従来の x86 protection ring は 0 から 3 までです。"}
:::

## 管理された遷移

いくつかの event が control を kernel entry point へ移します。

- system-call instruction が kernel service を要求する
- exception が page fault や invalid instruction などの状態を報告する
- hardware interrupt が外部 event を報告する

processor は execution context を保存し、設定済み entry mechanism に従って privilege を変え、信頼された kernel code の実行を始めます。カーネルは要求と state を検証し、処理を実行または拒否して、適切な場合は user mode へ戻ります。

application が一時的に kernel code になるわけではありません。CPU がその thread に代わって kernel handler を実行し、kernel が制御する stack と mapping を使います。

:::single-choice{#kernel-privilege-system-call-transition}
system-call transition 中に何が起きますか？

::option[application の user code が制限なしの ring 0 execution を得る。]{#kernel-privilege-user-ring-zero explanation="管理された entry の後に実行されるのは、信頼された kernel code だけです。"}
::option[process の UID が恒久的に 0 へ変わる。]{#kernel-privilege-uid-zero explanation="processor mode の遷移は user credential を書き換えません。"}
::option[要求を検証する定義済み kernel handler へ control が入る。]{#kernel-privilege-kernel-handler .correct explanation="processor は設定済み entry path から mode を変え、return 用の user context を保持します。"}
:::

## CPU Privilege と User Identity は別物

Linux user `root` として動く application も通常は user mode で実行されます。UID 0 はカーネルの authorization check に影響しますが、instruction が kernel memory へ直接アクセスできるようにはしません。逆に、kernel code はどのユーザーの system call が原因でも privileged mode で動きます。

capability、namespace、seccomp、security module、cgroup は process が要求できる内容をさらに制限します。この階層型 policy は、hardware の user/kernel mode boundary とは別です。

:::single-choice{#kernel-privilege-root-distinction}
root identity と kernel mode の比較として正しいものはどれですか？

::option[root は user-space credential、kernel mode は processor execution privilege。]{#kernel-privilege-credential-versus-mode .correct explanation="root process は user mode から許可済み要求を行い、信頼された kernel code が privileged execution を行います。"}
::option[root 所有の全 instruction は loadable kernel code として動く。]{#kernel-privilege-root-kernel-code explanation="UID ownership によって executable が kernel module へ変わることはありません。"}
::option[kernel mode は `/etc/passwd` に保存される別の username。]{#kernel-privilege-kernel-username explanation="processor mode は hardware state であり、login account ではありません。"}
:::

## 境界が重要な理由

この境界は通常の bug による被害を限定し、access check を行う地点を提供しますが、kernel vulnerability と malicious module は境界を破れます。信頼された経路で kernel と firmware を更新し、privileged code を最小化し、信頼できない module を読み込まないでください。

speculative-execution issue と side channel も、hardware isolation に継続的な mitigation が必要だと示します。「異なる ring」は土台であって、完全な security proof ではありません。

:::single-choice{#kernel-privilege-boundary-limit}
user/kernel mode の分離はシステム全体のセキュリティを保証しますか？

::option[はい。kernel vulnerability が user process へ影響することはないからです。]{#kernel-privilege-no-kernel-vulns explanation="kernel vulnerability はシステム全体を危険にさらす可能性があります。"}
::option[いいえ。privileged-code flaw と side channel が意図した境界を越える場合があります。]{#kernel-privilege-not-complete .correct explanation="mode split は attack surface を減らしますが、正しい kernel code と追加 mitigation の組み合わせが必要です。"}
::option[はい。hardware mode によって access-control policy は不要だからです。]{#kernel-privilege-no-policy explanation="許可された resource sharing には credential と security policy が引き続き不可欠です。"}
:::

## まとめ

これで、hardware execution privilege と Linux account authority を区別できます。

1. user mode を保護された virtual address space と関連付ける。
2. kernel mode を privileged instruction と mapping に関連付ける。
3. system call、exception、interrupt を管理された entry として扱う。
4. UID 0 authorization と ring 0 execution を分離する。
5. privilege mode を、より広い security design の一層として捉える。
