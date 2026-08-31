---
lesson_id: "kernel-overview"
course_id: "kernel"
lang: "ja"
order_index: 1
title: "カーネルの概要"
description: "Linux カーネルがハードウェア、リソース、分離、ユーザー空間からの要求を仲介する仕組みを学びます。"
meta_title: "カーネルの概要 - カーネル"
meta_description: "Linux カーネルの概要から Linux の旅を始めましょう。ハードウェアとユーザースペースの管理におけるその中核的な役割を理解することは、linuxjourney.com における基本的な概念です。"
meta_keywords: "Linux カーネル，オペレーティングシステム，ハードウェア，ユーザースペース，linuxjourney, linuxjourney.com, linuxjourney.com, linux ジャーニー, カーネル概要"
---

Linux は OS のカーネル、つまり processor、memory、device、process、共通の resource abstraction を管理する特権ソフトウェアです。完全な Linux システムには、user-space library、utility、service、shell、graphical software、distribution policy も含まれます。

## ハードウェアリソース

processor は instruction を実行し、memory は動作中の state を保存し、controller は storage、network、display、input device などの peripheral を接続します。ハードウェアが公開するのは architecture・device 固有の仕組みであり、すべてのアプリケーションが安全に使える単一 interface ではありません。

カーネルは architecture code と device driver を通じて、これらのリソースを初期化・制御します。interrupt、DMA coordination、timer、power-management event を処理しながら、workload 間のアクセス境界を強制します。

:::single-choice{#kernel-overview-hardware-manager}
Linux で device driver と hardware interrupt を通常調整する層はどれですか？

::option[各ユーザーの shell history file。]{#kernel-overview-shell-history explanation="history はコマンドを記録するもので、ハードウェア実行を処理しません。"}
::option[package repository index。]{#kernel-overview-repository-index explanation="repository metadata は software package を記述し、動作中の hardware event は扱いません。"}
::option[カーネル。]{#kernel-overview-kernel-layer .correct explanation="特権カーネルコードが hardware event と driver operation を、管理された system interface へ接続します。"}
:::

## カーネルの責務

主要な責務には次のものがあります。

- 実行可能な thread を CPU へ schedule する
- virtual address space を作成・分離する
- process credential、permission、security policy を強制する
- filesystem、networking、IPC、device interface を提供する
- signal、timer、process lifecycle を処理する
- resource を割り当て、計上し、回収する

Linux は、core service と多くの driver が一つの特権 kernel address space で動くため、一般に monolithic kernel と呼ばれます。同時に modular でもあり、対応する component を kernel module として load・unload できます。特権 kernel code の bug はシステム全体を危険にさらすため、kernel update と module provenance はセキュリティ上重要です。

:::single-choice{#kernel-overview-scheduler-role}
カーネル scheduler は何を管理しますか？

::option[ユーザーが次に読む documentation page。]{#kernel-overview-documentation explanation="学習ページの移動は kernel scheduling の対象外です。"}
::option[どの実行可能 thread に CPU 実行時間を与えるか。]{#kernel-overview-thread-scheduling .correct explanation="scheduler は policy、priority、affinity、CPU availability に従って実行 context を選びます。"}
::option[管理者がどの repository signing key を信頼すべきか。]{#kernel-overview-repository-key explanation="trust configuration は package-management policy に属します。"}
:::

## ユーザー空間

ユーザー空間には通常の process、つまり init と service、command-line tool、language runtime、database、shell、desktop application があります。hardware privilege により、これらの program は多くの機密 instruction を直接実行したり、任意の kernel memory へアクセスしたりできません。

process は system call を通じてカーネルへ処理を要求し、file descriptor、socket、device node、procfs、sysfs、netlink、memory mapping などの公開 interface とやり取りします。library がこれらを高水準 API で包むこともよくあります。

user-space root は policy 上大きな権限を持ちますが、通常は processor の user mode で実行されます。user identity と CPU privilege mode は別の概念です。

:::single-choice{#kernel-overview-root-user-mode}
通常の root 所有アプリケーションは、すべての instruction を kernel mode で実行しますか？

::option[はい。UID 0 が全 instruction を恒久的に ring 0 へ変えるからです。]{#kernel-overview-root-ring-zero explanation="通常の root process も user-space process のままです。"}
::option[はい。root application は自動的に loadable kernel module になるからです。]{#kernel-overview-root-module explanation="user executable が所有者 UID によって kernel code へ変換されることはありません。"}
::option[いいえ。通常は user mode で動き、管理された interface を通じて kernel へ入ります。]{#kernel-overview-root-userspace .correct explanation="root credential は認可に影響し、processor mode は kernel entry と execution の間だけ変化します。"}
:::

## 境界と抽象化

カーネルは生の物理機構を直接公開せず、virtual process、file、socket、address space を提示します。これらの abstraction は分離と移植性を支えますが、それだけで完全な security boundary になるわけではありません。namespace、cgroup、capability、security module、seccomp、virtualization が専用の制御を加えます。

トラブルシューティングでは、どの層が動作を所有するかを考えてください。application、library、system-call interface、filesystem、driver、kernel subsystem、firmware、hardware のいずれでしょうか。誤った層の証拠は、不適切な修正につながります。

:::single-choice{#kernel-overview-system-call-boundary}
system call とは何ですか？

::option[ユーザー空間から kernel service への管理された要求。]{#kernel-overview-controlled-request .correct explanation="processor が定義済み interface から kernel mode へ入り、カーネルが検証して操作を実行します。"}
::option[すべての access-control check を迂回する直接 command。]{#kernel-overview-bypass-checks explanation="system call は、まさに多くの validation と authorization check が行われる場所です。"}
::option[device driver を含む package archive。]{#kernel-overview-package-archive explanation="package は software を配布できますが、syscall は実行時 interface です。"}
:::

管理された環境でカーネルの modular な部分を観察するには、[Linux でカーネルモジュールを管理する](https://labex.io/labs/comptia-manage-kernel-modules-in-linux-590865)を利用できます。

## まとめ

これで、物理リソースと分離された user-space process の間にカーネルを位置付けられます。

1. driver と architecture code を hardware control と関連付ける。
2. scheduling、memory、security、filesystem、network の責務を識別する。
3. root credential と processor kernel mode を別の概念として扱う。
4. user-kernel interaction を管理された runtime interface に位置付ける。
