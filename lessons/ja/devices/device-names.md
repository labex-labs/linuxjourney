---
lesson_id: "device-names"
course_id: "devices"
lang: "ja"
order_index: 3
title: "デバイス名"
description: "Linux における一般的なストレージデバイス、パーティション、論理デバイス、永続デバイスリンクの命名方法を学びます。"
meta_title: "デバイス名 - デバイス"
meta_description: "ストレージや周辺機器に関する一般的な Linux デバイス名の解説。SCSI ディスク（sda など）の命名規則、sda の意味、/dev/null のような疑似デバイスについて説明します。"
meta_keywords: "linux デバイス名，linux デバイス名，sda は何の略か，sd 要素名，2 番目の SCSI ディスクの最初のパーティションの一般的なデバイス名は何か，/dev, SCSI デバイス，疑似デバイス，PATA デバイス"
---

Linux のデバイス名は、必ずしもハードウェアに印字された物理コネクターではなく、インターフェースを提示するカーネルサブシステムとドライバーを反映します。一般的なパターンを理解しつつ、ストレージを変更する前には、そのシステム上の実際の対応関係を調べてください。

## SCSI 層のディスク名

SCSI ディスク層を通じて提示されるディスクには、一般に `sd` で始まる名前が使われます。これには多くの SCSI、SATA、USB ストレージ、仮想ディスクが含まれます。

- `/dev/sda`: 一つのディスク全体
- `/dev/sdb`: 別のディスク全体
- `/dev/sda3`: `/dev/sda` のパーティション3
- `/dev/sdb1`: `/dev/sdb` のパーティション1

文字は列挙順を反映しており、永続的な識別子ではありません。コントローラーの追加、ファームウェア上の順序変更、デバイスの接続によって、特定の文字が割り当てられるディスクは変わる可能性があります。

:::single-choice{#device-names-sdb-first-partition} `sd` の命名パターンで、`/dev/sdb` のパーティション1を表すパスはどれですか？

::option[`/dev/sda2`]{#device-names-sda-two explanation="これは現在 `/dev/sda` と名付けられたディスクのパーティション2を表します。"}
::option[`/dev/sdbp1`]{#device-names-sdb-p-one explanation="`p` 区切りは、基本名がすでに数字で終わるパターンで使われ、通常の `sd` 名では使いません。"}
::option[`/dev/sdb1`]{#device-names-sdb-one .correct explanation="`sd` ディスクでは、ディスク全体の名前にパーティション番号を直接追加します。"}
:::

## 数字で終わる名前

デバイス全体の名前がすでに数字で終わる場合は、パーティション名で `p` を区切りとして使います。

- `/dev/nvme0n1`: コントローラー0上の NVMe 名前空間1
- `/dev/nvme0n1p2`: その名前空間のパーティション2
- `/dev/mmcblk0`: MMC ブロックデバイス
- `/dev/mmcblk0p1`: そのデバイスのパーティション1

NVMe デバイスは通常 `/dev/sdX` とは名付けられず、NVMe サブシステムの命名規則を使います。

:::single-choice{#device-names-nvme-partition} `/dev/nvme0n1` のパーティション2を表すパスはどれですか？

::option[`/dev/nvme0n1p2`]{#device-names-nvme-p-two .correct explanation="NVMe のパーティション名では、パーティション番号の前に `p` を挿入します。"}
::option[`/dev/nvme0n12`]{#device-names-nvme-no-p explanation="区切りがなければ、末尾の数字を名前空間番号と区別できません。"}
::option[`/dev/sda2`]{#device-names-nvme-sda explanation="これは `sd` 層のディスクパーティションであり、指定された NVMe 名前空間ではありません。"}
:::

## 論理ブロックデバイスと仮想ブロックデバイス

Linux は、物理ディスクと一対一には対応しないブロックデバイスも作成します。

- `/dev/dm-N`: device mapper のデバイス。多くの場合、`/dev/mapper/` 以下に説明的なリンクもあります。
- `/dev/mdN`: Linux のソフトウェア RAID アレイ
- `/dev/loopN`: 通常ファイルを接続した loop ブロックデバイス

パーティション、暗号化層、RAID、論理ボリューム、ファイルシステムは積み重なった構造を形成します。名前だけから構造を推測せず、`lsblk` などのツールで親子関係を確認してください。

:::single-choice{#device-names-device-mapper-link} device mapper のデバイスに説明的なリンクを提供することが多い場所はどれですか？

::option[`/dev/mapper/`]{#device-names-mapper-directory .correct explanation="LVM やディスク暗号化など device mapper の利用機能は、一般にこのディレクトリに名前付きリンクを公開します。"}
::option[`/dev/null/`]{#device-names-null-directory explanation="`/dev/null` はキャラクターデバイスであり、マッピングされたブロックデバイス用のディレクトリではありません。"}
::option[`/proc/partitions/mapper/`]{#device-names-proc-mapper explanation="これは device mapper の名前付きリンクに使う通常のパスではありません。"}
:::

## 永続的なストレージリンク

ユーザー空間のデバイス管理機能は `/dev/disk/` 以下にリンクを作成します。一般的な分類は次のとおりです。

- `by-id`: ハードウェアまたはトランスポートの識別子
- `by-uuid`: ファイルシステム UUID
- `by-label`: ファイルシステムラベル
- `by-partuuid`: パーティションテーブルの UUID
- `by-path`: トポロジーに依存するパス

何を安定させる必要があるかに合わせて識別子を選びます。ファイルシステム UUID が識別するのはファイルシステムであり、その下にある物理ディスクとは限りません。ファイルシステムを複製すると UUID も重複する場合があるため、依存する前に一意性を確認してください。

:::single-choice{#device-names-persistent-config} デバイス固有の設定で、`/dev/disk/by-id/` のリンクが `/dev/sdX` より望ましいことが多いのはなぜですか？

::option[破壊的な書き込みを自動的に元へ戻せるようにするから。]{#device-names-by-id-reversible explanation="安定した名前は、スナップショット、バックアップ、書き込み保護を提供しません。"}
::option[ブロックデバイスを通常ファイルへ変換するから。]{#device-names-by-id-regular explanation="この項目はシンボリックリンクであり、解決後もブロックデバイスノードを指します。"}
::option[現在の列挙順ではなく、デバイスの識別情報から作られるから。]{#device-names-by-id-stable .correct explanation="リンク先が変わっても、識別情報に基づくリンクは認識された同じデバイスと関連付けられます。"}
:::

## 疑似デバイスの名前

`/dev/null`、`/dev/zero`、`/dev/urandom` などの名前は、物理ストレージではなくカーネルの疑似デバイスを表します。`/dev/null` は書き込みを破棄し、読み取りではファイル終端を返します。`/dev/zero` はゼロのバイト列を、`/dev/urandom` はカーネルの乱数生成器から得たバイト列を提供します。

:::single-choice{#device-names-zero-read} `/dev/zero` から読み取ると何が得られますか？

::option[未使用ストレージデバイスの一覧。]{#device-names-zero-storage-list explanation="これはバイト列を生成するキャラクターデバイスであり、検出コマンドではありません。"}
::option[値がゼロのバイト列。]{#device-names-zero-bytes .correct explanation="zero 疑似デバイスは、要求された読み取りに対して null バイトを返します。"}
::option[`/dev/null` の読み取りと同様、直ちにファイル終端。]{#device-names-zero-eof explanation="`/dev/zero` はバイト列を生成し続けますが、`/dev/null` の読み取りはファイル終端を返します。"}
:::

パーティション作業を行う前に、[Linux でハードウェアデバイスを調査する](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)を利用して、名前、永続リンク、`lsblk` の関係を比較してください。

## まとめ

一般的な Linux のストレージ名を、永続的な識別情報と誤認せずに読み解けるようになりました。

1. `sdXNUMBER` を `sd` ディスクのパーティションとして読む。
2. デバイス全体の名前が数字で終わる場合は `pNUMBER` を使う。
3. device mapper、RAID、loop デバイスなどの論理デバイスを認識する。
4. 必要な識別対象に合わせて選んだ永続リンクを優先する。
5. ストレージの名前とカーネルの疑似デバイスを区別する。
