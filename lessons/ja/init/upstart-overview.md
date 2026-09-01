---
lesson_id: "upstart-overview"
course_id: "init"
lang: "ja"
order_index: 3
title: "Upstart の概要"
description: "従来の Upstart init システムが、イベント式とジョブのライフサイクル目標をどう結び付けるか学びます。"
meta_title: "Upstart の概要 - Init"
meta_description: "Upstart、そのイベント駆動モデル、および Linux でサービスを管理する方法について学習します。Upstart ジョブ構成とその init システムとしての役割を理解します。"
meta_keywords: "Upstart, init system, Linux サービス，Ubuntu, SysV, 初心者チュートリアル，Linux ガイド"
---

Upstart は Canonical が開発した、従来のイベント駆動型 init・サービス管理システムです。古い Ubuntu とほかのいくつかのディストリビューションで使われていましたが、現在の Ubuntu は systemd を使います。現代の環境で標準だと思い込まず、Upstart の稼働が確認された古いホストを保守するときに学ぶ仕組みです。

## 古い Upstart ホストを確認する

PID 1 と稼働中の制御インターフェースを調べます。

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
$ initctl version
```

最後のコマンドが意味のある形で成功するのは、Upstart の制御サービスとクライアントが存在する環境だけです。`/usr/share/upstart` のようなディレクトリや `/etc/init` に残るファイルは弱い証拠です。別の init システムへ移行した後も、パッケージや移行時の残骸が残ることがあります。

:::single-choice{#upstart-overview-active-evidence} ホストが実際に Upstart を使っていることを示す最も強い証拠はどれですか？

::option[ディレクトリ名に `upstart` という語が含まれていること。]{#upstart-overview-directory-only explanation="別の init を使うシステムにも、インストール済み文書や残骸が残ることがあります。"}
::option[システムに少なくとも1つシェルスクリプトがあること。]{#upstart-overview-shell-script explanation="シェルスクリプトはどの init 環境でも一般的です。"}
::option[PID 1 と稼働中の `initctl` インターフェースが Upstart を示すこと。]{#upstart-overview-live-interface .correct explanation="実行中のプロセスと制御インターフェースの証拠は、古いファイルの存在より確実です。"}
:::

## ジョブとイベント

Upstart の **ジョブ**は、プロセス用コマンドとライフサイクル条件を含む、サービスまたはタスクの定義です。**イベント**は、任意の環境変数を伴う名前付き通知です。ジョブ設定には、その目標がいつ開始または停止へ変わるかを記述できます。

システムジョブのファイルは通常、`.conf` という接尾辞を付けて `/etc/init/` の下に置きます。次に例を示します。

```text
description "Example worker"
start on runlevel [2345]
stop on runlevel [016]
exec /usr/local/sbin/example-worker
```

この例は、互換性のための入力としてランレベルイベントを使っています。システムが何をイベントとして発行するかによって、Upstart はファイルシステム、デバイス、ネットワーク、アプリケーション定義のイベントにも反応できます。

:::single-choice{#upstart-overview-start-on} Upstart の `start on` スタンザは何を定義しますか？

::option[次にコンパイルすべきカーネルのバージョン。]{#upstart-overview-kernel-version explanation="ジョブのイベント条件はカーネルビルドを選択しません。"}
::option[ジョブの目標を開始へ変えるイベント式。]{#upstart-overview-start-condition .correct explanation="式が満たされると、Upstart は設定されたジョブの開始移行を試みます。"}
::option[すべてのジョブがデータを保存するディスクパーティション。]{#upstart-overview-partition explanation="保存場所は Upstart のイベント構文とは無関係です。"}
:::

## イベント駆動の起動

起動中、Upstart はジョブ定義を読み込んでイベントを受信します。一致する `start on` または `stop on` の式によってジョブの目標が更新され、ジョブの状態移行から別のイベントが発行されて、ほかの処理が進めるようになる場合があります。互いに独立したジョブは並行して進行できます。

このモデルでは、単一の固定されたグローバルなスクリプト順序を避けられます。一方、イベント名、順序、条件が暗黙的な場合は診断が難しくなります。イベントは既定では永続的なメッセージキューではないため、後から追加したジョブや変更した条件で、過去のすべてのイベントが再送されるとは考えないでください。

:::single-choice{#upstart-overview-event-chain} ある Upstart ジョブが、別のジョブの開始につながる仕組みはどれですか？

::option[別のジョブの実行ファイルをメモリ上で書き換える。]{#upstart-overview-rewrite-binary explanation="連携はコードの変更ではなく、イベントを通じて行われます。"}
::option[すべてのジョブが必ずファイル名順に開始される。]{#upstart-overview-filename-order explanation="Upstart はファイル名順の単一起動リストではなく、イベント式を使います。"}
::option[状態移行によって、別のジョブが一致させるイベントを発行できる。]{#upstart-overview-emitted-event .correct explanation="イベント式が、独立したジョブのライフサイクル移行を結び付けます。"}
:::

## 移行と互換性

Systemd は一部の古いサービススクリプトに限定的な互換性を提供できますが、Upstart のジョブ構文をネイティブな systemd ユニットとして実行するわけではありません。移行時はファイル名を機械的に変えるのではなく、ライフサイクル条件、環境、再生成方針、ログ、依存関係、準備完了の意味を明示的に変換してください。

:::single-choice{#upstart-overview-current-ubuntu} 現在の標準的な Ubuntu リリースが使う init システムはどれですか？

::option[すべてのインストールで Upstart だけを使う。]{#upstart-overview-current-upstart explanation="それが当てはまるのは、過去の特定リリースと構成だけです。"}
::option[systemd。]{#upstart-overview-current-systemd .correct explanation="Upstart は古い世代の Ubuntu で使われ、現在のリリースは PID 1 として systemd を使います。"}
::option[init プロセスをまったく使わない。]{#upstart-overview-no-init explanation="完全な Ubuntu システムには、今も PID 1 のサービスマネージャーが必要です。"}
:::

## まとめ

Upstart を、従来のイベントとジョブのモデルとして読めるようになりました。

1. 稼働中の PID 1 と制御インターフェースを確認する。
2. ジョブ定義とイベント通知を区別する。
3. `start on` と `stop on` をライフサイクル式として解釈する。
4. 設定ファイル名だけを変えず、意味を明示的に移行する。
