---
lesson_id: "mounting-and-unmounting-filesystems"
course_id: "filesystem"
lang: "ja"
order_index: 6
title: "マウントとアンマウント"
description: "確認済みのソースとマウントポイントを使い、ファイルシステムを接続、確認、安全に切断する方法を学びます。"
meta_title: "マウントとアンマウント - ファイルシステム"
meta_description: "Linux で mount コマンドと umount コマンドを使用してファイルシステムをアタッチおよびデタッチする方法を学びます。このガイドでは、デバイスのマウント、安全な Linux アンマウントのための sudo umount プロセス、および UUID の使用について説明します。"
meta_keywords: "mount, umount, sudo umount, umount linux, linux アンマウント，debian umount, ファイルシステムのマウント，デバイスのアンマウント，Linux UUID, マウントポイント"
---

マウントとは、見えている名前空間内のディレクトリにファイルシステムを接続することです。ソースには、ブロックデバイス、ネットワークエクスポート、仮想ファイルシステム、バインド元、そのほか実装固有のオブジェクトを指定できます。接続先のディレクトリをマウントポイントと呼びます。

## マウントポイントを準備して確認する

ローカルの運用方針で必要な場合は、用途が分かる名前のディレクトリを作成します。

```bash
$ sudo mkdir -p /mnt/mydrive
```

マウント前に確認します。

```bash
$ findmnt --target /mnt/mydrive
$ sudo ls -la /mnt/mydrive
```

空でないディレクトリへマウントすると、既存のエントリはアンマウントするまで新しいファイルシステムの背後に隠れます。削除されるわけではありません。アプリケーションを混乱させ、見えないままディスク容量を消費することがあるため、空の専用マウントポイントを使ってください。

:::single-choice{#mount-umount-nonempty-target}
別のファイルシステムをディレクトリへマウントすると、その中にあったファイルはどうなりますか？

::option[新しいファイルシステムへ自動的にコピーされます。]{#mount-umount-copied-files explanation="マウントは名前空間の接続を変更するだけで、ディレクトリの内容を移行しません。"}
::option[カーネルによって完全に消去されます。]{#mount-umount-erased-files explanation="ファイルは削除されたのではなく隠れているため、通常はアンマウント後に再び見えるようになります。"}
::option[マウントを切断するまで隠れます。]{#mount-umount-hidden-files .correct explanation="元のディレクトリは残りますが、パス探索はマウントされたファイルシステムへ移ります。"}
:::

## 確認済みのファイルシステムをマウントする

ソースの識別情報、検出された種類、想定する内容を確認した後、明示的にマウントします。

```bash
$ sudo mount -t ext4 /dev/VERIFIED-PARTITION /mnt/mydrive
```

`-t` オプションはファイルシステムの実装を指定します。`mount` は種類を自動検出できることも多いですが、種類と検討済みのオプションを明示すると意図が明確になります。信頼できない内容やリムーバブルメディアには、ワークロードに適合する場合、`ro`、`nosuid`、`nodev`、`noexec` などの制限オプションを検討してください。ただし、それぞれに限界があり、完全なサンドボックスとして扱うことはできません。

実際にマウントされた内容を確認します。

```bash
$ findmnt --target /mnt/mydrive -o TARGET,SOURCE,FSTYPE,OPTIONS
```

マウントは名前空間単位です。コンテナやプライベートなサービス名前空間で作成したマウントは、別プロセスの表示には現れないことがあります。

:::single-choice{#mount-umount-mount-role}
この手順で `mount` コマンドが行うことは何ですか？

::option[新しいファイルシステムを作成し、ソースを消去する。]{#mount-umount-format-source explanation="ファイルシステムの作成は、別の破壊的な `mkfs` 操作です。"}
::option[ファイルシステムのソースを、マウント名前空間内のディレクトリへ接続する。]{#mount-umount-attach-filesystem .correct explanation="その後、対象より下のパス探索は接続されたファイルシステムへ入ります。"}
::option[ディスクのパーティション境界を変更する。]{#mount-umount-change-partitions explanation="パーティションテーブルの編集は、名前空間へのマウントとは別の操作です。"}
:::

## ファイルシステム UUID を使う

`/dev/sdb2` のような列挙名は変わることがあります。次のコマンドでファイルシステムの識別子を調べます。

```bash
$ lsblk -f
$ sudo blkid
```

確認済みのファイルシステムを UUID でマウントします。

```bash
$ sudo mount UUID=130b882f-7d79-436d-a096-1e594c92bb76 /mnt/mydrive
```

UUID が識別するのはファイルシステムであり、必ずしも物理ディスクではありません。再フォーマットすると変わり、複製すると重複することがあります。元のファイルシステムと複製を同じシステムへ接続する前に、一意であることを確認してください。

:::single-choice{#mount-umount-uuid-benefit}
永続的な設定で、`/dev/sdX` よりファイルシステム UUID が適していることが多いのはなぜですか？

::option[あらゆるストレージデバイスの障害を防ぐから。]{#mount-umount-uuid-no-failure explanation="識別子は、冗長性、整合性の修復、バックアップを提供しません。"}
::option[複製したファイルシステムの識別子が必ず異なると保証するから。]{#mount-umount-uuid-clone-unique explanation="ブロック単位の複製では UUID もコピーされ、競合が生じることがあります。"}
::option[現在の列挙順ではなく、ファイルシステムの識別情報に結び付いているから。]{#mount-umount-uuid-identity .correct explanation="ブロックデバイスのパスが変わっても、ファイルシステムのメタデータには UUID が残ります。"}
:::

## 安全にアンマウントする

正確なマウントポイントを指定して切断します。

```bash
$ sudo umount /mnt/mydrive
```

コマンド名は最初の `n` がない `umount` です。アンマウントに成功すると、カーネルが必要な書き戻しを完了し、参照状態が許せばファイルシステムが切断されます。ストレージを取り外す前に、`findmnt` でもう一度確認してください。

リムーバブルメディアでは、アンマウントに成功しても安全な取り外し操作が完了したとは限りません。デスクトップのストレージ機能には、デバイスキャッシュをフラッシュして USB デバイスの電源を切る、取り出しまたは電源オフ操作が用意されていることがあります。プラットフォームとハードウェアの手順に従ってください。

:::single-choice{#mount-umount-command-name}
`/mnt/mydrive` を切断するコマンドはどれですか？

::option[`umount /mnt/mydrive`]{#mount-umount-umount-correct .correct explanation="`umount` は、指定した対象にマウントされているファイルシステムを切断します。"}
::option[`unmount /mnt/mydrive`]{#mount-umount-unmount-spelling explanation="標準コマンド名には最初の `n` がありません。"}
::option[`mkfs /mnt/mydrive`]{#mount-umount-mkfs-target explanation="mkfs はファイルシステム構造を作成するため、切断には使用してはいけません。"}
:::

## 使用中のファイルシステムを診断する

開いているファイル、プロセスの作業ディレクトリ、入れ子のマウント、スワップ、そのほかのストレージ層など、名前空間にアクティブな参照が残っているとアンマウントは失敗します。すぐに強制せず、原因を調べます。

```bash
$ findmnt --submounts /mnt/mydrive
$ sudo fuser -vm /mnt/mydrive
```

シェルをツリーの外へ移動し、原因となるアプリケーションを正常に停止し、親より先に子マウントをアンマウントします。遅延アンマウントと強制オプションには特殊な意味があり、アクティブな参照が残ったりデータを失ったりするおそれがあります。文書に基づく復旧上の理由がある場合にだけ使ってください。

:::single-choice{#mount-umount-busy-cause}
`umount` がファイルシステムを使用中だと報告する原因になり得るものはどれですか？

::option[マウントポイントのディレクトリ名に小文字が含まれている。]{#mount-umount-lowercase explanation="パスの大文字と小文字だけでは、ファイルシステムへのアクティブな参照は生じません。"}
::option[プロセスの現在の作業ディレクトリがマウント内にある。]{#mount-umount-cwd-busy .correct explanation="プロセスがマウントされたファイルシステム内への参照を保持しているため、通常の切断が妨げられます。"}
::option[ファイルシステム UUID がデバイス名より長い。]{#mount-umount-uuid-length explanation="識別子の文字列長は、使用中かどうかの判定とは無関係です。"}
:::

指定された使い捨てストレージで練習するには、[Linux パーティションとファイルシステムの管理](https://labex.io/ja/labs/comptia-manage-linux-partitions-and-filesystems-590845) を利用してください。

## まとめ

これで、確認可能な範囲でファイルシステムを接続、切断できるようになりました。

1. 空の専用マウントポイントを使う。
2. ソース、種類、オプション、実際のマウント結果を確認する。
3. 永続的な参照には、一意のファイルシステム識別子を優先する。
4. 対象を指定してアンマウントし、取り外す前に切断を確認する。
5. 使用中のマウントを強制切断せず、アクティブな参照を診断する。
