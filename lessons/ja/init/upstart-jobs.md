---
lesson_id: "upstart-jobs"
course_id: "init"
lang: "ja"
order_index: 4
title: "Upstart ジョブ"
description: "Upstart の稼働が確認された古いシステムで、`initctl` を使ってジョブを確認、制御する方法を学びます。"
meta_title: "Upstart ジョブ - Init"
meta_description: "Linux 環境での Upstart ジョブを使用したサービス管理ガイド。initctl ユーティリティを使用して、Upstart Linux システム上のジョブの一覧表示、開始、停止、再起動を学習します。"
meta_keywords: "Upstart ジョブ，initctl, upstart linux, Linux サービス，システム管理，init システム，Linux チュートリアル"
---

`initctl` は稼働中の Upstart init デーモンと通信します。関連する PID 名前空間で実際に Upstart が動いていることを確認してから使ってください。現在の systemd ホストでは、代わりに systemd のネイティブツールを使います。

## ジョブの状態を一覧表示して読む

既知のジョブとインスタンスを一覧表示します。

```bash
$ initctl list
```

1つのジョブを調べます。

```bash
$ initctl status networking
networking start/running
```

Upstart は `start` や `stop` などの **目標**と、`running` や `waiting` などの現在の **状態**を両方報告します。`stop/waiting` はジョブが実行中ではなく、開始条件または手動の要求を待っていることを意味し、必ずしもエラーではありません。

:::single-choice{#upstart-jobs-stop-waiting} Upstart の状態出力で、`stop/waiting` は通常何を意味しますか？

::option[ジョブは実行中だが CPU を消費していない。]{#upstart-jobs-running-idle explanation="実行中のジョブは通常、start 目標と running 状態を示します。"}
::option[ジョブの目標が停止で、プロセスのインスタンスは動いていない。]{#upstart-jobs-stopped-waiting .correct explanation="定義は認識されたまま、Upstart が将来の条件またはコマンドを待っています。"}
::option[オペレーティングシステム全体が電源オフを待っている。]{#upstart-jobs-system-poweroff explanation="この組み合わせが表すのは対象ジョブのインスタンスであり、必ずしもシステム全体の状態ではありません。"}
:::

## ジョブを開始、停止する

依存関係と影響を確認した後、次を実行します。

```bash
$ sudo initctl start JOB_NAME
$ sudo initctl stop JOB_NAME
```

ジョブは、環境変数をキーにした複数のインスタンスを定義できます。その場合は、設定が要求する変数を正確に指定し、インスタンスの照会や停止でも一貫して含めます。ネットワーク、ストレージ、認証、リモートアクセスのジョブを操作するとセッションが切れる場合があるため、コンソールから復旧できる手段を確保してください。

:::single-choice{#upstart-jobs-start-command} ジョブ `peanuts` の手動開始を要求するコマンドはどれですか？

::option[`sudo initctl start peanuts`]{#upstart-jobs-start-peanuts .correct explanation="start サブコマンドの後に、設定されたジョブ名と必要なインスタンス変数を置きます。"}
::option[`sudo initctl peanuts start`]{#upstart-jobs-name-first explanation="initctl の構文では、ジョブ名より前にサブコマンドを置きます。"}
::option[`sudo systemctl initctl peanuts`]{#upstart-jobs-systemctl-mixed explanation="これは異なる2つのサービスマネージャーのインターフェースを誤って混ぜています。"}
:::

## 再起動と設定変更

実行中のジョブを再起動するには、次のように要求します。

```bash
$ sudo initctl restart peanuts
```

Upstart の `restart` は、ジョブファイルを編集した後の新たな `stop`、`start` と常に同じではありません。実行中のジョブでは既存の設定が引き続き基準になる場合があります。変更した `.conf` を検証し、インストール済みバージョンに合う方法で Upstart に設定を再読み込みさせ、新しい設定を反映する必要があるときは文書化された停止・開始手順に従ってください。

再起動では中断が発生し、サービスが復旧しない可能性もあります。操作後に実際のエンドポイントとログを確認してください。

:::single-choice{#upstart-jobs-restart-peanuts} 実行中の Upstart ジョブ `peanuts` の再起動を要求するコマンドはどれですか？

::option[`sudo initctl restart peanuts`]{#upstart-jobs-restart-command .correct explanation="restart サブコマンドは、Upstart の制御インターフェースを通じて指定したジョブを操作します。"}
::option[`sudo initctl emit peanuts`]{#upstart-jobs-emit-not-restart explanation="イベントの発行は一致するジョブ条件に影響し、直接的な再起動要求ではありません。"}
::option[`sudo service --status-all peanuts`]{#upstart-jobs-status-all explanation="状態の一覧表示は再起動を要求しません。"}
:::

## ジョブ設定を検証する

変更したジョブファイルをインストールする前に、古いディストリビューションが提供する検証ツール（一般には `init-checkconf`）を使い、読み込まれるスクリプト、環境、ユーザーとグループの設定、再生成方針、イベント式を確認します。その後、バージョンに適した `initctl reload-configuration` の手順で定義を再読み込みしてください。

構文検証だけでは、パスが存在すること、認証情報に実行権限があること、イベントが到着すること、プロセスが準備完了になることまでは証明できません。復旧できる環境でテストしてください。

:::single-choice{#upstart-jobs-syntax-validation-limit} ジョブの構文検証では証明できないことはどれですか？

::option[サービスが正常に起動し、準備完了になること。]{#upstart-jobs-runtime-not-proven .correct explanation="実行時のパス、権限、依存関係、イベントの流れは、実際に制御されたテストで確認する必要があります。"}
::option[設定のテキストを構文解析できること。]{#upstart-jobs-parse-purpose explanation="構文解析こそ、構文検証の主な目的です。"}
::option[検証ツールへファイルが渡されたこと。]{#upstart-jobs-file-supplied explanation="入力がなければツールはすぐに報告できます。"}
:::

## イベントを慎重に発行する

Upstart では名前付きイベントを発行できます。

```bash
$ sudo initctl emit EVENT_NAME
```

開始または停止の式が一致するすべてのジョブが反応できます。イベントは1つのジョブ宛てではなく、さらに別のイベントを通じて影響が連鎖する場合もあります。カスタムイベントやシステムイベントを発行する前に、一致する設定をすべて調べてください。本番ホストで中核的な起動イベントを不用意に再送してはいけません。

:::single-choice{#upstart-jobs-emit-scope} `initctl emit EVENT_NAME` を実行すると、何が起こり得ますか？

::option[そのイベントに一致するすべてのジョブ式が状態移行できる。]{#upstart-jobs-event-matches .correct explanation="イベントは1つの名前付きサービスだけに送られず、Upstart の依存関係モデルへブロードキャストされます。"}
::option[名前がイベントと完全に同じジョブだけが反応できる。]{#upstart-jobs-event-name-only explanation="一致はジョブ名の同一性ではなく、start on と stop on の式で定義されます。"}
::option[イベントが永続キューのメッセージとして永久保存される。]{#upstart-jobs-event-durable explanation="Upstart のイベントはライフサイクル通知であり、汎用の永続メッセージキューではありません。"}
:::

## まとめ

状態とイベントの影響範囲を明示して、Upstart ジョブを操作できるようになりました。

1. `initctl` の出力で、目標と状態を分けて読む。
2. 影響を確認してから、正確なジョブインスタンスを開始、停止する。
3. 再起動と、変更したジョブ設定の反映を別の問題として扱う。
4. 構文を検証した後、実行時の準備完了までテストする。
5. イベントを発行する前に、一致するすべての条件を調べる。
