---
lesson_id: "process-signals"
course_id: "processes"
lang: "ja"
order_index: 6
title: "シグナル"
description: "Linux がプロセス制御とイベント通知のため、シグナルを生成、遮断、配送、処理する仕組みを学びます。"
meta_title: "シグナル - プロセス"
meta_description: "プロセス管理の重要なメカニズムである Linux シグナルの基本を探ります。SIGTERM（シグナル 15 Linux）や SIGKILL などの Linux プロセスシグナルがどのように機能するかを学び、それらの OS シグナルコードを理解します。"
meta_keywords: "Linux シグナル，Linux プロセスシグナル，シグナル 15 Linux, OS シグナルコード，SIGKILL, SIGTERM, SIGINT, プロセス管理，Linux チュートリアル"
---

シグナルはプロセスまたは特定のスレッドへ配送される非同期通知です。イベントを報告し操作を要求しますが、データ指向のプロセス間通信より運べる情報は限られます。

## シグナルの発生元

- 端末が `Ctrl-C` で `SIGINT`、`Ctrl-Z` で `SIGTSTP` を生成し、フォアグラウンドプロセスグループへ送る。
- スレッドが不正なメモリ参照をしたとき、カーネルが `SIGSEGV` などの同期シグナルを生成する。
- プロセスが、許可された別プロセスやプロセスグループへシグナルを送る。
- タイマー、子の状態変化、端末のハングアップがほかのシグナルを生成する。

送信側には通常、認証情報や capability に基づく適切な権限が必要です。シグナルはカーネルを介する制御インターフェースで、任意のユーザー間の無制限なメッセージではありません。

:::single-choice{#process-signals-ctrl-c}
端末が `Ctrl-C` で通常生成するシグナルはどれですか？

::option[`SIGTSTP`]{#process-signals-ctrl-c-tstp explanation="通常は Ctrl-Z などの端末一時停止文字に関連します。"}
::option[`SIGCONT`]{#process-signals-ctrl-c-cont explanation="停止したプロセスを再開するもので、キーボード割り込みではありません。"}
::option[`SIGINT`]{#process-signals-ctrl-c-int .correct explanation="端末の割り込み文字は通常、フォアグラウンドプロセスグループへ SIGINT を生成します。"}
:::

## 処理方法と既定動作

多くのシグナルにはプロセス全体の処理方法があり、次の3つから応答を選びます。

- 定義済みの既定動作を行う
- シグナルを無視する
- ユーザーが設定したハンドラーを呼ぶ

既定動作は終了、コアダンプを伴う終了、停止、続行、無視などです。`SIGTERM` を捕捉すれば秩序立った終了を始められますが、ハンドラーは厳しい async-signal-safety 規則に従う必要があり、プログラムが終了を遅らせたり拒んだりもできます。

名前は番号より移植性と可読性に優れます。一般的な Linux では `SIGTERM` が15でも、関連規格が保証しない番号が全環境で同じとは限りません。ローカルの対応は `kill -l` で調べます。

:::single-choice{#process-signals-term-behavior}
プロセスが `SIGTERM` へ穏やかに応答できるのはなぜですか？

::option[そのシグナルのハンドラーを設定できるから。]{#process-signals-term-handler .correct explanation="SIGKILL と異なり捕捉できるため、独自の終了処理を開始できます。"}
::option[カーネルが開いた全文書を必ず自動保存するから。]{#process-signals-term-kernel-save explanation="後始末はプログラムのコード次第で、カーネルは任意の文書状態を理解して保存しません。"}
::option[`SIGTERM` は既定では終了を起こせないから。]{#process-signals-term-no-default explanation="処理方法を変更していなければ、既定動作は終了です。"}
:::

## 遮断と保留中シグナル

スレッドはシグナルマスクで、選択したシグナルの配送を一時的に遮断できます。遮断中に生成されたシグナルは、標準シグナルとリアルタイムシグナルの規則に従い、配送可能になるまで保留されます。同種の標準シグナルは発生回数ごとにキューへ入らず、まとめられる場合があります。

マルチスレッドプロセスでは、プロセス宛てシグナルは遮断していない適格なスレッドへ配送され、スレッド宛てシグナルは指定スレッドを対象にします。そのため「プロセスが遮断したか」だけでは不十分です。

:::single-choice{#process-signals-blocked-state}
遮断可能なシグナルが対象による遮断中に生成されると、通常どうなりますか？

::option[配送可能になるまで保留される。]{#process-signals-pending .correct explanation="遮断は処理を延期し、解除後に保留シグナルを配送できます。"}
::option[自動的に `SIGKILL` へ変換される。]{#process-signals-convert-kill explanation="カーネルは通常の遮断済みシグナルを捕捉不能なものへ昇格させません。"}
::option[対象プロセスのユーザー ID を変更する。]{#process-signals-change-uid explanation="シグナルマスクは配送へ影響し、認証情報を変えません。"}
:::

## 処理できないシグナル

`SIGKILL` はプロセスを終了し、`SIGSTOP` は停止します。どちらも捕捉、無視、遮断できません。カーネルが最終的な制御を保てますが、`SIGKILL` ではアプリケーションが後始末する機会がありません。

それでも観測上、タスクが即座に消えない場合があります。割り込み不可能なカーネル操作を待っていることがあり、終了後も親が状態を回収する必要があります。

:::single-choice{#process-signals-uncatchable-pair}
捕捉、無視、遮断できない組み合わせはどれですか？

::option[`SIGKILL` と `SIGSTOP`]{#process-signals-kill-stop .correct explanation="プロセスが基本動作を上書き・延期できないよう、カーネルがこの2つを予約しています。"}
::option[`SIGINT` と `SIGTERM`]{#process-signals-int-term explanation="どちらもユーザーハンドラーを設定でき、遮断もできます。"}
::option[`SIGHUP` と `SIGCONT`]{#process-signals-hup-cont explanation="特別な意味はありますが、捕捉不能な組み合わせではありません。"}
:::

## まとめ

Linux のシグナル処理における主な段階と制約を説明できるようになりました。

1. 端末、カーネル、プロセスが生成するシグナルを特定する。
2. 既定動作、無視、ハンドラーを区別する。
3. 遮断を保留中の配送とスレッドマスクへ関連付ける。
4. `SIGKILL` と `SIGSTOP` は処理も遮断もできないと覚える。
