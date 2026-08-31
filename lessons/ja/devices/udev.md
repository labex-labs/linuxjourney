---
lesson_id: "udev"
course_id: "devices"
lang: "ja"
order_index: 5
title: "udev"
description: "udev がカーネルのデバイスイベントを処理し、ポリシー、権限、永続リンクを適用する仕組みを学びます。"
meta_title: "udev - デバイス"
meta_description: "udev、Linux デバイスファイルの動的な管理方法、および udevadm の使用方法について学びます。初心者向けのデバイスノード作成を理解します。"
meta_keywords: "udev, udevadm, Linux デバイス管理，デバイスファイル，Linux チュートリアル，初心者 Linux, udev ルール，Linux ガイド"
---

Linux カーネルは uevent を通じて、デバイスの変化をユーザー空間へ通知します。現在の多くのディストリビューションでは、`systemd-udevd` が udev ルールとデバイスデータベースを使ってイベントを処理します。カーネルが生成する `devtmpfs` と組み合わさり、アプリケーションが `/dev` 周辺で目にする所有者、権限、属性、シンボリックリンクが作られます。

## カーネルイベントからデバイスポリシーへ

デバイスが追加、変更、移動、削除されると、udev は次の処理を行えます。

- sysfs の属性とイベントプロパティを読み取る
- デバイスノードへ所有者、グループ、モードのポリシーを適用する
- `/dev/disk/by-id/...` などの安定したシンボリックリンクを追加する
- 他のサービス向けにデバイスへタグを付ける
- 範囲を限定した補助処理を実行する

実際のデバイスとドライバーを担当するのは、引き続きカーネルです。`/dev` からノードを削除してもハードウェアが物理的に取り外されるわけではなく、`mknod` でノードを手動作成しても、未対応のハードウェアが出現したりドライバーがバインドされたりはしません。

:::single-choice{#udev-kernel-event-input}
デバイスの変化に対する udev の処理は、通常何によって開始されますか？

::option[APT によるパッケージリポジトリの更新。]{#udev-apt-refresh explanation="パッケージメタデータの更新は、稼働中のデバイスイベント処理とは無関係です。"}
::option[ユーザーが `/dev` 以下の全ファイルを手動で改名すること。]{#udev-manual-renaming explanation="動的ポリシーは、手動の一括改名ではなくカーネルイベントとルールによって駆動されます。"}
::option[デバイス操作を記述するカーネルの uevent。]{#udev-kernel-uevent .correct explanation="Udev はカーネルからデバイスイベントを受け取り、一致するユーザー空間ルールを適用します。"}
:::

## ルールの場所と優先順位

ルールは一般に次の場所にあります。

- `/usr/lib/udev/rules.d/`: ベンダーまたはパッケージが提供するルール
- `/run/udev/rules.d/`: 揮発性のランタイムルール
- `/etc/udev/rules.d/`: ローカル管理者のポリシー

ファイルはファイル名の辞書順で処理され、同名ファイルがある場合は、インストールされた udev 実装の規則に従い、優先度の高いディレクトリのものが低いディレクトリのものを置き換えます。ローカルルールには意図の明確なファイル名を付け、列挙名ではなく安定した属性に一致させてください。

一つのルールが一致するすべてのデバイスへ影響し得るため、範囲を慎重にテストします。ローカルな上書きまたは補足ルールで対応できる場合は、パッケージのルールを直接編集してはいけません。

:::single-choice{#udev-local-rules-directory}
ローカル管理者の永続的な udev ルールを置くためのディレクトリはどれですか？

::option[`/proc/udev/rules.d/`]{#udev-proc-rules explanation="Procfs は永続的なローカルルール用ディレクトリを提供しません。"}
::option[`/etc/udev/rules.d/`]{#udev-etc-rules .correct explanation="ローカルポリシーは、パッケージ管理されるベンダールールと分けて `/etc` 以下へ置きます。"}
::option[`/dev/udev/rules.d/`]{#udev-dev-rules explanation="`/dev` にあるのは実行時のデバイス向けオブジェクトであり、永続的なルール設定ではありません。"}
:::

## `udevadm` でデバイスを調べる

既存のノードについて udev のプロパティを問い合わせます。

```bash
$ udevadm info --query=all --name=/dev/sda
```

現在のシステムに存在するノードを使ってください。`udevadm info --attribute-walk --name=...` は sysfs の親階層に沿って属性を表示でき、ルールの作成に役立ちます。`udevadm monitor --kernel --udev --property` はカーネルイベントと処理済みイベントを監視します。デバイス識別子が現れる場合があるため、記録した出力は適切に扱ってください。

:::single-choice{#udev-info-purpose}
`udevadm info --query=all --name=/dev/sda` は何を要求しますか？

::option[ディスクのパーティションテーブルを破壊的に書き換えること。]{#udev-info-partition-write explanation="これは調査用の問い合わせであり、ストレージのフォーマットや再パーティションは行いません。"}
::option[不足しているカーネルドライバーをインターネットからインストールすること。]{#udev-info-install-driver explanation="Udevadm の調査機能はパッケージダウンローダーではありません。"}
::option[指定したデバイスノードについて既知の udev プロパティ。]{#udev-info-properties .correct explanation="info コマンドはデバイスデータベースと関連する sysfs 情報を問い合わせます。"}
:::

## ルール変更を慎重に適用する

ルールファイルを再読み込みすると、今後のイベント処理が変わります。既存デバイスの状態がすべて自動的に再構築されるわけではありません。手動でイベントを発生させると多数のデバイスやサービスへ影響する場合があるため、対象を絞り、インストール済み `udevadm` の文書に従ってください。テストコマンドでルール評価を模擬できますが、実イベントの副作用をすべて再現できるとは限りません。

権限や名前を変更する前に、ローカルルールをバックアップし、構文を検証し、既知のテストデバイス一つを観察し、復旧手段を確保します。udev のイベント処理内で長時間かかる作業を直接行わず、適切なサービスへ委ねてください。

:::single-choice{#udev-reload-effect}
udev ルールの再読み込みによって主に変わるものは何ですか？

::option[それ以降に一致するデバイスイベントの処理方法。]{#udev-future-events .correct explanation="再読み込みはメモリ上のルールを更新します。デバイスを再評価するには、その後にイベントが起きるか、意図的に発生させる必要があります。"}
::option[接続されたすべてのデバイスの物理配線。]{#udev-physical-wiring explanation="ソフトウェアのルールを読み込んでも、ハードウェア接続は変更できません。"}
::option[イベントや一致条件にかかわらず、既存の全デバイスノード。]{#udev-all-existing explanation="再読み込みだけで、現在の全デバイスが直ちに再評価されるとは限りません。"}
:::

[Linux でハードウェアデバイスを調査する](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)を利用して、管理された環境で `udevadm` のプロパティ、sysfs パス、`/dev` のリンクを対応付けてください。

## まとめ

udev を、カーネルイベントとユーザー空間のデバイスポリシーの間に位置付けられるようになりました。

1. uevent と sysfs 属性を udev ルールの照合に関連付ける。
2. ベンダー、ランタイム、ローカルのルール配置を区別する。
3. `udevadm` でプロパティとイベントの流れを調べる。
4. 狭くテストした範囲だけでルールを再読み込みし、イベントを発生させる。
