---
lesson_id: "systemd-goals"
course_id: "init"
lang: "ja"
order_index: 6
title: "systemd の目標"
description: "systemd のサービスユニットを確認、上書き、検証、開始、有効化し、問題を調査する方法を学びます。"
meta_title: "systemd の目標 - Init"
meta_description: "systemd の目標を探り、systemctl コマンドを使用して Linux サービスを管理する方法を学びます。このガイドでは、systemd ユニットファイルの基本、サービスの起動、停止、有効化の方法、およびステータスの表示について説明します。"
meta_keywords: "systemd, systemctl, Linux サービス，ユニットファイル，systemd の目標，サービス管理，systemd ユニット，初心者，チュートリアル，ガイド，Linux コマンド"
---

`systemctl` は systemd マネージャーへ要求を送ります。このレッスンではシステムのサービスユニットを扱います。状態を変える前に、正確なユニット名、マネージャーの対象範囲、依存関係、運用上の影響を確認してください。

## サービスユニットを読む

説明用の最小限のユニットは、次のようになります。

```ini
[Unit]
Description=Example worker
Wants=network-online.target
After=network-online.target

[Service]
Type=exec
ExecStart=/usr/local/bin/example-worker
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

- `[Unit]` には説明と依存関係を記述します。
- `[Service]` にはプロセスのライフサイクルとサービス固有の動作を定義します。
- `[Install]` は、有効化コマンドで作成する別名や依存関係リンクを指定します。実行時に自動で有効になる依存関係ではありません。

`ExecStart=` は既定ではシェルを経由しません。シェルを意図的かつ明示的に呼び出さない限り、パイプライン、リダイレクト、変数、引用符は対話型コマンドラインと同じようには動作しません。

:::single-choice{#systemd-goals-install-section}
`WantedBy=` など、`[Install]` のディレクティブが持つ主な目的は何ですか？

::option[サービスのプロセスがすでに実行中であることを保証する。]{#systemd-goals-install-running explanation="実行時の有効化には start または別の依存関係によるトリガーが必要です。"}
::option[ユニットの有効化時に作成するリンクまたは関係を記述する。]{#systemd-goals-enable-links .correct explanation="インストール用メタデータは有効化操作によって解釈され、現在のプロセス状態とは別です。"}
::option[すべてのコマンドをユーザーの対話型シェルで実行する。]{#systemd-goals-install-shell explanation="ユニットのコマンド解析は、既定では対話型シェルを使いません。"}
:::

## 有効な設定を調べる

読み込み済みユニットを一覧表示します。

```bash
$ systemctl list-units --type=service
```

インストール済みユニットファイルと有効化状態を一覧表示します。

```bash
$ systemctl list-unit-files --type=service
```

両者は異なるビューです。ユニットファイルには、有効だが非アクティブ、アクティブだが無効、static、generated、transient、masked、または一方の一覧に存在しない、といった状態があります。ベンダー設定とドロップインを統合した内容は、次のコマンドで調べます。

```bash
$ systemctl cat UNIT.service
$ systemctl show UNIT.service
```

:::single-choice{#systemd-goals-list-units-versus-files}
`list-unit-files` が主に表示し、`list-units` は主には表示しないものは何ですか？

::option[CPU を最も多く消費しているプロセスだけ。]{#systemd-goals-cpu-processes explanation="プロセスのリソース順位は、これらのユニット一覧コマンドの対象外です。"}
::option[インストール済みユニットファイルの有効化状態。]{#systemd-goals-unit-file-state .correct explanation="ユニットファイルが enabled、disabled、static、masked かといったインストール状態を報告します。"}
::option[ジャーナルへ過去に書かれたすべての行。]{#systemd-goals-all-journal explanation="ジャーナルの照会には journalctl を使います。"}
:::

## ローカルの上書きを作る

パッケージ化されたユニットを編集せず、ドロップインを使います。

```bash
$ sudo systemctl edit UNIT.service
```

現在の実装では通常、保存後にこの編集ワークフローの一部として systemctl がマネージャーへ再読み込みを要求します。ただし、別の方法でファイルを変更した場合は次を実行します。

```bash
$ sudo systemctl daemon-reload
```

`daemon-reload` はユニット定義を読み直して依存関係を再構築します。アプリケーション設定を再読み込みしたり、実行中のサービスを再起動したりはしません。必要に応じて `systemd-analyze verify` でユニットの構文と依存関係を検証し、統合後の有効なユニットを確認してください。

:::single-choice{#systemd-goals-daemon-reload}
`systemctl daemon-reload` は何をしますか？

::option[すべてのデーモンへ、アプリケーション設定の再読み込みを強制する。]{#systemd-goals-reload-all-apps explanation="アプリケーションの再読み込みはサービス固有であり、マネージャー設定とは別です。"}
::option[新しいリリースのカーネルで再起動する。]{#systemd-goals-reload-kernel explanation="カーネルを有効にするには起動が必要であり、ユニット定義の再読み込みではありません。"}
::option[systemd のユニット定義と依存関係情報を再読み込みする。]{#systemd-goals-reload-manager .correct explanation="サービス自体を再起動することなく、マネージャーが持つ設定のビューを更新します。"}
:::

## 実行時のサービス状態

サービス設定を検証し、復旧アクセスを確保した後、次のコマンドを使います。

```bash
$ sudo systemctl start peanut.service
$ sudo systemctl stop peanut.service
$ sudo systemctl restart peanut.service
$ sudo systemctl reload peanut.service
```

`reload` が成功するのは、ユニットが再読み込み操作を定義またはサポートする場合だけです。`restart` はプロセスを中断し、サービスを復旧できない場合もあります。リモートアクセス、ネットワーク、ストレージ、認証を扱うときは、別のコンソール経路を維持し、操作前に設定を検証してください。

状態とログを確認します。

```bash
$ systemctl status peanut.service
$ systemctl is-active peanut.service
$ journalctl -u peanut.service -b
```

「Active」はマネージャー上の状態であり、すべてのアプリケーションエンドポイントが正常である証拠ではありません。

:::single-choice{#systemd-goals-start-peanut}
`peanut.service` を今すぐ開始し、それ自体では将来の有効化を変えないコマンドはどれですか？

::option[`sudo systemctl enable peanut.service`]{#systemd-goals-enable-only explanation="enable はインストール用リンクを変更しますが、--now を組み合わせない限りサービスを開始しません。"}
::option[`sudo systemctl start peanut.service`]{#systemd-goals-start-command .correct explanation="start は現在の実行時有効化を要求し、永続的な有効化とは別です。"}
::option[`sudo systemctl daemon-reload peanut.service`]{#systemd-goals-daemon-reload-unit explanation="daemon-reload はユニットを有効化する引数を取らず、このサービスを開始しません。"}
:::

## 有効化、無効化、マスク

将来の依存関係リンクは次のコマンドで管理します。

```bash
$ sudo systemctl enable peanut.service
$ sudo systemctl disable peanut.service
```

enable は `--now` を追加しない限りユニットを開始しません。disable は `--now` を追加しない限り実行中のユニットを停止しません。static ユニットはインストール用メタデータを持たない場合がありますが、それでも別のユニットの依存関係として有効化できます。

マスクするとユニットを `/dev/null` へリンクし、解除するまで依存関係による有効化を含む通常の有効化を阻止します。disable より強力で依存先を壊す可能性があるため、使う前に逆方向の依存関係を調べてください。

:::single-choice{#systemd-goals-disable-runtime}
実行中のサービスに、`--now` を付けず `systemctl disable UNIT` を実行するとどうなりますか？

::option[すぐに `SIGKILL` で終了される。]{#systemd-goals-disable-kills explanation="disable だけでは現在の停止を要求しません。"}
::option[実行ファイルがファイルシステムから削除される。]{#systemd-goals-disable-deletes explanation="有効化操作が管理するのはリンクであり、プログラムのパッケージファイルではありません。"}
::option[通常は実行を続け、将来の有効化リンクだけが削除される。]{#systemd-goals-disable-keeps-running .correct explanation="実行時の状態とインストール状態は別々の軸です。"}
:::

## サービスの結果を検証する

変更後は、プロセス状態、直近のログ、待ち受けエンドポイント、依存ユニット、アプリケーションの正常性を確認します。起動時の有効化を変更した場合は、制御された再起動をまたいだ動作も検証してください。必要に応じて `systemctl is-failed`、`systemctl list-dependencies`、アプリケーション固有の検査を使います。

## まとめ

設定、実行時、有効化を混同せずに systemd サービスを管理できるようになりました。

1. `[Unit]`、`[Service]`、`[Install]` を、それぞれ異なる役割として読む。
2. 読み込み済みユニットの状態と、インストール済みユニットファイルの状態を比較する。
3. ドロップインを使い、外部でファイルを変更した後はマネージャーを再読み込みする。
4. 影響を確認してから、開始、停止、再読み込み、再起動を行う。
5. enable、disable、mask を別々の永続化制御として扱う。
