---
lesson_id: "killing-processes"
course_id: "processes"
lang: "ja"
order_index: 7
title: "kill（終了）"
description: "プロセスを特定し、`kill` で適切なシグナルを安全な段階的手順に従って送る方法を学びます。"
meta_title: "kill（終了） - プロセス"
meta_description: "Linux の kill コマンドをマスターしてプロセスを管理・終了する方法を学びます。このガイドでは、kill と terminate の違い、および kill sigterm (SIGTERM)、SIGKILL、kill sighup (SIGHUP) などのシグナルについて解説します。"
meta_keywords: "kill コマンド，kill sigterm, kill sighup, linux kill -0, kill vs terminate, kill -15 linux, SIGTERM, SIGKILL, プロセス管理，プロセス終了"
---

`kill` コマンドはプロセスまたはプロセスグループへシグナルを送ります。名前は歴史的なもので、要求するシグナルは終了、停止、続行、アプリケーション固有の操作などを起こせます。送信前に正確な対象と、プログラムが文書化したシグナル動作を確認してください。

## 秩序立った終了を要求する

PID だけを指定すると、既定で `SIGTERM` を送ります。

```bash
$ kill 12445
```

明示する場合は記号名を優先します。

```bash
$ kill -TERM 12445
```

`SIGTERM` の既定動作は終了ですが、プログラムは捕捉・無視できます。適切に設計されたサービスは新しい仕事の受け入れ停止、状態保存、リソース解放を行えますが、即時または正常な後始末の保証ではありません。

:::single-choice{#killing-processes-default-signal} `kill PID` が既定で要求するシグナルはどれですか？

::option[`SIGKILL`]{#killing-processes-default-kill explanation="強制的で捕捉不能なシグナルは明示的に選ぶ必要があります。"}
::option[`SIGTERM`]{#killing-processes-default-term .correct explanation="別のシグナルを指定しなければ、標準の終了要求を送ります。"}
::option[`SIGSTOP`]{#killing-processes-default-stop explanation="プロセス停止は kill の既定要求ではありません。"}
:::

## 対象を検証する

PID は再利用されるため、古い PID が後に別プロセスを指すことがあります。操作直前に対象を調べます。

```bash
$ ps -p 12445 -o pid,ppid,user,lstart,stat,cmd
```

ユーザー、開始時刻、コマンド、親、サービス所有者、運用上の役割を確認します。サービスマネージャーが所有するなら、その状態を正しく保ち、子の即時再起動を避けるため、可能な限りマネージャーの stop・reload を使います。

権限規則の範囲で自分のプロセスへ送信できます。他者のプロセスには通常、適切な権限が必要です。名前による広いコマンドは、全一致を確認するまで使わないでください。

:::single-choice{#killing-processes-pid-reuse} シグナル送信直前に PID を調べるべきなのはなぜですか？

::option[プロセスがファイルを読むたび PID が変わるから。]{#killing-processes-pid-read explanation="実行中プロセスは通常、生存中ずっと同じ PID を保ちます。"}
::option[以前のプロセス終了後、カーネルが PID を再利用できるから。]{#killing-processes-pid-reused .correct explanation="記憶した数値が、後に別の実行中プロセスを指す場合があります。"}
::option[`kill` はコマンド名だけを受け付け、数値を受け付けないから。]{#killing-processes-no-numeric explanation="数値 PID は kill の通常の対象引数です。"}
:::

## シグナル0で権限を確認する

シグナル番号0は実際のシグナルを配送せず、エラー検査を行います。

```bash
$ kill -0 12445
```

成功は、その瞬間に PID のプロセスが存在し、呼び出し元に送信権限があることを意味します。失敗は不在または権限不足のどちらもあり得るため、すべてを「実行していない」と解釈せず、エラーと終了状態を確認します。瞬間的な検査なので、後の PID 再利用競合は防げません。

:::single-choice{#killing-processes-signal-zero} `kill -0 PID` の成功がその瞬間に確立することは何ですか？

::option[プロセスが全後始末を終えて終了した。]{#killing-processes-zero-exited explanation="成功はシグナル可能な実行中対象を示し、終了完了ではありません。"}
::option[プロセスがその PID を永久に保つ。]{#killing-processes-zero-permanent explanation="検査は瞬間的で、終了後に PID は再利用できます。"}
::option[プロセスが存在し、呼び出し元がシグナルを送れる。]{#killing-processes-zero-permitted .correct explanation="通常のシグナルを配送せず、対象の存在と権限を検査します。"}
:::

## 必要な場合だけ段階的に強める

許可された対象が `SIGTERM` 後も終了しなければ、ワークロードに合う時間を待ち、理由を調べます。強制終了が正当なときは次を送ります。

```bash
$ kill -KILL 12445
```

`SIGKILL` は捕捉、無視、遮断できず、アプリケーションは後始末できません。不完全なトランザクション、一時状態、ほかの構成要素による復旧作業を残す場合があります。最初の通常手段ではなく、調査後の段階的な手段として使います。

ほかのシグナルの意味は受信プログラムの契約次第です。`SIGHUP` は設定再読み込みを要求することが多い一方、既定の終了動作を保つプログラムもあります。`SIGSTOP` は後始末なしに停止し、`SIGCONT` は再開します。

:::single-choice{#killing-processes-kill-tradeoff} `SIGKILL` の主な運用上の欠点は何ですか？

::option[プロセス所有者だけが処理できる。]{#killing-processes-kill-owner-handler explanation="対象プロセスは SIGKILL のハンドラーを設定できません。"}
::option[一時停止するだけで終了しない。]{#killing-processes-kill-pauses explanation="停止は SIGSTOP で、SIGKILL は終了させます。"}
::option[プログラムにアプリケーションレベルの後始末を行う機会がない。]{#killing-processes-kill-no-cleanup .correct explanation="ユーザー空間のハンドラーを呼ばず、カーネルが終了を強制します。"}
:::

隔離環境で自分が開始したプロセスだけを使ってシグナル選択を練習してください。[Linux プロセスの管理と監視](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) は確認と終了の制御された手順を提供します。

## まとめ

意図的で検証可能な手順に従い、プロセスへシグナルを送れるようになりました。

1. 操作前に実行中の対象と監督プロセスを確認する。
2. 通常の終了要求には `SIGTERM` を使う。
3. シグナル0を瞬間的な存在・権限検査として解釈する。
4. `SIGKILL` は調査後、正当な段階的強化に限定する。
