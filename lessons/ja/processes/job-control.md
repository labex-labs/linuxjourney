---
lesson_id: "job-control"
course_id: "processes"
lang: "ja"
order_index: 11
title: "ジョブ制御"
description: "対話型シェルがフォアグラウンド、バックグラウンド、停止中のジョブを管理する仕組みを学びます。"
meta_title: "ジョブ制御 - プロセス管理"
meta_description: "バックグラウンドプロセスを効果的に管理するための Linux ジョブ制御チュートリアルをご覧ください。jobs、bg、fg、kill コマンドを使用して強力なシェルマルチタスクを学びましょう。"
meta_keywords: "Linux ジョブ制御，バックグラウンドプロセス，jobs コマンド，bg コマンド，fg コマンド，kill コマンド，Linux チュートリアル，初心者 Linux"
---

対話型シェルはジョブ制御を使い、1つの端末セッション内のパイプラインを調整します。ジョブは1プロセスまたはパイプライン全体を含み、通常は1つのプロセスグループへまとめ、端末とシェルが一単位として操作できるようにします。

## バックグラウンドジョブを開始する

`&` を末尾に付け、パイプラインを非同期で開始します。

```bash
$ sleep 1000 &
[1] 18420
```

シェルは完了を待たずプロンプトを返します。バックグラウンド化だけでは、出力のリダイレクト、制御端末からの切り離し、ログアウト後の生存は保証されません。必要なら入出力を明示的にリダイレクトし、対話型シェルより長く動かす作業にはサービスマネージャー、スケジューラー、端末マルチプレクサーを使います。

バックグラウンドジョブが制御端末を読もうとすると、端末のフォアグラウンドプロセスグループではないため、通常 `SIGTTIN` で停止します。

:::single-choice{#job-control-ampersand-effect}
末尾の `&` は対話型シェルへ何を要求しますか？

::option[ログアウトとシステム再起動後もジョブが残ることを保証する。]{#job-control-survive-restart explanation="バックグラウンド化だけでは永続的な監督も再起動後の存続も提供しません。"}
::option[次のプロンプトまで待たず、パイプラインをバックグラウンドジョブとして動かす。]{#job-control-background-job .correct explanation="ジョブを非同期で開始し、シェルで次のコマンドを使えるようにします。"}
::option[ジョブの標準出力とエラーを破棄する。]{#job-control-discard-output explanation="リダイレクトしなければ、バックグラウンドジョブも端末へ書き込めます。"}
:::

## シェルジョブを一覧表示する

`jobs` 組み込みは現在のシェルが認識するジョブを表示します。

```text
$ jobs
[1]    Running    sleep 1000 &
[2]-   Running    sleep 1001 &
[3]+   Stopped    sleep 1002
```

角括弧内はシェルのジョブ ID で、PID ではありません。`%1` のように `%` を付けるとジョブ指定になります。`+` は引数なしの多くのコマンドが選ぶ現在のジョブ、`-` は前のジョブです。

ジョブ表は1つのシェルに属するため、通常別端末のシェルは自身の `jobs`、`fg`、`bg` でこれらを一覧・操作できません。

:::single-choice{#job-control-jobs-scope}
`jobs` 組み込みは何を一覧表示しますか？

::option[現在のシェルセッションが追跡するジョブ。]{#job-control-jobs-current-shell .correct explanation="ジョブ ID と状態は、そのジョブを開始または引き取った対話型シェルが保持します。"}
::option[システム上で現在見える全プロセス。]{#job-control-jobs-all-processes explanation="システム全体のプロセス検査は ps などの役割で、シェルのジョブ表はより限定的です。"}
::option[システム起動中に開始したサービスだけ。]{#job-control-jobs-boot-services explanation="起動サービスは通常サービスマネージャーが監督し、対話型シェルのジョブ表ではありません。"}
:::

## ジョブを停止・続行する

ジョブがフォアグラウンドのとき `Ctrl-Z` を押すと、通常端末がフォアグラウンドプロセスグループへ `SIGTSTP` を送り、停止後にシェルが制御を取り戻します。

```text
$ sleep 1002
^Z
[3]+  Stopped    sleep 1002
```

現在の停止中ジョブをバックグラウンドで続行します。

```bash
$ bg
```

`bg` は続行シグナルを送り、ジョブを端末のフォアグラウンド外に残します。停止中ジョブに使うもので、すでにバックグラウンドで実行中のコマンドを再開する必要はありません。

:::single-choice{#job-control-bg-purpose}
`bg %3` は停止中のジョブ3へ何をしますか？

::option[ファイルを `bg` というディレクトリへ移す。]{#job-control-bg-files explanation="シェルのジョブ制御組み込みで、ファイルを移動しません。"}
::option[バックグラウンドジョブとして続行する。]{#job-control-bg-continue .correct explanation="端末のフォアグラウンドへ割り当てず、選択した停止中ジョブを再開します。"}
::option[`SIGKILL` で終了する。]{#job-control-bg-kill explanation="終了ではなく続行します。"}
:::

## ジョブをフォアグラウンドへ移す

`fg` とジョブ指定で、端末のフォアグラウンドプロセスグループにして待ちます。

```bash
$ fg %1
```

引数なしでは通常 `+` の現在ジョブを選び、停止中ジョブはフォアグラウンドへ入ると続行されます。

:::single-choice{#job-control-fg-effect}
`fg %1` は何をしますか？

::option[ジョブ1を端末のフォアグラウンドへ割り当て、待機する。]{#job-control-fg-foreground .correct explanation="選択したジョブをフォアグラウンドにし、端末と対話できるようにします。"}
::option[ジョブ1を PID 1 へ変更する。]{#job-control-fg-pid-one explanation="シェルジョブ ID はプロセス ID を置き換えません。"}
::option[ジョブ1の2個目のコピーをバックグラウンドで開始する。]{#job-control-fg-copy explanation="既存ジョブを操作し、複製しません。"}
:::

## ジョブへシグナルを送る

シェルでは `kill` にジョブ指定を渡せます。

```bash
$ kill -TERM %1
```

通常、パイプラインの1要素だけでなくジョブのプロセスグループへ送ります。選択ジョブを先に確認し、強制的な段階へ進む前に `SIGTERM` を使ってください。ジョブ指定はシェル構文で、スクリプトや外部ツールは通常、検証済み PID またはプロセスグループ ID を使います。

:::single-choice{#job-control-job-specification}
プロセス ID 1 ではなく、シェルジョブ1を指す引数はどれですか？

::option[`1`]{#job-control-plain-one explanation="kill の通常の数値引数は PID と解釈されます。"}
::option[`#1`]{#job-control-hash-one explanation="ハッシュ接頭辞は、紹介したシェルジョブ ID 構文ではありません。"}
::option[`%1`]{#job-control-percent-one .correct explanation="パーセント接頭辞がシェルのジョブ指定を表します。"}
:::

[Linux プロセスの管理と監視](https://labex.io/labs/comptia-manage-and-monitor-linux-processes-590864) で `sleep` など無害なコマンドを使って練習できます。

## まとめ

シェルが制御する状態間でジョブを意図的に移動できるようになりました。

1. `&` で自動的な切り離しを行わず、バックグラウンドジョブを開始する。
2. `jobs` で現在のシェルのジョブ表を調べる。
3. `Ctrl-Z` で停止し、`bg` でバックグラウンド続行する。
4. `fg` で選択したジョブを端末へ戻す。
5. シグナル送信時は `%JOB_ID` でシェルジョブを指定する。
