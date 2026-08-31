---
lesson_id: "system-calls"
course_id: "kernel"
lang: "ja"
order_index: 3
title: "システムコール"
description: "ユーザー空間コードが Linux カーネルサービスを呼び出し、`strace` で安全に call を調べる方法を学びます。"
meta_title: "システムコール - カーネル"
meta_description: "Linux におけるシステムコールの基礎を探ります。ユーザースペースのプロセスが、カーネルサービスのリクエスト、モード切り替え、システムコールテーブルの仕組みのためにシステムコール（syscall）をどのように使用するかを学びます。`strace`を使用して、動作中のシステムコールを確認しましょう。"
meta_keywords: "システムコール linux, システムコール，システムコールテーブル，カーネルモード，ユーザモード，strace, linux カーネル，syscall API"
---

system call はカーネルへの定義済み entry で、user-space code は file の open、memory の map、process の作成、network data の送信などを要求します。カーネルは処理前に argument、credential、object state、security policy を検証します。

## Library と System-Call ABI

application は architecture 固有の entry instruction を直接書かず、通常は C library function を呼びます。library wrapper は system-call ABI に従って register と memory を準備し、カーネルへ入り、結果を language-level の規約へ変換します。

function と syscall は、常に一対一ではありません。

- 一つの library function が複数の system call を組み合わせる場合がある
- 完全にユーザー空間で動く function もある
- 最適化された vDSO function は、完全な mode transition なしに一部の kernel-maintained data を得られる
- 一つの system call が多数の高水準 API を支える場合がある

:::single-choice{#system-calls-library-wrapper}
一般的な libc の system-call wrapper は何をしますか？

::option[ABI argument を準備し、カーネルへ入り、結果を変換する。]{#system-calls-wrapper-role .correct explanation="wrapper は architecture 固有の calling convention を通常の library interface の背後へ隠します。"}
::option[application に kernel memory への無制限アクセスを与える。]{#system-calls-wrapper-unrestricted explanation="kernel entry は引き続き管理され、要求を検証します。"}
::option[function が呼ばれるたびにカーネルを再 compile する。]{#system-calls-wrapper-compile explanation="runtime call は、すでに動作しているカーネルを使います。"}
:::

## カーネルへの Entry と Return

wrapper は system-call number と argument を architecture 定義の場所へ置き、x86-64 の `syscall` や AArch64 の `svc` などの entry instruction を実行します。processor は設定済み privileged entry point へ切り替わり、カーネルが要求を dispatch します。

完了後、カーネルは値または error indication を返します。C library wrapper は error 時に通常 `-1` を返し、thread-local の `errno` を設定します。ほかの language と runtime は異なる error type を公開します。

現在の architecture で全 entry を「software interrupt」と呼ぶのは不正確です。trap、fast system-call instruction、supervisor call は関連する管理済み遷移を別の方法で実装します。

:::single-choice{#system-calls-entry-result}
system call の argument と authorization を検証するのは誰ですか？

::option[process 起動前の shell prompt。]{#system-calls-shell-validates explanation="process は shell なしでも syscall を行え、kernel check は引き続き必要です。"}
::option[要求された service の kernel implementation。]{#system-calls-kernel-validates .correct explanation="privileged handler が pointer、object state、credential、policy を確認してから処理します。"}
::option[disk partition table。]{#system-calls-partition-validates explanation="storage layout metadata は任意の kernel service を認可しません。"}
:::

## 番号と互換性

system-call number と calling convention は architecture 固有です。同じ symbolic call でも、別の ABI では番号や structure layout が異なる場合があります。kernel release は system call を追加できますが、安定した user-space ABI は既存動作を維持することを目指します。

非特権 process は、動作中カーネルの syscall table へ任意の新規 handler を挿入できません。interface の拡張には kernel code と慎重な ABI design が必要です。seccomp などの機能は process が使える call を filter できますが、新しい kernel implementation は作りません。

:::single-choice{#system-calls-number-portability}
別 architecture の syscall number を application が hard-code すべきでないのはなぜですか？

::option[number と calling convention が ABI 固有だから。]{#system-calls-abi-specific .correct explanation="一つの architecture で意味のある番号が、別の operation を示したり、別環境には存在しなかったりします。"}
::option[system call の名前が現在の作業ディレクトリから決まるから。]{#system-calls-directory-names explanation="pathname は syscall numbering ABI を定義しません。"}
::option[全 process が起動時に無作為な syscall table を受け取るから。]{#system-calls-random-table explanation="動作中カーネルの ABI は architecture に対して安定しており、process ごとに randomize されません。"}
:::

## `strace` で Trace する

単純な command を trace し、出力を別ファイルへ保存します。

```bash
$ strace -o trace.log -- ls
```

許可された範囲で child process を追うには `-f`、出力を絞るには次のような expression を使います。

```bash
$ strace -f -e trace=%file -o trace.log -- command
```

`strace` は path、argument、environment 由来データ、network address、file content の断片、argument を通じて誤って渡した credential を露出する場合があります。trace は厳しい権限で保存し、incident-data policy に従って削除してください。

:::single-choice{#system-calls-strace-purpose}
`strace` が主に観測するものは何ですか？

::option[application 内で実行された source-code line だけ。]{#system-calls-strace-source-lines explanation="source-level tracing には symbol を持つ debugger や instrumentation が必要です。"}
::option[user-kernel boundary の system call と signal。]{#system-calls-strace-boundary .correct explanation="trace 対象 process の要求、argument、結果、signal event を報告します。"}
::option[各 CPU core の物理電圧。]{#system-calls-strace-voltage explanation="hardware telemetry は syscall tracing の対象外です。"}
:::

## Trace を慎重に解釈する

tracing は timing を変え、大きな overhead を生む場合があります。失敗 call が想定済みの probe であることや、最後に見える error が以前の operation または application policy から生じることもあります。file descriptor を解読し、process 関係を追い、application log と相関させます。

permission と ptrace security policy は trace 可能な process を制限します。許可なく別ユーザーや production process へ attach してはいけません。suspension と timing change が service behavior へ影響する可能性があります。

:::single-choice{#system-calls-strace-failure}
trace 内で一つの syscall が失敗したら、必ず application が壊れているという意味ですか？

::option[はい。0 以外の return はすべて Linux を直ちに終了するからです。]{#system-calls-nonzero-terminates explanation="application は system failure なしに syscall error を日常的に処理します。"}
::option[いいえ。program は代替手段を probe し、想定済み error を処理することがあります。]{#system-calls-expected-failure .correct explanation="return を単独で見ず、control flow と application context の中で解釈します。"}
::option[はい。カーネルが想定済み error を返すことはないからです。]{#system-calls-no-expected-errors explanation="存在しない path や非対応 operation などの error は、通常の API 結果です。"}
:::

## まとめ

これで、library API から検証済み kernel work まで system call を追跡できます。

1. 高水準 function と system-call ABI を区別する。
2. architecture の entry instruction を、管理された kernel dispatch と関連付ける。
3. syscall number と structure を architecture 固有として扱う。
4. 機密データを保護しながら、filter した `strace` 出力を使う。
5. failure と tracing overhead を application context で解釈する。
