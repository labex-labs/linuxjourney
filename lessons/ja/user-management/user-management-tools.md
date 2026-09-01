---
lesson_id: "user-management-tools"
course_id: "user-management"
lang: "ja"
order_index: 6
title: "ユーザー管理ツール"
description: "明示的なオプションを使ってローカルアカウントを作成、変更、保護、検証、削除する方法を学びます。"
meta_title: "ユーザー管理ツール - ユーザー管理"
meta_description: "Linux のユーザー管理を、必須のコマンドラインツールで習得しましょう。このガイドでは、Linux でのアカウント管理に useradd、userdel、passwd を使用する方法を解説します。初心者にも最適です。"
meta_keywords: "linux ユーザー管理，linux アカウント管理 コマンドラインツール，useradd, userdel, passwd, linux アカウント，linux ユーザー 管理"
---

Linux ディストリビューションは一般に shadow utilities スイートのアカウントツールを提供しますが、既定値や上位レベルのラッパーは異なります。ローカルアカウントを変更する前に、中央管理のアカウントでないことを確認し、ローカルのコマンドマニュアルを読み、復旧経路を確保してください。

このレッスンのコマンドは認証と所有権の状態を変更します。本番ホストではなく、許可された破棄可能な環境だけで練習してください。

## アカウント作成の既定値を確認する

`useradd` は、コマンドオプションとサイトの既定値を使ってローカルアカウントを作成します。コンパイル時および設定済みの既定値は次のように確認します。

```bash
$ useradd -D
```

`/etc/default/useradd`、`/etc/login.defs`、スケルトンディレクトリの内容などが動作へ影響しますが、その役割はディストリビューションによって異なります。上位レベルの `adduser` コマンドが存在する場合もありますが、そのインターフェースはすべての Linux システムで標準化されていません。

## ローカルアカウントを明示的に作成する

管理された環境では、未知の既定値に依存せず、重要な属性を指定します。

```bash
$ sudo useradd -m -s /bin/bash -c "Bob Example" bob
```

- `-m` はホームディレクトリの作成を要求します。
- `-s /bin/bash` は、そのパスが許可されインストール済みだと確認したうえで、ログインシェルを選びます。
- `-c` は GECOS／コメントフィールドを指定します。

通常、新しいアカウントは利用可能なローカルパスワードを設定するまで認証できませんが、初期パスワードとロック状態の正確な動作はローカルツールとポリシーによります。仮定せず、レコードを検証してください。

```bash
$ getent passwd bob
$ sudo passwd -S bob
$ id bob
```

:::single-choice{#user-tools-create-home} 新しいアカウントのホームディレクトリ作成を明示的に要求する `useradd` オプションはどれですか？

::option[`-M`]{#user-tools-no-home-option explanation="大文字の `-M` は、一般的な `useradd` 実装にホームディレクトリを作成しないよう明示します。"}
::option[`-s`]{#user-tools-shell-option explanation="`-s` はログインシェルを選び、それ自体ではホームディレクトリを作成しません。"}
::option[`-m`]{#user-tools-home-option .correct explanation="小文字の `-m` は、ローカルの既定値に従ってホームディレクトリを作成し内容を配置するよう `useradd` へ要求します。"}
:::

## パスワードを設定・変更する

通常ユーザーは、次の対話的コマンドで自身のローカルパスワードを変更します。

```bash
$ passwd
```

認可された管理者は、別のローカルアカウントのパスワードを設定できます。

```bash
$ sudo passwd bob
```

パスワードは保護されたプロンプトだけで入力し、コマンド引数、シェル履歴、レッスンのメモ、チャットへ書いてはいけません。PAM ポリシーにより、弱いパスワードや再利用されたパスワードが拒否される場合があります。ディレクトリ管理されたアカウントには別のツールが必要なこともあります。

:::single-choice{#user-tools-change-own-password} 現在のユーザーが通常、対話的プロンプトを通じて自身のパスワードを変更するコマンドはどれですか？

::option[`useradd`]{#user-tools-add-not-password explanation="`useradd` はアカウントレコードを作成するもので、通常の対話的なパスワード変更コマンドではありません。"}
::option[`userdel`]{#user-tools-delete-not-password explanation="`userdel` はローカルアカウントを削除し、呼び出し元のパスワード変更とは無関係です。"}
::option[`passwd`]{#user-tools-passwd-self .correct explanation="ユーザー名を指定しない `passwd` は、PAM ポリシーの下で呼び出し元ユーザーのローカルパスワードを操作します。"}
:::

## アカウント属性とグループを変更する

`usermod` はローカルアカウントのフィールドを変更します。例は次のとおりです。

```bash
$ sudo usermod -s /bin/zsh bob
$ sudo usermod -d /srv/home/bob -m bob
$ sudo usermod -aG developers bob
```

ホームを移動する前に、移動先、所有権、空き容量、稼働中プロセス、マウント、サービスを確認します。補助グループでは、`-aG` は現在の一覧への追加を意味します。`-a` なしで `-G` を使うと補助グループ一覧全体を置き換え、予期せずアクセスを失う可能性があります。

グループ変更は通常、古い資格情報で実行中のプロセスではなく、新しいログインセッションへ反映されます。

:::single-choice{#user-tools-append-group} `bob` の他の補助グループ所属を置き換えず、補助グループ `developers` へ追加するコマンドはどれですか？

::option[`usermod -G developers bob`]{#user-tools-replace-groups explanation="`-a` がない `-G` は補助グループ一覧を置き換え、既存の所属を削除する場合があります。"}
::option[`usermod -aG developers bob`]{#user-tools-append-groups .correct explanation="`-a` オプションは `-G` で指定したグループを追加し、他の補助グループ所属を保持します。"}
::option[`groupdel developers bob`]{#user-tools-delete-group explanation="`groupdel` はグループ定義を削除するもので、ユーザー所属を追加しません。"}
:::

## ローカルパスワードをロックする

管理者は `passwd -l USER` でローカルパスワードハッシュをロックし、`passwd -S USER` で状態を確認できます。ロックを解除する `passwd -u USER` は、ロック理由と有効なハッシュが残っているかを確認してから使います。

パスワードロックで、SSH 鍵、トークン、スケジュール済みジョブ、実行中プロセス、サービス固有の認証が必ず停止するわけではありません。アカウントを包括的に無効化するには、脅威とアクセス経路を定義し、アカウント失効、ログインシェル、サービスアクセス、鍵、セッション終了などを組み合わせたポリシーを適用します。

:::single-choice{#user-tools-password-lock-scope} `passwd -l bob` が主にロックするものは何ですか？

::option[そのアカウントのあらゆる認証経路と実行経路。]{#user-tools-lock-everything explanation="鍵、トークン、ジョブ、サービス、既存セッションには別の制御が必要な場合があります。"}
::option[Bob の UID が現在所有するすべてのファイル。]{#user-tools-lock-files explanation="パスワード状態はファイルシステムの所有権を変更せず、所有データを自動的にアクセス不能にしません。"}
::option[パスワード認証で使われるローカルの Unix パスワードハッシュ。]{#user-tools-lock-local-password .correct explanation="このコマンドはローカルパスワードハッシュへ接頭辞を付けるなどして無効化し、その経路での通常検証を防ぎます。"}
:::

## ローカルアカウントを意図的に削除する

単なる `userdel bob` はローカルアカウントレコードを削除しますが、通常はホームディレクトリを残します。`userdel -r bob` はホームディレクトリとメールスプールの削除も試みるため、破壊的な操作です。

削除前に必ず次を行います。

1. `getent passwd bob` と `id bob` で正確なアカウントを確認する。
2. 稼働中プロセス、スケジュール済みタスク、サービス、鍵、委任済みアクセスを特定する。
3. 対象ファイルシステム全体で、その UID が所有するファイルを棚卸しする。
4. データを移管、アーカイブ、保持、安全に削除するか決める。
5. 孤立ファイルが残る間は UID を再割り当てしないことを確認する。

`userdel -r` は、設定されたホームとメールの場所の外にあるファイルまで削除するとは保証しません。アカウント削除後も、ファイルの数値所有権、データベース権限、アプリケーション識別情報、リモートディレクトリのレコードが残る場合があります。

:::single-choice{#user-tools-userdel-r-scope} 一般的な `userdel -r bob` は、単なる `userdel bob` に加えて何の削除を要求しますか？

::option[マウントされた全ファイルシステム上で Bob の UID を持つすべてのファイル。]{#user-tools-delete-all-owned explanation="このツールが、すべてのストレージから UID 所有ファイルを一律に検出して消去することはありません。"}
::option[ユーザー名が同じ `bob` であるすべてのリモートアカウント。]{#user-tools-delete-remote explanation="`userdel` は該当するローカルアカウントデータベースを操作し、無関係なディレクトリサービスの識別情報は削除しません。"}
::option[アカウントレコードに加えて、Bob のホームディレクトリとローカルメールスプール。]{#user-tools-delete-home-mail .correct explanation="再帰的なアカウント削除オプションは設定済みのホームとメールスプールを対象にしますが、Bob が別の場所で所有するすべてのオブジェクトではありません。"}
:::

隔離された環境でアカウントのライフサイクルを練習するには、次のハンズオンラボを利用できます。

1. **[useradd、usermod、userdel で Linux ユーザーアカウントを管理する](https://labex.io/labs/comptia-manage-linux-user-accounts-with-useradd-usermod-and-userdel-590837)** - 新規アカウントの作成と保護から変更、削除まで、ユーザー管理のライフサイクル全体を練習します。
2. **[groupadd、usermod、groupdel で Linux グループを管理する](https://labex.io/labs/comptia-manage-linux-groups-with-groupadd-usermod-and-groupdel-590836)** - グループの追加、変更、削除を含む、主要なコマンドラインユーティリティーを実践します。
3. **[Linux でユーザーアカウントと sudo 権限を設定する](https://labex.io/labs/comptia-configure-user-accounts-and-sudo-privileges-in-linux-590856)** - Linux システムのセキュリティを高める、ユーザーアカウントと sudo 権限の重要な管理方法を学びます。

## まとめ

明示的な範囲と検証を伴って、ローカルアカウントを管理できるようになりました。

1. 作成前に `useradd` の既定値を確認する。
2. ホーム、シェル、メタデータの設定を明示的に要求する。
3. 保護されたプロンプトだけでパスワードを変更する。
4. 既存の一覧を置き換えずに補助グループを追加する。
5. 破壊的な削除前に識別情報への依存関係を棚卸しする。
