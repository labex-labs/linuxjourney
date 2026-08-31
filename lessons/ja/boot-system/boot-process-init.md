---
lesson_id: "boot-process-init"
course_id: "boot-system"
lang: "ja"
order_index: 5
title: "ブートプロセス：Init"
description: "PID 1 がユーザー空間を初期化し、サービスを監督し、子プロセスを回収して、シャットダウンを調整する仕組みを学びます。"
meta_title: "ブートプロセス：Init - システムの起動"
meta_description: "この初心者向け Linux ガイドで、Linux ブートプロセスの核心を探ります。従来の System V、Upstart、そして現代の標準である systemd を含む、さまざまな Linux init システムについて学びます。これらのシステムがどのようにマシンのサービスを起動・管理するかを理解しましょう。"
meta_keywords: "Linux init, systemd, System V init, Upstart, Linux ブートプロセス，Linux チュートリアル，初心者 Linux, Linux ガイド"
---

カーネルは、PID 名前空間内の最初のユーザー空間プロセスを PID 1 として起動します。完全な Linux システムでは、この init プロセスがサービス環境を確立します。コンテナでは小さな init ラッパーやアプリケーション自体が PID 1 になることもありますが、シグナル処理と子プロセス回収に関する特別な責務は変わりません。

## PID 1 の責務

init システムは一般に、次の仕事を担います。

- サービス、ログイン、マウントなどの処理を起動・監督する
- 依存関係と設定された目標状態に従って処理順序を決める
- 孤児となった子プロセスを引き取り、終了状態を回収する
- ポリシーに従ってサービス障害へ対応する
- 正常なシャットダウンと再起動を調整する

正確な境界は実装によって異なります。デバイス管理、ネットワーク、ロギング、スケジュール実行は PID 1 に組み込まれず、init が監督する別プログラムの場合もあります。

:::single-choice{#boot-init-pid-one-role}
PID 名前空間内の PID 1 に固有の責務はどれですか？

::option[ブートのたびに全アプリケーションをソースからコンパイルする。]{#boot-init-compile-apps explanation="通常のサービス起動では、全ソフトウェアを再構築せず、インストール済みプログラムを使います。"}
::option[ディスクの物理セクターサイズを定義する。]{#boot-init-sector-size explanation="init がサービスを管理する前に、ストレージハードウェアとドライバーがセクター情報を公開します。"}
::option[孤児となった子プロセスを引き取り、終了状態を回収する。]{#boot-init-reap-orphans .correct explanation="PID 1 は最後の親となって終了状態を回収し、ゾンビの記録が蓄積しないようにします。"}
:::

## System V Init とランレベル

従来の sysvinit は `/etc/inittab` や、ランレベル別の起動・停止スクリプトを使います。ランレベルは動作モードを表しますが、番号の意味はディストリビューションごとに異なる場合があります。スクリプトの順序は規約に基づき、ディストリビューションのツールで拡張や並列化が可能です。

`/etc/init.d/` が存在するだけで、稼働中の init システムを断定してはいけません。別の実装が PID 1 のシステムにも互換スクリプトが残っている場合があります。

:::single-choice{#boot-init-sysv-runlevel}
System V のランレベルは何を表しますか？

::option[ブートローダーが選んだカーネルのバージョン番号。]{#boot-init-runlevel-kernel explanation="カーネル選択はローダーの役割であり、init のランレベルには符号化されません。"}
::option[サービス操作の組み合わせに対応する、設定済みの動作モード。]{#boot-init-runlevel-mode .correct explanation="SysV の構成では、各レベルを起動・停止スクリプトの集合や順序に関連付けます。"}
::option[ファイルシステムの現在の inode 使用率。]{#boot-init-runlevel-inodes explanation="ファイルシステムのメタデータ容量は、サービスの動作モードとは無関係です。"}
:::

## イベント駆動および依存関係ベースのシステム

Upstart はイベント駆動のジョブモデルを導入し、古い Ubuntu リリースなどで使われました。現在は主に歴史的な理解やレガシー運用の対象です。

systemd は現在の汎用ディストリビューションで広く使われています。サービス、ソケット、マウント、タイマー、デバイス、ターゲットなどを unit としてモデル化します。宣言的な依存関係とアクティベーションにより、必要な順序を守りながら独立した処理を並行して進められます。

ほかにも OpenRC、runit、s6、BusyBox init などが現役です。「最も新しいもの」を互換性の基準にせず、実際に稼働している実装を確認して、その文書を使ってください。

:::single-choice{#boot-init-systemd-unit-model}
systemd はサービスやマウントなどの管理対象をどのように表しますか？

::option[MBR のプライマリパーティションエントリとして。]{#boot-init-systemd-partitions explanation="ディスクのパーティションメタデータは、サービスマネージャーの unit とは無関係です。"}
::option[PID 1 の実行ファイルへのハードリンクだけで。]{#boot-init-systemd-hard-links explanation="unit は設定および実行時オブジェクトであり、単なる inode の別名ではありません。"}
::option[依存関係とアクティベーション関係を持つ unit として。]{#boot-init-systemd-units .correct explanation="各 unit 型は、順序、状態、監督を扱う共通モデルを提供します。"}
:::

## 稼働中の Init を特定する

インストール済みファイルから推測せず、PID 1 を調べます。

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

見える内容は権限、コンテナ、名前空間の影響を受けます。コンテナ内で実行したコマンドが示すのはその名前空間の PID 1 であり、必ずしもホストの init ではありません。特定後は、別系統の init のコマンドを混在させず、その実装固有の状態確認・ログツールを使います。

:::single-choice{#boot-init-detect-running}
従来のスクリプトディレクトリの有無より、PID 1 を調べるほうがよいのはなぜですか？

::option[PID 1 の実行ファイル名は全 Linux システムで同じだから。]{#boot-init-same-name explanation="systemd、sysvinit、BusyBox、コンテナ用 init など、さまざまなプログラムが PID 1 になります。"}
::option[別の init 実装が稼働していても互換ファイルが存在し得るから。]{#boot-init-compatibility-files .correct explanation="実際に動く PID 1 の実行ファイルは、稼働中の init システムを示すより強い証拠です。"}
::option[従来のディレクトリはブートのたびに自動削除されるから。]{#boot-init-directories-deleted explanation="インストール済みの互換ファイルはブート後も残ることがあります。"}
:::

## まとめ

これで、init を一つの必須実装ではなく、役割として説明できます。

1. PID 1 をサービス初期化、子プロセス回収、シャットダウンと関連付ける。
2. System V のランレベルをディストリビューション定義の動作モードとして認識する。
3. systemd のリソースと依存関係を unit に関連付ける。
4. ツールを選ぶ前に、該当する名前空間で実際の PID 1 を調べる。
