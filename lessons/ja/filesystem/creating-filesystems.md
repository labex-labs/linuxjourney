---
lesson_id: "creating-filesystems"
course_id: "filesystem"
lang: "ja"
order_index: 5
title: "ファイルシステムの作成"
description: "ブロックデバイスの対象を確認し、形式ごとのツールでファイルシステムを作成する方法を学びます。"
meta_title: "ファイルシステムの作成 - ファイルシステム"
meta_description: "mkfs コマンドを使用して Linux パーティション上にファイルシステムを作成する方法を学びます。この初心者向けガイドでは、ディスク管理、ext4 によるフォーマット、および Linux パーティショニングの必須手順を解説します。"
meta_keywords: "mkfs, ファイルシステム作成，ext4, Linux パーティショニング，Linux チュートリアル，初心者 Linux, ディスク管理，Linux ガイド，Linux ディスクフォーマット"
---

ファイルシステムを作成すると、ブロックデバイスに新しい割り当て構造とメタデータ構造が書き込まれます。これは単なるラベル変更ではなく、破壊的な初期化です。練習には使い捨てのストレージだけを使用し、価値のあるデータが入っていたデバイスをフォーマットする前には、復元テスト済みのバックアップを用意してください。

## `mkfs` を理解する

`mkfs` は通常、`mkfs.ext4`、`mkfs.xfs`、`mkfs.btrfs` など、ファイルシステム固有のプログラムへ処理を振り分けるフロントエンドです。一般的なコマンド形式は次のとおりです。

```bash
$ sudo mkfs -t ext4 /dev/VERIFIED-PARTITION
```

プレースホルダーは、対象を確認した後にだけ置き換えてください。形式固有の同等な構文は、一般に次のようになります。

```bash
$ sudo mkfs.ext4 /dev/VERIFIED-PARTITION
```

利用できるオプション、既定値、機能セット、上書き確認は実装ごとに異なります。すべての `mkfs` バックエンドが同じ動作をすると思い込まず、実際に使うフォーマッターのローカルマニュアルを読んでください。

:::single-choice{#creating-filesystems-mkfs-role}
`mkfs -t ext4 TARGET` は、何を要求するコマンドですか？

::option[既存のファイルシステムを変更せずにマウントすること。]{#creating-filesystems-mount-existing explanation="マウントは別の操作です。mkfs はデバイス上のメタデータを初期化します。"}
::option[対象に ext4 ファイルシステムの構造を作成すること。]{#creating-filesystems-create-ext4 .correct explanation="フロントエンドが、指定したブロックデバイスに対する ext4 のフォーマット実装を選択します。"}
::option[現在マウントされている全ファイルシステムを一覧表示すること。]{#creating-filesystems-list-mounted explanation="読み取り専用のマウント一覧には `findmnt` などのツールを使います。"}
:::

## すべてのストレージ層を確認する

フォーマットする前に、モデル、シリアル番号、サイズ、トポロジー、永続的なリンク、用途によって対象を識別します。

```bash
$ lsblk -o NAME,PATH,TYPE,SIZE,MODEL,SERIAL,FSTYPE,UUID,MOUNTPOINTS
$ findmnt --real
$ sudo wipefs --no-act /dev/VERIFIED-PARTITION
```

`wipefs --no-act` は、認識されたシグネチャを消去せずに報告します。スワップ、LVM、RAID、暗号化、仮想マシン、コンテナ、アプリケーションによる使用状況も確認してください。`MOUNTPOINTS` が空でも、デバイスが使用中の場合があります。

関連する層は、それぞれに対応するツールでアンマウントまたは無効化します。列挙時の名前は変わり得るため、フォーマッターを実行する直前にもう一度対象を確認してください。

:::single-choice{#creating-filesystems-wipefs-no-act}
この手順で `wipefs --no-act TARGET` が提供するものは何ですか？

::option[認識されたシグネチャの読み取り専用レポート。]{#creating-filesystems-signature-report .correct explanation="no-act モードでは、ファイルシステム、パーティションテーブル、RAID などのシグネチャを削除せずに確認できます。"}
::option[マウント可能な、新しい空のファイルシステム。]{#creating-filesystems-wipefs-formats explanation="シグネチャを調べるだけでは、新しいファイルシステムは初期化されません。"}
::option[対象を使用しているプロセスがないという保証。]{#creating-filesystems-wipefs-no-users explanation="使用状況は、マウントとストレージスタック全体にわたって別途確認する必要があります。"}
:::

## ファイルシステムを意図的に選ぶ

ディストリビューション、ブート環境、バックアップツール、修復ツール、ワークロードが対応する形式を選びます。必要な上限、スナップショット、チェックサム、クォータ、暗号化の層、拡大や縮小の可否、ほかのプラットフォームからのアクセスを検討してください。

単に広く使われているという理由だけで形式を選んではいけません。たとえば ext4、XFS、Btrfs では運用上の機能や復旧手順が異なります。相互運用のためのリムーバブルデバイスでは、Unix のパーミッションとは異なる意味を持つ別形式が必要になることもあります。

:::single-choice{#creating-filesystems-type-choice}
ファイルシステムの種類を選ぶ際の、妥当な基準はどれですか？

::option[入力する名前が最も短いもの。]{#creating-filesystems-shortest-name explanation="コマンド名の長さから、耐久性、機能、対応状況は判断できません。"}
::option[今後ストレージ障害が一切起きないという保証。]{#creating-filesystems-no-failure explanation="ハードウェア障害やバックアップの必要性をなくせるファイルシステムはありません。"}
::option[ワークロードの要件と、対応するバックアップ、ブート、復旧ツール。]{#creating-filesystems-supported-workflow .correct explanation="技術要件に適合し、運用環境で管理と復旧が可能な形式を選ぶ必要があります。"}
:::

## ラベル、UUID、検証

通常、フォーマッターはファイルシステム UUID を生成し、人が読めるラベルも設定できます。環境内で十分に一意なラベルを使い、複製したファイルシステムを同時にマウントする場合は識別子が競合しないようにしてください。

作成に成功したら、マウントせずに確認します。

```bash
$ lsblk -f /dev/VERIFIED-PARTITION
$ sudo blkid /dev/VERIFIED-PARTITION
```

後でマウントを設定できるよう、UUID を記録します。ファイルシステムを作成しても、マウント、アプリケーション用ディレクトリの作成、バックアップ内容の復元、起動後も有効な永続設定は行われません。

:::single-choice{#creating-filesystems-after-mkfs}
ファイルシステムを作成した後も、別途必要な手順はどれですか？

::option[目的のディレクトリへマウントすること。]{#creating-filesystems-mount-separate .correct explanation="フォーマットはファイルシステム構造を書き込み、マウントはそのファイルシステムを見えるディレクトリツリーへ接続します。"}
::option[ブロックデバイスへ何らかの容量を割り当てること。]{#creating-filesystems-capacity explanation="フォーマット対象の容量は、基になるパーティションや論理デバイスがすでに提供しています。"}
::option[カーネルの `/dev` ディレクトリを一から作成すること。]{#creating-filesystems-create-dev explanation="デバイスノードの管理は、1 つの対象をフォーマットする操作とは独立しています。"}
:::

[Linux パーティションとファイルシステムの管理](https://labex.io/ja/labs/comptia-manage-linux-partitions-and-filesystems-590845) は、ラボの使い捨てセカンダリディスクだけで利用してください。

## まとめ

これで、ファイルシステムの作成を、対象確認を伴う破壊的操作として説明できるようになりました。

1. `mkfs` を、形式固有のツールへ処理を振り分けるものとして扱う。
2. 永続的な識別情報、シグネチャ、使用中のすべてのコンシューマーを確認する。
3. 対応状況と復旧要件を基にファイルシステムを選ぶ。
4. マウント前に、生成された種類、ラベル、UUID を確認する。
