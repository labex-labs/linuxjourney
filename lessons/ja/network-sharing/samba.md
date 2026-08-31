---
lesson_id: "samba"
course_id: "network-sharing"
lang: "ja"
order_index: 5
title: "Samba"
description: "基本的な Samba ファイル共有を設定、検証、利用し、安全に保護する方法を学びます。"
meta_title: "Samba - ネットワーク共有"
meta_description: "Linux での Samba ネットワーク共有の設定方法を学びます。このガイドでは、Samba プロトコル、インストール、設定、および smb クライアントを使用した共有への接続について解説します。"
meta_keywords: "Samba, smb linux, linux smb, samba ネットワーク，samba プロトコル，smb samba, ファイル共有，smb.conf, cifs, smbclient, linux チュートリアル"
---

Samba は Unix 系システムで Server Message Block（SMB）プロトコルを実装し、Linux、Windows、macOS などのクライアント間でファイルやプリンターを共有できるようにします。現代の環境では現在の SMB dialect を使います。古い用語 CIFS が Linux クライアントツールに残っていても、廃止された SMB1 を有効にすべき理由にはなりません。

## 共有を計画する

Samba をインストールまたは変更する前に、許可するクライアント、ID、読み書き要件、ネットワークゾーン、データ所有者、バックアップポリシー、必要な SMB dialect を定義します。ホームやシステムのツリーを誤って公開せず、専用ディレクトリを使ってください。

アクセスは Samba のポリシーと基盤となるファイルシステム権限の両方で制御されます。`smb.conf` で書き込みを許可しても、アカウントにないファイルシステムアクセス権は与えられません。

:::single-choice{#samba-two-permission-layers}
Samba 共有を通じた書き込みを許可する必要があるものはどれですか？

::option[共有に表示されるコメントだけ。]{#samba-comment-permission explanation="コメントは説明文であり、アクセス権を与えません。"}
::option[Samba のルールとファイルシステム権限の両方。]{#samba-policy-and-filesystem .correct explanation="要求はプロトコル層のルールとローカルファイルシステムの認可をどちらも通過する必要があります。"}
::option[クライアントのデスクトップ壁紙設定だけ。]{#samba-wallpaper explanation="クライアントの外観設定はサーバー上のファイルを制御しません。"}
:::

## 基本的な共有を定義する

主要な設定ファイルは通常 `/etc/samba/smb.conf` です。制限された設定例を示します。

```ini
[team]
    path = /srv/samba/team
    browseable = yes
    read only = no
    valid users = @teamshare
```

ディレクトリを作り、Unix グループに対して確認済みの所有権と権限を適用します。

```bash
$ sudo install -d -o root -g teamshare -m 2770 /srv/samba/team
```

set-group-ID ビットは新しいエントリにディレクトリのグループを継承させるのに役立ちますが、共同アクセスには ACL や慎重に選んだ create mask も必要な場合があります。継承だけで十分と決めつけず、実際に作られたファイルとディレクトリをテストしてください。

:::single-choice{#samba-valid-users}
`valid users = @teamshare` は何を表しますか？

::option[すべての匿名ネットワークユーザーへ書き込み権を与える。]{#samba-every-anonymous explanation="このルールはアクセスを制限するもので、ゲスト書き込みを有効にしません。"}
::option[サーバーが共有名を `teamshare` に変更しなければならない。]{#samba-rename-share explanation="表示される共有名はセクション名 `[team]` のままです。"}
::option[指定グループのメンバーだけが、この共有ルールで許可される。]{#samba-valid-group .correct explanation="Samba のユーザー一覧構文で、`@` 形式はグループを指します。"}
:::

## ID を設定する

スタンドアロンの Samba 設定では、通常アカウントに対応する Unix ID と、有効な Samba 認証情報が必要です。

```bash
$ sudo smbpasswd -a alice
```

ディレクトリドメイン環境では別の ID 設計を使います。パスワードをシェル履歴や無関係な利用者が読める設定に置かず、Samba パスワードが Unix アカウントのパスワードと自動的に同じになるとも考えないでください。

:::single-choice{#samba-password-database}
スタンドアロンサーバーで `smbpasswd -a alice` は通常何をしますか？

::option[Unix ユーザーのホームディレクトリを削除する。]{#samba-delete-home explanation="このコマンドは Samba 認証情報を管理し、ホームディレクトリを削除しません。"}
::option[そのアカウントの Samba 認証情報を追加または初期化する。]{#samba-add-credential .correct explanation="SMB 認証データベースは、Unix ユーザーを作るだけとは別に管理されます。"}
::option[Alice として表示可能な全 SMB 共有をマウントする。]{#samba-mount-all explanation="サーバーの認証情報登録とクライアントのマウントは別の操作です。"}
:::

## 設定を検証して適用する

サービスを再読み込みする前に、解析された設定を確認します。

```bash
$ testparm -s
```

予期しない既定値やエラーを確認してから、ディストリビューションのサービスマネージャーで Samba サービスを再読み込みします。サービス名は環境により異なり、一般に `smbd.service` や `smb.service` などです。対応していれば reload は restart より影響が小さいものの、状態、待ち受けソケット、ファイアウォール範囲、ログは必ず確認してください。

クライアントからユーザーを明示してテストします。

```bash
$ smbclient //server.example.net/team -U alice
```

:::single-choice{#samba-testparm-purpose}
Samba の変更適用前に `testparm -s` を実行するのはなぜですか？

::option[全共有ファイルをバックアップサーバーへコピーするため。]{#samba-testparm-backup explanation="このツールは設定を解析・報告するもので、共有データをコピーしません。"}
::option[有効な Samba 設定を検証して表示するため。]{#samba-testparm-validate .correct explanation="パーサー出力から、サービスへ影響する前に設定エラーと解釈済み設定を確認できます。"}
::option[すべてのクライアントへ管理者権限を与えるため。]{#samba-testparm-admin explanation="検証してもクライアントの認可は変更されません。"}
:::

## Linux からマウントする

Linux クライアントは通常、`cifs` ファイルシステムドライバーと mount helper を使います。コマンド引数のパスワードは履歴やプロセス調査から漏れる可能性があるため避けてください。root だけが読める認証情報ファイル、または承認済みの認証情報管理機構を使います。

```bash
$ sudo mount -t cifs //server.example.net/team /mnt/team \
    -o credentials=/root/.smb-team,vers=3.1.1
```

認証情報ファイルを保護し、両端が対応する dialect を確認し、UID、GID、権限、暗号化の要件を意図して定義します。マウント後は `findmnt` で確認し、許可された読み書きテストを行い、利用中のユーザーと調整してからアンマウントします。

:::single-choice{#samba-command-line-password}
mount コマンドへ `password=...` を直接書くべきでないのはなぜですか？

::option[履歴やプロセス引数から秘密情報が露出する可能性があるから。]{#samba-password-exposure .correct explanation="保護された認証情報源なら偶発的な漏えいを減らせますが、それ自体にも慎重な権限設定が必要です。"}
::option[SMB はどのようなパスワード認証にも対応しないから。]{#samba-no-passwords explanation="ほかの ID システムもありますが、パスワードによる SMB 認証は一般的です。"}
::option[そのオプションが共有を恒久的に読み取り専用にするから。]{#samba-password-readonly explanation="秘密情報の置き場所は書き込みポリシーを決めません。"}
:::

## まとめ

これで、プロトコルとファイルシステム双方のセキュリティを考慮して Samba 共有を設定できます。

1. クライアント、ID、ネットワーク範囲、データポリシーを先に定義する。
2. 共有を制限し、基盤となる権限と整合させる。
3. 適切な ID モデルで Samba 認証情報を管理する。
4. `testparm` で検証し、クライアントからエンドツーエンドでテストする。
5. クライアント認証情報を保護し、マウント済みアクセスを検証する。
