---
lesson_id: "sysv-services"
course_id: "init"
lang: "ja"
order_index: 2
title: "System V サービス"
description: "稼働中のシステムが提供するラッパーを通じ、従来の SysV サービススクリプトを確認、操作する方法を学びます。"
meta_title: "System V サービス - Init"
meta_description: "Linux における従来の System V (SysV) サービスの管理方法を学びます。このガイドでは、`service` コマンドを使用して System V init システム上のサービスの一覧表示、開始、停止、再起動について解説します。"
meta_keywords: "system v, sysv init, linux サービス，service コマンド，linux サービス管理，サービス開始，サービス停止，サービス再起動，linux system v"
---

SysV サービスは通常、`/etc/init.d/` の下にある実行可能なスクリプトで表されます。スクリプトは、その実装とディストリビューションの慣例に従い、`start`、`stop`、`restart`、`status` などの操作を受け付けます。`service` コマンドは、名前を指定したスクリプトをより制御された環境で実行するラッパーです。

## サービスと操作を調べる

まずスクリプト名を一覧表示します。

```bash
$ ls -1 /etc/init.d/
```

実装によっては、次のコマンドも利用できます。

```bash
$ service --status-all
```

角括弧の印と終了ステータスの意味はラッパー固有で、スクリプトが状態不明と報告する場合もあります。個々のサービスについては、すべての操作が存在すると思い込まず、スクリプトの使用方法出力または文書を確認してください。

:::single-choice{#sysv-services-wrapper-purpose}
`service` コマンドは通常何をラップしますか？

::option[すべてのサービスファイル上で動くディスクパーティションエディター。]{#sysv-services-partition-editor explanation="サービス制御はストレージのパーティション分割とは無関係です。"}
::option[スクリプトによって動的に追加されるカーネルシステムコール。]{#sysv-services-new-syscall explanation="init スクリプトはユーザー空間のプロセス制御プログラムです。"}
::option[名前を指定した init スクリプトと、そのスクリプトが対応する操作。]{#sysv-services-script-action .correct explanation="ラッパーは古いサービススクリプトを見つけ、正規化した環境で呼び出します。"}
:::

## 開始と停止

実際に SysV が管理するホストでは、次の形式が一般的です。

```bash
$ sudo service SERVICE_NAME start
$ sudo service SERVICE_NAME stop
```

サービス、その依存先、現在の状態、運用への影響を特定してから、プレースホルダーを置き換えてください。リモートセッションからネットワーク、リモートアクセス、ストレージ、認証を停止すると、接続できなくなったり作業中のデータを壊したりするおそれがあります。

`/etc/init.d/SERVICE_NAME ACTION` という直接実行形式も存在します。ただし、稼働中のマネージャーが互換機能を提供するホストでは、状態と依存関係を追跡できるよう、マネージャー向けのコマンドを使ってください。

:::single-choice{#sysv-services-stop-peanut}
SysV サービス `peanut` の停止を要求するコマンドはどれですか？

::option[`sudo service stop peanut`]{#sysv-services-stop-first explanation="一般的な引数の順序では、操作より前にサービス名を置きます。"}
::option[`sudo stop --partition peanut`]{#sysv-services-partition-stop explanation="これは SysV の service ラッパー構文ではありません。"}
::option[`sudo service peanut stop`]{#sysv-services-peanut-stop .correct explanation="ラッパーにはサービス名、その後に要求する停止操作を渡します。"}
:::

## 再読み込み、再起動、状態確認

`restart` は通常、サービスを停止してから起動するため、中断が発生します。`reload` は完全に再起動せず設定を読み直すよう要求できますが、スクリプトとデーモンが対応している場合に限ります。一部のスクリプトは、ディストリビューション固有の代替動作を持つ `force-reload` も提供します。

再読み込みや再起動の前には設定を検証し、リモートアクセスを変更する場合は2つ目の管理用接続を確保してください。操作後は「実行中」という状態だけでなく、実際のエンドポイントとログでもサービスを確認します。

```bash
$ sudo service SERVICE_NAME status
$ sudo service SERVICE_NAME reload
```

:::single-choice{#sysv-services-reload-versus-restart}
`reload` が `restart` と同じだと思い込んではいけないのはなぜですか？

::option[reload は必ずオペレーティングシステム全体を停止するから。]{#sysv-services-reload-shutdown explanation="これはサービスの reload 操作が持つ通常の意味ではありません。"}
::option[restart は設定を表示するだけで、プロセスの状態を決して変更しないから。]{#sysv-services-restart-readonly explanation="restart は通常、サービスを停止してから起動します。"}
::option[reload はサービス固有で、プロセスを停止せず設定を読み直せる場合があるから。]{#sysv-services-reload-specific .correct explanation="対応状況と意味は init スクリプトとデーモン次第ですが、restart では通常ライフサイクルが中断します。"}
:::

## 実行時の制御と起動時の有効化

今サービスを開始しても、将来のランレベルで有効になるとは限りません。起動時の有効化はランレベルのリンクで表され、`update-rc.d`、`chkconfig`、サービスマネージャーの互換ジェネレーターなど、ディストリビューション固有のツールで管理されます。

ディストリビューションの依存関係メタデータと管理ツールを理解するまでは、`S` と `K` のリンクを手動で作らないでください。手動のリンクは上書きされたり、順序を誤ったりすることがあります。

:::single-choice{#sysv-services-start-versus-enable}
`service SERVICE start` を実行すると、将来の起動時にも必ずそのサービスが有効になりますか？

::option[はい。start 操作は常にすべてのランレベルリンクを作成します。]{#sysv-services-start-links explanation="ラッパーが永続的な有効化を変更するとは限りません。"}
::option[いいえ。実行時の状態とランレベルでの有効化は別です。]{#sysv-services-runtime-separate .correct explanation="起動リンクやマネージャーの方針が、現在プロセスを開始することとは別に将来の有効化を決めます。"}
::option[はい。実行中の PID がブートセクターへ永久保存されます。]{#sysv-services-pid-boot-sector explanation="PID は実行時の識別子であり、起動時の有効化メタデータではありません。"}
:::

## まとめ

実行時の制御と起動方針を混同せずに、従来のサービスを操作できるようになりました。

1. 実際のスクリプトと対応する操作を調べる。
2. ラッパー構文では、操作より前にサービス名を置く。
3. 再読み込みや再起動の動作を事前に検証し、操作後も確認する。
4. 将来のランレベルでの有効化は、ディストリビューションのツールで管理する。
