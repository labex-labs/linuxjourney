---
lesson_id: "sysfs"
course_id: "devices"
lang: "ja"
order_index: 4
title: "sysfs"
description: "sysfs が `/sys` 以下に Linux カーネルの稼働中のデバイス、ドライバー、バス、クラスモデルを公開する仕組みを学びます。"
meta_title: "sysfs - デバイス"
meta_description: "sysfs とは何か、また Linux の sys システムにおけるその役割を探ります。このガイドでは、デバイス情報のための仮想ファイルシステムである Linux の/sys ディレクトリについて解説し、/dev との違いを対比します。"
meta_keywords: "sysfs, sysfs とは，/sys, linux /sys, linux sys, sys システム，仮想ファイルシステム，linux デバイス，/dev"
---

`sysfs` は通常 `/sys` にマウントされる仮想ファイルシステムです。ディレクトリ、シンボリックリンク、小さな属性ファイルを通じて、カーネルオブジェクトとその関係を表します。デバイス検出ツールやデバイスマネージャーは、カーネルの現在のデバイスモデルを把握するために sysfs を使います。

## デバイスモデルをたどる

重要なトップレベルのビューには次のものがあります。

- `/sys/devices/`: 物理デバイスと論理デバイスの階層
- `/sys/class/`: block や network など、機能クラス別にまとめたデバイス
- `/sys/bus/`: バス、そのデバイス、ドライバー
- `/sys/block/`: ブロックデバイスの便利なビュー
- `/sys/dev/`: キャラクターまたはブロックのメジャー番号とマイナー番号で索引付けされたリンク

`/sys/devices` 以外にある多くの項目は、正規の階層を指すシンボリックリンクです。実際の親パスが必要なら、`readlink -f` でリンクを解決します。

```bash
$ readlink -f /sys/class/block/sda
```

異なるストレージインターフェースを使うシステムには、この例の名前が存在しない場合があります。

:::single-choice{#sysfs-canonical-device-tree} カーネルの主要なデバイス階層を含む sysfs のサブツリーはどれですか？

::option[`/sys/passwords/`]{#sysfs-passwords-tree explanation="Sysfs はユーザー認証情報の保管場所ではありません。"}
::option[`/sys/devices/`]{#sysfs-devices-tree .correct explanation="devices サブツリーはデバイスの親子トポロジーを表し、class や bus のビューはここへリンクします。"}
::option[`/sys/packages/`]{#sysfs-packages-tree explanation="インストール済みパッケージの状態は、ここではなくディストリビューションのパッケージツールが管理します。"}
:::

## 属性を読み取る

属性ファイルは、個別の値や制御を公開します。ブロックデバイスでは、次のような例があります。

```bash
$ cat /sys/class/block/sda/dev
8:0
$ cat /sys/class/block/sda/ro
0
$ cat /sys/class/block/sda/size
1953525168
```

`dev` はメジャー番号とマイナー番号を報告します。`ro` はブロックデバイスの読み取り専用フラグです。Linux のブロックデバイスでは、`size` は物理セクターサイズにかかわらず、慣例として512バイトセクター単位で表されます。特定の属性の単位と意味は、必ずカーネル ABI の文書で確認してください。

:::single-choice{#sysfs-dev-attribute} ブロックデバイスの sysfs `dev` 属性には通常何が含まれますか？

::option[そのデバイスに現在保存されている全ファイル。]{#sysfs-file-list explanation="ファイルシステムのディレクトリツリーが、この小さなデバイス属性に埋め込まれることはありません。"}
::option[ハードウェアをインストールしたパッケージ名。]{#sysfs-package-name explanation="ハードウェアは `dev` 属性で識別されるパッケージとしてインストールされるわけではありません。"}
::option[デバイスのメジャー番号とマイナー番号。]{#sysfs-major-minor .correct explanation="この属性によって sysfs オブジェクトが対応するブロックデバイス識別情報と結び付けられます。"}
:::

## `/sys` と `/dev` の関係

`/dev` には、アプリケーションがデバイス I/O のために開くノードがあります。`/sys` は、オブジェクトの関係、属性、状態、選択された制御を公開します。`/dev/sda` のようなブロックノードは `/sys/dev/block/8:0` と対応付けられ、後者を解決すると該当する sysfs オブジェクトへ到達します。

二つのインターフェースは互いを補完します。どちらか一方だけにハードウェアの全情報が揃っているわけではなく、調査中にデバイスが消えることもあります。

:::single-choice{#sysfs-versus-dev} `/sys` と `/dev` を正しく区別している説明はどれですか？

::option[`/sys` はユーザー文書を、`/dev` はパッケージアーカイブを保存する。]{#sysfs-dev-user-files explanation="どちらのディレクトリも、そのような通常データの保存用途ではありません。"}
::option[`/sys` はカーネルオブジェクトの属性を公開し、`/dev` は I/O 用のデバイスノードを提供する。]{#sysfs-dev-distinction .correct explanation="Sysfs はオブジェクトと制御をモデル化し、デバイスノードは操作をキャラクターまたはブロックドライバーへ送ります。"}
::option[どちらもインストール時に一度だけ作成される静的な一覧である。]{#sysfs-dev-static explanation="表示される状態は、デバイスやカーネルオブジェクトの出現と消失に応じて変化します。"}
:::

## 属性へ安全に書き込む

sysfs の属性には書き込み可能なものもあり、電源状態、ドライバーのバインド、キューの動作、デバイスの認可、LED など、稼働中の制御を変更できます。テキストの書き込みが成功すると、ハードウェアやサービスへ直ちに影響する場合があります。永続設定ファイルの編集と同じではありません。

文書化された ABI と現在値を読み、設定を永続化する正しい方法を確認したうえで、許可されたシステムだけでテストしてください。`/sys` 全体の権限を再帰的に編集したり、推測した値を書き込んだりしてはいけません。

:::single-choice{#sysfs-write-risk} sysfs 属性への書き込みが運用上重要な操作になり得るのはなぜですか？

::option[すべての書き込みで通常のバックアップコピーがディスク上に作られるから。]{#sysfs-backup-copy explanation="Sysfs は仮想ファイルシステムであり、制御変更の自動バックアップは提供しません。"}
::option[属性が書き込み可能でも、sysfs はすべての書き込みを無視するから。]{#sysfs-ignore-writes explanation="書き込み可能属性は、対応する制御値を受け付けるために存在します。"}
::option[書き込みによって、稼働中のカーネルまたはドライバーの制御を呼び出せるから。]{#sysfs-live-control .correct explanation="書き込み可能属性は能動的なインターフェースであり、デバイスの動作を直ちに変更する場合があります。"}
:::

[Linux でハードウェアデバイスを調査する](https://labex.io/labs/comptia-explore-hardware-devices-in-linux-590861)を利用して、sysfs を読み取り専用でたどり、デバイスノードと対応付けてください。

## まとめ

sysfs を、稼働中のカーネルオブジェクトを構造化して示すビューとして使えるようになりました。

1. デバイス、クラス、バス、ブロック、デバイス番号の各ビューをたどる。
2. 文書化された属性を、正しい単位で一つずつ読み取る。
3. sysfs オブジェクトと `/dev` ノードを対応付ける。
4. 書き込み可能属性を、稼働中の制御インターフェースとして扱う。
