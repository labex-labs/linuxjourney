---
lesson_id: "nfs-network-file-share"
course_id: "network-sharing"
lang: "ja"
order_index: 4
title: "NFS"
description: "NFS クライアントマウントを検出、マウント、検証し、安全に自動化する方法を学びます。"
meta_title: "NFS - ネットワーク共有"
meta_description: "Linux でのネットワークファイルシステム（NFS）の使用方法を発見してください。このレッスンでは、NFS クライアントの設定、mount コマンドの使用、ネットワーク共有へのシームレスなアクセスを実現するための automount の設定について解説します。"
meta_keywords: "NFS, NFS クライアント，automount, ネットワークファイルシステム，Linux ネットワーキング，mount コマンド，Linux チュートリアル，初心者"
---

Network File System（NFS）を使うと、クライアントはサーバーの export へローカルファイルシステムの名前空間からアクセスできます。サーバーは export とアクセス方針の多くを制御し、クライアントは許可済み export をどこへ、いつマウントするかを制御します。

## クライアントを準備する

ディストリビューションの NFS クライアントユーティリティをインストールします。Debian 系では通常 `nfs-common`、Red Hat 系では `nfs-utils` です。DNS またはアドレスへの到達性、許可された NFS バージョン、ファイアウォールポリシー、正確な export パスをサーバー管理者と確認してください。

`showmount -e SERVER` は旧来の mount プロトコルを通じて提供される export を一覧表示できますが、すべての NFSv4 専用サーバーに対して決定的な情報ではありません。一覧取得に失敗しても、許可済み NFSv4 export が存在しないとは証明できません。

:::single-choice{#nfs-showmount-limit} NFSv4 サーバーに対して `showmount -e` の結果が不完全になり得るのはなぜですか？

::option[公開されていない可能性のある旧式の export 一覧プロトコルへ問い合わせるから。]{#nfs-showmount-protocol .correct explanation="NFSv4 は、その独立した一覧サービスを提供しなくても動作できます。"}
::option[ローカル CPU の温度しか表示しないから。]{#nfs-showmount-temperature explanation="このコマンドが扱うのは NFS サーバーの export 情報です。"}
::option[一覧にあるすべての export を恒久的に無効化するから。]{#nfs-showmount-disables explanation="一覧取得は読み取り専用の検出要求です。"}
:::

## Export をマウントする

空の専用マウントポイントを作り、承認済み export をマウントします。

```bash
$ sudo mkdir -p /mnt/team
$ sudo mount -t nfs server.example.net:/srv/team /mnt/team
```

ポリシーまたは互換性のために必要な場合だけ、たとえば `-o vers=4.2` とバージョンを指定します。性能やセキュリティのオプションを推測で指定してはいけません。結果のコピー元、種類、オプションを確認します。

```bash
$ findmnt --target /mnt/team
```

:::single-choice{#nfs-mount-operands} mount コマンド内の `server.example.net:/srv/team` は何ですか？

::option[リモート export を隠すローカルディレクトリ。]{#nfs-local-mountpoint explanation="例のローカルマウントポイントは `/mnt/team` です。"}
::option[インストールするクライアントパッケージ名。]{#nfs-package-name explanation="パッケージ名はディストリビューションごとに異なり、mount のコピー元オペランドではありません。"}
::option[サーバーと、export されたリモートパス。]{#nfs-remote-export .correct explanation="ホストとコロンに続くパスが NFS のコピー元を識別します。"}
:::

## ID と権限を理解する

NFS のアクセスには、サーバーの export ルール、プロトコルのセキュリティ、数値 ID またはディレクトリサービス、ファイルシステム権限が組み合わさります。二つのホストで同じユーザー名が表示されても、数値 ID が一致するとは限りません。従来の `AUTH_SYS` はクライアント提供の数値 ID を送り、信頼できるクライアントとネットワーク制御に大きく依存します。より強い環境では、エンドツーエンドに設定された Kerberos セキュリティモードを利用できます。

サーバーは通常、root squashing によりリモート root を非特権 ID へ割り当てます。権限エラーを解決するだけのために、この保護を無効にしないでください。ID、ディレクトリ所有権、export ポリシー、意図したセキュリティモデルを調べます。

:::single-choice{#nfs-name-versus-id} 表示名が同じ二人のユーザーでも、NFS 権限が異なる場合があるのはなぜですか？

::option[NFS 権限が数値 ID の対応付けに依存する場合があるから。]{#nfs-numeric-mapping .correct explanation="名前が一致するだけでは、クライアントとサーバーが同じ UID とグループを解決するとは限りません。"}
::option[NFS がすべてのファイルシステム権限を無視するから。]{#nfs-ignores-permissions explanation="ファイルシステムと export の権限は、引き続き認可の一部です。"}
::option[マウントするたびにサーバーのアカウントデータベースを変更するから。]{#nfs-changes-accounts explanation="クライアントのマウントはサーバーの ID を書き換えません。"}
:::

## ネットワークマウントを自動化する

単純な `/etc/fstab` のブート時マウントは、ネットワークやサーバーが利用できないと起動を遅らせる場合があります。ホストに応じて、オンデマンドマップ用の `autofs`、または `_netdev,nofail,x-systemd.automount` などの systemd マウントオプションを使います。正確な意味は事前にテストしてください。

```fstab
server.example.net:/srv/team /mnt/team nfs4 rw,_netdev,nofail,x-systemd.automount 0 0
```

fstab の編集前に復旧アクセスを確保し、非破壊的なパーサーまたは制御されたマウントテストで検証します。automount は可用性の振る舞いを改善しますが、認可、DNS、サーバー停止は解決しません。

:::single-choice{#nfs-automount-benefit} NFS 共有をオンデマンドで automount する主な利点は何ですか？

::option[すべてのクライアントへ export の root アクセスを与える。]{#nfs-automount-root explanation="マウントのタイミングはサーバーの認可を上書きしません。"}
::option[初期ブート時にサーバーが利用可能でなくてもよくなる。]{#nfs-automount-boot .correct explanation="起動初期を必ず止めるのではなく、アクセス時に接続が開始されます。"}
::option[サーバーの全ファイルシステムをローカルディスクへコピーする。]{#nfs-automount-copy explanation="マウントはリモートアクセスを提示するもので、完全なローカルコピーではありません。"}
:::

## アンマウントと検証

アンマウント前に共有を使うプロセスを停止または調整し、アプリケーションの重要な書き込みを完了させます。その後マウントポイントをアンマウントし、なくなったことを確認します。

```bash
$ sudo umount /mnt/team
$ findmnt --target /mnt/team
```

強制または lazy unmount は、有効な参照を隠してアプリケーションエラーを引き起こす可能性があります。原因を診断済みで、明示的な復旧計画がある場合に限って使ってください。

:::single-choice{#nfs-safe-unmount} 通常の NFS アンマウント前に行うべきことはどれですか？

::option[共有を使うプロセスを調整し、重要な書き込みを終える。]{#nfs-coordinate-writers .correct explanation="利用中のファイルシステムをアプリケーションから取り除くと、I/O を中断したり作業を未完了にしたりする可能性があります。"}
::option[サーバー上の export ディレクトリを削除する。]{#nfs-delete-export explanation="クライアントのアンマウントに、サーバーデータの破壊は必要ありません。"}
::option[クライアントの全ネットワークインターフェースを無効にする。]{#nfs-disable-network explanation="正常な完了が難しくなる可能性があり、通常の手順ではありません。"}
:::

## まとめ

これで、ID と可用性の前提を明確にして NFS クライアントマウントを運用できます。

1. クライアントツール、export パス、プロトコル、ネットワークポリシーを確認する。
2. 専用パスへマウントし、有効なコピー元とオプションを検証する。
3. ID と export ポリシーから権限を診断する。
4. ブート時の可用性が重要なら、テスト済みのオンデマンドマウントを使う。
5. 利用者を調整して通常どおりアンマウントし、削除を確認する。
