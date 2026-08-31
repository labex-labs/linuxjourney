---
lesson_id: "disk-partitioning"
course_id: "filesystem"
lang: "ja"
order_index: 4
title: "ディスクパーティショニング"
description: "`parted` を使い、確認を優先してパーティション境界を調査、作成、サイズ変更する手順を学びます。"
meta_title: "ディスクパーティショニング - ファイルシステム"
meta_description: "parted コマンドで Linux のディスクパーティショニングを学びましょう。このガイドでは、`sudo parted -l`でのパーティションの表示、作成、サイズ変更の方法を解説します。人気のグラフィカル代替ツールである gparted も紹介します。"
meta_keywords: "Linux ディスクパーティショニング，parted コマンド，sudo parted -l, gparted, gparted Windows 代替，fdisk, ディスク管理，パーティション作成，パーティションサイズ変更，Linux ガイド"
---

パーティションの編集は、ストレージの境界を定める配置情報を変更する操作です。デバイス、開始位置、終了位置を誤ると、既存データにアクセスできなくなったり、重要なメタデータを上書きしたりします。練習には使い捨ての仮想ディスクだけを使い、価値のあるストレージを変更する前には、別の場所に保存して復元テストを済ませたバックアップを用意してください。

## ツールを選ぶ

一般的なツールには次のものがあります。

- `fdisk`：util-linux に含まれる端末用パーティションエディターで、MBR と GPT に対応する
- `parted`：GPT、MBR、そのほかのテーブル形式に対応する、端末用およびスクリプト利用可能なエディター
- `gdisk`：GPT に特化した対話型エディター
- GParted：パーティションとファイルシステムを扱うグラフィカルなフロントエンド

ツールの対応状況は変化するため、ローカルのマニュアルとディストリビューションの文書を確認してください。グラフィカルな画面でも、破壊的な操作が安全になるわけではありません。変更されるディスクメタデータは同じです。

:::single-choice{#disk-partitioning-fdisk-gpt}
現在の Linux `fdisk` について正しい説明はどれですか？

::option[MBR と GPT の両方のパーティションテーブルに対応しています。]{#disk-partitioning-fdisk-supports-gpt .correct explanation="現在の util-linux の fdisk は、DOS/MBR や GPT など複数の配置形式を編集できます。"}
::option[GPT だけを編集でき、MBR は一切扱えません。]{#disk-partitioning-fdisk-only-gpt explanation="この説明に近いのは GPT に特化した `gdisk` です。fdisk は複数のラベル形式に対応します。"}
::option[ファイルシステムは作成できますが、パーティションエントリは編集できません。]{#disk-partitioning-fdisk-filesystem-only explanation="fdisk の主な目的は、パーティションテーブルの表示と編集です。"}
:::

## 対象を特定して停止状態にする

まず、読み取り専用の一覧を確認します。

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,TRAN,PTTYPE,FSTYPE,MOUNTPOINTS
$ findmnt --real
$ sudo parted --list
```

デバイス全体を、永続的な識別情報、モデル、シリアル番号、サイズ、接続方式、トポロジーで確認してください。`/dev/sdX` だけを頼りにしてはいけません。続いて、マウント済みファイルシステム、スワップ、LVM、RAID、暗号化、コンテナ、仮想マシン、データベース、開いているファイル記述子など、すべての利用者を特定します。

関連する層は、それぞれの文書化された手順でアンマウントまたは無効化します。ツールを正常に開けるという理由だけで、稼働中のシステムディスクのパーティションテーブルを編集してはいけません。既存のテーブルを復元可能な形式で記録し、バックアップが別の障害領域に保存されていることを確認します。

:::single-choice{#disk-partitioning-target-identity}
`/dev/sdb` のようなデバイス名だけでは、対象確認として不十分なのはなぜですか？

::option[Linux はデバイス全体を `/dev` 配下に公開しないから。]{#disk-partitioning-no-whole-disks explanation="通常、ディスク全体にも `/dev` 配下のブロックデバイスノードがあります。"}
::option[デバイスやトポロジーが変わると、列挙時の名前も変わり得るから。]{#disk-partitioning-enumeration-changes .correct explanation="文字は検出順に割り当てられるため、後のセッションでは別のディスクを指す場合があります。"}
::option[パーティションツールは、オペランドにファイルシステム UUID しか受け付けないから。]{#disk-partitioning-only-uuid explanation="通常、エディターは、識別情報を確認した後のデバイス全体のパスを対象にします。"}
:::

## `parted` で 1 台のデバイスを調べる

明示的に確認したデバイス全体を開きます。

```bash
$ sudo parted /dev/VERIFIED-DISK
```

次に表示単位を統一し、テーブルを出力します。

```text
(parted) unit MiB
(parted) print free
```

`print free` は、現在のエントリと未割り当て領域を表示します。`parted` のコマンドは、最後に「保存」する操作を待たず、その場でディスクメタデータを更新することがあります。対話プロンプトは、書き込み可能な状態だと考えて扱ってください。

:::single-choice{#disk-partitioning-print-free}
`parted` の `print free` は、何を表示するのに役立ちますか？

::option[任意のファイルシステムを安全に縮小するため、削除できるファイル。]{#disk-partitioning-free-files explanation="parted が読み取るのはパーティション配置であり、ファイルシステム内部のファイル割り当てではありません。"}
::option[リモートシステム上に保存されたすべてのバックアップ。]{#disk-partitioning-remote-backups explanation="リモートバックアップの一覧は、パーティションエディターの対象外です。"}
::option[既存のパーティションエントリと未割り当て領域。]{#disk-partitioning-free-regions .correct explanation="現在のテーブルと残りの空き領域を基に、境界を選ぶ助けになります。"}
:::

## パーティションエントリを作成する

`mkpart` の正確な構文は、テーブル形式によって異なります。MiB 単位の GPT なら、次のようになります。

```text
(parted) mkpart data ext4 1MiB 5000MiB
```

これは、名前、想定する内容の種類、開始位置、終了位置を持つパーティションエントリを作成します。ext4 ファイルシステムは作成**しません**。フォーマットは独立した破壊的操作です。カーネルが目的の新しいパーティションを認識し、その識別情報を確認した後にだけ実行します。

ツールが推奨するアラインメントを使用し、終了位置を含むかどうか、どのように丸められるかを理解してください。`print` と `lsblk` で結果を確認し、指定した十進数の境界がそのまま記録されたと思い込まないようにします。

:::single-choice{#disk-partitioning-mkpart-effect}
`parted` の `mkpart` が作成するものは何ですか？

::option[ホームディレクトリを含む、マウント済みの ext4 ファイルシステム。]{#disk-partitioning-mounted-filesystem explanation="フォーマットとマウントは、パーティション作成後に行う別の操作です。"}
::option[以前のパーティション内容を収めた完全なバックアップ。]{#disk-partitioning-automatic-backup explanation="パーティションエディターが復旧用バックアップを自動的に作ることはありません。"}
::option[ファイルシステムをフォーマットしていない、パーティションテーブルのエントリ。]{#disk-partitioning-entry-only .correct explanation="ファイルシステムタイプの引数はパーティションメタデータに影響しますが、`mkfs` を実行するものではありません。"}
:::

## 境界と内容のサイズを変更する

`resizepart NUMBER END` が移動するのは、パーティションの終了境界だけです。内部に格納されたファイルシステムやほかの構造のサイズは変更しません。

操作の順序が重要です。

- 拡大する場合は、まず格納側のパーティションまたは論理デバイスを広げ、その後で専用ツールを使ってファイルシステムを拡大する
- 縮小する場合は、ファイルシステムが縮小に対応することを確認し、オフラインまたはオンラインでの要件に従って先に縮小してから、新しい終端を越えないように格納側の境界を縮める

縮小できないファイルシステムもあります。暗号化、LVM、RAID、入れ子になった構成では、順序を守るべき層がさらに増えます。また、デバイスの使用中はカーネルが変更後のテーブルの再読み込みを拒否し、新しい配置を利用する前に計画的な再起動が必要になる場合もあります。

:::single-choice{#disk-partitioning-shrink-order}
ファイルシステムが縮小に対応している場合、使用中のデータを切り落とさないための順序はどれですか？

::option[先にパーティションを縮小し、その後でファイルシステムが収まるかを確認する。]{#disk-partitioning-shrink-partition-first explanation="先にコンテナを短くすると、ファイルシステムの構造やデータを切り落とす可能性があります。"}
::option[先にファイルシステムを縮小し、その後で格納するパーティション境界を縮小する。]{#disk-partitioning-shrink-filesystem-first .correct explanation="外側のブロックデバイスを短くする前に、内容をより小さい範囲へ収める必要があります。"}
::option[パーティションテーブルを削除し、ファイルシステムに再作成させる。]{#disk-partitioning-delete-table explanation="通常の縮小処理で、ファイルシステムが安全なパーティションテーブルを再構築することはありません。"}
:::

[Linux パーティションとファイルシステムの管理](https://labex.io/ja/labs/comptia-manage-linux-partitions-and-filesystems-590845) は、指定されたセカンダリ仮想ディスクで利用してください。ホストのディスクを代わりに使ってはいけません。

## まとめ

これで、パーティション編集を、複数の層に関わる破壊的なストレージ操作として説明できるようになりました。

1. 実際のテーブルと作業手順に対応するツールを選ぶ。
2. ディスクの永続的な識別情報を確認し、すべての利用者を無効化する。
3. 書き込み前に、単位、エントリ、空き領域を確認する。
4. `mkpart` はファイルシステムを作成しないことを覚えておく。
5. 内側の内容と外側の境界を、安全な順序でサイズ変更する。
