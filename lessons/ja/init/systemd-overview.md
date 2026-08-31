---
lesson_id: "systemd-overview"
course_id: "init"
lang: "ja"
order_index: 5
title: "systemd の概要"
description: "systemd がユニットを読み込み、依存関係を解決し、ターゲットを有効化して、システムとユーザーのリソースを管理する仕組みを学びます。"
meta_title: "systemd の概要 - Init システム"
meta_description: "systemd init システムの基本を学びましょう。このガイドでは、systemd（または system d）がユニットとターゲットを使用して Linux の起動プロセスとシステムサービスをどのように管理するかを解説します。Linux 初期化の最新標準の核となる概念を理解しましょう。"
meta_keywords: "systemd, system d, init システム，systemd ユニット，systemd ターゲット，linux 起動プロセス，linux サービス，システム管理，初心者，チュートリアル"
---

Systemd は現在の多くの Linux ディストリビューションで使われる、PID 1 の init・サービスマネージャーです。systemd プロジェクトはログ、デバイス、ログイン、ネットワーク、時刻などのコンポーネントも提供しますが、どの部分を採用するかはディストリビューションが選べます。

## 稼働中のマネージャーを確認する

インストール済みディレクトリの有無ではなく、実際の状態を調べます。

```bash
$ ps -p 1 -o pid,comm,args=
$ systemctl is-system-running
```

別のプログラムが PID 1 のシステムにも `/usr/lib/systemd/` が存在する場合があり、コンテナは独自の PID 名前空間を公開できます。また、`systemctl` にはユーザーマネージャー用やリモート・コンテナ用のモードもあります。操作の対象となるマネージャーを特定してください。

:::single-choice{#systemd-overview-detection}
systemd がシステムの init マネージャーであることを最も直接的に示すものはどれですか？

::option[`/usr/lib/systemd` というディレクトリが存在すること。]{#systemd-overview-directory explanation="systemd が PID 1 でなくても、ライブラリやユニットファイルがインストールされたままの場合があります。"}
::option[あるユーザーが `systemctl` というコマンドを1回実行したこと。]{#systemd-overview-command-executed explanation="システムの systemd マネージャーを利用できなくても、クライアントバイナリは存在できます。"}
::option[ホストの PID 1 が systemd であること。]{#systemd-overview-pid-one .correct explanation="実行中の最初のプロセスは、インストール済みファイルやパッケージ名より強い証拠です。"}
:::

## 管理対象オブジェクトとしてのユニット

ユニットは、リソースまたは活動を表す systemd の名前付きモデルです。一般的なユニットタイプには次のものがあります。

- プロセスとデーモンを表す `.service`
- ソケットアクティベーション用の `.socket`
- ファイルシステム用の `.mount` と `.automount`
- イベント駆動の有効化に使う `.timer` と `.path`
- グループ化と同期に使う `.target`
- そのほかの管理対象リソースを表す `.device`、`.swap`、`.slice`、`.scope`

ユニットの状態は常に「実行中」とは限りません。マウントはマウント済み、タイマーは待機中、デバイスは存在、ターゲットは依存関係へ到達した後にアクティブ、という状態になれます。

:::single-choice{#systemd-overview-group-unit}
ほかのユニットをまとめ、同期点を提供するためによく使うユニットタイプはどれですか？

::option[`.socket`]{#systemd-overview-socket explanation="ソケットユニットは IPC またはネットワークのエンドポイントを公開し、サービスを有効化できます。"}
::option[`.target`]{#systemd-overview-target .correct explanation="ターゲットユニットは依存関係を集め、起動や運用上の到達点を表します。"}
::option[`.timer`]{#systemd-overview-timer explanation="タイマーユニットは、カレンダー時刻または単調時刻に基づいて有効化を予約します。"}
:::

## ユニットの読み込みパスと上書き

システムユニットは、次のようなディストリビューション用および管理者用のパスから読み込まれます。

- 多くのディストリビューションで、パッケージ提供ユニットを置く `/usr/lib/systemd/system/`
- 実行時に生成した設定や一時設定を置く `/run/systemd/system/`
- 永続的なローカル管理者設定と上書きを置く `/etc/systemd/system/`

ベンダー用の正確なパスは環境によって異なります。同じユニット名では、優先度の高いローカル設定が優先度の低いファイルを上書きします。パッケージ更新による変更を確認できるよう、ベンダーファイル全体をコピーして変更するより、`systemctl edit UNIT` でドロップイン上書きを作る方法を優先してください。

:::single-choice{#systemd-overview-local-override}
永続的なローカルのシステムユニット上書きは、通常どこに置くべきですか？

::option[`/proc/systemd/` の中。]{#systemd-overview-proc-systemd explanation="procfs は実行時のカーネルインターフェースであり、永続的なユニット設定ではありません。"}
::option[`/etc/systemd/system/` の下。]{#systemd-overview-etc-system .correct explanation="管理者設定の層は、パッケージ化されたベンダーユニットより優先されます。"}
::option[ディスクの MBR にあるブートコードのバイト内。]{#systemd-overview-mbr-units explanation="サービスユニットはユーザー空間の設定ファイルです。"}
:::

## 依存関係と順序

Systemd は依存関係からトランザクションを構築します。`Wants=` と `Requires=` は、強さの異なる依存関係としてほかのユニットをトランザクションへ取り込みます。`Before=` と `After=` は、両方のユニットが予定されている場合の順序を指定しますが、それ自体で別のユニットを開始させることはありません。

`After=network.target` という行があっても、利用可能な接続、DNS、特定のリモートエンドポイントの準備完了は保証されません。サービスは適切な network-online 連携を使うか、独自に再試行と準備完了の処理を実装する必要があります。

:::single-choice{#systemd-overview-after-semantics}
`After=other.service` だけでは何を指定しますか？

::option[相手サービスのアプリケーションエンドポイントが正常であることの保証。]{#systemd-overview-after-health explanation="順序上の完了とアプリケーションの準備完了は異なる概念です。"}
::option[両方のユニットがトランザクションに含まれる場合の順序。]{#systemd-overview-after-ordering .correct explanation="相手ユニットを取り込むには、Wants や Requires など別の要件が必要です。"}
::option[将来のすべての起動時に両ユニットを自動的に有効化すること。]{#systemd-overview-after-enable explanation="有効化はインストール時のメタデータであり、順序からは暗黙に設定されません。"}
:::

## ターゲットと既定の起動トランザクション

`default.target` は通常、`multi-user.target` や `graphical.target` などのターゲットへの別名です。Systemd はそのターゲットと依存関係のトランザクションを開始し、明示された順序を守りながら、無関係な処理を並行して進めます。

ターゲットがランレベルに似ているのは、大まかな互換性の範囲だけです。複数のターゲットを同時にアクティブにでき、独自のターゲットも作成できます。また、ターゲットがアクティブでも、マシン上の全サービスが正常とは限りません。

:::single-choice{#systemd-overview-default-target}
`default.target` は通常何を選択しますか？

::option[`mkfs` が消去すべき既定のブロックデバイス。]{#systemd-overview-default-disk explanation="ターゲットはユニットの有効化を表し、破壊的なストレージ選択ではありません。"}
::option[常に唯一アクティブになれるターゲット。]{#systemd-overview-only-target explanation="ターゲットはグループであり、1回の起動で複数をアクティブにできます。"}
::option[通常のシステム起動に使うターゲットのトランザクション。]{#systemd-overview-normal-boot .correct explanation="通常は、管理者が選んだマルチユーザーまたはグラフィカル起動ターゲットへの別名です。"}
:::

## まとめ

systemd を、稼働中のマネージャー、ユニット、トランザクションという観点で説明できるようになりました。

1. 関連する PID 1 とマネージャー接続を通じて systemd を確認する。
2. リソースの種類をユニットの接尾辞に対応付ける。
3. ローカルの上書きをベンダー設定より優先度の高い場所へ置く。
4. 依存関係の強さ、順序、アプリケーションの準備完了を区別する。
5. ターゲットを排他的な状態ではなく、グループと到達点として扱う。
