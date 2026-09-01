---
lesson_id: "sysv-overview"
course_id: "init"
lang: "ja"
order_index: 1
title: "System V の概要"
description: "従来の System V init が、ランレベルと順序付けられたサービススクリプトのリンクをどう使うか学びます。"
meta_title: "System V の概要 - Init"
meta_description: "SysV または init v としても知られる従来の System V init システムを探ります。このガイドでは、systemv がプロセスをどのように管理するか、その逐次起動、および Linux におけるランレベルの役割について説明します。古典的な initv プロセスの基本を学びましょう。"
meta_keywords: "System V, systemv, SysV init, systemv init, init v, initv, Linux ランレベル，init システム，プロセス管理，Linux チュートリアル"
---

System V init は通常 SysV init または sysvinit と呼ばれ、従来から使われてきた PID 1 とサービス起動の仕組みです。古いシステムや互換スクリプトを扱ううえで今も重要ですが、SysV 形式のファイルがインストールされているだけでは、実行中の PID 1 が sysvinit であるとは断定できません。

## 稼働中の init システムを特定する

実際に動いている PID 1 を調べます。

```bash
$ ps -p 1 -o pid,comm,args=
$ readlink /proc/1/exe
```

`/etc/inittab` ファイルや `/etc/init.d/` ディレクトリがあることは、補助的な証拠にすぎません。systemd などの init システムも互換性のためにこれらを残すことがあり、コンテナではホストと異なる PID 名前空間が見える場合もあります。

:::single-choice{#sysv-overview-detection} sysvinit が稼働中であることを示す最も強い証拠はどれですか？

::option[実行中の PID 1 の実行ファイルが sysvinit またはその init プログラムであること。]{#sysv-overview-live-pid-one .correct explanation="互換用ファイルから推測するより、実際に動く最初のプロセスを調べる方が直接的です。"}
::option[`/etc/init.d/` ディレクトリが存在すること。]{#sysv-overview-init-d-only explanation="ほかの init システムも SysV スクリプトやラッパーを残すことがよくあります。"}
::option[パッケージの説明に service という語が含まれること。]{#sysv-overview-package-word explanation="パッケージの文章から、現在 PID 1 として動くプロセスは特定できません。"}
:::

## ランレベル

ランレベルとは、数値で名前を付けた動作モードです。SysV の設定では伝統的に `0` から `6` と特殊なレベルを使いますが、その意味は普遍的な規則ではなく、ディストリビューションの方針で決まります。一般的な慣例は次のとおりです。

- `0`：停止または電源オフへの移行
- `1` または `S`：シングルユーザーまたはレスキューモード
- `2` から `5`：ディストリビューションが定義するマルチユーザーモード
- `6`：再起動への移行

Debian 系では歴史的にレベル 2～5 をほぼ同じように扱い、Red Hat 系の慣例ではテキストモードとグラフィカルモードを区別します。実際のホストで `/etc/inittab`、init の文書、ランレベルディレクトリを調べてください。

:::single-choice{#sysv-overview-shutdown-runlevel} 多くの SysV システムで、停止または電源オフを要求するランレベルは慣例上どれですか？

::option[`3`]{#sysv-overview-runlevel-three explanation="これは通常、シャットダウンではなくマルチユーザーの動作モードです。"}
::option[`0`]{#sysv-overview-runlevel-zero .correct explanation="通常はレベル0がシャットダウンへの移行ですが、ローカルの init 方針が最終的な基準です。"}
::option[`6`]{#sysv-overview-runlevel-six explanation="通常、レベル6は再起動を要求します。"}
:::

## init スクリプトとランレベルのリンク

サービススクリプトは通常 `/etc/init.d/` の下にあります。`/etc/rc2.d/` や `/etc/rc.d/rc2.d/` などのランレベルディレクトリには、移行時の操作と順序を名前に符号化したリンクがあります。

- `SNNname` のリンクは開始操作を要求します。
- `KNNname` のリンクは停止操作を要求します。
- `NN` は、その移行におけるリンクの辞書順を定めます。

正確なアルゴリズムとディレクトリは環境によって異なります。依存関係をスクリプトのヘッダーに記述してディストリビューションのツールで処理する場合や、一部の処理を並列化する実装もあります。SysV を「すべてのサービスが必ず1つずつ順番に起動する仕組み」と単純化してはいけません。

:::single-choice{#sysv-overview-start-link} ランレベルへ移行するとき、`S20networking` というリンクは慣例上何を要求しますか？

::option[すべてのネットワークプロセスへシグナル20を直接送る。]{#sysv-overview-signal-twenty explanation="数字は順序のメタデータであり、シグナル番号ではありません。"}
::option[ネットワーク設定のバックアップを20個保存する。]{#sysv-overview-twenty-backups explanation="ランレベルのリンクにバックアップ保存機能はありません。"}
::option[`S` の順序に従い、リンク先のサービススクリプトを start 操作で実行する。]{#sysv-overview-start-action .correct explanation="接頭辞は起動用リンクを表し、数字は実行順序に関与します。"}
:::

## ランレベル間を移行する

init がランレベルを変更すると、ディストリビューションの rc 機構は不要になったサービスを停止し、新しいモードで必要なサービスを起動します。スクリプトは、状態確認や移行操作を繰り返しても扱える程度に冪等で、意味のあるステータスを返す必要があります。

ランレベル 0 または 6 の要求は、システム全体の可用性を失わせる操作です。生の init 移行を不用意に呼び出さず、システムのシャットダウン用インターフェースを使い、ユーザーへ通知し、作業中の内容を保存し、リモートコンソールへ接続できることを確認してください。

:::single-choice{#sysv-overview-runlevel-six-meaning} ランレベル `6` は慣例上何を要求しますか？

::option[ユーザーアカウントを6個追加すること。]{#sysv-overview-six-users explanation="ランレベルは動作モードを表し、アカウント数ではありません。"}
::option[システムの再起動への移行。]{#sysv-overview-reboot .correct explanation="従来の SysV 方針では、サービスを停止してシステムを再起動するためにレベル6を使います。"}
::option[すべてのファイルシステムを永久に読み取り専用でマウントすること。]{#sysv-overview-six-readonly explanation="これはランレベル6の一般的な目的ではありません。"}
:::

## 互換機能の限界

systemd ホストでは、SysV スクリプトが生成ユニットとしてラップされる場合がありますが、それでも systemd の依存関係、タイムアウト、ログ、状態の意味が適用されます。古いスクリプトを直接実行すると、サービスマネージャーの追跡を迂回することがあります。稼働中のマネージャーを特定し、可能ならそのネイティブなインターフェースを使ってください。

:::single-choice{#sysv-overview-compatibility-script} systemd ホスト上の SysV 形式スクリプトを、通常はサービスマネージャー経由で呼び出すべきなのはなぜですか？

::option[直接実行すると、依存関係や状態の追跡を迂回する場合があるから。]{#sysv-overview-manager-tracking .correct explanation="マネージャーはプロセスの所有関係、順序、タイムアウト、状態を協調して管理する必要があります。"}
::option[systemd システムではシェルスクリプトを実行できないから。]{#sysv-overview-scripts-impossible explanation="実行はできますが、監督を迂回すると状態の不整合が起こる場合があります。"}
::option[systemd がすべてのサービススクリプトをカーネルモジュールへ変換するから。]{#sysv-overview-script-module explanation="互換ユニットもユーザー空間のサービス管理です。"}
:::

## まとめ

従来の SysV 構成が実際に稼働中だと思い込まず、その内容を解釈できるようになりました。

1. init コマンドを選ぶ前に、実行中の PID 1 を特定する。
2. ランレベルの意味を、ディストリビューションが定める慣例として扱う。
3. ランレベルリンクの `S`、`K`、数字による順序を読み取る。
4. レベル 0 と 6 では、制御されたシャットダウン手順を使う。
5. 互換スクリプトがある場合も、稼働中のマネージャーを尊重する。
